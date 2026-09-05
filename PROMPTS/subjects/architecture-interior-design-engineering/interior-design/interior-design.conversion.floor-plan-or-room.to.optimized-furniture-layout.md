# Floor Plan or Room to Optimized Furniture Layout

## Conversion

- **Source type:** Floor plan or existing-room reference
- **Target type:** Optimized top-down furniture layout

## Description

Analyze a floor plan or room and produce a practical furniture plan for a specified number of users while preserving structural and service constraints.

## Usage

Use for residential space planning, office layouts, client options, renovation planning, circulation studies, and furniture-placement reviews.

## Prerequisites

- A legible floor plan or room reference
- User count `(NUMBER)`
- Known dimensions or scale where available
- Existing doors, windows, plumbing points, and structural walls identified

## Preservation Rules

- Preserve doors, windows, plumbing, structural walls, fixed openings, and room boundaries.
- Keep access routes and door swings unobstructed.
- Mark inferred measurements as approximate rather than factual.

## Complete Prompt

```text
Analyze this floor plan or room and propose an optimized furniture layout for (NUMBER) users. Preserve doors, windows, plumbing points and structural walls. Ensure comfortable circulation, functional zones, ergonomic distances and visual balance. Show the result as a clean top-down layout with clear furniture placement and approximate measurements.
```

## Variables and Planning Rules

- **`(NUMBER)`:** 1, 2, 3, 4, 5-6, 8-10, or 12+ users
- **Walkways:** At least 90 cm / 36 in where applicable
- **Dining allowance:** Approximately 60 cm per person
- **TV distance:** Approximately 2-3 times the screen diagonal
- **Zones:** Conversation, dining, work, relaxation, storage, or circulation as appropriate

## Example

```text
Analyze this floor plan or room and propose an optimized furniture layout for 4 users. Preserve doors, windows, plumbing points and structural walls. Ensure comfortable circulation, functional zones, ergonomic distances and visual balance. Show the result as a clean top-down layout with clear furniture placement and approximate measurements.
```

## Negative Prompt

```text
moved walls, altered openings, blocked doors, blocked windows, relocated plumbing, invented room, distorted plan, impossible scale, oversized furniture, undersized furniture, blocked circulation, overlapping furniture, floating furniture, missing labels, false precise measurements, perspective view, illegible layout, watermark, logo
```

## Quality Checklist

- [ ] User-count variable is replaced.
- [ ] Structural walls, openings, and plumbing remain fixed.
- [ ] Furniture scale is realistic.
- [ ] Circulation and door swings remain clear.
- [ ] Functional zones are legible and balanced.
- [ ] Measurements are included and identified as approximate.

## Source

Extracted from [Interior Design AI Prompt Collection - Professional Architectural Visualization](interior-design-ai-prompt-collection.md), Prompt 02.