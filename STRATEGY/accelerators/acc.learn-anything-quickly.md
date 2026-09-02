# Learn Anything Quickly Prompts

## Purpose

Six focused prompts for learning a skill quickly through prioritization, deliberate practice, retrieval, diagnosis, and explanation. Use them independently or run them as a progression from orientation to demonstrated competence.

## Recommended Learning Sequence

```text
Learning Curve Destroyer -> Personal Learning Path Architect -> Impossible Language Translator -> Real Error Simulator -> Hidden Gap Detector -> Forced Feynman Method
```

The sequence is not a substitute for practice or expert instruction. It is a way to make limited study time concrete, expose weak understanding, and turn passive reading into observable performance.

## 1. The Learning Curve Destroyer

### Use When

You have a short, fixed amount of time and need functional competence rather than comprehensive theory.

### Prompt

```
You are a teacher who only has 4 hours with me and will never see me again. Your only objective is to make me functional in [SKILL] before the time runs out.

Do not give me theory without practical use. Do not give me a list.

Tell me:

- What to learn first
- What to completely ignore for now
- What exercise, if I do it once, will give me an unusually strong practical advantage over typical beginners
- What a functional result looks like
- What mistakes would waste the limited time

Build a four-hour sequence with time blocks, one practical task per block, a clear success test, and the minimum theory required to complete each task. State what the sequence cannot teach me within four hours.
```

### Output Contract

- Define functional competence in observable terms.
- Prioritize the smallest high-leverage skill set.
- Explain why each excluded topic can wait.
- Use exercises, feedback, and a final performance test.
- Do not claim a guaranteed percentile advantage; label any comparison as an estimate.

## 2. The Real Error Simulator

### Use When

You understand a concept superficially but need to discover whether you can apply it under realistic pressure.

### Prompt

```
Do not explain [CONCEPT] to me.

Put me directly into a realistic situation where I would have to use it and would probably make a mistake.

When I make a mistake, do not give me the answer. Ask me a question that forces me to discover where my reasoning is broken.

Only give me the answer after I have tried at least two times. Repeat this cycle until I can get it right without hesitation.

After each attempt, track:

- My decision or answer
- The hidden assumption behind it
- The exact reasoning failure
- One question that would help me self-correct
- Whether the failure is conceptual, procedural, perceptual, or execution-related
```

### Output Contract

- Start with a realistic scenario and do not front-load an explanation.
- Give one decision point at a time.
- Require at least two attempts before revealing the answer unless safety requires immediate correction.
- Increase difficulty only after the learner demonstrates the current step.
- End with a similar but novel scenario to test transfer.

## 3. The Impossible Language Translator

### Use When

Technical material feels confusing and you need the central idea before the supporting details.

### Prompt

```
This content below is confusing to me.

Before explaining it, tell me: what is the one sentence that, if I understand it, will make the rest make sense on its own?

Explain only that sentence first.

Use an everyday analogy, with no technical terms. Then ask me 3 questions that only someone who truly understood it would be able to answer.

Do not continue until I pass all three.

[PASTE THE CONTENT HERE]
```

### Output Contract

- Identify one central sentence, not a summary of every paragraph.
- Explain the analogy and state where it stops being accurate.
- Ask three transfer or application questions, not simple definition questions.
- Wait for the learner's answers before continuing.
- Correct misconceptions directly and preserve necessary nuance.

## 4. The Personal Learning Path Architect

### Use When

You have a specific outcome and deadline, but generic learning plans keep producing irrelevant study.

### Prompt

```
My real goal is [GOAL].

It is not to learn [SKILL] in general. It is to achieve [SPECIFIC RESULT] within [DEADLINE].

I already know [WHAT I ALREADY MASTER].

Based on that, build me a 7-day learning path.

Each day must include:

- One single task that fits within 45 minutes
- A clear criterion so I know whether I did it correctly
- What not to do that day so I do not waste time
- One artifact or evidence of progress

If the entire path does not lead me to the goal, rebuild it until it does. State which prerequisite is missing if the goal cannot be reached within the deadline.
```

### Output Contract

- Work backward from the target result, not forward from a generic curriculum.
- Keep each day's main task within 45 minutes.
- Include a pass/fail or observable quality criterion.
- Remove tasks that do not contribute to the deadline outcome.
- Include a final demonstration that matches the actual goal.

## 5. The Hidden Gap Detector

### Use When

You believe you understand a skill and want a direct diagnostic of the gaps beneath that confidence.

### Prompt

```
I think I already master [SKILL].

I want you to prove me wrong.

Ask me 5 questions that seem simple but expose the gaps of someone who has never truly gone deep.

For every answer I give, tell me:

- What my answer reveals about what I understand
- What is still missing in my foundation
- What assumption or edge case I overlooked
- What I should practice next

Do not go easy on me.

If I am being shallow, tell me directly. Do not confuse confidence, vocabulary, or familiarity with mastery.
```

### Output Contract

- Ask questions that test mechanisms, trade-offs, edge cases, and application.
- Do not reveal the ideal answers before the learner responds.
- Distinguish factual gaps from imprecise language and reasoning gaps.
- Rate confidence only against demonstrated evidence.
- End with a prioritized remediation plan.

## 6. The Forced Feynman Method

### Use When

You have just studied a topic and want to test whether you can explain it clearly without hiding behind jargon.

### Prompt

```
I just studied [TOPIC].

I am going to explain what I understood as if you were a 10-year-old child.

While I explain, stop me every time I:

- Use jargon without knowing what it means
- Skip a step in the reasoning
- Make an unsupported leap
- Use an analogy that breaks
- Simplify so much that it becomes wrong

At the end, tell me exactly what those mistakes reveal about what is still not solid in my mind.

Do not rewrite my explanation for me until you have identified the specific weakness.
```

### Output Contract

- Interrupt only for a meaningful jargon, logic, analogy, or accuracy problem.
- Ask the learner to repair the explanation before supplying a replacement.
- Identify the missing link rather than merely correcting wording.
- Preserve necessary complexity where simplification would become false.
- End with a short re-explanation request that tests whether the weakness was repaired.

## Shared Rules for All Six Prompts

- Prefer retrieval, decisions, explanations, and artifacts over passive summaries.
- Ask clarifying questions when the skill, goal, level, or deadline is underspecified.
- Separate knowing a definition from performing the skill.
- Give corrective feedback that is specific, actionable, and proportionate.
- Do not shame the learner for mistakes; use mistakes as diagnostic evidence.
- Label uncertainty, estimates, and domain-specific exceptions.
- Add immediate safety or accuracy corrections when delayed feedback could cause harm.
- Keep the task narrow enough that progress can be observed.

## Quick Selection Guide

| Need                                           | Use                              |
| ---------------------------------------------- | -------------------------------- |
| Four hours to become functional                | Learning Curve Destroyer         |
| Practice under likely failure                  | Real Error Simulator             |
| Understand confusing material                  | Impossible Language Translator   |
| Reach a specific result by a deadline          | Personal Learning Path Architect |
| Test whether confidence is justified           | Hidden Gap Detector              |
| Check whether you can explain what you studied | Forced Feynman Method            |
