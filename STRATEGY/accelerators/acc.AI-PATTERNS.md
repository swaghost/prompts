# Agentic AI Design Patterns Accelerator

## Purpose

This accelerator explains eight common agentic AI design patterns and shows how to enable each pattern in Claude and GitHub Copilot. Use it when designing a single assistant, a multi-step workflow, a group of specialist agents, or a quality-controlled automation system.

The patterns are architectural choices, not product features. Claude and Copilot can both implement them, but the configuration surface differs:

- **Claude**: project instructions, custom slash commands, subagents, skills, and explicit handoff prompts.
- **GitHub Copilot**: workspace instructions, prompt files, custom agents, agent delegation, tools, and task-specific workflows.

The examples below use the same request so the difference between patterns is easy to see:

> Turn a rough business idea into a validated low-ticket digital product, sales page, and seven-day launch plan.

## Pattern Selection Map

| Pattern                     | Core question                                | Best when                                                     |
| --------------------------- | -------------------------------------------- | ------------------------------------------------------------- |
| Single-Agent System         | Can one agent complete the whole task?       | The task is coherent and context switching is low             |
| Sequential Pattern          | What must happen before the next step?       | Each stage depends on the previous output                     |
| Parallel Pattern            | Which independent analyses can run at once?  | Tasks are separable and results can be combined               |
| Iterative Refinement        | How does the system improve its own output?  | Quality can be measured against explicit criteria             |
| Loop Pattern                | What repeats until an exit condition is met? | The task needs repeated attempts or checks                    |
| Co-ordinator Pattern        | Which specialist should handle each part?    | Requests vary and routing is non-trivial                      |
| Swarm Pattern               | How can many agents explore a problem?       | Breadth, diversity, or discovery matters more than one answer |
| Review and Critique Pattern | How do we catch defects before delivery?     | Accuracy, risk, quality, or compliance matters                |

## Shared Design Rules

Use these rules with every pattern:

1. Define the user's desired outcome before choosing the architecture.
2. Give every agent one clear responsibility and one clear output contract.
3. Pass structured outputs between agents instead of conversational summaries where possible.
4. Keep source evidence, assumptions, decisions, and unresolved questions separate.
5. Define an exit condition before starting a loop or iterative workflow.
6. Add a reviewer for claims, safety, quality, or irreversible actions.
7. Use parallelism only where tasks are genuinely independent.
8. Keep a human approval gate before publishing, spending money, deleting data, or contacting third parties.
9. Test the smallest workflow that can prove the architecture works.
10. Log which agent produced each decision and which evidence supported it.

## 1. Single-Agent System

### Definition

One agent receives the request, reasons through the work, uses available tools, and returns the final result. The agent may use an internal checklist, but there are no separate specialist agents or explicit handoffs.

### Flow

```text
User -> Agent -> Tools or files -> Agent -> Response
```

### Strengths

- Lowest setup and maintenance cost.
- One context window makes the conversation coherent.
- Fastest pattern for small or moderately structured tasks.
- Easy to debug because there is one decision-maker.

### Risks

- The agent may be weak at one stage of a broad task.
- Long requests can cause omissions and context drift.
- No independent reviewer catches confident mistakes.
- Tool use and final writing compete for the same attention.

### Claude Enablement

Create one project instruction or custom command that contains the role, workflow, output schema, and quality checks. A Claude command can be as simple as:

```text
You are my digital product strategist. Turn the supplied business idea into one validated low-ticket product and launch plan.

WORKFLOW:
1. Identify audience pain, buying intent, and quick win.
2. Generate three differentiated products.
3. Score urgency, value, ease, impulse-buy potential, and upsell potential from 1-10.
4. Select one winner and create the offer, funnel, and seven-day plan.
5. Check that every claim is supported or labeled as an assumption.

OUTPUT:
Audience diagnosis, three product options, scoring table, winner, offer architecture, funnel, seven-day plan, risks, and cheapest validation test.
```

Place the command in the project's Claude command directory or save it as a reusable project prompt. Invoke it with the required audience and offer context.

### Copilot Enablement

Create a workspace prompt file or custom agent with one role and one complete workflow. For this repository, a strategy agent belongs under `AGENTS/COPILOT/strategy` and should define its scope, expertise, instructions, and output format. The instruction should tell Copilot to complete all stages in one response and to avoid delegating unless the task exceeds the single-agent boundary.

### Use This Pattern When

Use it for drafting, summarizing, explaining, small audits, simple transformations, and tasks where one consistent voice matters more than independent verification.

## 2. Sequential Pattern

### Definition

Several agents or stages run in a fixed order. Each stage consumes the previous stage's output and produces the input required by the next stage.

### Flow

```text
User -> Research -> Product Design -> Offer Design -> Funnel -> Review -> User
```

### Example Stages

1. **Research**: identify recurring pain and buyer intent.
2. **Product designer**: turn the pain into three product concepts.
3. **Offer architect**: define price, deliverables, lead magnet, order bump, and upsell.
4. **Funnel writer**: map the path from content to purchase.
5. **Reviewer**: check evidence, promise credibility, and missing outputs.

### Strengths

- Makes dependencies explicit.
- Each stage can be specialized and tested independently.
- Easier to inspect where an error entered the workflow.
- Useful for repeatable production pipelines.

### Risks

- A bad early output contaminates every later stage.
- Sequential execution is slower than necessary when stages are independent.
- Handoff formats must be precise.
- More agents create more configuration and maintenance.

### Handoff Contract

Use a small structured handoff:

```text
STAGE: Research
STATUS: complete | needs_input | blocked
EVIDENCE: [observations or sources]
ASSUMPTIONS: [unverified beliefs]
RECOMMENDATION: [one sentence]
INPUT_FOR_NEXT_STAGE: [structured facts and constraints]
OPEN_QUESTIONS: [questions that could change the decision]
```

### Claude Enablement

Create one command per stage, then create an orchestration command that invokes them in order. Each command should say exactly what it accepts and returns. The orchestrator should not silently skip a failed stage:

```text
Run this workflow in order: /RESEARCH_PRODUCT, /DESIGN_PRODUCT, /ARCHITECT_OFFER, /BUILD_FUNNEL, /REVIEW_OUTPUT.

After each stage:
- verify STATUS is complete;
- preserve EVIDENCE, ASSUMPTIONS, and OPEN_QUESTIONS;
- pass only INPUT_FOR_NEXT_STAGE to the next command;
- stop and report the blocker if STATUS is blocked.
```

Claude can also implement the stages as subagents or skills when each stage has substantial domain instructions. Keep the orchestration command short and keep stage expertise in the stage files.

### Copilot Enablement

Create one custom agent or prompt file for each specialist and one coordinator instruction that delegates in order. The coordinator should specify the handoff schema and tell Copilot when to wait for the previous result. Use task dependencies rather than asking all agents to work from an incomplete initial request.

### Use This Pattern When

Use it for research-to-writing pipelines, content production, product development, code generation followed by tests, and any workflow where later decisions depend on earlier artifacts.

## 3. Parallel Pattern

### Definition

Independent agents work on separate parts of a request at the same time. A synthesis stage combines their outputs after all required branches finish.

### Flow

```text
                    -> Market Research --\
User -> Dispatcher -- > Buyer Psychology --- > Synthesizer -> Reviewer -> User
                    -> Competitor Scan --/
```

### Good Parallel Branches

- Research audience pain, competitor offers, and pricing separately.
- Ask three copywriters for independent headline sets.
- Analyze separate files or modules that do not share mutable state.
- Run tests for independent components.

### Bad Parallel Branches

- Two agents editing the same file simultaneously.
- Research tasks that depend on one another's findings.
- Agents using different definitions of the same key term.
- Parallel actions with irreversible side effects.

### Strengths

- Reduces wall-clock time.
- Produces multiple perspectives.
- Limits one specialist's blind spots.
- Works well for exploration and comparison.

### Risks

- Duplicate or contradictory work.
- Synthesis becomes the new bottleneck.
- More token and tool usage.
- Race conditions when branches modify shared files or state.

### Claude Enablement

Ask Claude to split the work into independent branches and label each branch. When using subagents, define a separate output file or return object for each branch. A coordinator prompt should state:

```text
Decompose the request into independent branches. Run these branches in parallel only if none requires another branch's output. Each branch must return:

BRANCH:
FINDINGS:
EVIDENCE:
CONFIDENCE:
CONFLICTS:
RECOMMENDATION:

After all branches finish, synthesize them. Do not average contradictory claims; explain the conflict and choose based on evidence.
```

Use Claude subagents for isolated research or analysis. Keep the parent command responsible for synthesis and final formatting.

### Copilot Enablement

Use agent delegation or separate custom agents for each independent branch. Give each agent a distinct task and tell it not to edit shared files unless explicitly assigned. The parent Copilot agent should collect branch outputs, resolve conflicts, and perform the final write. In a codebase, parallelize read-only investigation first, then serialize edits.

### Use This Pattern When

Use it for competitive analysis, multi-file review, option generation, independent tests, research triangulation, and any workload where branches do not need intermediate results.

## 4. Iterative Refinement Pattern

### Definition

An agent generates an output, a quality evaluator scores it, and an improver revises it using the feedback. The cycle ends when the quality threshold is met or the revision budget is exhausted.

### Flow

```text
User -> Generator -> Evaluator -> Prompt or Draft Enhancer -> Generator
                         |                         |
                         +---- threshold met ------> User
```

### Example Quality Criteria

For a sales page, score:

- Promise clarity.
- Audience relevance.
- Specificity of outcome.
- Evidence and credibility.
- Objection handling.
- Call-to-action clarity.
- Reading ease.

### Strengths

- Makes quality explicit instead of relying on vague confidence.
- Good for writing, code, designs, and plans.
- Feedback can target one defect at a time.
- Produces measurable improvement.

### Risks

- The evaluator may reward its own preferences.
- Revisions can overfit to the score and damage the original goal.
- Endless refinement without a stopping rule.
- A weak rubric creates false confidence.

### Claude Enablement

Create three reusable commands or skills: `/GENERATE`, `/EVALUATE`, and `/IMPROVE`. The evaluator must not rewrite the draft; it should return a score, defects, and prioritized changes. The orchestrator can use this instruction:

```text
Generate a draft. Evaluate it against the rubric below. If the total score is at least 42/50 and no critical defect exists, return the draft. Otherwise revise only the three highest-impact defects and evaluate again.

Maximum iterations: 3.
Critical defects: unsupported claims, missing required sections, unsafe action, broken links, or a promise that the deliverable cannot support.
```

Keep the draft and evaluation separate so the improver cannot erase useful criticism.

### Copilot Enablement

Define a generator custom agent and a reviewer custom agent, or use a prompt file that explicitly separates generation, evaluation, and revision phases. Copilot's reviewer should return machine-readable findings or a checklist. Use `start` or delegation only when the revision task is independent; otherwise keep the loop in one parent agent so the latest draft remains available.

### Use This Pattern When

Use it for copy editing, code quality, prompt improvement, design critique, test repair, and any output with a stable scoring rubric.

## 5. Loop Pattern

### Definition

An agent repeatedly performs a task until an exit condition is satisfied. Unlike refinement, a loop may repeat discovery, testing, execution, or monitoring rather than rewriting one artifact.

### Flow

```text
Start -> Task A -> Task B -> Task C -> Exit check
             ^                         |
             +------ not satisfied ----+
```

### Examples

- Generate product ideas until one passes the demand threshold.
- Run tests, repair failures, and rerun until the test suite passes or the budget ends.
- Search for evidence until the minimum source-quality requirement is met.
- Process records until the queue is empty.

### Exit Conditions

Always define at least one success and one failure exit:

```text
SUCCESS: score >= 8/10 and no critical defect.
FAILURE: 3 attempts, 20 minutes, or $5 tool budget reached.
BLOCKED: required input, permission, or source is unavailable.
```

### Strengths

- Handles uncertain tasks and gradual convergence.
- Makes repeated work systematic.
- Useful for testing and operational queues.
- Can stop early when the goal is reached.

### Risks

- Infinite loops and runaway cost.
- Repeating the same failed action without changing strategy.
- Stale state between iterations.
- The exit condition may be technically satisfied but strategically wrong.

### Claude Enablement

Put the loop controller in a command or project instruction. Require an iteration log:

```text
ITERATION: [number]
ACTION: [what was attempted]
RESULT: [what happened]
CHANGE_FOR_NEXT_ITERATION: [what will differ]
SCORE: [numeric score]
EXIT_STATUS: continue | success | failure | blocked
```

Tell Claude to change one meaningful variable after a failed iteration and to stop when the budget or attempt limit is reached. For tool-heavy loops, require confirmation before external side effects.

### Copilot Enablement

Use a custom agent with explicit loop state, or a task workflow that reruns a command after inspecting the result. Store the iteration log in the response or a workspace file. State the maximum number of attempts and tell Copilot what constitutes a real strategy change rather than a cosmetic retry.

### Use This Pattern When

Use it for test-repair workflows, validation, batch processing, evidence gathering, monitoring, and search problems with measurable completion conditions.

## 6. Co-ordinator Pattern

### Definition

A coordinator agent interprets the request, chooses the appropriate specialist or sequence, manages context, and synthesizes the result. Specialists do not decide the overall workflow.

### Flow

```text
User -> Coordinator -> Specialist A
                   -> Specialist B
                   -> Specialist C
                   -> Final synthesis
```

### Routing Table Example

| Request signal              | Specialist               |
| --------------------------- | ------------------------ |
| Learn or explain a topic    | Primer or teaching agent |
| Compare options             | Comparison agent         |
| Audit a business or offer   | Audit agent              |
| Build repeatable operations | Systems agent            |
| Write conversion copy       | Copy or CTA agent        |
| Create a launch plan        | Go-to-market agent       |

### Strengths

- One entry point for many capabilities.
- Specialists stay narrow and maintainable.
- Routing can select sequential, parallel, or review flows.
- The user does not need to know internal agent names.

### Risks

- Misrouting at the front door.
- Coordinator becomes a bottleneck or overrules specialists without evidence.
- Hidden delegation makes debugging difficult.
- Too many specialists create a taxonomy nobody maintains.

### Claude Enablement

Create a coordinator command such as `/ROUTE` and a small registry describing each command or skill. The coordinator should classify before acting:

```text
Classify the request by primary goal, required expertise, dependency structure, risk level, and expected output.

Return:
ROUTE: [command or specialist]
PATTERN: single | sequential | parallel | refinement | loop | review
RATIONALE: [brief reason]
REQUIRED_INPUTS: [missing inputs]
APPROVAL_REQUIRED: yes | no

If required inputs are missing, ask only for those inputs. Do not route to multiple specialists unless the request genuinely has multiple independent goals.
```

The current Claude command catalog can serve as a lightweight registry. Keep command names stable and make their descriptions mutually distinct.

### Copilot Enablement

Create a coordinator custom agent with routing rules and a registry of specialist agents in `AGENTS/COPILOT`. Use `applyTo` patterns carefully so a specialist is activated for the right file or request context. The coordinator should delegate, collect results, and own the final response. Add a fallback route for requests that do not match any specialist.

### Use This Pattern When

Use it for a broad assistant, a strategy workspace with many commands, a support desk, a codebase with domain specialists, or any system that must choose the workflow dynamically.

## 7. Swarm Pattern

### Definition

Many agents explore the same broad problem from different angles. Agents can hand off partial findings, discover new subproblems, or converge on a shared answer through a dispatcher.

### Flow

```text
User -> Dispatcher -> Agent 1 -> handoff -> Agent 2
                  -> Agent 3 -> handoff -> Agent 4
                  -> Agent 5 -> shared findings
                         |
                         +----------> Synthesizer
```

### Example Swarm Roles

- Audience researcher.
- Buyer-psychology analyst.
- Competitor analyst.
- Pricing analyst.
- Skeptical validator.
- Simplicity and implementation analyst.
- Synthesizer.

### Strengths

- Broad exploration and diverse hypotheses.
- Useful when the solution space is poorly understood.
- Agents can discover new questions and routes.
- Reduces dependence on one framing of the problem.

### Risks

- High cost and coordination overhead.
- Duplicate work and noisy findings.
- Emergent handoffs can lose the original objective.
- Consensus can amplify a shared mistake.

### Claude Enablement

Use Claude subagents for bounded investigations and require a dispatcher prompt to enforce a shared mission, role limits, and a handoff schema. Do not let every agent edit the same artifact. A swarm handoff should include:

```text
MISSION: [unchanged top-level goal]
ROLE: [this agent's narrow responsibility]
NEW_FINDING: [what was learned]
SUPPORT: [evidence or reasoning]
UNTESTED_HYPOTHESIS: [what remains uncertain]
NEXT_BEST_AGENT: [role, not a person]
```

Set a maximum agent count, handoff count, and time or token budget. End with a synthesizer that actively looks for disagreement instead of counting repeated claims.

### Copilot Enablement

Use multiple custom agents with narrow expertise and a dispatcher agent that assigns work. Copilot can delegate to specialists, but the parent agent must retain the mission and consolidate outputs. Use separate workspace artifacts for findings, and add a final critic to detect groupthink, unsupported consensus, and duplicated evidence.

### Use This Pattern When

Use it for open-ended research, ideation, incident investigation, complex product discovery, and problems where multiple independent perspectives create meaningful value.

## 8. Review and Critique Pattern

### Definition

A generator creates the proposed output and a separate critic evaluates it against requirements, risks, evidence, and likely failure modes. The critic may approve, request changes, or block delivery.

### Flow

```text
User -> Generator -> Critic -> Approve
                         |
                         +-> Request changes -> Generator
                         +-> Block -> Human decision
```

### Review Dimensions

- Requirement coverage.
- Factual accuracy and source quality.
- Internal consistency.
- Security, privacy, and safety risks.
- User impact and accessibility.
- Operational feasibility.
- Formatting and delivery correctness.

### Strengths

- Separates creation from judgment.
- Makes quality and risk visible.
- Suitable for high-impact or public outputs.
- Can provide an approval gate without rewriting everything.

### Risks

- A critic may be too lenient or too strict.
- Review can become ceremonial if it never blocks.
- Critic and generator may share the same blind spot.
- Extra latency and cost.

### Claude Enablement

Create a critic command or skill that receives the draft and the acceptance criteria. It should return findings first, not a polished replacement:

```text
Review the draft against the acceptance criteria.

Return:
DECISION: approve | revise | block
CRITICAL_FINDINGS: [issues that prevent delivery]
NONCRITICAL_FINDINGS: [improvements]
MISSING_REQUIREMENTS: [omissions]
EVIDENCE_GAPS: [unsupported claims]
RISK_LEVEL: low | medium | high
REQUIRED_CHANGES: [ordered list]
```

Use a second review pass for high-risk outputs, ideally with a different role or rubric. Require human approval for irreversible actions or claims that materially affect people.

### Copilot Enablement

Create a reviewer custom agent or prompt file that runs after generation. In coding tasks, pair implementation with a test/review agent; in documentation or strategy tasks, pair drafting with a requirements and evidence reviewer. Configure the parent agent to act on `revise` findings and stop on `block` rather than presenting an unreviewed answer.

### Use This Pattern When

Use it for production code, public copy, legal or financial claims, security-sensitive changes, customer-facing plans, and any deliverable where a plausible-looking mistake is costly.

## Pattern Compositions

Real systems commonly combine patterns. Use the simplest composition that covers the risk:

### Sequential Plus Review

```text
Research -> Draft -> Review -> Publish
```

Use for content, reports, and customer-facing documents.

### Parallel Plus Synthesis Plus Review

```text
Independent analyses -> Synthesis -> Critique -> Final
```

Use for strategy, comparison, and research-heavy decisions.

### Coordinator Plus Sequential Specialists

```text
Coordinator -> selected workflow -> Review -> User
```

Use for a broad command library or multi-domain assistant.

### Loop Plus Review

```text
Generate -> Test -> Review -> Repair -> repeat until exit condition
```

Use for code repair, validation, and measurable optimization.

### Swarm Plus Coordinator

```text
Coordinator -> bounded swarm -> Synthesis -> Critique
```

Use for difficult discovery problems, but impose strict budgets.

## Claude Implementation Checklist

- [ ] Project instructions define the shared mission and constraints.
- [ ] Commands or skills have stable names and narrow responsibilities.
- [ ] Subagents are used only for bounded specialist work.
- [ ] Handoffs preserve evidence, assumptions, status, and open questions.
- [ ] Parallel branches do not edit the same mutable artifact.
- [ ] Loops have success, failure, blocked, and budget exits.
- [ ] A coordinator owns routing and final synthesis.
- [ ] A critic can return `revise` or `block`.
- [ ] Human approval is required for irreversible external actions.
- [ ] The workflow is tested with a small representative request.

## Copilot Implementation Checklist

- [ ] Workspace instructions define the shared mission and boundaries.
- [ ] Custom agents have narrow descriptions and targeted activation patterns.
- [ ] Prompt files define repeatable task workflows and output contracts.
- [ ] Delegated agents receive complete context and return structured results.
- [ ] Parallel agents have isolated write scope.
- [ ] Loops have explicit attempt, time, and cost limits.
- [ ] A coordinator handles routing and final synthesis.
- [ ] A reviewer checks requirements, evidence, quality, and risk.
- [ ] Blocked or high-risk outcomes stop for human review.
- [ ] The workflow is tested against both normal and adversarial inputs.

## Quick Enablement Procedure

1. Start with the single-agent version.
2. Identify the first repeated failure or bottleneck.
3. Extract only that responsibility into a specialist.
4. Add a structured handoff contract.
5. Parallelize only independent branches.
6. Add a reviewer before adding more agents.
7. Add loops only with explicit exit conditions.
8. Add a coordinator when users need multiple workflows.
9. Add a swarm only when diversity materially improves discovery.
10. Measure quality, latency, cost, omissions, and human corrections after each change.

## Final Decision Rule

Choose the smallest architecture that reliably meets the quality bar. More agents do not automatically create a better system. A clear single agent with a strong rubric often beats a poorly coordinated swarm, while a small sequential pipeline with an independent reviewer is usually the right next step when one agent starts dropping requirements.
