# The Flooded Hall Koi Carousel Guide

## Overview

**Effect**: A seamless two-slide carousel made from one wide animated frame.
**Platform**: Adobe Firefly
**Format**: One horizontal 3:2 image and animation, cut into two 3:4 slides
**Motion**: A single foreground koi swims across a static flooded hall
**Source**: Phil Franco, Adobe Firefly Ambassador

This guide creates a carousel that reads like one camera move across a single room. Slides 1 and 2 are not separate designs: they are the left and right halves of the same wide frame. Generate wide, animate wide, then cut once at the very end.

The remaining carousel slides can be text slides built on the same visual world. The shared environment makes the set feel like one shoot rather than unrelated exports.

## The System

The order is important:

1. Generate one wide 3:2 still.
2. Composite the headline and secondary copy onto that still.
3. Animate the finished composite as one continuous wide shot.
4. Remove the letterbox bars.
5. Duplicate the clip and crop the copies into matching 3:4 left and right halves.
6. Upload the left half first and the right half second.

Do not generate or animate the halves separately. The marble, light, fish, lettering, and motion will not match across the seam.

## Three Rules That Make the Cut Work

### 1. Keep the Centre Line Empty

The frame is sliced down the exact vertical centre. Nothing important may sit on that line: no fish, limb, column edge, or other subject. An object crossing the centre will be split between slides and destroy the illusion.

### 2. Make Each Half Stand Alone

The left half needs a subject and the right half needs its own subject and depth. Place the woman about one third of the way across the left half rather than directly in the centre. Give the right half its own koi, column depth, and visual focus.

### 3. Add Type Before Animation

Composite the headline and secondary line onto the still before sending it to the video model. This gives the model a finished opening frame and allows a foreground koi to pass in front of the lettering. Adding type after animation makes it look pasted over the moving image.

Leave the left quarter of the wide frame as clean, unbroken surface for the headline. Strong marble veining in that area will compete with the type.

## Step 01: Generate the Wide Image

Set Adobe Firefly Image settings to:

- **Aspect ratio**: Wide, 3:2
- **Quality**: High
- **Text in image**: None
- **Attempts**: Generate four or five variations

Choose the version where the left quarter is genuinely clean, the centre line is empty, and the foreground koi is genuinely huge. Two out of three is not enough for a clean cut.

### Image Prompt

```text
One horizontal frame, 3:2 landscape. Photorealistic, shot on a full-frame camera. No text anywhere in the image.

COMPOSITION
The frame will later be cut in half down the exact vertical centre, and each half has to stand on its own. Place the woman in the LEFT half, about a third of the way across. Leave the leftmost quarter of the frame as clean unbroken marble. The RIGHT half holds the hall receding between columns with its own koi and its own open depth. Nothing important crosses the vertical centre line: no fish, no limb, no column edge sitting on it.

SCENE
The interior of a vast empty stone hall. A row of massive round columns recedes into depth across the frame, cut from cool turquoise-grey marble veined with dusty rose, their surfaces worn and softly polished by age. The nearest column stands immediately behind the woman, thick enough to fill that part of the frame, cropped by the top edge, its round base sitting on the floor beside her. Behind it the hall recedes into deep saturated teal shadow between further columns. The floor is worn stone in the same cool turquoise-grey, faintly reflective. Hard daylight cuts in low from the left through an opening out of frame, striking the near columns and laying long column shadows across the floor, turquoise light bouncing back off the marble into the shadows. The far depth is almost black-teal. The air is faintly hazy so the depth reads.

CAMERA
Standing eye level, 35mm, straight on, deep focus except for the extreme foreground.

SUBJECT
A young East Asian woman with model features, tall and slim, high cheekbones, a long neck, straight black hair pulled into a low knot with a few loose strands at the temples. She stands in the left half of the frame, her shoulder and back resting against the nearest column, weight on one leg, the other foot crossed over it, both hands in her pockets, her head turned into a clean profile looking off toward the right of frame, chin slightly lifted. Full length, from her shoes to well above her head, with headroom above her.

WARDROBE
An oversized soft rose-pink knitted sweater, slouched at the neck, over wide-legged cream linen trousers that break over white leather sneakers. Fine silver jewellery. Nothing branded, nothing patterned.

KEY DETAIL
A soft dusty-rose leather weekender bag stands on the floor at her feet, leaning against her ankle.

FLOATING KOI
Seven pearl-white koi carp hang in the air of the hall as if it were flooded, at clearly different depths and sizes. In the LEFT half: two small koi in the upper left, far back in the depth of the hall; one small koi at middle left around the woman's elbow height, further back than she is. In the RIGHT half: one enormous koi filling the bottom right corner in the extreme foreground, cut by both the right and bottom edge, head toward the lower left, well out of focus and far larger than anything else; one large sharply focused koi in the upper right at the same depth as the woman, swimming toward the left, its whole body inside the right half; one mid-size koi well inside the right half at hip height, floating just in front of the base of a column; one mid-size koi higher up between the columns on the right, half veiled by shadow. None touches the vertical centre of the frame.

The koi have vivid coral-pink and magenta markings across the back and shoulders, pale undersides, translucent trailing fins, and long barbels. Each fish is fully opaque and completely blocks whatever sits behind it. Nearer fish are softer; far fish are veiled by haze. Each casts a soft shadow on the stone below it.

FINISH
Everything is perfectly still: no wind in her clothes or hair. Skin rendered naturally with visible pores and fine texture. Rich saturated colour throughout: turquoise, teal, coral pink, rose, and cream. High contrast, punchy, nothing muted or washed out.

DO NOT INCLUDE
No text, words, letters, captions, logo, watermark, or signage; no water, ripples, bubbles, or splash; no other people; no beige, brown, gold, orange, travertine, sandstone, or warm stone; no tile, glazed surfaces, swimming pool, or modern building; no muted or desaturated grade, pastel wash, or faded film look; no transparent or ghosted fish; no fish overlapping flatly; no fish smaller than described in the foreground; no retouching, skin smoothing, or beautification; no illustration, painterly effect, or CGI look.
```

## Step 02: Lay on the Type

Open the selected 3:2 still in the tool used for compositing type.

- Put the main headline in the clean left quarter.
- Use four short lines in heavy condensed capitals, ranged left.
- Put one smaller line somewhere in the right half so slide 2 has a reason to exist.
- Add the sponsorship disclosure now if the post is sponsored.
- Keep the exact vertical centre line empty.
- Export the finished composite as a flat image.

Example cover treatment:

```text
THE
FLOODED
HALL
```

The composited image, rather than the bare render, becomes the opening frame for video generation.

## Step 03: Animate the Composite

Load the composited frame as the opening frame. Use these settings:

- **Duration**: 6 seconds
- **Orientation**: Landscape
- **Resolution**: 1080p
- **Frame rate**: 24 fps
- **Audio**: Off
- **Cuts**: None

### Video Prompt

```text
6 seconds, landscape, one continuous shot, no cuts. Photorealistic live-action, rich saturated teal and coral colour, cinematic. The opening frame is the reference image: the hall, columns, woman, koi, letterboxing, and lettering all continue exactly from it.

LETTERBOX RULE, ABSOLUTE
The picture is letterboxed inside the canvas. A solid pure black bar runs across the top and another across the bottom, each holding exactly the same height, the same straight horizontal edges, and the same pure black for every frame. The bars are empty and dead: no fish, fin, light spill, reflection, haze, or motion ever enters them or crosses their edge. The picture area between them keeps its exact original scale and position. It is never stretched, squeezed, zoomed, cropped, or shifted inside the canvas.

CAMERA RULE, ABSOLUTE
The camera is locked on a tripod and never moves. Identical framing, angle, distance, and lens from the first frame to the last. No pan, tilt, push, pull, orbit, zoom, reframing, handheld drift, or parallax shift of the columns.

TEXT RULE, ABSOLUTE
The lettering in the opening frame is painted into the image. Every letter of the large headline on the left and of the two smaller lines holds its exact shape, weight, colour, size, position, and spelling for the whole clip. The lettering never moves, warps, wobbles, duplicates, re-renders, brightens, or fades.

FOREGROUND RULE, ABSOLUTE
The huge koi in the lower right corner is the closest object to the lens, far closer than anything else in the hall. It is enormous, soft, out of focus, and completely solid. Whatever it passes over is hidden behind it while it is there: the marble floor, column base, bag, woman's legs, and large pale headline all disappear under its body as it crosses and reappear untouched once it has gone.

SUBJECT RULE, ABSOLUTE
The woman stays exactly where she is for the whole clip: the same lean against the column, the same weight on the same leg, both hands in her pockets, the same profile head angle, eyeline off to the right, and calm expression. She is alive but rooted. Her chest rises and falls with slow deep breathing, her shoulders settle with it, she blinks slowly twice, and the loose strands at her temples and hem of her sweater drift as if the hall were flooded with still water. Her feet never move.

TIMING
0-1 seconds: The koi already in frame glide slowly forward through the hall, bodies undulating from head to tail, pectoral fins sculling, dorsal fins flexing, and barbels trailing. Their reflections stretch and shimmer across the wet marble floor. The woman breathes and blinks once.

1-4 seconds: The huge foreground koi swims steadily from the right edge all the way to the left edge, holding a low horizontal path across the lower half of the picture. It crosses in front of the bag, in front of the woman's legs, and then travels straight through the area where the headline sits. Its enormous blurred body fills that part of the screen and blocks the letters underneath it until its tail clears the left edge.

4-5 seconds: The picture is fully revealed again, the headline whole and unchanged. The mid-right koi turns gently and drifts deeper between the columns. The small koi at upper left continue their slow crossing. The woman blinks a second time.

5-6 seconds: The koi settle back into a sparse spread close to the opening frame. The woman is still leaning exactly as she started, and the shot holds steady.

PHYSICAL RULES
The koi move as they would in water: slow, weighted, continuous undulation through the whole body, never rigidly and never flapping like wings. Their fins are translucent and flutter softly at the trailing edges. The huge foreground koi stays heavily out of focus for its whole pass; its scales remain smeared and soft, and the shallow depth of field never resolves it. The light stays exactly as in the opening frame: one cool source from the left, unchanged in direction, intensity, and colour. The colour grade stays saturated. The marble, sweater knit, linen trousers, and leather bag keep their original texture and colour.
```

### Negative Prompt

```text
No stretching, squeezing, or rescaling of the picture area; no content entering the black bars; no bars changing height, turning grey or transparent, or disappearing; no camera movement, zoom, pan, tilt, reframing, or handheld shake; no cuts, shot changes, or dissolves; no warping, wobbling, duplicated, or misspelled letters; no drifting or fading type; no letters drawn on top of the large koi; no walking, stepping, turning, hands leaving pockets, gestures, expression change, or head turn toward the lens; no transparent or ghosted fish; no fish sinking behind the floor, passing through columns, passing through the woman, or flat overlapping; no water surface, bubbles, splash, or flooding of the room; no colour shift, desaturation, or fade to black; no new people or objects; no music, background music, library audio, musical instruments, rhythmic beat, orchestral swell, subtitles, watermark, or logo.
```

### Why the Letterbox Is Deliberate

The model may prefer its own aspect ratio while the source image is 3:2. Letterboxing the picture inside the canvas prevents the model from cropping or stretching it. Forbid the bars from moving, then crop them away after generation. If the bars still creep, try a shorter four-second generation.

## Step 04: Make the Cut

No desktop editor is required; any crop tool that supports exact dimensions will work.

1. Crop away the black bars from the top and bottom to restore the clean 3:2 moving picture.
2. Duplicate the same clip so both copies are identical.
3. Crop one copy to 3:4, hard against the left edge. Export as slide 1.
4. Crop the other copy to 3:4, hard against the right edge. Export as slide 2.
5. Confirm the crops meet at the exact centre, with no overlap and no gap.
6. Upload the left crop first and the right crop second.

Zoom in on the seam before posting. A few pixels of overlap can make the koi appear twice; a few pixels of gap can make the room jump.

## Troubleshooting

### Fish Pass Through Columns

The depth instruction is too weak. Repeat that each fish is fully opaque and completely blocks whatever sits behind it. Add `no fish passing through columns or through the woman` to the negative prompt.

### The Letters Wobble

The model is re-rendering the type. Give the lettering its own absolute rule covering shape, weight, colour, size, position, and spelling. Explicitly forbid warping, duplication, and re-rendering.

### The Camera Drifts

A motion word elsewhere in the prompt may be giving the model permission to move. Use `locked on a tripod` and list every banned movement individually: pan, tilt, push, pull, orbit, and zoom. Regenerate if the columns shift.

### The Bars Creep

Restate the letterbox rule with `absolute`, `pure black`, and `equal heights`. Forbid anything entering the bars. If the problem persists, generate a shorter clip.

### The Halves Do Not Match

Re-crop at the exact centre and check for overlap or a gap. If the seam still moves, the camera drifted during generation. Regenerate rather than trying to patch the two clips.

### The Woman Moves Too Much

Name every part that must remain still: face, eyes, hair, clothing, body, hands, bag, and feet. Permit only slow breathing and two blinks.

### The Clip Feels Busy

Reduce the motion to one moving element. A single element moving through a frozen room feels cinematic; several moving elements feel noisy.

## Adapt the Structure

The koi are interchangeable. Keep the structure and change one column at a time so you can see what changes the result.

| Column           | Variations                                  |
| ---------------- | ------------------------------------------- |
| Subject          | Woman, queen, fairy, mermaid, princess      |
| Background       | Palace, forest, library, beach, mountains   |
| Floating element | Koi, butterflies, flowers, leaves, crystals |
| Lighting         | Golden hour, moonlight, candlelight, studio |

### Variations That Fit the System

1. Floating koi in a marble palace
2. Golden butterflies around a queen
3. Cherry blossom drifting through a still hall
4. Crystal shards floating in a fantasy world
5. Autumn leaves moving through a cinematic forest

Keep the physics honest. Butterflies beat their wings, petals tumble and stall, and crystals barely move. A leaf that swims like a fish will look wrong.

## Quick Reference Checklist

- [ ] Generate one 3:2 horizontal frame.
- [ ] Keep the left quarter clean for the headline.
- [ ] Keep the exact centre line empty.
- [ ] Give each half its own subject and depth.
- [ ] Composite all type before animation.
- [ ] Animate the finished composite as one wide shot.
- [ ] Lock the camera on a tripod.
- [ ] Animate only one primary element.
- [ ] Keep the letterbox bars pure black, equal, and static.
- [ ] Remove the bars before cropping.
- [ ] Crop two identical clips at the exact centre into 3:4 halves.
- [ ] Upload the left half before the right half.
- [ ] Check the seam at high zoom.

## Remember These Three Things

1. **Keep the camera static.** Every drift reads as an error; stillness reads as control.
2. **Animate only one element.** One thing moving in a frozen room is a photograph that came alive.
3. **Generate wide, cut once.** The seam is invisible because there never was one.

**Made in Adobe Firefly**: firefly.adobe.com

**Creator credit**: Phil Franco | Adobe Firefly Ambassador | @ai.withphil

**Disclosure**: This guide is based on a paid partnership with Adobe. Use appropriate sponsorship disclosure when publishing sponsored work.
