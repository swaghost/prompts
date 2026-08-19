# THE 9-ANGLE CAMERA PACK

**Platform:** GPT Image 2 · Picsart Flow  
**Technique:** Image-to-Image Re-rendering  
**Purpose:** Shoot one hero frame — then re-render the same moment from 9 camera angles

---

## HOW IT WORKS

You generate one hero shot first, then every other angle is a re-render of that same frame — same subject, same scene, same pose, only the camera moves. That's how you get a full coverage set that actually looks like the same moment shot from nine positions, instead of nine different photos.

> **Note:** Swap the subject, wardrobe and location for your own — keep the structure. The skeleton is what does the work, not the farm setting.

---

## THE SKELETON

Every prompt (except the hero) is built from the same five parts. Learn these and you can re-render any hero frame from any angle:

### 5-Part Prompt Structure

1. **Reference lock** — image 1 = the base frame, image 2 = her exact face. This ties the re-render to what you already made.

2. **Scene lock** — same place, nothing added, removed or moved. This paragraph does more work than the camera line.

3. **Pose lock** — her body position described in physical detail so it can't drift — every limb, hand and weight-shift named.

4. **Re-render** — the only thing that changes: where the camera stands.

5. **Constraints** — a negative list that kills the model's favourite mistakes.

> **Key Principle:** The whole point: say what STAYS before you say what CHANGES. The scene-lock and pose-lock paragraphs are the anchor — the camera instruction is just one line at the end.

---

## HOW TO USE

Runs in **Picsart Flow** with **GPT Image 2** as image-to-image.

### Workflow

1. **Shoot the hero** — Generate the Wide shot first — this is your base frame (image 1).

2. **Lock the face** — Keep a clean face reference as image 2 for every re-render.

3. **Pick an angle** — Choose a re-render prompt and feed it image 1 + image 2.

4. **Re-render** — Only the camera moves — same subject, scene and pose come back from the new angle.

5. **Build the set** — Repeat for all 9 to get full coverage of the same moment.

---

## THE 9 ANGLES

| Angle                      | Where the camera goes                                |
| -------------------------- | ---------------------------------------------------- |
| **1 · Wide Shot**          | Eye level, full body — the hero frame you build from |
| **2 · Side View**          | 90° to her side, clean profile                       |
| **3 · Three-Quarter Back** | 45° behind, she looks back over her shoulder         |
| **4 · Extreme Close-Up**   | Tight on the face, pores and eyelashes               |
| **5 · Low Angle**          | Knee height, tilted up, she rises tall               |
| **6 · Over the Shoulder**  | Behind her, looking out past her shoulder            |
| **7 · Worm's Eye**         | On the ground at her boots, pointing up              |
| **8 · High Angle**         | Raised above, tilted down onto her                   |
| **9 · Dutch Angle**        | Tilted horizon, everything on a diagonal             |

---

## THE PROMPTS

Start with the Wide shot, then re-render the rest from it.

---

### 🎬 1 · WIDE SHOT

**GPT Image 2 — start here, this is your hero frame**

Generate this one first — it becomes image 1 (the base frame) for all eight re-renders below.

```
Use image 1 for the woman's exact face, hair, glasses, butterfly clips, jewellery and wardrobe. Use image 2 for the exact location, light and colour: the same homestead, the same weathered pale blue timber house further back, the same dry rutted earth, the same low golden hour sun raking from the right with long shadows and dust in the beam, the same warm faded film grade. Photorealistic fashion editorial photograph with a documentary feel, as if found on a scanned film negative.

Move the camera out to the vegetable patch at the edge of the yard and photograph her digging there. She stands in three-quarter view to the camera, mid-stroke with a long-handled steel spade: her left boot driving down hard on the shoulder of the blade, the blade half sunk into the dark turned soil, both hands gripping the shaft with her weight leaning over it, right leg straight behind her, back angled forward, shoulders loaded. Her head is turned toward the camera and she is looking straight into the lens with a level, unbothered expression, breathing through it, a strand of damp hair stuck across her cheek.

She has been at it a while and it shows: dry earth smeared up both forearms and across the backs of her hands, a dark streak of soil on one thigh of the jeans, a smudge on her jaw and another below her collarbone, dust settled on the white ribbed tee and greying its hem, the boots caked. Nothing theatrical, just the ordinary dirt of an hour's work.

Around her: a strip of freshly turned black soil running away from her feet with the clods still loose, a rusted metal watering can and a pair of work gloves dropped on the unturned ground, and a low post-and-wire fence a few metres behind her. Beyond the fence, three brown and white cows stand in the pasture in soft focus, one of them lifted its head toward her, the others grazing. Beyond them the pasture runs to a treeline in haze.

Camera: eye level, from about two and a half metres away and slightly to her left, 35mm equivalent, level horizon, her full body in frame with the spade, the turned soil, the fence and the cows all layered behind her.

Light: the low sun from the right rims her shoulder, her right arm and the loose hair, catches the edge of the wet spade blade, and lights the airborne dust kicked up from the soil. Her face sits in soft shadow lifted by warm bounce off the bare earth. Long shadows from her and the fence posts rake across the ground.

Detail: real skin texture with freckles, sweat and dirt, individual soil crumbs on her forearms and the spade, scratched steel and worn timber shaft, dust in the ribbed knit, denim weave, caked leather boots, the coarse hair and wet noses of the cows.

Constraints: one person only, no other people, no gloves on her hands, no text, no captions, no watermark, no logos, no brand names, no modern tools, no plastic, no power lines, no tractor, no mud on her face beyond a light smudge, no HDR halos, no oversaturation, no fisheye, no tilted horizon, hands and fingers anatomically correct.
```

---

### ↔ 2 · SIDE VIEW

**GPT Image 2 — re-render at 90° profile**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery, wardrobe and the dirt on her skin and clothes — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity, the same cows in the same places beyond the fence. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she stands mid-stroke with the long-handled steel spade, her left boot driving down on the shoulder of the blade which is half sunk in the turned soil, both hands gripping the shaft with her weight leaning over it, right leg straight behind her, back angled forward, shoulders loaded.

Re-render from ninety degrees to her side, the camera relocated to that position at eye level while she holds the identical pose and head direction — her face now reading in clean profile past the lens. From this angle the whole load reads: the straight line from her shoulders down the shaft to the buried blade, the driving boot, the extended back leg. The fence and the cows run along behind her at the level of her waist, the pasture and treeline beyond in haze.

Constraints: no change of pose, no change of head direction, no lifting the spade, no objects added or removed, no other people, no text, no captions, no watermark, no logos, no fisheye distortion, no tilted horizon.
```

---

### ↩ 3 · THREE-QUARTER BACK

**GPT Image 2 — re-render from 45° behind**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she is bent forward at the waist over the iron hand pump, her left hand pushing the handle down, her right hand steadying the bucket beneath the spout, back flat, hair falling forward past her face.

Re-render from behind and to one side at roughly forty-five degrees, at eye level, so we see the curve of her back, the line of her spine and the small of her back above the low waistband in the near frame, while she looks back over that shoulder toward the lens, three quarters of her face visible with the far eye catching the low sun. The falling column of water and the wet slab read sharp beyond her, the house softer behind.

Constraints: no change of pose, no straightening up, no objects added or removed, no other people, no text, no captions, no watermark, no logos, no fisheye distortion.
```

---

### 🔬 4 · EXTREME CLOSE-UP

**GPT Image 2 — re-render tight on the face**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she is bent forward at the waist over the iron hand pump, her left hand pushing the handle down, her right hand steadying the bucket beneath the spout, back flat, hair falling forward past her face, watching the water.

Re-render as an extreme close-up: the camera moved in very tight on her face from below and to the side, framing from her brow to just below her lower lip, individual eyelashes, pores, freckles and the damp strand of hair stuck across her cheek all resolved, one bright droplet caught on her jaw. The pump and the yard fall completely out of focus into warm amber and dusty green.

Constraints: no change of pose, no change of expression, no lifting her head, no objects added or removed, no makeup added, no smoothing of skin, no text, no captions, no watermark, no logos, no fisheye distortion.
```

---

### ⬆ 5 · LOW ANGLE

**GPT Image 2 — re-render from knee height, tilted up**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she stands facing the washing line with both arms raised above her head, a wet white bedsheet half thrown over the rope and gripped in both hands, two wooden clothes pegs held between her teeth, chin lifted, weight on her right leg with the left heel off the ground, looking up at the sheet.

Re-render from a low angle: the camera lowered to knee height a short distance in front of her and tilted up, so she rises tall in the frame with her raised arms and the sheet against the sky, the dirt running as a broad band across the bottom, and the backlit glowing sheets and the hazy golden sky filling the background. The basket of laundry sits large in the near foreground, a hen beside it.

Constraints: no change of pose, both arms stay raised, no upward perspective distortion of her body, no objects added or removed, no other people, no text, no captions, no watermark, no logos, no fisheye distortion, no tilted horizon.
```

---

### 👤 6 · OVER THE SHOULDER

**GPT Image 2 — re-render past her shoulder**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she stands facing the washing line with both arms raised above her head, a wet white bedsheet half thrown over the rope and gripped in both hands, two wooden clothes pegs held between her teeth, chin lifted, weight on her right leg with the left heel off the ground, looking up at the sheet.

Re-render as an over-the-shoulder view: the camera behind her and just to one side, framing past the back of her head and her raised near shoulder in the large soft foreground, looking out along the line ahead of her. The hanging sheets and towels receding down the rope, the basket of damp laundry at her boots, the hens and the house beyond all read sharp and fill most of the view. Her face is turned away, only the edge of her cheek and a butterfly clip catching the low sun.

Constraints: no change of pose, both arms stay raised, no turning her face back to camera, no objects added or removed, no other people, no text, no captions, no watermark, no logos, no fisheye distortion.
```

---

### 🐛 7 · WORM'S EYE

**GPT Image 2 — re-render from the ground, pointing up**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she stands upright in the middle of the yard carrying the heavy galvanised bucket in her right hand, that shoulder pulled down by the weight, her weight on her left leg, left arm slightly out for balance, head turned toward the lens.

Re-render from a worm's eye view: the camera resting on the dirt right at her boots pointing steeply upward, her legs towering long and enormous in the foreground, her torso dramatically foreshortened, the bucket hanging heavy above, her face small and far at the top of frame, the hazy golden sky opening wide overhead behind her. A hen steps past in the near foreground. The scuffed leather and the dry cracked earth read sharp right at the lens.

Constraints: no change of pose, no putting the bucket down, no objects added or removed, no other people, no extreme lens distortion of her face, no text, no captions, no watermark, no logos.
```

---

### 🔽 8 · HIGH ANGLE

**GPT Image 2 — re-render from above, tilted down**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she sits on the second wooden step facing the yard, knees apart with her boots planted on the bottom step, elbows resting on her knees, forearms hanging loose, a chipped enamel mug in her right hand, shoulders relaxed and leaning slightly forward.

Re-render from a high angle: the camera raised well above her out in the yard and tilted down at roughly forty-five degrees, so we look down onto her seated figure, seeing the top of her head and shoulders with the body foreshortened below, the steps and the dirt filling most of the frame and only a strip of porch above. Her eyes lift to meet the raised camera. The hen on the step and the tipped bucket stay in place.

Constraints: she stays seated — no standing, no change of pose, no objects added or removed, no other people, no text, no captions, no watermark, no logos, no fisheye distortion.
```

---

### 📐 9 · DUTCH ANGLE

**GPT Image 2 — re-render with a tilted horizon**

```
Use image 1 as the base image and image 2 for her exact face. Keep the same subject — her exact face, hair, glasses, jewellery and wardrobe — and the same location, lighting and colour grade. Change only the camera position.

Scene lock: this is the same place as image 1, photographed from a different position. Everything visible in image 1 stays exactly as it is — the same setting, the same background, the same objects in the same positions and the same quantity. Nothing is added, nothing is removed, nothing is moved.

Pose lock: she sits on the second wooden step facing the yard, knees apart with her boots planted on the bottom step, elbows resting on her knees, forearms hanging loose, a chipped enamel mug in her right hand, shoulders relaxed and leaning slightly forward, looking straight into the lens.

Re-render as a dutch angle shot with a strongly tilted horizon, the entire frame rotated about twenty degrees so the steps, the porch rail, the roofline and every horizontal run as clear diagonals and the porch posts lean with them. Fill all four corners with continuous environment. She holds the identical pose and eyeline, tilted with the frame.

Constraints: she stays seated — no standing, no change of pose, no objects added or removed, no other people, no text, no captions, no watermark, no logos, no fisheye distortion.
```

---

## THREE RULES THAT MAKE IT WORK

1. **Never describe the pose vaguely.** "Bent over the pump" drifts. "Bent forward at the waist, left hand pushing the handle down, right hand steadying the bucket, back flat" holds.

2. **Say what stays before what changes.** The scene-lock paragraph is doing more work than the camera instruction — anchor the world first, move the camera last.

3. **The constraints list is not filler.** Every "no" in it is a mistake the model made on an earlier attempt — keep them, and add your own as you spot new drift.

---

## TIPS FOR BEST RESULTS

- **Build the hero first.** The Wide shot is the source of truth — get it clean before re-rendering, because every angle inherits it.

- **Keep a locked face reference.** Image 2 (her exact face) carries across all nine — a sharp, consistent face ref keeps identity from drifting.

- **Detail the pose like a physio.** Name every limb, hand, weight-shift and head direction — vague poses are where re-renders fall apart.

- **Grow the constraints list.** When a re-render adds a person, a logo or a tilted horizon, add that as a new "no" and re-run.

- **Swap the whole scenario.** The farm is just an example — drop in your subject, wardrobe and location and keep the five-part skeleton.

- **One camera move per prompt.** Each re-render changes only the camera — don't also change the pose or the scene, or it stops matching.

---

**Source:** aididthat.netlify.app  
**Platform:** GPT Image 2 · Picsart Flow
