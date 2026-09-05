# Palette Role and Psychology Decoder

## Description

Analyze an existing palette as a system of hierarchy, emotional signals, saturation, temperature, context, and role conflicts. This tool explains why a palette works or fails before recommending controlled corrections.

## Best For

- Reviewing extracted palettes
- Diagnosing flat or noisy designs
- Brand and campaign color strategy
- UI semantic-color planning
- Mood and narrative analysis

## Inputs

- Four to six HEX, RGB, or sampled colors
- Intended audience, medium, and emotional outcome
- Optional screenshot or reference image showing the palette in use

## Tool Prompt

```text
Analyze the supplied palette in the context of [MEDIUM], [AUDIENCE], and [INTENDED EMOTION]. Treat color meaning as contextual rather than universal.

ROLE ANALYSIS
Assign or evaluate these roles:
- BASE - approximately 60%
- STRUCTURE - approximately 30%
- SIGNATURE - approximately 7%
- ACCENT - approximately 3%

Identify role collisions, missing roles, colors used at equal volume, and accents that have expanded into competing bases.

PSYCHOLOGY ANALYSIS
For each color report:
- Hue family and nearest descriptive name
- Value and saturation level
- Relative temperature within this palette
- Likely emotional and behavioral signals in this context
- Cultural or category-dependent ambiguity
- Where the color supports the brief
- Where the same color could break the brief

Use these starting signals only when context supports them:
- Red: urgency, appetite, danger, desire; visually fatiguing at scale
- Orange: warmth, memory, decay, nostalgia; weak for clinical or premium-cold briefs
- Yellow or gold: optimism, attention, value; must be rationed and should not carry body text on white
- Green: nature and growth at one extreme, systems or sickness when cool and desaturated
- Blue: distance, truth, cold, competence; credible but forgettable without another idea
- Purple or violet: fantasy, imagination, dusk, transition, constructed worlds
- Pink: play, softness, confident artifice; not a substitute for layout hierarchy
- Near-black: weight, luxury, absence; use a hue-biased black rather than pure #000 where appropriate
- Cream or off-white: craft, patience, editorial calm, reduced glare; unsuitable when maximum contrast is required

OVERRIDING RULES
1. Saturation may change meaning more strongly than hue. Compare muted and saturated interpretations explicitly.
2. Temperature is relative. Identify which color makes another appear warm or cool.

TWO-AXIS MAP
Place the palette on two scales:
- Saturation: considered / historic / premium <-> urgent / young / loud
- Temperature: distant / precise / institutional <-> intimate / memorable / appetizing

OUTPUT
Return:
1. Role table with current and recommended ratios
2. Psychology table for every color
3. Saturation and temperature assessment
4. Three strengths
5. Three risks
6. A corrected four-color palette only if necessary, with every change documented
7. A one-sentence rule for protecting the signature and accent colors

Do not rely on hue stereotypes without considering saturation, value, neighboring colors, medium, audience, and semantic use.
```

## Quality Checklist

- [ ] Every color has one clear role or is flagged as redundant.
- [ ] Psychology is explained in context rather than as a universal rule.
- [ ] Saturation and relative temperature are analyzed explicitly.
- [ ] Near-black, off-white, and gray biases are identified.
- [ ] Role collisions and overused accents are reported.
- [ ] Any recommended color change includes a reason and before/after values.

## Source

Adapted from **The Cinema Colour Vault** by [@itsdesignare](https://www.instagram.com/itsdesignare/).
