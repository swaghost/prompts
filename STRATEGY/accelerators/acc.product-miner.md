# Product Miner Accelerator Prompts

## Purpose

Use these eight prompts to generate, challenge, combine, invert, clarify, connect, and filter product ideas. They work especially well for digital products, content offers, services, educational products, and new business concepts.

## Recommended Flow

```text
Expand -> Challenge -> Question -> Explore -> Connect -> Combine -> Invert -> Filter
```

Run the prompts separately when you need one specific thinking mode. Run them in sequence when you want broad exploration followed by structured selection. Keep the original idea list and the reasons for rejecting ideas so the final choice remains auditable.

## 1. Expand

### Purpose

Generate a wide range of directions before evaluating them. This prevents premature judgment from narrowing the opportunity space too early.

### Prompt

```
I have this rough idea: [IDEA]. Give me 15 different directions I could take it.

Include practical, unexpected, controversial, emotional, educational, and highly relatable angles. For each direction, briefly explain the target audience, the core problem or desire, and what would make the angle meaningfully different from the others.
```

### Output Rules

- Produce 15 genuinely distinct directions, not minor wording changes.
- Include a mix of safe, unconventional, and high-upside options.
- Do not rank or eliminate ideas until all 15 are visible.

## 2. Challenge

### Purpose

Stress-test an idea before investing time, money, or reputation in it.

### Prompt

```
Here is my idea: [IDEA]. Do not agree with me automatically.

Find its weaknesses, hidden assumptions, and possible problems. Then suggest 5 stronger versions of the idea.

For each weakness, explain the likely consequence, what evidence would confirm or disprove it, and how the idea could be repaired without losing its core appeal.
```

### Output Rules

- Identify demand, audience, distribution, execution, pricing, and differentiation risks where relevant.
- Separate facts from assumptions and questions that still need testing.
- Do not criticize without proposing a stronger alternative.

## 3. Combine

### Purpose

Create fresh concepts by combining compatible ideas without producing incoherent feature piles.

### Prompt

```
Combine these ideas into new concepts: [IDEAS]. Give me 10 combinations that make logical sense but feel fresh and different.

For each combination, explain the shared audience, the problem solved, why the elements belong together, the simplest viable product format, and the main risk of combining them.
```

### Output Rules

- Make the relationship between the combined ideas explicit.
- Reject combinations that are merely bundles without a shared customer problem.
- Keep each concept narrow enough to test.

## 4. Invert

### Purpose

Use inversion to reveal overlooked alternatives, failure modes, and contrarian opportunities.

### Prompt

```
Take this idea: [IDEA]. Now brainstorm what the complete opposite appropriate approach would look like.

Give me 10 useful ideas from that perspective. For each, explain what assumption it reverses, who might benefit, what problem it solves, and whether the inversion is practical, experimental, or deliberately provocative.
```

### Output Rules

- Identify the assumption being inverted rather than treating the opposite as automatically correct.
- Include practical alternatives, not only rhetorical opposites.
- Flag ideas that require evidence because they challenge established constraints.

## 5. Question

### Purpose

Discover demand, objections, confusion, and content opportunities through the questions a target audience already carries.

### Prompt

```
For [TOPIC], list 20 questions my target audience might genuinely ask, worry about, misunderstand, or be curious about.

Prioritize questions that could lead to useful content, a product, a service, a diagnostic, or a meaningful buying decision. Group them by awareness, problem, solution, implementation, risk, and outcome where appropriate.
```

### Output Rules

- Write questions in the audience's natural language.
- Avoid generic questions that could apply to every topic.
- Mark which questions show urgent pain, active buying intent, or only casual curiosity.

## 6. Explore

### Purpose

Use guided clarification when the creator is stuck, instead of generating generic ideas from insufficient context.

### Prompt

```
I want to create something around [TOPIC], but I am stuck. Ask me 7 questions that will help uncover better ideas before you suggest anything.

Ask about my experience, repeated tasks, unusual insights, audience, constraints, existing assets, problems I can solve, and results I have created. Ask one question at a time and wait for my answer before continuing.
```

### Output Rules

- Do not suggest products until all seven questions have been answered.
- Use follow-up questions when an answer is vague or reveals a promising thread.
- After the questions, summarize the strongest raw materials for an idea before proposing concepts.

## 7. Connect

### Purpose

Find useful intersections between two domains, audiences, skills, or bodies of knowledge.

### Prompt

```
Find unexpected connections between [TOPIC A] and [TOPIC B]. Give me 10 ideas that could come from combining them.

For each idea, explain the connection, the specific audience, the problem or opportunity created by the intersection, the possible product or content format, and why the connection is more than a superficial theme match.
```

### Output Rules

- Explain the mechanism connecting the two topics.
- Prefer intersections that create a distinct advantage, audience, workflow, or outcome.
- Identify whether each idea is a product, service, content series, research angle, or experiment.

## 8. Filter

### Purpose

Reduce a large idea list into a focused shortlist without losing the reasoning behind the selection.

### Prompt

```
Here are my ideas: [PASTE IDEAS].

Group similar ideas, remove weak or repetitive ideas, and rank the remaining ideas by:

- Usefulness
- Originality
- Potential audience interest
- Evidence of demand
- Ease of execution
- Fit with my skills and resources

Show which ideas were merged or removed and explain why. Then recommend the top 3 ideas, identify the single best one to test first, and give me the cheapest validation test for it.
```

### Output Rules

- Do not remove an idea without recording the reason.
- Score each criterion from 1-10 and show assumptions behind the scores.
- Distinguish audience interest from willingness to pay.
- Recommend a test before recommending full production.

## Combined Product-Mining Workflow

### Stage 1: Generate Raw Material

Use `/EXPAND` or Prompt 1 to create a broad set of directions. Use `/QUESTION` and `/EXPLORE` to uncover real audience problems and the creator's existing advantages.

### Stage 2: Create Differentiation

Use `/CONNECT`, `/COMBINE`, and `/INVERT` to develop non-obvious angles. Keep the underlying customer problem visible so novelty does not become the only selling point.

### Stage 3: Stress-Test

Use `/CHALLENGE` to identify assumptions, weaknesses, and likely failure modes. Ask what evidence would change the ranking.

### Stage 4: Select and Validate

Use `/FILTER` to shortlist ideas, choose one test, define a pass/fail signal, and validate demand before building the complete product.

## Quality Guardrails

- Do not confuse a large idea list with progress; selection and validation are required.
- Do not treat originality as proof of demand.
- Do not use controversy merely for attention if it damages trust or misleads the audience.
- Label speculative ideas, inferred demand, and observed evidence separately.
- Keep validation ethical, legal, low-cost, and reversible.
- Preserve useful rejected ideas in a backlog instead of deleting them permanently.
