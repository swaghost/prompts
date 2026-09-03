# Character Sheet Prompt 01 - Classic Menswear and Business Suit

## Use

Create a production-ready character model sheet from one uploaded reference photo. The same recognizable person must appear in every panel.

## Master Consistency Anchor

```text
Maintain the exact facial identity, bone structure, eye shape, skin tone, and hair texture of the person in the uploaded reference photo across every panel of the character sheet. Do not alter their face. Preserve the same age, ethnicity, body proportions, hair, outfit, accessories, and shoes unless the selected style prompt explicitly specifies a new wardrobe. Render a comprehensive high-resolution character design sheet using the requested layout, with every panel clearly showing the same person.
```

## Image Prompt

```text
Maintain the exact facial features and identity of the person in the uploaded reference photo across the entire sheet. Create a complete professional character model turnaround sheet on a clean light-grey studio backdrop. At the top, show three full-body standing views: FRONT VIEW, 90-DEGREE SIDE PROFILE VIEW, and BACK VIEW. The subject wears a tailored charcoal-black modern suit, crisp white dress shirt, slim black silk tie, and polished black dress shoes.

The middle section displays a horizontal strip of five facial-expression headshots: SMILE, LAUGH, THOUGHTFUL WITH HAND ON CHIN, SERIOUS, and SURPRISED. The bottom-right section shows three dynamic poses: walking forward, sitting on a tall wooden studio stool, and adjusting suit cuffs. The bottom-left section includes circular zoom-in callouts of suit wool fabric, cotton shirt weave, silk tie, and leather shoe details alongside color palette swatches.

Professional fashion design document, razor-sharp studio lighting, 8K resolution, clean hierarchy, precise labels, and consistent identity across every panel. Use a modular 4:5 vertical layout with complete full-body figures and feet visible.
```

## Workflow and Parameters

Upload one clear front-facing reference photo, paste the anchor, then paste the image prompt. For Midjourney or Flux.1 append: `[IMAGE_URL] comprehensive professional character sheet, front side back turnaround, expressions, dynamic poses, fabric callouts, color chips, 8K --ar 4:5 --style raw --cref [IMAGE_URL] --cw 20 --iw 2.0`.

Add exact labels and metadata in post-production. Keep FRONT VIEW, SIDE PROFILE VIEW, and BACK VIEW aligned above or below the figures.

## Production Checklist

- Front, side, and back views are present.
- Five specified expressions are present.
- Three dynamic poses are present.
- Suit, shirt, tie, and shoe material callouts are present.
- The same face, hair, proportions, and identity appear throughout.
- Full-body figures, feet, labels, and panels remain readable.

## Negative Prompt

```text
Altered identity, inconsistent face, changing hairstyle, missing turnaround view, cropped feet, duplicate limbs, malformed hands, extra props, unreadable labels, invented metadata, overlapping panels, plastic skin, low resolution, logos, watermark, compositing artifacts.
```
