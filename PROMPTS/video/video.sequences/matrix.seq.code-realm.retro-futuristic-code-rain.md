# The Code Realm - Retro-Futuristic Code Rain Sequence

## Classification

**Product Category:** Character-driven cinematic content

**Reveal Effect:** Retro-futuristic world integration

**Reveal Mechanism:** A separately generated character sheet and location plate are combined as locked reference elements, then animated through a constrained movement prompt

**Sequence Type:** Reference-match character animation workflow

**Filename:** `seq.code-realm.retro-futuristic-code-rain.md`

## Description of Resulting Video or Video Sequence

A 15-second, 16:9 retro-futuristic character film showing a lone figure walking away down a tree-lined avenue while luminous code falls in vertical columns. The camera remains locked as the coat and code rain move, preserving the supplied character and location designs without palette or identity drift.

## Usage

Perfect for creator identity films, retro-futuristic fashion pieces, cyber-noir brand visuals, profile introductions, and reference-consistency demonstrations. The workflow is especially useful when the character and environment must remain independently editable while sharing one visual language.

## Engines/Models

- **GPT Image:** Generate the character sheet and location plates.
- **Seedance 2.5:** Load the character and location as separate elements and animate the final shot.
- **Format:** Set 16:9 before generation.
- **Source workflow:** Tudor.ai, _The Code Realm: One Photo, Two Images, One Prompt_.

## Prerequisites / Dependencies

- **Dependency 1 - Source portrait:** A clean, front-facing photograph with even light, no sunglasses, and no heavy facial shadows.
- **Dependency 2 - Character sheet:** Front, three-quarter, profile, and back views on one board, plus a row of expression close-ups.
- **Dependency 3 - Location plate:** A tree-lined avenue with vertical code rain and a lit doorway at the end of the path, composed with room for the character.
- Load the character sheet as `@[character]` and the location plate as `@[location]` in separate Seedance element slots.
- Load the elements in the same order in which the prompt names them.

## Workflow

### 1. Take a Clean Portrait

Photograph the subject front-facing under even light. Avoid sunglasses and heavy shadows because every downstream image inherits the facial information in this source.

### 2. Generate the Character Sheet

Use the portrait in GPT Image to create a retro-futuristic character sheet. Include front, three-quarter, profile, and back full-body views plus expression close-ups. The back view is required; otherwise, the video model may invent it.

### 3. Customize the Outfit

Iterate on the same sheet until the silhouette is distinctive at a distance. Explicitly define the coat length and fall, shoulder line, collar, eyewear, hair mass, facial hair, scars or markings, and logo placement. Place a logo on a specific garment area such as the chest, shoulder, or back rather than treating it as a floating graphic.

### 4. Generate Location Plates

Create three or four environments in the same visual register as the character. Preserve rendering style, line treatment, finish, palette, time of day, light direction, and practical-light colors. Compose every plate with plausible open space for the figure.

### 5. Load Separate Elements

In Seedance 2.5, place the character sheet and location plate in separate element slots. Do not merge them into one reference image. The separation allows the character identity and background design to remain independently locked.

### 6. Configure the Generation

Set the aspect ratio to 16:9 before generating. Paste the movement prompt, then adjust only the action, pace, mood, and motion beats. Preserve the element names, design locks, camera instruction, and negative controls.

### 7. Generate and Review

Generate the shot and check character identity, outfit silhouette, palette, lighting, camera stability, code-rain direction, figure count, and unwanted text or redesigns.

## Character Sheet Prompt

This reusable GPT Image prompt is derived from the requirements in the supplied guide. Replace the bracketed fields while preserving the consistency locks.

```text
Using the attached front-facing portrait as the exact identity reference, create one complete retro-futuristic character sheet on a flat, visually consistent background.

Show the same adult character in every panel with identical facial identity, body proportions, hair mass, facial hair, eyewear, markings, outfit, palette, and rendering style.

BOARD LAYOUT
- Full-body front view
- Full-body three-quarter view
- Full-body side profile
- Full-body back view
- One row of head close-ups with varied natural expressions

CHARACTER DESIGN
Dress the character in a [COAT LENGTH] retro-futuristic coat with [COAT FALL AND MATERIAL], [SHOULDER LINE], and [COLLAR DESIGN]. Add [EYEWEAR SHAPE], [HAIRSTYLE AND HAIR MASS], [FACIAL HAIR], and [SCAR OR DISTINCTIVE MARKING]. Place [LOGO] physically on the [CHEST / SHOULDER / BACK] of the garment, following its folds and perspective.

VISUAL LANGUAGE
Use a restrained black, deep green, and luminous code-green palette with a graphic retro-futuristic finish. Keep the background flat and in the same visual register as the character. Preserve identical lighting, color treatment, garment construction, and details in every angle.

No missing back view, no duplicate angle, no identity drift, no changing facial structure, no changing eyewear, no changing hair or facial hair, no alternate outfit, no floating logo, no extra limbs, no cropped feet, no text labels, no watermark.
```

## Location Plate Prompt

This reusable GPT Image prompt is derived from the environment and location-building guidance in the supplied guide.

```text
Create a wide 16:9 retro-futuristic location plate for the supplied character design. Show a long tree-lined avenue at night, viewed along its central path, with luminous green code rain falling in straight vertical columns between the trees. A softly illuminated doorway stands at the far end of the avenue as the destination.

Match the character sheet's exact rendering language, line treatment, finish, black and deep-green palette, luminous code-green accents, time of day, and light direction. The code rain falls vertically at a constant density and rate. Trees, path, fallen leaves, benches, and distant architecture remain dark and legible without competing with the figure.

Leave a clear, naturally composed standing and walking area on the central avenue for one full-body character. Maintain depth along the path and enough negative space around the intended silhouette. Generate the environment without a person so it can be loaded separately in Seedance.

No character, no crowd, no second figure, no palette shift, no daylight, no diagonal rain, no random symbols on physical surfaces, no floating interface panels, no text overlay, no logo, no watermark.
```

## Video Prompt

**Duration:** 15 seconds

**Format:** 16:9 horizontal, configured before generation

**Style:** Retro-futuristic cyber-noir illustration or cinematic rendering matching the two supplied elements exactly

**Scene Setup/Context:** Use `@[character]` as the exact character identity and design reference. Use `@[location]` as the exact avenue, palette, lighting, composition, and code-rain reference. Both references remain independently locked.

### Original Movement Prompt

Preserved in full from the supplied guide:

```text
HE WALKS AWAY DOWN THE AVENUE AS THE CODE RAIN FALLS | LOCKED CAMERA, IT NEVER MOVES | THE COAT MOVES, HE DOES NOT LOOK BACK | THE RAIN FALLS IN VERTICAL COLUMNS AT A CONSTANT RATE | HOLD @[character] AND @[location] EXACTLY AS THEY ARE, NO REDESIGN, NO PALETTE SHIFT | NO MUSIC, NO TEXT, NO SECOND FIGURE
```

### Structured Generation Prompt

```text
Create a 15-second, 16:9 retro-futuristic cinematic shot using two separately loaded reference elements.

REFERENCE LOCK
Use @[character] as the exact identity, face, body proportions, hair, facial hair, eyewear, markings, coat silhouette, collar, garment details, logo placement, and palette reference. Use @[location] as the exact avenue, trees, path, code-rain design, illuminated doorway, lighting, depth, composition, and palette reference. Hold both elements exactly as supplied. Do not redesign, merge, restyle, recolor, or substitute either element.

ACTION
The character walks steadily away from the camera down the center of the avenue toward the illuminated doorway. He never turns, glances back, or reveals a new outfit angle inconsistent with @[character]. His stride is controlled and natural. The long coat responds with restrained, physically believable movement around his legs and settles between steps.

CAMERA
The camera is completely locked. It never pans, tilts, dollies, zooms, reframes, tracks, shakes, or changes focal length. Preserve the original horizon, perspective, crop, and vanishing point from @[location] for the entire shot.

ENVIRONMENTAL MOTION
The luminous code rain falls in straight vertical columns at a constant direction, density, brightness, and speed. It does not swirl, blow sideways, pulse, accelerate, form shapes, or attach itself to the character. The trees, avenue, benches, ground, and distant doorway remain structurally fixed.

LIGHTING AND PALETTE
Preserve the exact black, deep-green, and luminous code-green palette from the references. Keep the original light direction and practical glow unchanged. The moving character receives lighting consistent with @[location], with no color clash or exposure shift.

AUDIO
No music. Use only restrained environmental ambience if audio is generated.

NEGATIVE
No second figure, crowd, duplicate character, face redesign, identity drift, changing eyewear, changing hair, changing facial hair, changing coat length, changing collar, changing logo, outfit mutation, palette shift, lighting shift, camera movement, pan, tilt, dolly, zoom, tracking, reframing, handheld shake, diagonal code rain, fluctuating rain speed, morphing trees, moving architecture, new props, looking back, turning toward camera, text, subtitles, captions, interface graphics, watermark, or music.
```

## What to Preserve and What to Change

| Preserve                                       | Adapt                                           |
| ---------------------------------------------- | ----------------------------------------------- |
| `@[character]` and `@[location]` element names | Character action                                |
| Character and environment design locks         | Pace                                            |
| Locked-camera instruction                      | Mood                                            |
| Palette and lighting continuity                | Specific performance beats                      |
| Negative controls                              | Location variation, if regenerated consistently |

## Quality Checklist

- [ ] The source portrait is front-facing, evenly lit, and unobstructed.
- [ ] The character sheet includes front, three-quarter, profile, back, and expression views.
- [ ] Face, eyewear, hair, facial hair, coat, collar, markings, and logo remain identical across the sheet.
- [ ] Character and location use the same palette, lighting logic, rendering, line, and finish.
- [ ] The location plate leaves usable room for the figure.
- [ ] `@[character]` and `@[location]` are loaded in separate slots and in prompt order.
- [ ] The aspect ratio is set to 16:9 before generation.
- [ ] The camera remains completely locked.
- [ ] The character walks away and never looks back.
- [ ] The coat moves naturally without changing design.
- [ ] Code rain remains vertical and falls at a constant rate.
- [ ] No second figure, redesign, palette shift, text, watermark, or music appears.

## Source

Adapted from Tudor.ai, _The Code Realm: One Photo, Two Images, One Prompt_ workflow guide. The original movement prompt is preserved verbatim; the reusable character-sheet, location, and structured-generation prompts were expanded from the guide's stated requirements.
