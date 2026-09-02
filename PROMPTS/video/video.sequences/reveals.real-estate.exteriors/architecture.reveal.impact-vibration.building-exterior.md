# Architecture Exterior Reveal - Impact Vibration Building Assembly

## Description of Resulting Video or Video Sequence

An 8-second photorealistic exterior architectural reveal that reconstructs a primary building or structure from an empty version of its exact reference scene. Structural sections arrive as complete, rigid components through physically grounded pop-in, drop, descend, and instant movements, with subtle 1-2 frame impact vibrations on landing. The camera remains locked with only a restrained drift, ending on a static frame that matches the supplied finished reference exactly.

## Usage

Perfect for architecture firms, real-estate developers, construction companies, facade manufacturers, landmark presentations, hospitality launches, and property marketing. Use it to create repeatable empty-site-to-finished-building reveals while preserving the surrounding environment, foreground objects, lighting, camera perspective, and architectural proportions.

## Engines/Models

The source document recommends Google Flow at [flow.google](https://flow.google/). The prompt is suitable for image-to-video models that accept one finished exterior reference and can animate a generated empty-state version, including Seedance, Kling, Runway, Veo, Sora, or comparable tools.

## Prerequisites / Dependencies

- **Dependency 1 - Required exterior reference:** One high-resolution finished exterior image showing the complete main building or structure.
- **Dependency 2 - Required empty-state image:** An empty-site version generated from the exact exterior reference, with the primary building removed and the environment preserved.
- **Dependency 3 - Recommended storyboard reference:** An 8-panel storyboard or shot map showing the empty state, base assembly, middle tiers, top details, and final hold.
- Keep both image states at the exact same resolution, aspect ratio, crop, camera position, camera height, focal length, field of view, horizon, and perspective.
- Preserve every non-primary object visible in the finished reference: sky, clouds, ground, water, foliage, distant scenery, surrounding structures, and foreground objects.

## Reference Preparation Workflow

### Finished Reference

Use the finished exterior image as the final state at approximately 6 seconds. It defines the exact primary building design, object inventory, proportions, position, orientation, materials, colours, reflections, and final lighting.

### Empty-State Reference

Create an empty-site version of the same image by removing only the primary building or structure. Leave the sky, clouds, ground, water, foliage, distant scenery, surrounding smaller structures, foreground objects, lighting, crop, and perspective unchanged. Replace the building footprint with matching cleared ground and open background.

### Alignment Check

Before video generation, compare the two states for identical pixel dimensions, crop, horizon, vanishing points, ground edges, background boundaries, and camera perspective. If any of these differ, regenerate the empty state from the original finished reference.

## Storyboard Requirement

The storyboard is recommended and should be treated as required for complex buildings, multi-tier structures, repetitive facades, lattices, spires, or scenes with important foreground occlusion. Use one 8-panel storyboard image as a camera and timing map, not as separate shots to edit together. Every panel must show the same exterior viewpoint, building geometry, environment, and object inventory.

### Storyboard Notes

**Panel 1 (0:00-0:02):** Empty-state exterior. Show all environmental and foreground elements already present, with bare cleared ground where the primary building will sit. Keep the camera framing, horizon, lighting, and negative space identical to the finished reference.

**Panel 2 (0:02-0:03):** Base structures arrive. Show foundations, podiums, heaviest lower body, and lowest structural sections appearing from above or below with full opacity and a subtle landing vibration.

**Panel 3 (0:03-0:03.7):** Lower-to-middle assembly. Show the next structural tier arriving in the correct position while the surrounding environment remains unchanged.

**Panel 4 (0:03.7-0:04.4):** Main body assembly. Show the shaft, walls, columns, domes, or central body locking into place with realistic weight and contact shadows.

**Panel 5 (0:04.4-0:05):** Upper sections arrive. Show upper floors, roof, crown, or major facade sections assembling from above or below without morphing or gradual growth.

**Panel 6 (0:05-0:05.5):** Fine structural completion. Show repeated patterns, lattice, texture, thin vertical elements, and facade details arriving already complete and rigid.

**Panel 7 (0:05.5-0:06):** Final accents and lighting. Show spires, finials, top accents, surface lighting, reflections, and contact shadows settling with the final micro-vibration.

**Panel 8 (0:06-0:08):** Finished reference hold. Show the completed primary building exactly matching the finished reference. Stop all assembly and vibration; retain only subtle natural environmental motion already present.

**Storyboard Style:** Photorealistic architectural visualization, identical reference framing, natural lighting, stable exterior environment, complete rigid structural sections, subtle physical impact feedback, clear construction order, and final-frame fidelity.

## Effect

### Effect Name: Discrete Architectural Assembly with Impact Vibration

**Purpose:** Make heavy architectural sections feel physically grounded, massive, and mechanically placed rather than digitally morphed onto a scene.

**Trigger:** Each complete structural section triggers a brief 1-2 frame micro-camera contact rattle at the exact moment it lands or snaps into position.

**Visual Behaviour:** Structural sections arrive in short, controlled movements from above or below. Each section is fully opaque, complete, rigid, and correctly proportioned from its first visible frame. Contact shadows and the micro-vibration occur simultaneously, then the section settles immediately.

**Motion Rules:**

- **POP-IN:** Heaviest foundations, podiums, lowest body, and base structures appear directly or rise/drop into final position.
- **DROP / DESCEND:** Middle tiers, main shaft, body, columns, walls, domes, and roofs lower from above or rise from below.
- **INSTANT:** Top accents, crowns, spires, finials, upper details, and surface lighting appear as complete rigid pieces with a sharp micro-shake.
- Repeating lattice, facade patterns, textures, and thin vertical elements arrive as complete rigid sections; they never build cell by cell, scramble, bend, lean, curve, or wobble.

**Effect Negative Controls:** No morphing, cross-fading, gradual scaling, ghosting, translucent sections, random particles, long flight paths, spinning parts, elastic wobble, melting, stretching, bending towers, premature reflections, or foreground occlusion.

## Video Prompt

```
Static architectural reveal, 8 seconds. Locked-off camera. The only camera movement allowed is a subtle continuous drift of a few degrees that eases to a stop at 6s, small enough that the composition stays recognisably the same shot from start to finish. No dolly, no zoom, no whip pan.

CAMERA LOCK - ANGLE AND PERSPECTIVE NEVER CHANGE: The camera position, height, angle, focal length, field of view, and perspective are exactly those of the reference image and stay fixed for the entire 8 seconds. All vanishing points, horizon lines, ground edges, and background boundaries remain in the same directions throughout. Do not reframe, re-angle, re-render, or re-photograph the scene from a different viewpoint. Do not change lens compression or widen the view. Do not reveal any part of the scene not visible in the reference image. The composition at every frame must overlay onto the reference image with the main subject in the same place.

HOW TO USE THE REFERENCE IMAGE - READ CAREFULLY: The reference image is the FULLY BUILT final state at 6s. Begin the video from an empty-site version of this exact same scene at 0s: keep every background and environment element exactly as it appears in the reference image - same sky, same clouds, same ground, same water, same distant scenery, same surrounding smaller structures, same foreground objects, same lighting - but with the MAIN SUBJECT, the primary building or structure, completely absent, leaving only bare cleared ground and open background where it will sit. From that empty state, the structural sections of the main subject from the reference image are placed onto the scene one group at a time until the frame equals the reference image exactly. These are two discrete states, NOT two ends of a blend. Do not cross-fade, morph, or gradually transform the empty frame into the built frame. Do not compute intermediate frames by mixing the two states together. At every moment the frame shows the empty scene plus whichever sections have already arrived, never a partial blend or a translucent ghost.

STRICT OBJECT INVENTORY - NOTHING NEW: The complete and final set of objects is defined entirely by the reference image. Every object that appears must already be visible in the reference image, in the same position, at the same scale, in the same orientation, in the same material, colour, and finish. Do not add, invent, substitute, duplicate, restyle, or embellish anything. Do not add extra buildings, extra towers, extra structures, extra trees, or extra props beyond exactly what the reference image shows. If an object is absent from the reference image, it must never appear at any point in the video. The final frame must contain exactly the same object count as the reference image, nothing more, nothing less.

ABSOLUTE LOCK: All environment - sky, clouds, ground, water, foliage, distant scenery, surrounding structures, foreground objects, and lighting direction - is present from 0s and must stay identical for the entire 8 seconds, never redrawn, warped, shifted, or reinterpreted. Any element that sits in front of the main subject in the reference image, including foreground trees, hedges, walls, or objects, always stays in front of it, never behind, and is never covered by arriving sections. No reflection of the main subject appears in any water or glass until the corresponding section has physically arrived.

REVEAL METHOD - FLEXIBLE DIRECTION & IMPACT VIBRATION: Structural sections arrive in groups using flexible top-down or bottom-up assembly movements. Every section is fully opaque, complete, and correctly proportioned from the first frame it is visible. A section either does not exist yet or exists fully. Any repeating pattern, lattice, texture, or facade arrives already complete and rigid on its section - never built up cell by cell, never scrambled, never growing. Any thin vertical element, including a spire, mast, minaret, antenna, or column, arrives as a single straight rigid piece, never bending, leaning, curving, or wobbling. Upon the exact frame each section lands or snaps into place, apply a very subtle, brief micro-vibration impact shake lasting 1-2 frames to make the heavy physical arrival feel realistic, grounded, and massive.

POP-IN - the heaviest base structures, foundations, podiums, and lowest body: appears directly or rises/drops into place with a subtle micro-vibration impact shake upon contact, then settles immediately.

DROP / DESCEND - the middle tiers, main shaft or body, columns, walls, domes, and roofs: lowers from above or rises from below and lands with a firm settle accompanied by a slight impact vibration.

INSTANT - the top accents, crowns, spires, finials, upper details, and any surface lighting: appear in place as complete rigid pieces with a sharp micro-shake frame effect on arrival.

Each arrival takes about 0.2 to 0.3 seconds. Sections travel short distances. Contact shadows and micro-impact vibrations trigger simultaneously on landing.

TIMELINE:
0-2s: The frame is the empty scene - all background, environment, and foreground present and unchanged, with bare ground where the main subject will sit. Camera begins its slow drift.

2-3.5s: The base structures and foundations arrive from above/below, landing with a subtle ground-impact vibration effect. Everything else in the frame is unchanged.

3.5-5s: The middle tiers, main body, and upper sections arrive from above/below, each triggering a brief micro-vibration shake as they lock into position.

5-6s: The top accents, spires, and fine details SETTLE with a final subtle micro-shake; all contact shadows land; all vibrations cease and the camera drift eases to a stop. The frame now equals the reference image exactly.

6-8s: The frame is exactly the reference image, completely static, no new objects, no repositioning, no further changes or vibrations. Stable ambient light with only subtle natural motion already present in the scene, such as drifting clouds, water shimmer, or a gentle breeze.

Photorealistic architectural photography, natural lighting matching the reference image.
```

## Camera

- Locked-off camera with only a subtle drift of a few degrees that eases to a stop at 6 seconds.
- Fixed camera position, height, angle, focal length, field of view, lens compression, horizon, and perspective.
- No dolly, zoom, whip pan, orbit, arc shot, crane move, or reframing.
- Maintain foreground occlusion and reference-matched composition throughout.

## Lighting

- Match the reference image's natural lighting direction, colour, intensity, and shadow behaviour.
- Keep all environmental lighting present from the first frame and unchanged during assembly.
- Create contact shadows when sections arrive.
- Do not show reflections of the main subject before the corresponding section physically exists.

## Visual Effects and Technical Details

- Discrete fully opaque structural arrival, never a blend between empty and finished states.
- Short travel paths with realistic mass, contact, and settling.
- 1-2 frame micro-vibration on every section landing or snap.
- Complete rigid repeated patterns, lattices, textures, and thin vertical elements.
- Preserve all non-primary environmental and foreground objects exactly.
- Final frame must match the finished reference object-for-object.

## Quality and Technical Requirements

- **Duration:** 8 seconds
- **Format:** Match the reference image's aspect ratio
- **Rendering:** Photorealistic architectural photography
- **Motion:** Controlled discrete assembly, realistic physical weight
- **Camera:** Locked-off with subtle drift, no perspective changes
- **Reference:** Finished reference plus pixel-aligned empty-site state
- **Final frame:** Exact finished-reference match at 6 seconds, held through 8 seconds
- **Quality:** Stable geometry, natural lighting, accurate materials, no artifacts

## Negative Prompt

```
changing camera angle, changing perspective, new viewpoint, reframing, re-angling, rotating camera, orbiting, arc shot, crane move, changing camera height, changing focal length, changing field of view, lens distortion, wide angle shift, perspective warp, shifting vanishing point, tilting horizon, revealing unseen areas of the scene, added buildings, added towers, extra structures, invented objects, new decor, additional props, extra trees, duplicated objects, restyled architecture, changed colour, changed material, changed lattice pattern, morphing pattern, objects not present in the reference, interpolation between states, blending two images, image morph, cross-fade between frames, gradual transformation, morphing, object morphing, shape shifting, transforming, geometry changing, slow growth, growing from zero, unfolding, assembling from parts, dissolving in, fade in, fade out, cross dissolve, opacity transition, ghosting, double exposure, translucent objects, glowing particles, light shimmer, warping, melting, stretching, squashing, elastic wobble, bending tower, leaning tower, curved spire, wobbling spire, foreground covered, premature reflection, excessive camera shake, violent vibration, objects flying across frame, long travel paths, spinning objects, sliding along the floor, floating objects, people, birds, text, watermark, changing architecture, redrawn scene, altered lighting direction, distorted subject, objects appearing after 6s, camera push in, dolly, zoom, whip pan
```

## Repeatability Checklist

- [ ] Finished reference is high resolution and clearly shows the complete primary structure.
- [ ] Empty-site state was generated directly from the finished reference.
- [ ] Both states have identical dimensions, crop, camera, horizon, and perspective.
- [ ] Only the primary building or structure was removed from the empty state.
- [ ] Environment and foreground objects remain unchanged and in front where applicable.
- [ ] Storyboard is attached for complex architecture and covers the full 8 seconds.
- [ ] Structural sections are assigned POP-IN, DROP/DESCEND, or INSTANT motion.
- [ ] Repeated patterns and thin vertical elements are specified as rigid and complete.
- [ ] Impact vibration is subtle, synchronized, and limited to 1-2 frames.
- [ ] No new reflections appear before the corresponding structure arrives.
- [ ] Generation uses the exact prompt and negative prompt without omitted sections.
- [ ] Final frame matches the finished reference exactly and holds from 6-8 seconds.

## File-Naming

`ARCHITECTURE.REVEAL.[EFFECT].[SETTING].md`
