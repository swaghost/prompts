# AI Property Construction Reveal Workflow

## Executive Summary

Create photorealistic 8-second AI property construction animations where bare land seamlessly transforms into a fully built architectural project—perfect for real estate marketing, property development showcases, and architectural presentations without complex 3D modeling or video editing software.

**Platform:** Pollo.ai (Nano Banana + Omni Flash)  
**Duration:** 8 seconds  
**Method:** Two-step inverted generation (deconstruction → reconstruction)  
**Aesthetic:** Broadcast-quality architectural reveal with discrete component assembly

---

## Core Operational Mechanics

### The Inverted Generation Principle

Rather than creating a building from nothing, this workflow **establishes the destination first and reconstructs the origin second**.

**Traditional Approach:**  
❌ Generate building construction from scratch

**Inverted Approach:**  
✅ Start with finished building → Remove structure → Animate reassembly

---

### Workflow Diagram

```
[Original Property Photo]
         ↓
Step 1: Nano Banana (Structure Removal)
         ↓
[Bare Land Reference Image] (Ref 1)
         ↓
[Bare Land (Ref 1)] + [Original Property (Ref 2)]
         ↓
Step 2: Omni Flash (Dual-Reference Animation)
         ↓
[8-Second Construction Reveal Video]
```

---

## The Two-Step Framework

### Step 1: Land Deconstruction (Nano Banana)

**Input:** Final photo of completed property

**Execution:**
- AI strips away all architectural structures
- Removes paving, walls, artificial landscaping
- Maintains exact frame, lens compression, angle
- Preserves environmental sky and background

**Output:** Reference Image 1 (Bare Soil / Empty Plot)

**Critical:** Camera angle, framing, and background must remain 100% identical

---

### Step 2: Sequential Animation Construction (Omni Flash)

**Inputs:**
- Reference Image 1 (Bare Soil) → Position 1 (0s mark)
- Original Property Photo → Position 2 (6s mark)

**Execution:**
- Places structural components onto bare land
- Discrete timeline stages (not cross-fade)
- Camera angle strictly locked
- Elements appear fully opaque (never partial blend)

**Output:** 8-second MP4 architectural reveal video

**Critical:** References must share pixel-perfect identical framing

---

## Technical Requirements & Software Setup

### Platform Access

**Pollo.ai Tools:**
- **Nano Banana:** Object & structure removal engine (Step 1)
- **Omni Flash:** Video generation engine (Step 2)

**Why These Tools:**
- Nano Banana preserves perspective, focal length, lighting better than standard image editors
- Omni Flash accepts dual reference inputs with precise prompt-based motion controls

---

### Prerequisites Checklist

**Image Resolution:**
- Minimum: 1080p resolution
- Recommended: High-contrast, well-lit exterior photos
- Best: 4K for maximum detail

**Crop Alignment:**
- Reference 1 and Reference 2 must share **identical pixel-for-pixel framing**
- No re-cropping between steps
- No resizing or aspect ratio changes

**Aspect Ratio:**
- 9:16 (vertical - social media reels)
- 16:9 (landscape - presentations)
- 1:1 (square - Instagram)
- **Keep consistent across both steps**

**Photo Quality:**
- Sharp focus
- Clear architectural details
- Good natural lighting
- Straight-on or slight angle shot
- Minimal lens distortion

---

## Step-by-Step Implementation Guide

### Step 1: Generating the Empty Plot (Nano Banana)

**Process:**

1. **Access Nano Banana on pollo.ai**

2. **Upload Property Photo:**
   - High-resolution exterior photograph
   - Final completed building state
   - This becomes Reference Image 2

3. **Apply Structural Removal Prompt:**
   ```
   Remove the entire house, building structures, outdoor furniture, driveway paving, and artificial landscaping from this scene. Clear the ground down to a bare, natural plot of land or bare soil. Keep everything else in the background exactly as it is: identical camera angle, identical field of view, identical crop, identical framing, identical horizon line, and identical surrounding environment/trees in the distance. Fill the cleared area with natural dirt and ground texture matching the environment. Same lighting, same shadow direction, same time of day.
   ```

4. **Verify Output Against Quality Control Checklist**

---

#### Quality Control Checklist for Step 1

**Before proceeding to Step 2, verify:**

✅ **Camera Lock:**  
- Horizon line unchanged?
- Background environment identical?

✅ **Perspective:**  
- Distant background elements (sky, trees) in identical positions?

✅ **Surface Replacement:**  
- Building footprint replaced with clean natural soil?
- Terrain matches local environment?

✅ **Framing:**  
- Crop dimensions exactly the same?
- No shift in composition?

**⚠️ CRITICAL:** If camera angle shifts or crop changes during Step 1, **regenerate the image**. Do NOT proceed to Step 2 with mismatched framing—this causes architectural warping.

---

### Step 2: Generating the Reveal Video (Omni Flash)

**Process:**

1. **Access Omni Flash on pollo.ai**

2. **Set Video Duration:**
   - **8 seconds** (fixed)

3. **Upload References:**
   - **Reference Image 1** (emptied land from Step 1) → Starting frame (0s)
   - **Reference Image 2** (original property photo) → Target frame (6s)

4. **Input Main Prompt:**
   - Paste primary construction reveal prompt (see Section 5)

5. **Input Negative Prompt:**
   - Paste into designated negative prompt field
   - Or append to main prompt with "Negative:" prefix

6. **Execute Generation**

7. **Review Output:**
   - Check camera lock
   - Verify discrete assembly (no morphing)
   - Confirm final frame matches Reference 2

---

## Primary Master Prompt Set

### Step 1 Prompt: Structure Removal (Nano Banana)

```
Remove the entire house, building structures, outdoor furniture, driveway paving, and artificial landscaping from this scene. Clear the ground down to a bare, natural plot of land or bare soil. Keep everything else in the background exactly as it is: identical camera angle, identical field of view, identical crop, identical framing, identical horizon line, and identical surrounding environment/trees in the distance. Fill the cleared area with natural dirt and ground texture matching the environment. Same lighting, same shadow direction, same time of day.
```

**Key Elements:**
- Remove all human-made structures
- Preserve camera perspective 100%
- Maintain background environment
- Replace with natural terrain
- Match lighting conditions

---

### Step 2 Prompt: Construction Reveal Animation (Omni Flash)

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

Negative: changing camera angle, changing perspective, new viewpoint, reframing, re-angling, rotating camera, orbiting, arc shot, crane move, changing camera height, changing focal length, changing field of view, lens distortion, wide angle shift, perspective warp, shifting vanishing point, tilting horizon, revealing unseen areas of the scene, added structures, extra walls, invented objects, new trees, additional props, restyled house, changed exterior colour, changed wall material, objects not present in the reference, interpolation between reference images, blending two images, image morph, cross-fade between frames, gradual transformation, morphing, object morphing, shape shifting, transforming, geometry changing, slow growth, gradual scaling, growing from zero, unfolding, assembling from parts, dissolving in, fade in, fade out, cross dissolve, opacity transition, ghosting, double exposure, translucent objects.
```

---

## Motion Physics & Timeline Architecture

### Timeline Sequence Breakdown

```
0s ------- 2s ------------------- 3.5s ------------------ 5s -------- 6s ------- 8s
|          |                     |                        |          |          |
| Bare Soil| Foundations &       | Roofs, Upper Levels,   | Paving,  | Fully    | Static  |
| Frame    | Walls               | Doors & Windows        |Landscape | Built    | Hold    |
| Static   | (POP-IN & DROP)     | (DESCEND)              | Fixtures | House    | Frame   |
|          |                     |                        |(SETTLE & | Frame    |         |
|          |                     |                        | INSTANT) | Complete |         |
```

---

### Motion Type Definitions

#### POP-IN (Foundations & Ground Slabs)

**Use For:**
- Foundation slabs
- Concrete bases
- Heavy ground-level walls

**Effect:**
- Elements appear directly at final coordinates
- Undersized by 2% for two frames
- Settles to 100% scale
- Duration: ~0.2 seconds

**Visual Weight:**
- Imparts sense of mass to concrete bases
- Firm settle upon arrival
- Immediate contact shadows

---

#### DROP (Walls, Main Pillars & Doors)

**Use For:**
- Exterior wall panels
- Main structural pillars
- Door frames
- Mid-level structures

**Effect:**
- Descends from slightly above resting position
- Locks into place upon contact
- Immediate shadow formation

**Motion Path:**
- Short vertical travel (just above final position)
- Quick lock-in
- Duration: ~0.2-0.3 seconds

---

#### DESCEND (Roof Assemblies, Upper Floors & Cantilevers)

**Use For:**
- Roof structures
- Upper story floors
- Ceiling beams
- Overhead architectural elements
- Cantilevers and overhangs

**Effect:**
- Lowers vertically from above
- Settles onto previously placed lower structures
- Creates top-down assembly logic

**Motion Path:**
- Longer vertical travel than DROP
- Gentle descent
- Settles with weight
- Duration: ~0.3 seconds

---

#### SETTLE (Paving, Lawn Turf & Gravel)

**Use For:**
- Grass and lawn turf
- Stone pathways
- Gravel driveways
- Garden beds
- Ground cover elements

**Effect:**
- Drops from low height
- Flattens smoothly upon contact
- Integrates with terrain

**Motion Path:**
- Short drop to ground level
- Spreads/flattens on impact
- Natural ground-covering behavior

---

#### INSTANT (Glass Panes, Wall Lights, House Numbers & Plants)

**Use For:**
- Window glass
- Exterior lighting fixtures
- House numbers/address
- Small decorative plants
- Trim details and accents

**Effect:**
- Appears in single frame
- No spatial travel
- Instant materialization

**Visual Purpose:**
- Adds finishing touches
- Detail elements that don't need motion
- Final polish items

---

### Motion Assignment Strategy

**Order of Construction (Physical Logic):**

1. **Ground Level First (2-3.5s):**
   - Foundation → Walls → Base Structure
   - POP-IN and DROP motions
   - Establishes building footprint

2. **Upper Structures Second (3.5-5s):**
   - Roofs → Upper Floors → Overhangs
   - DESCEND motions
   - Builds on foundation

3. **Finishing Elements Last (5-6s):**
   - Landscaping → Pathways → Lights → Details
   - SETTLE and INSTANT motions
   - Completes the property

---

## Critical Prompt Blocks (Do Not Modify)

### 1. CAMERA LOCK Block

**Purpose:** Prevents perspective breathing and warping

**Critical Language:**
- "Camera position, height, angle, focal length stay fixed"
- "All vanishing points remain in same directions"
- "Composition must overlay onto reference images"

**Why It Matters:**  
Without strict camera lock instructions, AI will attempt to regenerate scene from different angles, causing warping.

---

### 2. HOW TO USE THE TWO REFERENCE IMAGES Block

**Purpose:** Prevents interpolation/morphing

**Critical Language:**
- "Two discrete states, NOT two ends of a blend"
- "Do not interpolate between them"
- "First image stays exactly as it is, unchanged"
- "Never a partial blend of the two"

**Why It Matters:**  
Default AI behavior is to cross-fade/morph between images. This block forces discrete component placement.

---

### 3. STRICT OBJECT INVENTORY Block

**Purpose:** Prevents AI from adding extra elements

**Critical Language:**
- "Defined entirely by the second reference image"
- "Do not add, invent, substitute, duplicate, restyle"
- "Final frame must contain exactly the same details"

**Why It Matters:**  
AI will attempt to "improve" or "complete" scenes by adding decor, trees, or embellishments not in original photo.

---

### 4. ABSOLUTE LOCK Block

**Purpose:** Freezes background environment

**Critical Language:**
- "Background, sky, distant trees stay identical"
- "Never redrawn, warped, shifted, or reinterpreted"

**Why It Matters:**  
Ensures only the building animates while environment remains static.

---

## Troubleshooting & Failure Modes

### Problem 1: Architectural Warping or Perspective Breathing

**Symptoms:**
- Building appears to warp during animation
- Perspective shifts or wobbles
- Background environment distorts

**Root Cause:**
- Misaligned framing between Reference 1 and Reference 2
- Crop differences between steps

**Solution:**
- Re-generate Reference 1 in Step 1
- Ensure source file for Nano Banana is **identical** to Reference 2 uploaded to Omni Flash
- Verify pixel-perfect dimensional match
- Do not re-crop or resize between steps

---

### Problem 2: Melting or Liquid Morphing Structures

**Symptoms:**
- Building melts/morphs into place
- Walls appear to grow organically
- Cross-fade effect instead of discrete assembly
- Translucent/ghosting structures

**Root Cause:**
- Video AI defaulted to image interpolation
- "HOW TO USE THE TWO REFERENCE IMAGES" block missing or truncated

**Solution:**
- Ensure anti-interpolation block is **completely intact**
- Do not edit out discrete state language
- Verify "never a partial blend" language is present
- Check that motion types (POP-IN, DROP, DESCEND) are specified

---

### Problem 3: Unwanted Objects Appearing (Unplanned Decor/Trees)

**Symptoms:**
- Extra trees appear that weren't in original photo
- Additional furniture or decor materializes
- Landscaping elements not in Reference 2
- Style changes to building exterior

**Root Cause:**
- AI model auto-styling the scene
- "STRICT OBJECT INVENTORY" section missing

**Solution:**
- Confirm STRICT OBJECT INVENTORY block is present
- Ensure "nothing more, nothing less" language included
- Strengthen negative prompt with "added structures, extra walls, invented objects"
- Verify Reference 2 clearly shows all desired elements

---

### Problem 4: Everything Appears Simultaneously

**Symptoms:**
- All architectural elements appear at once
- No sequential assembly
- Timeline skipped
- Instant full building

**Root Cause:**
- Prompt length exceeded model context limits
- Timeline instructions truncated or ignored

**Solution:**
- Trim non-essential descriptions
- Prioritize critical blocks: CAMERA LOCK, HOW TO USE IMAGES, STRICT OBJECT INVENTORY
- Keep TIMELINE block but simplify motion descriptions
- Remove verbose explanations while keeping core instructions

---

### Problem 5: Camera Movement Too Aggressive

**Symptoms:**
- Camera zooms or pans noticeably
- Composition changes significantly
- Scene appears re-framed

**Root Cause:**
- Camera drift language too strong
- Default camera behavior overriding instructions

**Solution:**
- Emphasize "subtle," "minimal," "a few degrees"
- Add "composition stays recognisably the same shot"
- Strengthen "No dolly, no zoom, no whip pan"
- Consider removing camera drift entirely for maximum stability

---

### Problem 6: Background Environment Changes

**Symptoms:**
- Sky color shifts
- Distant trees move or change
- Lighting direction changes
- Surrounding landscape warps

**Root Cause:**
- ABSOLUTE LOCK block insufficient
- Background not preserved from Reference 1

**Solution:**
- Ensure "background environment stay identical" language present
- Verify Reference 1 preserved background perfectly
- Add to negative prompt: "changing sky, altered background, warped landscape"

---

### Problem 7: Final Frame Doesn't Match Reference 2

**Symptoms:**
- Completed building looks different from original
- Colors changed
- Elements missing or repositioned
- Details altered

**Root Cause:**
- AI took creative liberties
- Object inventory not enforced

**Solution:**
- Strengthen "final frame equals reference image exactly" language
- Verify Reference 2 image is high-quality and clear
- Ensure STRICT OBJECT INVENTORY block intact
- Add specific color/material descriptions if needed

---

## Advanced Techniques

### Multi-Property Developments

**For Multiple Buildings:**
- Ensure all structures visible in Reference 2
- Stagger assembly: Building 1 (2-3.5s), Building 2 (3.5-5s)
- Maintain logical construction order

**Timeline Adjustment:**
```
2-3s: First building foundation and walls
3-4s: First building roof, second building foundation
4-5s: Second building complete
5-6s: Landscaping and shared amenities
```

---

### Commercial Properties

**Large Structures:**
- May need more complex motion sequencing
- Consider splitting DESCEND phase for multi-story buildings:
  - 3.5-4.5s: Floors 1-3
  - 4.5-5.5s: Floors 4-6 + roof
  - 5.5-6s: Finishing details

**Emphasis Elements:**
- Signage (INSTANT at 5-6s)
- Parking lots (SETTLE at 5-6s)
- Landscaped entryways (SETTLE sequence)

---

### Seasonal Variations

**Adapt Reference Images:**
- **Spring/Summer:** Lush green landscaping, vibrant gardens
- **Fall:** Autumn foliage colors, fallen leaves
- **Winter:** Snow coverage on roof and ground

**Prompt Adjustments:**
- Specify seasonal ground texture in Step 1
- Maintain seasonal consistency between references
- Adjust lighting descriptions (warm summer vs. cool winter light)

---

### Dramatic Lighting

**Golden Hour:**
- Shoot Reference 2 during golden hour
- Warm sunset lighting on building facade
- Long shadows for dramatic effect

**Blue Hour:**
- Twilight photography
- Exterior lights on (INSTANT appearance at 5-6s creates dramatic glow)
- Cool blue sky with warm interior glow

**Overcast:**
- Even, soft lighting
- Reduces shadow complexity
- Easier for AI to maintain consistency

---

## Use Cases & Applications

### Real Estate Marketing

**Property Developers:**
- Pre-construction sales visualization
- Show completed property before building exists
- Marketing materials for new developments
- Investor presentations

**Real Estate Agents:**
- Listing video enhancements
- Social media property showcases
- Virtual tours opening sequences
- Property portfolio reels

**Benefits:**
- No 3D modeling required
- Photorealistic output
- Quick turnaround (minutes, not days)
- Cost-effective vs. traditional CGI

---

### Architectural Firms

**Project Presentations:**
- Client proposal videos
- Design concept reveals
- Before/after transformations
- Portfolio showcase pieces

**Competition Submissions:**
- Dynamic project presentations
- Engaging visual narratives
- Professional broadcast quality

---

### Construction Companies

**Progress Documentation:**
- Reverse sequence (completed → bare land)
- Show project scope dramatically
- Investor updates
- Website/social media content

**Marketing Materials:**
- Capability demonstrations
- Brand storytelling
- Commercial video content

---

### Social Media Content

**Instagram Reels:**
- 9:16 vertical format
- Engaging property reveals
- High shareability
- Viral potential

**TikTok:**
- Before/after property transformations
- Real estate content creation
- Behind-the-scenes development

**YouTube:**
- Property tour intros
- Real estate channel content
- Documentary segments

**LinkedIn:**
- Professional development showcases
- B2B marketing
- Industry thought leadership

---

## Technical Specifications

### Input Requirements

**Reference Image 2 (Original Property):**
- Resolution: 1080p minimum, 4K recommended
- Format: JPG, PNG
- Lighting: Bright natural daylight preferred
- Angle: Straight-on or slight angle (avoid extreme perspectives)
- Focus: Sharp throughout
- Composition: Property centered, clear surroundings visible

**Reference Image 1 (Bare Land - Generated):**
- Must match Reference 2 dimensions exactly
- Identical crop and framing
- Same aspect ratio
- No color correction or adjustments between steps

---

### Output Specifications

**Video Output:**
- Duration: 8 seconds (fixed)
- Frame Rate: Platform default (typically 24-30fps)
- Resolution: Matches input (1080p or 4K)
- Format: MP4
- Quality: High bitrate

**Aspect Ratios:**
- 16:9 (landscape) - Presentations, YouTube
- 9:16 (vertical) - Instagram, TikTok, mobile
- 1:1 (square) - Instagram feed
- 4:5 (portrait) - Instagram feed optimization

---

## Workflow Efficiency Tips

### Time Investment

**Total Time per Property:**
- Image selection/preparation: 5-10 minutes
- Step 1 (Nano Banana removal): 5-10 minutes
- Step 2 (Omni Flash animation): 15-30 minutes
- Review and refinement: 10-15 minutes
- **Total: 35-65 minutes per property**

**Batch Processing:**
- Prepare multiple properties in Step 1
- Queue multiple animations in Step 2
- Process 3-5 properties in 2-3 hours

---

### Cost Considerations

**Platform Credits:**
- Check Pollo.ai current pricing
- Nano Banana: Typically 1 credit per removal
- Omni Flash: 2-4 credits per 8-second video
- Budget 3-5 credits per completed property reveal

**Quality vs. Cost:**
- First generation often successful with good references
- May need 1-2 refinements for perfection
- Higher resolution = slightly higher cost but better results

---

## Quick Reference Checklist

### Before Starting

- ☐ High-quality property photo selected (Reference 2)
- ☐ Bright, clear lighting
- ☐ Sharp focus throughout
- ☐ Property centered in frame
- ☐ Minimal lens distortion
- ☐ Aspect ratio decided (9:16, 16:9, 1:1)

---

### Step 1: Nano Banana (Structure Removal)

- ☐ Original property photo uploaded
- ☐ Structure removal prompt pasted
- ☐ Generation complete
- ☐ Camera angle unchanged (verify horizon line)
- ☐ Background environment identical
- ☐ Building replaced with natural terrain
- ☐ Image saved as Reference 1
- ☐ Dimensions match original exactly

---

### Step 2: Omni Flash (Animation)

- ☐ Duration set to 8 seconds
- ☐ Reference 1 uploaded to 0s position
- ☐ Reference 2 uploaded to 6s position
- ☐ Both references have identical framing (verified)
- ☐ Main construction reveal prompt pasted
- ☐ Negative prompt pasted
- ☐ All critical blocks present (CAMERA LOCK, HOW TO USE IMAGES, STRICT OBJECT INVENTORY)
- ☐ Timeline section intact
- ☐ Motion types specified (POP-IN, DROP, DESCEND, SETTLE, INSTANT)

---

### After Generation

- ☐ Camera remains locked (no warping)
- ☐ Elements assemble discretely (no morphing/melting)
- ☐ Foundation appears first (2-3.5s)
- ☐ Roof/upper structures appear second (3.5-5s)
- ☐ Landscaping/details appear last (5-6s)
- ☐ Final frame matches Reference 2 exactly
- ☐ No extra objects added
- ☐ Background environment unchanged
- ☐ 6-8s section is static hold
- ☐ Contact shadows appear with elements

---

## Summary

Create stunning property construction reveal animations by:

1. Starting with completed property photo
2. Removing structure to create bare land (Nano Banana)
3. Animating discrete component assembly (Omni Flash)
4. Using mixed motion physics (POP-IN, DROP, DESCEND, SETTLE, INSTANT)
5. Maintaining strict camera lock
6. Preserving environment completely

**Result:** Broadcast-quality 8-second reveals showing photorealistic transformation from bare land to finished property—perfect for real estate marketing, architectural presentations, and property development showcases without expensive 3D modeling or complex video editing.
