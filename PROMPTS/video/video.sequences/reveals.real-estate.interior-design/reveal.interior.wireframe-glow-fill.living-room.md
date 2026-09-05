# Living Room Wireframe Glow-Fill Reveal

## Classification

**Product Category:** living-room interior
**Reveal Effect:** luminous wireframe material fill
**Reveal Mechanism:** glowing spatial outlines form in mid-air and fill continuously with their final real materials
**Sequence Type:** reference-match interior materialization reveal

## Description of Resulting Video or Video Sequence

A 10-second one-take reveal where thin glowing frames outline the sofa, table, rug, chairs, shelves, lights, curtains, plants, and decor in an empty shell before each volume fills with photoreal materials.

## Usage

For interior-design presentations, furniture campaigns, residential marketing, and room-transformation films.

## Engines/Models

Reference-aware video model with spatial line tracking, volumetric filling, material boundaries, object support, and final-frame lock.

## Prerequisites / Dependencies

- Finished living room as `@reference`.
- Optional aligned empty-shell first frame.

## Storyboard Requirement

Optional six-panel board: empty shell, primary outlines, complete wireframe room, material fill, finishing details, hero frame.

## Effect

### Effect Name: Wireframe Glow Fill

Each outline occupies one exact final volume; real material fills from its support surface inward and extinguishes the corresponding glow without changing object shape or location.

## Video Prompt

```text
Use @reference as the exact final living-room target. Create a 10-second one-take interior reveal from the exact final camera position with no cuts.

0.0-1.0s: Begin with the empty architectural shell, preserving the reference walls, windows, doors, ceiling, floor boundaries, perspective, and daylight.
1.0-3.8s: Thin elegant glowing frames draw the exact outlines of the rug, sofa, chairs, coffee table, side tables, shelves, lamps, curtains, plants, artwork, and decor in their final positions.
3.8-7.8s: Starting at each object's supported base, the frames fill continuously with reference-accurate wood, stone, glass, metal, fabric, foliage, and other real materials. Filled surfaces gain correct texture, weight, shadows, and reflections as their glow fades.
7.8-9.2s: Cushions soften, curtains hang naturally, rug fibers settle, lamps illuminate, and small decor resolves without moving the completed layout.
9.2-10.0s: Hold on the finished photorealistic room matching @reference exactly.

Preserve the camera, shell, openings, furniture inventory, scale, layout, lighting direction, and @reference fidelity. Keep wireframes spatially stable, fills bounded by their outlines, objects supported, and transformations continuous. No people, text, logos, cuts, floating outlines, neon residue, fill leakage, hollow objects, duplicate furniture, intersecting geometry, layout drift, camera movement, or unfinished final frame.
```

## Interior Reveal Checklist

- [ ] Empty shell and final camera align with the reference.
- [ ] Every major furnishing receives one exact spatial outline.
- [ ] Wireframes remain fixed in final positions.
- [ ] Materials fill from supported surfaces within clear boundaries.
- [ ] Glow disappears as each real material completes.
- [ ] Textiles, foliage, shadows, and reflections settle naturally.
- [ ] Room layout, scale, architecture, and lighting remain continuous.
- [ ] No people, text, logos, cuts, duplicates, or intersections appear.
- [ ] The 10-second final frame matches `@reference` exactly.
