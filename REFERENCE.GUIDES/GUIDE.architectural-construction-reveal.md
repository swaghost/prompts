# 🏗️ TRANSFORMING EMPTY PLOTS INTO MODERN BUILDINGS

**A complete, step-by-step workflow guide for real estate marketing, architects, and content creators. Learn how to turn a photo of a finished property into an 8-second time-lapse animation where a complete building constructs itself out of an empty plot of land.**

---

## 1. Introduction & Core Concept

### What is an Architectural Construction Reveal?

An Architectural Construction Reveal is a two-step AI video animation workflow. Instead of generating a property from scratch, you take an existing photo of a finished property, generate an emptied version of the plot or land, and use video AI models to sequentially construct the building frame by frame.

### How It Works

The secret behind this technique relies on reversing the destination and starting points:

1. **The Original Photo**: Serves as the End Point (Reference 2).
2. **The Empty Lot Photo**: Created using AI image editing, serving as the Start Point (Reference 1).
3. **The Video Generator**: Synthesizes the transition by sequentially building the foundation, walls, glass, roof features, and exterior props without morphing or warping the architecture.

---

## 2. Prerequisites & Four Golden Rules

Before generating any image or video, ensure your setup meets these four mandatory requirements to prevent failure:

### Rule 1: Identical Image Framing & Crop

Both the empty lot photo (Reference 1) and the finished property photo (Reference 2) must share the **exact same resolution, camera angle, crop, and framing**. A slight shift in framing forces the AI video model to warp or stretch the architecture.

### Rule 2: Clean and Well-Lit Reference Photos

High-resolution photos with crisp daylight or balanced dusk lighting provide clear surface boundaries for object placement. **Avoid blurry or dim photos.**

### Rule 3: Preserve the Environmental Foundation

When generating the empty plot in Step 1, **erase the building, fixtures, and loose furniture**, but **keep the ground surface** (asphalt, concrete, gravel), sidewalks, curbs, background trees, and sky **fully intact**.

### Rule 4: Verify Step 1 Quality Before Moving On

Always inspect the empty plot image generated in Step 1. If the camera perspective, horizon line, or ground boundaries changed, regenerate the image until it matches Reference 2 perfectly.

---

## 3. Two-Step Workflow

### Required Tools

- **Image Generator / Inpainting Tool**: Nano Banana (or equivalent image editing tool)
- **Video Generation Tool**: Omni Flash via pollo.ai

---

### Step 1: Generating the Empty Plot (Nano Banana)

Upload your original property photo to Nano Banana, paste **Prompt 1**, and generate an image of the cleared land. This generated output will become **Reference Image 1**.

#### 📄 PROMPT 1: Object & Building Removal (Empty Plot Generation)

```
Remove the entire building structure, including walls, windows, doors, roof, awnings, signage, outdoor furniture, planters, and all fixtures attached to the building.

WHAT TO REMOVE:
- Complete building/structure
- All architectural elements (walls, windows, doors, roof)
- Signage and text
- Outdoor furniture and fixtures
- Planters and movable objects
- Any items attached to or part of the building

WHAT TO PRESERVE:
- Ground surface (asphalt, concrete, gravel, paving)
- Sidewalks and curbs
- Background trees and vegetation
- Sky and clouds
- Distant background elements
- Natural terrain features
- Street elements not attached to building

CRITICAL REQUIREMENTS:
- Maintain exact camera angle and perspective
- Keep horizon line perfectly level
- Preserve original image resolution and aspect ratio
- Ensure ground surface texture remains consistent
- No distortion or warping of remaining elements
- Clean edges where building was removed

OUTPUT GOAL:
A clean, empty plot of land showing only the ground surface, background environment, and sky, with all traces of the building completely removed while preserving the exact framing and perspective of the original photo.
```

---

### Step 2: Generating the Reveal Animation (Omni Flash)

Open Omni Flash and upload your images into the reference fields in this precise order:

- **Reference 1**: The empty plot photo (from Step 1)
- **Reference 2**: The original finished property photo

Set the video duration to **8 seconds**, paste **Prompt 2**, and execute the video generation.

#### 📄 PROMPT 2: Sequential Construction Animation (Building Reveal)

```
Create an 8-second time-lapse construction animation showing a modern building materializing from an empty plot of land through sequential, realistic construction stages.

ANIMATION SEQUENCE (8 seconds):

0:00-0:02 — FOUNDATION & STRUCTURE
- Ground preparation and foundation layout appears
- Primary structural frame begins rising from ground
- Steel/concrete skeleton emerges vertically

0:02-0:05 — WALLS & ENCLOSURE
- Wall panels and exterior cladding install progressively
- Windows and glass facade elements appear and lock into place
- Door frames and entry elements materialize
- Roof structure completes

0:05-0:08 — FINISHING & DETAILS
- Exterior finishes and facade details complete
- Signage and branding elements appear
- Landscaping elements (planters, fixtures) install
- Final polish and completion

CONSTRUCTION REALISM RULES:
- Building constructs from bottom to top (foundation → walls → roof → details)
- Each construction phase follows logical architectural assembly sequence
- No floating elements or pieces appearing before their supporting structure
- Materials appear to install/assemble rather than fade in
- Maintain structural integrity throughout animation

SPATIAL & CAMERA CONSTRAINTS:
- Camera remains completely locked in exact position and angle
- No camera movement, zoom, pan, or rotation
- Background environment (trees, sky, ground, distant elements) stays perfectly static
- Horizon line remains level throughout
- No morphing, warping, or distortion of architectural elements
- Building geometry stays precise and clean throughout construction

ENVIRONMENTAL PRESERVATION:
- Ground surface texture remains constant
- Background trees and vegetation stay static
- Sky and clouds remain stable
- No environmental changes or shifting elements
- Lighting conditions stay consistent

NEGATIVE PROMPTS:
camera movement, camera drift, zooming, panning, morphing architecture, warped walls, distorted windows, floating elements, illogical construction sequence, environmental changes, shifting perspective, wobbly motion, flickering, glitching, duplicated buildings, text distortion, warped signage
```

---

## 4. Master Prompt Library (Property-Specific Examples)

This library contains tailored prompts for specific properties processed in this workflow.

### Property 1: "Tinyhouse777 COFFEE" Storefront

**PROMPT 1 (Empty Plot):**

```
Remove the entire "Tinyhouse777 COFFEE" building structure, including the cream-colored walls, black-framed windows and doors, roof overhang, signage, outdoor cafe tables and chairs, planters with greenery, and all fixtures.

Preserve: The concrete/asphalt ground surface, background trees and mountains, sky, and distant landscape elements.

Maintain exact camera angle, perspective, and framing.
```

**PROMPT 2 (Construction Animation):**

```
Create an 8-second time-lapse construction animation of the "Tinyhouse777 COFFEE" modern minimalist cafe building materializing from the empty plot.

0:00-0:02 — Foundation and primary structure frame rises
0:02-0:05 — Cream walls install, black-framed windows and doors lock into place, roof overhang completes
0:05-0:08 — "Tinyhouse777 COFFEE" signage appears, outdoor furniture installs, planters with greenery materialize

Camera completely locked. Background mountains, trees, and sky remain static throughout.
```

---

### Property 2: Minimalist White Cafe with Gravel Yard

**PROMPT 1 (Empty Plot):**

```
Remove the white minimalist cafe building, including all walls, large windows, doors, roof structure, attached fixtures, and the small tree/landscaping near the entrance.

Preserve: The gravel/crushed stone ground surface, background trees, sky, and distant elements.

Maintain exact camera perspective and framing.
```

**PROMPT 2 (Construction Animation):**

```
Create an 8-second construction reveal of the white minimalist cafe with floor-to-ceiling windows.

0:00-0:02 — Foundation emerges, structural frame rises from gravel surface
0:02-0:05 — White walls install, large glass windows appear and lock in, roof completes
0:05-0:08 — Entrance details finish, small tree appears near entry, final architectural details complete

Locked camera. Gravel surface texture and background environment stay perfectly static.
```

---

### Property 3: "Attention, please" Facade & Mountain Backdrop

**PROMPT 1 (Empty Plot):**

```
Remove the modern building with "Attention, please" signage, including all structural elements, glass panels, signage, and attached fixtures.

Preserve: The paved ground surface, background mountains, sky, distant trees, and natural landscape.

Keep exact camera angle and mountain backdrop alignment.
```

**PROMPT 2 (Construction Animation):**

```
Create an 8-second construction sequence for the "Attention, please" modern building with mountain backdrop.

0:00-0:02 — Foundation and steel frame structure rises
0:02-0:05 — Walls and glass facade panels install, main structure completes
0:05-0:08 — "Attention, please" signage materializes, finishing details appear

Camera locked. Mountain backdrop and natural environment remain completely static.
```

---

### Property 4: "PLANT" Minimalist Cafe & Patio

**PROMPT 1 (Empty Plot):**

```
Remove the "PLANT" cafe building, patio furniture, planters, outdoor seating area, signage, and all cafe fixtures.

Preserve: The concrete patio surface, gravel areas, background trees, sky, and distant elements.

Maintain exact framing and surface textures.
```

**PROMPT 2 (Construction Animation):**

```
Create an 8-second reveal of the "PLANT" minimalist cafe with outdoor patio area.

0:00-0:02 — Foundation and basic structure emerge from patio surface
0:02-0:05 — Walls rise, windows install, roof structure completes
0:05-0:08 — "PLANT" signage appears, patio furniture materializes, planters with greenery install, final details complete

Locked camera. Concrete and gravel surface textures stay constant throughout.
```

---

### Property 5: "COFFEE HOUSE" Facade with Topiary Shrubs

**PROMPT 1 (Empty Plot):**

```
Remove the "COFFEE HOUSE" building, including all walls, windows, doors, signage, awnings, topiary shrubs, and fixtures.

Preserve: The paved ground surface, background trees, sky, and environmental elements.

Keep exact camera angle and ground plane perspective.
```

**PROMPT 2 (Construction Animation):**

```
Create an 8-second construction sequence for the "COFFEE HOUSE" with sculptural topiary landscaping.

0:00-0:02 — Foundation and structural skeleton rises from pavement
0:02-0:05 — Walls and facade install, windows and doors lock in, roof completes
0:05-0:08 — "COFFEE HOUSE" signage appears, topiary shrubs materialize, landscaping details finish

Camera locked. Background environment and ground surface remain perfectly static.
```

---

## 5. Troubleshooting & Common Issues

### Issue: Building warps or morphs during animation

**Solution**: Verify that Reference 1 (empty plot) and Reference 2 (finished building) have identical framing, resolution, and perspective. Regenerate the empty plot if needed.

### Issue: Background elements shift or change

**Solution**: Ensure Step 1 preserved all environmental elements (ground, trees, sky). Use stronger camera lock language in Prompt 2.

### Issue: Construction sequence is illogical

**Solution**: Add more specific timeline breakdowns (foundation before walls before roof). Emphasize "bottom-to-top" construction logic.

### Issue: Elements appear blurry or distorted

**Solution**: Start with higher resolution source images. Ensure original property photo is well-lit and sharp.

---

## 6. Best Practices

✅ **Always verify Step 1 output** before proceeding to Step 2
✅ **Use high-resolution source photos** (at least 1920x1080)
✅ **Keep camera angles straight-on or slight angles** (avoid extreme perspectives)
✅ **Test with simple buildings first** before attempting complex architecture
✅ **Preserve ground textures perfectly** in Step 1 - they're critical anchor points
✅ **Include "locked camera" language** in every video prompt
✅ **Break timeline into 2-3 second chunks** for better control

---

**Source**: [Notion Guide](https://efficient-mink-952.notion.site/Transforming-Empty-Plots-into-Modern-Buildings-3b59502993ae809b8a75cfc2ace4ff39)
