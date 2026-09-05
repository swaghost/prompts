# Full Breakdown - Higgsfield Genjutsu Swap Video

## Overview

An end-to-end workflow for creating a realistic source clip and then changing people, clothing, objects, or locations without rebuilding its motion. Higgsfield Soul 2.0 establishes the photographic look, Seedance 2.5 creates the reference-driven performance, and Genjutsu modifies selected elements while preserving the finished video's movement and edit structure.

## Source

**Creator:** [Maxi Made (@bymaximade)](https://www.instagram.com/bymaximade/)  
**Guide:** [The Full Breakdown - Higgsfield GENJUTSU](https://app.notion.com/p/The-Full-Breakdown-Higgsfield-GENJUTSU-3d143fb2d09c8014b1ebd7445507e391)  
**Tool link supplied by source:** [Higgsfield AI](https://higgsfield.ai/s/viral-ig-v2-bymaximade-nUqJfF)

## Pipeline at a Glance

| Step | Tool                | Result                                                                        |
| ---- | ------------------- | ----------------------------------------------------------------------------- |
| 1    | Higgsfield Soul 2.0 | Base image defining skin, light, composition, and old-camera character        |
| 2    | Seedance 2.5        | Finished video grown from the base image and mapped character references      |
| 3    | Higgsfield Genjutsu | Targeted swaps inside the finished video while preserving its motion and edit |

# Step 1 - Build the Look in Higgsfield Soul 2.0

The look is decided in the image, not in the video. If the base image already resembles a real photograph, downstream motion is more likely to remain photographic.

## Source Image Prompt

```text
Two women framed by a tall open doorway - one in the near foreground at frame right in a pale knit sleeveless top and wide cream linen trousers, standing side-on with hands clasped, looking out; the second further back on the terrace in a lilac shirt and white trousers, leaning against a column facing the camera.

Setting: the threshold of a Mediterranean villa, terracotta tile floor and a weathered white-painted French door in the foreground, a sunlit stone terrace beyond with wicker chairs, a round table and a low wall, flat blue sea and pale sky filling the horizon, soft late-afternoon light.

Shot on an early-2000s point-and-shoot digicam with harsh direct on-camera fill flash that aggressively illuminates the near woman and the doorframe, flattening her features and putting sharp specular highlights on the linen, the door paint and her shoulders; the terrace and sea beyond stay visible but hazy, milky and underexposed relative to the flash.

Warm, slightly saturated CCD tones, strong bloom and halation at the doorway edges, minor digital noise. Candid amateur, Y2K editorial, unpolished but stylized. 4:5.
```

## What Creates the Look

- Name a real camera era and its optical or sensor character instead of relying on generic words such as `cinematic`.
- Name the light source and describe what it hits, flattens, overexposes, or leaves dark.
- Ask for photographic flaws: bloom, halation, noise, hot highlights, haze, uneven exposure, and imperfect grain.
- Treat cleanliness as the tell of synthetic imagery; controlled imperfection makes the image feel captured.

# Step 2 - Build the Motion in Seedance 2.5

Upload the Soul image as the first frame, then upload the identity, daylight-skin, multi-angle, and wardrobe references beside it. Map every reference before describing action.

## Reference Map

```text
=== REFERENCE MAP ===

<<<image_1>>> (villa doorway) -> the villa doorway scene: the woman at frame right, the woman in the lilac shirt out on the terrace, the sea and the low sun beyond. This is the exact first frame of the clip and the room, light and camera look for the whole take.

<<<image_2>>> (George) -> <<<CHARACTER_ID>>> - face and identity. Eyes bare.

<<<image_3>>> (George daylight) -> <<<CHARACTER_ID>>> - identity plus daylight skin tone. The sunglasses in this image are NOT used.

<<<image_4>>> (George sheet) -> <<<CHARACTER_ID>>> - multi-angle character sheet. Head shape, platinum buzzed fade, profile and three-quarter geometry.

<<<image_5>>> (wardrobe) -> wardrobe reference only for <<<CHARACTER_ID>>>: the light blue and white pinstriped shirt with the stiff white contrast collar, the dark burgundy tie with small white dots, and the dark pants. The man, his face, the bed and the room in this image are not used.

=== CHARACTER ELEMENT ===

<<<CHARACTER_ID>>> -> blond man, mid-20s, olive-tan skin, very short platinum-blond buzzed fade, thick dark eyebrows, warm hazel-brown eyes, strong jawline, full lips. Eyes bare, no sunglasses. Identity from <<<image_2>>> / <<<image_3>>> / <<<image_4>>>. Wardrobe from <<<image_5>>>. He does not film and never holds the camera. He comes from the right side of the terrace, from outside, and goes after her to the left.
```

## Complete Seven-Second Video Prompt

```text
PART 1 - SHOT BREAKDOWN

SHOT 1 - one continuous visibly unsteady handheld take, exactly 7 seconds, no cuts before the out-point.

MOMENT 0.0-0.4s - FRAME ZERO
Frame 0.0 is exactly <<<image_1>>>: same room, framing, light, crop, and two women in the same positions. The take grows directly out of it with no settle-in. The near woman is already mid-step at frame right, walking left toward the open doorway while looking back over her right shoulder into the lens. Her clasped hands separate on the first step: her right hand becomes her talking hand; her left hangs and swings naturally.

The woman in the lilac shirt on the terrace turns her head left as if called from off-frame. Her hair moves continuously in the wind while she remains visible. The camera is only a viewpoint, handheld at chest height by an unseen walking operator who cannot keep it steady. The frame continuously drifts, dips, and corrects. The operator never appears and never speaks.

Natural sound: footsteps on terracotta tile, faint sea through the doorway, and a very short room echo.

MOMENT 0.4-2.4s - LINE 1, LATE PAN LEFT, FRAME-EDGE CLIP
She continues left, looks back into the lens, and says in quiet, unbothered American English at natural conversational speed: "No one is telling you how to make your AI look like this,". She sounds as though she is letting the operator in on something, faintly amused rather than selling. Stress NO ONE with a small brow lift and chin tip toward the lens.

On LIKE THIS, her right hand draws one loose circle in front of her, index finger only slightly extended, taking in the door, terrace, and sea. The line remains one flowing phrase without dragged words or gaps. Her eyes land casually on the lens, slide back toward her path before the sentence ends, and she takes a small breath afterward.

She drifts farther left than the camera expects. The camera reacts a beat late and pans left, briefly clipping half her face and shoulder at the left edge. The terrace woman, hair still blowing, walks left and exits. By 2.4 seconds the terrace behind is empty except for chairs, table, sea, and two or three tiny defocused seagulls far over the water. The speaker's hair moves naturally with each step and she blinks once mid-sentence.

Natural sound: her room-distance voice with faint tile echo, both women's footsteps, sea, light wind, and a faint distant door opening somewhere in the house.

MOMENT 2.4-2.9s - TURN BACK, CATCH-UP PAN RIGHT, FOCUS HUNT 1
She turns halfway back and walks right toward the doorway with her front open to the camera at normal pace. Because she has slipped partly out of frame, the operator corrects right to find her. As she returns, autofocus hunts and locks over roughly one second, creating a soft breathing of sharpness across her face and the door. This is silent and purely in-lens.

Natural sound: her steps changing direction, sea, and wind increasing slightly near the opening.

MOMENT 2.9-4.3s - LINE 2, THREE DISTINCT GESTURES, SMALL TILT
Still walking right, she says naturally and continuously: "The skin, light, that old camera look." No long pauses between items.

On THE SKIN, her right hand passes in front of her face, palm toward her, moving across her cheek and past her temple.

On LIGHT, both hands open outward at waist height, palms turning up and away into the room. They present the air and surrounding light, travel away from her body, and never return toward her chest, face, or torso. This is a small offhand gesture, distinct from the earlier circular sweep.

On THAT OLD CAMERA LOOK, her right hand lifts loosely toward the lens and drops again in one open-handed sweep. Fingers remain relaxed together. She does not point, jab, or bring the hand toward herself. A slight smile arrives and her eyes soften, clearly showing affection for the look.

On "light," the camera makes one small handheld tilt toward the light, sea, and sky, then returns immediately. She remains in frame. No zoom, push, whip, smear, snap, or movement sound.

As brighter sky enters the frame, phone auto-exposure meters for it: doorway highlights recover and retain detail, contrast tightens, and the interior sits slightly deeper. This is camera metering, not a change to any light source. The response rolls back gradually as framing returns. Her hair becomes more active near the open door.

Natural sound: voice, steps, sea, stronger doorway wind, and first audible gulls.

MOMENT 4.3-5.1s - CROSS THE THRESHOLD
She reaches and walks through the doorway without stopping, still speaking. Her left hand touches the edge of the white door as she passes. By the last words, "old camera look," she is already outside and moving left along the terrace. Every movement has a visible beginning, middle, and end; nothing starts completed and nobody teleports.

Autofocus hunts and locks on her for roughly one second as she crosses the threshold. This is focus hunt 2 and the final hunt on her.

Phone auto-exposure gradually adapts from interior to daylight. The blown doorway recovers into real sky and sea, terrace stone emerges from glare, her skin and linen settle from hot exposure into daylight tone, contrast re-seats, and the interior behind sinks naturally into shadow. No source light changes, dims, brightens, switches, or fades. The transition is gradual across many frames, never a jump or brightness ramp, and completely silent.

A restrained sun flare crosses the lens from the low sea-side sun: a soft milky wash and faint corner bloom that never fills the frame and passes as framing settles. Outside, the sea wind catches her hair strongly and streams it sideways.

Natural sound: strong constant wind, sea, clear gulls, soft hand contact on the door, and her voice becoming slightly quieter and roomier as she turns seaward.

MOMENT 5.1-5.5s - STEP OUT, TURN RIGHT
The unseen operator follows her through the doorway and takes one step onto the terrace. She continues left. Without cutting, the camera turns slightly right and nearly straightens. This is an ordinary unsteady hand movement at normal speed, not a whip or accelerated swing, with no smear and no attached sound.

MOMENT 5.5-6.7s - CHARACTER CATCH
<<<CHARACTER_ID>>> is already in frame when the camera lands, close in front of the doorway, roughly one metre from the lens. His head, shoulders, chest, arms, and waist fill the frame; he is cut at the waist or upper pants with only a little upper leg visible. Never show him full length.

He has come from the terrace's right side, from outdoors, and is already moving after the woman who went left. He pauses only in passing and speaks almost immediately. Autofocus hunts and catches him over roughly half a second, silently.

He wears the pinstriped shirt, stiff white contrast collar, burgundy dotted tie, and dark pants from the wardrobe reference. His eyes remain bare. Wind moves his collar and loose tie tail.

He looks into the lens and says only: "But I will," with emphasis on I. Use a slight Australian accent: warm, easy, low-key, friendly, unhurried, and quietly certain. He winks with a slight smile, tips his head subtly toward himself, blinks naturally, and makes one small natural hand gesture.

Natural sound: his voice through the same thin phone mic at the same modest level as hers, wind across the microphone, sea, gulls, footsteps on terrace stone, and faint collar rustle.

MOMENT 6.7-7.0s - HARD CUT ON MOTION
He is already moving left again after her. Cut at the instant his next step begins, mid-motion. No trailing beat, settle, hold, fade, or black frame. He never touches or covers the camera.

PART 2 - EFFECTS LIST

Unsteady handheld: continuous from 0.0-7.0 seconds. Constant drift, small dips, late corrections; never still.

Reactive late handheld pans: exactly two. Pan left after her during 0.4-2.4 seconds; catch up right during 2.4-2.9 seconds.

Frame-edge clip: exactly one during line 1.

Small handheld tilt toward light and back: exactly one on "light," with her visible throughout.

Auto-exposure adaptation: exactly two. First while metering brighter sky during the small tilt; second while crossing from interior to daylight. Both are silent gradual sensor responses, never lighting changes.

Autofocus hunt-and-lock on her: exactly two, each about one second. One as she returns after the edge clip and one at the threshold.

Autofocus hunt-and-lock on <<<CHARACTER_ID>>>: exactly one, about half a second when the camera finds him.

Subtle sun flare: exactly one as the camera follows her outdoors.

Handheld step through doorway and slight right turn: exactly one from 5.1-5.5 seconds.

Hard cut on motion: exactly one at the 7.0-second out-point.

Do not use cuts before the out-point, whips, smears, slow motion, speed ramps, digital zoom, punch-ins, stabilization, color grading, added light, changing light, transition effects, whooshes, swishes, shutter sounds, clicks, music, on-screen text, palm-over-lens, camera reversal, or a second line from <<<CHARACTER_ID>>>.

PART 3 - EFFECT DENSITY BY TIME

0.0-2.4s: MEDIUM - late pan left, frame-edge clip, terrace woman's head turn and exit.
2.4-4.3s: MEDIUM - catch-up pan, focus hunt 1, small tilt with exposure metering and return; do not stack these events.
4.3-5.5s: HIGH - focus hunt 2, door contact, interior-to-daylight exposure adaptation, sun flare, wind striking her hair, audio-field change, step-through, and right turn. This is the peak.
5.5-7.0s: LOW - focus catch on <<<CHARACTER_ID>>>, his line, and hard cut on motion.

PART 4 - MOTION FLOW

Opening: real time and already moving. The operator feels half a step behind someone who is not waiting. Camera chases her while the terrace clears.

Build: her left drift and the late pan pull the frame apart; she clips the edge and focus finds her again. Three distinct gestures carry the dialogue. A small tilt admits sky without losing her. Wind increases. She walks through the doorway mid-sentence while exposure re-meters, highlights recover, flare crosses the corner, and wind takes her hair.

Resolution: the camera follows outside, turns right, and catches <<<CHARACTER_ID>>> already close and passing. He does not arrive or pose. Focus catches, he winks and says his single line, then continues left. Cut on his first departing step.

=== HARD RULES ===

Total duration is exactly 7 seconds. One continuous handheld take from first frame to out-point. Frame 0.0 exactly matches <<<image_1>>>. No cuts, scene changes, transitions, time skips, or slow motion before the hard cut at 7.0 seconds.

Skin is never smooth. Preserve visible pores, fine texture, unevenness, tiny marks, and natural sheen. No retouching, waxy skin, plastic skin, beauty filter, or poreless faces.

Use strong visible coarse film grain throughout, heavier in interior shadows but still visible on the terrace.

Handheld movement remains obvious throughout: constant drift, small dips, late corrections, and an imperfect horizon. Every person and camera move has a visible beginning, middle, and end. Nobody teleports and no action begins already completed.

No unnatural camera work: no zoom, punch-in, whip, smear, snap, digital effect, stabilization, or speed change. Every camera move is an ordinary hand movement at ordinary speed.

NO LIGHT IN THIS SCENE EVER CHANGES. Exposure and contrast changes are only silent phone auto-exposure responses to frame content. No lamp, sun, flash, or source brightens, dims, switches, fires, or pulses. No shutter, click, beep, flash frame, or UI sound.

The only allowed in-lens behavior is exactly two silent autofocus hunts on her, one silent half-second hunt on <<<CHARACTER_ID>>>, two gradual auto-exposure responses, and one subtle outdoor sun flare.

The camera device and operator are never visible. The operator never speaks. She holds nothing. <<<CHARACTER_ID>>> never films, touches the camera, or covers the lens.

<<<CHARACTER_ID>>> appears only after the right turn at 5.5 seconds, close at roughly one metre, framed head to waist. He comes from terrace right and follows her left. His legs are never fully visible.

Wind increases continuously toward the doorway and becomes strong outdoors. The terrace woman's hair moves throughout her appearance. Seagulls become audible near the doorway and remain tiny and defocused over the sea.

Keep the hard on-camera fill active and unchanged for the whole take. Surfaces it reaches run slightly hot; untouched areas remain darker. Outside, daylight is much brighter, so the same flash reads only as weak fill. Keep terrace, sky, and sea slightly hazy and milky.

The look is candid, amateur, and unpolished, straight from a phone gallery. No added color grade, cinematic polish, text, or music.

She never performs for the camera or stays centered. Her body keeps its own rhythm; eye contact lands casually and drifts away. Preserve natural blinks, breaths, mouth movement, and brow life between words. Both lines flow at conversational speed and finish early rather than late.

Her three gestures stay distinct and never point toward her body: circular one-hand view sweep on "like this"; low two-handed outward opening on "light"; loose open-hand lift toward the lens on "that old camera look." Her right hand talks; her left touches the door. Never swap roles.

The terrace woman turns left, exits left before 2.4 seconds, never returns, never gestures, and never looks at camera.

Dialogue occurs exactly once in this order with no additions or repeats: "No one is telling you how to make your AI look like this," / "The skin, light, that old camera look." / "But I will,". The first two lines belong to her; the final line belongs to <<<CHARACTER_ID>>>.

<<<CHARACTER_ID>>> has bare eyes, platinum buzzed fade from identity references, and only the specified pinstriped shirt, white contrast collar, burgundy dotted tie, and dark pants from the wardrobe reference. Nothing else from the wardrobe image transfers.

End exactly when <<<CHARACTER_ID>>> starts moving left after her. No beat afterward.

=== AUDIO ===

Use raw, unprocessed external phone-mic sound: thin, slightly boxy, light auto-gain pumping, handling noise, wind hitting the microphone near and outside the doorway, no denoising or polish. No music, designed sound effects, narrator, or on-screen text. Camera movement, focus hunts, and exposure adaptation are silent.

Her voice remains at room distance with faint short room echo, becomes slightly quieter and roomier toward the sea, and becomes clearer when her face turns to the lens. His voice uses the same phone mic, modest level, and wind contamination, never becoming close-mic or sharper than hers.

Sound palette: sea below the terrace; growing wind; gulls near the doorway; her terracotta-tile steps; the other woman's fading terrace steps; his terrace steps; her hand touching the door; faint short indoor echo; and one distant door opening faintly in the middle.

=== VOICE ===

Her voice: quiet, silky American accent, relaxed and unbothered, speaking to the operator rather than an audience. Natural tempo, one flowing phrase per line, small breaths, occasional fry at phrase ends, and one or two natural mouth clicks. Line 1 carries amused confidentiality; line 2 is matter-of-fact inventory that becomes fond on the final words.

His voice: slight Australian accent, natural, friendly, easy grin, quiet certainty, emphasis on "I," carried by the wink. Same raw phone-mic character and modest level as hers.
```

## Three Seedance Rules That Make or Break the Clip

1. Map every reference first and state its sole purpose: first frame, identity, daylight skin tone, multi-angle geometry, or wardrobe.
2. Explicitly state that frame 0 is the source image with the same room, framing, light, and crop, and that motion grows from it.
3. End with hard rules covering duration, cuts, skin texture, grain, dialogue, camera prohibitions, and non-transferable reference content.

# Step 3 - Change Anything in Higgsfield Genjutsu

Genjutsu operates on finished footage. It can preserve camera motion, VFX, particles, simulations, masks, roto, occlusion order, cut points, pacing, character continuity across cuts, grain, lens character, flares, color imperfections, and mixed frame rates while changing only instructed elements.

## Mode 1 - Object Swaps

Upload the finished video and reference images for the replacement elements. Write one short sentence per change and close each instruction by protecting everything else.

### Clothing Swap

```text
Replace the clothing on the guy sitting in the chair in @Video 1 with this clothing from @Image 2, keep everything else the same.

Replace the clothing on the girl in the background in @Video 1 with this clothing from @Image 2, keep everything else the same.
```

### Background or Location Swap

```text
Replace the location and background in this <<<video_1>>> with the location and background from the <<<image_1>>> (city, buildings...). Keep everything else the same.
```

## Mode 2 - Motion Transfer

Take motion from an existing video and rebuild it with new characters, locations, or products. Preserve the source moves, timing, and camera while changing the world.

```text
Replace the guy from the video with the guy from @Image 1, @Image 2, @Image 3, @Image 4, @Image 5, @Image 6 - the main look and aesthetic for him should be like in @Image 4, @Image 5, @Image 6. The clothing he is wearing is the same clothing as in @Image 7 and @Image 4, @Image 5, @Image 6.

Replace the girl from the video with the girl in @Image 8, @Image 9, @Image 10, @Image 11, @Image 12, @Image 13, @Image 14. The main aesthetic and look for that girl are like in @Image 10, @Image 11, @Image 12, @Image 13, @Image 14.

Replace the locations from the video with the locations in @Image 15, @Image 16, @Image 17.

Keep the same aesthetic throughout the entire video as in @Image 4, @Image 5, @Image 6, @Image 10, @Image 11, @Image 12, @Image 13, @Image 14.
```

## How to Write a Genjutsu Prompt

- Short prompts win. Describe a change, not a new scene.
- Say what changes and then explicitly say what stays. `Keep everything else the same` protects the finished footage.
- Identify an element by visible frame location and state: `the guy sitting in the chair`, `the girl in the background`, or `the bottom-left corner`.
- Label references by exact upload order: `@Video 1`, `@Image 1`, `@Image 2`.
- Use one change per sentence. Two swaps require two sentences.
- Assign each reference a clear role and do not transfer unwanted people, rooms, props, sunglasses, or wardrobe from it.

## What Genjutsu Should Preserve

- Camera motion, including fast or unstable movement
- VFX, particles, simulations, and composited elements
- Masks, rotoscoping, occlusions, and layer order
- Existing cut points, timing, pacing, and edit rhythm
- The same replacement identity across every cut
- Grain, lens look, flares, and color imperfections
- Mixed frame rates rather than flattening the source cadence

## Applications

- Turn one video into a campaign with different products, people, settings, or languages.
- Replace outfits and backgrounds without reshooting.
- Apply client changes after picture lock without reopening production.
- Recast one product video with multiple models.
- Rebuild a trend, advertisement, or scene using owned characters and locations while retaining source motion.

## Swap Quality Checklist

- [ ] The driving video is finished before Genjutsu edits begin.
- [ ] Every reference is named in exact upload order.
- [ ] Each sentence requests only one clearly located change.
- [ ] Each swap instruction states what must remain unchanged.
- [ ] New identities remain stable through profiles, occlusions, motion blur, and cuts.
- [ ] Clothing follows the body with natural folds and no color drift.
- [ ] Products remain correctly scaled, gripped, lit, reflected, and labelled.
- [ ] Replacement locations preserve camera paths, masks, occlusions, and contact shadows.
- [ ] Original cuts, timing, pacing, VFX, grain, lens character, and frame-rate changes remain intact.
- [ ] No original identity, object, wardrobe, or background ghosts through the replacement.

## Related Guide

See [Genjutsu Motion Transfer Prompt Pack](INDEX.genjutsu-motion-transfer-pack.md) for ten reusable recast and object-swap variants.
