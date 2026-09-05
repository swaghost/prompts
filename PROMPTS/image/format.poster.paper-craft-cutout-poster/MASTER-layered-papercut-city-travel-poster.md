# Layered Papercut City Travel Poster

## Description

A reusable landmark-led travel poster template that constructs a recognizable city from six to eight physically separated sheets of cut paper. Each sheet uses one flat color, and all depth comes from a consistent back-to-front stacking order and soft, short shadows rather than perspective, gradients, or internal shading.

## Usage

Replace the three slots in the master prompt: define one or two primary landmarks on dedicated layers, describe three to five secondary elements as a back-to-front stack, and state which landmark features must survive simplification. Keep the shared palette and every shadow and shading constraint unchanged so multiple cities read as one coherent poster series.

For the fastest city-specific adaptation, provide this guide to an LLM and ask: `Write me a layered papercut travel poster prompt for [CITY] following this guide.` Verify that it selects real landmarks, writes a stacking order rather than a list, and identifies details that must be physically cut through the paper.

## Engines / Models

- **Original platform:** Picsart AI Playground
- **Original model:** GPT Image 2
- **Mode:** Text-to-image; no reference photo required
- **Format:** Vertical 2:3

## Source

[Layered Papercut Posters - Cut Paper Edition](https://docs.google.com/document/d/1uQDYrEzpeyKsMqlFnB13BCPPmJbWIkW1R6bzeXCr3qg/mobilebasic?urp=gmail_link)

## Core Construction Rules

### Write a Stack, Not a List

Write secondary elements in explicit back-to-front order: sky, distant silhouettes, landmarks on dedicated layers, near buildings, trees or foreground planting, ground or water, and one cut edge at the very front. The model needs this order to create real separation between sheets.

### Cut Detail Through the Paper

Windows, arches, ribs, railings, and comparable structural openings must be holes cut through one sheet to reveal the sheet behind it. Never render these details as painted lines or surface marks.

### Preserve Flat Paper

Each layer is one flat, unmodulated color. Do not use a gradient, tonal modeling, or internal shading within any sheet. Physical stacking and shadows are the only sources of depth.

### Keep Shadows Soft and Short

Use one soft upper-left light across the entire composition. Every layer casts a soft, short, diffuse shadow onto the layer immediately behind it. Hard offset shadows or long shadows make the result look like flat vector art.

## Shared Series Palette

Use approximately seven colored art papers from this fixed palette:

- Mineral blue
- Dusty teal
- Pale sky
- Warm sandstone
- Muted coral
- Deep navy for the front-most layers
- Soft cream for the back sky layer

Keep this palette identical across every city in a series.

## Master Prompt

```text
DESTINATION LANDMARK-LED LAYERED PAPERCUT POSTER - [CITY NAME]

Create a tactile vertical travel art poster featuring [CITY NAME] in the manner of a layered cut-paper diorama. Aspect ratio 2:3, dimensional, soft, crafted - a photograph of stacked cut paper lit gently from one side.

CORE CONCEPT - LANDMARK 70% + PAPERCUT LAYERING 30%. Recognizable landmark first, papercut construction second. The viewer should immediately think: "This is [CITY NAME]."

LANDMARK PRIORITY -

Primary landmarks: [SLOT 1 - ONE OR TWO LANDMARKS, each occupying its OWN dedicated paper layer. Describe the distinctive shape, do not just name it]

Secondary elements: [SLOT 2 - THREE TO FIVE SUPPORTING ELEMENTS WRITTEN AS A STACKING ORDER, back to front: distant silhouettes, then near buildings, then trees or foreground planting, then ground or water. End with ONE FOREGROUND CUT EDGE at the very front of the stack]

The main landmarks retain their real-world silhouette and essential proportions and dominate everything around them. Simplify surface detail, never structure. [SLOT 3 - ONE SENTENCE NAMING WHAT MUST SURVIVE THE SIMPLIFICATION, for example: "The dome must keep its ribbed profile and lantern"]

PAPERCUT TREATMENT - the image is built from SIX TO EIGHT distinct depth layers of cut paper, each a SINGLE FLAT COLOUR, stacked front to back with real physical separation between them. Every layer casts a SOFT, SHORT, DIFFUSE drop shadow onto the layer behind it - gentle, never hard or graphic, and these shadows are the ONLY thing describing depth. There is no perspective, no atmospheric haze and no rendering. Every edge is a cut edge: clean, crisp, with the barest suggestion of paper thickness catching the light along the top of each form. DETAIL IS ACHIEVED BY CUTTING THROUGH - window openings, arch shapes, structural ribs and the gaps in railings are cut HOLES revealing the layer behind, not painted marks. Light comes softly from the UPPER LEFT, consistent across all layers.

COMPOSITION - upper 40% is the flat back sky layer. At upper center place only: [CITY NAME], rendered as individually CUT uppercase sans-serif letters with wide letter spacing, sitting slightly in front of the sky layer and casting the same soft shadow as everything else. Build the city across the middle and lower frame.

COLOR PALETTE - Colored art paper in a cool register: mineral blue, dusty teal, pale sky, warm sandstone, muted coral, deep navy for the front-most layers, and soft cream for the back sky layer. Roughly seven flat papers. Each layer is a single unmodulated color - depth is described by shadow and stacking order, NEVER by shading within a layer. KEEP THIS PALETTE IDENTICAL ACROSS EVERY CITY - it is what makes the set read as one series.

TEXTURE - matte art paper surface: a fine even fiber tooth visible on every layer, crisp clean cut edges with a hairline of paper thickness, soft ambient occlusion in the crevices where layers meet. Clean and contemporary. No aged paper, brown filters, sepia tones or yellowing.

Constraints: exact spelling "[CITY NAME]", no text other than that word, NO hard graphic drop shadows, NO gradients within a layer, NO shading within a layer, no perspective depth cues, no photorealism, no 3D rendering of materials other than paper, no glow, no neon colors, no gold, no glitter, no aged paper, no sepia, no tears, no crumpling, no travel sticker aesthetics, no cartoon style, no cute characters, no complex typography, no watermark, no logos.
```

## Slot Checklist

- **Slot 1:** One or two real landmarks, each assigned its own paper layer and described by silhouette.
- **Slot 2:** Three to five supporting elements in explicit back-to-front order, ending with a foreground cut edge.
- **Slot 3:** One sentence naming the essential shape, opening, rib, arch, railing, or profile that must survive simplification.

## Quality Checklist

- [ ] The city is identifiable before the papercut technique is noticed.
- [ ] The poster contains six to eight visibly separated paper sheets.
- [ ] Every sheet has one flat color with no gradient or internal shading.
- [ ] Secondary elements follow a readable back-to-front stacking order.
- [ ] Important windows, arches, ribs, and railings are cut holes, not painted details.
- [ ] One foreground cut edge closes the front of the stack.
- [ ] Lighting comes only from the upper left.
- [ ] Every shadow is soft, short, and diffuse.
- [ ] The shared mineral-blue, teal, sandstone, coral, navy, and cream palette is preserved.
- [ ] The upper 40% remains the flat sky layer.
- [ ] Only the correctly spelled city name appears as cut uppercase letters.
- [ ] The result is vertical 2:3 with no watermark or logo.

---

_Landmark first. Physical paper construction second. Detail is cut, not drawn._
