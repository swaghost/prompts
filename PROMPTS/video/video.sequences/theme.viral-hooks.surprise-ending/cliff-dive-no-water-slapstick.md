# The Cliff Dive With No Water — One-Shot Slapstick Comedy

**Tutorial by Deniz Akkabak (@deniz.akkabak)**

A photoreal, one-take slapstick comedy in Seedance 2.0 — from two ordinary selfies to a fifteen-second gag with a full crowd, a mid-air reveal and a perfect comedic landing.

## Technical Specifications

- **Model:** Seedance 2.0
- **Input:** 2 reference photos (same person)
- **Duration:** 15 seconds
- **Aspect Ratio:** 16:9 horizontal
- **Audio:** Yes (diegetic sound design)
- **Editing:** Zero cuts — single continuous shot
- **Genre:** Surreal slapstick comedy with ultra-realistic execution

## Tutorial Overview

This entire video is a single Seedance 2.0 generation — no editing, no compositing, no second attempt stitched in. The trick is that the prompt is built like a director's shooting script: it locks the actor's identity twice, choreographs the scene beat by beat, pins the camera to one unbroken move, and designs the sound before a single frame exists.

## Step 01 — Preparing the References

### Two Selfies, One Identity Lock

Seedance gets two photos of the same person — and the duplication is the point. The video contains a costume change in plain sight: the character starts in wayfarer sunglasses and removes them mid-shot. A single reference would leave the model guessing what the hidden half of the face looks like, and guessing is where identity drift begins.

**Reference 1 (attach first):** The main character, sunglasses on

- Defines the on-camera starting look
- Sunglasses, curly hair, mustache and goatee
- Full starting costume visible

**Reference 2 (attach second):** The same face, sunglasses off

- Insurance policy for identity consistency
- The bare face that appears after glasses removal
- Ground truth to prevent facial drift

**Why 16:9 horizontal?** The aspect ratio does quiet work here: the gag needs room for a crowd on the bridge, a fall, and a wide final frame with legs against the sky — vertical would crop the punchline.

## Step 02 — Writing the Prompt

### The Anatomy of a One-Shot Gag

The prompt reads long, but it is seven short documents fused together — the same paperwork a real comedy shoot would generate, compressed into one block. Understanding what each section is for makes this template reusable:

**FORMAT:**
The contract: 15 seconds, 16:9, slapstick genre, and the hardest constraint of all — one continuous shot, declared before anything else.

**STYLE:**
"Ultra-realistic natural iPhone footage" plus "one cartoon-logic gag executed photorealistically" — the entire comedic thesis in one line. The world obeys physics; only the joke doesn't.

**REFERENCES:**
Assigns each photo a job and locks identity twice — including the exact handoff rule: after the sunglasses come off, the face must match Reference 2.

**VIDEO PROMPT:**
The scene itself, written in strict story order: hype crowd, skeptical grandmothers, the swagger, the strip-and-salute, the dive, the no-water REVEAL, the THUNK, the kicking legs, the reactions.

**CAMERA:**
One unbroken handheld move that follows the actor over the ledge and drops with him — the camera is a character that commits to the bit.

**SFX:**
No music, all diegetic: cheering, seagulls, the sunglasses click, wind rush, the dirt THUNK, muffled grumbling, Italian muttering. Sound sells the impact more than the pixels do.

**NEGATIVE PROMPT:**
The guardrails — and the funniest section to read: no water anywhere (protecting the reveal), no flagpole, no flag, no speedo. Every item is a failure mode banned by name.

## The Verbatim Prompt

### SEEDANCE 2.0 · 15S · 16:9 · ONE CONTINUOUS SHOT · WITH AUDIO

**FORMAT:** 15s / 16:9 / surreal slapstick comedy / one continuous shot, no cuts

**STYLE:** Ultra-realistic natural iPhone footage texture, handheld authenticity, vivid saturated summer colors, crisp daylight, real-world physics with one cartoon-logic gag executed photorealistically, subtle motion blur, no CGI feel.

**REFERENCES:** Reference 1 = the man, main character: preserve his exact face, curly brown hair, mustache and goatee, body proportions, black wayfarer sunglasses at the start. He wears loose knee-length board shorts under a grey t-shirt. Identity locked. Reference 2 = the same man's face without sunglasses: after removing sunglasses his face must match Reference 2 exactly. Same person throughout.

**VIDEO PROMPT:** One continuous shot, no cuts. Summer midday on an old Italian stone bridge. The man from Reference 1 stands near the bridge ledge. Around him, a lively mixed crowd of attractive young women and men in colorful beach outfits cheer him on in English — "Jump! Jump! Do it! You got this!" — clapping and filming with phones. Off to the side, two elderly Italian ladies back from the market with woven vegetable bags watch with skeptical amusement, one shaking her head. He smirks with total confidence, climbs onto the stone ledge with cool swagger, pulls off his grey t-shirt and tosses it, calmly removes his sunglasses and sets them on the ledge — his bare face matching Reference 2. He flexes once, salutes the crowd, and leaps off in a perfect stylish cliff-diving arc. The camera swings over the ledge following him down — REVEAL: there is NO water. Below is a vast dry cracked-earth basin, dusty and sun-baked. He plummets and his head plants straight into the soft dry soil with a comedic THUNK and a big dust puff — his body stays stuck perfectly vertical and upside down, head buried in the ground, torso and legs pointing straight up at the sky, loose board shorts visible, legs kicking and wiggling helplessly in the air. Above, the crowd leans over the ledge gasping then bursting into laughter; the elderly ladies peer down unimpressed, one muttering with a dismissive hand wave before they shuffle off. His muffled voice grumbles from the dirt as his legs keep pedaling.

**CAMERA:** Natural handheld iPhone at eye level on the bridge, tracks his swagger walk, tips over the ledge following the dive, drops WITH him in one unbroken move, lands to a low wide angle on the planted body, legs kicking against the sky. No cuts, no zoom snaps.

**SFX:** Mixed male and female cheering in English, whistles, seagulls, paper bags rustling, fabric toss, sunglasses click on stone, wind rush during fall, deep comedic dirt THUNK, dust hiss, muffled grumbling, elderly lady muttering in Italian, laughter echoing. No music.

**NEGATIVE PROMPT:** no identity change, no face distortion, no cartoon look, no cheap CGI, no water anywhere, no morphing, no plastic skin, no flat lighting, no limb distortion, no flagpole, no flag, no speedo, no tight briefs.

## Key Directing Notes

### Physical Comedy Needs Precise Physical Language

- "head plants straight into the soft dry soil"
- "body stays stuck perfectly vertical"
- "legs kicking and wiggling helplessly"

These specific descriptions leave the model no room to improvise the punchline.

### Background Characters Get Personalities, Not Headcounts

A crowd that chants specific words ("Jump! Jump! Do it! You got this!") and two grandmothers with a specific opinion generate reactions worth watching.

### The Reveal Works Through Strategic Withholding

The water is never mentioned until the camera goes over the ledge, and then only to deny it. The prompt withholds information the same way the video does.

### Sound Design Sells the Impact

Diegetic audio creates realism: cheering, seagulls, sunglasses click, wind rush, the THUNK, muffled grumbling, Italian muttering. Sound sells the impact more than the pixels do.

## Scene Beat Structure

1. **The Hype:** Crowd cheering, elderly skeptics watching
2. **The Swagger:** Confident climb onto ledge
3. **The Strip:** T-shirt toss, sunglasses removal (identity switch to Reference 2)
4. **The Salute:** Flex and salute to crowd
5. **The Dive:** Perfect cliff-diving arc
6. **The Reveal:** Camera follows over — NO WATER, dry cracked earth
7. **The Plant:** Head-first THUNK into soft soil, dust puff
8. **The Punchline:** Body stuck vertical, legs kicking helplessly upward
9. **The Reactions:** Crowd laughing, grandmothers unimpressed and leaving

## Camera Movement Choreography

- **Start:** Natural handheld iPhone at eye level on bridge
- **Track:** Follows swagger walk
- **Commit:** Tips over ledge with the dive
- **Drop:** Falls WITH the character in one unbroken move
- **Land:** Low wide angle on planted body, legs against sky
- **No cuts, no zoom snaps**

## Technical Requirements for Reusability

### Identity Lock Protocol

- Reference 1: Starting appearance with accessories
- Reference 2: Same person without accessories
- Explicit handoff instruction in prompt ("his face must match Reference 2 exactly")

### Continuous Shot Declaration

- Stated in FORMAT section
- Reinforced in VIDEO PROMPT ("One continuous shot, no cuts")
- Camera movement described as unbroken journey

### Sound as Character

- All diegetic, no music
- Specific sound effects called out by name
- Audio cues reinforce physical comedy beats

### Negative Prompt as Guardrails

- Protect the reveal (no water anywhere)
- Ban specific failure modes (no flagpole, no flag, no speedo)
- Prevent identity drift (no identity change, no face distortion)

## Result: Fifteen Seconds, Zero Cuts, One THUNK

The finished one-shot delivers every beat exactly where the prompt placed them:

- The confidence build on the ledge
- The sunglasses set down (clean switch to Reference 2 face)
- The stylish arc
- The camera committing over the edge
- The dry-basin reveal
- The vertical plant with legs pedaling at the sky
- The grandmothers delivering the silent review

**One generation, straight out of Seedance 2.0.**

## Reusable Template Philosophy

**"Comedy is direction, not luck."**

Every laugh in this clip was written before the render: the swagger, the reveal, the THUNK, the kicking legs, even the unimpressed Italian grandmothers.

**To adapt this template:**

1. Prepare two reference photos (with/without costume element)
2. Design your reveal (what surprise comes after the commit)
3. Choreograph the camera as a character that commits to the bit
4. Write precise physical language for the punchline
5. Give background characters personalities and specific reactions
6. Design diegetic sound that sells the impact
7. Use negative prompts to protect your reveal and ban failure modes

---

_Created & written by Deniz Akkabak · Instagram @deniz.akkabak · © 2026_
