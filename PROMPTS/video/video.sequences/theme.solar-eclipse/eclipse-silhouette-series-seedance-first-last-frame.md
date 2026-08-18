# Eclipse Silhouette Series - Seedance First & Last Frame Workflow

**Platform:** Seedance (Higgsfield AI)  
**Technique:** First & Last Frame Workflow  
**Duration:** 5 seconds per shot  
**Style:** Cinematic anamorphic silhouette cinematography  
**Series Concept:** One empty eclipse plate, multiple subjects, consistent visual language

---

## Concept

The Eclipse Silhouette Series demonstrates a powerful first-and-last-frame workflow where one empty eclipse plate serves as the first frame for multiple shots. Each subject enters from off-screen right, walks to center, and strikes a final pose. The camera never moves, the background never changes, and subjects are rendered as pure black silhouettes—simplifying the generation problem while creating visually striking cinematic sequences.

**Perfect for:** Epic fantasy sequences, character introductions, dramatic reveals, silhouette cinematography, series consistency, brand campaigns, cinematic trailers

---

## The Method

### Core Principle

Every shot uses the same trick: **the camera never moves, the background never changes, and the subject is pure black silhouette**. This means the model only has to solve one problem—moving a shape across a static frame—and it solves that well. The instant you add camera movement or readable surface detail on the subject, the eclipse starts warping and the illusion dies.

### Why First & Last Frame Works

The subject enters from off-screen right, so it **does not exist in the opening frame**. That makes the empty eclipse plate a perfect first frame. The final pose already exists as a still, so that becomes the last frame. The model is left to interpolate the walk-in—which is exactly the part it should be inventing, and the part your prompt describes.

### Workflow Steps

1. **Generate the empty plate once** - Eclipse ring, bare ridgeline, nothing on the crest. This single file is the first frame for all three shots—that is what makes the set feel like one series instead of three unrelated clips.

2. **Generate each subject plate** - Same eclipse, same ridge, subject standing dead center in its final pose. Feed the empty plate in as a reference so the ring size and ridge line match.

3. **Load first frame = empty plate, last frame = subject plate**

4. **Paste the matching prompt, set 5 seconds, generate**

---

## Four Rules That Make or Break It

### 1. State the Camera Lock Three Ways

**"Locked-off tripod, no camera movement whatsoever, the frame never changes."**

Saying it once is not enough—Seedance will drift. Repeat the constraint at the beginning of the prompt with variations:

- "no zoom, no push-in, no pull-back"
- "no pan, no tilt, no reframing"
- "the camera stays completely still"

### 2. Say "The Crest is Empty" Explicitly

Without it, the model often opens with the subject already standing there and you lose the entrance entirely. Make it explicit in the video prompt.

### 3. Name the Exact Centre as the Destination

**"Walks steadily left until it reaches the exact centre of the eclipse"** is what lands the subject on your last frame cleanly. Be specific about the endpoint.

### 4. Describe Cloth as Fluid, Never as Snapping

Words like **taut** and **snaps** produce a stiff cardboard flag. Use:

- "Rolling waves"
- "Folding over on itself"
- "Curling edges"
- "Rippling loosely"
- "Billowing and collapsing"

That is what gets real fabric physics.

---

## The Base Plate (Generate Once)

Everything downstream depends on this file. Generate it first, keep it, and feed it in as a reference image when you generate each subject plate—that is what keeps the ring diameter, ridge curve, and corona brightness identical across the series. If the ring shifts even slightly between plates, the cuts stop matching and the set falls apart.

### Empty Eclipse Plate - Image Prompt

```
A cinematic anamorphic still photograph, extreme wide shot on a heavy telephoto lens. A total solar eclipse dominates the frame — a flat charcoal disc ringed by a searing thin band of amber-white corona, bleeding a soft warm halo outward into a deep neutral grey-violet sky — sitting low behind a bare dark ridgeline. The ridgeline is a smooth unbroken dark curve cutting across the lower third of the frame, its top edge kissed by a thin rim of amber light where it meets the glow. The crest is completely empty — no figures, no vegetation, no structures, no landmarks. Fine dust and atmospheric haze drift through the light, catching faint volumetric beams that fan down toward the ridge. Shot on ARRI Alexa Mini LF, Panavision Ultra Vintage anamorphic 85mm at T2.3, Tiffen Black Pro-Mist 1/4, heavy telephoto compression flattening the eclipse against the ridge, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D film emulation with fine 400 ASA grain, subtle chromatic aberration at the frame edges, soft lens vignette, gentle halation bloom around the corona edge. Photographic, not rendered.
```

**Key Elements:**

- Total solar eclipse with searing amber-white corona
- Bare dark ridgeline across lower third
- Completely empty crest (critical)
- Grey-violet sky
- Anamorphic cinematic aesthetic
- Heavy telephoto compression
- Kodak Vision3 250D film emulation
- No figures, vegetation, or structures

---

## Shot 1: The Banner Warrior

### Direction Note

The hardest of the three, because the flag is the whole shot. Roughly a third of the video prompt is spent on cloth physics alone—that ratio is deliberate. If the banner comes back stiff, push further into the fluid language rather than adding wind.

### Step 1: Build the Last Frame Plate

**Image Prompt:**

```
A cinematic anamorphic still photograph, extreme wide shot on a heavy telephoto lens. A lone warrior stands in full silhouette on the crest of a bare dark ridgeline, dead centre of frame, rendered entirely as black shape with no facial detail and no colour readable — only contour. Segmented plate armour with layered pauldrons and a ridged crested helm, a heavy cloak hanging from the shoulders and lifting at the hem in the wind. Both hands gripping a long banner staff driven into the ground at his side, the staff rising vertically through the centre of the frame. A large heavy banner hangs from a crossbar near the top of the staff, catching wind and pulling sideways, the fabric rippling with visible weight and a ragged frayed trailing edge, its embroidered emblem readable only as dark negative shape against the light behind it. Behind and above the ridge, a total solar eclipse fills the upper two thirds of the frame — flat charcoal disc, searing thin amber-white corona, warm halo bleeding into a deep grey-violet sky. Dust and haze drift through faint volumetric beams. The ridge is a smooth unbroken dark curve across the lower third, top edge rimmed in amber. No vegetation, no structures. Shot on ARRI Alexa Mini LF, Panavision Ultra Vintage anamorphic 85mm at T2.3, Tiffen Black Pro-Mist 1/4, heavy telephoto compression, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D with fine grain, soft vignette and halation bloom on the corona edge. Fabric with real weave, real weight, real drape and wind load. Metal armour with worn edges and a hard specular rim where the backlight catches the silhouette. Photographic, not rendered.
```

### Step 2: Animate It

**Settings:**

- First frame: the empty eclipse plate
- Last frame: the plate you just generated
- Duration: 5 seconds
- Multi-shot: off

**Video Prompt (5 seconds):**

```
Extreme long-lens telephoto shot, locked-off tripod, no camera movement whatsoever — no zoom, no push-in, no pull-back, no pan, no tilt, no reframing. The frame never changes. A total solar eclipse fills the frame — a flat black disc ringed by a searing amber-white corona bleeding into a deep grey-violet sky — sitting low behind a bare dark ridgeline. The crest is empty. A lone warrior in pure black silhouette walks in from the right edge of frame along the ridgeline, crested helm, segmented plate armour, a long banner staff carried in one hand, his cloak dragging sideways in the wind, dust lifting from each footfall. The banner is thin worn cloth, soft and weightless, never stiff and never board-like — it undulates continuously in slow rolling waves down its length, the fabric rippling and folding over on itself, the frayed trailing edges curling and fluttering loosely, catching air pockets that travel from the staff outward to the tip. He walks steadily left until he reaches the exact centre of the eclipse, then stops and plants the staff butt into the ground, both hands settling on it, chin lifting. The banner keeps flowing the whole time, billowing and collapsing and billowing again, folds sliding across the corona behind it, the cloak rippling loosely against his legs. Dust drifts through the corona light, heat shimmer along the horizon. Only the subject and the cloth move; the camera stays completely still. Heavy telephoto compression flattening the eclipse against the ridge, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D with fine grain, soft vignette and halation bloom on the corona edge, 24fps 180 degree shutter, roughly five seconds. Audio: diegetic only — low steady wind across open ground, boots compressing dry earth, armour plates shifting with each stride, the staff thudding into the ground, soft cloth rippling and fluttering, grit skittering downslope, no music.
```

---

## Shot 2: The Rearing Horseman

### Direction Note

The rear is a landing pose, not a passing moment, which is why it works as a last frame. The video prompt lets the horse settle its hooves back down after the rear so the clip does not end on a frozen peak—that small resolution beat is what makes it feel filmed rather than generated.

### Step 1: Build the Last Frame Plate

**Image Prompt:**

```
A cinematic anamorphic still photograph, extreme wide shot on a heavy telephoto lens. A lone rider on horseback in full silhouette on the crest of a bare dark ridgeline, dead centre of frame, rendered entirely as black shape with no facial detail and no colour readable — only contour. The horse mid-rear, front hooves lifted clear of the ground and forelegs folded, neck arched, tail streaming sideways, mane lifting. The rider leaning back into the motion, a long spear held upright in one raised hand, a cloak flaring out behind and breaking into a torn ragged edge against the light. Behind and above the ridge, a total solar eclipse fills the upper two thirds of the frame — flat charcoal disc, searing thin amber-white corona, warm halo bleeding into a deep grey-violet sky. Dust kicked up from the hooves drifts through the beam, catching faint volumetric shafts fanning down toward the ridge. The ridge is a smooth unbroken dark curve across the lower third, top edge rimmed in amber. No vegetation, no structures. Shot on ARRI Alexa Mini LF, Panavision Ultra Vintage anamorphic 85mm at T2.3, Tiffen Black Pro-Mist 1/4, heavy telephoto compression, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D with fine grain, soft vignette and halation bloom on the corona edge. Cloak fabric with real weave, real weight and wind load. Horse musculature and tack with real surface detail and a hard specular rim where the backlight catches the silhouette. Photographic, not rendered.
```

### Step 2: Animate It

**Settings:**

- First frame: the empty eclipse plate
- Last frame: the plate you just generated
- Duration: 5 seconds
- Multi-shot: off

**Video Prompt (5 seconds):**

```
Extreme long-lens telephoto shot, locked-off tripod, no camera movement whatsoever — no zoom, no push-in, no pull-back, no pan, no tilt, no reframing. The frame never changes. A total solar eclipse fills the frame — a flat black disc ringed by a searing amber-white corona bleeding into a deep grey-violet sky — sitting low behind a bare dark ridgeline. The crest is empty. A rider on horseback in pure black silhouette gallops in from the right edge of frame along the ridgeline, a long spear held upright in one raised hand, a cloak streaming out behind, the horse at full stride with mane and tail flying, hooves throwing up plumes of dust that hang and drift through the corona light. He rides steadily left until he reaches the exact centre of the eclipse, then hauls back on the reins and the horse rears, front hooves lifting clear of the ground and forelegs folding, neck arching, the rider leaning back into the motion with the spear still held high. The cloak flares wide and falls, rippling loosely, never stiff. The horse settles its front hooves back down and holds, chest heaving, tail swinging. Dust continues drifting through the light, heat shimmer along the horizon. Only the subject and the cloth move; the camera stays completely still. Heavy telephoto compression flattening the eclipse against the ridge, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D with fine grain, soft vignette and halation bloom on the corona edge, 24fps 180 degree shutter, roughly five seconds. Audio: diegetic only — hooves drumming on dry earth, a low whinny, wind across open ground, cloth rippling and snapping loose, tack and stirrups jangling, heavy breathing from the animal, grit skittering downslope, no music.
```

---

## Shot 3: The Dragon Rider

### Direction Note

The wing unfurl is the payoff. Backlight through the membrane exposes the vein structure, so both prompts call that out directly—it is the one moment in the series where the subject stops being a flat black shape. Keep the walk-in with wings folded so the reveal has somewhere to go.

### Step 1: Build the Last Frame Plate

**Image Prompt:**

```
A cinematic anamorphic still photograph, extreme wide shot on a heavy telephoto lens. A colossal winged dragon stands on the crest of a bare dark ridgeline, centred in frame, rendered entirely as black shape with no colour or surface detail readable — only contour. Broad ribbed wings raised and spread wide, the thin membrane translucent where the light behind burns through it, the dark branching finger-bones and segmented leading-edge ridge clearly visible inside the membrane as darker lines. Head lowered and turned in profile with swept-back horns and open jaw. Four legs planted, long spined tail curling down the far slope. A single small rider silhouette seated at the base of the neck, upright, one hand raised, dwarfed to almost nothing against the mass of the animal. Behind and above the ridge, a total solar eclipse fills the upper two thirds of the frame — flat charcoal disc, searing thin amber-white corona, warm halo bleeding into a deep grey-violet sky. Dust and haze drift through faint volumetric beams. The ridge is a smooth unbroken dark curve across the lower third, top edge rimmed in amber. No vegetation, no structures. Shot on ARRI Alexa Mini LF, Panavision Ultra Vintage anamorphic 85mm at T2.3, Tiffen Black Pro-Mist 1/4, heavy telephoto compression, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D with fine grain, soft vignette and halation bloom on the corona edge. Wing membrane with real thickness and real light transmission through the skin, hide and scale plating with real surface relief along the silhouette edge. Photographic, not rendered.
```

### Step 2: Animate It

**Settings:**

- First frame: the empty eclipse plate
- Last frame: the plate you just generated
- Duration: 5 seconds
- Multi-shot: off

**Video Prompt (5 seconds):**

```
Extreme long-lens telephoto shot, locked-off tripod, no camera movement whatsoever — no zoom, no push-in, no pull-back, no pan, no tilt, no reframing. The frame never changes. A total solar eclipse fills the frame — a flat black disc ringed by a searing amber-white corona bleeding into a deep grey-violet sky — sitting low behind a bare dark ridgeline. The crest is empty. A colossal winged dragon in pure black silhouette walks in from the right edge of frame along the ridgeline, four-legged and heavy, wings folded tight against its flanks, horned head swinging low with each stride, the long spined tail dragging a slow curve behind it, dust lifting in plumes from every footfall. A small rider silhouette sits at the base of its neck, upright, one hand raised. It walks steadily left until it reaches the exact centre of the eclipse, then stops, plants its feet, and unfurls both wings wide and high in one slow heavy sweep — the thin ribbed membrane stretching taut and lighting up translucent as the corona burns through it, the dark branching vein structure blazing into visibility inside the skin. The head lifts and turns into profile, jaw parting. The wings hold spread, trembling faintly under the wind, membrane rippling. Dust drifts up through the corona light, long shadows stretching down the slope toward camera. Only the creature moves; the camera stays completely still. Heavy telephoto compression flattening the eclipse against the ridge, deep focus, strong negative space, warm amber against cold desaturated grey, Kodak Vision3 250D with fine grain, soft vignette and halation bloom on the corona edge, 24fps 180 degree shutter, roughly five seconds. Audio: diegetic only — heavy footfalls compressing dry earth, a deep leathery groan as the wings unfurl, membrane snapping and rippling under wind load, a low chest rumble, claws scraping stone, wind across open ground, grit skittering downslope, no music.
```

---

## Troubleshooting Guide

| **What You See**                                  | **What To Change**                                                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **The eclipse ring drifts, breathes or warps**    | Camera lock is not stated hard enough. Repeat the no-move clause at the very start of the prompt, not the end.            |
| **Subject is already centred at frame one**       | Add or strengthen "the crest is empty" and "enters from the right edge of frame".                                         |
| **Subject overshoots or stops off-centre**        | Reinforce the destination — "the exact centre of the eclipse" — and confirm your last frame is loaded.                    |
| **Flag or cloak looks like painted cardboard**    | Strip out taut/snap/whip. Replace with rolling waves, folding over on itself, curling frayed edges.                       |
| **Corona goes wispy and white, not a tight ring** | Drop "total solar eclipse" back to "eclipse ring" — the astro-photo phrasing pulls it that way.                           |
| **Silhouette reads as a solid black blob**        | The subject needs a gap in it — spread wings, a raised spear, a flag pulling sideways. Solid shapes vanish at this scale. |

---

## Extending the Series

The frame is the format—anything that enters from the right and stops centre will fit.

**Strong Candidates:**

- A pegasus landing with wings in the upstroke
- A lone wolf cresting the ridge
- A ship's mast rising behind the hill
- An armoured column marching through in single file
- A giant with a massive hammer raised
- A mounted knight with lance
- A winged angel descending
- A mechanical walker (sci-fi variant)

**Critical Rule:** Keep the empty plate identical every time and the whole set cuts together as one sequence.

---

## Technical Specifications

**Platform:** Seedance (Higgsfield AI)  
**Technique:** First & Last Frame Workflow  
**Duration:** 5 seconds per shot  
**Frame Rate:** 24fps, 180 degree shutter  
**Aspect Ratio:** Anamorphic (likely 2.39:1)  
**Film Emulation:** Kodak Vision3 250D, 400 ASA grain  
**Camera Specs:** ARRI Alexa Mini LF, Panavision Ultra Vintage anamorphic 85mm at T2.3  
**Filtration:** Tiffen Black Pro-Mist 1/4  
**Lens Characteristics:** Heavy telephoto compression, deep focus  
**Audio:** Diegetic only (no music)

---

## Advanced Techniques

### Cloth Physics Language Library

**Fluid (Good):**

- "Rolling waves"
- "Folding over on itself"
- "Curling edges"
- "Rippling loosely"
- "Billowing and collapsing"
- "Undulates continuously"
- "Frayed trailing edges fluttering"
- "Catching air pockets"

**Stiff (Bad):**

- "Taut"
- "Snaps"
- "Whips"
- "Pulled tight"
- "Rigid"

### Camera Lock Reinforcement Pattern

State the constraint three ways at the start of every video prompt:

1. "Extreme long-lens telephoto shot, locked-off tripod"
2. "no camera movement whatsoever — no zoom, no push-in, no pull-back, no pan, no tilt, no reframing"
3. "The frame never changes"

Then reinforce later: "Only the subject and the cloth move; the camera stays completely still."

### Subject Entry & Landing Pattern

**Opening State:**

- "The crest is empty"
- "[Subject] walks/rides/moves in from the right edge of frame"

**Journey:**

- "walks/rides steadily left"
- "until it reaches the exact centre of the eclipse"

**Landing:**

- "then stops and [performs final action]"
- End with resolution beat (banner settles, horse hooves down, wings hold spread)

---

## Use Cases & Applications

### Cinematic Trailers

- Character introductions
- Epic fantasy sequences
- Army reveals
- Hero moments

### Brand Campaigns

- Product launches with dramatic silhouette reveals
- Logo animations with epic scale
- Series consistency across multiple products

### Music Videos

- Artist introduction sequences
- Silhouette performance segments
- Visual metaphor sequences

### Title Sequences

- Opening credits with character reveals
- Chapter transitions
- Episode markers

### Social Media Content

- Instagram story sequences
- TikTok dramatic reveals
- YouTube intro sequences

---

## Quick Reference Card

**WORKFLOW:**

1. Generate empty eclipse plate (once)
2. Generate subject plate (use empty as reference)
3. Load: First frame = empty, Last frame = subject
4. Paste video prompt, 5 seconds, generate

**CRITICAL CONSTRAINTS:**

- Camera lock (state 3 ways)
- "Crest is empty" (explicit)
- "Exact centre of eclipse" (destination)
- Cloth = fluid language (never taut/snap)

**EMPTY PLATE ESSENTIALS:**

- Total solar eclipse, amber-white corona
- Bare ridgeline, lower third
- Completely empty crest
- Grey-violet sky
- Anamorphic cinematic style

**SUBJECT PLATE ESSENTIALS:**

- Pure black silhouette (no color/detail)
- Dead centre positioning
- Final pose clear and readable
- Gaps in silhouette (wings, spear, flag)
- Same eclipse/ridge as empty plate

**QUALITY CHECKS:**

- ✓ Eclipse ring consistent across plates
- ✓ Ridge curve identical
- ✓ Camera completely locked
- ✓ Subject enters from right
- ✓ Subject stops at exact centre
- ✓ Cloth flows with fluid physics
- ✓ Pure silhouette (no color bleed)
- ✓ Clear gaps in silhouette shape
- ✓ Diegetic audio only

---

_Platform: Seedance (Higgsfield AI) | Technique: First & Last Frame | Duration: 5 seconds | Style: Cinematic anamorphic silhouette | Updated: 2026_
