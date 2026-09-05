# Film-Palette Adaptation Tool

## Description

Convert an admired film palette into an original color system by preserving its relationships and roles while rotating hues, adapting values, and assigning motivated applications. The result should inherit the mechanism without remaining traceable as a direct copy.

## Best For

- Original brand systems inspired by cinema
- Campaign and editorial art direction
- Website section palettes
- Product launch visuals
- Narrative or chapter-based color arcs

## Inputs

- Source four-color film palette or three source frames
- Target brand, project, or visual medium
- Desired emotional outcome
- Preferred hue-shift direction or permission to select one

## Tool Prompt

```text
Adapt the supplied film palette into an original working system for [PROJECT / BRAND / MEDIUM]. Preserve the palette's hierarchy and relationships, not its exact swatches.

STEP 1 - DEFINE THE SOURCE MECHANISM
Identify:
- Base, Structure, Signature, and Accent roles
- Approximate 60 / 30 / 7 / 3 usage ratio
- Dominant value pattern
- Saturation strategy
- Warm-cool relationship
- Whether the system is complementary, analogous, monochrome, chapter-based, or driven by intentional hue absence
- Motivated source for each important color in the original world

STEP 2 - ROTATE THE SYSTEM
Rotate every chromatic hue in the same direction by one consistent amount between 10 and 20 degrees. Select the amount that best suits [DESIRED EMOTION] and state it. Preserve relative hue spacing. Do not rotate colors independently merely to make them attractive.

STEP 3 - ADAPT VALUE AND SATURATION
Adjust value and saturation only as required for [MEDIUM]. Preserve the original relationship while ensuring:
- A stable dominant field
- A legible structural neutral
- A recognizable but controlled signature
- A scarce high-impact accent
- Hue-biased near-black and off-white instead of automatic pure #000 and #FFF

STEP 4 - MOTIVATE EVERY COLOR
Assign each role to a real function such as background, typography, border, brand mark, CTA, state, product, light source, chapter, or human element. No color may float into the layout only because an area feels empty.

STEP 5 - CREATE A COLOR ARC
If the project has sections or time, define how temperature, saturation, or dominant hue moves from opening to ending. Keep one human or brand anchor stable where appropriate.

OUTPUT
Return:
1. Source-role table
2. Chosen hue rotation and rationale
3. Adapted four-color palette with HEX, RGB, HSL, role, ratio, and semantic use
4. Before-and-after comparison
5. Application rules for [MEDIUM]
6. Optional three-stage color arc
7. Prohibited uses and traceability risks

The final system must feel inspired by the source relationship without reproducing the source palette exactly. If a knowledgeable viewer can immediately name the film from the colors alone, adapt it further.
```

## Quality Checklist

- [ ] Source roles and relationships are identified before colors are changed.
- [ ] All chromatic hues rotate consistently by 10-20 degrees.
- [ ] Relative spacing and hierarchy survive the adaptation.
- [ ] Each color has a motivated semantic or environmental use.
- [ ] Near-black and off-white carry the dominant hue bias when appropriate.
- [ ] The result no longer reads as a direct film-palette copy.
- [ ] The output includes exact values, ratios, use rules, and prohibited uses.

## Source

Adapted from **The Cinema Colour Vault** by [@itsdesignare](https://www.instagram.com/itsdesignare/).
