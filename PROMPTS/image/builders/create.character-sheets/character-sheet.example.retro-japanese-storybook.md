# Character Sheet Prompt 02 - Retro Japanese Storybook Illustration

## Use

Create a full character reference sheet from one uploaded reference photo, translating the subject into a vintage Japanese anime and storybook editorial illustration while preserving identity.

## Master Consistency Anchor

```text
Maintain the exact facial identity, bone structure, eye shape, skin tone, and hair texture of the person in the uploaded reference photo across every panel of the character sheet. Do not alter their face. Preserve the same age, ethnicity, body proportions, hair, outfit, accessories, and shoes unless the selected style prompt explicitly specifies a new wardrobe. Render a comprehensive high-resolution character design sheet using the requested layout, with every panel clearly showing the same person.
```

## Image Prompt

```text
Maintain the exact facial features and identity of the person in the uploaded reference photo, translated into a charming vintage Japanese anime and storybook editorial illustration style. Create a full character reference sheet on an off-white parchment-paper texture.

The top section shows a full-body character turnaround in FRONT VIEW, SIDE VIEW, and BACK VIEW. Dress the subject in a cozy brown knitted wool vest over an ivory puff-sleeve blouse, dark forest-green pleated midi skirt, white socks, brown leather oxford shoes, and a vintage leather crossbody satchel bag.

The middle row shows four expressive illustrated headshots: NEUTRAL, THINKING, SOFT SMILE, and SURPRISED. The bottom row shows dynamic poses: walking, reading an open book, holding a coffee cup, and carrying wild flowers. Add circular material swatches and muted earth-tone color chips. Use clean lined character-design-sheet composition and preserve identity across every panel.

Use a modular 4:5 vertical layout, complete full-body figures with feet visible, clear panel hierarchy, and consistent linework, palette, clothing, face, and hair.
```

## Workflow and Parameters

Upload one clear front-facing reference photo, paste the anchor, then paste the image prompt. For Midjourney or Flux.1 append: `[IMAGE_URL] vintage Japanese storybook character sheet, front side back turnaround, illustrated expressions, action poses, material swatches, 8K --ar 4:5 --style raw --cref [IMAGE_URL] --cw 20 --iw 2.0`.

Add exact labels and metadata in post-production. If the composite becomes too dense, generate the turnaround, expressions, poses, and swatches separately before assembling.

## Production Checklist

- Front, side, and back views are present.
- Four specified illustrated expressions are present.
- Four dynamic poses are present.
- Wool, leather, and earth-tone swatch callouts are present.
- The same face, hair, body proportions, and identity appear throughout.
- The parchment grid and linework remain readable without overlapping panels.

## Negative Prompt

```text
Identity drift, altered facial structure, inconsistent hair, realistic photographic rendering, missing views, cropped feet, malformed anatomy, extra limbs, unreadable labels, invented text, extra props, panel overlap, muddy linework, logos, watermark, low resolution, compositing artifacts.
```
