# Volcano Reel - Tune Out the World

## Classification

**Product Category:** social-media-concept

**Reveal Effect:** calm-chaos-environment-replacement

**Reveal Mechanism:** reference footage preserves a calm beach subject while an erupting volcano, lava, ash, and fleeing background extras transform the surrounding world

**Sequence Type:** reference-video environment transformation

**Filename:** `seq.beach-volcano-calm-contrast-reel.md`

## Description of Resulting Video or Video Sequence

A set of 6-8-second cinematic social-reel clips in which a person lies calmly on a beach wearing playful pink headphones while a volcano erupts and people flee in the background. The hook comes from the immediate contrast between the subject's undisturbed, music-like head movement and the physically realistic panic surrounding them.

## Usage

Perfect for short-form social reels, creator-led visual-effects concepts, music-driven edits, surreal lifestyle content, and reference-video transformations.

Ideal for a wide establishing angle paired with a top-down close-up, with optional low-ground and over-the-shoulder inserts cut together on the beat.

## Engines/Models

Originally designed for Seedance 2.5. Use a model that supports a source video as `@Video1`, a prop image as `@Image2`, identity and motion preservation, environment replacement, realistic physical simulation, and diegetic audio generation.

Source: [VOLCANO REEL - WORKFLOW SHEET by @by.jadla - Tune out the world](https://literate-aurora-778.notion.site/VOLCANO-REEL-WORKFLOW-SHEET-by-jadla-Tune-out-the-world-3d0f0dc2f654800384b7ca3b2c1d8a5a), version 1.0.

## Prerequisites / Dependencies

- Dependency #1 - `@Video1`: footage of the subject lying on a beach with eyes closed and head gently swaying to music. Shoot a wide angle with the whole body and visible sky plus a top-down close-up of the face. Do not wear headphones in the source footage. Golden-hour side light works best.
- Dependency #2 - `@Image2`: generated product reference of the headphones used throughout the sequence.
- Dependency #3 - Headphone image prompt: "A pair of oversized wireless over-ear headphones, bubblegum pink, glossy candy finish with soft matte pastel ear cushions, chunky playful proportions, cute cartoon sticker details (tiny star and cloud) on the ear cups. Fun, slightly goofy character, but high-quality material. Product shot on a plain white background, soft even studio light, gentle reflection below, photoreal, centered, square, no glare, no watermark."
- Dependency #4 - Music selected in editing. Do not generate music in the video clips.

## Video Prompt

### How It Works

Film yourself lying on the beach, eyes closed, head gently swaying to music. Seedance 2.5 makes a volcano erupt behind you and people run past in panic - you stay calm. That contrast is the whole film. Shoot two angles: a WIDE (your whole body, sky visible) and a TOP-DOWN CLOSE-UP (your face). No headphones in the footage - the AI adds them. Golden hour light works best.

### Step 1 - Headphone Prompt (Text-to-Image)

A pair of oversized wireless over-ear headphones, bubblegum pink, glossy candy finish with soft matte pastel ear cushions, chunky playful proportions, cute cartoon sticker details (tiny star and cloud) on the ear cups. Fun, slightly goofy character, but high-quality material. Product shot on a plain white background, soft even studio light, gentle reflection below, photoreal, centered, square, no glare, no watermark.

Generate as an image and use as the `@Image2` reference.

### Step 2 - Universal Template

Use with Seedance 2.5. Swap only the `SCENE` line.

```text
@Video1 is the reference - the same person, same place, same light, same camera angle as the footage. Their identity, body and movements stay 100%.

SCENE: a man lies on the beach, eyes closed, headphones on, while a volcano erupts behind him and people run screaming past; he stays calm.

@Image2 is a PROP reference - a pair of glossy pink over-ear headphones with three stickers (star, cloud, lightning bolt). The subject wears them through the ENTIRE video, never removed, matching the image exactly.

The scene plays at real physical speed. Everything inside it moves with real weight, gravity and wind - nothing floats, nothing glides unnaturally.

CAMERA: exactly the reference's framing and movement - keep the subject and their motion; only the scene (background, environment, extras) changes.

LOOK - SONY FX3 CINEMATIC: S-Cinetone color, natural skin tones, golden-hour sun from the side, long warm shadows, soft warm highlight rolloff, subtle organic film grain, rich amber-gold grade, gentle haze, high dynamic range.

LIGHT: the sun from the side as key; any secondary light source in the scene (fire, lava, neon, glow) adds its own deep-color accent and a faint bounce on the subject.

AUDIO - NO music (added in editing). Diegetic only: environment ambience, wind, distant shouts/sounds tied to the scene, the subject's soft breathing. No dialogue, no voiceover.

CONSISTENCY: same person, same place, same framing in every frame; no text, no watermark, no extra people near the subject.
```

**Duration:** 6-8 seconds per clip. Generate each angle as its own small clip, inspect it, and then edit the approved clips together.

**Style:** Photoreal Sony FX3 cinematic realism with S-Cinetone color, natural skin, golden-hour warmth, rich volcanic accents, subtle organic film grain, gentle haze, high dynamic range, grounded motion, and an absurd calm-versus-chaos contrast.

**Scene Setup/Context:**
The same person from `@Video1` lies on the beach with eyes closed and their head gently swaying as though listening to music. Add the exact glossy pink headphones from `@Image2`. An erupting volcano must already be visible within the first second; lava traces the ridge, ash fills the sky, and distant people flee in panic while the subject remains completely calm.

**Timeline/Shot Breakdown:**

0:00-0:01 - Open on the source framing with the volcano already clearly visible. Preserve the subject's exact identity, body, position, light, camera angle, and original head movement. The pink headphones are already present and correctly fitted.

0:01-0:06/0:08 - The volcano erupts behind the subject. Ash drifts, embers fall under gravity, lava follows the ridge, and distant silhouettes run through the background in panic. The subject remains undisturbed with eyes closed and head swaying gently. Keep all motion at real physical speed and maintain the original camera behavior through the end of the clip.

### Extra Angle Variants

Generate each variant as a separate 6-8-second clip using the complete universal template above and replacing only its `SCENE` line.

**Low Ground:**

```text
SCENE: same as before, but camera flat near the sand, looking past his head toward the erupting volcano; his head and headphones a calm silhouette against the fire. Keep him motionless-calm, head swaying gently.
```

**Top-Down:**

```text
SCENE: camera directly above his face looking down; ash motes drift past, amber sky glow at the frame edges, his head tilts slowly to the music. Same man, same headphones, same calm.
```

**Over-the-Shoulder:**

```text
SCENE: camera behind his head toward the chaos: silhouettes running in the distance, lava tracing the ridge, ash cloud huge. He sways undisturbed.
```

**Camera:**
Match each `@Video1` clip exactly. Preserve its framing, angle, movement, subject placement, and motion. Only the environment and distant extras change. Capture a wide shot and top-down close-up as the core sequence; use low-ground and over-the-shoulder variants as optional inserts.

**Lighting:**
Use golden-hour sun from the side as the key light, with long warm shadows and soft highlight rolloff. Fire and lava add a deep-color accent and faint, physically plausible bounce on the subject. Preserve the source footage's light direction and natural skin tones.

**Visual Effects/Technical Details:**
The volcano, lava, ash, embers, wind, and fleeing silhouettes obey real physics. Embers fall, ash drifts, people move at natural speed, and nothing floats or glides unnaturally. Keep background extras distant and never place additional people near the subject. The headphones match `@Image2` exactly and remain on the subject for the entire clip.

**Quality/Technical Requirements:**
Preserve the same person, body, place, framing, source movement, and light in every frame. Maintain stable identity and anatomy, exact prop consistency, physically grounded effects, natural motion, high dynamic range, subtle grain, no text, no watermark, no dialogue, no voiceover, and no generated music.

### Editing

Use hard cuts with no fades. Cut the clips to the beat and add the music yourself. The volcano must already be visible in the first second. Keep the person exactly as filmed while only the world reacts. Generate small clips, check each one, and then cut the approved takes together.

### Instagram Reply Template

> Thanks for the love! The volcano-reel workflow is in this sheet - film yourself lying down with your head moving to music, generate fun headphones, and paste the Seedance prompt in. The AI adds the volcano and the panic - you stay calm. Tag me if you post it!

---

Original concept and workflow: @by.jadla, Volcano Reel, v1.0.
