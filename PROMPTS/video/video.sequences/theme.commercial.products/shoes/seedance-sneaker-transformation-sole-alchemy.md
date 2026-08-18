# Sole Alchemy — Sneaker Transformation Spell

**Tutorial by:** Deniz Akkabak (@deniz.akkabak)  
**Pipeline:** Nano Banana Pro → Seedance 2.5  
**Platform:** invideo  
**Format:** 9:16 vertical, 20 seconds, single continuous shot  
**Concept:** Product transformation through three colorways with physics-based material transitions

---

## Overview

A sneaker transformation spell in two generations — Nano Banana Pro conjures the editorial opening frame from your own photo, then Seedance 2.5 transmutes the shoe through three colorways in one continuous 20-second shot.

**The Magic:** A shoe floats between two hands, dismantles into its real materials (suede panels, laces, threads), and reweaves itself into the next colorway — twice — before duplicating into a proper left-and-right pair that lands on the wearer's feet. No glow, no sparks, no smoke; the ban on fantasy effects is precisely what makes it feel supernatural.

---

## Pipeline at a Glance

### Stage 1: Conjure the Frame (Nano Banana Pro)

Nano Banana Pro fuses your portrait (Image A) with the product sheet (Image B) into one editorial still: the shoe razor-sharp in mid-air, you soft-focused behind it. This becomes @Image 1 of the video.

### Stage 2: Cast the Spell (Seedance 2.5)

Seedance 2.5 — selected from invideo's model picker — takes that still plus three sneaker sheets and runs a five-stage transformation in a single continuous 20-second shot.

---

## Step 01: Nano Banana Pro — Conjuring the Opening Frame

### Inputs Required

- **Image A:** Your own photo (strict identity lock — face, hair, skin, eyewear stay untouched)
- **Image B:** The product sheet (here the green sneaker's multi-panel sheet)

### Critical Design Logic

The prompt directs the photograph like a set of blocking notes:

- Which hand enters from where
- Where the product floats
- **CRITICAL FOCUS LOGIC:** Puts the shoe on the focal plane and the face in soft blur

That inversion — **product sharp, human soft** — is what makes the frame read as a premium campaign instead of a portrait holding a shoe.

---

## Nano Banana Pro Prompt — Copy Exactly

```
NANO BANANA PRO · VERTICAL · TWO REFERENCES: IMAGE A + IMAGE B

Use Image A as the strict identity lock for the person: preserve their exact facial features, hairstyle, hair color and texture, facial hair if present, skin tone with no idealization, and any eyewear they are wearing in the reference — if Image A shows the person wearing glasses or sunglasses, keep them on the face unchanged.

Composition — a vertical editorial product shot, described precisely: the person stands centered, facing the camera against the backdrop. Their RIGHT hand enters the frame from the upper area, raised to roughly face height, fingers spread downward in an elegant relaxed claw — as if they have just released or are delicately suspending the product in mid-air with invisible control. Their LEFT hand waits below at roughly chest-stomach height, palm open and turned upward in a soft receiving gesture. The product from Image B floats in mid-air in the vertical gap between the two hands, positioned in the exact center-foreground of the frame, closer to the camera than the person, tilted at a slight dynamic three-quarter angle that shows its most recognizable side.

CRITICAL FOCUS LOGIC: the product is the sharpest element in the image, rendered in crisp macro-level detail — material, texture, edges, and branding exactly as in Image B with no redesign; the person's face and body sit slightly behind in soft focus, recognizable but gently blurred, eyes looking straight into the camera through the gap between the product and the hands.

Scale and physics: render the product at a believable real-world size relative to the hands — a sneaker spans roughly two hand-lengths, sunglasses roughly one palm-width, a watch or ring smaller than the palm — floating with a subtle sense of suspended weight, no strings, no stand, no support. Both hands show natural skin texture, knuckle creases, and realistic finger spacing.

Wardrobe: an elevated minimal outfit in soft neutral tones — an oversized cream-ivory wool overshirt or coat with visible fabric texture, worn over a simple tonal base layer — unless Image A clearly establishes a different signature style, in which case echo that style in neutral tones so the product remains the only strong color statement in the frame.

Background: a seamless luxury white studio backdrop with a very subtle vertical gradient — soft warm white falling into a faint cool grey-white, premium and minimal, with gentle studio depth behind the person.

Editorial photographic treatment: shot like a premium eyewear campaign, 85mm f/2 look — shallow depth of field with the focal plane locked on the floating product, soft even studio light with one broad diffused key from the front-left, delicate highlight roll-off on the product's surfaces, natural skin texture in the blurred zones, no digital smoothing.

Constraints: identity locked to Image A with no drift; the product locked to Image B with no redesign, no color shift, no invented branding, no duplicated or morphed parts; exactly two hands, anatomically correct with no extra fingers; the product floats free with no visible support; background stays clean luxury white gradient with no props, no text, no watermark.
```

**Output:** The editorial still — shoe pin-sharp between the hands, the person soft behind it. This image becomes @Image 1 of the video.

---

## Step 02: Setting Up Seedance 2.5 Inside invideo

1. Open invideo's generative models catalog
2. Pick **Seedance 2.5** from the Video row (sits next to Seedance 2.0, Kling, Veo)
3. This tutorial requires Seedance 2.5 specifically because a five-stage transformation needs its 20-second single-generation window

### Reference Images — Attach in This Order

1. **@Image 1:** Person & opening pose (from Step 01)
2. **@Image 2:** Green sneaker sheet
3. **@Image 3:** Blue sneaker sheet
4. **@Image 4:** Brown sneaker sheet

### Settings

- **Duration:** 20s
- **Aspect:** Portrait (9:16)
- **Outputs:** x1
- **Mode:** Seedance 2.5 · Reference to Video

---

## Step 03: The Seedance 2.5 Prompt — Copy Exactly

```
SEEDANCE 2.5 · 9:16 · 20S · SINGLE CONTINUOUS SHOT · REFERENCE TO VIDEO

FORMAT: 20s / 9:16 / cinematic sneaker transformation / single continuous shot

STYLE: Photorealistic smartphone capture with cinematic polish: sharp phone sensor detail, natural micro-shake, realistic autofocus, soft studio daylight, seamless backdrop, subtle grain, real-world physics, no fantasy glow.

REFERENCES:
@Image 1 defines the person: preserve their exact face, hair, wardrobe and accessories, no changes. Also defines the opening pose: green sneaker floating between their hands.

@Image 2: multi-panel sheet of the SAME single green suede sneaker, beige sole. Design detail only; ignore the panel grid, never render split-screen.

@Image 3: multi-panel sheet of the SAME single light-blue suede sneaker, pale-yellow and green sole. Design detail only; ignore panel layout.

@Image 4: multi-panel sheet of the SAME single brown-and-tan sneaker, dark grey sole. Design detail only; ignore panel layout.

VIDEO PROMPT:

[Stage 1 - approx 0-4s] The person centered, right hand raised above, left palm open below, the green sneaker suspended in the gap between their hands, rotating on its vertical axis. Camera: one continuous push-in from wide to a chest-height medium shot. Their fingers glide around the floating shoe without touching it; hands stay normal, no light or particles. End state: medium framing, green shoe rotating.

[Stage 2 - approx 4-9s] Mid-rotation the green sneaker separates into its real materials: suede panels lift apart, laces unravel, fine threads drift in a tight controlled cloud between their hands, then weave back together into the blue sneaker from @Image 3. Clean minimal particulation, no sparks, no glow, no smoke. End state: one blue sneaker rotating in place.

[Stage 3 - approx 9-13s] The blue sneaker disassembles the same way, reassembling into the brown sneaker from @Image 4. End state: one brown sneaker rotating between their hands.

[Stage 4 - approx 13-16s] The brown sneaker duplicates with a brief subtle spatial blur: a mirrored second sneaker slides out of the first; the pair hovers side by side as correct left and right shoes. End state: exactly two brown sneakers floating.

[Stage 5 - approx 16-20s] The person presses both palms gently downward. The pair glides down, aligns with their feet and wraps onto them, laces settling. They turn and walk out of frame with relaxed confident strides; camera holds, slight tilt-down to the shoes. Hard stop.

AUDIO: <soft room tone, fabric and thread whispers at each disassembly, low whoosh as the pair descends, two subtle sole impacts, fading footsteps> No dialogue, no music.

CONSISTENCY: Keep the person's face, wardrobe, accessories, lighting unchanged. Exactly one person. One shoe in Stages 1-3, exactly two in Stages 4-5.

NEGATIVE PROMPT: no glowing hands, no magic energy, no sparks, no smoke, no split-screen, no panel borders, no duplicate person, no face distortion, no wardrobe change, no extra shoes, no cartoon, no cheap CGI, no leftover debris, no text, no watermark.
```

---

## Anatomy — Why the Spell Holds

### 1. One Still, Two Jobs

@Image 1 carries both the identity and the opening pose — because Step 01 staged the exact first frame, the video begins already composed, and Seedance spends zero seconds finding its shot.

### 2. The Sheet Waiver, Three Times

Every sneaker reference is a multi-panel sheet, so each one repeats the same clause: **design detail only, ignore the panel grid, never render split-screen**. One waiver per sheet keeps four references from leaking layouts.

### 3. Materials, Not Magic

The transformation is engineered from **real components** — suede panels lift, laces unravel, threads reweave — while the negative prompt bans glow, sparks and smoke. Physics-based transitions are what let a supernatural event pass the eye's realism check.

### 4. End States as Checkpoints

Every stage closes with an explicit **End state** line:

- Green rotating
- One blue
- One brown
- Exactly two
- Worn and walking

Checkpoints stop a 20-second morph chain from drifting mid-sequence.

### 5. Counted Objects

CONSISTENCY pins the arithmetic: **one person, one shoe in Stages 1-3, exactly two in Stages 4-5** — and the pair is specified as correct left and right shoes. Object counts are where transformation videos usually break; this prompt locks them by name.

### 6. Sound of Craft, Not Sorcery

The audio is thread whispers, a low whoosh, two sole impacts, fading footsteps — **no music, no dialogue**. Quiet, material sound keeps the spell inside the same realism contract as the visuals.

### 7. The Insurance

The negative prompt closes every classic failure at once:

- Glowing hands and magic energy (tone drift)
- Split-screen and panel borders (sheet leakage)
- Duplicate person and extra shoes (count drift)
- Leftover debris (incomplete reassembly)

---

## Expected Output

**Twenty seconds, three shoes, one pair:**

- Push-in lands on chest-height medium exactly as Stage 1 orders
- Each disassembly stays a tight thread cloud with nothing glowing
- Pair appears as true mirrored left-and-right shoes
- Film ends on tilt-down and hard stop
- Five end states, five delivered

---

## Key Techniques

### Physics-Based Transformation

- Real materials: suede panels, laces, threads
- No fantasy effects (no glow, sparks, smoke)
- Controlled particulation during transitions
- Believable weight and scale

### Staged Prompt Architecture

- Five explicit stages with timecodes
- End state checkpoints prevent drift
- Object counting (one shoe → two shoes)
- Camera movement integrated (push-in, tilt-down, hard stop)

### Reference Image Strategy

- Opening still defines both identity and starting pose
- Multi-panel product sheets with explicit waivers
- Design detail locked, layout ignored
- Prevents split-screen leakage

### Audio Design

- Diegetic sound only (fabric, threads, impacts, footsteps)
- No music, no dialogue
- Material-based audio reinforces realism

---

## Adaptation Notes

This template works for any product transformation:

- Swap sneakers for sunglasses, watches, jewelry, phones
- Adjust scale in Nano Banana prompt (sneaker = two hand-lengths, watch = smaller than palm)
- Maintain materials-based transformation logic
- Keep end states explicit for each stage
- Ban fantasy effects in negative prompt

**Platform:** Runs inside invideo where Seedance 2.5 sits in the model picker alongside frontier lineup.

---

**Source:** Deniz Akkabak (@deniz.akkabak) · invideo.io/i/DENIZ-ig  
**Tutorial Type:** Two-stage pipeline (image generation → video transformation)  
**Core Innovation:** Physics-based product morphing with explicit stage architecture and checkpoint system
