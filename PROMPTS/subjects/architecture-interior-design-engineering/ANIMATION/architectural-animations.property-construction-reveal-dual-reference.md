# AI Property Construction Reveal Workflow (Dual-Reference)

## Description

Complete technical workflow for creating photorealistic 8-second AI-generated property construction animations. Using a single static reference image of a finished building, this process generates a seamless visual reveal where a bare plot of land transforms into a fully constructed architectural project through sequential component assembly. The fundamental principle rests on inverted generation: establish the destination first, reconstruct the origin second, then animate the discrete arrival of structural elements with physically grounded motion physics.

## Usage

Perfect for property development marketing videos, real estate showcase reels, architecture firm portfolio pieces, construction company presentations, before-and-after property reveals, social media real estate content, investor pitch presentations, land development proposals, architectural visualization demos, construction timeline animations, property sales presentations, urban development showcases, residential project marketing, commercial property reveals, luxury home presentations, housing development promos, construction progress simulations, architectural rendering alternatives, property transformation videos, development milestone celebrations, real estate agent marketing materials, property listing enhancements, and broadcast-quality reveal videos without complex 3D modeling or video editing software.

## Prerequisites

- **AI Platform Access**: pollo.ai account with access to both tools
- **Object Removal Tool**: Nano Banana (Step 1 - structure removal)
- **Video Generation Tool**: Omni Flash (Step 2 - animation construction)
- **Source Image**: High-resolution photo of completed property (minimum 1080p)
- **Image Quality**: High-contrast, well-lit exterior photography
- **Duration**: 8 seconds (fixed output)
- **Aspect Ratio**: Flexible (9:16 for vertical social media, 16:9 for landscape presentations)

## Technical Specifications

- **Animation Type**: Sequential discrete component assembly (not morphing or cross-fading)
- **Camera Behavior**: Locked-off with subtle continuous drift (eases to stop at 6s)
- **Reference Framework**: Dual-reference (empty plot at 0s, full property at 6s)
- **Motion Physics**: Mixed motion types (POP-IN, DROP, DESCEND, SETTLE, INSTANT)
- **Assembly Duration**: 0-2s empty, 2-6s construction, 6-8s static hold
- **Final Frame Accuracy**: Must exactly match Reference 2 (original property photo)
- **Environment Consistency**: Background, sky, lighting remain completely static throughout

---

## Core Operational Mechanics

### **The Inverted Generation Principle**

Rather than creating a building from nothing, this workflow establishes the destination first and reconstructs the origin second:

```
[Original Property Image]
        ↓
Step 1: Nano Banana (Structure Removal)
        ↓
[Bare Land Reference Image]
        ↓
[Bare Land (Ref 1)] + [Original Property (Ref 2)]
        ↓
Step 2: Omni Flash (Sequential Animation)
        ↓
[8-Second Reveal Video]
```

### **The Two-Step Progression**

**Step 1: Land Deconstruction (Nano Banana)**

- **Input**: Final photo of completed property
- **Execution**: AI strips away all architectural structures, paving, walls, artificial landscaping
- **Preservation**: Maintains exact frame, lens compression, angle, environmental sky
- **Output**: Reference Image 1 (Bare Soil / Empty Plot)

**Step 2: Sequential Animation Construction (Omni Flash)**

- **Inputs**: Reference Image 1 (Bare Soil) at Position 1; Original Property Photo at Position 2
- **Execution**: AI places structural components onto Reference Image 1 in designated timeline stages
- **Camera Lock**: Camera angle strictly locked throughout entire sequence
- **Output**: 8-second MP4 architectural reveal video

---

## Prerequisites Checklist

### **Image Resolution**

- Minimum 1080p resolution required
- High-contrast, well-lit exterior photos yield highest structural precision
- Natural daylight or balanced dusk lighting preferred
- Avoid blurry, dim, or low-resolution source images

### **Crop Alignment**

- **Critical**: Reference Image 1 and Reference Image 2 must share identical pixel-for-pixel framing
- Any framing mismatch forces AI to warp or stretch architecture
- Generate Reference 1 directly from Reference 2 without intermediate edits
- Verify horizon line, vanishing points, and background elements align exactly

### **Aspect Ratio Consistency**

- Keep aspect ratios consistent across both steps
- 9:16 for vertical social media reels (Instagram, TikTok, YouTube Shorts)
- 16:9 for landscape presentations (YouTube, websites, TV displays)
- 1:1 for square social media posts (Instagram feed)

### **Environmental Preservation**

- When generating empty plot, erase building, fixtures, loose furniture
- **Preserve completely**: Ground surface (asphalt, concrete, gravel), sidewalks, curbs, background trees, sky
- Maintain all non-structural environmental elements
- Keep lighting direction and shadow angles unchanged

---

## Step-by-Step Implementation Guide

### **Step 1: Generating the Empty Plot (Nano Banana)**

1. **Access Tool**: Navigate to pollo.ai and select Nano Banana
2. **Upload Image**: Upload high-resolution property exterior photograph (becomes Reference 2)
3. **Apply Removal Prompt**: Use Step 1 prompt template (see Master Prompts section)
4. **Generate**: Execute structural removal
5. **Quality Control**: Verify output against checklist below before proceeding

#### **Quality Control Checklist for Step 1**

✓ **Camera Lock**: Horizon line and background environment unchanged?  
✓ **Perspective**: Distant background elements (sky, trees) remain in identical positions?  
✓ **Surface Replacement**: Building footprint replaced with clean natural soil matching local terrain?  
✓ **Framing Match**: Crop, aspect ratio, and pixel dimensions identical to original?  
✓ **No Artifacts**: Clean removal without warping, stretching, or visual glitches?

**⚠️ Critical**: If camera angle shifts or crop changes during Step 1, regenerate the image. Do NOT proceed to Step 2 with mismatched framing.

---

### **Step 2: Generating the Reveal Video (Omni Flash)**

1. **Access Tool**: Navigate to pollo.ai and select Omni Flash
2. **Set Duration**: Configure video duration to exactly 8 seconds
3. **Upload Reference 1**: Upload empty plot image (from Step 1) as starting frame at **0s mark**
4. **Upload Reference 2**: Upload original property photo as target frame at **6s mark**
5. **Input Main Prompt**: Paste complete Step 2 prompt into main prompt box
6. **Input Negative Prompt**: Paste negative prompt into dedicated field (or append with "Negative:")
7. **Execute Generation**: Process video (typically 2-10 minutes depending on queue)
8. **Download**: Retrieve video in highest available quality format

---

## Master Prompt Templates

### **Step 1 Prompt: Structure Removal (Nano Banana)**

```
Remove the entire house, building structures, outdoor furniture, driveway paving, and artificial landscaping from this scene. Clear the ground down to a bare, natural plot of land or bare soil.

Keep everything else in the background exactly as it is: identical camera angle, identical field of view, identical crop, identical framing, identical horizon line, and identical surrounding environment/trees in the distance. Fill the cleared area with natural dirt and ground texture matching the environment. Same lighting, same shadow direction, same time of day.
```

---

### **Step 2 Prompt: Construction Reveal Animation (Omni Flash)**

```
Static real estate architectural reveal, 8 seconds. Locked-off camera. The only camera movement allowed is a subtle continuous drift of a few degrees that eases to a stop at 6s, small enough that the composition stays recognisably the same shot from start to finish. No dolly, no zoom, no whip pan.

CAMERA LOCK - ANGLE AND PERSPECTIVE NEVER CHANGE: The camera position, height, angle, focal length, field of view, and perspective are exactly those of the reference images and stay fixed for the entire 8 seconds. All vanishing points, horizon lines, and background landscape elements remain in the same directions throughout. Do not reframe, re-angle, re-render, or re-photograph the scene from a different viewpoint. Do not change lens compression or widen the view. Do not reveal any part of the scene not visible in the reference images. The composition at every frame must overlay onto the reference images with the landscape in the same place.

HOW TO USE THE TWO REFERENCE IMAGES - READ CAREFULLY: The first reference image is the state of the land at 0s (bare land). The second reference image is the completed house at 6s. These are two discrete states, NOT two ends of a blend. Do not interpolate between them. Do not cross-fade, morph, or gradually transform the first image into the second. Do not compute intermediate frames by mixing the two images together. Instead, the first image stays exactly as it is, unchanged, and the architectural elements from the second image are placed onto it one group at a time until the house is complete. At every moment the frame shows the base land plus whichever structural elements have already arrived, never a partial blend of the two.

STRICT OBJECT INVENTORY - NOTHING NEW: The complete and final set of architectural elements and landscaping is defined entirely by the second reference image. Every wall, roof, window, door, pillar, light fixture, plant, path, and exterior feature that appears must already be visible in the second reference image, in the same position, at the same scale, in the same orientation, in the same material, colour, and finish. Do not add, invent, substitute, duplicate, restyle, or embellish anything. If an element is absent from the second reference image, it must never appear at any point in the video. The final frame must contain exactly the same architectural details as the second reference image, nothing more, nothing less.

ABSOLUTE LOCK: All surrounding background environment, sky, distant trees, terrain elevation, and lighting direction are identical in both reference images and must stay identical for the entire 8 seconds, never redrawn, warped, shifted, or reinterpreted.

REVEAL METHOD - MIXED MOTION: Architectural structures and landscape elements arrive in groups sequentially, never all at once. Every piece is fully opaque, complete, and correctly proportioned from the first frame it is visible. An element either does not exist yet or exists fully, there is no in-between state for any object.

POP-IN - foundational slabs and heavy walls: appear directly at final ground position with a slight firm settle.

DROP - wall panels, pillars, doors, and main structure: fall in from just above final positions and lock in place.

DESCEND - roof structures, upper floors, ceiling beams, and overhead elements: lower from above and settle onto the lower structure.

SETTLE - grass, lawn turf, stone pathways, and garden beds: drop onto ground level and flatten smoothly into place.

INSTANT - exterior lights, window glass, trim details, and small outdoor decor: appear instantly in place in a single frame.

Each arrival takes about 0.2 to 0.3 seconds. Contact shadows appear the moment an element lands or pops.

TIMELINE:
0-2s: The frame is exactly the first reference image (bare land), unchanged. Camera begins its slow drift.
2-3.5s: The foundation slab, main exterior walls, and primary structure from the second reference image arrive via POP-IN and DROP. Everything else in the frame is unchanged.
3.5-5s: The roof structure, upper levels, doors, windows, and pillars DESCEND into final position; major structural elements complete. Everything else is unchanged.
5-6s: Landscaping, pathways, exterior lighting, and small fixtures INSTANTLY appear and SETTLE into place; all contact shadows land; the camera drift eases to a stop. The frame now equals the second reference image exactly.
6-8s: The frame is exactly the second reference image (fully built house), completely static, no new elements, no repositioning, no further changes. Only gentle leaf movement and stable ambient light.

Photorealistic exterior architectural photography, natural daylight, no people.
```

---

### **Universal Negative Prompt**

```
changing camera angle, changing perspective, new viewpoint, reframing, re-angling, rotating camera, orbiting, arc shot, crane move, changing camera height, changing focal length, changing field of view, lens distortion, wide angle shift, perspective warp, shifting vanishing point, tilting horizon, revealing unseen areas of the scene, added structures, extra walls, invented objects, new trees, additional props, restyled house, changed exterior colour, changed wall material, objects not present in the reference, interpolation between reference images, blending two images, image morph, cross-fade between frames, gradual transformation, morphing, object morphing, shape shifting, transforming, geometry changing, slow growth, gradual scaling, growing from zero, unfolding, assembling from parts, dissolving in, fade in, fade out, cross dissolve, opacity transition, ghosting, double exposure, translucent objects, glowing particles, light streaks, magic effects, supernatural appearance
```

---

## Motion Physics & Timeline Architecture

### **Specialized Motion Paths by Material Category**

The construction sequence uses motion paths assigned to different architectural material categories to prevent default cross-fades or liquid morphing effects.

#### **Timeline Sequence Visualization**

```
0s ─────── 2s ───────────── 3.5s ─────────── 5s ────── 6s ─────── 8s
│          │                 │                │         │          │
│ Bare     │ Foundations &   │ Roofs, Upper  │ Paving, │ Fully   │ Static │
│ Soil     │ Walls           │ Levels, Doors │ Landsca-│ Built   │ Hold   │
│ Frame    │ (POP-IN & DROP) │ & Windows     │ ping &  │ House   │ Frame  │
│ Static   │                 │ (DESCEND)     │ Fixtures│ Frame   │        │
│          │                 │                │ (SETTLE │ Complete│        │
│          │                 │                │ &INSTANT│         │        │
└──────────┴─────────────────┴────────────────┴─────────┴─────────┴────────┘
```

### **Motion Type Definitions**

**POP-IN (Foundations & Ground Slabs)**

- Elements appear directly at final coordinates
- Undersized by 2% for two frames before settling to 100% scale
- Duration: Approximately 0.2 seconds
- Imparts visual weight to concrete bases

**DROP (Walls, Main Pillars & Doors)**

- Elements descend from slightly above resting position
- Lock into place with immediate contact shadows
- Short vertical travel distance (1-2 meters typical)
- Natural gravity-driven motion

**DESCEND (Roof Assemblies, Upper Floors & Cantilevers)**

- Overhead structures lower vertically into position
- Settle on top of previously placed lower structures
- Controlled lowering speed (realistic crane simulation)
- Maintains horizontal orientation throughout

**SETTLE (Paving, Lawn Turf & Gravel)**

- Ground covers drop from low height
- Flatten upon contact with terrain
- Dust or particle effect on impact (optional)
- Final settling takes 0.1-0.2 seconds

**INSTANT (Glass Panes, Wall Lights, House Numbers & Plants)**

- Trim items appear in single frame
- No spatial travel or motion blur
- Used for small-scale detail elements
- Synchronizes with final camera drift stop

---

## Troubleshooting & Failure Modes

### **1. Architectural Warping or Perspective Breathing**

**Symptoms:**

- Building appears to stretch, compress, or distort during animation
- Landscape elements shift position or scale
- Horizon line moves or tilts

**Root Cause:**

- Misaligned framing between Reference Image 1 and Reference Image 2
- Different pixel dimensions or aspect ratios
- Crop boundaries don't match exactly

**Solution:**

- Re-generate Reference Image 1 in Step 1
- Ensure source file used for Nano Banana is identical to Reference Image 2 uploaded to Omni Flash
- Verify both images have same resolution, aspect ratio, and file dimensions
- Check that horizon line and vanishing points align in both references

---

### **2. Melting or Liquid Morphing Structures**

**Symptoms:**

- Buildings appear to "grow" or "melt" into place
- Smooth cross-fade transitions between empty and built states
- Elements partially visible or semi-transparent during arrival

**Root Cause:**

- Video AI model defaulted to image interpolation/morphing
- "HOW TO USE THE TWO REFERENCE IMAGES" block missing or truncated

**Solution:**

- Ensure the complete anti-interpolation prompt block is intact
- Do not edit out or shorten the "READ CAREFULLY" section
- Verify "discrete states, NOT two ends of a blend" language is present
- Add stronger negative prompts against morphing/cross-fading

---

### **3. Unwanted Objects Appearing (Unplanned Decor/Trees)**

**Symptoms:**

- Extra furniture, plants, or decorative elements not in original photo
- Additional architectural features invented by AI
- Background elements duplicated or stylized

**Root Cause:**

- AI model attempted to auto-style or "improve" the scene
- "STRICT OBJECT INVENTORY" section missing or weak

**Solution:**

- Confirm "STRICT OBJECT INVENTORY" section is present and complete
- This restricts model strictly to elements visible in Reference Image 2
- Strengthen negative prompts with "no extra buildings, no additional trees, no invented objects"
- Use "nothing more, nothing less" language repeatedly

---

### **4. Everything Appears Simultaneously**

**Symptoms:**

- All architectural elements pop in at once around 2-3s mark
- No sequential assembly sequence
- Timeline completely ignored

**Root Cause:**

- Prompt length exceeded model context limits
- Timeline instructions skipped or truncated during processing

**Solution:**

- Trim non-essential descriptions from prompt
- Remove fine motion detail descriptions while maintaining core blocks
- Keep "CAMERA LOCK," "HOW TO USE," and "STRICT OBJECT INVENTORY" sections intact
- Preserve timeline structure but simplify component descriptions

---

### **5. Camera Angle Changes or Rotates**

**Symptoms:**

- Camera perspective shifts during animation
- Viewpoint appears to orbit or crane
- Framing changes noticeably

**Root Cause:**

- Camera lock instructions too weak or missing
- Drift descriptor interpreted as permission to move freely

**Solution:**

- Verify "CAMERA LOCK - ANGLE AND PERSPECTIVE NEVER CHANGE" is at top of prompt
- Add multiple repetitions of "stay fixed for the entire 8 seconds"
- Reduce drift intensity in descriptor ("subtle" vs "slight" vs "minimal")
- Add explicit negative prompts against camera movement types

---

### **6. Background Environment Changes**

**Symptoms:**

- Sky gradients shift or clouds move unnaturally
- Trees change position or appearance
- Lighting direction or quality alters

**Root Cause:**

- "ABSOLUTE LOCK" section not enforced
- Environmental elements being regenerated instead of preserved

**Solution:**

- Strengthen "ABSOLUTE LOCK" language
- List specific environmental elements that must stay frozen
- Add "never redrawn, warped, shifted, or reinterpreted"
- Include negative prompts against environment changes

---

## Best Practices for Optimal Results

### **Source Image Selection**

- Choose high-resolution daytime photography (minimum 1080p, 4K preferred)
- Ensure clear structural edges and details
- Avoid extreme angles (prefer straight-on or slight angle views)
- Select images with clean, uncluttered backgrounds
- Natural lighting preferred over artificial or mixed lighting
- Minimal atmospheric haze or fog
- Crisp shadows that define structure clearly

### **Reference Image Preparation**

- Always generate Reference 1 from Reference 2 without intermediate steps
- Maintain exact pixel dimensions between both references
- Preserve all metadata and color space information
- Use high-quality inpainting/removal tools (Nano Banana recommended)
- Verify clean removal with no visible artifacts or seams
- Check that all non-structural elements remain completely intact
- Test alignment by overlaying both images in photo editor

### **Prompt Optimization**

- Never truncate critical instruction blocks
- Preserve exact structure of "CAMERA LOCK," "HOW TO USE," "STRICT OBJECT INVENTORY," "TIMELINE"
- Trim only decorative or redundant descriptive language if token limits reached
- Maintain negative prompt in dedicated field or clearly marked section
- Test with single property type first before batch processing
- Keep backup copies of working prompts for iterative refinement

### **Platform Settings**

- Use Omni Flash or equivalent dual-reference capable platform
- Set duration to exactly 8 seconds (no variation)
- Upload references at correct timing marks (0s and 6s precisely)
- Verify aspect ratio matches source images before generation
- Check that both references loaded successfully (preview thumbnails)
- Monitor generation queue status and estimated completion time

### **Quality Control Post-Generation**

- Verify final frame (8s) matches Reference 2 exactly
- Check that environment remains static throughout entire sequence
- Confirm discrete arrival pattern (not morphing/fading)
- Validate appropriate motion types used for each element type
- Ensure camera perspective stays locked (no drift beyond subtle)
- Check no extra objects or hallucinations appeared
- Review shadow consistency and realism

---

## Advanced Techniques

### **Multi-Property Batch Processing**

- Create Reference 1 images for multiple properties in batch
- Maintain consistent naming convention (property-name_ref1.jpg, property-name_ref2.jpg)
- Use same prompt template with minimal adjustments
- Process similar property types together (residential vs commercial)
- Monitor for consistent quality across batch

### **Seasonal Variations**

- Generate multiple Reference 1 images with seasonal environmental changes
- Keep building footprint identical, vary background foliage/sky
- Create winter, spring, summer, fall variants of same property
- Useful for showing property in different seasons

### **Time-of-Day Variations**

- Capture or generate golden hour, midday, dusk variants
- Maintain exact framing and structure between time variants
- Requires re-shooting or advanced lighting manipulation
- Creates dramatic mood variations for same property

### **Custom Motion Timing**

- Adjust timeline ratios for emphasis
- Extend foundation phase for dramatic base establishment (0-2s empty, 2-4.5s foundation)
- Or rapid construction with longer hold (0-1.5s empty, 1.5-5s build, 5-8s hold)
- Maintain 8-second total duration for consistency

### **Property Type Customization**

Adjust motion types based on construction style:

**Residential Homes:**

- Heavy use of DROP for wood frame walls
- SETTLE for landscaping and lawn
- INSTANT for decorative trim and lights

**Commercial Buildings:**

- POP-IN for steel frame structure
- DESCEND for roof assemblies and canopies
- DROP for glass curtain walls

**High-Rise Properties:**

- Sequential floor-by-floor POP-IN
- DESCEND for rooftop mechanical equipment
- Extended timeline (may require longer animation)

---

## Property Type Examples & Variations

### **Single-Family Residential**

- Foundation slab appears first (POP-IN)
- Wood or concrete frame walls rise (DROP)
- Roof structure descends into place (DESCEND)
- Windows and doors install (DROP/INSTANT)
- Landscaping and pathways settle (SETTLE)
- Exterior lights and details (INSTANT)

### **Multi-Story Apartment Complex**

- Ground floor foundation and walls (POP-IN)
- Second floor structure builds on top (DROP)
- Third/fourth floors if applicable (DROP sequentially)
- Roof and balconies descend (DESCEND)
- Exterior cladding and windows (DROP/INSTANT)
- Landscaping and parking areas (SETTLE)

### **Commercial Storefront**

- Foundation and main structural walls (POP-IN)
- Large glass windows and doors (DROP)
- Signage and branding elements (DESCEND/INSTANT)
- Outdoor seating or displays (DROP/SETTLE)
- Lighting fixtures and details (INSTANT)

### **Modern Cafe/Restaurant**

- Base structure and walls (POP-IN)
- Awnings or overhead structures (DESCEND)
- Outdoor furniture and tables (DROP)
- Plants and landscaping elements (SETTLE)
- Menu boards and decorative signage (INSTANT)

---

## Output Specifications

### **Technical Output**

- **Duration**: 8 seconds (fixed)
- **Resolution**: Matches input (typically 1920x1080 or higher)
- **Frame Rate**: 24fps or 30fps
- **Format**: MP4 (H.264) or similar
- **File Size**: Varies by resolution and compression (typically 5-20MB)

### **Quality Indicators**

- Final frame matches Reference 2 exactly
- Environment remains static throughout
- Discrete component arrivals (no morphing/melting)
- Appropriate motion types for each element category
- Smooth camera drift with ease-out at 6s
- No warping or perspective shift
- No extra objects or hallucinations
- Realistic shadows that sync with element arrivals

### **Use Case Deliverables**

- **Social Media**: 8-second standalone clip (9:16 vertical optimal)
- **Marketing**: Can be extended with intro/outro graphics
- **Presentations**: Loop-ready (last frame stable for seamless loop)
- **Portfolio**: High-resolution export for showreel
- **Website**: Embed-ready MP4 for property listings

---

## Related Files

- See also: [architectural-landmark-reveal-animation.md](./architectural-landmark-reveal-animation.md) for iconic landmark reveal techniques
- See also: [architectural-animations-construction-timelapse.md](./architectural-animations-construction-timelapse.md) for traditional construction sequence animations
- See also: [architectural-animations-explosive-construction.md](./architectural-animations-explosive-construction.md) for dramatic explosive assembly effects

---

## Source Reference

Based on **AI Property Construction Reveal Workflow** by efficient-mink-952 (Notion).  
Original documentation: https://efficient-mink-952.notion.site/AI-Property-Construction-Reveal-Workflow-3b79502993ae80e493f0daeffa8204ae

Adapted for the A7 ai.prompts library structure with expanded troubleshooting guidance, best practices, property type variations, and platform integration details.
