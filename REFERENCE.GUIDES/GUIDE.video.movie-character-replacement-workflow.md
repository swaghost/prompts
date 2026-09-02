# Movie Scene Character Replacement - AI Video Guide

## Description

Recreate the movement, staging, camera language, and atmosphere of a short movie scene while replacing the original performers with new character references. This workflow uses a scene video as the motion and edit blueprint, a depth map to preserve spatial structure, character cards for identity, and an environment reference for set continuity.

## Use and Rights

Use source footage that you own or are authorized to process. Get permission from any person whose likeness you use, and label the result as AI-generated when publishing it. Avoid presenting a generated recreation as an original studio clip or as an endorsement by the original performers, filmmakers, or rights holders.

## Engines / Tools

- Seedance 2.5, accessed through a compatible video-generation interface such as CapCut or WaveSpeed
- Depth Anything video, accessed through [WaveSpeed](https://wavespeed.ai/models/wavespeed-ai/depth-anything/video) or an equivalent depth-map tool
- A video editor for trimming, reference preparation, and audio finishing

## What You Need

1. **Short scene reference video** - A clip of up to 30 seconds with the action, framing, camera cuts, and timing you want to preserve.
2. **Character reference image for each replacement role** - Clear character cards showing face, hair, wardrobe, and body proportions.
3. **Environment reference image** - A clean image of the set or location when the scene reference alone does not provide enough environmental detail.
4. **Optional audio reference** - The original scene audio, only when you have the rights to use it.

## Workflow at a Glance

| Step | Input                           | Output                     |
| ---- | ------------------------------- | -------------------------- |
| 01   | Authorized scene clip           | Trimmed motion reference   |
| 02   | Motion reference                | Depth-map video            |
| 03   | Character and location material | Upload-ready reference set |
| 04   | All references                  | Character-replaced video   |

---

## Step 01 - Prepare the Scene Reference

_The original clip is the timing blueprint._

### Select the right segment

1. Choose one continuous scene or a short sequence with a clear beginning and end.
2. Trim it to **30 seconds or less**, matching the maximum generation length supported by the workflow.
3. Keep the original resolution and frame rate when possible.
4. Prefer footage with readable silhouettes, stable exposure, and visible body movement.
5. Remove subtitles, watermarks, or overlays from your working reference when you are authorized to do so.

### Preserve these properties

- Character entrances and exits
- Relative position and screen direction of every performer
- Camera framing, movement, and cuts
- Timing of gestures, impacts, pauses, and reactions
- Set layout, lighting direction, and practical effects
- Ambient sound and music cues, if the audio is licensed for reuse

### Settings

- **Maximum reference duration:** 30 seconds
- **Shot structure:** One continuous sequence or an intentional series of cuts
- **Preferred source:** Clean, stable, high-resolution footage
- **Export:** Use a widely supported video format such as MP4

**Critical:** Do not ask the model to invent new choreography if the goal is a replacement. The reference clip should remain the authority for motion and timing.

---

## Step 02 - Generate the Depth Map

_Depth protects the scene's spatial logic._

### Process

1. Upload the trimmed scene to a video depth-estimation tool.
2. Generate a depth-map video for the full clip.
3. Check the result for broken edges around faces, hands, hair, props, and foreground objects.
4. Regenerate or clean the depth map if foreground and background layers collapse into one plane.
5. Keep the depth map synchronized with the original clip from the first frame to the last.

### Why it matters

The depth reference helps the video model retain subject scale, camera parallax, foreground/background separation, blocking, and the spatial rhythm of the original scene. It is especially valuable for action scenes, moving cameras, and layered environments.

### Depth-map checklist

- The full scene duration is present.
- Major subjects remain separate from the set.
- Hands, faces, and fast-moving limbs are not merged with nearby surfaces.
- Camera movement remains legible.
- No frame offset exists between the source video and depth video.

---

## Step 03 - Build the Reference Set

_Identity and environment are separate sources of truth._

### Character cards

Prepare one image per replacement role. Each card should show:

- Clear face and hairline
- Hairstyle, hair texture, and distinctive accessories
- Wardrobe and color relationships
- Natural body proportions
- A neutral or easily readable pose
- Even lighting and enough resolution for facial detail

Use consistent names such as `Character 1`, `Character 2`, and `Character 3` so the prompt can refer to each image unambiguously.

### Environment card

Use a separate location image when you need to preserve a set more precisely than the scene clip allows. Include the architecture, materials, props, weather, time of day, and lighting that should survive the replacement.

For a wooden forest dojo, for example, the environment card might show an open-air karate platform, tatami flooring, dark timber posts, tiled roof, hanging banners, and dense green forest. Replace that description with the actual location details for your scene.

### Upload order

Use a consistent order in the generation interface:

1. **Video 1:** Original scene reference
2. **Video 2:** Synchronized depth map
3. **Image 1:** Character 1 card
4. **Image 2:** Character 2 card
5. **Image 3:** Environment card

If your interface labels uploads differently, update the `@` references in the prompt before generating.

---

## Step 04 - Generate the Replacement

_Paste the prompt after attaching every reference._

### Complete Video Prompt

```
Use @Video 1 as the exact motion, staging, cinematography, and timing reference. Use @Video 2 as the synchronized depth reference for spatial structure and subject separation. Recreate the complete sequence with the same duration, camera cuts, shot order, framing, camera movement, subject blocking, screen direction, gestures, poses, reactions, action timing, and interaction with the environment.

Replace the appearing performers with the provided character cards: Character 1 from @Image 1 and Character 2 from @Image 2. Preserve each character's identity consistently throughout the entire video. Character 1 must retain the exact facial structure, skin tone, hairstyle, hair texture, hairline, distinctive features, body proportions, and wardrobe shown in @Image 1. Character 2 must retain the exact facial structure, skin tone, hairstyle, hair texture, hairline, distinctive features, body proportions, and wardrobe shown in @Image 2. Do not blend identities, borrow facial features, or allow either character to morph into the other.

Keep the original choreography and performance dynamics exactly as shown in @Video 1. Match every entrance, exit, step, turn, gesture, impact, pause, reaction, camera cut, and duration. Preserve the original screen positions and relative scale of the characters. Do not add new actions, extra performers, new camera angles, slow motion, or alternate choreography.

Use @Image 3 as the exact environment reference. Preserve the location's architecture, floor, walls, props, materials, weather, time of day, lighting direction, color relationships, and atmosphere. Integrate both replacement characters naturally into the environment with correct contact shadows, reflections, occlusion, scale, perspective, and interaction with the floor and surrounding objects.

Maintain realistic anatomy, stable hands, stable faces, stable clothing, consistent hair, and temporal continuity from beginning to end. Preserve the original cinematography and visual effects without allowing them to alter the identity or wardrobe of either character. Match the original lighting, exposure, depth of field, motion blur, lens perspective, film grain, and color grade.

Generate a photorealistic cinematic video. No subtitles, captions, text overlays, logos, watermarks, identity drift, face morphing, duplicate limbs, extra fingers, warped hands, unstable eyes, floating props, background replacement, altered choreography, altered camera movement, or unexplained objects. Keep all sound effects and background music only when the uploaded audio is authorized for reuse; otherwise generate no replacement audio and finish the sound separately.
```

### Prompt controls that matter most

- **Video 1 is the authority for motion:** Repeat timing, blocking, cuts, and choreography explicitly.
- **Video 2 is the authority for depth:** Use it to reinforce camera parallax and foreground/background separation.
- **Character cards are the authority for identity:** State that identities must not blend or drift.
- **The environment card is the authority for the set:** Describe physical details that must remain unchanged.
- **Negative constraints are deliberate:** Name common failure modes instead of relying on a generic negative prompt.

### Generation settings

Use the closest available settings to the source clip:

- **Duration:** Match the reference, up to 30 seconds
- **Aspect ratio:** Match the source video
- **Motion strength:** Low to moderate when exact choreography matters
- **Reference strength:** High for character identity and environment continuity
- **Audio:** Keep only licensed source audio; otherwise finish in the editor
- **Output:** Generate multiple passes and compare the same timecodes

---

## Finishing the Result

_The edit restores the details generation cannot guarantee._

1. Compare the generated clip with the reference at the same timecodes.
2. Select the pass with the most stable identities and closest blocking, even if another pass has prettier individual frames.
3. Trim any extra frames at the head or tail.
4. Repair short identity or hand defects with targeted re-generation when possible.
5. Reapply the authorized source audio, or build a new sound design that matches the timing without copying protected audio.
6. Match the final grade, grain, aspect ratio, and delivery resolution to the intended output.
7. Review every face, hand, prop, reflection, and cut before publishing.

### Quality pass

- Motion matches the reference rather than merely resembling it.
- Characters remain recognizable in wide shots, close-ups, and profile views.
- Wardrobe and hair stay stable across cuts.
- Feet and hands contact the environment correctly.
- Depth and occlusion remain believable during camera movement.
- No generated subtitles, logos, or accidental text appear.
- Rights, consent, and AI disclosure are handled for the final publication.

---

## Troubleshooting

### Characters drift or morph

**Cause:** Character references are ambiguous, underweighted, or not assigned clearly to roles.

**Solution:** Use cleaner character cards, label every upload, shorten the clip, and repeat identity locks for each role. Generate a shorter difficult shot before attempting the full sequence.

### Choreography changes

**Cause:** The prompt describes the desired mood but does not make the source video authoritative for timing and motion.

**Solution:** State that the original clip controls every action, screen position, cut, and duration. Lower motion strength and remove creative additions from the prompt.

### Camera movement or depth collapses

**Cause:** The depth map is missing, poorly synchronized, or too noisy around moving subjects.

**Solution:** Regenerate the depth map, verify frame alignment, and inspect edges around hands, hair, props, and foreground objects.

### Environment changes between shots

**Cause:** The scene video does not contain enough location detail, or the environment reference is treated as optional.

**Solution:** Supply a clear environment card and name the architecture, materials, props, weather, and lighting as fixed constraints.

### Audio becomes unusable

**Cause:** Generated audio may invent dialogue, music, or effects, and source audio may not be cleared for reuse.

**Solution:** Generate visuals without replacement audio and complete the soundtrack in the editor using original or properly licensed material.

---

## Quick Reference Checklist

- [ ] Authorized scene clip is 30 seconds or shorter
- [ ] Motion reference is trimmed and synchronized
- [ ] Depth map covers the entire clip
- [ ] One clear character card exists for each role
- [ ] Environment reference is prepared when needed
- [ ] Upload labels match the `@` references in the prompt
- [ ] Motion, identity, environment, and negative constraints are explicit
- [ ] Several passes are generated and compared by timecode
- [ ] Audio rights and likeness consent are confirmed
- [ ] Final output is reviewed for artifacts and labeled as AI-generated where appropriate

## Source

Adapted from [How to recreate a movie scene with AI](https://unmarred-soil-d0f.notion.site/How-to-recreate-a-movie-scene-with-AI-3c0ee347be0580459603ee111995b407) by Daniel Volui. The source demonstrates a Matrix dojo scene recreated with a depth map, character references, an environment reference, and Seedance 2.5.

_The scene is the blueprint. The references are the cast and set._
