# Living Room Horizontal Curtain-Sweep Reveal

## Classification

**Product Category:** living-room interior
**Reveal Effect:** giant-curtain horizontal unveiling
**Reveal Mechanism:** one elegant curtain sweeps left to right and exposes the completed interior directly behind its moving edge
**Sequence Type:** reference-match interior unveiling

## Description of Resulting Video or Video Sequence

A 10-second one-take reveal where a giant curtain travels left to right across an empty room, revealing finished flooring, walls, furniture, textiles, lights, art, plants, and decor behind it.

## Usage

For luxury interior launches, furniture collections, residential marketing, and design presentations.

## Engines/Models

Reference-aware video model with cloth simulation, horizontal tension, progressive occlusion, surface collision, and final-frame lock.

## Prerequisites / Dependencies

- Finished living room as `@reference`.
- Optional aligned empty-room plate.

## Storyboard Requirement

Optional six-panel board: empty room, curtain entry, left-side reveal, center crossing, right-side clearance, hero frame.

## Effect

### Effect Name: Horizontal Curtain Sweep

One continuous curtain remains vertically hung and laterally tensioned as its trailing edge exposes a fully finished, spatially stable room without touching or dragging the revealed objects.

## Video Prompt

```text
Use @reference as the exact final living-room target. Create a 10-second one-take unveiling from the exact final camera position with no cuts.

0.0-1.0s: Begin on the aligned empty room shell as one floor-to-ceiling elegant curtain enters from the left, spanning the visible depth without hiding the camera.
1.0-7.8s: The curtain sweeps steadily from left to right. Directly behind its trailing edge, flooring and wall finishes, then rug, sofa, chairs, tables, shelves, curtains, lamps, artwork, plants, and decor are revealed already complete in their exact @reference positions.
7.8-9.2s: The cloth clears the right edge of frame with believable folds, weight, and airflow; nothing in the completed room moves or follows it.
9.2-10.0s: Practical lights settle to their final level and the unobstructed photorealistic room holds, matching @reference exactly.

Preserve camera, shell, openings, layout, object inventory, scale, materials, and @reference fidelity. Maintain one continuous left-to-right reveal boundary, correct cloth topology, collisions, shadows, and occlusion. No people, text, logos, cuts, extra curtains, tearing, snagging, cloth passing through furniture, premature revealed objects, re-covering, object drag, camera drift, or fabric remaining in the final frame.
```

## Interior Reveal Checklist

- [ ] Empty shell and final camera align exactly.
- [ ] One floor-to-ceiling curtain sweeps left to right.
- [ ] A single trailing edge controls the reveal.
- [ ] Cloth folds, tension, airflow, and collisions remain plausible.
- [ ] Revealed furnishings are complete and spatially fixed.
- [ ] The curtain exits fully before the final hold.
- [ ] Architecture, layout, materials, and lighting remain continuous.
- [ ] No people, text, logos, cuts, snagging, or object drag appears.
- [ ] The 10-second final frame matches `@reference` exactly.
