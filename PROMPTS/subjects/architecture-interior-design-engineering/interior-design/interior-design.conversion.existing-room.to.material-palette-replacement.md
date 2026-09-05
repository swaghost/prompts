# Existing Room to Material Palette Replacement

## Conversion

- **Source type:** Existing furnished room image
- **Target type:** Photorealistic finish and material replacement

## Description

Replace only visible room finishes with a coordinated wood, stone, fabric, and metal palette while locking architecture, furniture placement, lighting, and camera.

## Usage

Use for finish studies, client material options, renovation visualization, interior styling, value engineering, and palette comparison.

## Prerequisites

- One clear room reference image
- Selected `(STYLE)`, `(WOOD)`, `(STONE)`, `(FABRIC)`, and `(METAL)`
- Visible floors, walls, ceilings, furniture, and material boundaries

## Preservation Rules

- Preserve geometry, openings, furniture positions, object count, lighting, camera angle, crop, and proportions.
- Modify finishes only; do not redesign architecture or furniture.
- Keep material scale, joints, transitions, reflections, and wear physically plausible.

## Complete Prompt

```text
Replace only the visible finishes in this room with a sophisticated (STYLE) material palette. Use (WOOD), (STONE), (FABRIC) and (METAL) in realistic proportions. Preserve architecture, furniture positions, lighting and camera angle. Create physically accurate textures, scale, reflections and material transitions. Photorealistic.
```

## Variable Examples

- **`(STYLE)`:** Modern minimalist, rustic farmhouse, industrial chic, coastal luxury, contemporary warm, traditional elegant, Scandinavian natural, Mediterranean villa, Japanese zen, Art Deco glamour
- **`(WOOD)`:** White oak, walnut, teak, ash, cherry, maple, reclaimed pine, ebony, bamboo, cedar
- **`(STONE)`:** Carrara marble, Calacatta marble, granite, travertine, limestone, slate, quartzite, terrazzo, concrete, basalt
- **`(FABRIC)`:** Linen, velvet, leather, wool boucle, silk, cotton canvas, mohair, cashmere, jute, hemp
- **`(METAL)`:** Brushed brass, matte-black steel, chrome, aged bronze, copper, nickel, gunmetal, rose gold, stainless steel, oxidized iron

## Example

```text
Replace only the visible finishes in this room with a sophisticated contemporary warm material palette. Use white oak, travertine, linen and brushed brass in realistic proportions. Preserve architecture, furniture positions, lighting and camera angle. Create physically accurate textures, scale, reflections and material transitions. Photorealistic.
```

## Negative Prompt

```text
changed architecture, moved furniture, removed furniture, added furniture, changed camera, changed lighting direction, invented window, altered opening, incorrect material scale, stretched wood grain, impossible stone veining, floating texture, abrupt transition, fake reflection, plastic fabric, oversaturation, low detail, illustration, watermark, logo
```

## Quality Checklist

- [ ] All five variables are replaced.
- [ ] Architecture and furniture placement remain unchanged.
- [ ] Only visible finishes are modified.
- [ ] Texture scale and orientation are realistic.
- [ ] Material joints, edges, reflections, and transitions are coherent.
- [ ] Camera, lighting, and composition match the source.

## Source

Extracted from [Interior Design AI Prompt Collection - Professional Architectural Visualization](interior-design-ai-prompt-collection.md), Prompt 03.