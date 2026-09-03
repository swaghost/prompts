# Character Model Sheets - Extracted Style Prompts

Six standalone character-sheet image prompts extracted from the Professional AI Character Model Sheets and Turnarounds guide. Each file repeats the shared production instructions so it can be used independently.

## Shared Sheet Anatomy

Every sheet should include a front, side, and back turnaround; four or five expression headshots; three to five dynamic poses; material or fabric callouts; color palette chips; and biographical or production notes where appropriate. Keep the same recognizable person, face, hair, proportions, outfit, accessories, and shoes in every panel.

## Collection

1. [Classic Menswear and Business Suit](01-classic-menswear-business-suit.md)
2. [Retro Japanese Storybook Illustration](02-retro-japanese-storybook.md)
3. [Pro Footballer and Athletic Kit](03-pro-footballer-athletic-kit.md)
4. [Evening Gown and Luxury Gala](04-evening-gown-luxury-gala.md)
5. [Dark Academia Detective](05-dark-academia-detective.md)
6. [Modern Business Chic](06-modern-business-chic.md)

## Shared Identity Anchor

```text
Maintain the exact facial identity, bone structure, eye shape, skin tone, and hair texture of the person in the uploaded reference photo across every panel of the character sheet. Do not alter their face. Preserve the same age, ethnicity, body proportions, hair, outfit, accessories, and shoes unless the selected style prompt explicitly specifies a new wardrobe. Render a comprehensive high-resolution character design sheet using the requested layout, with every panel clearly showing the same person.
```

## Shared Production Settings

- Upload one clear, front-facing reference photo to an image-capable model.
- Append the identity anchor before the selected style prompt.
- Use a modular, readable grid with no overlapping panels.
- Recommended format: 4:5 vertical, 8K, sharp focus.
- For Midjourney or Flux.1: `--ar 4:5 --style raw --cref [IMAGE_URL] --cw 20 --iw 2.0`
- Add exact labels, metadata, and swatches in Canva, Photoshop, or Figma when text fidelity matters.
- If the composite becomes too dense, generate turnaround, expressions, poses, and material callouts separately, then assemble them with the same reference and anchor.

## Shared Negative Direction

Avoid altered identity, inconsistent face or hair, changing body proportions, missing views, duplicate or malformed limbs, cropped feet, unreadable labels, invented metadata, extra props, overlapping panels, logos, watermarks, low resolution, plastic skin, and compositing artifacts.
