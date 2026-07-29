# Reference Boards Vol 2 — Film & Animation Studio Reference Sheets

## Description

Six film and animation reference-board prompts designed for GPT Image 2 and Picsart Flow. Each takes one image and builds a densely-packed, studio-style reference sheet: a hero shot, a full metadata block, and a set of panels. Five hold one subject identical across every panel (pose, character, object, location, creature)—the sixth, the Shot Board, breaks a single keyframe into a full 12-shot storyboard sequence instead.

**Signature look on all six:** Dark near-black board, thin yellow neon accent, film grain, studio UI, a 6-swatch color palette with hex codes, and a flexible layout that adapts to any aspect ratio.

## Tools Required

- **GPT Image 2** — Image-to-image generation with reference lock
- **Picsart Flow** — Image workflow platform
- **Reference Image** — High-quality subject photo or scene keyframe

## What These Are

Image-to-image boards that treat your attached reference as the single source of truth and hold consistency across every panel. Each board outputs a professional studio-grade reference sheet you'd see in animation studios, VFX houses, or production design departments.

---

## What Every Board Has

All six share the same anatomy—only the panels change to fit the job:

### Core Components

1. **Hero Shot** — A large defining shot (or the source keyframe, for the Shot Board)
2. **Metadata Block** — A job-specific spec sheet (pose language, materials, emotional arc—whatever fits)
3. **4-6 Content Panels** — Always includes:
   - **COLOR PALETTE** with hex codes
   - Job-specific panels (poses, expressions, growth stages, time-of-day, the 12-shot sequence, etc.)
4. **Caption + Tags** — Bottom caption and bottom-right tags that make it read like a real studio board

### Consistent Visual Style

- **Dark near-black board** background
- **Thin yellow neon accent** light
- **Film grain** overlay
- **Studio UI** elements
- **Flexible non-locked layout** that adapts to aspect ratio
- **Photorealistic 8K** quality
- **No illustration** — photorealistic only

---

## How To Use

All six run in **Picsart Flow** as image-to-image.

### Step 1 — Pick a Board

Match it to the job—poses, a character, an object, a place, a creature, or a shot breakdown.

### Step 2 — Attach Your Reference

A clean subject image—or, for the Shot Board, a single scene keyframe.

### Step 3 — Run in GPT Image 2

Image-to-image; let it build the full board.

### Step 4 — Set Aspect Ratio

The layout adapts:

- **4:5 / 9:16** for feed/story format
- **16:9 / wider** for desktop-style board

### Step 5 — Regenerate for Variants

The layout reshuffles each run; pick the cleanest, most readable board.

---

## The 6 Boards

| Board             | For                                               | What You Attach          |
| ----------------- | ------------------------------------------------- | ------------------------ |
| **1 · Pose**      | Animation / video pose sheet—basic + action poses | A photo of the character |
| **2 · Character** | A person, consistent across views & lighting      | A photo of them          |
| **3 · Object**    | A product, prop or object                         | An object photo          |
| **4 · Location**  | An environment / set                              | A location photo         |
| **5 · Creature**  | Creatures / monsters with growth stages           | A creature image         |
| **6 · Shot**      | A 12-shot storyboard from one keyframe            | A scene keyframe         |

---

## 🤸 1 · POSE BOARD

**GPT Image 2 — Animation pose sheet · Attach a character photo**

### What It Creates

- **Hero Standing Shot** — Full-body, clean and readable
- **Metadata Block** — Name, age, build, height, outfit, pose language, center of gravity, dominant hand, purpose
- **5 Content Panels:**
  1. **BASIC POSES** — Stand, sit, walk, run, jump (5 full-body shots)
  2. **ACTION POSES** — Fight stance, throw, dodge, climb, land (5 dynamic shots)
  3. **EXPRESSIONS** — Neutral, laugh, angry, sad, surprised (5 tight headshots)
  4. **ANGLE COVERAGE** — Front, 3/4, side, back (4 standing neutral portraits)
  5. **COLOR PALETTE** — 6 swatches with hex codes from outfit + skin tones

### Use Case

Animation and video-generation reference. Provides consistent pose library for character animation, video generation prompts, and motion reference.

### Complete Prompt

```
Create a single high-resolution, densely packed character pose reference sheet titled "POSE BOARD" using the attached photo of the character as the single source of truth for face, hair, body proportions and outfit. The character must be identical across every panel — same person, same age, same outfit. All on-image labels in ENGLISH. Editorial animation-reference layout with a dark near-black background, thin yellow neon accent light, faint film-grain overlay, and studio reference UI. The composition should feel organized but not rigidly fixed: allow the hero standing figure, metadata, pose studies, expression studies, and supporting panels to shift position naturally within the board. The board should preserve strong readability and hierarchy while allowing panel placement to vary between generations. Keep the overall design adaptable to multiple aspect ratios rather than relying on a fixed horizontal arrangement.

Include: A large full-body hero standing shot, clean and readable, with a detailed metadata block: NAME · AGE · BUILD · HEIGHT · OUTFIT: (describe the exact clothing from the attached photo) · POSE LANGUAGE: (confident / relaxed / aggressive / playful) · CENTER OF GRAVITY · DOMINANT HAND · PURPOSE: animation and video-generation reference.

Also include five content groupings:

PANEL 01 — BASIC POSES (5 full-body shots, identical outfit and lighting): STAND · SIT · WALK · RUN · JUMP.

PANEL 02 — ACTION POSES (5 dynamic full-body shots): FIGHT STANCE · THROW · DODGE · CLIMB · LAND.

PANEL 03 — EXPRESSIONS (5 tight headshots, same lighting): NEUTRAL · LAUGH · ANGRY · SAD · SURPRISED.

PANEL 04 — ANGLE COVERAGE (4 standing neutral portraits): FRONT · 3/4 · SIDE · BACK.

PANEL 05 — COLOR PALETTE: 6 swatches with HEX codes from outfit + skin tones.

Bottom caption: "Use this pose sheet as a visual reference for consistent animation of the character across all generations."

Bottom-right tags: STYLE · Animation Ready · Realistic · Cinematic.

Style: photorealistic, no illustration. Consistent character across every panel. 8K, fine grain, cinematic color grading.
```

---

## 🧑 2 · CHARACTER BOARD

**GPT Image 2 — A person, held consistent · Attach a photo**

### What It Creates

- **Hero Portrait** — Large 3/4-length character image
- **Metadata Block** — Name, age, height, build, hair, eyes, features, outfit, character, mood
- **6 Content Panels:**
  1. **VIEWS** — Front, 3/4 left, side left, back (4 full-body shots)
  2. **EXPRESSIONS** — Neutral, smile, thoughtful, focused, serious (5 tight headshots)
  3. **DETAILS** — Face/eyes close-up, distinctive outfit detail (2 macros)
  4. **OUTFIT FLAT-LAYS** — Jacket, shirt/knit, trousers, watch, shoes (5 isolated product shots)
  5. **LIGHTING / MOOD** — Soft daylight, warm tungsten interior, cool blue night, hard cinematic side-light (4 same-pose portraits)
  6. **COLOR PALETTE** — 6 swatches with hex codes from outfit and skin tones

### Use Case

Consistent character depiction across projects, video generations, and multi-shot sequences. Locks identity, outfit, and styling.

### Complete Prompt

```
Create a single high-resolution, densely packed character reference sheet titled "CHARACTER BOARD" using the attached photo of the person as the single source of truth for face, hair, beard, eyes, skin tone and body proportions. The same person must appear in every panel — same age, same features. Outfit identical to the attached photo across all panels. All on-image labels in ENGLISH. Editorial reference-board layout with a dark near-black background, thin yellow neon accent light, faint film-grain overlay, and production-grade character-design UI. The composition should feel organized but not rigidly locked: allow the main portrait, metadata, and supporting panels to shift position naturally within the board. The panel arrangement can vary from generation to generation while remaining readable, balanced, and premium. Design the board so it works cleanly in different aspect ratios without depending on a fixed left-column structure.

Include: A large hero portrait or 3/4-length character image, accompanied by a detailed metadata block: NAME · AGE · HEIGHT · BUILD · HAIR · EYES · FEATURES · OUTFIT (describe the exact clothing from the attached photo) · CHARACTER · MOOD.

Also include six content groupings:

PANEL 01 — VIEWS (4 full-body shots, identical outfit and lighting, neutral tan backdrop): FRONT · 3/4 LEFT · SIDE LEFT · BACK.

PANEL 02 — EXPRESSIONS (5 tight headshots, same lighting): NEUTRAL · SMILE · THOUGHTFUL · FOCUSED · SERIOUS.

PANEL 03 — DETAILS (2 macros): face/eyes close-up · distinctive outfit detail (jacket lapel, watch, or shoe).

PANEL 04 — OUTFIT FLAT-LAYS (5 isolated product shots on dark background): jacket · shirt/knit · trousers · watch · shoes.

PANEL 05 — LIGHTING / MOOD (4 same-pose portraits under different lighting): SOFT DAYLIGHT · WARM TUNGSTEN INTERIOR · COOL BLUE NIGHT · HARD CINEMATIC SIDE-LIGHT.

PANEL 06 — COLOR PALETTE: 6 swatches with HEX codes derived from the outfit and skin tones.

Bottom caption: "Use this character board as a visual reference for consistent depiction of the character across all generations."

Bottom-right tags: STYLE · Modern · Realistic · Cinematic.

Style: photorealistic, no illustration. Consistent face across every single panel. 8K, fine grain, cinematic color grading.
```

---

## 📦 3 · OBJECT BOARD

**GPT Image 2 — A product / prop / object · Attach an object photo**

### What It Creates

- **Hero Product Shot** — Prominent studio angle
- **Metadata Block** — Name, era, origin, material, dimensions, weight, description, key features, condition, purpose
- **4 Content Panels:**
  1. **VIEWS** — Front, 3/4 left, left side, back, 3/4 right, top-down (6 angles on neutral plinth)
  2. **DETAILS** — Handle/grip, body/blade, engraving/maker's mark, edge/wear (4 macros)
  3. **LIGHTING / MOOD** — Soft daylight, warm tungsten, cool blue night, hard cinematic side-light (4 same-angle portraits)
  4. **COLOR PALETTE** — 6 swatches with hex codes from object's surfaces

### Use Case

Product photography reference, hero props for film/video, consistent object depiction across shots, e-commerce product sheets.

### Complete Prompt

```
Create a single high-resolution, densely packed product/object reference sheet titled "OBJECT BOARD" using the attached photo of the object as the single source of truth for design, materials, proportions, color and detailing. The object must be identical across every panel — same item, same era, same condition. All on-image labels in ENGLISH. Editorial product-design board layout with a dark near-black background, thin yellow neon accent light, faint film-grain overlay, and premium industrial-design UI. The composition should feel controlled but flexible: allow the main hero product shot, metadata, and detail studies to appear in different balanced positions instead of being fixed to a left-column layout. The panel arrangement can vary subtly between generations while remaining clean, legible, and premium. The board should work well across different aspect ratios.

Include: A prominent hero product shot, ideally a strong studio angle, accompanied by a detailed metadata block: NAME · ERA · ORIGIN · MATERIAL · DIMENSIONS · WEIGHT · DESCRIPTION: (1-2 lines) · KEY FEATURES: (3-5 bullets) · CONDITION: (pristine / weathered / aged) · PURPOSE: (e.g. ceremonial sword / luxury watch / hero prop)

Also include four content groupings:

PANEL 01 — VIEWS (6 angles on a neutral plinth, identical lighting): FRONT · 3/4 LEFT · LEFT SIDE · BACK · 3/4 RIGHT · TOP-DOWN.

PANEL 02 — DETAILS (4 macros): handle/grip · body/blade · engraving/maker's mark · edge/wear.

PANEL 03 — LIGHTING / MOOD (4 same-angle product portraits): SOFT DAYLIGHT · WARM TUNGSTEN · COOL BLUE NIGHT · HARD CINEMATIC SIDE-LIGHT.

PANEL 04 — COLOR PALETTE: 6 swatches with HEX codes from the object's surfaces.

Bottom caption: "Use this product board as a visual reference for consistent depiction of the object across all generations."

Bottom-right tags: STYLE · Premium · Realistic · Cinematic.

Style: photorealistic, no illustration. Consistent object across every panel. 8K, fine grain, cinematic color grading.
```

---

## 🗺 4 · LOCATION BOARD

**GPT Image 2 — An environment / set · Attach a location photo**

### What It Creates

- **Hero Location Shot** — Wide establishing or defining view
- **Metadata Block** — Name, type, era, scale, architecture, materials, atmosphere, default time, default weather, purpose
- **6 Content Panels:**
  1. **VIEWS** — Wide, mid, tight, alt angle, overhead (5 same-location shots)
  2. **TIME OF DAY** — Dawn, noon, dusk, night (4 same-angle shots)
  3. **DETAILS** — Material/texture close-up, distinctive architectural detail (2 macros)
  4. **SET DRESSING / PROPS** — 5 key props or signage elements from the location (5 isolated studies)
  5. **WEATHER / MOOD** — Clear sunny, overcast, rain-soaked, misty fog (4 same-angle shots)
  6. **COLOR PALETTE** — 6 swatches with hex codes from location's dominant tones

### Use Case

Location scouting reference, set design consistency, environment continuity across scenes, visual development for film/animation.

### Complete Prompt

```
Create a single high-resolution, densely packed location reference sheet titled "LOCATION BOARD" using the attached photo of the location as the single source of truth for its architecture, atmosphere, lighting, materials and color palette. The space must be identical across every panel — same place, same materials, same era. All on-image labels in ENGLISH. Editorial location-reference board layout with a dark near-black background, thin yellow neon accent light on the far left, faint film-grain overlay, subtle cinematic interface elements, and production-grade location-scout UI. The composition should feel structured but not rigidly fixed: allow the hero location view, metadata, environmental studies, and supporting panels to shift position naturally within the board. The arrangement may vary from generation to generation while remaining readable, balanced, and premium. Design the board so it adapts cleanly to different aspect ratios without depending on a fixed left-column layout.

Include a prominent hero shot of the location, ideally a wide establishing or defining view, accompanied by a detailed metadata block: NAME · TYPE (street / interior / exterior / forest) · ERA · SCALE (intimate / vast) · ARCHITECTURE: (key features) · MATERIALS: (stone, brick, wood, glass, etc.) · ATMOSPHERE: (busy / quiet / eerie / romantic) · DEFAULT TIME · DEFAULT WEATHER · PURPOSE (e.g. chase sequence, dialogue scene)

Also include six content groupings:

PANEL 01 — VIEWS (5 same-location shots, identical lighting): WIDE · MID · TIGHT · ALT ANGLE · OVERHEAD.

PANEL 02 — TIME OF DAY (4 same-angle shots): DAWN · NOON · DUSK · NIGHT.

PANEL 03 — DETAILS (2 macros): material/texture close-up · distinctive architectural detail.

PANEL 04 — SET DRESSING / PROPS (5 isolated prop or signage studies on dark background): 5 key props or signage elements from the location.

PANEL 05 — WEATHER / MOOD (4 same-angle shots): CLEAR SUNNY · OVERCAST · RAIN-SOAKED · MISTY FOG.

PANEL 06 — COLOR PALETTE: 6 swatches with HEX codes from the location's dominant tones.

Optional subtle interface accents may suggest cinematic surveying or environmental documentation, but should remain secondary to the imagery and never lock the board into a single fixed screen layout.

Bottom caption: "Use this location board as a visual reference for consistent depiction of the environment across all generations."

Bottom-right tags: STYLE · Modern · Realistic · Cinematic.

Style: photorealistic, no illustration. Consistent location across every panel. 8K, fine grain, cinematic color grading.
```

---

## 🐉 5 · CREATURE BOARD

**GPT Image 2 — Creature + growth stages · Attach a creature image**

### What It Creates

- **Hero Creature Portrait** — Full creature in neutral standing or resting pose
- **Metadata Block** — Name/species, age, size, weight, habitat, diet, temperament, distinct features, abilities/traits, lore note
- **6 Content Panels:**
  1. **VIEWS** — Front, 3/4 left, side left, back (4 full-body angles)
  2. **LIFE CYCLE / GROWTH STAGES** — Stage 01 (larval/embryonic, 10-15% adult mass), Stage 02 (juvenile, 30-40% adult mass), Stage 03 (sub-adult, 70-80% adult mass), Stage 04 (adult/final, 100% adult)
  3. **ANATOMY DETAILS** — Eyes, mouth, skin/scales/fur/shell texture, claw/limb/wing (4 macros)
  4. **SCALE COMPARISON** — Adult creature beside 1.8m human silhouette
  5. **BEHAVIOR / POSES** — Resting, stalking, attacking, fleeing (4 environmental shots)
  6. **COLOR PALETTE** — 6 swatches with hex codes from creature's body

### Use Case

VFX creature design, fantasy/sci-fi character development, game asset reference, consistent creature depiction across maturation stages.

### Complete Prompt

```
Create a single high-resolution, densely packed creature reference sheet titled "CREATURE BOARD" using the attached image of the creature as the single source of truth for anatomy, skin/scale/fur texture, color and proportions. The creature must be identical across every panel — same species, same individual lineage, with growth stages showing the same creature at different ages. All on-image labels in ENGLISH. Editorial creature-design board layout with a dark near-black background, thin yellow neon accent light, faint film-grain overlay, and VFX-studio creature-design UI. The composition should feel highly designed but not mechanically fixed: allow the hero creature portrait, metadata, anatomy studies, scale comparison, behavioral poses, and palette panels to shift into different balanced arrangements across generations. Preserve readability, premium presentation, and strong hierarchy, but avoid a rigid left-column lockup. The board should adapt naturally to different aspect ratios.

Include: A large hero portrait of the full creature in a neutral standing or resting pose, with a detailed metadata block: NAME / SPECIES · AGE · SIZE (e.g. 4 m tall) · WEIGHT (estimate) · HABITAT · DIET · TEMPERAMENT · DISTINCT FEATURES: (3-5 bullets) · ABILITIES / TRAITS: (3-4 bullets) · LORE NOTE: (1-line backstory)

Also include six content groupings:

PANEL 01 — VIEWS (4 full-body angles, neutral pose, identical lighting): FRONT · 3/4 LEFT · SIDE LEFT · BACK.

PANEL 02 — LIFE CYCLE / GROWTH STAGES (4 full-body stages of maturation, neutral lighting, identical pose conventions, ordered left-to-right from earliest to final form): STAGE 01 — LARVAL / EMBRYONIC FORM (roughly 10-15% adult mass, soft underdeveloped anatomy, key features only hinted at, paler translucent coloring). STAGE 02 — JUVENILE FORM (roughly 30-40% adult mass, recognizable proportions with slightly oversized limbs typical of juveniles, lower color saturation, primary features clearly emerging but not full-scale). STAGE 03 — SUB-ADULT FORM (roughly 70-80% adult mass, fully proportioned anatomy, color and textures approaching adult, secondary characteristics at two-thirds final development). STAGE 04 — ADULT / FINAL FORM (100% adult, peak saturation, fully developed secondary growths, signs of mature wear and small scars). All four stages share the same orientation, lighting, and scale-relative framing for proportional comparison. Small caption under each stage with stage name and approximate age or size.

PANEL 03 — ANATOMY DETAILS (4 macros): EYES (or primary sensory organ if no eyes) · MOUTH (or feeding apparatus if no traditional mouth) · SKIN/SCALES/FUR/SHELL TEXTURE · CLAW/LIMB/WING.

PANEL 04 — SCALE COMPARISON: adult creature beside a 1.8 m human silhouette for proportion.

PANEL 05 — BEHAVIOR / POSES (4 environmental shots): RESTING · STALKING · ATTACKING · FLEEING.

PANEL 06 — COLOR PALETTE: 6 swatches with HEX codes derived from the creature's body.

Bottom caption: "Use this creature board as a visual reference for consistent depiction of the creature across all generations."

Bottom-right tags: STYLE · VFX Ready · Realistic · Cinematic.

Style: photorealistic, no illustration. Consistent creature across every panel. 8K, fine grain, cinematic color grading.
```

---

## 🎬 6 · SHOT BOARD

**GPT Image 2 — A 12-shot storyboard · Attach a scene keyframe**

### What It Creates

- **Source Keyframe** — Hero scene image
- **Metadata Block** — Scene, act, shot count (12), runtime (~30s), setting, characters, emotional arc, camera style, color script, edit style
- **6 Content Panels:**
  1. **SHOT SEQUENCE** — 12 frames in narrative order: 01 Extreme Wide (world in), 02 Slow push-in on location, 03 Over-the-shoulder entry, 04 Full medium (character), 05 Insert (hands or object), 06 Close-up reaction, 07 Profile medium, 08 Low angle hero, 09 Rack-focus insert, 10 Tracking shot, 11 Wide (turn point), 12 Slow pull-back (resolution)
  2. **KEY EMOTIONAL BEATS** — 3 highlighted dramatic close-ups extracted from sequence
  3. **CAMERA NOTES** — Lens choices, motion, framing, height (4-5 entries)
  4. **LIGHTING CONTINUITY** — 4 frames showing light evolution across scene
  5. **TRANSITION TYPES** — Cut, match cut, rack focus, whip-pan, crossfade (5 visual examples)
  6. **COLOR PALETTE** — 6 swatches with hex codes from the sequence

### Use Case

Storyboard development, scene breakdown, cinematography planning, shot list visualization, editing reference.

### Complete Prompt

```
Create a single high-resolution, densely packed storyboard reference sheet titled "SHOT BOARD" using the attached photo as the single source keyframe. Generate a sequential 12-shot storyboard that breaks the scene into a coherent visual progression — same character(s), same location, same lighting continuity — as if filmed as continuous coverage. All on-image labels in ENGLISH. Editorial storyboard layout with a dark near-black background, thin yellow neon accent light, faint film-grain overlay, and production-grade storyboard UI. The composition should feel structured but flexible: allow the source keyframe, metadata, shot grid, camera notes, and secondary panels to float into different balanced placements rather than locking them into a fixed left-and-right arrangement. The internal panel composition may vary between generations while preserving clarity, hierarchy, and continuity. Design the board so it adapts cleanly to different aspect ratios.

Include: A prominent source keyframe or hero scene image, with a detailed metadata block: SCENE · ACT · SHOT COUNT: 12 · RUNTIME ~30s · SETTING: (location) · CHARACTERS: (list) · EMOTIONAL ARC: (e.g. tension → release) · CAMERA STYLE: (handheld / gimbal / static / dolly) · COLOR SCRIPT: (e.g. cool → warm) · EDIT STYLE: (rhythmic / patient / aggressive)

Also include six content groupings:

PANEL 01 — SHOT SEQUENCE (12 frames in clear narrative order, each frame labeled with its number and shot type, identical character/location continuity): 01 EXTREME WIDE — WORLD IN · 02 SLOW PUSH-IN ON LOCATION · 03 OVER-THE-SHOULDER ENTRY · 04 FULL MEDIUM — CHARACTER · 05 INSERT — HANDS OR OBJECT · 06 CLOSE-UP REACTION · 07 PROFILE MEDIUM · 08 LOW ANGLE HERO · 09 RACK-FOCUS INSERT · 10 TRACKING SHOT · 11 WIDE — TURN POINT · 12 SLOW PULL-BACK — RESOLUTION.

PANEL 02 — KEY EMOTIONAL BEATS (3 highlighted dramatic close-ups extracted from the sequence above).

PANEL 03 — CAMERA NOTES (small icons + text): lens choices, motion, framing, height — 4-5 entries.

PANEL 04 — LIGHTING CONTINUITY (4 frames showing how light evolves across the scene).

PANEL 05 — TRANSITION TYPES (5 small visual examples): CUT · MATCH CUT · RACK FOCUS · WHIP-PAN · CROSSFADE.

PANEL 06 — COLOR PALETTE: 6 swatches with HEX codes derived from the sequence.

Bottom caption: "Use this shot board as a visual reference for consistent scene breakdown across all generations."

Bottom-right tags: STYLE · Cinematic · Realistic · Continuous.

Style: photorealistic, no illustration. Consistent characters, location, and continuity across every panel. 8K, fine grain, cinematic color grading.
```

---

## Tips for Best Results

### 1. One clean reference = a consistent board

The attached image is the source of truth for every panel—start with a sharp, clear shot.

**What makes a good reference:**

- High resolution (minimum 1024px on shortest side)
- Clear focus on subject
- Good lighting
- Minimal background distractions
- Subject clearly visible

### 2. Boards adapt to aspect ratio

No fixed column, so run at whatever ratio you need:

- **4:5 / 9:16** — Feed, story, vertical display
- **16:9 / 21:9** — Wide desktop board, presentation format

### 3. Palette + hex are built in

Every board ends with 6 swatches and hex codes you can pull straight into your design tools.

**Use the hex codes for:**

- Color grading continuity
- UI design matching character palette
- Brand consistency
- Production design reference

### 4. Pose Board is animation-ready

It's built for video generation—basic + action poses give you clean motion references.

**Perfect for:**

- Character animation reference
- Video generation prompt libraries
- Motion capture planning
- Game character development

### 5. Shot Board is a sequence

Feed one keyframe and it breaks the scene into 12 continuous shots—a full storyboard, not a single subject.

**Generates:**

- Complete scene coverage
- Emotional beat progression
- Camera movement notes
- Lighting continuity
- Transition types

### 6. Use them to lock consistency

Generate a board first, then reference it to keep a character, creature or location identical across a whole project.

**Workflow:**

1. Generate reference board from single clean image
2. Save board as project reference
3. Attach board + prompt for subsequent generations
4. Maintain perfect consistency across 10s or 100s of shots

### 7. Swap the subject, keep the board

The format works for anything you need a clean reference sheet for.

**Additional applications:**

- Fashion lookbooks (use Character Board)
- Product catalogs (use Object Board)
- Architectural portfolios (use Location Board)
- Concept art development (use Creature Board)
- Film pitches (use Shot Board)

### 8. Regenerate for layout variations

Each generation reshuffles panel placement while keeping content consistent. Run 3-5 times and pick the cleanest, most balanced composition.

### 9. Customize metadata blocks

The metadata fields are templates—adjust them to your project needs:

- Add production-specific fields
- Include episode/scene numbers
- Add notes for team members
- Customize terminology for your industry

### 10. Export and annotate

Use the board as a living document:

- Screenshot and annotate in Photoshop
- Add notes in Figma for team collaboration
- Print for physical production bibles
- Embed in pitch decks and presentations

---

## Quick Workflow Examples

### Example 1: Character Development Pipeline

**Goal:** Create complete character reference for video series

1. Take high-quality portrait photo of character
2. Generate **Character Board** (views, expressions, lighting, outfit)
3. Generate **Pose Board** with same character (basic + action poses)
4. Use both boards as reference for all subsequent video generations
5. Maintain perfect identity consistency across 50+ video clips

### Example 2: Product Launch Campaign

**Goal:** Consistent product visualization across marketing materials

1. Shoot clean product photo on neutral background
2. Generate **Object Board** (6 angles, detail macros, 4 lighting moods)
3. Extract hex codes from color palette
4. Use board for:
   - Website product imagery
   - Social media posts
   - Print catalog consistency
   - 3D model reference

### Example 3: Film Pre-Production

**Goal:** Develop location reference for indie film

1. Scout location and capture wide establishing shot
2. Generate **Location Board** (views, time of day, weather, props)
3. Share board with DP, production designer, art department
4. Use for:
   - Shot list planning
   - Lighting design
   - Set dressing continuity
   - VFX reference

### Example 4: Fantasy Creature Design

**Goal:** Complete creature concept with life stages

1. Generate or illustrate initial creature concept
2. Create **Creature Board** (views, growth stages, anatomy, behavior)
3. Use for:
   - VFX pipeline reference
   - Animation rigging guide
   - Game asset development
   - Franchise bible documentation

### Example 5: Scene Storyboarding

**Goal:** Break script scene into shot sequence

1. Generate single hero keyframe of scene
2. Create **Shot Board** (12-shot sequence breakdown)
3. Share with director, DP, editor
4. Use for:
   - Shot list creation
   - Coverage planning
   - Edit structure visualization
   - Client pitch deck

---

## Board Selection Guide

**Use this to pick the right board for your project:**

| Your Need                                    | Best Board       | Why                                                  |
| -------------------------------------------- | ---------------- | ---------------------------------------------------- |
| **Consistent character across video series** | Character Board  | Locks identity, outfit, expressions, lighting moods  |
| **Animation pose library**                   | Pose Board       | Basic + action poses, expressions, angle coverage    |
| **Product photography reference**            | Object Board     | 6-angle coverage, detail macros, lighting variations |
| **Location/set consistency**                 | Location Board   | Time of day, weather, props, architectural details   |
| **Fantasy/sci-fi creature design**           | Creature Board   | Growth stages, anatomy, scale, behavioral poses      |
| **Scene shot breakdown**                     | Shot Board       | 12-shot storyboard sequence from single keyframe     |
| **Brand character development**              | Character + Pose | Use both for complete identity + motion library      |
| **Hero prop showcase**                       | Object Board     | Premium product-design presentation                  |
| **Environment concept art**                  | Location Board   | Comprehensive environment reference                  |
| **VFX creature pipeline**                    | Creature Board   | Complete creature bible from concept to final form   |
| **Film pre-viz**                             | Shot Board       | Visual scene breakdown for production planning       |

---

## Technical Specifications

### Input Requirements

- **File Format:** JPG, PNG, WEBP
- **Minimum Resolution:** 1024px shortest side
- **Recommended Resolution:** 2048px or higher
- **Aspect Ratio:** Any (board adapts)
- **File Size:** Under 10MB

### Output Specifications

- **Resolution:** 8K quality
- **Style:** Photorealistic, no illustration
- **Color Space:** sRGB
- **Format:** As generated by GPT Image 2
- **Color Palette:** 6 swatches with hex codes included
- **Layout:** Flexible, adapts to aspect ratio

### Platform Settings

**GPT Image 2 in Picsart Flow:**

- Mode: Image-to-Image
- Attach reference image
- Paste complete prompt
- Set desired aspect ratio
- Generate

**Recommended aspect ratios:**

- **4:5** — Instagram feed, portrait display
- **9:16** — Instagram/TikTok story, mobile vertical
- **16:9** — Desktop, presentation, YouTube thumbnail
- **21:9** — Ultra-wide desktop board

---

## Common Questions

### Q: Can I use illustrated references instead of photos?

**A:** The boards are designed for photorealistic output. You can use illustrated references, but the output will interpret them as photorealistic versions. For best results, use photo references.

### Q: Will the character/object/location stay identical across panels?

**A:** Yes—that's the core function. The attached reference is treated as the single source of truth. Identity consistency is the primary goal.

### Q: Can I customize the metadata fields?

**A:** The prompts include standard metadata blocks, but you can modify them. Edit the metadata section of the prompt to include your specific fields.

### Q: How many times should I regenerate to get the best board?

**A:** Typically 3-5 generations. The layout reshuffles each time while keeping content consistent. Pick the cleanest, most balanced composition.

### Q: Can I use these boards commercially?

**A:** Follow GPT Image 2 and Picsart Flow's commercial usage terms. The board format itself is a prompt template—output usage depends on the generation platform's terms.

### Q: Do I need all 6 boards for one project?

**A:** No. Pick the board(s) that match your needs. A character-driven project might use Character + Pose. A product campaign might only need Object Board.

### Q: Can I combine multiple boards in one project?

**A:** Absolutely. Use Character Board + Pose Board for complete character reference. Use Location Board + Shot Board for environment + scene planning.

### Q: What if the layout doesn't work for my aspect ratio?

**A:** Regenerate at a different aspect ratio. The layout is flexible and adapts. Try 16:9 for wide boards, 4:5 for vertical.

---

## Final Tips

**The secret to getting professional studio-quality reference boards:**

1. **Start with a clean, high-quality reference** — Sharp focus, good lighting, clear subject
2. **Match the board to the job** — Pose for animation, Character for identity, Shot for sequences
3. **Regenerate 3-5 times** — Layout reshuffles; pick the most readable composition
4. **Use the color palette hex codes** — Built-in color reference for design consistency
5. **Treat boards as project source of truth** — Reference them for all subsequent generations
6. **Customize metadata to your needs** — Edit prompt fields to match your production terminology
7. **Export and share with team** — Living reference document for collaboration
8. **Combine boards for comprehensive coverage** — Character + Pose, Location + Shot

That's how you create production-grade reference sheets that actually lock consistency across entire projects instead of starting from scratch every time.

---

**Reference Boards · Vol 2 · GPT Image 2 · Picsart Flow**

---
