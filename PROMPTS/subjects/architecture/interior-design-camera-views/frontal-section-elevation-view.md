# Frontal Section Elevation View – Kitchen and Living Room

## Description

Photorealistic frontal side-view architectural section of kitchen and living room spaces. Shows interior spaces as a straight-on elevation drawing with the kitchen on the left and living room on the right, viewed from eye level. This viewpoint preserves all existing design elements, furniture positions, and materials from the input image while changing only the camera angle to a formal architectural section view.

## Usage

Use with an existing interior design image as input. The AI will maintain all design decisions, layout, furniture placement, materials, colors, and styling from the reference image, but present it as a clean frontal section elevation suitable for architectural presentation or client review.

## Prerequisites

- **Input Image Required**: Must provide a reference image of the kitchen and living room design
- **Design Locked**: All elements from input image are preserved exactly as shown
- **Viewpoint Change Only**: Only the camera angle is modified, not the design itself

## Subject/Scene

- **Space**: Combined kitchen and living room shown in section
- **Layout**: Kitchen on left side, living room on right side
- **Viewpoint**: Straight frontal elevation, eye level, no perspective distortion
- **Floor Position**: At bottom of frame
- **Ceiling Position**: At top of frame

## Design Preservation Rules

### Living Room Elements (Exact Positions)

- Light-colored boucle armchair and small side table in exact original positions
- Olive sofa positioned with back facing camera exactly as in input layout
- All windows, lighting fixtures, plants, accessories preserved
- All colors, materials, textures, finishes unchanged

### Kitchen Elements (Exact Positions)

- Cabinet fronts: light-colored, handleless
- Island, stools, appliances in exact positions
- All accessories, plants, lighting preserved

### Materials (From Input Image)

- **Flooring**: Warm oak herringbone
- **Kitchen Cabinetry**: Matte taupe
- **Countertops & Backsplash**: Light marble with subtle veining
- **Window Treatments**: Beige linen curtains
- **Living Room Seating**: Light boucle armchair, olive upholstered sofa

## Image Prompt

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  Create a photorealistic frontal side-view section of the kitchen and  │
│  living room. Show the kitchen on the left and the living room on the  │
│  right, viewed straight from the side at eye level. The floor must be  │
│  at the bottom and the ceiling must be at the top.                     │
│                                                                         │
│  Preserve exactly the existing layout, furniture positions, cabinetry, │
│  island, stools, sofa, armchair, tables, windows, lighting, plants,    │
│  accessories, colors, materials, textures and finishes from the input  │
│  image. In the living room, clearly show the light-colored boucle      │
│  armchair and the small side table in their exact original positions.  │
│  The olive sofa may remain, but must be positioned with its back       │
│  facing the camera exactly as in the input layout.                     │
│                                                                         │
│  In the kitchen, keep the cabinet fronts light-colored. Materials:     │
│  warm oak herringbone flooring, matte taupe kitchen cabinetry, light   │
│  marble countertops and backsplash with subtle veining, beige linen    │
│  curtains, a light boucle armchair and an olive upholstered sofa.      │
│                                                                         │
│  Do not add any extra details, furniture, accessories, furniture or    │
│  styling elements not visible in the input image. Do not move,         │
│  replace, redesign, recolor or restyle any element. Change only the    │
│  viewpoint.                                                             │
│                                                                         │
│  Use a straight frontal elevation with no top-down angle, no           │
│  axonometric view, no dollhouse view and no visible floor plan. White  │
│  background, dark cut walls, no text.                                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## Technical Specifications

### Camera View

- **Type**: Frontal section elevation
- **Angle**: Straight-on, 90° perpendicular to section plane
- **Height**: Human eye level
- **Perspective**: No perspective distortion (orthographic projection preferred)

### Composition

- **Kitchen**: Left side of frame
- **Living Room**: Right side of frame
- **Floor**: Bottom edge of frame
- **Ceiling**: Top edge of frame
- **Background**: White, clean architectural presentation style
- **Cut Walls**: Dark to show section depth

### Rendering Style

- **Quality**: Photorealistic architectural visualization
- **Detail Level**: High detail showing materials, textures, finishes
- **Lighting**: Natural, accurate material representation
- **Style**: Professional architectural section drawing with photorealistic rendering

### Design Constraints

- ✅ **Preserve**: Layout, furniture positions, all accessories, plants, lighting, materials, colors, textures
- ✅ **Show Clearly**: Light boucle armchair, small side table, olive sofa back
- ✅ **Material Accuracy**: Herringbone flooring, matte taupe cabinets, marble countertops, linen curtains
- ❌ **Do Not Add**: Extra furniture, accessories, styling elements not in input
- ❌ **Do Not Change**: Layout, colors, materials, furniture positions, design elements
- ❌ **Avoid**: Top-down angles, axonometric views, dollhouse views, floor plans visible

### Negative Prompt

```
top-down view, bird's eye view, axonometric view, isometric view, dollhouse view,
visible floor plan, perspective distortion, angled view, diagonal view, added
furniture, extra accessories, moved furniture, redesigned elements, recolored
materials, restyled furniture, dark cabinets, wrong materials, cluttered
composition, text overlays, labels, dimensions, annotations, unrealistic lighting,
oversaturated colors, extra windows, added plants, furniture not in original,
changed layout, rotated furniture, 3/4 view, corner view
```

## Platform

- **Primary**: Midjourney (excellent for architectural sections and photorealistic rendering)
- **Alternative**: DALL-E 3 (good for image-to-image transformations with design preservation)
- **Alternative**: Stable Diffusion with ControlNet (precise layout preservation)

## Use Cases

- **Architectural Presentations**: Clean section views for client presentations
- **Design Documentation**: Formal elevation drawings with photorealistic quality
- **Portfolio Work**: Professional architectural visualization
- **Client Communication**: Clear side-by-side room comparison
- **Design Review**: Easy-to-understand spatial relationships
