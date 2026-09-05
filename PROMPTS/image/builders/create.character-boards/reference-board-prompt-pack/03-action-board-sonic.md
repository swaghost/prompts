# Action Board - Sonic

## Description

A cinematic action-reference board that captures one character in nine distinct movement states while preserving identity, proportions, signature materials, costume elements, and visual readability. The board emphasizes clear silhouettes and controlled motion effects for animation, game, and campaign planning.

## Use It When

Use this board for movement libraries, animation blocking, game-production references, action campaigns, pose ideation, speed studies, and sequence planning.

## Prerequisites

- One clear character reference showing identity, body proportions, and signature costume details
- A readable full-body silhouette suitable for dynamic motion
- A model capable of consistent character rendering across nine action panels
- Native 4:5 output; do not crop from another aspect ratio

## Workflow

1. Upload one character image as the identity and design source of truth.
2. Paste the complete prompt with all action, layout, text, and continuity rules intact.
3. Generate natively at exact 4:5, preferably 3000 x 3750 px or higher.
4. Verify that all nine actions have distinct body mechanics and readable silhouettes.
5. Regenerate if motion effects obscure anatomy, panels repeat, or labels drift.

## Continuity Rules

- Preserve the same face, blue fur, tan muzzle, green eyes, white gloves, red shoes, athletic proportions, and personality.
- Keep materials, colors, scale, and character design stable across every action.
- Change only pose, body mechanics, camera support, and restrained action effects required by each label.
- Keep speed trails, dust, sparks, and blur subordinate to the silhouette and face.
- Maintain one coherent cinematic rendering and board-design system.

## Platform and Format

**Platform:** GPT Image 2  
**Format:** Exact 4:5 vertical Instagram carousel, 3000 x 3750 px preferred

## Prompt

```text
Create a premium vertical 4:5 ACTION BOARD featuring Sonic the Hedgehog. Use the uploaded reference image as the visual identity reference. Preserve Sonic's blue fur, tan muzzle, large green eyes, white gloves, red shoes, athletic proportions and confident personality in every panel.

LAYOUT: Exact Instagram carousel ratio 4:5. The board fills 96-98% of the canvas. No white margins, side bars or excessive padding. Use only a thin solid black perimeter frame, matte-black and charcoal production-board styling, distressed golden-yellow borders and typography, subtle film grain, cinematic motion lighting, a compact hero header with Sonic running, and the exact title "ACTION BOARD".

CTA: In the extreme upper-left, render COMMENT in white above FACE in golden yellow. No panel numbering.

PANEL GRID: Create a precise 3x3 grid showing: FULL SPRINT / SPIN DASH / POWER SLIDE / HIGH JUMP / WALL RUN / RAIL GRIND / MID-AIR SPIN / SUDDEN STOP / VICTORY POSE.

CONSISTENCY: Every action must have a clearly different body position and readable silhouette. Use controlled speed trails, dust, sparks and cinematic motion effects without obscuring Sonic. Preserve identity, outfit and proportions.

STYLE: High-end cinematic 3D animation, energetic action concept art, sharp character rendering, controlled motion blur and premium game-production presentation.

TEXT: Render only COMMENT, FACE, ACTION BOARD and the nine action labels.

AVOID: No other characters, combat, weapons, costume changes, duplicated poses, panel numbers, logos, watermark, additional text or misspellings.
```

## Output Checklist

- [ ] Nine distinct actions with readable silhouettes
- [ ] Blue fur, tan muzzle, green eyes, gloves, shoes, and proportions remain consistent
- [ ] Motion effects support rather than obscure the character
- [ ] No combat, weapons, duplicate poses, or unapproved text

## Negative Prompt

```text
9:16, square, landscape, cropped board, white margins, fewer than nine panels, extra panels, duplicate action, weak silhouette, identity drift, changed face, changed fur color, missing tan muzzle, changed eye color, missing gloves, changed shoes, changed proportions, broken anatomy, extra limbs, duplicate limbs, detached limbs, impossible joints, uncontrolled motion blur, face obscured by effects, excessive speed trails, combat, weapons, other characters, panel numbers, extra text, misspelled labels, logo, watermark
```

## Quick Correction Line

```text
Keep the exact same character identity, colors, proportions, nine action labels, board design, and approved text. Rebuild natively in exact 4:5 portrait format with one hero header and a complete 3x3 action grid. Make every action mechanically distinct and keep all motion effects behind or around the readable character silhouette.
```

## Fast Regeneration Commands

```text
Keep the same face, fur, eyes, gloves, shoes, and body proportions in every panel.

Increase pose variety and make each action silhouette immediately readable.

Reduce motion effects where they obscure the face, hands, feet, or body mechanics.

Correct anatomy, foot placement, limb ownership, and action-specific balance.

Rebuild natively in exact 4:5 with nine labelled panels, no repeats, and no extra text.
```

## Source

Part of the [Reference Board Prompt Pack](README.md). Adapt the named example only when you have the right to use the character or reference imagery; for original characters, replace identity-specific traits while preserving the board structure.
