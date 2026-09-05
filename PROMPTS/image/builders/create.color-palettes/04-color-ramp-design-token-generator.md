# Color Ramp and Design Token Generator

## Description

Turn a four-color palette into a deployable system of tints, shades, semantic tokens, interaction states, borders, dividers, surfaces, and text colors while preserving the original hierarchy.

## Best For

- Design systems
- Websites and applications
- Brand guidelines
- Campaign templates
- Presentation and editorial systems

## Inputs

- Four core colors assigned to Base, Structure, Signature, and Accent
- Target medium and color-space requirements
- Optional light, dark, or dual-theme requirement

## Tool Prompt

```text
Convert the supplied four-color palette into a production-ready token system for [MEDIUM]. The input colors already have these roles: BASE 60%, STRUCTURE 30%, SIGNATURE 7%, and ACCENT 3%. Preserve that hierarchy throughout the expanded system.

CORE RAMP REQUIREMENT
For each of the four colors, create:
- 3 tints lighter than the core
- The original core color
- 3 shades darker than the core

Return seven ordered values per role. Build perceptually even steps rather than mechanically mixing arbitrary percentages. Preserve hue identity while controlling saturation so pale tints do not become fluorescent and dark shades do not collapse into indistinguishable black.

NEUTRAL BIAS
Create hue-biased near-black, off-white, and gray values derived from the dominant palette. Avoid pure #000000 and #FFFFFF unless maximum-contrast output explicitly requires them.

SEMANTIC TOKENS
Map the ramps to:
- canvas and primary surface
- elevated and recessed surface
- primary and secondary text
- muted text
- borders and dividers
- signature brand element
- primary action
- hover, active, focus, selected, and disabled states
- informational, success, warning, and error states where required

Keep the accent scarce. Do not assign the accent to multiple large surfaces or routine decoration. Distinguish status states with icon, label, shape, or pattern as well as color.

OUTPUT
Return:
1. Four seven-step ramps with HEX, RGB, HSL, and optional OKLCH
2. Hue-biased neutral ramp
3. Semantic token table
4. CSS custom properties using clear role-based names
5. Light-theme mapping
6. Dark-theme mapping when requested
7. Usage examples and forbidden combinations
8. Contrast warnings requiring review

Do not flatten the system into equal-use swatches. The 60 / 30 / 7 / 3 hierarchy remains the governing rule even after expansion.
```

## Quality Checklist

- [ ] Every core color has three tints, one core, and three shades.
- [ ] Ramp steps are perceptually ordered and retain hue identity.
- [ ] Neutral values carry a deliberate palette bias.
- [ ] Semantic tokens preserve the 60 / 30 / 7 / 3 hierarchy.
- [ ] Accent use remains scarce and action-oriented.
- [ ] Interactive and status states do not rely on color alone.
- [ ] CSS tokens and contrast warnings are included.

## Source

Adapted from **The Cinema Colour Vault** by [@itsdesignare](https://www.instagram.com/itsdesignare/).
