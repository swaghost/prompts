# The Flooded Hall: Wide Animation Carousel-Cut Guide

## Overview

Build the first two 3:4 slides of a carousel from one horizontal 3:2 scene. Generate one wide still, composite the typography before animating, animate the entire wide image with a locked camera, then crop the finished clip into exact left and right halves. Because both slides come from the same frame, the swipe reads as a continuous camera view rather than a page turn.

## Tools and Settings

- Adobe Firefly Image: Wide 3:2, Quality High
- Adobe Firefly Video: Landscape, 1080p, 24 fps, 6 seconds, audio off
- Image editor for the typography composite
- Phone photo/video editor for final crops

## Core Rules

1. Keep the vertical centerline empty. No fish, limbs, or column edges may cross it.
2. Give each half a complete composition: subject and clean type space on the left, depth and a second visual anchor on the right.
3. Composite all typography onto the still before animation so foreground koi can pass in front of it.
4. Generate wide, animate wide, then cut once. Never generate or animate the two slides separately.

## Workflow

### Step 1: Generate the 3:2 Hero Image

Create four or five variations, then select one with a genuinely clean left quarter, clear centerline, and enormous foreground koi. Use this complete Firefly image prompt:

```text
FORMAT
One horizontal frame, 3:2 landscape. Photorealistic, shot on a full-frame camera. No text anywhere in the image.

COMPOSITION - this governs everything else
The frame will later be cut in half down the exact vertical centre, and each half has to stand on its own. Place the woman in the LEFT half, about a third of the way across. Leave the leftmost quarter of the frame as clean unbroken marble. The RIGHT half holds the hall receding between columns with its own koi and its own open depth. Nothing important crosses the vertical centre line - no fish, no limb, no column edge sitting on it.

SCENE
The interior of a vast empty stone hall. A row of massive round columns recedes into depth across the frame, cut from cool turquoise-grey marble veined with dusty rose, their surfaces worn and softly polished by age. The nearest column stands immediately behind the woman, thick enough to fill that part of the frame, cropped by the top edge, its round base sitting on the floor beside her. Behind it the hall recedes into deep saturated teal shadow between further columns. The floor is worn stone in the same cool turquoise-grey, faintly reflective. Hard daylight cuts in low from the left through an opening out of frame, striking the near columns and laying long column shadows across the floor, turquoise light bouncing back off the marble into the shadows. The far depth is almost black-teal. The air is faintly hazy so the depth reads.

CAMERA
Standing eye level, 35mm, straight on, deep focus except for the extreme foreground.

SUBJECT
A young East Asian woman with model features - tall and slim, high cheekbones, a long neck, straight black hair pulled into a low knot with a few loose strands at the temples. She stands in the left half of the frame, her shoulder and back resting against the nearest column, weight on one leg, the other foot crossed over it, both hands in her pockets, her head turned into a clean profile looking off toward the right of frame, chin slightly lifted. Full length, from her shoes to well above her head, with headroom above her.

WARDROBE
An oversized soft rose-pink knitted sweater, slouched at the neck, over wide-legged cream linen trousers that break over white leather sneakers. Fine silver jewellery. Nothing branded, nothing patterned.

KEY DETAIL
A soft dusty-rose leather weekender bag stands on the floor at her feet, leaning against her ankle.

FLOATING KOI - seven, placed deliberately
Seven koi carp hang in the air of the hall as if it were flooded, at clearly different depths and sizes. Placed exactly like this:

In the LEFT half, with the woman:
- two small koi in the upper left, far back in the depth of the hall
- one small koi at middle left, around her elbow height, further back than she is

In the RIGHT half:
- one enormous koi filling the bottom right corner in the extreme foreground, cut by both the right and the bottom edge, head toward the lower left, well out of focus and far larger than anything else in frame
- one large sharply focused koi in the upper right, at the same depth as the woman, swimming toward the left, its whole body inside the right half
- one mid-size koi well inside the right half at hip height, floating just in front of the base of a column
- one mid-size koi higher up between the columns on the right, half veiled by shadow

None of them touches the vertical centre of the frame.

They are pearl-white koi with vivid coral-pink and magenta markings across the back and shoulders, pale undersides, translucent trailing fins and long barbels. Each fish is fully opaque and completely blocks whatever sits behind it; the nearer ones are softer, the far ones veiled by haze. Each casts a soft shadow on the stone below it.

FINISH
Everything is perfectly still - no wind in her clothes or hair. Skin rendered naturally with visible pores and fine texture. Rich saturated colour throughout - turquoise, teal, coral pink, rose and cream, high contrast, punchy, nothing muted or washed out.

DO NOT INCLUDE
No text, no words, no letters, no captions, no logo, no watermark, no signage; no water, no ripples, no bubbles, no splash; no other people; no beige, no brown, no gold, no orange, no travertine, no sandstone, no warm stone; no tile, no glazed surfaces, no swimming pool, no modern building; no muted or desaturated grade, no pastel wash, no faded film look; no transparent or ghosted fish, no fish overlapping flatly, no fish smaller than described in the foreground; no retouching, no skin smoothing, no beautification; no illustration, no painterly effect, no CGI look.
```

### Step 2: Composite Typography

Place a four-line heavy condensed all-caps headline in the clean left quarter, a smaller line of body copy in the right half, and any sponsorship disclosure in a top corner. Export the type-composited 3:2 image as a flat frame. Keep the centerline clear.

### Step 3: Animate the Composite

Use the extracted sequence in [seq.flooded-hall.locked-camera-koi-carousel.md](seq.flooded-hall.locked-camera-koi-carousel.md). Upload the composited image as the opening frame. Do not animate the bare render.

### Step 4: Crop the Carousel Slides

1. Trim the letterbox bars from the finished clip to recover the moving 3:2 picture.
2. Duplicate the clip.
3. Crop one duplicate to the left 3:4 half, hard against the left edge, for slide 1.
4. Crop the other duplicate to the right 3:4 half, hard against the right edge, for slide 2.
5. Confirm the two crops meet at the exact center with no gap or overlap.

## Troubleshooting

- Fish pass through objects: explicitly state they are fully opaque and block everything behind them; forbid passing through columns or the woman.
- Type wobbles: state the shape, weight, color, size, position, and spelling are immutable; forbid warping, duplication, and re-rendering.
- Camera drifts: use "locked on a tripod" and individually prohibit pan, tilt, push, pull, orbit, zoom, reframing, and handheld shake.
- Letterbox bars creep: restate equal pure-black bars as an absolute rule; generate a shorter clip if required.
- Halves do not match: crop exactly at the center or regenerate if camera drift caused the mismatch.
- Scene feels busy: only the koi should have meaningful movement; woman and environment stay rooted.

## Reusable Pattern

Keep the structure, then swap the subject, background, floating element, and lighting. Match motion to the element's actual physics: butterflies beat wings, petals tumble, crystals barely move, and leaves drift irregularly.
