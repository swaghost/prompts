# Outfit Board - Harley Quinn

## Description

A cinematic wardrobe-development board that presents one recognizable character in nine complete costume directions while preserving face, body proportions, hair identity, attitude, pose system, and studio presentation. The result functions as a production-ready 4:5 costume reference rather than nine unrelated redesigns.

## Use It When

Use this board for costume exploration, fashion campaigns, alternate-universe styling, wardrobe continuity, character pitches, cosplay planning, and visual-development reviews.

## Prerequisites

- One clear full-body or three-quarter character reference
- Readable face, hairstyle, body proportions, signature makeup, and baseline costume language
- Enough model capability for nine distinct head-to-toe outfits with one stable identity
- Native 4:5 output; never crop from square, landscape, or 9:16

## Workflow

1. Upload one reference image as the identity source of truth.
2. Paste the full prompt without deleting its grid, identity, text, or full-body rules.
3. Generate natively at exact 4:5, preferably 3000 x 3750 px or higher.
4. Check that all nine looks are distinct, complete, and appropriate to their labels.
5. Regenerate rather than crop if feet, labels, panels, or safe-area content are missing.

## Continuity Rules

- Preserve the exact face, apparent age, complexion, facial structure, makeup language, body proportions, blonde twin ponytails, pink-and-blue ends, and character attitude.
- Keep one consistent front-facing fashion-reference pose, camera height, lens character, background, exposure, and lighting system.
- Change wardrobe, materials, accessories, and styling only as required by each outfit label.
- Keep every look fully visible from head to toe with no cropped feet or hidden silhouette.
- Treat the nine panels as one coordinated costume-development system.

## Platform and Format

**Platform:** GPT Image 2  
**Format:** Exact 4:5 vertical Instagram carousel, 3000 x 3750 px preferred

## Prompt

```text
Create a premium vertical 4:5 OUTFIT BOARD featuring Harley Quinn. Use the uploaded reference image as the single source of truth. Preserve the same recognizable face, pale complexion, blonde twin ponytails with pink and blue ends, dark eye makeup and playful attitude across every panel.

LAYOUT: Exact Instagram carousel ratio 4:5. The board fills 96-98% of the canvas. No white margins, side bars or excessive padding. Use only a thin solid black perimeter frame, matte-black and charcoal production-board styling, distressed golden-yellow borders and typography, subtle film grain, premium cinematic lighting, a compact hero header with a large portrait, and the exact title "OUTFIT BOARD".

CTA: In the extreme upper-left, render COMMENT in white above FACE in golden yellow. No panel numbering.

PANEL GRID: Create a precise 3x3 grid with fully visible head-to-toe looks: CLASSIC JESTER / 2016 STREET LOOK / BIRDS OF PREY / PUNK ROCK / GOTHAM MAFIA / RED CARPET / CYBERPUNK / MEDIEVAL / POST-APOCALYPTIC.

CONSISTENCY: Every outfit must be distinct and appropriate to its label. Preserve the same face, body proportions, hair and character identity. Use a consistent front-facing fashion-reference pose and dark neutral studio background.

STYLE: Photorealistic cinematic costume concept art, premium wardrobe-development board, realistic fabrics, leather, metal and accessories.

TEXT: Render only COMMENT, FACE, OUTFIT BOARD and the nine outfit labels.

AVOID: No other characters, identity changes, repeated outfits, cropped feet, panel numbers, logos, watermark, additional text or misspellings.
```

## Output Checklist

- [ ] Nine distinct head-to-toe looks in a 3x3 grid
- [ ] Same face, body proportions, hair, and character identity in every panel
- [ ] Front-facing fashion pose and dark neutral studio background stay consistent
- [ ] Feet remain visible and labels are limited to the approved text

## Negative Prompt

```text
9:16, square, landscape, cropped board, white margins, sidebars, fewer than nine outfits, extra panels, repeated outfit, identity drift, changed face, changed age, changed body proportions, changed ponytail structure, missing pink or blue hair ends, random makeup, inconsistent pose, inconsistent camera, inconsistent background, inconsistent lighting, cropped head, cropped feet, incomplete outfit, merged garments, impossible clothing, panel numbers, extra text, misspelled labels, clipped labels, logo, watermark, other characters
```

## Quick Correction Line

```text
Keep the exact same character identity, hair, body proportions, nine outfit labels, board design, and approved text. Rebuild natively in exact 4:5 portrait format with one hero header and a complete 3x3 outfit grid. Show every look head to toe with one consistent fashion-reference pose and dark neutral background.
```

## Fast Regeneration Commands

```text
Keep the same face, hair, makeup language, and body proportions in all nine panels.

Make every outfit more distinct and more faithful to its label without changing identity.

Show every look fully from head to toe; restore any cropped feet or missing accessories.

Keep one front-facing pose, camera, background, lighting, and color grade across the board.

Improve label spelling and rebuild natively in exact 4:5 with no extra text or panel numbering.
```

## Source

Part of the [Reference Board Prompt Pack](README.md). Adapt the named example only when you have the right to use the character or reference imagery; for original characters, replace identity-specific traits while preserving the board structure.
