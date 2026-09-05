# Self-Build Interior Design Reveal - Surface Emergence

## Classification

**Category:** Interior-design animation / luxury real estate

**Reveal Effect:** Furniture and decor emerge directly from walls, floor, and ceiling

**Reveal Mechanism:** Surface-anchored growth and extension into the exact final layout

**Sequence Type:** Single-reference empty-shell to furnished-interior transformation

## Description of Resulting Video

A bare architectural shell transforms into the exact finished interior shown in `@reference`. Furniture does not fly into the room or appear through cuts. Each object grows from the surface that physically supports it: the sofa pushes outward from a wall, tables rise from the floor, shelving extends from wall planes, pendant lights descend from ceiling points, curtains flow down beside windows, and plants grow from their final planters. Every element settles into the precise final position, scale, orientation, material, and color shown in the reference.

## Usage

Use for interior-design presentations, luxury-property reveals, furniture campaigns, design-before-and-after reels, architectural visualization, client approvals, room-styling demonstrations, and single-reference image-to-video generation.

## Engines And Models

Suitable for Seedance 2/2.5, Veo, Kling, Runway, Sora, or another reference-aware image-to-video model capable of preserving architecture and resolving a precise final frame.

## Prerequisites And Reference Lock

- Upload one high-resolution image of the completed interior as `@reference`.
- Use `@reference` as a design and final-frame reference, not as the opening frame.
- The reference defines the exact room geometry, camera, furniture, decor, materials, lighting, landscaping or exterior view, and final composition.
- If the model requires a start frame, first generate a matching empty-shell plate with the same camera, crop, architecture, lighting, and window view.

`@reference` is the sole source of truth for:

- Camera position, height, angle, lens, framing, crop, and perspective
- Walls, floor, ceiling, columns, windows, doors, and built-in architecture
- Sofa, chairs, tables, shelving, rugs, curtains, lights, plants, artwork, and decor
- Object count, dimensions, position, rotation, spacing, materials, and colors
- Natural and artificial lighting, shadows, reflections, exposure, and grade
- Exterior scenery visible through windows

Do not invent, remove, duplicate, restyle, or relocate any final object.

## Empty-Shell Opening State

At frame one, show the same room as `@reference` but stripped to its permanent architectural shell:

- Preserve walls, floors, ceiling, columns, windows, doors, stairs, built-in recesses, and permanent glazing.
- Preserve the exact camera and all vanishing points.
- Preserve window views, daylight direction, and permanent architectural shadows.
- Remove loose furniture, rugs, curtains, pendant fixtures, movable shelving, plants, artwork, accessories, and decor.
- Keep every final attachment point and floor position empty until its assigned emergence beat.

## Surface-Origin Rules

Every element must originate from the surface that supports or anchors it:

| Element                         | Required origin and motion                                                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sofa and upholstered seating    | Push outward from the nearest supporting wall or rise a short distance from the exact floor footprint; gain full depth without sliding across the room. |
| Coffee, side, and dining tables | Rise vertically from their final floor positions; legs and top resolve coherently as one stable object.                                                 |
| Shelving and wall cabinetry     | Extend horizontally from their final wall planes; brackets and supports remain attached to the wall.                                                    |
| Pendant lights                  | Descend vertically from exact ceiling connection points; cables and fixtures extend to final length and settle with one damped sway.                    |
| Curtains                        | Unroll or flow downward from installed tracks beside the correct windows; fabric gathers and settles under gravity.                                     |
| Rugs                            | Unroll or spread outward from the correct floor center, then flatten with realistic textile behavior.                                                   |
| Plants                          | Emerge from final planters after the pots resolve; stems, branches, and leaves grow naturally without changing species.                                 |
| Artwork and mirrors             | Extend from or resolve against their exact wall locations; remain flush and correctly scaled.                                                           |
| Small decor                     | Resolve last at exact support points with no floating or random scattering.                                                                             |

Objects may emerge smoothly, but they must never travel long distances, cross through one another, or detach from their logical support surfaces.

## Technical Specifications

- **Duration:** 10 seconds
- **Aspect Ratio:** Match `@reference`
- **Camera:** Locked or an extremely subtle luxury push/glide that preserves the final composition
- **Take Structure:** One continuous take
- **Transformation:** Smooth sequential surface emergence
- **Lighting:** Match `@reference`; maintain direction and color throughout
- **Final Hold:** At least 1.5 seconds on the exact completed interior
- **Rendering:** Ultra-realistic premium architectural visualization
- **People:** None
- **Text and Branding:** None unless physically present in `@reference`

## Beat-by-Beat Timeline

### 0:00-0:01.5 - Empty Architectural Shell

Establish the completely empty room from the reference camera. Hold long enough to read the floor, walls, ceiling, windows, and spatial proportions. No furniture silhouettes, ghost objects, outlines, or premature decor are visible.

### 0:01.5-0:04 - Primary Furniture Emergence

The sofa pushes smoothly outward from its supporting wall or rises directly from its exact floor footprint. Its frame, upholstery, cushions, seams, and legs gain full realistic volume without stretching or changing design.

Primary tables rise vertically from their final positions. Keep each object separate, fully proportioned, and grounded with contact shadows as soon as it touches the floor.

### 0:04-0:06 - Storage And Lighting

Shelving and wall-mounted cabinetry extend outward from their exact wall planes. Preserve alignment, dimensions, joinery, finishes, and spacing from `@reference`.

Pendant lights descend from their exact ceiling points. Cords or rods lengthen cleanly, fixtures stop at the final height, and one small physically damped sway settles. Lights switch on only if illuminated in the final reference.

### 0:06-0:08.5 - Textiles, Curtains, And Plants

Curtains flow down beside the correct windows from their installed tracks, forming natural pleats and reaching the exact final length. Rugs spread or unroll across their final floor footprints and flatten naturally.

Planters resolve in place. Plants grow into their final species, height, density, leaf direction, and silhouette. Add artwork, mirrors, cushions, and secondary furniture only where shown in `@reference`.

### 0:08.5-0:10 - Detail Completion And Hero Hold

Small accessories resolve at their exact support locations. Contact shadows, reflections, fabric folds, glass response, and material detail finalize. All movement stops.

Settle into the exact completed layout and final composition of `@reference`. Hold the photorealistic luxury interior with no further additions or repositioning.

## Master Video Prompt

```text
Use @reference as the exact final interior target and sole design authority. It defines the final camera position, angle, lens, framing, room architecture, furniture inventory, object count, layout, spacing, orientation, dimensions, materials, colors, lighting, shadows, reflections, window view, and color grade. The final frame must match @reference exactly.

Create a 10-second, one-take, ultra-realistic luxury interior-design reveal. Begin with the same room as a completely empty architectural shell from the same camera direction and perspective. Preserve all permanent architecture: walls, floor, ceiling, columns, windows, doors, recesses, and exterior view. At the opening, remove all loose furniture, rugs, curtains, hanging lights, movable shelving, plants, artwork, and decor. Do not show ghost furniture, outlines, or completed objects early.

Furniture and decor must emerge directly from their logical supporting surfaces. Nothing flies in from offscreen and nothing appears through cuts.

0:00-0:01.5: show the empty architectural shell, unchanged and fully readable.

0:01.5-0:04: the sofa pushes smoothly outward from its supporting wall or rises only from its exact final floor footprint. It gains full depth, upholstery, cushions, seams, legs, and reference-matched materials without stretching, sliding, or changing shape. Tables rise vertically from their exact floor positions and settle with correct contact shadows.

0:04-0:06: shelving and wall cabinetry extend outward from their exact wall planes with correct supports, dimensions, spacing, and material finishes. Pendant lights descend from exact ceiling connection points. Their cords or rods extend to the final length, fixtures settle with one subtle damped sway, and illuminated fixtures switch on only as shown in @reference.

0:06-0:08.5: curtains flow downward from tracks beside the correct windows, forming realistic pleats and final fabric length. Rugs spread or unroll across their exact floor footprints. Planters resolve in final positions and plants grow naturally to the exact species, height, density, direction, and silhouette shown in @reference. Artwork, mirrors, cushions, secondary furniture, and decor appear only in their exact final locations.

0:08.5-0:10: small accessories complete the arrangement. Finalize contact shadows, reflections, glass, fabric folds, wood grain, stone, metal, and upholstery. Stop all object movement and hold the exact completed interior for the final 1.5 seconds.

Use a locked camera or an extremely subtle premium push/glide that never changes perspective or prevents the final frame from matching @reference. Keep light direction, exposure, white balance, shadow geometry, and color grade stable. No people, no text, no logos, no cuts.

Every final element must already exist in @reference. Do not add, duplicate, substitute, redesign, restyle, recolor, resize, or relocate anything. The final frame contains exactly the same interior as @reference, nothing more and nothing less.
```

## Camera And Lighting

- Keep the camera locked when exact overlay accuracy is critical.
- If movement is used, limit it to a subtle straight push or short luxury glide.
- No orbit, crane, pan, tilt, whip, zoom, or perspective reset.
- Maintain the reference focal length and vanishing points.
- Preserve daylight direction and practical-light placement.
- Lights may activate during their emergence but cannot alter overall exposure abruptly.
- Maintain realistic shadows under every newly grounded object.

## Transformation Physics And Continuity

- Each object begins only at its final support surface.
- Architecture never bends, breathes, warps, or redraws.
- Furniture gains depth without morphing into another design.
- Completed objects remain fixed after settling.
- No two solid objects intersect.
- Heavy objects settle faster and with less bounce than textiles.
- Curtains and rugs use cloth behavior; shelving and furniture use rigid-body behavior.
- Plant growth follows stems and branches rather than ballooning uniformly.
- Contact shadows and reflections appear coherently with object emergence.
- The final inventory equals the reference inventory exactly.

## Customization Fields

- `[ROOM_TYPE]`
- `[PRIMARY_SOFA_OR_SEATING]`
- `[PRIMARY_TABLES]`
- `[SHELVING_OR_CABINETRY]`
- `[PENDANT_LIGHTS]`
- `[CURTAIN_STYLE]`
- `[RUG_STYLE]`
- `[PLANT_SPECIES]`
- `[ARTWORK_AND_DECOR]`
- `[CAMERA_BEHAVIOR]`
- `[DURATION]`
- `[FINAL_HOLD_DURATION]`

## Negative Prompt

```text
people, humans, hands, text, captions, logo, watermark, cut, hidden cut, jump edit, scene change, time jump, camera reset, new camera angle, orbit, crane, whip pan, zoom, perspective change, changing vanishing points, changing room dimensions, moving walls, bending ceiling, warped windows, altered architecture, imported furniture, invented furniture, extra sofa, duplicate tables, extra plants, random decor, changed object count, changed layout, changed materials, changed colors, changed lighting, object flying from offscreen, long travel paths, furniture sliding across floor, random floating objects, ghost furniture, semi-transparent objects, cross-fade, image blend, whole-room morph, melting furniture, rubber furniture, stretched sofa, malformed table legs, shelves detached from wall, pendant lights disconnected from ceiling, curtains emerging from wrong wall, curtains clipping through windows, rugs floating, plants ballooning, incorrect plant species, objects intersecting, missing contact shadows, reflection mismatch, lighting flicker, exposure pumping, final frame mismatch
```

## Quality Checklist

- [ ] `@reference` is used as the exact final target.
- [ ] Opening camera, architecture, and window view match the reference.
- [ ] Opening frame contains only the empty permanent shell.
- [ ] Sofa emerges from its supporting wall or exact floor footprint.
- [ ] Tables rise from exact final positions.
- [ ] Shelving remains attached to its correct wall.
- [ ] Pendant lights descend from exact ceiling points.
- [ ] Curtains emerge beside the correct windows.
- [ ] Rugs settle with believable cloth physics.
- [ ] Plants match reference species, scale, and location.
- [ ] No object travels across the room.
- [ ] No object is invented, duplicated, recolored, or restyled.
- [ ] Completed objects remain fixed after arrival.
- [ ] Architecture and perspective remain stable.
- [ ] Lighting and shadows remain coherent.
- [ ] Final inventory and layout exactly match `@reference`.
- [ ] Final frame holds for at least 1.5 seconds.
- [ ] No people, text, logos, watermarks, or cuts appear.

## Related Prompts

- [AI Furniture Reveal for Real Estate and Interior Visualizations](../../../video/video.sequences/reveals.real-estate.interior-design/reveal.interior-design.autonomous-assembly.real-estate-interiors.md)
- [Interior Wave Assembly](../interior-design/reveal.interior-design.interior-wave-assembly.md)
- [Magic Box Interior Transformation](reveal.interior-design.magic-box-interior-transformation.md)
