# Cohesive 3x3 Interior Camera-View Contact Sheet

## Description

Create one cinematic architectural contact sheet containing nine camera views of the same physical interior. The uploaded image remains the only source of truth: architecture, furniture, decor, materials, colors, proportions, and lighting stay fixed while only camera position, angle, focal length, and framing change.

## Usage

Use this board for interior-design presentations, architectural visualization reviews, camera-coverage planning, portfolio sheets, and consistency studies. It works best with a clear wide reference image that reveals the room's principal architecture and furniture relationships.

## Source

[Cohesive 3x3 cinematic architectural contact sheet](https://docs.google.com/document/d/1MDmsDfwEJnA66ZCUjKQpwP90H-I1uw3RGuJEjFQdNA4/mobilebasic?urp=gmail_link)

## Prerequisites

- One uploaded interior image
- Sufficient visible geometry for physically plausible alternate viewpoints
- An image model capable of reference-guided multi-panel generation

## Image Prompt

```text
Use the uploaded image as the ONLY source of truth and reference. Analyze the exact existing interior architecture, spatial layout, furniture arrangement, materials, colors, proportions, lighting design, wall treatment, curtains, sofa, coffee table, ottoman, artwork, pendant lights, plants, flooring, and all visible objects.

Generate a cohesive 3x3 cinematic architectural contact sheet containing NINE views of the IDENTICAL INTERIOR SPACE.

CRITICAL RULE: This is NOT a redesign and NOT nine different interiors. Every frame must represent the EXACT SAME room shown in the uploaded image. Keep the architecture, furniture, objects, dimensions, proportions, materials, styling, colors, and spatial relationships IDENTICAL in every frame. Only the camera position, camera angle, focal length, and framing may change.

3x3 CAMERA ANGLES:

1. ZOOM VIEW - Medium-close cinematic view of the main living area, slightly tighter framing than the original image while preserving the exact composition and objects.

2. WIDE VIEW - Wide-angle architectural view showing as much of the same room as physically possible, revealing the full spatial relationship of the existing sofa, sectional, coffee table, ottoman, curtains, wall, pendant lights, plant and flooring without changing anything.

3. RIGHT VIEW - Camera positioned toward the right side of the room, looking diagonally across the exact same interior. Preserve all existing elements and their actual positions.

4. LEFT VIEW - Camera positioned toward the left side of the room, looking diagonally across the exact same interior. Preserve all existing elements and their actual positions.

5. BACK VIEW - Camera positioned from the opposite/rear side of the same room, looking back toward the original seating and feature wall. Infer only the physically necessary unseen continuation of the same architecture; do not invent a new layout or furniture.

6. FRONT VIEW - Straight-on frontal architectural composition centered on the main feature wall and sofa arrangement, maintaining the exact original room design and proportions.

7. ZOOM-TO-FRAME VIEW - Close cinematic detail shot focusing on the framed artwork and surrounding wall treatment, while keeping the frame, wall proportions, lighting, and materials exactly identical to the reference.

8. ZOOM-TO-LIGHT VIEW - Close-up cinematic detail focusing on the existing pendant lights, showing their exact shape, placement, materials, ceiling relationship, and warm illumination. Do not redesign or replace the fixtures.

9. ZOOM-TO-TABLE VIEW - Close cinematic detail focusing on the existing coffee table and its styling, including the vase, small objects, tabletop material, lower table structure, nearby rug and surrounding furniture exactly as shown.

CONTACT SHEET REQUIREMENTS:

- Arrange all 9 views in a clean 3x3 grid
- Each cell must be a separate camera viewpoint of the same physical interior
- Maintain strong visual continuity between all frames
- Same architecture, same furniture, same decor, same materials, same colors, same lighting language
- No object duplication
- No object removal
- No furniture movement
- No redesign
- No additional furniture
- No changes to wall dimensions or openings
- No changes to ceiling, flooring, curtains, artwork, plants, sofa, table, ottoman or lighting fixtures
- Do not mirror the room
- Do not change the interior style
- Do not generate nine variations; generate nine camera views of ONE identical interior
- Photorealistic architectural visualization
- Consistent time of day and lighting conditions
- Consistent materials and texture scale
- Natural perspective and physically believable camera placement
- Premium high-end interior photography
- Cinematic composition, realistic depth, subtle shadows, accurate geometry

The uploaded image must remain the absolute visual reference. Camera changes are allowed; the interior itself is not.
```

## Panel Order

| Position        | View          | Purpose                                                   |
| --------------- | ------------- | --------------------------------------------------------- |
| Row 1, Column 1 | Zoom          | Tighter hero view of the main living area                 |
| Row 1, Column 2 | Wide          | Full spatial relationship of the room                     |
| Row 1, Column 3 | Right         | Diagonal view from the right side                         |
| Row 2, Column 1 | Left          | Diagonal view from the left side                          |
| Row 2, Column 2 | Back          | Reverse view toward the original seating and feature wall |
| Row 2, Column 3 | Front         | Straight-on view of the feature wall and sofa             |
| Row 3, Column 1 | Zoom to frame | Artwork and wall-treatment detail                         |
| Row 3, Column 2 | Zoom to light | Pendant-light and ceiling detail                          |
| Row 3, Column 3 | Zoom to table | Coffee-table styling and material detail                  |

## Technical Specifications

- **Output:** One image containing exactly nine panels
- **Grid:** Clean 3x3 contact sheet with equal, clearly separated cells
- **Subject:** One identical physical interior across all panels
- **Allowed changes:** Camera position, angle, focal length, and framing only
- **Rendering:** Photorealistic architectural visualization and premium interior photography
- **Continuity:** Identical time of day, lighting language, materials, texture scale, geometry, and object placement
- **Perspective:** Natural and physically plausible for every camera position

## Negative Prompt

```text
nine different rooms, redesigned interior, alternate furniture, moved furniture, duplicated objects, removed objects, additional furniture, changed architecture, changed wall dimensions, changed openings, changed ceiling, changed flooring, changed curtains, changed artwork, changed plants, changed sofa, changed table, changed ottoman, changed lighting fixtures, mirrored room, inconsistent materials, inconsistent texture scale, inconsistent time of day, inconsistent lighting, impossible camera placement, distorted perspective, warped geometry, fisheye, collage variations, concept variations, labels, captions, watermark, logo
```
