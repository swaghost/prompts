# Transforming Empty Plots into Modern Buildings (Dual-Reference)

## Description

A complete, step-by-step workflow guide for transforming photos of finished properties into 8-second cinematic construction reveal animations. Rather than generating architecture from scratch, this technique takes an existing photo of a finished property, generates an emptied version of the plot or land using AI inpainting, and uses dual-reference video AI to sequentially construct the building frame by frame. The methodology reverses destination and starting points: the original photo serves as the end point (Reference 2), the empty lot serves as the start point (Reference 1), and the video generator synthesizes the transition by sequentially building foundation, walls, glass, roof features, and exterior props without morphing or warping the architecture.

## Usage

Perfect for modern building showcase videos, cafe and restaurant reveal reels, storefront construction animations, commercial property marketing, real estate social media content, architecture firm presentations, small business property reveals, retail space showcases, hospitality venue marketing, coffee shop branding videos, boutique building reveals, urban development content, property transformation stories, construction sequence simulations, business opening announcements, property listing enhancements, before-and-after reveals, commercial real estate marketing, franchise location showcases, small business success stories, property development portfolios, architectural visualization alternatives, and real estate agent content creation for modern commercial and mixed-use properties.

## Prerequisites

- **AI Platform Access**: pollo.ai account
- **Image Generator/Inpainting Tool**: Nano Banana or equivalent
- **Video Generation Tool**: Omni Flash via pollo.ai
- **Source Image**: Clean, well-lit photo of finished property
- **Image Quality**: High-resolution with crisp daylight or balanced dusk lighting
- **Duration**: 8 seconds (fixed output)
- **Aspect Ratio**: Flexible (matches source image)

## Technical Specifications

- **Animation Type**: Sequential discrete component assembly (not morphing)
- **Camera Behavior**: Locked-off with subtle continuous drift (eases to stop at 6s)
- **Reference Framework**: Dual-reference (empty lot at 0s, full building at 6s)
- **Motion Physics**: Mixed motion types (POP-IN, DROP, DESCEND, INSTANT)
- **Assembly Timeline**: 0-2s empty, 2-6s construction, 6-8s static hold
- **Final Frame Match**: Must exactly equal Reference 2 (original property photo)
- **Environment Stability**: Ground, background, sky remain completely unchanged

---

## Core Concept: Architectural Construction Reveal

### **What Is It?**

An Architectural Construction Reveal is a two-step AI video animation workflow. Instead of generating a property from scratch, you take an existing photo of a finished property, generate an emptied version of the plot or land, and use video AI models to sequentially construct the building frame by frame.

### **How It Works**

The secret behind this technique relies on reversing the destination and starting points:

1. **The Original Photo**: Serves as the End Point (Reference 2)
2. **The Empty Lot Photo**: Created using AI image editing, serving as the Start Point (Reference 1)
3. **The Video Generator**: Synthesizes the transition by sequentially building the foundation, walls, glass, roof features, and exterior props without morphing or warping the architecture

---

## Four Golden Rules (Prerequisites)

### **Rule 1: Identical Image Framing & Crop**

Both the empty lot photo (Reference 1) and the finished property photo (Reference 2) must share the exact same resolution, camera angle, crop, and framing.

**Why It Matters:**

- A slight shift in framing forces the AI video model to warp or stretch the architecture
- Misaligned horizons cause perspective breathing
- Different aspect ratios result in composition distortion

**How to Ensure:**

- Generate Reference 1 directly from Reference 2 file (no intermediate crops)
- Verify pixel dimensions match exactly
- Check horizon line and vanishing points align perfectly

---

### **Rule 2: Clean and Well-Lit Reference Photos**

High-resolution photos with crisp daylight or balanced dusk lighting provide clear surface boundaries for object placement.

**Ideal Conditions:**

- Natural daylight (golden hour or midday)
- Balanced dusk lighting with ambient visibility
- High contrast between building and background
- Sharp focus on architectural details

**Avoid:**

- Blurry or motion-blurred images
- Dim nighttime photography without supplemental lighting
- Extreme shadows that obscure structural edges
- Low-resolution or heavily compressed images

---

### **Rule 3: Preserve the Environmental Foundation**

When generating the empty plot in Step 1, erase the building, fixtures, and loose furniture, but keep the ground surface (asphalt, concrete, gravel), sidewalks, curbs, background trees, and sky fully intact.

**Preserve:**
✓ Ground surfaces (asphalt, concrete, gravel, paving stones)  
✓ Sidewalks and curb lines  
✓ Background trees and distant buildings  
✓ Sky gradients and cloud patterns  
✓ Lighting direction and shadow angles  
✓ Environmental textures and materials

**Remove:**
✗ Main building structure and walls  
✗ Outdoor furniture (tables, chairs, umbrellas)  
✗ Signage and branding elements  
✗ Planters and loose decorative items  
✗ Lighting fixtures attached to building  
✗ Any elements connected to structure

---

### **Rule 4: Verify Step 1 Quality Before Moving On**

Always inspect the empty plot image generated in Step 1. If the camera perspective, horizon line, or ground boundaries changed, regenerate the image until it matches Reference 2 perfectly.

**Quality Checklist:**

- [ ] Horizon line identical to original
- [ ] Background elements (trees, buildings) in same positions
- [ ] Ground surface texture clean and natural
- [ ] No visible artifacts or seams from removal
- [ ] Crop and framing unchanged
- [ ] Lighting and shadow direction preserved
- [ ] Aspect ratio and pixel dimensions match

---

## Two-Step Workflow

### **Required Tools**

- **Image Generator / Inpainting Tool**: Nano Banana (or equivalent image editing tool)
- **Video Generation Tool**: Omni Flash via pollo.ai

---

### **Step 1: Generating the Empty Plot (Nano Banana)**

Upload your original property photo to Nano Banana, paste Prompt 1, and generate an image of the cleared land. This generated output will become Reference Image 1.

#### **Prompt 1 Template (Object & Building Removal)**

```
Remove the entire building structure, all architecture, outdoor furniture, seating, tables, planters, and fixtures from this image. Show a completely empty cleared plot of land with only the surrounding environmental ground surface intact.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep the road, curb lines, sidewalk pavement, surrounding background trees, and lighting completely unchanged. Fill the cleared area with clean matching ground pavement in the same materials already visible. Same lighting, same shadow direction, same time of day.
```

**Customization Notes:**

- Specify ground surface type: "grey concrete," "asphalt road," "gravel yard," "brick paving"
- Mention specific background elements to preserve: "distant mountain," "pine trees," "string lights"
- Reference lighting: "overcast daylight," "twilight sunset," "bright midday sun"

---

### **Step 2: Generating the Reveal Animation (Omni Flash)**

Open Omni Flash, upload your images into the reference fields in this precise order:

- **Reference 1**: The empty plot photo (from Step 1)
- **Reference 2**: The original finished property photo

Set the video duration to 8 seconds, paste Prompt 2, and execute the video generation.

#### **Prompt 2 Template (Sequential Construction Animation)**

```
Static real estate architectural construction reveal, 8 seconds. Locked-off camera. The only camera movement allowed is a subtle continuous drift of a few degrees that eases to a stop at 6s, small enough that the composition stays recognisably the same shot from start to finish. No dolly, no zoom, no whip pan.

CAMERA LOCK - ANGLE AND PERSPECTIVE NEVER CHANGE: The camera position, height, angle, focal length, field of view, and perspective are exactly those of the reference images and stay fixed for the entire 8 seconds. All vanishing points, floor grid lines, wall directions, and pavement edges remain in the same directions throughout. Do not reframe, re-angle, re-render, or re-photograph the lot from a different viewpoint. Do not change lens compression or widen the view. Do not reveal any part of the scene not visible in the reference images. The composition at every frame must overlay onto the reference images with the ground in the same place.

HOW TO USE THE TWO REFERENCE IMAGES - READ CAREFULLY: The first reference image is the state of the empty cleared lot at 0s. The second reference image is the state of the fully constructed building at 6s. These are two discrete states, NOT two ends of a blend. Do not interpolate between them. Do not cross-fade, morph, or gradually transform the first image into the second. Do not compute intermediate frames by mixing the two images together. Instead, the first image stays exactly as it is, unchanged, and the structural elements and furniture from the second image are placed onto it one group at a time until the building is complete. At every moment the frame shows the first image plus whichever construction elements have already arrived, never a partial blend of the two.

STRICT BUILDING INVENTORY - NOTHING NEW: The complete and final set of architectural elements, fixtures, and outdoor furniture is defined entirely by the second reference image. Every wall, window frame, door, sign, table, chair, and planter that appears must already be visible in the second reference image, in the same position, at the same scale, in the same orientation, in the same material, colour, and finish. Do not add, invent, substitute, duplicate, restyle, or embellish anything. No extra buildings, no extra seating, no extra plants, and no structural additions beyond exactly what the second reference image shows. If an element is absent from the second reference image, it must never appear at any point in the video. The final frame must contain exactly the same details as the second reference image, nothing more, nothing less.

ABSOLUTE LOCK: Ground flooring, surrounding environmental elements, horizon, and daylight direction are identical in both reference images and must stay identical for the entire 8 seconds, never redrawn, warped, shifted, or reinterpreted.

REVEAL METHOD - MIXED MOTION: Building components and furniture arrive in groups using different movements suited to their type, never all the same way. Every element is fully opaque, complete, and correctly proportioned from the first frame it is visible. An element either does not exist yet or exists fully, there is no in-between state.

POP-IN - core building walls, main door frame, and primary glass window grids: appears directly at its final ground position, slightly undersized for about two frames, overshoots very slightly, then settles to exact final size. Roughly 0.2 seconds. Silhouette and proportions never change, only overall scale.

DROP - awnings, roof features, secondary wall structures, and outdoor furniture: falls down from just above its final position and lands with a firm settle onto the ground.

DESCEND - wall signage, hanging lights, roof vines, and wall typography: lowers from above into final height on the building facade.

INSTANT - wall lamps, small signs, potted plants, and interior window accessories: appear in place in a single frame, no motion at all.

Each arrival takes about 0.2 to 0.3 seconds. Components travel only a short distance, no long flight paths, no crossing the frame. Shadows appear the moment a structural element or object lands or pops.

TIMELINE:
0-2s: The frame is exactly the first reference image (empty cleared lot), unchanged. Camera begins its slow drift.
2-3.5s: Core building walls, door openings, and primary window glass POP-IN onto the empty land. Everything else in the frame is unchanged.
3.5-5s: Roof structures, wall text, awnings, and outdoor seating DROP and DESCEND into position.
5-6s: Wall lamps, small decor, and potted plants appear INSTANT; all contact shadows land on the ground; camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image, completely static, no new elements, no repositioning, no further changes. Faint leaf movement and stable daylight.

Photorealistic architectural exterior photography, natural daylight, modern building construction, no people.
```

#### **Universal Negative Prompt**

```
changing camera angle, changing perspective, new viewpoint, reframing, re-angling, rotating camera, orbiting, arc shot, crane move, changing camera height, changing focal length, changing field of view, lens distortion, wide angle shift, perspective warp, shifting vanishing point, tilting horizon, revealing unseen areas of the lot, added structural elements, invented architecture, new props, restyled facade, changed building colour, changed materials, components not present in the reference, interpolation between reference images, blending two images, image morph, cross-fade between frames, gradual transformation, morphing, object morphing, shape shifting, transforming, geometry changing, slow growth, gradual scaling, growing from zero, unfolding, assembling from parts, dissolving in, fade in, fade out, cross dissolve, opacity transition, ghosting, double exposure, translucent objects, glowing particles, light streaks
```

---

## Property-Specific Prompt Library

### **Property 1: "Tinyhouse777 COFFEE" Storefront**

**Context**: Coffee shop with white walls, arched doorway, oval window, green roof vines, outdoor seating

**Step 1 - Remove Building (Nano Banana):**

```
Remove the entire building structure, all architecture, outdoor furniture, plants, signs, and fixtures from this image. Show a completely empty cleared plot of land and open lot.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep the asphalt road, yellow lane markings, curb lines, sidewalk pavement, surrounding background trees, and overcast daylighting completely unchanged. Fill the cleared lot area with clean matching grey concrete pavement and smooth ground surfaces in the same materials already visible. Same soft natural lighting, same shadow direction, same time of day.
```

**Step 2 - Reveal Animation (Omni Flash):**

```
[Use complete Step 2 template above with these specific customizations:]

Timeline customization:
2-3.5s: Core white building walls, arched glass door, and oval window POP-IN onto the empty land. Everything else in the frame is unchanged.
3.5-5s: The green roof vines and "Tinyhouse777 COFFEE" text DESCEND onto the facade; white awning and outdoor black tables with stools DROP onto the pavement.
5-6s: Black wall lamps, round sign, and small potted plants appear INSTANT; all contact shadows land on the sidewalk; camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image, completely static, no new elements, no repositioning, no further changes. Faint leaf movement on roof vines and stable daylight.

Photorealistic architectural exterior photography, soft natural daylight, modern coffee shop construction, no people.
```

---

### **Property 2: Minimalist White Cafe with Gravel Yard**

**Context**: White minimalist cafe with rounded windows, gravel yard, outdoor seating with umbrellas, dusk lighting

**Step 1 - Remove Building (Nano Banana):**

```
Remove the entire building structure, all architecture, outdoor furniture, umbrellas, plants, signs, and fixtures from this image. Show a completely empty cleared plot of land with only the gravel ground surface.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep the grey gravel yard floor, flat stone stepping pavers, surrounding green trees, string lights, and the dusk sunset sky completely unchanged. Fill the cleared area with clean matching grey gravel and stone pavers in the same materials already visible. Same twilight lighting, same shadow direction, same time of day.
```

**Step 2 - Reveal Animation (Omni Flash):**

```
[Use complete Step 2 template with these customizations:]

Timeline customization:
2-3.5s: Core white building walls, rounded oblong window frames, and arched glass door POP-IN onto the gravel lot. Everything else in the frame is unchanged.
3.5-5s: The white patio umbrella and folding chairs DROP onto the gravel; wall typography and box sign DESCEND onto the facade.
5-6s: White standing mailbox and sign boards appear INSTANT; all contact shadows land on the ground; camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image, completely static, no new elements, no repositioning, no further changes. Faint leaf movement on surrounding trees and stable twilight glow.

Photorealistic architectural exterior photography, soft sunset ambient light, modern minimalist cafe construction, no people.
```

---

### **Property 3: "Attention, please" Facade & Mountain Backdrop**

**Context**: Modern white building with glass doors, "Attention, please" wall logo, standing sign pole, mountain background

**Step 1 - Remove Building (Nano Banana):**

```
Remove the entire building structure, all architecture, outdoor signs, standing poles, trees, and fixtures from this image. Show a completely empty cleared plot of land with only the gravel and concrete ground surface.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep the grey gravel yard floor, concrete base, background mountain peak, and bright blue clear sky completely unchanged. Fill the cleared area with clean matching grey gravel and concrete paving in the same materials already visible. Same bright daylight lighting, same shadow direction, same time of day.
```

**Step 2 - Reveal Animation (Omni Flash):**

```
[Use complete Step 2 template with these customizations:]

Timeline customization:
2-3.5s: Core white building structure, glass double entrance door, and tree trunk POP-IN onto the gravel lot. Everything else in the frame is unchanged.
3.5-5s: The green and orange standing sign pole DROPS into position; blue "Attention, please" logo DESCENDS onto the wall facade.
5-6s: Small ground sign and entrance decals appear INSTANT; all contact shadows land on the ground; camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image, completely static, no new elements, no repositioning, no further changes. Faint sway in tree branches and stable clear daylight.

Photorealistic architectural exterior photography, clear blue sky, bright daylight, modern minimalist building construction, no people.
```

---

### **Property 4: "PLANT" Minimalist Cafe & Patio**

**Context**: White curved-roof cafe with "PLANT" wall text, large glass windows, outdoor seating, concrete patio

**Step 1 - Remove Building (Nano Banana):**

```
Remove the entire building structure, all architecture, outdoor furniture, seating, tables, planters, and fixtures from this image. Show a completely empty cleared plot of land with only the grey concrete pavement surface and side concrete wall.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep the smooth concrete patio flooring, side concrete wall, road edge, and soft overcast daylighting completely unchanged. Fill the cleared area with clean matching concrete paving in the same materials already visible. Same soft natural lighting, same shadow direction, same time of day.
```

**Step 2 - Reveal Animation (Omni Flash):**

```
[Use complete Step 2 template with these customizations:]

Timeline customization:
2-3.5s: Core white building structure, curved roofline, and large glass windows POP-IN onto the concrete patio. Everything else in the frame is unchanged.
3.5-5s: The "PLANT" wall typography DESCENDS onto the upper facade; outdoor tables, chairs, cylinder stools, and cubic planters DROP onto the patio floor.
5-6s: Small potted plants appear INSTANT; all contact shadows land on the ground; camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image, completely static, no new elements, no repositioning, no further changes. Faint leaf movement on olive tree and stable daylight.

Photorealistic architectural exterior photography, soft overcast light, modern minimalist building construction, no people.
```

---

### **Property 5: "COFFEE HOUSE" Facade with Topiary Shrubs**

**Context**: White coffee house with black glass windows, wooden slat panels, white awning, large potted topiary shrubs

**Step 1 - Remove Building (Nano Banana):**

```
Remove the entire building structure, all architecture, outdoor plants, potted shrubs, lights, and fixtures from this image. Show a completely empty cleared plot of land with only the paved sidewalk, curb, and asphalt road surface.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep the grey brick paved sidewalk, black and white striped curb, asphalt street, background pine trees, and warm bright daylighting completely unchanged. Fill the cleared lot area with clean matching grey sidewalk paving in the same materials already visible. Same warm natural lighting, same shadow direction, same time of day.
```

**Step 2 - Reveal Animation (Omni Flash):**

```
[Use complete Step 2 template with these customizations:]

Timeline customization:
2-3.5s: Core white building walls, black glass window grid, and large white potted topiary shrubs POP-IN onto the sidewalk. Everything else in the frame is unchanged.
3.5-5s: The vertical wooden slat panels DROP onto the facade; white awning and "COFFEE HOUSE" text DESCEND into position.
5-6s: Black wall sconce lights and interior window decor appear INSTANT; all contact shadows land on the ground; camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image, completely static, no new elements, no repositioning, no further changes. Faint sway in background pine trees and stable warm sunlight.

Photorealistic architectural exterior photography, warm bright daylight, modern coffee house construction, no people.
```

---

## Troubleshooting

### **Problem: Warping or perspective changes**

**Solution**: Verify Reference 1 and Reference 2 have identical pixel dimensions and framing. Regenerate Reference 1 if needed.

### **Problem: Elements morph or fade in smoothly**

**Solution**: Ensure "HOW TO USE THE TWO REFERENCE IMAGES" block is intact. Strengthen anti-interpolation language.

### **Problem: Extra objects appear**

**Solution**: Confirm "STRICT BUILDING INVENTORY" section is present. Add specific negative prompts for unwanted elements.

### **Problem: Timeline ignored, everything appears at once**

**Solution**: Shorten prompt by removing non-essential descriptions while preserving core instruction blocks.

---

## Best Practices

- Always use high-resolution, well-lit source images
- Generate Reference 1 directly from Reference 2 (no intermediate edits)
- Verify Step 1 quality before proceeding to Step 2
- Preserve all environmental elements (ground, sky, trees, lighting)
- Maintain identical framing between both references
- Use property-specific timeline customizations for best results
- Test with one property before batch processing

---

## Output Specifications

- **Duration**: 8 seconds fixed
- **Resolution**: Matches source image
- **Format**: MP4 (H.264)
- **Quality**: Photorealistic architectural photography
- **Use Cases**: Social media reels, marketing videos, portfolio pieces, presentation content

---

## Related Files

- See also: [property-construction-reveal-dual-reference.md](./property-construction-reveal-dual-reference.md) for general property construction workflow
- See also: [architectural-landmark-reveal-animation.md](./architectural-landmark-reveal-animation.md) for iconic landmark reveals
- See also: [architectural-animations-video.md](./architectural-animations-video.md) for other animation types

---

## Source Reference

Based on **Transforming Empty Plots into Modern Buildings** by efficient-mink-952 (Notion).  
Original documentation: https://efficient-mink-952.notion.site/Transforming-Empty-Plots-into-Modern-Buildings-3b59502993ae809b8a75cfc2ace4ff39

Adapted for the A7 ai.prompts library structure with expanded examples, detailed troubleshooting, and platform integration guidance.
