# Expression Board - Wednesday Addams

## Description

A cinematic facial-expression reference board that presents one character in nine clearly differentiated emotional states while locking identity, hairstyle, wardrobe, camera, background, and lighting. The board is designed as a compact 4:5 production artifact for facial-performance planning and generation consistency.

## Use It When

Use this board for expression libraries, acting references, animation planning, portrait campaigns, reaction-image sets, character continuity, and emotion-driven storyboards.

## Prerequisites

- One sharp uploaded character reference with the face unobstructed
- Readable eyes, eyebrows, mouth, jawline, hairstyle, and signature wardrobe
- A model capable of consistent multi-panel identity and controlled typography
- Native 4:5 output; do not crop a square, landscape, or 9:16 generation

## Workflow

1. Upload one clear reference image as the single source of truth.
2. Paste the complete prompt without removing its layout, identity, text, or expression rules.
3. Generate natively at exact 4:5, preferably 3000 x 3750 px or higher.
4. Verify that only facial expression changes between the nine panels.
5. Regenerate rather than crop if margins, labels, identity, or panel count are incorrect.

## Continuity Rules

- Preserve the exact face, apparent age, complexion, skull proportions, eyes, nose, mouth, jawline, bangs, braids, uniform, collar, tie, body proportions, and character identity.
- Keep camera angle, crop, background, focal-length character, exposure, white balance, and lighting identical across all expression panels.
- Change only facial musculature, gaze nuance, and the smallest natural head response required by each label.
- Keep all labels and design elements safely inside the native 4:5 frame.
- Treat the result as one production reference board, not nine unrelated portraits.

## Platform and Format

**Platform:** GPT Image 2  
**Format:** Exact 4:5 vertical Instagram carousel, 3000 x 3750 px preferred

## Prompt

```text
Create a premium vertical 4:5 EXPRESSION BOARD featuring Wednesday Addams. Use the uploaded image as the single visual reference. Preserve her pale complexion, straight black bangs, two long braids, dark eyes, black Nevermore-style uniform, white collar and black tie in every panel.

LAYOUT: Exact Instagram carousel ratio 4:5. The board fills 96-98% of the canvas. No white margins, side bars or excessive padding. Use only a thin solid black perimeter frame, a matte-black and charcoal production-board aesthetic, distressed golden-yellow borders and typography, subtle film grain, a compact hero header with a large portrait, and the exact title "EXPRESSION BOARD".

CTA: In the extreme upper-left, render COMMENT in white above FACE in golden yellow. No panel numbering.

PANEL GRID: Below the hero portrait, create a precise 3x3 grid showing: NEUTRAL / SUBTLE SMILE / SUSPICIOUS / ANGRY / SHOCKED / SAD / DISGUSTED / EVIL SMIRK / DEADPAN.

CONSISTENCY: Keep the camera angle, hairstyle, wardrobe, background and lighting identical across every panel. Only the facial expression may change.

STYLE: Photorealistic cinematic character photography, dark gothic atmosphere, premium production reference sheet, highly detailed and consistent.

TEXT: Render only COMMENT, FACE, EXPRESSION BOARD and the nine expression labels.

AVOID: No other characters, outfit changes, hairstyle changes, exaggerated cartoon faces, panel numbers, logos, watermark, additional text or misspellings.
```

## Output Checklist

- [ ] Nine distinct expressions in a 3x3 grid
- [ ] Same face, hair, uniform, camera, background, and lighting in every panel
- [ ] Only permitted CTA, title, and expression labels are rendered
- [ ] Native 4:5 output with no white margins or panel numbering

## Negative Prompt

```text
9:16, square, landscape, cropped board, white margins, sidebars, excessive padding, fewer than nine panels, extra panels, duplicate expressions, unclear expression, exaggerated cartoon face, changed identity, changed age, changed facial proportions, changed hairstyle, missing braids, changed uniform, changed collar, changed tie, camera drift, background drift, lighting drift, inconsistent crop, panel numbering, extra text, misspelled labels, clipped labels, illegible typography, logo, watermark, additional character
```

## Quick Correction Line

```text
Keep the exact same character identity, hairstyle, uniform, expression list, board design, and approved text. Rebuild the entire sheet natively in exact 4:5 portrait format with one hero header and a complete 3x3 expression grid. Change only the facial expression between panels; keep camera, background, lighting, and crop identical.
```

## Fast Regeneration Commands

```text
Keep the exact same identity and uniform. Increase facial consistency across all nine expression panels.

Make every expression clearly distinct while keeping it anatomically natural and recognizable.

Keep camera, crop, background, lighting, hairstyle, and wardrobe identical in every panel.

Improve label spelling and typography readability without adding any new text.

Rebuild natively in exact 4:5 portrait format with no white margins, clipped panels, or panel numbering.
```

## Source

Part of the [Reference Board Prompt Pack](README.md). Adapt the named example only when you have the right to use the character or reference imagery; for original characters, replace the identity-specific traits while preserving the board structure.
