# Living Room Paint-Roller Materialization Reveal

## Classification

**Product Category:** living-room interior

**Reveal Effect:** giant paint-roller spatial materialization

**Reveal Mechanism:** one realistic roller sweeps across surfaces and space, leaving completed finishes and furnishings directly behind its contact front

**Sequence Type:** reference-match tool-driven interior reveal

## Description of Resulting Video or Video Sequence

A giant realistic roller travels through an empty white room, applying final surfaces and revealing furniture, curtains, lighting, artwork, and decor wherever it passes.

## Usage

Use for renovation campaigns, paint and finish brands, interior-design reels, property makeovers, and playful tool-driven reveals.

## Engines/Models

Reference-aware video model with tool-path tracking, contact-front materialization, stable geometry, occlusion handling, and final-frame lock.

## Prerequisites / Dependencies

- Finished living room as `@reference`.
- Aligned empty white shell.
- One roller with a clear continuous route covering all final zones.

## Storyboard Requirement

Optional six-panel board: empty white room, floor pass, wall pass, furniture pass, details and roller exit, hero frame.

## Effect

### Effect Name: Spatial Paint-Roller Reveal

Only areas physically crossed by the roller become complete. The reveal front follows roller contact, leaves stable final geometry, and never paints over completed objects incorrectly.

## Video Prompt

```text
Use @reference as the final living room design target and final visual match. Create a 10-second interior transformation. Start with an empty white room. A giant realistic paint roller moves across the floor, walls, and through space. Wherever it passes, finished surfaces, furniture, curtains, lighting, artwork, and decor appear, resulting in the fully photorealistic living room matching @reference exactly. No people, no text, no logos, no cuts.

Use one continuous locked-camera take. 0.0-1.0s: hold the empty white shell. 1.0-3.0s: the roller crosses the floor, revealing exact flooring and rug behind its contact edge. 3.0-5.2s: it sweeps wall planes, applying final finishes, shelving, and artwork. 5.2-8.2s: controlled passes through space reveal sofa, chairs, tables, curtains, lamps, plants, and decor directly behind the roller. 8.2-9.0s: roller exits without touching finished objects. 9.0-10.0s: hold the final room.

Preserve camera, architecture, inventory, layout, materials, lighting, and @reference fidelity. No visible operator, random paint, splatter, roller clipping, geometry ahead of contact, duplicate objects, cuts, or unfinished final frame.
```

## Interior Reveal Checklist

- [ ] Opening room is empty, white, and reference-aligned.
- [ ] One roller follows a continuous readable path.
- [ ] Materialization occurs only behind roller contact.
- [ ] Floor, wall, and spatial passes remain distinct.
- [ ] Completed objects stay fixed and unpainted.
- [ ] Roller exits before the final hold.
- [ ] Camera, architecture, layout, and lighting remain stable.
- [ ] No people, text, logos, cuts, splatter, or duplicates appear.
- [ ] The 10-second final frame matches `@reference` exactly.
