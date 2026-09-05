# Genjutsu Motion Transfer Prompt Pack

Recast any driving clip with a new character while preserving motion, camera, timing, blocking, and edit rhythm. Includes ten copy-paste variants plus a universal structure and troubleshooting guide.

For the complete Higgsfield Soul 2.0 -> Seedance 2.5 -> Genjutsu production pipeline, see [Full Breakdown - Higgsfield Genjutsu Swap Video](GUIDE.full-breakdown-higgsfield-genjutsu-swap-video.md).

## What Genjutsu Does

Genjutsu is a video-to-video model. It re-performs an existing clip rather than generating a new scene.

- **Motion transfer:** Recast the performer while movement remains unchanged.
- **Objects swap:** Replace one product, prop, or garment while leaving the rest of the frame untouched.

## Setup

- **Slot 1:** Driving video, 4-30 seconds; prefer a clean single-subject action.
- **Slot 2:** Reference images or elements, addressed as `@image1`, `@image2`, and so on.
- Turn the prompt toggle on and write a replacement instruction, not a new scene description.
- Select Genjutsu, choose the quality tier, and generate.

## What Controls Quality

- Use a driving clip with a clearly readable subject; heavy motion blur and fast cuts weaken identity.
- Use a full-body character sheet with neutral pose, clean background, and even lighting.
- Never describe a new camera move; inherit the driving video 1:1.
- Put identity lock near the beginning and always close with a negative list.
- In multi-person scenes, identify the replaced subject by position and clothing.

## Eight-Block Prompt Anatomy

1. **Recast:** Who is replaced, with what, and what stays untouched.
2. **Identity lock:** Face, build, hair, and wardrobe remain stable.
3. **Light:** Preserve or rebuild key direction, intensity, and falloff.
4. **Camera:** Inherit 1:1 with no new moves or reframing.
5. **Motion:** Transfer 1:1 with cloth physics and correct proportions.
6. **Performance:** Dialogue, expression, or ending beat.
7. **Sound FX:** Ambience and dialogue treatment.
8. **Negative:** Glitches, morphing, and drift exclusions, always last.

## Universal Base

```text
Replace the [MAIN SUBJECT - e.g. male lead / female lead / person on the left] in the source video with the character from @image1 - same face, same build, same hairstyle, same outfit [DESCRIBE OUTFIT]. Performs the exact same motion, blocking, posture and timing as the original subject. Everyone else in the frame stays untouched. Environment, architecture, props and edit rhythm completely unchanged.

IDENTITY LOCK: Face from @image1 held stable across every frame - no aging, no gender shift, no ethnicity drift, no face swap mid-shot, no reversion to the original subject at any point.

LIGHT: Preserve source lighting exactly - same key direction, same intensity, same shadow falloff. New character lit by that same key with correct skin response. No flat relighting, no plastic sheen.

CAMERA & ANGLE: Inherit the driving video 1:1 - same lens, framing, shot scale and head height. No new camera moves, no reframing.

MOTION: 1:1 transfer. Shoulder rolls, head tilts, eye direction, hand gestures and weight shifts mapped precisely onto the new body. Natural cloth physics - fabric folds and settles with movement. Body proportions from @image1, not stretched to the original frame.

PERFORMANCE: [EXPRESSION / END BEAT / DIALOGUE LINE].

SOUND FX: Retain source ambience. [DIALOGUE TREATMENT IF NEEDED]

VIBE: [GRADE + MOOD], filmic grain, 24fps motion cadence.

NEGATIVE: No glitches, no morphing, no warped face or hands, no identity flicker, no melting fingers, no duplicate limbs, no background wobble, no outfit colour shift, no extra people, no text or watermark, no stutter, no ghosting.
```

## 01 - Epic Film Recast

```text
Replace the lead in the source video with the character from @image1 - same face, same build, same streetwear outfit. Exact same motion, blocking and timing as the original. All other characters, extras and background untouched. IDENTITY LOCK: face from @image1 stable every frame, no drift, no reversion, no swap on profile frames. LIGHT: preserve the warm tungsten key, golden bounce and deep amber shadow falloff; new character lit identically with correct skin response. CAMERA: inherit 1:1, no new moves, no reframing. MOTION: 1:1 transfer with natural cloth physics on jacket and denim, body proportions from @image1. SOUND FX: source ambience, low room tone, faint distant crowd murmur. VIBE: cinematic epic frame with a modern lead, high contrast, rich warm grade, filmic grain, 24fps cadence. NEGATIVE: no glitches, no morphing, no face flicker, no warped hands, no altering other characters, no background wobble, no watermark, no stutter.
```

## 02 - Action Sequence Recast

```text
Replace the performer in the source video with the character from @image1 - same face, same physique, same outfit. Identical choreography, impact timing and body mechanics. Background, stunt environment and all other figures unchanged. IDENTITY LOCK: face held stable through fast movement, no smearing, no swap on motion-blur frames, no reversion at impact. LIGHT: preserve source contrast and direction, hard key with crushed shadows. CAMERA: inherit 1:1 including handheld shake and whip movement. MOTION: 1:1 transfer, full weight and momentum carried through the body, clothing reacting to force, feet correctly planted. SOUND FX: source impacts, footsteps, cloth snap, no added music. VIBE: gritty action grade, desaturated cool shadows, heavy grain. NEGATIVE: no morphing on fast frames, no ghosting, no limb duplication, no identity flicker, no floating body, no background warp, no rubber joints.
```

## 03 - Dance / Trend Recast

```text
Replace the dancer in the source video with the character from @image1 - same face, same build, same outfit. Every step, hip movement, arm swing and beat hit mapped exactly. Location and other dancers untouched. IDENTITY LOCK: face from @image1 stable through every rotation and turn, including profile and back-to-camera frames. LIGHT: preserve source lighting and colour spill on skin and fabric. CAMERA: inherit 1:1. MOTION: 1:1 transfer with full cloth physics - fabric swings, lifts and settles on beat, shoes grip the floor, no sliding. SOUND FX: retain source track and ambience. VIBE: punchy contemporary grade, clean skin tones, light grain. NEGATIVE: no morphing on spins, no foot sliding, no limb detachment, no identity flicker, no outfit colour shift, no background wobble.
```

## 04 - Location Swap, Same Performance

```text
Keep the character from @image1 performing the exact motion from the source video, but relocate the scene to [NEW LOCATION - e.g. a neon-lit alley at night]. Subject motion, blocking and timing stay 1:1 with the source. IDENTITY LOCK: face and outfit from @image1 stable every frame. LIGHT: relight the subject to match the new environment - [KEY: e.g. cool magenta neon from frame left, cyan rim from behind] with correct skin response and matching shadow direction on the ground. CAMERA: inherit the source move exactly, applied to the new environment. MOTION: 1:1 transfer, natural cloth physics, feet correctly grounded to the new surface with contact shadows. SOUND FX: new location ambience layered under source movement sound. VIBE: [GRADE + MOOD], filmic grain. NEGATIVE: no floating feet, no mismatched shadows, no background wobble, no morphing, no identity flicker, no doubled environment layers, no lighting that ignores the new scene.
```

## 05 - Dialogue End Beat

```text
Replace the lead in the source video with the character from @image1 - same face, build and outfit, identical motion and timing. All other elements untouched. IDENTITY LOCK: stable face every frame, no reversion. LIGHT and CAMERA: inherit source 1:1. MOTION: 1:1 transfer with natural cloth physics. PERFORMANCE END BEAT: on the final beat the character turns to look directly into camera, holds a small confident half-smile, and delivers in clean lip-sync: "[YOUR LINE HERE]". Lips match syllables exactly, jaw and cheek movement natural, line completes with one second of hold before the last frame. SOUND FX: source ambience retained, clean dialogue on top, no music bed, no reverb wash over the line. VIBE: cinematic grade, filmic grain. NEGATIVE: no rubber-mouth, no audio drift, no morphing, no face flicker, no stutter, no line cut off before the end frame.
```

## 06 - Product Swap (Objects Mode)

```text
Replace only the [ORIGINAL OBJECT] held by the subject with the product from @image1 - exact same shape, colour, label, proportions and material finish as the reference. The performer, their face, their outfit, the environment and the camera all stay completely unchanged. IDENTITY LOCK ON PRODUCT: label text, logo placement and colourway from @image1 held stable across every frame, no warping of the label as the object rotates. LIGHT: the product picks up the scene's existing key and reflections, correct specular highlights on its surface, accurate contact shadow where it meets the hand. CAMERA: inherit 1:1. MOTION: the object tracks the hand precisely with correct scale and grip contact through the full move, no sliding, no floating. SOUND FX: source audio untouched. NEGATIVE: no morphing label, no logo drift, no floating product, no scale jump, no ghost of the original object, no hand distortion, no reflection mismatch.
```

## 07 - Two-Character Recast

```text
Replace the two leads in the source video: the [SUBJECT A - e.g. person on the left] becomes the character from @image1, the [SUBJECT B - e.g. person on the right] becomes the character from @image2. Each keeps their own reference's face, build, hair and outfit - no cross-contamination between the two. Identical motion, interaction, eyelines and timing to the source. Background and extras untouched. IDENTITY LOCK: both faces stable every frame, @image1 never adopts @image2 features and vice versa, no swap when they cross or overlap in frame. LIGHT: preserve source key on both, correct individual shadow falloff. CAMERA: inherit 1:1. MOTION: 1:1 transfer for both bodies, correct relative scale, natural contact where they touch, cloth physics on both outfits. SOUND FX: source ambience retained. VIBE: [GRADE], filmic grain. NEGATIVE: no identity bleed between characters, no morphing on overlap, no merged limbs, no size mismatch, no face flicker, no background wobble.
```

## 08 - Period Scene, Modern Lead

```text
Replace the lead in the source video with the character from @image1 in full modern streetwear - same face, build and outfit as the reference, deliberately out of period with the surrounding scene. Everything else stays historically intact: costumes on all other figures, set dressing, props and architecture unchanged. Motion, blocking and timing 1:1 with the original. IDENTITY LOCK: face and modern outfit from @image1 stable every frame, wardrobe never drifts toward period costume, no partial blending of the two. LIGHT: preserve the source period lighting - [e.g. warm firelight key, heavy shadow] - falling correctly on modern fabric with accurate sheen on synthetic material. CAMERA: inherit 1:1. MOTION: 1:1 transfer with modern cloth physics on hoodie, denim and sneakers. SOUND FX: source ambience retained. VIBE: period grade, filmic grain, high contrast. NEGATIVE: no costume drift, no morphing, no period elements bleeding onto the modern outfit, no face flicker, no background wobble, no anachronism in the untouched parts of the frame.
```

## 09 - Close-Up Expression Hold

```text
Replace the face in the source close-up with the character from @image1 - exact same facial structure, skin texture, hair edge and expression timing as the source performance. Framing, background and everything outside the subject unchanged. IDENTITY LOCK: this is a close-up, so the face must be absolutely stable - no breathing distortion, no jaw drift, no eye-size shift, no hairline movement, no reversion for a single frame. Skin texture with real pores, not smoothed plastic. LIGHT: preserve the source key exactly with correct falloff across the nose and cheekbone, catchlights in both eyes matching the source position. CAMERA: inherit 1:1, hold the same framing. MOTION: micro-expressions transferred precisely - blink timing, brow movement, subtle mouth tension. SOUND FX: source ambience retained. VIBE: [GRADE], fine grain, shallow depth of field. NEGATIVE: no morphing, no waxy skin, no dead eyes, no asymmetric drift, no hair flicker, no edge halo, no jitter.
```

## 10 - Wide Environment Walk

```text
Replace the walking figure in the source video with the character from @image1 - same face, build, height and outfit. Identical stride, pace, path and arrival timing. Environment and all other figures untouched. IDENTITY LOCK: face and outfit stable at distance and as the subject moves closer to camera, no scale-dependent drift, no detail loss on the face in wide framing. LIGHT: preserve source ambient and key, correct full-body shadow cast on the ground matching the source shadow direction and length. CAMERA: inherit 1:1 including any track or pan. MOTION: 1:1 gait transfer, correct heel-to-toe contact with the ground, no sliding or skating, cloth physics through the full stride, arms swinging naturally. SOUND FX: source ambience and footstep presence retained. VIBE: [GRADE], filmic grain, wide lens character. NEGATIVE: no floating, no foot sliding, no shadow mismatch, no scale jump, no morphing at distance, no identity flicker, no background warp.
```

## When It Breaks

| Problem                   | Fix                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Face reverts mid-clip     | Move identity lock higher; add `no reversion to the original subject at any point`; crop the reference tighter on the face. |
| Wrong person is swapped   | Name the subject by position and clothing rather than role.                                                                 |
| Background wobbles        | Remove invented camera directions and say `inherit the driving video 1:1`.                                                  |
| Feet slide or body floats | Add heel-to-toe contact, contact shadow, and no-skating language.                                                           |
| Outfit color drifts       | State exact colors in recast and identity-lock blocks; add `no outfit colour shift`.                                        |
| Dialogue lands late       | Finish the line one second before the last frame, or generate silently and add voice in post.                               |
| Hands melt                | Shorten the driving clip or avoid hand-crossing sections; prohibit melting fingers and duplicate limbs.                     |

## The One Rule

You are writing a replacement, not a new scene. Protect everything the driving clip already supplies: camera, timing, blocking, and rhythm. Spend prompt detail on identity and failure prevention.
