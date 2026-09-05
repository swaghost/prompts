# Luxury Property White Curtain Lift Reveal

## Classification

**Product Category:** luxury-property exterior
**Reveal Effect:** architectural curtain unveiling
**Reveal Mechanism:** a large white fabric cover lifts while architecture finishes beneath its retreating edge
**Sequence Type:** reference-match exterior reveal

## Description of Resulting Video or Video Sequence

A 10-second continuous luxury presentation where an elegant white curtain lifts from the property silhouette as facade, glazing, pool, and landscape finish in real time.

## Usage

For launch films, listing reveals, architecture presentations, hospitality openings, and ceremonial unveilings.

## Engines/Models

Reference-aware video model with cloth simulation, occlusion continuity, and architectural final-frame matching.

## Prerequisites / Dependencies

- Completed exterior photo as `@reference`.
- Optional site plate matching its camera and environment.

## Storyboard Requirement

Optional four-panel board: covered silhouette, initial lift, progressive completion, clear final property.

## Effect

### Effect Name: White Curtain Lift

The cloth behaves as one continuous textile with gravity, tension, folds, and wind response. Completion follows the visible retreating edge and never changes geometry behind it.

## Video Prompt

```text
Use @reference as the final exterior design target and exact final visual match. Create a 10-second continuous luxury property reveal with no cuts.

0.0-1.2s: Start on the site with a giant elegant white curtain draped over the complete property-shaped volume. Camera and context align with @reference.
1.2-4.5s: The curtain lifts and pulls upward and away smoothly. Fabric gathers, folds, stretches under realistic tension, and clears architectural edges without clipping.
2.0-7.5s: Directly behind the retreating curtain edge, the property finishes forming in real time: facade materials resolve, windows become clear and reflective, roof and trims complete, and no unfinished zone is exposed prematurely.
6.0-8.8s: Pool water fills, landscaping grows, driveway and pathways settle, and exterior lights activate in completed areas.
8.8-10.0s: The curtain exits completely and the camera holds or gently pushes toward the fully photorealistic property matching @reference.

Luxury presentation style, warm natural light, realistic cloth weight, contact, shadows, and reflections. No people, text, logos, cuts, hidden cuts, fabric passing through architecture, duplicated cloth, unexplained wind, incomplete surfaces, architecture mismatch, or final curtain remnants.
```

## Exterior Reveal Checklist

- [ ] Curtain initially conforms to one plausible property volume.
- [ ] Cloth motion has gravity, tension, folds, and clean edge interaction.
- [ ] Completion follows the retreating fabric edge.
- [ ] No unfinished area is exposed before its reveal.
- [ ] Pool, landscape, and lights complete after the main facade.
- [ ] Curtain fully exits the final frame.
- [ ] Completed property matches `@reference` in one 10-second shot.
