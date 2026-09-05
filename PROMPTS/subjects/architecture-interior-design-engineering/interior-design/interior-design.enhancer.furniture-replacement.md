# Interior Design Enhancer - Furniture Replacement

## Description

Replace the furniture in a base interior with furniture supplied by a second reference while preserving the room architecture, layout logic, camera, lighting, and spatial relationships. This enhancer supports product visualization, furniture selection, and controlled before-and-after comparisons.

## Best For

- Furniture-shopping visualization
- Product-placement testing
- Client furniture selection
- Before-and-after comparisons using specific products

## Prerequisites

- **Image 1:** Base interior scene and source of truth for architecture, camera, layout, and lighting
- **Image 2:** Furniture reference and source of truth for furniture design, materials, colors, and proportions

## Original Prompt

```text
In image 1 replace all the furniture with the furniture shown on image 2.
```

## Production-Ready Prompt

```text
In Image 1, replace all existing furniture with the furniture shown in Image 2. Use Image 1 as the exact source of truth for the room architecture, dimensions, floor plan, camera position, lens perspective, windows, doors, fixed fixtures, lighting direction, and circulation. Use Image 2 only as the source of truth for the replacement furniture's design, geometry, materials, colors, upholstery, and detailing.

Place each replacement item in the corresponding functional position with realistic scale, orientation, floor contact, spacing, and clearance. Adapt only the furniture arrangement as needed to fit the existing room safely and naturally without changing the architecture. Match Image 1's lighting, shadows, reflections, depth of field, and color environment so every replacement appears genuinely photographed in the room.
```

## Preservation Rules

- Image 1 controls architecture, camera, room geometry, fixed elements, and light.
- Image 2 controls furniture appearance only; do not import its room or background.
- Preserve circulation paths, functional clearances, realistic scale, and floor contact.
- Do not retain ghosted remnants of the original furniture.

## Negative Prompt

```text
changed architecture, changed room dimensions, imported background from Image 2, mixed rooms, moved windows, moved doors, altered fixed fixtures, wrong furniture design, wrong upholstery, duplicate furniture, original furniture ghost, floating furniture, sunk furniture, incorrect scale, blocked circulation, mismatched perspective, mismatched light, impossible shadows, warped legs, merged objects, text, logo, watermark
```

## Quality Checklist

- [ ] Image 1 architecture, camera, fixed fixtures, and lighting remain unchanged.
- [ ] Replacement furniture accurately matches Image 2.
- [ ] Original furniture is fully removed without ghosts or remnants.
- [ ] Scale, orientation, spacing, floor contact, and circulation are plausible.
- [ ] Shadows, reflections, perspective, and color belong naturally to Image 1.
- [ ] No duplicate, floating, warped, merged, or unrelated furniture appears.

## Source

Extracted from [Interior Design Quick Reference Prompts](interior-quick-reference-prompts.md), prompt 3.
