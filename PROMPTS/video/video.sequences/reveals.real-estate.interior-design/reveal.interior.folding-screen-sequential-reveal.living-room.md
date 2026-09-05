# Living Room Folding-Screen Sequential Reveal

## Classification

**Product Category:** living-room interior

**Reveal Effect:** sequential folding-screen uncover

**Reveal Mechanism:** tall screens open from left to right, exposing successive fixed sections of the completed room

**Sequence Type:** reference-match occlusion reveal

## Description of Resulting Video or Video Sequence

A row of tall folding screens hides the interior and opens panel by panel from left to right, revealing the exact finished living room in coherent spatial sections.

## Usage

Use for elegant property openings, furniture collections, theatrical interiors, hospitality reveals, and sequential spatial presentations.

## Engines/Models

Reference-aware video model with hinged screen motion, stable hidden scene, correct occlusion, sequential timing, and final-frame lock.

## Prerequisites / Dependencies

- Finished living room as `@reference` behind the screens.
- Screen row sized to hide the whole room at frame one.
- Clear left-to-right hinge order and exit positions.

## Storyboard Requirement

Optional six-panel board: fully closed screens, first opening, sofa reveal, central reveal, final section and screen exit, hero frame.

## Effect

### Effect Name: Folding-Screen Sequential Reveal

Screens operate as temporary occluders only. The completed room remains geometrically stable behind them while each hinged section opens once and leaves the frame cleanly.

## Video Prompt

```text
Use @reference as the final living room design target and final visual match. Start with the entire room hidden behind a row of tall folding screens. The screens open one by one from left to right. Behind each opened section, more of the final completed living room is revealed: sofa area, rug, coffee table, lounge chairs, shelves, curtains, and decor. End with the full photorealistic room matching @reference exactly. No people, no text, no logos, no cuts.

Create one continuous 10-second locked-camera reveal. 0.0-1.0s: closed screens fully cover the room. 1.0-7.8s: screen sections hinge open sequentially from left to right, revealing exact fixed zones of the completed room with correct parallax and no object movement behind them. 7.8-9.0s: final screen clears the composition and all hinges settle outside the hero view. 9.0-10.0s: hold the unobstructed final interior.

Preserve camera, completed room geometry, inventory, layout, materials, lighting, and @reference fidelity behind the screens. No room assembly, changing hidden objects, screen transparency, wrong reveal order, screen collision, leftover occlusion, cuts, or unfinished final frame.
```

## Interior Reveal Checklist

- [ ] Closed screens cover the complete opening frame.
- [ ] Screens open one by one from left to right.
- [ ] Each screen uses plausible hinge motion.
- [ ] Revealed room sections are already final and stable.
- [ ] Occlusion and parallax remain physically correct.
- [ ] Screens clear the hero composition before final hold.
- [ ] Camera, room, layout, materials, and lighting remain stable.
- [ ] No people, text, logos, cuts, collisions, or residual screens obscure the room.
- [ ] The 10-second final frame matches `@reference` exactly.
