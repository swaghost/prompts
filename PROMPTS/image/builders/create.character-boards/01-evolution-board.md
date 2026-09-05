# Evolution Board

## Description

A cinematic production-reference board that tracks one character through six logical stages of development while documenting changes to the face, costume, body, signature details, power state, silhouette, materials, and color system. The final board is designed as a dense but readable 4:5 portrait artifact for character development and generation continuity.

## Use It When

Best for showing how one character develops across eras, upgrades, or forms.

## Prerequisites

- One clear full-body or three-quarter character reference image
- A readable face, costume silhouette, signature traits, and primary materials
- Optional verified names for origin, forms, or progression stages; otherwise use neutral labels and do not invent canon

## Workflow

1. Upload the character reference image as the single source of truth.
2. Paste the complete master prompt without deleting its panel structure.
3. Generate natively in exact 4:5 portrait format, ideally 1080 x 1350 px or higher.
4. Verify that every stage remains recognizably the same character and progresses logically.
5. Regenerate rather than crop if the output is 9:16, square, landscape, or extra tall.

## Continuity Rules

- Preserve the same face, age, body proportions, signature traits, and costume language across all stages.
- Change only features justified by the stated progression; never present six unrelated redesigns.
- Keep titles, labels, panels, swatches, and captions inside the 4:5 safe area.
- Use readable English labels. Use `UNKNOWN` or `CLASSIFIED` when a fact cannot be inferred.
- Keep one border system, typography hierarchy, grain treatment, interface language, and accent palette throughout.
- Treat the output as a production reference system, not a generic mood board.

## Master Prompt

```
Create a single high-resolution, densely packed character evolution reference sheet titled "EVOLUTION BOARD" using the attached character image as the single source of truth for identity, face, body proportions, signature visual traits, costume language, materials, and colour palette.

Output must be a true Instagram carousel portrait image in EXACT 4:5 aspect ratio, composed natively for 4:5. Do not generate 9:16, square, landscape, or an extra-tall poster. Keep every panel, title, label, and caption safely inside the 4:5 frame.

The same character must remain clearly recognizable throughout every evolutionary stage while showing meaningful, logical progression. Use a premium cinematic production-reference board: deep near-black background, subtle distressed texture, thin yellow/gold technical borders, restrained character-derived neon accents, faint film grain, sophisticated sci-fi/editorial UI, realistic materials, and dramatic studio lighting.

TOP SECTION: Large title EVOLUTION BOARD and a prominent hero image showing the character's most advanced/final form.

METADATA: SUBJECT · ORIGIN · CORE IDENTITY · BASE FORM · SIGNATURE TRAITS · EVOLUTION TYPE · PRIMARY MATERIALS · COLOR SYSTEM · FINAL STATE.

PANEL 01 — EVOLUTION TIMELINE: Show 6 full-body stages: ORIGIN · EARLY FORM · DEVELOPED FORM · ASCENSION · ADVANCED FORM · FINAL FORM. Arrange them sequentially with subtle arrows or progression markers. Each stage must feel like a logical evolution of the previous one.

PANEL 02 — FACE / HEAD EVOLUTION: Show 4 close-up portraits demonstrating how the head, mask, hair, skin, helmet, or facial features evolve while maintaining identity.

PANEL 03 — COSTUME / BODY EVOLUTION: Show 4 detailed studies of changes in armor, clothing, anatomy, surface materials, or silhouette.

PANEL 04 — SIGNATURE DETAIL EVOLUTION: Show 4 macro studies of the character's most recognizable visual element evolving across stages.

PANEL 05 — POWER / ENERGY PROGRESSION: Show 4 increasingly powerful visual states: DORMANT · ACTIVE · OVERCHARGED · MAXIMUM.

PANEL 06 — COLOR PALETTE: Show 6 swatches with HEX codes derived directly from the character.

Add the bottom caption: "Use this evolution board as a visual reference for consistent character progression across all generations." Bottom-right tags: STYLE · Evolution · Realistic · Cinematic.

Photorealistic where appropriate to the source, production-design quality, extremely detailed, consistent identity, sophisticated information hierarchy, sharp readable English typography, 8K appearance, fine cinematic grain.
```

## Negative Prompt

```
9:16, square, landscape, cropped poster, inconsistent face, identity drift, random costume changes, unrelated stages, illegible labels, clipped panels, invented canon, cluttered layout, cartoon, low detail, watermark, logo, or unsafe-edge content.
```

## Quick Correction Line

```text
Keep all existing content and character identity. Rebuild the entire composition natively in EXACT 4:5 portrait aspect ratio. Do not crop a 9:16 poster. Reflow every panel, title, label, stage, swatch, and caption inside the 4:5 safe area.
```

## Quality Checklist

- [ ] Output is native 4:5 portrait, not a cropped taller composition.
- [ ] The same identity, age, proportions, and signature design remain recognizable in every stage.
- [ ] Six full-body stages show one coherent progression from origin to final form.
- [ ] Face, costume, signature-detail, power, and silhouette studies agree with the timeline.
- [ ] The hero final form and main title read first.
- [ ] All labels and HEX codes are legible, accurate, and safely framed.
- [ ] Borders, UI, grain, and accent colors form one visual system.
- [ ] No unsupported biography, unrelated redesign, watermark, or clipped content appears.

## Fast Regeneration Commands

```text
Keep the exact same character identity and evolution logic. Improve face consistency across every stage.

Make every stage feel like a direct development of the previous stage rather than an unrelated redesign.

Reduce visual clutter by 15% while preserving every required panel, label, timeline stage, and swatch.

Increase typography readability and give the final-form hero image stronger visual priority.

Rebuild natively in EXACT 4:5 portrait format and keep all content inside the safe area.
```
