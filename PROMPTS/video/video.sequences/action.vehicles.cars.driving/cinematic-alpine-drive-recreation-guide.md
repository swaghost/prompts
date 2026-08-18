# Cinematic Alpine Drive - Video Recreation Guide

## Description

Create a moody, cinematic automotive-lifestyle short film featuring a young woman driving a white supercar solo through misty alpine passes, culminating in an emotional reunion at a luxury mountain chalet at dusk. The complete 45-second piece is assembled from 17 carefully choreographed Seedance 2.0 clips with consistent character and vehicle identity throughout.

## Overview

This workflow guide provides a systematic approach to generating a professional-quality cinematic automotive narrative using AI video generation. The story progresses from solitary alpine driving through winding roads, tunnels, and fog-shrouded passes, transitions into reflective nature moments with wildflowers, and concludes with a warm emotional reunion as golden hour light bathes the scene.

**Technical Platform:**

- **AI Platform**: Vosu AI
- **Model**: Seedance 2.0
- **Target Duration**: ~45 seconds
- **Resolution**: 4K
- **Aspect Ratio**: 16:9 (final delivery), 2.39:1 letterbox
- **Shot Count**: 17 clips

## Step 1: Prepare Your Consistency Anchors

Before generating any video, lock down two reference images. These are what keep the woman's face and the car from drifting across 17 separate clips—Seedance 2.0's strength is elite character consistency and motion cloning, but only if you feed it the same references every time.

### Portrait Reference

**Requirements:**

- One clean, well-lit, front-facing image of the woman
- Mid-20s age appearance
- Long wavy blonde hair
- Visible freckles
- Natural makeup
- Tailored white coat
- Neutral expression

### Car Reference

**Requirements:**

- One clean side/three-quarter image of the white two-seat mid-engine supercar
- Glossy wet bodywork
- Black five-spoke wheels
- Clear, unobstructed view

**Workflow:**

1. Generate these stills first in Midjourney, Flux, or your usual image generation tool
2. Keep them in a dedicated project folder
3. Re-upload the matching reference for every shot in Steps 4–5

## Step 2: Set Up the Vosu AI Dashboard

### Initial Configuration

1. Log into Vosu AI and open the Video Generation dashboard
2. Select **Seedance 2.0** from the model list
3. Set your global defaults once so every clip matches:
   - **Aspect Ratio**: 16:9
   - **Resolution**: 1080p
   - **Duration**: 5s (you'll trim/retime later)
   - **Output Count**: 2–4 per shot

### Consistency Protocol

- Keep these settings constant across all 17 shots for uniform look
- Work **image-to-video**: Upload the matching reference as the main image, then paste the prompt

## Step 3: Lock the Master Look

Append this style block to every prompt so the lens and grade stay identical across all clips. Save it in Vosu's PromptGPT as a reusable template so it auto-attaches.

### Global Style Suffix

**Append to Every Shot:**

```
Cinematic automotive lifestyle film, anamorphic 2.39:1 widescreen, shallow depth of field, moody overcast alpine light warming toward golden dusk, desaturated teal-grey-green grade, drifting fog and mist, wet reflective roads, fine 35mm film grain, natural photorealistic color, 4K.
```

### Consistency Anchors

**Include in Matching Shots:**

- **Woman**: Same young woman, mid-20s, long wavy blonde hair, light freckles, natural makeup, tailored white coat—lock identity to the reference image, no face morphing
- **Car**: Same sleek white two-seat mid-engine supercar, glossy wet bodywork, black five-spoke wheels

## Step 4: Shot-by-Shot Generation

Generate in order. For each shot, upload the reference noted in the Setup column, paste the prompt (with the global suffix appended), and generate 2–4 takes. Shots 1–11 cover the drive and detail beats; shots 12–17 cover the nature and emotional beats.

### Shot 1: Hands on Steering Wheel

**Setup:** 2s · Car interior ref · low motion

**Prompt:**

```
Close-up inside the cabin of a luxury supercar on a woman's elegant hands resting on a black leather sports steering wheel, delicate silver watch, crisp white blazer cuff, soft ambient dashboard glow, small deliberate steering adjustments, static locked-off camera, shallow focus, intimate warm cabin light.
```

---

### Shot 2: High Heel on Accelerator

**Setup:** 2s · Car interior ref · low motion

**Prompt:**

```
Extreme macro close-up of a white high heel slowly and deliberately pressing the accelerator pedal in a premium car footwell, brushed-aluminium pedals catching a faint reflection, low warm interior light, fully static camera, razor-thin depth of field with only the shoe and pedal sharp.
```

---

### Shot 3: Aerial Hairpin Bend

**Setup:** 3s · Car ref · high motion

**Prompt:**

```
Sweeping cinematic aerial drone shot high above a wet mountain pass, a lone white supercar carving through a tight hairpin bend, a vivid turquoise glacial lake far below ringed by steep green slopes, low clouds clinging to the peaks, camera slowly cranes and tracks the car from above revealing epic alpine scale.
```

---

### Shot 4: Front Wheel Detail

**Setup:** 2s · Car ref · high motion

**Prompt:**

```
Low-angle tracking close-up of the white supercar's front wheel spinning fast on glistening wet tarmac, a fine veil of water spray misting off the tyre, the road reflecting the grey sky, fog behind, camera skims low and fast alongside the moving wheel with subtle motion blur.
```

---

### Shot 5: Car Approaching Through Mist

**Setup:** 2s · Car ref · medium motion

**Prompt:**

```
Wide static cinematic shot of the white supercar driving straight toward camera along a misty rain-soaked mountain road, headlights glowing and reflecting across the wet asphalt, a rocky fog-shrouded slope behind, the car steadily approaches, grows in frame, then sweeps past the lens through heavy atmospheric haze.
```

---

### Shot 6: Mirror Reflection Portrait

**Setup:** 2s · Portrait ref · low motion

**Prompt:**

```
Close-up of the blonde driver's face reflected in the car's side wing mirror with raindrops scattered across the mirror glass, blurred green landscape rushing past behind the reflection, a subtle turn of her head with calm focused eyes, gentle handheld micro-shake, shallow focus on the reflection.
```

---

### Shot 7: Hood-Mounted POV

**Setup:** 2s · Car ref · high motion

**Prompt:**

```
Hood-mounted POV looking down a wet mountain road lined with roadside marker poles flicking past on either side, fog softening the distance ahead, the road rushing smoothly beneath the camera at speed, overcast desaturated light, wet sheen on the asphalt, strong feeling of forward motion and quiet isolation.
```

---

### Shot 8: Epic Valley Aerial

**Setup:** 3s · Car ref · high motion

**Prompt:**

```
High sweeping aerial of a single white car threading along a thin winding ribbon of road through a vast misty green valley framed by towering peaks, low clouds drifting across the mountainsides, pockets of fog in the folds of the terrain, the drone glides slowly and steadily emphasizing the awe-inspiring scale.
```

---

### Shot 9: Driver Portrait Interior

**Setup:** 3s · Portrait ref · low motion

**Prompt:**

```
Medium close-up of the young blonde woman driving, calm and focused expression, soft daylight raking through the side window across her face and freckled skin, strands of hair moving gently in the cabin air, faint windshield reflections, slow subtle push-in, shallow depth of field, intimate and cinematic.
```

---

### Shot 10: Tunnel Approach Aerial

**Setup:** 2s · Car ref · medium motion

**Prompt:**

```
Atmospheric aerial shot of the white car approaching a dark stone tunnel carved into a fog-covered mountainside, mist drifting across the road and cliff face, as the car nears the tunnel mouth the camera slowly cranes back to reveal the dramatic alpine drop and sheer scale of the pass, moody and imposing.
```

---

### Shot 11: Parked Car Detail

**Setup:** 2s · Car ref · low motion

**Prompt:**

```
Low-angle detail shot of the parked white supercar on a wet road focused on the front wheel and headlight, beads of water on the glossy paint, cold morning fog lingering behind, camera performs a slow smooth dolly along the sleek bodywork admiring the curves and finish, premium and refined.
```

---

### Shot 12: Alpine Meadow Portrait

**Setup:** 3s · Portrait ref · low motion

**Prompt:**

```
Cinematic portrait of the blonde woman standing alone in an alpine meadow wearing a white coat, soft overcast light falling evenly on her face, wind gently lifting her hair, calm distant gaze, misty mountains stretching out behind her, slow subtle push-in with shallow depth of field, peaceful and introspective.
```

---

### Shot 13: Picking Wildflowers

**Setup:** 3s · Portrait ref · medium motion

**Prompt:**

```
Wide-to-medium shot of the woman crouching gracefully among mountain wildflowers in her white outfit, gently reaching down to pick a small white daisy, soft diffused light bathing the scene, a misty valley spread out behind her, slow gentle handheld camera move following her hands, tender and serene.
```

---

### Shot 14: Daisy Behind Ear

**Setup:** 3s · Portrait ref · low motion

**Prompt:**

```
Extreme close-up profile of the woman tucking a white daisy behind her ear, freckled skin and silver earring and ring catching the soft light, a breeze moving fine strands of her hair, muted green landscape blurred into bokeh behind her, delicate slow motion, very shallow focus, intimate and emotional.
```

---

### Shot 15: Arriving at Chalet

**Setup:** 3s · Car ref · medium motion

**Prompt:**

```
Aerial dusk shot of the white supercar arriving at a modern luxury mountain chalet, large windows glowing warm from within, the chalet on a green hillside ringed by misty forest and distant peaks, camera slowly orbits as the last golden-hour warmth seeps into the frame contrasting the cooler earlier blues.
```

---

### Shot 16: Emotional Reunion

**Setup:** 3s · Portrait ref · medium motion

**Prompt:**

```
Emotional wide-to-medium dusk shot of two women running toward each other to embrace in front of the parked white supercar outside the chalet, arms open wide in a warm heartfelt reunion, soft golden light wrapping the scene, misty peaks glowing behind them, gentle slow motion, warm and deeply human.
```

---

### Shot 17: Final Portrait with Daisy

**Setup:** 3s · Portrait ref · low motion

**Prompt:**

```
Cinematic close-up of the blonde woman smiling warmly with a white daisy tucked behind her ear in soft golden dusk light, a gentle rim light catching her hair, her friend and the green mountains out of focus behind her, a light breeze moving her hair, slow subtle push-in, tender and uplifting closing note.
```

## Step 5: Curate & Re-Roll Drift

For each shot, review the takes and keep the strongest. If her face shifts or the car's proportions change between clips:

### Troubleshooting Character Consistency

- **Re-upload the reference image** and regenerate
- **Add anti-morphing wording**: "same face, consistent identity, no distortion, stable proportions"
- **Push motion strength higher** on the driving and aerial shots (3, 4, 7, 8)
- **Keep motion low** on portraits (1, 6, 9, 12, 14, 17) for stillness

### Selection Criteria

- Character face matches reference exactly
- Car proportions and color consistent
- Motion quality smooth and natural
- Atmospheric elements (fog, mist) well-rendered
- Overall cinematic quality maintained

## Step 6: Assemble, Retime & Finish

### Post-Production Workflow

1. **Import** all 17 selected clips into CapCut or DaVinci Resolve in sequence order
2. **Trim** each clip to its target 2–3s to land the full piece around 45 seconds
3. **Retime** the emotional beats (shots 14, 16, 17) into slow motion
4. **Apply** a 2.39:1 letterbox crop for the cinematic anamorphic frame
5. **Layer** a cinematic music bed plus light engine and ambience sound design
6. **Match** a single unified grade across all clips (desaturated teal-grey-green warming to golden dusk)
7. **Export** at 4K, 16:9

### Color Grading Notes

- **Shots 1–13**: Cool desaturated teal-grey-green grade, moody overcast alpine atmosphere
- **Shots 14–17**: Gradual warming, introducing golden hour tones
- **Final shots**: Warm golden dusk light contrasting with cooler mountain blues
- **Consistency**: Maintain fine 35mm film grain throughout

### Sound Design Elements

- **Engine sounds**: Subtle supercar engine notes during driving sequences
- **Ambient sounds**: Wind, rain on road, mountain atmosphere
- **Music**: Cinematic, emotional score building through narrative
- **Foley**: Footsteps, clothing rustle, daisy handling (subtle)

## Technical Notes

### Seedance 2.0 Best Practices

- **Character consistency**: Always use same reference image for same subject
- **Motion strength**: Adjust per shot type (low for portraits, high for action)
- **Generation count**: 2-4 takes per shot to ensure quality options
- **Duration**: Generate at 5s, trim to 2-3s in post for best results

### Common Issues and Solutions

- **Face drift**: Re-upload reference, add "same face, consistent identity"
- **Car color shift**: Ensure reference image is clearly lit and unambiguous
- **Motion artifacts**: Lower motion strength, regenerate
- **Atmospheric inconsistency**: Ensure global style suffix is appended to all prompts

### Shot Categories

**Low Motion** (shots 1, 2, 6, 9, 11, 12, 14, 17):

- Portraits and intimate details
- Minimal camera movement
- Focus on emotion and character

**Medium Motion** (shots 5, 10, 13, 15, 16):

- Establishing shots and transitions
- Moderate camera movement
- Balanced between action and stillness

**High Motion** (shots 3, 4, 7, 8):

- Driving sequences and aerials
- Dynamic camera work
- Action and scale emphasis

## Story Arc

### Act 1: The Drive (Shots 1-11)

- Solitary journey through misty alpine passes
- Focus on car, driving, and atmospheric landscape
- Cool, desaturated color palette
- Building sense of isolation and contemplation

### Act 2: Nature Interlude (Shots 12-14)

- Transition from car to character on foot
- Intimate connection with nature
- Wildflowers and personal moment (daisy)
- Introspective, peaceful tone

### Act 3: Arrival & Reunion (Shots 15-17)

- Arrival at destination (luxury chalet)
- Emotional reunion with friend
- Golden hour warmth replacing cool tones
- Uplifting, human connection conclusion

## Quality Control Checklist

- [ ] Both reference images (portrait and car) generated and saved
- [ ] Vosu AI dashboard configured with consistent settings (16:9, 1080p, 5s)
- [ ] Global style suffix saved as reusable template
- [ ] All 17 shots generated with correct reference images uploaded
- [ ] Character face consistent across all portrait shots (1, 6, 9, 12, 13, 14, 16, 17)
- [ ] Car appearance consistent across all vehicle shots (3, 4, 5, 7, 8, 10, 11, 15, 16)
- [ ] Motion strength appropriate for each shot type
- [ ] Best takes selected from 2-4 generations per shot
- [ ] All clips imported in correct sequence order
- [ ] Each clip trimmed to 2-3s target length
- [ ] Slow motion applied to emotional beats (14, 16, 17)
- [ ] 2.39:1 letterbox crop applied for anamorphic look
- [ ] Unified color grade: cool teal-grey-green warming to golden dusk
- [ ] Music bed and sound design layered
- [ ] Final export: 4K, 16:9, ~45 seconds total duration
- [ ] 35mm film grain maintained throughout
- [ ] Narrative arc clear: drive → nature → reunion

## Related Prompts

- [Luxury Car Commercial - Mountain Drive](../action-driving/luxury-car-commercial-mountain-drive.md) — Alternative luxury car narrative
- [Cinematic Night Scene Rendering](../../architectural-boards/cinematic-night-scene-rendering.md) — Atmospheric lighting techniques
