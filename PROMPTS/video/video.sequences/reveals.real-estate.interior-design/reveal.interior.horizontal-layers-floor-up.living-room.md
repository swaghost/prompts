# Living Room Horizontal Layers Floor-Up Reveal

## Classification

**Product Category:** living-room interior
**Reveal Effect:** stacked horizontal layer assembly
**Reveal Mechanism:** ordered horizontal layers rise from floor level and lock before the next furnishing layer appears
**Sequence Type:** reference-match interior build reveal

## Description of Resulting Video or Video Sequence

A 10-second one-take reveal where clean layers establish floor, rug, furniture bases, cushions, tables, shelves, decor, curtains, and lights in strict bottom-up order.

## Usage

For interior-design breakdowns, furniture systems, residential marketing, and architectural visualization.

## Engines/Models

Reference-aware video model with planar reveal masks, ordered object assembly, support validation, material continuity, and final-frame lock.

## Prerequisites / Dependencies

- Finished living room as `@reference`.
- Optional aligned empty-shell first frame.

## Storyboard Requirement

Optional six-panel board: empty shell and floor layer, rug, furniture bases, cushions and tables, shelves and upper details, hero frame.

## Effect

### Effect Name: Floor-Up Horizontal Layer Stack

Each thin horizontal band resolves all geometry at its height, locks completely, and becomes the stable support for the next band without slicing or moving completed objects.

## Video Prompt

```text
Use @reference as the exact final living-room target. Create a 10-second one-take floor-up reveal from the exact final camera position with no cuts.

0.0-1.0s: Begin with the aligned empty architectural shell and a clean horizontal guide at floor level.
1.0-2.2s: The first layer establishes final flooring and baseboards; the second lays the full rug flat in its exact @reference footprint.
2.2-4.2s: Successive low layers lock sofa and chair bases, table legs, shelf plinths, and planter bases onto the floor before building upward.
4.2-6.4s: Middle layers complete upholstery frames, cushions, tabletops, side tables, cabinets, and lower shelving with exact materials and contact shadows.
6.4-8.5s: Upper layers resolve shelf contents, lamps, plants, artwork, curtain rails, and curtains; every hanging item connects to its real support.
8.5-9.4s: The final thin layer completes light fixtures and upper decor, then all guide lines disappear and practical lights activate.
9.4-10.0s: Hold on the complete photorealistic room matching @reference exactly.

Preserve camera, shell, openings, furniture inventory, scale, layout, materials, and @reference fidelity. Keep layers level, ordered, non-overlapping, and fully locked before advancement; completed geometry must remain whole and supported. No people, text, logos, cuts, visible slicing of finished objects, skipped layers, floating upper parts, duplicate furnishings, moving completed layers, guide residue, camera drift, or unfinished final frame.
```

## Interior Reveal Checklist

- [ ] Empty shell and floor guide align exactly to the reference.
- [ ] Flooring completes before the rug and furniture bases.
- [ ] Every horizontal layer locks before the next begins.
- [ ] Lower geometry supports all later upper geometry.
- [ ] Completed objects remain whole and stationary.
- [ ] Curtains, artwork, plants, and lights connect to valid supports.
- [ ] Camera, shell, layout, materials, and lighting remain continuous.
- [ ] No people, text, logos, cuts, skipped layers, or floating parts appear.
- [ ] The 10-second final frame matches `@reference` exactly.
