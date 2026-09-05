# Cinema Colour Vault - Color Extraction Tools

Five reusable prompts for extracting, understanding, adapting, expanding, and validating color palettes from film frames or other visual references.

## Tools

1. [Film-Frame Palette Extractor](01-film-frame-palette-extractor.md)
2. [Palette Role and Psychology Decoder](02-palette-role-psychology-decoder.md)
3. [Film-Palette Adaptation Tool](03-film-palette-adaptation.md)
4. [Color Ramp and Design Token Generator](04-color-ramp-design-token-generator.md)
5. [Palette Accessibility and Hierarchy Audit](05-palette-accessibility-hierarchy-audit.md)

## Core Model

Assign four colors distinct jobs before applying them:

| Role      | Ratio | Job                                                                       |
| --------- | ----: | ------------------------------------------------------------------------- |
| Base      |   60% | The world or dominant field that holds the composition                    |
| Structure |   30% | Type, lines, panels, borders, shadows, and organization                   |
| Signature |    7% | The recognizable color associated with the identity or story              |
| Accent    |    3% | A scarce high-impact event such as one action, highlight, or focal object |

Use the ratio as a hierarchy rather than treating all swatches equally. When the design is blurred or viewed at thumbnail scale, the base should read first, structure second, and one small hot spot last.

## Recommended Workflow

1. Pull three frames from one sequence: one wide, one medium, and one close view.
2. Extract six candidates: darkest, lightest, dominant field, brightest accent, and two intermediates.
3. Remove two candidates and assign the remaining four to Base, Structure, Signature, and Accent.
4. Decode saturation, temperature, context, emotional signal, and failure risks.
5. Rotate all four hues consistently by 10-20 degrees when adapting the relationship into original work.
6. Build three tints and three shades per core color for usable states and tokens.
7. Audit value hierarchy, contrast, outdoor-phone legibility, and color-vision resilience before shipping.

## Shared Principles

- Restriction creates authorship; prefer four purposeful hues over a broad undirected range.
- A palette may move across a narrative or interface rather than remain fixed.
- Every accent should have a motivated source or semantic job.
- Tint near-black, off-white, and gray toward the dominant hue instead of defaulting to pure neutrals.
- Saturation often changes meaning more strongly than hue.
- Temperature is relational: a color reads warm only beside something cooler.
- Do not use color as the only signal for status, meaning, or interaction.

## Film Reference Palettes

| Film                     | Palette                                    | Transferable Structure                                                       |
| ------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------- |
| La La Land               | `#21119F`, `#3368C8`, `#652ADB`, `#FEDB26` | Violet base, blue structure, orchid signature, tightly rationed yellow event |
| The Grand Budapest Hotel | `#BB080A`, `#46193F`, `#8989AF`, `#D19B91` | Jewel signature supported by dusty, desaturated relatives and a dark anchor  |
| The Matrix               | `#0E3D15`, `#498362`, `#D5CBA9`, `#051905` | One hue at several values, warm human neutral, hue-biased near-black         |
| Blade Runner 2049        | `#610000`, `#C03400`, `#F2651B`, `#FDAA37` | Monochrome value ladder with depth created through contrast and haze         |
| In the Mood for Love     | `#7A1220`, `#C4302B`, `#D8A24A`, `#2A2117` | Saturated red and gold held against a very dark base                         |
| Amelie                   | `#2F5A32`, `#C1272D`, `#E0A93B`, `#F0E2C0` | Complementary green and red organized by a golden neutral                    |
| Mad Max: Fury Road       | `#D9541F`, `#F2A03D`, `#1E6E8C`, `#0E2A33` | Strong orange-blue complement with limited middle values                     |
| Moonlight                | `#0B2A4A`, `#1D6E8E`, `#7A3E86`, `#E8C9A0` | One hue family per narrative chapter with stable human skin reference        |
| Her                      | `#D65A4E`, `#E8A08D`, `#F2E3D5`, `#8A3B36` | Warm monochrome shaped partly by intentional absence of blue                 |

## Source

Adapted into reusable tools from **The Cinema Colour Vault**, Designare Colour Study No. 01, by [@itsdesignare](https://www.instagram.com/itsdesignare/).
