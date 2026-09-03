# Flooded Hall Locked-Camera Koi Carousel Sequence

## Classification

**Product Category:** Editorial carousel cover animation

**Reveal Effect:** Foreground occlusion across fixed typography

**Reveal Mechanism:** A huge foreground koi crosses a fixed, type-composited horizontal scene, temporarily blocking the subject and headline before revealing them unchanged

**Sequence Type:** Reference-match locked-camera sequence

**Filename:** `seq.flooded-hall.locked-camera-koi-carousel.md`

## Description of Resulting Video or Video Sequence

A six-second landscape animation for a two-slide carousel made by splitting one 3:2 master frame into left and right 3:4 crops. The locked camera, immutable typography, static subject, and weighted koi movement preserve an invisible seam between both slides.

## Usage

Use after creating a 3:2 Flooded Hall still and compositing headline and body copy onto it. Generate the full-width animation first, remove its temporary letterbox bars, then crop the same clip into left and right 3:4 carousel slides.

## Engines/Models

- Adobe Firefly Video
- Other image-to-video models capable of opening-frame reference matching and static-camera control

## Prerequisites / Dependencies

- Dependency #1 - A composited 3:2 horizontal opening frame containing the hall, woman, seven koi, letterbox treatment, and finalized typography
- The frame must have an empty vertical centerline and both carousel halves must work as standalone compositions

## Storyboard Prompt

**Panel 1 (0:00-0:01):** Locked wide view. The woman remains rooted against the left column; koi glide forward through the hall. The left text and right text remain completely fixed.

**Panel 2 (0:01-0:04):** The enormous soft-focus koi moves from the right edge to the left edge across the lower picture, passing in front of the bag, woman, and headline.

**Panel 3 (0:04-0:05):** With the foreground koi cleared, the original lettering is whole and unchanged. The mid-right koi turns gently deeper between columns; the woman blinks again.

**Panel 4 (0:05-0:06):** Koi settle back toward the opening distribution while the camera and every static element hold exactly.

Style: Photorealistic live-action editorial image, rich saturated teal and coral, landscape, camera locked on a tripod, static 3:2 composition inside immutable pure-black letterbox bars.

## Video Prompt

```text
6 seconds, landscape, one continuous shot, no cuts.
Photorealistic live-action, rich saturated teal and coral colour, cinematic.
The opening frame is the reference image - the hall, the columns, the woman, the koi, the letterboxing and the lettering all continue exactly from it.

LETTERBOX RULE, ABSOLUTE
The picture is letterboxed inside the canvas. A solid pure black bar runs across the top and another across the bottom, each holding exactly the same height, the same straight horizontal edges and the same pure black for every frame of the clip. The bars are empty and dead - no fish, no fin, no light spill, no reflection, no haze and no motion of any kind ever enters them or crosses their edge. The picture area between them keeps its exact original scale and position: it is never stretched, squeezed, zoomed, cropped or shifted inside the canvas.

CAMERA RULE, ABSOLUTE
The camera is locked on a tripod and never moves. Identical framing, identical angle, identical distance and identical lens from the first frame to the last. No pan, no tilt, no push, no pull, no orbit, no zoom, no reframing, no handheld drift, no parallax shift of the columns.

TEXT RULE, ABSOLUTE
The lettering in the opening frame is painted into the image. Every letter of the large headline on the left and of the two smaller lines holds its exact shape, weight, colour, size, position and spelling for the whole clip. The lettering never moves, never warps, never wobbles, never duplicates, never re-renders, never brightens and never fades.

FOREGROUND RULE, ABSOLUTE
The huge koi in the lower right corner is the closest object to the lens, far closer than anything else in the hall. It is enormous, soft and out of focus, and it is completely solid. Whatever it passes over is hidden behind it while it is there - the marble floor, the column base, the bag, the woman's legs and the large pale headline on the left of frame all disappear under its body as it crosses, and reappear untouched once it has gone.

SUBJECT RULE, ABSOLUTE
The woman stays exactly where she is for the whole clip. The same lean against the column, the same weight on the same leg, both hands staying in her pockets, the same profile head angle, the same eyeline off to the right, the same calm expression. She is alive but rooted: her chest rises and falls with slow deep breathing, her shoulders settle with it, she blinks slowly twice, and the loose strands at her temples and the hem of her sweater drift as if the hall were flooded with still water. Her feet never move.

0-1s
The koi already in frame glide slowly forward through the hall, bodies undulating from head to tail, pectoral fins sculling, dorsal fins flexing, barbels trailing behind their mouths. Their reflections stretch and shimmer across the wet marble floor. The woman breathes and blinks once.

1-4s
The huge foreground koi swims steadily from the right edge of frame all the way to the left edge, holding a low horizontal path across the lower half of the picture. It crosses in front of the bag, in front of the woman's legs, and then travels straight through the area where the headline sits, its enormous blurred body filling that part of the screen and blocking the letters underneath it, until its tail finally clears the left edge of frame.

4-5s
The picture is fully revealed again, the headline whole and unchanged. The mid-right koi turns gently and drifts deeper between the columns; the small koi at the upper left continue their slow crossing. The woman blinks a second time.

5-6s
The koi settle back into a sparse spread close to the opening frame, the woman still leaning exactly as she started, and the shot holds steady.

PHYSICAL RULES
The koi move as they would in water - slow, weighted, continuous undulation through the whole body, never gliding rigidly and never flapping like wings. Their fins are translucent and flutter softly at the trailing edges. The huge foreground koi stays heavily out of focus for its whole pass, its scales smeared and soft, the shallow depth of field never resolving it. The light stays exactly as in the opening frame, one cool source from the left, unchanged in direction, intensity and colour for the whole clip. The colour grade stays exactly as saturated as the opening frame. The marble, the sweater knit, the linen trousers and the leather bag all keep their original texture and colour.

NEGATIVE PROMPT
No stretching, squeezing or rescaling of the picture area; no content entering the black bars, no bars changing height, no bars turning grey or transparent, no bars disappearing; no camera movement, no zoom, no pan, no tilt, no reframing, no handheld shake; no cuts, no shot changes, no dissolves; no warping, wobbling, duplicated or misspelled letters, no drifting or fading type, no letters drawn on top of the large koi; no walking, no stepping, no turning, no hands leaving the pockets, no gesture, no change of expression, no head turn toward the lens; no transparent or ghosted fish, no fish sinking behind the floor, no fish passing through columns or through the woman, no flat overlapping; no water surface, no bubbles, no splash, no flooding of the room; no colour shift, no desaturation, no fade to black; no new people or objects entering frame; no music, no background music, no library audio, no musical instruments, no rhythmic beat, no orchestral swell, no subtitles; no watermark, no logo.
```

**Duration:** 6 seconds. Landscape, 1080p, 24 fps, audio off.

**Style:** Photorealistic live-action, rich saturated teal and coral, cinematic editorial composition.

**Camera:** Locked tripod. No camera movement whatsoever.

**Lighting:** One cool source from the left, unchanged in direction, intensity, or colour.

**Quality/Technical Requirements:** Animate the already type-composited opening frame. Preserve every text character, the picture area, bars, subject, interior geometry, material texture, and exact camera framing. After generation, crop off the letterbox bars, then make exact left and right 3:4 crops from duplicated copies of this same clip.
