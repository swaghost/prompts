# Draw-the-Path: Image Animation with Camera Movement

**AI-Анімація картин і фото / AI Animation of Paintings and Photos**

Comprehensive tutorial on animating still images using camera path drawing technique. Transform static images (paintings, photos, panoramas) into dynamic video by drawing the camera's flight path.

---

## What's Inside

1. **Part 1**: How it works — Draw-the-Path principle
2. **Part 2**: "Kateryna" — 270° figure orbit
3. **Part 3**: "Motherland Monument" — ascending spiral around statue
4. **Part 4**: Lviv Panorama — fast FPV flythrough over city
5. **Part 5**: Ukrainian Classics + Cat — following a moving character
6. **Part 6**: Troubleshooting guide: common bugs and fixes

---

## PART 1: How It Works

### Main Concept

You take a still image (painting, photo, panorama) and draw a line on it — the path that the camera will fly. The video generator (Seedance / similar) reads the drawn line as a camera trajectory in 3D space, and the image itself as a real scene with depth. The line is not visible in the final video: it's only a "director's instruction."

### Two Types of Movement

**1. Frozen Scene**

- Painting/statue stays motionless, ONLY camera moves (orbit, spiral, flythrough)
- Used for: Kateryna, Motherland Monument, Lviv

**2. Moving Character**

- Scene has a living object (cat) that moves along the route, camera follows
- People can react
- Used for: Classics + Cat case

### General Workflow

**STEP 1**: Prepare image

- Take existing painting/photo in high quality, or generate frame for your concept

**STEP 2**: Draw camera path

- In any editor (Preview, Canva, Paint, phone markup)
- Draw one continuous line
- Mark start with a bold dot and direction arrows along the path

**STEP 3**: Insert prompt and generate

- Upload marked image to generator
- Insert ready prompt from this guide
- Launch

### Golden Rules for Lines

- **One continuous line** without branching
- Never cross the line over itself
- Never go backwards — reads as glitch
- Wide smooth arcs generate cleanly, sharp angles cause distortion
- Use bright color not present in image (neon-green, cyan, magenta)

---

## PART 2: Figure Orbit — "Kateryna"

**Goal**: Camera orbits motionless figure in wide arc (up to 270°), goes behind her back and returns to face. Scene is frozen, only camera and ribbons in wind move.

### Step by Step

**STEP 1: Image**

- Take high-quality painting reproduction
- Save clean file separately (needed if line needs redrawing)

**STEP 2: Draw orbit arc**

- Start dot: bottom-right of figure
- Draw arc around figure — right, behind back, exit left (almost a circle)
- Direction arrows along path
- Leave air space, don't press line to face
- Color: neon-green or cyan (NOT magenta/red — will blend with red skirt and ribbons)

**STEP 3: Insert prompt and generate**

- Duration: 8 seconds (270° cannot be shorter — camera will rush and distort)

### Hardest Part

When orbiting >180°, camera goes behind figure — but there's no back in the painting. Prompt has special "CROSSING BEHIND HER" block that forces back to be drawn once and kept stable. If back still drifts — reduce arc to 150–180° or set duration to 10s.

### Ready Prompt — "Kateryna"

```
COPY-PASTE · FIGURE ORBIT · 8S

CRITICAL — REMOVE THE MARKING FIRST: there is a bright magenta/pink hand-drawn line, arrow and numbers drawn over this image. It is a DIRECTOR'S ANNOTATION, NOT part of the painting. It is never rendered, never visible, never treated as an object, never lit and never reflected. There is NO pink or magenta line, arrow or number anywhere in the scene. Remove it completely from every single frame. Under the line is the woman's red skirt, her red ribbons and the background — render those normally, clean, without any drawn line on top.

FIRST FRAME: exactly the reference image, full composition, untouched, but WITHOUT the drawn magenta line, arrow or numbers. The shot opens on this identical framing and the camera is already easing into motion from the very first frame.

The reference image is a real 3D space. It is an open-air Ukrainian steppe scene with real depth. The young barefoot woman stands at the centre as a solid three-dimensional body with a real front, real sides and a real back. Behind and around her at genuine distances are the mounted soldier on his horse at the left, the old seated peasant in the broad straw hat at the lower right, the wooden windmill far left, the great oak trunk at the right, the roadside post, the small dog and the hazy steppe horizon.

Preserve everything exactly: the young woman standing at centre, head bowed, eyes lowered, calm and sad, the flower wreath and trailing red ribbons on her head, the loose white embroidered blouse, the red skirt and patterned woven apron, her bare feet on the sandy road, her hands at her sides; the mounted soldier in dark uniform on the brown horse at the left; the old peasant in the broad straw hat seated at the lower right; the windmill, the oak, the roadside post, the dog, each in its exact position, pose, scale and proportion.

CAMERA, one unbroken 8 second move, no cuts, ONE SINGLE WIDE ORBIT around the standing woman: The camera makes one clean continuous circle around her, roughly two hundred and seventy degrees, beginning low at her front-right near the seated peasant, sweeping around her right side, behind her, and around her left side to end facing her from the left near the soldier.

PARALLAX IS THE POINT, and the wide orbit is what creates it. As the camera circles, the woman's nearest shoulder and skirt sweep past fastest, her body next, the seated peasant and the oak trunk behind her slower, and the soldier, the windmill, the post and the far steppe haze slowest of all.

CROSSING BEHIND HER — THE HARD PART: because the camera orbits roughly 270 degrees, the woman's back WILL come fully into view partway through the move. Build her back once and keep it stable: the back of her flower wreath with the red ribbons trailing down, the back of her white blouse, the back of her red skirt and woven apron sash, her hair gathered under the wreath, her arms at her sides seen from behind.

THE SCENE IS OTHERWISE COMPLETELY FROZEN. The woman does not move, breathe, turn or change expression. The soldier, horse, seated peasant and dog are all held perfectly still. Nothing walks, turns or gestures.

THE ONLY MOVING ELEMENT: the red ribbons trailing from the wreath on her head flutter and wave gently and continuously in a soft breeze, lifting and drifting to the side and settling, light and airy — subtle and constant throughout.

Cinematic, 24fps, 8 seconds total, shallow depth of field with focus riding the woman.

NEGATIVE: no drawn line, no magenta line, no pink line, no arrow, no hand-drawn marking, no numbers, no path overlay. No cuts, no jump, no teleport, no camera reversal.

AUDIO: no music, foley only — faint steppe wind, distant birds, soft rustle of fabric and ribbons.
```

---

## PART 3: Ascending Spiral — "Motherland Monument"

**Goal**: Camera spirals upward around statue from bottom to top — wraps figure like a helix and exits at face level, with sword and shield against sky. Simultaneously rotating + climbing.

### Step by Step

**STEP 1: Image**

- Photo of statue at full height, with space around (sky, city below)

**STEP 2: Draw spiral**

- Start dot: bottom near pedestal
- Draw line as helix upward — wrap statue: skirt → waist → chest → shoulders → face
- Finish arrow at face level
- Color: gold, white or neon — main thing is contrast with metal and sky

**STEP 3: Insert prompt and generate**

- Duration: 8–10 seconds (full spiral bottom-up 8s minimum; if cramped, set to 10)

### Key for Spiral

Model tends to break helix into "first rotation, then climb." Prompt has direct line "It BOTH climbs and orbits at the same time" and prohibition "never descends, never stalls" — this keeps movement as one helix. This is ambitious movement: may need 2–3 generations.

### Ready Prompt — "Motherland Monument"

```
COPY-PASTE · ASCENDING SPIRAL · 8–10S

FIRST FRAME: exactly the reference image, full composition, untouched — but WITHOUT any drawn glowing line, arrow or numbers. The golden spiral drawn over the image is a DIRECTOR'S ANNOTATION marking the camera path, NOT part of the scene.

The reference image is a real 3D space. It is a colossal metal statue of a standing woman holding a raised sword and a shield, on a tall stone pedestal, high above a real city at golden-hour sunset.

CAMERA, one unbroken 8 second move, no cuts, ONE CONTINUOUS RISING SPIRAL climbing around the statue: The camera begins low at the base of the pedestal on the right side, then spirals upward and around the statue in one smooth continuous helix — circling her lower robe, rising past her waist, continuing around and up past her chest and shoulders, and ending high, level with her face.

CAMERA RULES: one direction, one continuous ascending spiral, start to finish. It BOTH climbs and orbits at the same time, smoothly and continuously — the height rises steadily the entire move and the angle rotates steadily the entire move, together forming one clean helix. Never reverses, never doubles back, never descends, never stalls.

PARALLAX IS THE POINT, and the rising spiral is what creates it. As the camera climbs and circles, the statue's nearest surfaces sweep past fastest and closest, the body next, while the city, river, bridges and hills far below rotate and drift slowly beneath.

CLIMBING AND CIRCLING — THE HARD PART: because the camera spirals around her, her sides and partly her back WILL rotate into view as it climbs. Build them once and keep them stable and consistent with the front. The statue stays a single consistent monument throughout.

THE SCENE IS COMPLETELY FROZEN except for slow natural atmosphere. The statue does not move, bend, turn or change. The only living motion is environmental and subtle: the sunset clouds drift slowly across the sky, faint haze shifts over the distant city.

STYLE: cinematic aerial photography, golden-hour sunset, epic scale, atmospheric haze.

NEGATIVE: no drawn line, no glowing line, no golden spiral, no arrow, no numbers. No cuts, no jump, no teleport, no camera reversal, no descent.

AUDIO: no music, foley only — high wind at altitude, faint distant city hum, soft air.
```

---

## PART 4: FPV Flythrough — Lviv Panorama

**Goal**: Fast FPV drone flight over Old Town — camera dives between roofs, wraps around Town Hall tower, climbs to horizon. City motionless, camera provides movement.

### Step by Step

**STEP 1: Image**

- Aerial photo or generated panorama of Lviv from above (roofs, Town Hall, domes, High Castle hill in distance)

**STEP 2: Draw flight route**

- Start dot: bottom over near roofs
- Draw winding line through city: past Town Hall tower → over roofs → up to horizon
- Smooth arcs, not sharp angles
- Direction arrows; final arrow toward hill/tower in distance
- Color: red or neon — contrast with warm roofs

**STEP 3: Insert prompt and generate**

- Duration: 8–10 seconds for long route (5s cannot fit long line — will cause cut)

### If Mid-Frame Cut (Jump)

Main cause: route too long/dynamic for time; model "teleports" between nodes. Fix: (1) simplify line — fewer nodes, wider arcs; (2) increase duration; (3) prompt already has "ONE SINGLE UNBROKEN TAKE" block against cuts. Smooth sharp angles on line into wide banks.

### Ready Prompt — Lviv Panorama

```
COPY-PASTE · FPV FLYTHROUGH · 8–10S

Please remove all drawn red lines, arrows and the dot from the final video. They are ONLY a camera-path guide.

FIRST FRAME: exactly the reference image, untouched and clean of any drawn line — a golden-hour aerial panorama of the old city of Lviv.

This is a cinematic ULTRA-FAST FIRST-PERSON FPV DRONE SHOT, one continuous single take, no cuts, following the drawn path EXACTLY and in sequence through the real 3D city.

FOLLOW THE DRAWN PATH IN ORDER, start dot to final arrow: begin low at the lower-left over the near rooftops, skim fast and weave upward over the tiled roofs and baroque domes, banking left and right between the towers, rushing toward the central Town Hall clock tower. Sweep in close and bank sharply around the Ratusha tower, then climb and accelerate away over the rooftops to the upper right, threading between church towers, and finally race up and out toward the distant wooded hill and the lattice tower on the horizon.

ABSOLUTELY ONE SINGLE UNBROKEN TAKE — no cut, no jump, no edit, no scene change, no transition of any kind at any point in the middle of the shot.

CAMERA FEEL: real FPV racing drone, hand-flown, fast but smooth and continuous. Aggressive banking into every turn, fast dives and steep climbs.

PARALLAX IS THE POINT and the speed creates it: the near rooftops and façades tear past the lens fast, the Town Hall tower and church domes swing past with strong depth separation.

THE CITY ITSELF IS STILL — only the drone moves through it, plus soft natural atmosphere.

STYLE: cinematic aerial FPV footage, warm golden-hour light over Lviv's Old Town.

NEGATIVE: no drawn line, no red line, no arrows, no dot. No cuts, no jump cuts, no teleport.

AUDIO: no music, foley only — fast wind rush at speed, faint city ambience below, distant church bells, air.
```

---

## PART 5: Moving Character — Classics + Cat

**Goal**: Most complex case: ginger cat walks through living room past Ukrainian classics (Shevchenko, Franko, Hrushevsky, Lesia Ukrainka, Krushelnytska), jumps on them and furniture, camera follows cat. People are alive and react.

Requires TWO images: clean frame + frame with route.

### Step by Step

**STEP 1: Generate starting frame**

- Frame must be designed for movement: cat large in foreground with back to camera, camera at its level, five classics arranged in S-shaped path
- Prompt for frame generation below (separate)

**STEP 2: Save clean frame + draw route**

- Save clean frame separately (this is image_1)
- On copy, draw cat's route: start dot on cat → past Shevchenko's boot → onto Franko's desk → past Hrushevsky's table → to Lesia → finish arrow at Krushelnytska by piano (this is image_2)
- Draw line low (along floor, furniture legs, dress edges), not through faces
- Color: yellow/green

**STEP 3: Insert video prompt with two frames**

- Upload image_1 (clean) + image_2 (with line)
- Insert video prompt below
- Format 3:4

### Secret Why Cat "Just Walks"

Draw-the-path only sets SEQUENCE. For cat to jump and climb, actions must be described in words at each node (JUMPS UP onto his lap, WALKS ALONG THE DESK, leaps down). For people to react — write "ALIVE AND REACT". Video prompt below already has this.

### Prompt 1 — Starting Frame Generation (photo, 3:4)

```
COPY-PASTE · FOR GPT IMAGE / NANO BANANA

Create a photorealistic, cinematic live-action style 3:4 vertical opening frame.

BRIGHT SUNNY DAYTIME. Warm golden sunlight streams in through a tall window.

A LOW CAT-HEIGHT wide-angle perspective, camera down at floor level. A large ginger (orange tabby) cat enters from the lower foreground, big and close in frame, its back to the camera — the camera is right down at the cat's level behind it.

The room is a warm, bright, richly detailed late-19th-century Ukrainian salon parlour on a sunny day: velvet armchairs, a carved wooden writing desk, tall bookshelves, an ornate rug, a grand piano on the right, framed pictures on the walls, potted plants catching the light.

Five recognizable figures of Ukrainian cultural history are placed around the room at staggered nodes along an S-shaped path:

1. Near the entrance, lower left, reading in an armchair: Taras Shevchenko — bald with a full drooping moustache, in a warm fur-collared coat
2. At the carved desk with books: Ivan Franko — bearded, round spectacles, modest dark suit
3. Central, tallest node, standing at a large writing table: Mykhailo Hrushevsky — long full grey beard, glasses, formal dark suit
4. In a soft armchair: Lesya Ukrainka — elegant young woman, dark hair in a braided crown, refined high-collared dress
5. At the grand piano by the sunlit window: Solomiya Krushelnytska — poised opera diva in a graceful day gown

The ginger cat starts far from the piano, large in the lower foreground, back to camera. The whole space forms one continuous S-shaped path winding from the cat past Shevchenko, to Franko, around Hrushevsky, past Lesya Ukrainka, ending at Krushelnytska by the piano.
```

### Prompt 2 — Video Generation (image_1 + image_2, 3:4)

```
COPY-PASTE · FOR SEEDANCE · CAT FOLLOWING + ACTIONS + REACTIONS

Use image_1 as the exact clean starting frame and primary visual identity reference. Use image_2 only as an invisible director map — the blue line, the start dot (1) on the cat and the arrow (2) define the ginger cat's route, node order, camera direction and endpoint. NO drawn marks appear in the video.

Aspect ratio 3:4, vertical.

Preserve the same photorealistic sunlit salon and the same five figures: Taras Shevchenko, Ivan Franko, Mykhailo Hrushevsky, Lesya Ukrainka, Solomiya Krushelnytska.

Start immediately with the ginger cat moving from the lower foreground, its back to the camera. THE CAMERA FOLLOWS CLOSE BEHIND THE CAT AT CAT HEIGHT — a smooth low invisible FPV camera gliding just behind the cat, at floor level.

THE CAT'S ROUTE AND ACTIONS, in order along the drawn path:
- It pads across the parquet toward Shevchenko, then JUMPS UP onto his lap; Shevchenko lowers his book and gently looks down at the cat with a warm smile
- The cat steps off onto the carved desk and WALKS ALONG THE DESK past Franko's books; Franko lifts his pen and watches the cat, amused
- The cat crosses to Hrushevsky's table and pads along its edge; Hrushevsky looks up and follows the cat with his eyes
- The cat leaps down toward Lesya Ukrainka and brushes along the arm of her chair; she turns her head and lightly reaches toward it
- The cat moves to the grand piano and JUMPS DOWN to the floor by Krushelnytska, who turns from the piano and reaches toward the cat

THE PEOPLE ARE ALIVE AND REACT to the cat: each figure naturally turns their head, shifts their gaze, and moves a hand toward the cat — subtle, warm, lifelike reactions. Their faces stay stable, lifelike and photoreal at all times.

CAMERA FEEL: smooth low FPV at cat height, following the cat like a steadicam, banking gently around furniture.

NEGATIVE: no drawn line, no blue line, no dot, no number, no arrow. No cuts, no jump cuts, no teleport. No morphing or distorting faces.

AUDIO: no music, foley only — soft cat footsteps and landings, page turning, gentle laughter, a piano note near the end.
```

---

## PART 6: Troubleshooting Guide

### Common Problems and Fixes

**• Drawn line stayed in video**

- Redraw with color not in frame (neon-green/cyan)
- Move line prohibition to start of prompt and duplicate in NEGATIVE
- Make line thinner

**• Camera just goes up-down, doesn't orbit**

- Your line is arc/loop above scene, model reads only vertical
- Redraw as arc FROM THE SIDE around object
- In prompt: "PRIMARY motion is horizontal orbit, NOT vertical"

**• Mid-frame cut / jump**

- Route too long for time
- Simplify line (fewer nodes, wider arcs) or increase duration
- "ONE SINGLE UNBROKEN TAKE" block already in prompt

**• Face/back drift during orbit**

- Camera went behind, back doesn't exist in painting
- Reduce arc angle, or give more time (10s)
- "build the back once and keep it stable" block

**• Spiral "sags" or breaks apart**

- Model splits helix into rotation+climb separately
- Keep line "BOTH climbs and orbits at the same time" and "never descends, never stalls"

**• Cat just walks, doesn't jump**

- Describe ACTIONS in words at each node (JUMPS UP, WALKS ALONG)
- Line alone doesn't set actions — only sequence

**• People frozen, don't react**

- Add "THE PEOPLE ARE ALIVE AND REACT" + reaction description for each (turns head, reaches hand to cat)

**• Object "hangs" in air (vehicle/character)**

- Triple emphasize it moves itself ("keeps moving, never hovers")
- Add to NEGATIVE "no frozen, no floating"

**• Style drifted to cartoon**

- At start of prompt hard: "photorealistic, NOT animated, NOT cartoon, NOT 3D"
- Add "35mm film, realistic photography"

**• Too dark/depressive frame**

- In frame generation prompt: "BRIGHT SUNNY DAYTIME, high-key, cheerful"
- Direct negation "NOT dark, NOT moody, NOT gloomy"

### General Principle

Scene is motionless OR has one moving character · camera goes along drawn line · movement is described in words.

---

## Credits

Tutorial demonstrates Draw-the-Path technique for animating still images with camera movement control. Works with paintings, photos, architectural visualizations, and generated images.
