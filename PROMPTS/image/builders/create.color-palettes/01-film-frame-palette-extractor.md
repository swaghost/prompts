# Film-Frame Palette Extractor

## Description

Extract a disciplined four-color working palette from three related film frames or visual references. The tool samples broad visual behavior rather than a promotional poster and assigns each retained color a practical compositional role.

## Best For

- Film-inspired brand systems
- Campaign art direction
- Editorial and poster design
- UI and web visual systems
- Production-design analysis

## Inputs

- **Image 1:** Wide frame from one scene or sequence
- **Image 2:** Medium frame from the same scene or sequence
- **Image 3:** Close frame from the same scene or sequence
- **Target use:** Brand, campaign, interface, poster, environment, or other application

## Tool Prompt

```text
Analyze Images 1-3 as three distances from the same visual sequence: one wide, one medium, and one close frame. Extract how color behaves across the sequence rather than copying the most dramatic single frame.

STEP 1 - SAMPLE SIX CANDIDATES
Identify exactly six representative colors:
1. Darkest meaningful value
2. Lightest meaningful value
3. Dominant environmental field
4. Brightest or most memorable accent
5. Mid-value supporting color A
6. Mid-value supporting color B

For each candidate provide:
- HEX
- RGB
- HSL
- Approximate visible coverage across all three frames
- Source location in the imagery
- Saturation and temperature description
- Emotional or narrative function in context

STEP 2 - DELETE TWO
Remove the two candidates that are redundant, too similar in role, too incidental, or least useful for [TARGET USE]. Explain each deletion in one sentence. Do not keep six colors merely because they are present.

STEP 3 - ASSIGN FOUR ROLES
Assign the retained colors to:
- BASE - 60%: dominant world or field
- STRUCTURE - 30%: typography, panels, borders, lines, shadows, or organization
- SIGNATURE - 7%: recognizable identity or story color
- ACCENT - 3%: scarce high-impact action, highlight, or focal event

No two colors may share the same role. If a sampled color cannot perform its role with adequate contrast, adjust value or saturation minimally and disclose the change.

STEP 4 - EXPLAIN THE SYSTEM
Describe:
- Why the four colors work together
- Dominant saturation position: low, medium, or high
- Dominant temperature: warm or cool
- Complementary, analogous, monochrome, or mixed relationship
- How the palette changes between wide, medium, and close framing
- Which color must remain scarce
- Which neutral carries a bias from the dominant hue
- Where the system is likely to fail

STEP 5 - OUTPUT
Return:
1. A four-swatch palette table with role, ratio, HEX, RGB, HSL, source, and use
2. One horizontal proportional bar displaying 60 / 30 / 7 / 3 coverage
3. A concise application map for [TARGET USE]
4. A do-not-use list
5. A machine-readable JSON object with base, structure, signature, and accent tokens

Do not return five equal swatches. Do not extract colors from titles, subtitles, logos, player UI, letterbox bars, or promotional graphics. Analyze only the visual world inside the frames.
```

## Quality Checklist

- [ ] All three images come from one coherent sequence or visual system.
- [ ] Exactly six candidates are sampled and exactly two are removed.
- [ ] The final palette contains four non-redundant roles.
- [ ] Ratios total 100% and follow 60 / 30 / 7 / 3.
- [ ] Sample locations and color values are explicit.
- [ ] Interface overlays and letterbox bars are excluded.
- [ ] The output includes a usage map, failure risks, and JSON tokens.

## Source

Adapted from **The Cinema Colour Vault** by [@itsdesignare](https://www.instagram.com/itsdesignare/).
