# Cinematic Alpine Drive — AI Video Recreation Guide

## Description

A comprehensive workflow for creating a moody, cinematic automotive-lifestyle short film using AI video generation. A young woman driving a white supercar solo through misty alpine passes—winding roads, tunnels, a turquoise lake, rain and fog—then a reflective nature beat (wildflowers, a daisy behind the ear), arrival at a luxury mountain chalet at dusk, and an emotional reunion. The grade stays cool and desaturated throughout, warming into golden dusk for the finale. Assembled from 17 short clips generated in Vosu AI using Seedance 2.0.

## Tools Required

- **Vosu AI** — Video generation platform
- **Seedance 2.0** — AI video generation model with elite character consistency and motion cloning
- **Nano Banana 2** (or similar) — Image generation for reference stills
- **CapCut or DaVinci Resolve** — Video editing and assembly
- **Music bed + sound design** — Engine sounds, ambience, cinematic score

## Target Specifications

- **Duration:** ~45 seconds
- **Resolution:** 4K
- **Aspect Ratio:** 16:9 (with 2.39:1 letterbox crop for cinematic frame)
- **Shot Count:** 17 clips (2-3 seconds each)
- **Color Grade:** Cool desaturated teal-grey-green → warm golden dusk finale

---

## Step 1 — Prepare Your Consistency Anchors

Before generating any video, lock down two reference images. These are what keep the woman's face and the car from drifting across 17 separate clips—Seedance 2.0's strength is elite character consistency and motion cloning, but only if you feed it the same references every time.

### Portrait Reference

**One clean, well-lit, front-facing image of the woman:**

- Mid-20s
- Long wavy blonde hair
- Visible freckles
- Natural makeup
- Tailored white coat
- Neutral expression

### Car Reference

**One clean side / three-quarter image of the white two-seat mid-engine supercar:**

- Glossy wet bodywork
- Black five-spoke wheels

**Generate these stills first in Nano Banana 2** (or your usual image tool) and keep them in a project folder. You will re-upload the matching reference for every shot in Steps 4–5.

---

## Step 2 — Set Up the Vosu AI Dashboard

1. Log into **Vosu AI** and open the **Video Generation dashboard**
2. Select **Seedance 2.0** from the model list
3. Set your global defaults once so every clip matches:
   - **Aspect ratio:** 16:9
   - **Resolution:** 1080p
   - **Duration:** 5s (you'll trim/retime later)
   - **Output count:** 2–4 per shot
4. Keep these settings constant across all 17 shots for a uniform look
5. Work **image-to-video:** upload the matching reference as the main image, then paste the prompt

---

## Step 3 — Lock the Master Look

Append this style block to every prompt so the lens and grade stay identical across all clips. Save it in Vosu's **PromptGPT** as a reusable template so it auto-attaches.

### Global Style Suffix (Append to Every Shot)

```
Cinematic automotive lifestyle film, anamorphic 2.39:1 widescreen, shallow depth of field, moody overcast alpine light warming toward golden dusk, desaturated teal-grey-green grade, drifting fog and mist, wet reflective roads, fine 35mm film grain, natural photorealistic color, 4K.
```

### Consistency Anchors (Include in Matching Shots)

**Woman:**

```
Same young woman, mid-20s, long wavy blonde hair, light freckles, natural makeup, tailored white coat — lock identity to the reference image, no face morphing.
```

**Car:**

```
Same sleek white two-seat mid-engine supercar, glossy wet bodywork, black five-spoke wheels.
```

---

## Step 4 — Shot-by-Shot Generation

Generate in order. For each shot, **upload the reference noted in the Setup column**, paste the prompt (with the global suffix appended), and generate 2–4 takes.

**Shots 1–11** cover the drive and detail beats.  
**Shots 12–17** cover the nature and emotional beats.

### Shot Table

| #      | Setup                              | Seedance 2.0 Prompt                                                                                                                                                                                                                                                                                                          |
| ------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**  | 2s · Car interior ref · low motion | Close-up inside the cabin of a luxury supercar on a woman's elegant hands resting on a black leather sports steering wheel, delicate silver watch, crisp white blazer cuff, soft ambient dashboard glow, small deliberate steering adjustments, static locked-off camera, shallow focus, intimate warm cabin light.          |
| **2**  | 2s · Car interior ref · low motion | Extreme macro close-up of a white high heel slowly and deliberately pressing the accelerator pedal in a premium car footwell, brushed-aluminium pedals catching a faint reflection, low warm interior light, fully static camera, razor-thin depth of field with only the shoe and pedal sharp.                              |
| **3**  | 3s · Car ref · high motion         | Sweeping cinematic aerial drone shot high above a wet mountain pass, a lone white supercar carving through a tight hairpin bend, a vivid turquoise glacial lake far below ringed by steep green slopes, low clouds clinging to the peaks, camera slowly cranes and tracks the car from above revealing epic alpine scale.    |
| **4**  | 2s · Car ref · high motion         | Low-angle tracking close-up of the white supercar's front wheel spinning fast on glistening wet tarmac, a fine veil of water spray misting off the tyre, the road reflecting the grey sky, fog behind, camera skims low and fast alongside the moving wheel with subtle motion blur.                                         |
| **5**  | 2s · Car ref · medium motion       | Wide static cinematic shot of the white supercar driving straight toward camera along a misty rain-soaked mountain road, headlights glowing and reflecting across the wet asphalt, a rocky fog-shrouded slope behind, the car steadily approaches, grows in frame, then sweeps past the lens through heavy atmospheric haze. |
| **6**  | 2s · Portrait ref · low motion     | Close-up of the blonde driver's face reflected in the car's side wing mirror with raindrops scattered across the mirror glass, blurred green landscape rushing past behind the reflection, a subtle turn of her head with calm focused eyes, gentle handheld micro-shake, shallow focus on the reflection.                   |
| **7**  | 2s · Car ref · high motion         | Hood-mounted POV looking down a wet mountain road lined with roadside marker poles flicking past on either side, fog softening the distance ahead, the road rushing smoothly beneath the camera at speed, overcast desaturated light, wet sheen on the asphalt, strong feeling of forward motion and quiet isolation.        |
| **8**  | 3s · Car ref · high motion         | High sweeping aerial of a single white car threading along a thin winding ribbon of road through a vast misty green valley framed by towering peaks, low clouds drifting across the mountainsides, pockets of fog in the folds of the terrain, the drone glides slowly and steadily emphasizing the awe-inspiring scale.     |
| **9**  | 3s · Portrait ref · low motion     | Medium close-up of the young blonde woman driving, calm and focused expression, soft daylight raking through the side window across her face and freckled skin, strands of hair moving gently in the cabin air, faint windshield reflections, slow subtle push-in, shallow depth of field, intimate and cinematic.           |
| **10** | 2s · Car ref · medium motion       | Atmospheric aerial shot of the white car approaching a dark stone tunnel carved into a fog-covered mountainside, mist drifting across the road and cliff face, as the car nears the tunnel mouth the camera slowly cranes back to reveal the dramatic alpine drop and sheer scale of the pass, moody and imposing.           |
| **11** | 2s · Car ref · low motion          | Low-angle detail shot of the parked white supercar on a wet road focused on the front wheel and headlight, beads of water on the glossy paint, cold morning fog lingering behind, camera performs a slow smooth dolly along the sleek bodywork admiring the curves and finish, premium and refined.                          |
| **12** | 3s · Portrait ref · low motion     | Cinematic portrait of the blonde woman standing alone in an alpine meadow wearing a white coat, soft overcast light falling evenly on her face, wind gently lifting her hair, calm distant gaze, misty mountains stretching out behind her, slow subtle push-in with shallow depth of field, peaceful and introspective.     |
| **13** | 3s · Portrait ref · medium motion  | Wide-to-medium shot of the woman crouching gracefully among mountain wildflowers in her white outfit, gently reaching down to pick a small white daisy, soft diffused light bathing the scene, a misty valley spread out behind her, slow gentle handheld camera move following her hands, tender and serene.                |
| **14** | 3s · Portrait ref · low motion     | Extreme close-up profile of the woman tucking a white daisy behind her ear, freckled skin and silver earring and ring catching the soft light, a breeze moving fine strands of her hair, muted green landscape blurred into bokeh behind her, delicate slow motion, very shallow focus, intimate and emotional.              |
| **15** | 3s · Car ref · medium motion       | Aerial dusk shot of the white supercar arriving at a modern luxury mountain chalet, large windows glowing warm from within, the chalet on a green hillside ringed by misty forest and distant peaks, camera slowly orbits as the last golden-hour warmth seeps into the frame contrasting the cooler earlier blues.          |
| **16** | 3s · Portrait ref · medium motion  | Emotional wide-to-medium dusk shot of two women running toward each other to embrace in front of the parked white supercar outside the chalet, arms open wide in a warm heartfelt reunion, soft golden light wrapping the scene, misty peaks glowing behind them, gentle slow motion, warm and deeply human.                 |
| **17** | 3s · Portrait ref · low motion     | Cinematic close-up of the blonde woman smiling warmly with a white daisy tucked behind her ear in soft golden dusk light, a gentle rim light catching her hair, her friend and the green mountains out of focus behind her, a light breeze moving her hair, slow subtle push-in, tender and uplifting closing note.          |

---

## Step 5 — Curate & Re-Roll Drift

For each shot, review the takes and keep the strongest. If her face shifts or the car's proportions change between clips:

### Solutions

1. **Re-upload the reference image** and regenerate
2. **Add anti-morphing wording:** "same face, consistent identity, no distortion, stable proportions"
3. **Push motion strength higher** on the driving and aerial shots (3, 4, 7, 8)
4. **Keep it low** on portraits (1, 6, 9, 12, 14, 17) for stillness

---

## Step 6 — Assemble, Retime & Finish

1. Import all **17 selected clips** into CapCut or DaVinci Resolve in sequence order
2. **Trim each clip** to its target 2–3s to land the full piece around 45 seconds
3. **Retime the emotional beats** (14, 16, 17) into slow motion
4. Apply a **2.39:1 letterbox crop** for the cinematic frame
5. **Layer a cinematic music bed** plus light engine and ambience sound design
6. **Match a single unified grade** across all clips
7. **Export at 4K, 16:9**

---

## Shot Categories Breakdown

### Driving Shots (1-11)

**Interior Details:**

- Shot 1: Hands on steering wheel
- Shot 2: Heel on accelerator pedal

**Aerials:**

- Shot 3: Drone above hairpin bend with turquoise lake
- Shot 8: High aerial of winding valley road
- Shot 10: Aerial approaching stone tunnel

**Road-Level:**

- Shot 4: Low-angle tracking wheel spray
- Shot 5: Wide frontal approach through mist
- Shot 7: Hood-mounted POV racing forward
- Shot 11: Detail dolly along parked car

**Character:**

- Shot 6: Face in wing mirror with raindrops
- Shot 9: Medium close-up driving interior

### Nature & Emotional Beats (12-17)

**Meadow Sequence:**

- Shot 12: Standing portrait in alpine meadow
- Shot 13: Crouching to pick daisy
- Shot 14: Extreme close-up tucking daisy behind ear

**Arrival & Reunion:**

- Shot 15: Aerial of car arriving at chalet at dusk
- Shot 16: Two women embracing in front of car
- Shot 17: Smiling close-up with daisy, golden light

---

## Color Grading Notes

### Shots 1-14: Cool Desaturated

- **Base:** Teal-grey-green grade
- **Atmosphere:** Moody overcast alpine light
- **Fog/Mist:** Heavy, drifting, fog-shrouded
- **Roads:** Wet reflective surfaces
- **Feel:** Introspective, isolated, calm

### Shots 15-17: Warm Golden Dusk

- **Transition:** Cool blues warming to golden hour
- **Light Quality:** Soft golden dusk light, rim lighting
- **Windows:** Warm interior glow from chalet
- **Feel:** Uplifting, human connection, tender

### Unified Elements

- **Film Grain:** Fine 35mm texture across all shots
- **Depth of Field:** Shallow, cinematic bokeh
- **Aspect Ratio:** 2.39:1 anamorphic widescreen feel
- **Resolution:** 4K photorealistic quality

---

## Motion Strength Guidelines

| Motion Level | Shots                      | Characteristics                                                    |
| ------------ | -------------------------- | ------------------------------------------------------------------ |
| **Low**      | 1, 2, 6, 9, 11, 12, 14, 17 | Static locked camera, minimal subject movement, portrait stillness |
| **Medium**   | 5, 10, 13, 15, 16          | Controlled camera moves, steady approach/orbit, gentle handheld    |
| **High**     | 3, 4, 7, 8                 | Fast tracking, aerial sweeps, racing POV, dynamic motion blur      |

---

## Troubleshooting

### Problem: Face morphs between clips

**Solution:**

- Re-upload portrait reference for that specific shot
- Add "lock identity to the reference image, no face morphing"
- Regenerate with anti-drift language in prompt

### Problem: Car changes appearance

**Solution:**

- Verify car reference is uploaded for that shot
- Add "same sleek white two-seat mid-engine supercar, glossy wet bodywork, black five-spoke wheels"
- Ensure "stable proportions, consistent vehicle" is in prompt

### Problem: Color grade inconsistent

**Solution:**

- Verify global style suffix is appended to every prompt
- Match grade in post-production using reference frame from best clip
- Apply adjustment layer across all clips in editing software

### Problem: Motion too smooth/floaty (doesn't feel real)

**Solution:**

- Add "subtle motion blur" and "natural photorealistic movement"
- Increase motion strength setting in Vosu
- Add "gentle handheld micro-shake" for realism

### Problem: Clips don't flow together in edit

**Solution:**

- Check that each clip has matching 16:9 aspect ratio and 1080p resolution
- Trim to emotional beats rather than arbitrary durations
- Add short crossfades (0.5-1 second) between tonal shifts

---

## Advanced Techniques

### Adding Sound Design Layers

**Essential audio:**

1. **Cinematic music bed** — Moody, builds to warm finale
2. **Engine sounds** — Supercar revs, acceleration, distant rumble
3. **Ambience** — Wind, rain on windshield, mountain atmosphere
4. **Foley** — Steering wheel leather, heel on pedal, footsteps in grass

### Extended Cut Options

**Additional shots to consider:**

- **Interior rearview mirror shot** — Driver's eyes reflected
- **Dashboard detail macro** — Speedometer, instrument cluster glow
- **Waterfall or stream beside road** — Nature interlude
- **Coffee/thermos in cupholder** — Intimate travel detail
- **Map or phone navigation** — Journey element

### Alternative Endings

**Option 1: Solo Reflective**

- End at shot 14 (daisy behind ear)
- Woman alone, introspective, peaceful

**Option 2: Arrival Only**

- End at shot 15 (chalet arrival)
- No reunion, just destination reached

**Option 3: Full Reunion** (current)

- Shots 16-17 with emotional embrace and smile
- Human connection, warm closure

---

## Final Tips

**The secret to cinematic AI video that feels professionally shot:**

1. **Lock references before starting** — Same portrait, same car, every single shot
2. **Append global style suffix** — Consistent lens, grade, atmosphere across all 17 clips
3. **Match motion strength to shot type** — High for aerials/tracking, low for portraits
4. **Generate 2-4 takes per shot** — Pick the cleanest, most consistent
5. **Edit to emotional beats** — Don't force arbitrary clip lengths
6. **Retime key moments** — Slow motion on shots 14, 16, 17 for impact
7. **Unified color grade in post** — Lock the look across all clips
8. **Letterbox crop for cinema feel** — 2.39:1 anamorphic widescreen
9. **Layer sound design** — Music + engine + ambience + foley
10. **Watch for face/car drift** — Re-roll immediately if identity changes

---

**Platform: Vosu AI · Model: Seedance 2.0 · Target: ~45s · 4K · 16:9**

---
