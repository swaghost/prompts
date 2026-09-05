# Living Room Flat-Panel Folding Reveal

## Classification

**Product Category:** living-room interior

**Reveal Effect:** flat-panel folding assembly

**Reveal Mechanism:** planar pieces hinge, fold, and lock into furniture and wall structures before receiving final materials

**Sequence Type:** reference-match origami-mechanical interior reveal

## Description of Resulting Video or Video Sequence

Flat panels on floors and walls fold into sofa, tables, shelving, wall details, and lighting structures, then gain realistic wood, fabric, metal, glass, and decor.

## Usage

Use for modular interiors, flat-pack furniture campaigns, joinery systems, product launches, and engineered room transformations.

## Engines/Models

Reference-aware video model with hinge motion, rigid panel geometry, mechanical locking, material conversion, and final-frame lock.

## Prerequisites / Dependencies

- Finished living room as `@reference`.
- Aligned shell with staged panels at final zones.
- Defined panel-to-object assignments and hinge axes.

## Storyboard Requirement

Optional six-panel board: flat panels, first hinges, furniture frames, complete folded geometry, material finish, hero frame.

## Effect

### Effect Name: Flat-Panel Folding Assembly

Each rigid panel rotates around one plausible hinge, locks without bending, and contributes to one final object before material finish hides construction seams.

## Video Prompt

```text
Use @reference as the final living room design target and final visual match. Start with flat panels lying across the floor and leaning against the walls. The panels fold and lock together to form the sofa, coffee table, side tables, shelving, wall details, and lighting structure. Real wood, fabric, metal, glass, and decor then appear, completing the photorealistic living room matching @reference exactly. No people, no text, no logos, no cuts.

Create one continuous 10-second locked-camera reveal. 0.0-1.2s: show separate flat panels assigned to exact final zones. 1.2-5.8s: panels hinge in a logical support-first order, forming shelving, tables, seating frames, wall details, and lighting structures. 5.8-7.4s: panels lock into precise final geometry; upholstery and soft components form around supported frames. 7.4-9.0s: real materials, glass, decor, curtains, plants, shadows, and reflections finish. 9.0-10.0s: hold the room.

Preserve camera, architecture, inventory, layout, proportions, materials, lighting, and @reference fidelity. No flexible panels, impossible hinges, intersections, flying parts, origami residue, duplicate furniture, cuts, or unfinished final frame.
```

## Interior Reveal Checklist

- [ ] Panels begin separate and assigned to final zones.
- [ ] Every fold uses a plausible hinge axis.
- [ ] Support frames assemble before loads and soft finishes.
- [ ] Panels remain rigid and collision-free.
- [ ] Final geometry matches reference silhouettes.
- [ ] Seams and flat-pack residue disappear.
- [ ] Camera, architecture, layout, and lighting remain stable.
- [ ] No people, text, logos, cuts, intersections, or duplicates appear.
- [ ] The 10-second final frame matches `@reference` exactly.
