# UGC Videos with Node-Based Workflows — Authentic Ads at Scale

## Description

Create high-quality User Generated Content (UGC) style videos using AI-powered node-based workflows. Build authentic-looking product ads with real people, cinematic camera movements, and TikTok-style effects — then automate the entire pipeline to generate 10+ variations with different products or characters in one click. Uses Arcads (node workflow platform), Higgsfield Soul 2.0 (character generation), GPT Image 2 (scene composition), and Seedance 2.0 (animation). Perfect for social media ads, product launches, influencer-style content, and brand campaigns that need authentic, scroll-stopping video at scale.

## Tools Required

- **Arcads** — Node-based AI workflow platform for automation
- **Higgsfield Soul 2.0** — AI image generation for base character images
- **GPT Image 2** — Advanced scene composition and character reference sheets
- **Seedance 2.0** — Video animation from still images
- **Video editing software** (optional) — For final stitching and refinement

## What You'll Learn

- Understanding node-based workflow systems
- Creating authentic UGC-style character images
- Building multi-angle character reference sheets
- Writing extremely detailed animation prompts for Seedance 2.0
- Implementing TikTok-style video effects (whip pans, zoom pulses, snap cuts)
- Automating video generation pipelines
- Swapping products/characters while maintaining consistency
- Stitching multiple clips for seamless UGC ads

---

## Complete Workflow

### Overview

**5-Phase Process:**

1. Generate base character image (Higgsfield Soul 2.0)
2. Create character reference sheet (GPT Image 2)
3. Compose scene with product (GPT Image 2)
4. Animate with detailed effects (Seedance 2.0)
5. Build node workflow for automation (Arcads)

**Duration:** 2-3 hours for initial setup, 10 minutes for variations  
**Difficulty:** Advanced  
**Output:** Professional UGC video ads with automation pipeline

---

## Understanding Node-Based Workflows

### What Are Node Workflows?

**Concept:** Work on infinite canvas where each node represents an action, connected together to create automated pipelines.

**Basic structure:**

```
[Prompt Node] → [Image Node] → [Video Node] → [Output]
```

**Real example:**

```
[Product Description] → [Generate Image] → [Animate with Seedance] → [Final Video]
```

---

### How Nodes Work

**Each node is an action:**

- Text prompt input
- Image generation (Higgsfield, GPT, etc.)
- Video animation (Seedance 2.0, Veo, etc.)
- Character reference
- Product reference
- Video modification
- Output/export

**Connecting nodes:**

1. Drag from output handle of one node
2. Drop onto input handle of next node
3. Data flows through connection automatically

**Running workflows:**

- Single node: Click "Run" on that node
- Multiple nodes: Select all, click "Run" once
- Entire pipeline executes automatically

---

### Why Node Workflows Are Powerful

**Automation at scale:**

- Set up once, run infinite variations
- Change one input, entire pipeline updates
- 10 products = 10 videos with one click
- 10 characters = 10 variations simultaneously

**Modular flexibility:**

- Swap any step without rebuilding
- Test different AI models at each stage
- Branch workflows for A/B testing
- Reuse components across projects

**Visual organization:**

- See entire pipeline at a glance
- Understand dependencies clearly
- Debug specific nodes easily
- Share workflows with team

---

## Phase 1: Generate Base Character Image

**Tool:** Higgsfield Soul 2.0  
**Goal:** Create ultra-realistic UGC-style character for your ad

### The UGC Aesthetic

**What makes it "UGC":**

- No makeup or minimal makeup
- Raw, unfiltered skin texture
- Natural lighting (not studio-perfect)
- Casual, candid expressions
- Authentic environment (car, home, cafe)
- Horizontal/selfie camera angle
- Visible imperfections (the point is realism)

---

### Base Character Prompt Template

**Paste into Higgsfield Soul 2.0:**

```
Young blonde woman, mid 20s, straight or loosely wavy blonde hair worn naturally down, soft defined brows, completely bare face — no makeup, no product, no tinted skin. Raw realistic skin texture: visible pores, natural sebum sheen, subtle uneven tone, faint blemishes or skin variation where natural. Seated in the driver's seat of a Tesla, horizontal selfie framing — camera held at arm's length or propped, shot in landscape orientation at near eye level. Gaze directed straight into lens, relaxed and candid. Wearing a fitted white top. Tesla white interior surrounds her — white vegan leather seat. Ambient natural daylight through the panoramic windshield as primary light source, soft and diffused, wrapping evenly across her bare skin and hair with no harsh shadows. Background: Tesla cabin interior softly out of focus, clean white tones with subtle depth. Frame shows shoulders up to mid chest. Zero skin smoothing, zero airbrushing, zero digital correction — skin looks exactly as it would in an unfiltered front camera photo. Authentic candid UGC energy.
```

---

### Prompt Breakdown

**Physical description:**

- "Young blonde woman, mid 20s" → Age range and hair color
- "Straight or loosely wavy blonde hair worn naturally down" → Hair texture and style
- "Soft defined brows" → Facial feature specificity
- "Completely bare face — no makeup, no product, no tinted skin" → UGC authenticity

**Skin texture (critical for UGC):**

- "Raw realistic skin texture: visible pores, natural sebum sheen"
- "Subtle uneven tone, faint blemishes or skin variation where natural"
- "Zero skin smoothing, zero airbrushing, zero digital correction"
- "Skin looks exactly as it would in an unfiltered front camera photo"

**Environment:**

- "Seated in the driver's seat of a Tesla" → Specific, relatable setting
- "Horizontal selfie framing — camera held at arm's length or propped"
- "Shot in landscape orientation at near eye level" → TikTok/social media format

**Lighting:**

- "Ambient natural daylight through the panoramic windshield as primary light source"
- "Soft and diffused, wrapping evenly"
- "No harsh shadows" → Natural, not staged

**Camera & framing:**

- "Horizontal selfie framing" → Social media standard
- "Gaze directed straight into lens" → Direct engagement
- "Relaxed and candid" → Not posed
- "Frame shows shoulders up to mid chest" → Typical UGC crop

---

### Customization for Different Demographics

**Young man (20s):**

```
Young man, early 20s, short dark hair with natural texture, strong jawline, minimal facial hair or clean-shaven, completely natural appearance — no grooming products visible. Raw realistic skin texture: visible pores, natural skin tone with subtle variation, maybe slight stubble shadow. Seated in passenger seat of modern car, horizontal selfie framing — camera held at arm's length, shot in landscape orientation. Direct eye contact with lens, confident but casual expression. Wearing plain black t-shirt. Car interior modern and clean, soft natural daylight from side window. Background slightly out of focus. Frame shows shoulders to mid chest. Zero skin retouching — authentic unfiltered phone camera quality. Natural UGC energy.
```

**Woman (30s, professional):**

```
Woman in her early 30s, shoulder-length brown hair with natural waves, minimal everyday makeup — light foundation only, soft natural brows, no dramatic contouring. Realistic skin texture: fine lines around eyes visible, pores showing, natural skin variation. Seated at home office desk, horizontal selfie angle — camera slightly above eye level, landscape orientation. Warm natural window light from left side. Wearing casual sweater or button-up. Background: home office softly blurred, bookshelves or plants visible. Direct gaze to camera, friendly and approachable expression. Frame shows upper chest to top of head. Natural lighting with slight overexposure from window — authentic work-from-home aesthetic. Real skin, real environment, unfiltered.
```

**Man (40s, casual professional):**

```
Man in his 40s, salt-and-pepper short hair, natural facial lines, laugh lines around eyes, authentic aging features — no smoothing. Realistic skin texture: visible pores, slight weathering, natural skin tone variation. Seated in kitchen or living room, horizontal framing at natural arm's length. Wearing casual button-down or polo shirt. Soft ambient interior lighting with natural window light supplementing. Direct eye contact with camera, relaxed smile or neutral expression. Background: kitchen counters or living room softly out of focus, realistic home environment. Zero retouching, zero corrections — looks like a real person recording a testimonial from home.
```

---

### Critical UGC Elements

**Always include:**

1. **"Completely bare face" / "minimal makeup"** → Authenticity
2. **"Raw realistic skin texture: visible pores"** → Prevents AI over-smoothing
3. **"Natural sebum sheen" / "natural skin variation"** → Real skin behavior
4. **"Horizontal selfie framing"** → Social media format
5. **"Camera held at arm's length or propped"** → Authentic angle
6. **"Ambient natural daylight"** → Not studio lighting
7. **"Zero skin smoothing, zero airbrushing, zero digital correction"** → Forces realism
8. **"Unfiltered phone camera photo"** → Sets expectation for AI

**Why this matters:**

- AI defaults to "beauty shot" perfection
- UGC buyers want _authentic_, not perfect
- Brands distrust overly polished AI content
- Real texture = believable testimonial

---

## Phase 2: Create Character Reference Sheet

**Tool:** GPT Image 2  
**Goal:** Multi-angle reference for consistent character across shots

### Why Character Sheets Matter

**Problem without reference sheet:**

- AI generates different face each time
- Character inconsistency kills believability
- No way to reuse character in new scenes

**Solution with reference sheet:**

- Consistent face from any angle
- Can generate unlimited scenes with same person
- Reference for video animation (Seedance 2.0)
- Enables automation (swap characters systematically)

---

### Character Reference Sheet Prompt

**Paste into GPT Image 2:**

```
Character reference sheet, four-panel layout on a pure white seamless studio background. Four head angles of the same young woman — mid-20s, light golden-tanned complexion with warm undertones, long straight blonde hair with natural highlights ranging from platinum to honey, scattered light freckles across the nose and upper cheeks, full lips with a natural mauve tone, strong arched brows slightly darker than the hair, hazel-green eyes, prominent bone structure with a defined jawline and soft cheekbones. No makeup or very minimal — natural lashes only.

Panel 1 — Front facing: Full frontal head and shoulders, direct neutral gaze at camera, relaxed expression, hair falling loosely over both shoulders.

Panel 2 — Left profile: Clean 90-degree left side profile, hair swept back to fully reveal the jaw, ear, and neck line, gaze directed forward.

Panel 3 — Right profile: Clean 90-degree right side profile, mirroring the left, same relaxed neutral expression.

Panel 4 — Back of head: Rear view, hair hanging straight down the back, showing natural blonde hair texture, volume at the crown, and slight movement at the ends.

All four panels shot with an 85mm studio lens, soft large diffused key light from front-above with gentle fill from below to eliminate harsh shadows, clean even separation from the white background. Skin rendered with full visible texture — fine pores, natural freckle variation, subtle warmth across the nose bridge, zero retouching or smoothing. Hair shows individual strand separation, natural flyaways at the crown, realistic weight and fall. Fashion casting card aesthetic, clinical four-view character reference quality, 8K resolution, tack-sharp focus on all panels.
```

---

### Prompt Breakdown

**Layout structure:**

- "Four-panel layout on a pure white seamless studio background"
- Clear separation, professional reference format

**Physical specificity:**

- "Light golden-tanned complexion with warm undertones"
- "Long straight blonde hair with natural highlights ranging from platinum to honey"
- "Scattered light freckles across the nose and upper cheeks"
- "Hazel-green eyes, prominent bone structure"

**Four required angles:**

1. **Front facing** — Main reference, direct eye contact
2. **Left profile** — 90-degree side view, hair swept back
3. **Right profile** — Mirrored angle
4. **Back of head** — Shows hair texture and volume

**Why these specific angles:**

- Front: Most common shot in UGC
- Profiles: Side-angle testimonials, looking at product
- Back: Transitional shots, hair product ads, environmental depth

**Technical quality:**

- "85mm studio lens" → Portrait lens standard
- "Soft large diffused key light from front-above" → Professional but natural
- "8K resolution, tack-sharp focus" → Maximum detail for AI reference

---

### Customization for Different Characters

**Young man character sheet:**

```
Character reference sheet, four-panel layout on pure white seamless background. Four angles of the same young man — early 20s, warm tan skin tone, short dark brown hair with natural texture and slight wave, strong defined jawline, straight nose, warm brown eyes, full eyebrows, clean-shaven or very light stubble. Natural masculine features, athletic build visible in shoulders.

Panel 1 — Front facing: Direct gaze, neutral expression, shoulders squared to camera.
Panel 2 — Left profile: 90-degree side view, showing jawline and nose profile clearly.
Panel 3 — Right profile: Mirrored, same neutral expression.
Panel 4 — Back of head: Showing hair texture, crown, and neck.

85mm studio lens, soft even lighting, visible skin texture with pores and natural variation, zero retouching. Fashion casting reference quality, 8K resolution.
```

**Mature woman (40s) character sheet:**

```
Character reference sheet, four-panel layout on pure white seamless background. Four angles of the same woman — early 40s, fair skin with natural aging visible (fine lines around eyes, slight nasolabial folds), shoulder-length brown hair with subtle grey strands, warm hazel eyes, natural smile lines, authentic mature beauty.

Panel 1 — Front facing: Warm friendly expression, direct gaze.
Panel 2 — Left profile: Natural profile showing authentic aging features.
Panel 3 — Right profile: Mirrored angle.
Panel 4 — Back of head: Hair texture showing natural grey integration.

85mm studio lens, soft natural lighting, full skin texture detail including fine lines and age spots, zero smoothing or correction. Realistic mature character reference, 8K resolution.
```

---

## Phase 3: Compose Scene with Product

**Tool:** GPT Image 2  
**Goal:** Create specific frame with character holding/using product

### Strategy: Start Frame + End Frame

**For seamless animation, you need:**

- **Start frame** of Clip 1 (character looking at camera)
- **End frame** of Clip 1 (character transitioning)
- **Start frame** of Clip 2 (same as end frame of Clip 1)
- **End frame** of Clip 2 (character with product in new position)

**Why this matters:**

- Allows seamless stitching between clips
- Smooth transitions look professional
- Consistent character position = believable motion

---

### Scene Composition Prompt Template

**Example: Character with matcha drink in car**

**Paste into GPT Image 2:**

```
The woman from the multi-angle reference sheet — preserving her exact facial identity: long straight blonde hair with natural highlights and darker roots, hazel eyes, full lips, scattered freckles across nose and cheeks, warm tan skin tone, thick natural brows. Camera angle, framing, and environment taken entirely from the car photo — same low propped-camera perspective looking slightly upward at the subject, same mid-chest-up horizontal framing, same white ribbed top, same cream leather car interior with seatbelt visible left side, same soft green foliage through rear window, same warm natural daylight flooding in from above. Pose relaxed and laid back — body settled into the seat, shoulders dropped. Both hands wrapped loosely around a clear plastic cup of iced matcha held at chest level — fingers curled naturally around the cup, condensation visible on the outside, straw pointing upward. Both arms bent inward toward the body, elbows down, no arm reaching forward. Head tilted back very slightly, gaze directed upward and to one side — not at the camera. Expression: lips relaxed with a barely-there smile pulling at one corner of the mouth — asymmetric, natural, not posed. Eyes slightly lit up, one brow gently raised, the kind of look that comes right before saying something she shouldn't. Playful and effortless — caught mid-thought with a quiet smirk that hasn't fully landed yet. Hair falling loosely around shoulders with natural movement. Visible skin texture, pores, freckles — zero smoothing. Authentic propped-camera candid realism.
```

---

### Prompt Structure Breakdown

**Character consistency:**

- "The woman from the multi-angle reference sheet — preserving her exact facial identity"
- Lists specific features: hair, eyes, freckles, skin tone, brows
- **Upload reference sheet image alongside this prompt**

**Environment consistency:**

- "Camera angle, framing, and environment taken entirely from the car photo"
- References original base image environment
- "Same low propped-camera perspective looking slightly upward"
- "Same cream leather car interior with seatbelt visible"
- **Upload base car image alongside this prompt**

**Product integration:**

- "Both hands wrapped loosely around a clear plastic cup of iced matcha"
- "Fingers curled naturally around the cup, condensation visible"
- Specific, natural interaction with product

**Expression & pose:**

- "Head tilted back very slightly, gaze directed upward and to one side — not at the camera"
- "Lips relaxed with a barely-there smile pulling at one corner"
- "The kind of look that comes right before saying something she shouldn't"
- Natural, caught-moment authenticity

---

### Product Swap Variations

**Same character, different products:**

**Skincare product:**

```
...Both hands holding a small glass dropper bottle of serum at chest level, left hand supporting the base, right hand holding the dropper cap, about to apply. Bottle shows amber liquid inside, minimalist white label. Gaze directed at the bottle with slight smile, like she's about to share a secret...
```

**Supplement bottle:**

```
...Right hand holding an orange prescription-style bottle of supplements at shoulder height, fingers wrapped around the middle, label facing slightly toward camera. Left hand resting casually on lap. Gaze directed at camera with knowing look, eyebrows slightly raised, like she's recommending it to a friend...
```

**Tech gadget (earbuds):**

```
...Right hand holding open a white charging case for wireless earbuds at chest level, left hand reaching to take one earbud out. Case shows LED indicator light, sleek minimalist design. Gaze directed down at the case with slight smile of satisfaction, natural unboxing moment energy...
```

**Food product (protein bar):**

```
...Both hands holding an unwrapped protein bar at chest level, left hand supporting the bottom, right hand near the top like about to take a bite. Wrapper visible but peeled back, bar shows chocolate coating and texture. Gaze directed at camera with playful anticipatory smile, like she's excited to eat it...
```

---

## Phase 4: Animate with Seedance 2.0

**Tool:** Seedance 2.0  
**Goal:** Create cinematic UGC animation with TikTok-style effects

### The Critical Secret: Extreme Detail

**Standard prompt:**
"Animate the woman in the car turning to face camera, then showing product"

**Result:** Generic, flat animation with no energy

**Seedance 2.0 requires extreme specificity:**

- Frame-by-frame timing
- Exact camera movements
- Effect descriptions
- Motion physics
- Expression changes
- Lighting shifts

**The more detailed your prompt, the better your animation.**

---

### Master Animation Prompt Structure

Seedance 2.0 prompts should include these sections:

1. **IMAGE REFERENCE MAP** — What each uploaded image represents
2. **EFFECTS TIMELINE** — Shot-by-shot breakdown with exact timing
3. **MASTER EFFECTS INVENTORY** — Complete list of all effects used
4. **EFFECTS DENSITY MAP** — How many effects in each time segment
5. **MOTION FLOW** — Overall energy arc of the video

---

### Complete Seedance 2.0 Prompt Example

**Paste into Seedance 2.0 (for 2-shot UGC ad):**

```
IMAGE REFERENCE MAP

Image 1 (car selfie) → First frame / opening scene. Woman in passenger seat taking selfie. Primary talent for Shot 1.

Image 2 (multi-angle portrait sheet) → Woman character reference. Face, hair, skin tone. Minimal freckles.

Image 3 (blonde man multi-angle) → Man reference. Driver seat, primary subject from Shot 2 onward.

SECTION 1: EFFECTS TIMELINE

SHOT 1 / MOMENT (0:00–1:20s) — Snap Open, Woman to Camera

EFFECT: Jump-cut snap open + handheld selfie hold + fast push-in (digital zoom)

The clip opens mid-action — the woman has already whipped the phone up to selfie position. No slow start. Frame snaps into existence on her face, slightly closer than arm's length, filling more of the frame than the reference shot. Energy is already elevated.

She throws a quick look directly into the lens — confident, slightly playful — and delivers: "Let me show you how to do it" fast, punchy, no pause before or after.

As she speaks, the frame auto-pushes in digitally — approximately 8-10% scale increase over the line, landing tighter on her by the last word. Feels like a TikTok zoom-in emphasis.

Handheld micro-bounce on every syllable — the phone has weight, her wrist has movement. Not shaky, but alive.

Her hair has movement — subtle wind or AC from the open window. Skin: natural glow, minimal freckles. White top catching window light.

Transition: she physically FLIPS the camera toward him — fast wrist snap, the frame motion-blurs in the direction of the swing.

SHOT 2 / MOMENT (1:20s–2:20s) — Whip Pivot to Driver

EFFECT: Whip pan (wrist flip) + motion blur smear + rack focus snap

This is the SIGNATURE VISUAL EFFECT — the camera swings hard from her to him in a single fast wrist-turn. The frame motion-blurs mid-rotation, roughly 10-15 frames of directional smear, then snaps sharp on his face.

As the camera lands, focus racks instantly from blurred interior to crisp lock on the curly blonde man. He's already looking toward the camera when it arrives — like he knew it was coming.

His expression: slight grin already forming. Not waiting, not posed — caught mid-smirk.

The camera landing has a tiny overshoot and settle — natural phone physics, not mechanical.

SHOT 3 / MOMENT (2:20s–4:00s) — Man Delivers, Direct Energy

EFFECT: Digital zoom (scale-in, two pulses) + handheld bounce + natural cut or hold

He says: "in under a minute, baby" — British accent, punchy and upbeat. The word "baby" lands with a slight lean toward camera, like he's in on it.

On "in under a minute" — the frame tightens with a fast digital zoom-in, approximately 10-12% over the first three words. Pulls back slightly. Then on "baby" — a second smaller zoom pulse, tight on his face for the payoff word.

Handheld bounce tracks his natural head movement as he speaks. Not stabilized — alive. His curls catch the window light.

He breaks into a fuller grin on the final beat and flicks his eyes back to the road — the clip ends on that moment. Frame holds for half a second on his profile, sun catching his hair, slight smile still visible.

Background: soft bokeh of road and trees through the driver window. Interior feels warm, lit, real.

SECTION 2: MASTER EFFECTS INVENTORY

Snap open (jump-cut entry) — used 1x, Shot 1. No fade, no build — clip starts at full energy.

Digital zoom / push-in (scale-in) — used 3x total. Shot 1 (single push over her line), Shot 3 (two pulses synced to his words). Emulates TikTok emphasis zoom. Each pulse is 8-12% scale increase.

Handheld selfie bounce — used throughout Shots 1 and 3. Micro-movement on every syllable. Wrist-held, not stabilized.

Whip pan (wrist flip pivot) — used 1x, Shot 1-to-2 transition. Fast physical camera rotation. This is the signature kinetic moment of the clip.

Motion blur smear (directional) — used 1x, mid-whip. Approximately 10-15 frames of horizontal blur in the direction of the swing. Resolves sharply on his face.

Rack focus snap — used 1x, Shot 2 landing. Instant focus pull from blurred transition to sharp lock on the man's face.

Natural daylight interior exposure — throughout. Bright window overexposure, raw phone-camera skin rendering. No grade.

Shallow depth of field / bokeh — used in all shots. Background always softer than subject.

SECTION 3: EFFECTS DENSITY MAP

0:00–1:20s = MEDIUM DENSITY (snap open, digital zoom push, handheld bounce, daylight — 3 effects)

1:20–2:20s = HIGH DENSITY (whip pan, motion blur smear, rack focus snap, bokeh shift — 4 effects)

2:20–4:00s = MEDIUM DENSITY (dual zoom pulses, handheld bounce, bokeh, natural hold — 3 effects)

SECTION 4: MOTION FLOW

Opening: No warmup. The clip snaps in hot — she's already talking, camera already up. The zoom-in on her line adds a beat of momentum before anything physically moves.

Build: The whip pan is the peak kinetic moment — it's fast, physical, and the blur-to-snap transition creates a genuine jolt. Everything before it is setup; everything after it is payoff.

Resolution: He delivers the line in two zoom pulses that sync to his rhythm, then the clip eases off — his grin, the road, the light. The energy drops just enough to feel real. It ends relaxed but still charged, the way good influencer content does — you felt something and it didn't try too hard.
```

---

### Prompt Anatomy: Why This Works

**IMAGE REFERENCE MAP section:**

- Tells Seedance which uploaded images to use
- Clarifies role of each image (start frame, character reference, etc.)
- Prevents confusion about which image is which

**EFFECTS TIMELINE section:**

- Shot-by-shot breakdown with exact timing (0:00-1:20s, etc.)
- Describes camera movement, character action, expression
- Details visual effects applied
- Includes dialogue/voiceover timing

**MASTER EFFECTS INVENTORY section:**

- Complete list of every effect used in video
- How many times each effect appears
- Technical specifics (8-10% scale increase, 10-15 frames of blur)
- Helps AI understand full toolkit

**EFFECTS DENSITY MAP section:**

- Shows concentration of effects over time
- Prevents over-animating or under-animating
- Creates rhythm and pacing

**MOTION FLOW section:**

- Describes energy arc: opening → build → resolution
- Emotional journey of the video
- Why effects are chosen for each moment
- Overall storytelling impact

---

### Common TikTok/UGC Effects Library

**Snap open:**

- Jump-cut entry, no fade-in
- Starts mid-action, high energy immediately
- Use at: Video openings

**Digital zoom / push-in:**

- Scale-in effect, 8-12% increase
- Emulates TikTok emphasis zoom
- Use at: Punchline words, key moments

**Handheld bounce:**

- Micro-movement on every syllable
- Phone has weight and wrist movement
- Use throughout: All handheld shots

**Whip pan:**

- Fast physical camera rotation
- Signature kinetic transition
- Use at: Camera flips, subject changes

**Motion blur smear:**

- Directional blur during fast movement
- 10-15 frames of blur
- Use at: Whip pans, fast transitions

**Rack focus snap:**

- Instant focus pull from blurred to sharp
- Cinematic depth effect
- Use at: Landing on new subject after transition

**Zoom pulse:**

- Quick in-and-out zoom
- Synced to music beat or word emphasis
- Use at: Key words, rhythm moments

**Overshoot and settle:**

- Camera momentum effect
- Passes target, then settles back
- Use at: End of whip pans, physical camera moves

---

### Single-Shot Simpler Prompt Template

**For product showcase (one character, one shot):**

```
IMAGE REFERENCE MAP

Image 1 (woman with product) → Start frame. Character holding product at chest level.
Image 2 (character reference sheet) → Face consistency reference.

EFFECTS TIMELINE

SHOT 1 / MOMENT (0:00–3:00s) — Product Reveal

EFFECT: Slow zoom-in + subtle head tilt + natural smile reveal

Opens on the woman in car, holding matcha cup at chest level with both hands. She's looking down at the product with a subtle smile, not at camera yet.

First 0.5 seconds: Static hold, letting viewer register the scene.

0.5–1.5s: Slow digital zoom-in, approximately 5-8% scale increase, moving from mid-chest framing to tighter upper-chest/face framing. Not aggressive — gentle and inviting.

1.5–2.0s: Her head tilts up slowly, gaze shifting from product to camera. Smile broadens naturally as eye contact is made. Feels like she just noticed you watching.

2.0–3.0s: Hold on her face with slight handheld micro-bounce. Eyes bright, genuine smile, product still visible at bottom of frame. Natural daylight catches her hair. Feels authentic and warm.

Background: Soft bokeh of car interior throughout. Natural lighting from window creates soft overexposure on her hair and shoulders.

MASTER EFFECTS INVENTORY

Slow zoom-in (gradual scale increase) — 5-8% over 1 second
Head tilt animation — natural human movement timing
Eye line shift — from product to camera
Expression change — subtle smile to full warm smile
Handheld micro-bounce — throughout final hold
Shallow depth of field / bokeh — consistent background softness
Natural lighting with overexposure — authentic UGC quality

MOTION FLOW

Opening: Calm and inviting, not aggressive. Lets viewer settle into the scene.
Build: Zoom and head tilt create gentle momentum.
Resolution: Eye contact and smile create connection. Holds emotion.
```

---

## Phase 5: Build Node Workflow in Arcads

**Tool:** Arcads  
**Goal:** Create automated pipeline for generating variations

### Setting Up Your First Workflow

**Step 1: Create base nodes**

1. **Text Prompt Node** — Description of your character/scene
2. **Image Generation Node (Higgsfield)** — Connects to text prompt
3. **Character Reference Node (GPT Image 2)** — Character sheet generation
4. **Scene Composition Node (GPT Image 2)** — Character + product image
5. **Video Animation Node (Seedance 2.0)** — Animates the scene

**Step 2: Connect the nodes**

```
[Text Prompt] → [Higgsfield Image] → [GPT Character Sheet]
                                    ↓
[Product Image] → [GPT Scene Composition] → [Seedance Animation] → [Output]
                           ↑
                [Character Sheet Reference]
```

**Step 3: Run the workflow**

- Click on any node and "Run" to test individual step
- Select all nodes and "Run" to execute entire pipeline
- Output appears in final node

---

### Automation: The Power of Node Workflows

**Scenario: 10 products, same character**

**Without automation:**

- Manually create 10 scenes in GPT Image 2
- Manually animate 10 videos in Seedance 2.0
- 2-3 hours of repetitive work

**With node workflow automation:**

1. Create 10 product image nodes
2. Connect each to the scene composition node
3. Connect each scene node to a video animation node
4. Select all, click "Run"
5. **10 videos generate simultaneously in 10 minutes**

---

### Workflow Diagram for Product Variations

```
                    [Character Reference Sheet]
                             ↓
[Product 1 Image] → [Scene Composition 1] → [Video 1] → [Output 1]
[Product 2 Image] → [Scene Composition 2] → [Video 2] → [Output 2]
[Product 3 Image] → [Scene Composition 3] → [Video 3] → [Output 3]
[Product 4 Image] → [Scene Composition 4] → [Video 4] → [Output 4]
[Product 5 Image] → [Scene Composition 5] → [Video 5] → [Output 5]
      ...                    ...                ...          ...
[Product 10 Image] → [Scene Composition 10] → [Video 10] → [Output 10]
```

**Each branch runs in parallel.**

---

### Video Modification Nodes

**Scenario: You have a finished video but want to change one element**

**Process:**

1. Drag from your existing video node's output handle
2. Create new video node (Seedance 2.0)
3. Write simple modification prompt: "Change the product to a blue water bottle"
4. Upload reference images (new product, character reference)
5. Connect and run

**The AI modifies the existing video rather than creating from scratch.**

---

### Modification Prompt Examples

**Change product:**

```
Modify the video to show the woman holding a clear glass water bottle instead of the matcha cup. Keep all other elements identical: same character, same expression timing, same camera movements, same lighting, same background. Only the product changes.

Reference Image 1: Original video
Reference Image 2: Product image of clear glass water bottle
Reference Image 3: Character reference sheet
```

**Change character:**

```
Modify the video to show the man from the reference sheet instead of the woman. Keep all actions identical: same camera movements, same environment (car interior), same timing of expressions and gestures. Only the character changes.

Reference Image 1: Original video
Reference Image 2: Man character reference sheet
```

**Change environment:**

```
Modify the video to show the same character and actions but in a coffee shop interior instead of car. Natural cafe lighting, wooden tables and plants in soft-focus background. Keep character expressions, product interaction, and camera movements identical.

Reference Image 1: Original video
Reference Image 2: Coffee shop interior reference
Reference Image 3: Character reference sheet
```

---

### Complete Automation Workflow Example

**Goal:** Generate 10 UGC ads for 10 different beauty products with same character

**One-time setup (2 hours):**

1. Generate base character image (Higgsfield)
2. Create character reference sheet (GPT Image 2)
3. Build master workflow in Arcads:
   - Text prompt node → Character image node → Character sheet node
   - Scene composition template node (with variable product input)
   - Video animation node (with master Seedance prompt)
4. Test with one product to validate pipeline

**Batch generation (10 minutes):**

1. Upload 10 product images to 10 product nodes
2. Each product node connects to a scene composition node
3. Each scene node connects to a video animation node
4. Each video node uses same character reference and Seedance template
5. Select all nodes, click "Run"
6. **10 videos generate automatically**

**Result:**

- 10 high-quality UGC ads
- Same character across all videos (consistency)
- Each showcasing different product
- All with same cinematic effects and UGC aesthetic
- Total time: 10 minutes vs. 20+ hours manual work

---

## Advanced Techniques

### Multi-Shot Storytelling

**Structure: 3-shot narrative arc**

**Shot 1 (Problem):**

- Character looking frustrated, no product visible
- Static or slow camera
- Low energy

**Shot 2 (Solution):**

- Whip pan or transition to product reveal
- Character expression changes to interest/surprise
- Dynamic camera movement (zoom, push-in)

**Shot 3 (Result):**

- Character using product with satisfaction
- Genuine smile, direct eye contact
- Confident energy, zoom pulse on key moment

**Animation workflow:**

- Generate 3 separate images (one per shot)
- Animate each shot separately with Seedance 2.0
- Stitch in video editor
- Add transition effects (whip blur between shots)

---

### Dialogue-Synced Effects

**Technique:** Time visual effects to spoken words for emphasis

**Example script:**
"This changed my _morning routine_ completely. I used to feel _sluggish_ until noon. Now? _Energy_ from the first sip."

**Effects timing:**

- "morning routine" → 8% zoom pulse
- "sluggish" → Slight head tilt, expression shift
- "Energy" → 12% zoom pulse + subtle light flare

**Seedance prompt structure:**

```
0:00-1:50s: "This changed my" — static hold, natural expression
1:50-2:20s: "morning routine" — 8% zoom pulse synchronized to the word "morning", face tightens into frame
2:20-3:00s: "completely. I used to feel" — zoom out slightly, handheld bounce
3:00-3:50s: "sluggish until noon" — expression shifts from bright to tired memory, slight head drop
3:50-4:20s: "Now?" — head lifts back up, eyebrows raise, energy returns
4:20-5:00s: "Energy from the first sip" — 12% zoom pulse on the word "Energy", smile breaks into full grin
```

---

### Character Consistency Across Campaigns

**Strategy:** Build character library for reuse

**Setup:**

1. Generate 5-10 diverse character reference sheets (different ages, genders, ethnicities)
2. Save as reusable assets in Arcads
3. Name clearly: "Woman_20s_Blonde_Casual", "Man_40s_Professional", etc.

**Usage:**

- New product campaign? Pick character from library
- A/B test different demographics on same product
- Build character consistency over multiple videos (like real influencer)

**Benefit:**

- Audiences start recognizing "your people"
- Builds pseudo-influencer authority
- Faster production (no new character generation)

---

### Seasonal Variations

**Same character, different settings:**

**Summer campaign:**

- Car interior with sunshine, bright lighting
- Outdoor cafe, natural greenery background
- Beach or pool environment (blurred)

**Winter campaign:**

- Home interior, cozy fireplace background (soft focus)
- Coffee shop with warm lighting
- Car interior with rain on windows

**Holiday campaign:**

- Home with holiday decorations (blurred background)
- Festive lighting (string lights bokeh)
- Seasonal clothing (sweaters, scarves)

**Implementation:**

- Keep character reference sheet identical
- Modify scene composition prompt for environment
- Adjust lighting descriptions in Seedance prompt
- Run through same workflow pipeline

---

## Troubleshooting

### Problem: Character looks different in each scene

**Causes:**

- Not uploading character reference sheet with scene composition prompt
- GPT Image 2 not receiving reference properly
- Prompt doesn't explicitly call for "exact facial identity" preservation

**Solutions:**

- Always upload character reference sheet alongside composition prompt
- Start prompt with: "The woman/man from the multi-angle reference sheet — preserving exact facial identity..."
- List specific features (hair color/style, eye color, facial structure)
- Generate multiple variations and pick most consistent

---

### Problem: Animation looks robotic or unnatural

**Causes:**

- Seedance prompt too short or generic
- Missing motion flow description
- No natural imperfections specified
- Effects not timed to human rhythm

**Solutions:**

- Use detailed prompt structure (Effects Timeline + Motion Flow)
- Include "handheld bounce", "natural weight", "organic timing"
- Specify imperfections: "slight overshoot", "micro-adjustments"
- Describe emotional journey, not just physical movements
- Add phrases like "feels like", "energy of", "as if"

---

### Problem: Product looks fake or poorly integrated

**Causes:**

- Product reference image low quality
- Product not described in enough detail
- Lighting on product doesn't match environment
- Hands/fingers interaction not specified

**Solutions:**

- Use high-quality product images (white background, well-lit)
- Describe product explicitly: "clear plastic cup with condensation visible, straw pointing upward"
- Specify how lighting hits product: "window light catching the bottle surface"
- Detail hand interaction: "fingers curled naturally around the cup, thumb near logo"

---

### Problem: Workflow fails mid-automation

**Causes:**

- Node connections broken
- One node failed, cascading to others
- Resource limits (too many simultaneous generations)
- Missing input references

**Solutions:**

- Verify all nodes connected properly (visual check)
- Run individual nodes first to test before batch
- Stagger large batches (run 5, then next 5)
- Check each node has required inputs (references, prompts)
- Review error messages in failed nodes

---

### Problem: Video quality lower than expected

**Causes:**

- Source images too low resolution
- Seedance settings not optimized
- Too many effects causing artifacts
- Compression during export

**Solutions:**

- Use 2K+ resolution for all source images
- Check Seedance quality settings before generating
- Reduce effects density if image quality suffers
- Export at highest quality setting available
- Use lossless export if platform allows

---

### Problem: Modifications don't maintain original video's style

**Causes:**

- Modification prompt not referencing original closely enough
- Not uploading original video as reference
- Missing "keep all other elements identical" instruction

**Solutions:**

- Always upload original video to modification node
- Use explicit language: "Keep all actions, timing, camera movements identical"
- List what should NOT change alongside what should change
- Include character reference sheet even for product-only swaps

---

## Best Practices Summary

### Character Generation

1. **Emphasize raw, unfiltered texture** — "Visible pores, natural sebum sheen"
2. **Specify "zero retouching" explicitly** — AI defaults to beauty perfection
3. **Use authentic environments** — Car, home, cafe (not studio)
4. **Horizontal selfie framing** — Social media standard format
5. **Natural lighting described** — "Ambient natural daylight", not "studio lighting"

### Character Reference Sheets

1. **Four angles minimum** — Front, left profile, right profile, back
2. **Pure white background** — Clean separation for AI reference
3. **8K resolution specified** — Maximum detail for consistency
4. **List distinctive features** — Hair highlights, freckle placement, eye color
5. **"Fashion casting card aesthetic"** — Sets professional reference tone

### Scene Composition

1. **Upload character sheet + base image** — Both as references
2. **Start with "The woman/man from the multi-angle reference sheet"** — Establishes consistency
3. **Describe product interaction in detail** — How hands hold it, finger placement
4. **Match environment to original** — "Same lighting, same background, same framing"
5. **Natural expressions** — "Barely-there smile", "caught mid-thought"

### Seedance Animation

1. **Use complete prompt structure** — Reference Map + Effects Timeline + Motion Flow
2. **Timing in seconds** — "0:00-1:20s", "1:20-2:20s" (precise timing)
3. **Specify exact effect percentages** — "8-10% scale increase", "10-15 frames of blur"
4. **Describe energy arc** — Opening, build, resolution
5. **Include imperfections** — "Tiny overshoot", "handheld bounce", "not mechanical"

### Node Workflow Automation

1. **Test single path first** — Validate before batch automation
2. **Name nodes clearly** — "Product_1_Scene", "Product_2_Scene"
3. **Verify connections** — Visual check of all node links
4. **Use reference sheets systematically** — Same character sheet connected to all scene nodes
5. **Stagger large batches** — Don't generate 50 videos at once (system load)

### Video Modification

1. **Upload original video as reference** — Critical for maintaining style
2. **Explicit preservation instructions** — "Keep all timing, movements, expressions identical"
3. **List what changes AND what doesn't** — Clear distinction
4. **Include character/product references** — Even for small modifications
5. **Test modification before batch** — One modification to validate approach

---

## Use Cases and Applications

### Brand Product Launches

**Scenario:** Launching new supplement line with 8 SKUs

**Workflow:**

1. Create one UGC character (matches target demographic)
2. Generate character reference sheet
3. Build base scene composition (character in relatable environment)
4. Create 8 product nodes (one per SKU)
5. Automate: 8 videos with same character, different products
6. Stitch A/B variations (different dialogue per video)

**Deliverables:**

- 8 unique UGC-style ads
- Consistent brand spokesperson (the character)
- Authentic testimonial aesthetic
- All generated in under 1 hour

---

### Social Media Ad Testing

**Scenario:** A/B testing different demographics for same product

**Workflow:**

1. Create 4 character reference sheets (diverse demographics)
2. Build one master scene composition template
3. Create 4 parallel branches (one per character)
4. Run automation: 4 videos, different characters, same product
5. Launch as Facebook ad variants, measure CTR

**Result:** Data-driven insight on which demographic performs best

---

### Influencer-Style Content at Scale

**Scenario:** Weekly content for beauty brand (52 videos/year)

**Strategy:**

- Create 3-4 recurring characters (like brand ambassadors)
- Build modular workflow library:
  - Morning routine module
  - Product comparison module
  - Tutorial module
  - Testimonial module
- Each week: Pick character + module + new product
- Generate in 15 minutes

**Benefit:** Consistent influencer-style content without paying influencers

---

### Testimonial Video Generation

**Scenario:** E-commerce brand needs 50 testimonial videos

**Workflow:**

1. Generate 10 diverse character reference sheets
2. Write 5 testimonial script templates
3. Build workflow: Character + Script + Product → Video
4. Automate: 10 characters × 5 scripts = 50 unique testimonials
5. Each features different person with authentic delivery

**Use on:**

- Product pages (rotating testimonials)
- Email campaigns
- Paid ads
- Social proof content

---

## Resource Checklist

### Before Starting

- [ ] Arcads account created (node workflow platform)
- [ ] Higgsfield Soul 2.0 access (character generation)
- [ ] GPT Image 2 access (scene composition)
- [ ] Seedance 2.0 access (video animation)
- [ ] Product images prepared (if applicable)
- [ ] Target demographic decided

### Character Generation Phase

- [ ] Base character prompt written (includes UGC-specific texture details)
- [ ] Base character image generated (Higgsfield)
- [ ] Character looks authentic and unretouched
- [ ] Image resolution 2K+ minimum

### Character Reference Sheet Phase

- [ ] Character reference prompt written (4-panel layout)
- [ ] Reference sheet generated (GPT Image 2)
- [ ] All 4 angles present and consistent
- [ ] Features match base character
- [ ] High resolution (8K specified)

### Scene Composition Phase

- [ ] Scene composition prompt written
- [ ] Character reference sheet uploaded
- [ ] Base environment image uploaded (if applicable)
- [ ] Product image uploaded and described in prompt
- [ ] Natural interaction with product specified
- [ ] Scene generated and validated

### Animation Phase

- [ ] Seedance prompt structure complete (Reference Map, Timeline, Motion Flow)
- [ ] Timing specified in seconds
- [ ] Effects detailed with percentages/frame counts
- [ ] All reference images uploaded to Seedance
- [ ] Animation generated
- [ ] Video reviewed for quality and authenticity

### Node Workflow Phase

- [ ] Nodes created for each step
- [ ] Connections verified visually
- [ ] Single path tested successfully
- [ ] Variation nodes added (products/characters)
- [ ] Batch automation run
- [ ] All outputs downloaded

### Final Delivery

- [ ] Videos stitched if multi-shot
- [ ] Exported at high quality
- [ ] Tested on mobile (primary viewing platform)
- [ ] Authentic UGC aesthetic confirmed
- [ ] Ready for deployment

---

## Prompt Library

### Base Character Prompts (UGC Style)

**Young Woman (Gen Z, Casual):**

```
Young woman, early 20s, long brown hair with subtle highlights worn in relaxed waves, natural brows, completely bare face — no makeup, no filters. Raw realistic skin texture: visible pores, natural skin tone with slight variation, maybe faint acne scarring on cheek. Seated at home desk with laptop visible, horizontal phone-propped angle slightly above eye level. Wearing oversized hoodie. Gaze directed at camera, relaxed candid expression like she's FaceTiming a friend. Ambient natural window light from left side, soft and diffused. Background: bedroom or home office softly blurred, posters or plants visible. Frame shows shoulders to top of head. Zero smoothing, zero correction — looks exactly like unfiltered phone camera selfie. Authentic Gen Z UGC energy.
```

**Man (30s, Professional Casual):**

```
Man in early 30s, short dark hair with natural texture, trimmed beard, warm skin tone. Natural skin texture visible: pores, slight under-eye circles from normal life, authentic features. Seated in modern home office, natural window light from right side. Wearing casual button-up or henley shirt. Horizontal angle at eye level, like video call framing. Direct eye contact with camera, friendly approachable expression. Background: home office with bookshelf and plants softly out of focus. Frame shows upper chest to top of head. No retouching — real person recording real testimonial from home. Professional but authentic energy.
```

**Woman (40s, Mature Professional):**

```
Woman in early 40s, shoulder-length blonde hair with natural grey streaks, minimal professional makeup — light foundation only, natural lip color. Visible aging features: laugh lines around eyes, slight crow's feet, natural forehead lines — all present and unretouched. Seated in bright kitchen, natural daylight from window behind camera. Wearing casual sweater. Horizontal phone angle at natural arm's length. Warm genuine smile, eyes crinkled naturally. Background: modern kitchen counter with coffee mug and fruit bowl visible, softly blurred. Frame shows shoulders to top of head. Authentic mature beauty, zero smoothing, real skin texture with fine lines visible. Confident approachable energy.
```

---

### Scene Composition Prompts

**Skincare Product:**

```
The woman from the multi-angle reference sheet — preserving exact facial identity: [list specific features]. Camera angle and environment from the reference photo — same horizontal selfie framing, same soft natural window light, same home interior background. She's holding a small glass dropper bottle of serum at chest level, left hand supporting the bottle base, right hand holding the dropper above it, one drop of serum caught mid-air between dropper and bottle opening. Gaze directed down at the bottle with concentrated but pleased expression, like she's carefully applying her favorite product. Slight smile playing at corner of mouth. Natural lighting catches the amber liquid inside the bottle and the falling drop. Hair falling naturally over one shoulder. Visible skin texture, natural glow, zero retouching. Authentic skincare ritual moment.
```

**Supplement Product:**

```
The man from the multi-angle reference sheet — preserving exact facial identity: [list specific features]. Camera angle and environment from the reference photo — same home office setting, same natural side lighting from window. He's holding an orange supplement bottle at shoulder height with right hand, fingers wrapped around middle of bottle, label facing slightly toward camera. Left hand holding the bottle cap in pinching gesture like he just opened it. Gaze directed at camera with knowing smile and slight eyebrow raise, like he's sharing a secret with a friend. Body language relaxed, leaning slightly toward camera. Background shows desk and computer monitor softly blurred. Natural window light creating soft shadow on one side of face. Visible skin texture, natural expression, authentic recommendation energy.
```

**Beverage Product:**

```
The woman from the multi-angle reference sheet — preserving exact facial identity: [list specific features]. Environment from reference — car interior, natural daylight through windshield. She's holding a branded energy drink can with both hands at chest level, fingers wrapped naturally around the sides, condensation visible on the can surface. Head tilted back slightly, taking a sip — can near lips, eyes closed in satisfied expression like the first sip on a long drive. Hair catching the window light. Other hand resting on steering wheel (car in park). Background shows soft-focus car interior and greenery through rear window. Natural lighting creates soft overexposure on her hair. Authentic refreshment moment, caught mid-action.
```

---

## Final Tips

**The secret to professional UGC videos with AI:**

1. **Texture is authenticity** — Never skip "visible pores, zero smoothing"
2. **Extreme detail in animation prompts** — Seedance responds to specificity
3. **Character consistency is everything** — Reference sheets are non-negotiable
4. **Build once, generate infinite** — Node workflows eliminate repetitive work
5. **Natural imperfections = believability** — "Slight overshoot", "handheld bounce"
6. **TikTok effects language** — Whip pans, zoom pulses, snap cuts
7. **Timing in exact seconds** — "0:00-1:20s", not "at the beginning"
8. **Test single before batch** — Validate pipeline before automation
9. **Upload ALL references** — Character sheet + environment + product
10. **Energy arc storytelling** — Opening → Build → Resolution

**Pro Tip:** The most successful UGC-style AI videos don't look like AI generated them — they look like someone recorded a genuine moment on their phone. The secret isn't hiding the AI; it's instructing the AI to replicate the specific imperfections, lighting conditions, and camera physics that make phone-shot content feel authentic. When viewers can't tell if it's a real person or AI, you've mastered the technique.

**Automation Tip:** Once your workflow is built and tested, you can generate an entire month's worth of social content in an afternoon. The initial setup takes 2-3 hours, but every subsequent campaign takes 10-15 minutes. That's the power of node-based automation — build once, leverage forever.

---

**Difficulty:** Advanced  
**Duration:** 2-3 hours setup, 10-15 minutes per batch  
**Platform:** Arcads (node workflows) + Multiple AI tools  
**Output:** Professional UGC video ads at scale  
**Skill ceiling:** Unlimited (automation complexity, character library, workflow library)

Welcome to the future of UGC content creation. 🎬🤖

---
