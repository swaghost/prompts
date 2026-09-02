# Invideo Agent Two - Full-Movie Prompt Workflow

## Description of Resulting Video or Video Sequence

A director-led workflow for producing a complete short film inside Invideo Agent Two from a natural-language brief. The agent coordinates character consistency sheets, location references, generated stills, video clips, B-roll, sound, and iterative edits in one project. The workflow is demonstrated with a roughly 45-second tropical beach-cabana short film and an 8-second first-person laptop-error sequence.

## Classification

**Product Category:** Full-movie / short-film production workflow

**Reveal Effect:** Agent-orchestrated multi-asset cinematic assembly

**Reveal Mechanism:** Natural-language direction expanded into consistent image, video, B-roll, and edit assets

**Sequence Type:** Full-movie prompt workflow

**Filename:** `seq.invideo-agent-two-full-movie-workflow.md`

## Usage

Use this workflow when a film needs multiple consistent characters, locations, props, shots, B-roll clips, and edits without manually generating every asset in separate tools. It is suited to short narrative films, lifestyle commercials, branded stories, cinematic social videos, and POV sequences that require an agent to maintain continuity while the director iterates conversationally.

## Engines/Models

- **Invideo Agent Two:** project orchestration, asset generation, editing, and iteration
- **GPT Image 2:** high-quality character sheets, location images, stills, and design references
- **Seedance 2.5:** generated video clips and cinematic motion
- **Optional manual mode:** generate individual assets directly inside the same Invideo project while preserving the project asset context

## Prerequisites / Dependencies

- A short film brief with approximate total duration, genre, characters, location, action, tone, and aspect ratio
- Character reference images or enough text detail for the agent to create character consistency sheets
- Location, prop, interface, or wardrobe references where continuity matters
- Desired image-generation model and quality/resolution settings
- Desired video-generation model and clip settings
- A project in Invideo Agent Two where generated assets can remain available for later shots and edits

## Core Full-Movie Prompt

Paste this into Invideo Agent Two and customize the bracketed fields:

```text
I want to generate a short film, approximately [TOTAL DURATION] seconds in total. Use the provided character images and references to generate character consistency sheets for [CHARACTER NAMES OR ROLES]. Generate a complete visual plan for the film before producing the final clips.

The film genre and tone are [GENRE, TONE, AND EMOTIONAL ARC]. The primary location is [LOCATION]. The characters begin in [OPENING STATE] and the story progresses through [KEY STORY BEATS] before ending with [ENDING STATE]. The visual style is [VISUAL STYLE, CAMERA LANGUAGE, LIGHTING, COLOR GRADE, AND ASPECT RATIO].

Create and use character sheets for every recurring character. Lock identity, age, facial structure, hair, wardrobe, body proportions, accessories, and performance continuity across every shot. Create or use a location reference that locks the architecture, geography, time of day, weather, lighting direction, materials, and palette. Create prop and interface references wherever the story depends on recognizable objects, packaging, screens, signage, or repeated details.

Use GPT Image 2 on high quality at [RESOLUTION] for image generation and Seedance 2.5 for video generation. Keep all generated assets inside this project so they can be reused as references. Produce a shot list with durations, camera position, subject blocking, action, transitions, sound, and the reference assets used for each shot. Generate the hero frames first, then the video clips, then the B-roll and assembly edit.

The film should feel directed rather than randomly assembled. Preserve spatial continuity, character identity, wardrobe, prop placement, light direction, and motivated camera movement. Use natural performance and realistic physical motion. Avoid generic stock footage, disconnected locations, identity drift, random wardrobe changes, impossible object continuity, unmotivated camera movement, garbled text, watermarks, and accidental logos.

After the first assembly, review the result as a director. Identify continuity errors, weak transitions, incorrect assets, and missing B-roll. Regenerate or replace only the affected assets while keeping the established references. Finish with a coherent edit, consistent color and sound, and an export-ready version in [FINAL FORMAT].
```

## Director Setup Instructions

1. Start a new Invideo Agent Two project and provide the short-film brief.
2. Attach relevant character, location, wardrobe, prop, and interface references.
3. Tell the agent which references are identity locks, environmental locks, or design references.
4. Set GPT Image 2 to high quality and the requested resolution for image generation.
5. Set Seedance 2.5 for video generation and define the project's aspect ratio.
6. Ask the agent to generate consistency sheets before generating the shot sequence.
7. Ask for hero stills and keyframes before requesting motion clips.
8. Review the first assembly conversationally and request targeted replacements or additional B-roll.

## Worked Example - Tropical Beach Cabana Short Film

### Initial Brief

```text
I want to generate a short film, approximately 45 seconds in total. Use the provided character images to generate character consistency sheets for the male and female characters. Generate a pixelated character of the blonde curly-haired man.

The location is a tropical beachfront, and they are both seated on sunbeds in the shade. Build a cinematic short film around their interaction, maintaining character, wardrobe, environment, lighting, and prop continuity across every shot. Use GPT Image 2 on high quality at 2K resolution for all image generation and Seedance 2.5 for videos. Keep the project's aspect ratio consistent across all assets.
```

### Reference Map

- **Image 1 - Original still:** beach cabana daybed, palm line, blown-out turquoise shallows, linen shirt and shorts, woven side table, iced drink, and child's crayon drawing. The blond curly-haired man becomes the POV camera; only hands, forearms, and legs are visible.
- **Image 2 - Female character sheet:** adult woman, approximately 5'7", dark hair pulled back with damp strands at the temples, sun-flushed cheeks, white open-weave crochet cover-up worn off-shoulder over a navy patterned bikini. Use this to lock identity, wardrobe, and proportions.
- **Image 3 - Laptop wallpaper reference:** wide green rolling hill under blue sky with scattered clouds, early-2000s desktop aesthetic.
- **Image 4 - Error dialog design reference:** retro operating-system modal with blue gradient title bar, minimise/maximise/close controls, red circular X icon, short body text, one grey action button, and drop shadow.

## Worked Sequence - Tropical Laptop Error Cascade

**Duration:** 8 seconds

**Format:** First-person POV with shallow depth of field and natural handheld micro-drift

**Persistent frame element:** The woman remains at frame-left, reclined on the daybed from 0:00 to approximately 0:06.8, lower than the man's eyeline, softly out of focus and never the focal plane. She moves naturally with a slow breath, a small weight shift, and one curious turn toward the screen.

### Master Sequence Prompt

```text
Create an 8-second continuous first-person POV sequence in the tropical beach cabana using the supplied reference map. The blond curly-haired man is the camera operator and is never seen except for his hands, forearms, and legs. Preserve the female character sheet, beach cabana location, daybed, palm line, turquoise shallows, linen wardrobe, woven side table, iced drink, laptop wallpaper, and retro error-dialog design exactly. Use natural outdoor light, shallow depth of field, realistic phone capture, motivated handheld micro-drift, and no disconnected edits.

0:00-0:01.0 - GLANCE, RETURN, COLLAPSE SETUP. Open looking down at roughly 40-45 degrees. The man's bare legs in pale linen shorts fill the bottom third. A silver open laptop rests angled across the left thigh and shows the green rolling-hill wallpaper. The left hand is at the trackpad edge. The right hand holds a child's crayon drawing in the upper-middle: pink wavy border and a stick figure in a yellow straw hat. The woman is present from the first frame at frame-left, reclined and softly out of focus, looking toward the water. Camera is locked to the operator's head with 1-2 degrees of organic breathing sway; it is not stabilised. Focus is on the paper while the keyboard, table, iced glass, and woman remain in gentle bokeh. Palms and bright shallows are blown out at the top of frame. Hold roughly one second with no lingering.

0:01.0-0:02.2 - TILT AND SET DOWN. The right wrist rotates the drawing approximately 15-20 degrees clockwise. A broad sheet of sunlight rolls left to right across the paper, hot-clipping the white page and making the yellow crayon glow. The POV rotates 8-12 degrees, slightly less than the paper, so the drawing continues to read as moving within frame. The woman shifts slightly up and right through parallax rather than independent movement. The hand lowers the drawing onto the woven side table beside the sweating glass and flattens it with a fingertip press. Camera tracks down and right with a combined 10-15 degree tilt-and-pan, decelerates with a 2-3 degree overshoot, then settles level. Use directional motion blur on the moving hand and forearm only. The woman remains soft and stable.

0:02.2-0:03.2 - BACK TO THE SCREEN. Camera swings back left and up in a smooth reverse arc, slightly faster than the descent, settling with the laptop centred low in frame. The screen is readable as an older daylight display: milky blacks, slightly washed contrast, faint blue-grey viewing-angle shift across the upper third, diffuse glare sheet over the top edge, low-amplitude refresh shimmer, and subtle pixel-grid texture at close range. Keep the green hill wallpaper identifiable. Hot midday exterior light still governs the shot. The left hand makes a short scroll and a single tap on the trackpad. Focus racks onto the laptop panel; the woman falls further into softness.

0:03.2-0:06.0 - ERROR CASCADE. On the tap, one retro OS-style error dialog appears instantly, fully formed and dead centre on the screen: blue gradient title bar, red circular X, short body text, one grey button lower-right, and soft drop shadow. No fade, scale-in, or motion. A second dialog appears after a beat, then a third at offset positions. Around 0:04.5, the woman turns her head toward the screen in one slow curious movement but stays out of focus and does not speak or reach in. From 0:04.2 to 0:06.0, dialogs appear in rapid succession and then in pairs, scattered at varied positions and sizes, some clipped at screen edges and some nearly flush on top of one another. Approximately ten identical dialogs bury the wallpaper. The camera makes a small involuntary 2-3 percent recoil around 0:04.5, then leans in again; this is body movement, not a zoom. Hand motion becomes faster and less precise with aborted gestures and repeated taps. Screen glare remains constant and the dialogs stay legible.

0:06.0-0:08.0 - HEAD DOWN. Both forearms leave the laptop and fold onto the daybed cushion. The woven table and drawing pass briefly through the lower frame. Hands settle one over the other, palms down, forming a resting shelf. The body leans forward and the forehead rests on the backs of the hands in one continuous exhausted slump. This is not a hand raised to cover the face. Camera descends and pitches forward with the head, travelling roughly 25-35 cm down and forward over about one second, decelerating into a soft contact settle against skin and cushion. No bounce. The woman sweeps up and out of the top-left as the frame drops; the last visible edge is a blurred suggestion of crochet sleeve and shoulder against bright sand. Hands, forearms, and cushion fill the frame as large soft warm shapes. Light falls off as the eyeline seals against the arms. Reach full black by roughly 0:07.2, hold black for the final 0.8 seconds with only faint residual breathing movement. Hard out, no recovery.

Maintain continuous spatial logic. All acceleration comes from event cadence, not playback speed. Keep the woman peripheral and defocused. Preserve the external tropical light so the scene never becomes an indoor shot. No generic B-roll, no new character, no additional interface design, no camera teleportation, no random cutaways.
```

## Effects Inventory

### Camera Movement

- First-person POV throughout; the operator appears only through hands, forearms, and legs.
- Natural handheld micro-drift of 1-2 degrees, increasing slightly during the cascade.
- Object-led camera coupling while the drawing rotates.
- Descending pan-tilt with 2-3 degree overshoot during set-down.
- Reverse arc return to the laptop, faster than the descent.
- Small 2-3 percent POV micro-recoil during the error cascade.
- Forward-and-down POV descent of 25-35 cm into the resting hands.

### Screen and Interface

- Aged-LCD behavior: milky blacks, washed contrast, blue-grey viewing shift, refresh shimmer, pixel-grid texture, and diffuse glare.
- Instant-appearance UI stacking with zero animation.
- Accelerating event cadence from roughly one-second spacing to near-simultaneous pairs.
- Layered dialog drop shadows onto the wallpaper and other dialogs.

### Optical and Physical Effects

- Shallow depth of field with subject-plane focus.
- Rack focus from foreground drawing to laptop and screen.
- Sunlight specular roll across the paper.
- Blown-out sky and shallows as fixed exterior anchors.
- Warm bounce spill from the woman's crochet cover-up and skin.
- Selective directional motion blur on hand and forearm only.
- Defocus collapse and occlusion falloff to black at the end.

## Effects Density Map

- **0:00-0:01.0:** Low density - POV, shallow depth, micro-drift, peripheral subject.
- **0:01.0-0:02.2:** Medium density - wrist coupling, rotation, specular roll, pan-tilt, overshoot, blur, parallax.
- **0:02.2-0:03.2:** Medium density - reverse arc, rack focus, aged-LCD treatment, glare, trackpad movement.
- **0:03.2-0:06.0:** High density - instant dialog stacking, accelerating cadence, shadow layering, recoil, peripheral reaction, imprecise hand motion.
- **0:06.0-0:08.0:** Low density - forward-down descent, contact settle, parallax, defocus, and black occlusion.

## Audio Direction

Use diegetic sound only: outdoor room tone, light water and palm ambience, paper movement, fingertip contact on woven table, trackpad taps, subtle laptop handling, quiet interface clicks if physically motivated, and the soft contact of forehead against hands and cushion. Do not use music or a generic soundtrack.

## Negative Prompt

```text
identity drift, changing character, changing wardrobe, changing location, disconnected shots, random B-roll, camera teleportation, stabilised floating camera, unmotivated zoom, interface redesign, animated dialog movement, fade-in dialogs, generic stock footage, indoor lighting, artificial studio light, plastic skin, perfect retouching, unreadable screen, garbled interface, extra characters, extra limbs, visible camera operator face, watermark, logo, subtitles, music, soundtrack
```

## Quality and Continuity Checklist

- [ ] Total film duration and aspect ratio are established before generation.
- [ ] Every recurring character has a consistency sheet.
- [ ] The location plate locks light, weather, architecture, and geography.
- [ ] Props, screens, logos, packaging, and interfaces have explicit references.
- [ ] GPT Image 2 and Seedance 2.5 settings are defined before asset generation.
- [ ] Hero stills are approved before motion clips are generated.
- [ ] Camera movement is motivated by subject or object action.
- [ ] Character, wardrobe, props, and lighting remain consistent across shots.
- [ ] B-roll supports the story instead of hiding continuity problems.
- [ ] Audio is built from diegetic textures unless the project explicitly requires music.
- [ ] The first edit is reviewed conversationally and only weak assets are replaced.
- [ ] Final export is checked for unwanted text, watermarks, crop changes, and continuity errors.

## Source Note

Adapted from the supplied Craft guide, `Invideo Agent Two`, which describes agent-orchestrated image, video, B-roll, multi-agent, and project-asset workflows.
