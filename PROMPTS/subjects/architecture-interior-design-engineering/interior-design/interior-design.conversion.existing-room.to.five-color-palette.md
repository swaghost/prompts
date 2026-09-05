# Existing Room to Five-Color Palette

## Conversion

- **Source type:** Existing room image and style or mood brief
- **Target type:** Applied five-color interior palette with HEX codes

## Description

Generate and visualize a harmonious five-color palette using a 60/30/10 distribution while preserving the source architecture and objects.

## Usage

Use for color consulting, concept development, client palette options, styling, staging, renovation studies, and mood alignment.

## Prerequisites

- One room reference image
- Selected `(ROOM)` and `(STYLE OR MOOD)`
- Existing materials, daylight direction, and room size visible or documented

## Preservation Rules

- Preserve architecture, openings, object inventory, furniture placement, camera, and lighting direction.
- Apply color changes only to plausible finishes, furniture, textiles, and decor.
- Keep HEX codes consistent with the visualized colors.

## Complete Prompt

```text
Generate a harmonious five-color palette for this (ROOM), inspired by (STYLE OR MOOD). Consider the existing materials, natural light and room size. Define 60% dominant, 30% secondary and 10% accent colors. Apply the palette realistically while preserving all architecture and objects. Include the five HEX codes.
```

## Distribution

- **60% dominant:** Walls, largest surfaces, and background
- **30% secondary:** Furniture, larger decor, and optional accent wall
- **10% accents:** Three smaller colors distributed approximately 5%, 3%, and 2%

## Example

```text
Generate a harmonious five-color palette for this bedroom, inspired by Scandinavian serenity. Consider the existing materials, natural light and room size. Define 60% dominant, 30% secondary and 10% accent colors. Apply the palette realistically while preserving all architecture and objects. Include the five HEX codes.
```

## Required Output Format

- Dominant (60%): `[NAME]` `#[HEX]`
- Secondary (30%): `[NAME]` `#[HEX]`
- Accent 1 (5%): `[NAME]` `#[HEX]`
- Accent 2 (3%): `[NAME]` `#[HEX]`
- Accent 3 (2%): `[NAME]` `#[HEX]`

## Negative Prompt

```text
changed architecture, moved objects, removed furniture, added furniture, changed camera, changed lighting direction, incoherent palette, more or fewer than five colors, missing HEX codes, mismatched HEX values, oversaturation, muddy colors, equal color distribution, unrealistic paint boundaries, floating color overlays, text clutter, watermark, logo
```

## Quality Checklist

- [ ] Room and style or mood variables are replaced.
- [ ] Exactly five named colors and HEX codes are supplied.
- [ ] Palette follows 60/30/10 distribution.
- [ ] Existing materials and natural light inform color selection.
- [ ] Architecture and objects remain unchanged.
- [ ] Applied colors match the listed HEX values closely.

## Source

Extracted from [Interior Design AI Prompt Collection - Professional Architectural Visualization](interior-design-ai-prompt-collection.md), Prompt 05.