# 8-Panel Character Sheet Generator – Multi-Angle Reference Sheet (9:16 Vertical)

## Description

A professional character sheet prompt that transforms a single reference image into a clean, studio-quality 8-panel reference sheet showing the same person from multiple angles and distances. Creates a vertical 9:16 format sheet with strict identity consistency across all panels: same face, hair, skin tone, body proportions, outfit, accessories, shoes, and overall appearance. Layout includes 4 full-body views (front, side, back, 3/4) and 4 close-up portraits (front, side, back of head, 3/4) on white studio background with photorealistic rendering, sharp focus, clean professional lighting, and zero text/watermarks. Perfect for fashion lookbooks, character reference for AI video generation, animation model sheets, 3D character design reference, casting portfolios, and maintaining visual consistency across multi-shot productions.

## Usage

Ideal for AI video character reference (Seedance, Runway, Pika, Kling AI with character lock), fashion lookbook creation, model casting sheets, animation character design reference, 3D modeling reference, game character concept sheets, costume design documentation, e-commerce model reference, influencer content planning, brand ambassador portfolios, virtual fitting room development, character consistency for serialized content, turnaround sheets for illustration, comic book character reference, film production continuity sheets, and any project requiring comprehensive multi-angle character documentation with strict identity preservation.

## Prerequisites

- **Source Image**: Single clear photo of person (full-body or portrait) with visible features, outfit, and styling
- **Identity Lock Requirement**: Person's face must be clearly visible for AI to maintain consistency
- **AI Platform**: Midjourney, DALL-E 3, Stable Diffusion, Leonardo AI, or any image generation platform supporting reference images
- **Reference Image Quality**: Higher quality source produces better consistency across panels
- **Outfit Visibility**: If creating full-body panels, source should show complete outfit or clearly describable styling

## Technical Specifications

- **Aspect Ratio**: 9:16 vertical (portrait orientation)
- **Layout**: 8-panel grid (4 panels × 2 rows full-body + 2 panels × 2 rows close-ups)
- **Background**: Pure white studio background, no gradients or shadows
- **Lighting**: Clean professional studio lighting, soft even illumination, no harsh shadows
- **Panel Count**: 8 total panels
  - **Top Row (4 panels)**: Full-body front view, full-body side profile, full-body back view, full-body 3/4 view
  - **Middle Row (2 panels)**: Front close-up portrait, side profile close-up
  - **Bottom Row (2 panels)**: Back of head/hair close-up, 3/4 close-up portrait
- **Style**: Photorealistic, premium fashion lookbook aesthetic
- **Focus**: Sharp focus throughout all panels, no blur
- **Skin Texture**: Realistic skin texture (not overly smoothed)
- **Text**: Zero text, captions, watermarks, or interface elements
- **Consistency Requirements**: Exact same person across all 8 panels (identity lock)

## Complete Character Sheet Prompt

```
Using the attached image as the strict reference, create a clean vertical 9:16 character sheet on a white studio background. No text, no captions, no watermark, no interface elements.

Keep the exact same person in all panels: same face, hair, skin tone, body proportions, outfit, accessories, shoes, and overall appearance. Do not change age, ethnicity, hairstyle, clothing, or identity.

Create 8 panels in a clean sheet layout:

Top row:
1. Full-body front view
2. Full-body side profile
3. Full-body back view
4. Full-body 3/4 view

Middle row:
5. Front close-up portrait
6. Side profile close-up

Bottom row:
7. Back of head / hair close-up
8. 3/4 close-up portrait

Style: photorealistic, clean studio lighting, sharp focus, realistic skin texture, premium fashion lookbook aesthetic, minimal background, highly consistent identity across all panels.
```

## Negative Prompt

```
Multiple different people, changed identity, different faces, inconsistent appearance, different hairstyles, different outfits, changed clothing, different accessories, age changes, ethnicity changes, text overlays, captions, watermarks, labels, panel numbers, grid lines, interface elements, UI elements, messy background, colored backgrounds, shadows on background, gradients, cluttered composition, blurry panels, out of focus, low resolution, distorted proportions, deformed anatomy, extra limbs, missing limbs, duplicate features, morphed faces, inconsistent skin tone, different makeup, changed hair color, different shoes, background distractions, props, furniture, outdoor settings, uneven lighting, harsh shadows, overexposed, underexposed, noise, grain, compression artifacts, cartoon style, illustration, sketch, painting, 3D render look, anime style, unrealistic proportions
```

## Layout Specifications

### Panel Arrangement (8 Total Panels)

**Top Row – Full-Body Views (4 Panels Horizontal)**

- **Panel 1**: Full-body front view (facing camera directly, feet together or slight stance, arms naturally at sides or slight pose)
- **Panel 2**: Full-body side profile (90° turn, facing left or right, full body visible head to toe)
- **Panel 3**: Full-body back view (180° turn, showing back of outfit and hairstyle from behind)
- **Panel 4**: Full-body 3/4 view (45° angle, between front and side, showing dimension)

**Middle Row – Portrait Close-Ups (2 Panels Horizontal)**

- **Panel 5**: Front close-up portrait (head and shoulders, direct eye contact, facial features clear)
- **Panel 6**: Side profile close-up (90° turn, profile from forehead to chin, ear visible)

**Bottom Row – Additional Close-Ups (2 Panels Horizontal)**

- **Panel 7**: Back of head / hair close-up (showing hairstyle from behind, hair texture and styling visible)
- **Panel 8**: 3/4 close-up portrait (45° angle portrait, cheek contour visible, dimensional face view)

### Identity Consistency Requirements

**Must Remain EXACTLY the Same Across All 8 Panels:**

- **Face**: Exact same facial features, facial structure, eye shape, nose, lips, chin
- **Hair**: Identical hairstyle, hair color, hair length, hair texture, styling
- **Skin Tone**: Exact same skin color, undertones, complexion
- **Body Proportions**: Same height, build, body type, proportions
- **Outfit**: Exact same clothing items, colors, patterns, fit, styling
- **Accessories**: Same jewelry, watches, belts, bags, hats, scarves, sunglasses
- **Shoes**: Identical footwear in all full-body panels
- **Makeup** (if applicable): Same makeup style, lip color, eye makeup
- **Age**: No aging or de-aging between panels
- **Ethnicity**: Must preserve exact ethnicity across all views
- **Expression**: Neutral or slight smile consistent across portrait panels

## Platform Recommendations

**Primary Platforms:**

**Midjourney v6.1** (Best for Character Sheets)

- Use `--cref` (character reference) with source image URL
- Add `--cw 100` for maximum character weight (strictest identity lock)
- Use `--ar 9:16` for vertical aspect ratio
- Prompt: Include "character sheet, multiple views, model sheet" keywords
- Strategy: Generate once, upscale favorite, use as new reference if consistency needs improvement

**DALL-E 3** (Good for Layout Control)

- Upload reference image and describe desired 8-panel layout
- Emphasize "same person in all panels, maintain exact identity"
- Request "professional model sheet" or "casting sheet"
- Good for clean backgrounds and structured layouts

**Stable Diffusion + ControlNet** (Advanced Control)

- Use OpenPose ControlNet to define exact poses for each panel
- Use Reference-Only or IP-Adapter for identity consistency
- Model recommendations: Realistic Vision, DreamShaper, Deliberate
- LoRA: Consider fashion photography or model sheet LoRAs
- Generate each panel separately with same seed + reference, then composite in Photoshop

**Leonardo AI** (Good Alternative)

- Upload reference image using "Image Guidance" feature
- Use PhotoReal mode for realistic rendering
- Prompt with "character turnaround sheet" keywords
- Adjust "Image Strength" slider for identity consistency

**Magnific AI** (For Upscaling Final Sheet)

- After generating 8-panel sheet, upscale for maximum detail
- Maintains consistency while adding fine texture
- Use "Cinematic" preset for fashion lookbook quality

**Secondary Platforms:**

- **Adobe Firefly** — Upload reference, generate character sheets with Adobe's consistency
- **Runway ML** — Can generate reference sheets, good for video projects
- **Scenario.gg** — Create custom character model with reference, generate multiple angles
- **Invoke AI** — Open-source with ControlNet support for precise control

## Use Cases

- **AI Video Character Reference** — Lock character identity for Seedance, Runway Gen-3, Pika Labs, Kling AI, Luma AI with consistent appearance across shots
- **Fashion Lookbook Creation** — Document complete outfit from all angles for e-commerce, catalogs, or brand presentation
- **Model Casting Sheets** — Comprehensive model portfolio showing versatility and range for casting directors
- **Animation Reference** — Character turnaround sheets for 2D/3D animators showing proportions and details from all angles
- **3D Character Modeling** — Reference images for 3D artists modeling characters in Blender, Maya, ZBrush
- **Game Character Design** — Concept art reference for game character creation showing front/side/back views
- **Costume Design Documentation** — Document complete costume from all angles for film, theater, or cosplay
- **Comic Book Character Reference** — Consistent character reference for comic artists maintaining continuity
- **Virtual Fashion** — Character sheets for virtual clothing try-on systems and digital fashion
- **Brand Ambassador Portfolios** — Professional presentation of brand representatives showing professional versatility
- **Influencer Content Planning** — Reference sheet for maintaining consistent appearance across content series
- **E-Commerce Model Reference** — Internal reference for product photography teams showing model from all angles
- **Continuity for Film/TV** — Production reference sheets for costume, makeup, and hair departments
- **Illustration Turnarounds** — Reference for illustrators drawing character from multiple perspectives
- **Virtual Fitting Rooms** — 3D avatar creation for online shopping experiences
- **Character Acting Reference** — Theater or film actors showing physical presence from multiple angles

## Quality Checklist

- [ ] Vertical 9:16 aspect ratio (portrait orientation)
- [ ] Exactly 8 panels visible (no more, no fewer)
- [ ] Pure white studio background (no gradients, shadows, or colored backgrounds)
- [ ] Zero text, captions, labels, or watermarks anywhere
- [ ] No interface elements, panel numbers, or grid lines
- [ ] Top row contains 4 full-body panels (front, side, back, 3/4)
- [ ] Middle row contains 2 close-up portraits (front, side profile)
- [ ] Bottom row contains 2 close-up panels (back of head, 3/4 portrait)
- [ ] Panel 1: Full-body front view clearly visible
- [ ] Panel 2: Full-body side profile (90° turn visible)
- [ ] Panel 3: Full-body back view (complete back visible)
- [ ] Panel 4: Full-body 3/4 view (45° angle visible)
- [ ] Panel 5: Front close-up portrait (head and shoulders, clear face)
- [ ] Panel 6: Side profile close-up (90° profile, ear visible)
- [ ] Panel 7: Back of head / hair close-up (hairstyle from behind)
- [ ] Panel 8: 3/4 close-up portrait (45° angle face)
- [ ] EXACT same face across all 8 panels (identity locked)
- [ ] Identical hairstyle in every panel (no style changes)
- [ ] Consistent hair color throughout (no color shifts)
- [ ] Same skin tone in all panels (no lightening/darkening)
- [ ] Identical body proportions across full-body panels
- [ ] Exact same outfit in all panels (no clothing changes)
- [ ] Same accessories visible where appropriate
- [ ] Identical shoes in all full-body panels
- [ ] Makeup consistent across all portrait panels (if applicable)
- [ ] No age changes between panels
- [ ] Ethnicity preserved exactly across all views
- [ ] Consistent expression (neutral or slight smile) in portrait panels
- [ ] Same jewelry visible in all relevant panels
- [ ] Photorealistic rendering quality throughout
- [ ] Clean professional studio lighting (even, soft)
- [ ] Sharp focus in all 8 panels (no blur)
- [ ] Realistic skin texture (not over-smoothed)
- [ ] Premium fashion lookbook aesthetic achieved
- [ ] Minimal background distractions (white only)
- [ ] No harsh shadows on subject or background
- [ ] Even illumination across all panels
- [ ] Professional photography quality
- [ ] High resolution output (suitable for printing or detailed viewing)
- [ ] No distorted proportions in any panel
- [ ] Proper anatomy in all full-body and close-up panels
- [ ] No extra or missing limbs
- [ ] No deformed features in any panel
- [ ] Hands look natural in full-body panels (if visible)
- [ ] Feet properly rendered in full-body panels
- [ ] Hair looks natural from all angles (not pasted or artificial)
- [ ] Clothing drapes naturally on body
- [ ] Outfit fits properly from all viewing angles
- [ ] Back view shows realistic clothing and hair from behind
- [ ] 3/4 views show proper dimensional perspective
- [ ] Side profiles show accurate side view proportions
- [ ] Close-ups maintain consistent facial features from originals
- [ ] Hair texture consistent between full-body and close-up panels
- [ ] Skin tone matches between distant and close views
- [ ] No compression artifacts or noise
- [ ] Clean panel edges (no bleeding between panels)
- [ ] Panels evenly spaced and aligned
- [ ] Professional grid layout (organized, clean)
- [ ] No duplicate panels (each angle unique)
- [ ] All 8 required angles present
- [ ] No camera distortion or lens effects
- [ ] Natural proportions (no fish-eye or wide-angle distortion)
- [ ] Color consistency across all panels
- [ ] White balance consistent throughout
- [ ] No color casts or tinting
- [ ] Professional color grading (clean, neutral)
- [ ] Suitable for professional use (portfolio, reference, production)

## Pro Tips

### Maximum Identity Consistency

- **Use High-Quality Reference**: The better your source image, the more consistent the AI can maintain identity. Use clear, well-lit photos with visible facial features.
- **Character Reference Weight**: In Midjourney, always use `--cw 100` for maximum character consistency. Lower values allow more variation.
- **Seed Locking**: If generating panels separately in Stable Diffusion, use the same seed + reference image for all panels to maintain consistency.
- **Face Lock First**: Some platforms (Seedance, Kling AI) require uploading a face reference. Create a clean front-facing portrait first, then use it as the face lock for all subsequent panels.

### Layout and Composition

- **Grid Generators**: Some AI platforms struggle with multi-panel layouts. Consider generating each panel separately at high quality, then compositing into 8-panel grid in Photoshop/Figma.
- **White Balance**: Request "pure white background RGB(255,255,255)" to ensure truly white background suitable for clean composition.
- **Panel Spacing**: If compositing manually, use consistent spacing between panels (e.g., 20-40px gaps) for professional appearance.
- **Alignment**: Ensure all full-body panels show feet at same baseline height for proper visual alignment.

### Professional Quality

- **Studio Lighting Standard**: Professional fashion photography uses soft, even lighting. Specify "soft studio lighting, no harsh shadows, even illumination."
- **Fashion Lookbook Aesthetic**: Reference "Zara lookbook," "H&M model sheet," or "fashion casting sheet" for specific professional styling.
- **Sharp Focus Throughout**: Request "sharp focus on all panels" to avoid AI blurring background panels while focusing on foreground.
- **Realistic Skin Texture**: Balance between too-smooth (fake) and too-textured (gritty). Request "natural skin texture, not over-smoothed."

### Technical Execution

- **Aspect Ratio Strategy**: Some platforms default to square. Always specify `--ar 9:16` or equivalent vertical portrait ratio.
- **Multi-Generation Approach**: If consistency is poor, generate 2-3 variations and composite best panels from each into final sheet.
- **Reference Multiple Times**: In DALL-E 3 or ChatGPT, re-upload reference image and explicitly state "use this exact person" in each generation attempt.
- **ControlNet for Poses**: Advanced users can create OpenPose skeletons for each of 8 panels to ensure exact pose control while maintaining identity.

### Platform-Specific Tips

**For Midjourney:**

- Upload reference to Discord first, get image URL
- Prompt: `[image URL] character sheet, 8 panels, model turnaround, full body views and close-up portraits, 9:16 vertical layout, white studio background, photorealistic --cref [same URL] --cw 100 --ar 9:16 --style raw --v 6.1`
- Use `--style raw` for more photorealistic results
- If consistency fails, try lower `--cw` values (70-90) for more flexibility

**For DALL-E 3:**

- Upload reference via ChatGPT
- Prompt: "Create a vertical 9:16 character reference sheet with 8 panels showing this exact person [describe key features from reference]. Include full-body front/side/back/3-4 views and portrait close-ups. White studio background, no text."
- If identity drifts, generate new sheet using best result as new reference

**For Stable Diffusion:**

- Model: Realistic Vision V6.0 or DreamShaper 8
- Sampler: DPM++ 2M Karras or Euler A
- Steps: 30-40
- CFG Scale: 7-8
- Use IP-Adapter or Reference-Only for identity consistency
- ControlNet: OpenPose for exact pose control
- Generate each panel at 768x1024, composite into 9:16 grid

**For Leonardo AI:**

- PhotoReal mode enabled
- Upload reference using "Image Guidance"
- Image Strength: 0.6-0.8 for balance between reference and prompt
- Prompt Elements: Medium (Photo), Style (Studio Portrait), Preset (Fashion Photography)

### Outfit Documentation Best Practices

- **Accessory Visibility**: Ensure accessories are clearly visible in at least 2 panels (front view + close-up)
- **Shoe Detail**: Full-body panels should show complete shoes - important for fashion documentation
- **Back Detail**: Back panel crucial for outfits with interesting back design (open back, unique patterns, cape, etc.)
- **Fabric Texture**: Close-ups should show fabric texture (denim weave, knit pattern, leather grain)
- **Layering**: If outfit has layers (jacket over shirt), ensure visible in front and 3/4 views

### Hair Documentation

- **Back View Critical**: Panel 7 (back of head close-up) shows hairstyle from behind - essential for full documentation
- **Hair Length**: Side profile (Panel 6) best shows hair length when worn down
- **Updos and Braids**: If complex hairstyle, back close-up panel shows construction details
- **Hair Texture**: Close-ups (Panels 5-8) should show realistic hair texture, individual strands, natural shine

### Common Issues & Solutions

**Problem: Inconsistent Face Between Panels**

- **Cause**: AI generating different people or features changing
- **Solution**: Use stronger character reference (`--cw 100`), generate fewer panels at once, or composite best consistent panels

**Problem: Different Outfits in Different Panels**

- **Cause**: AI "imagining" clothing not visible in reference
- **Solution**: Describe outfit explicitly in prompt ("wearing blue denim jacket, white t-shirt, black jeans, white sneakers")

**Problem: Text or Watermarks Appearing**

- **Cause**: AI training on stock photos with watermarks
- **Solution**: Emphasize "no text, no watermarks, clean panels" and add "text, watermark, captions" to negative prompt

**Problem: Messy Background or Shadows**

- **Cause**: AI adding environment or dramatic lighting
- **Solution**: Request "pure white studio background, no shadows on background, even lighting, minimal background"

**Problem: Wrong Aspect Ratio (Square Instead of Vertical)**

- **Cause**: Platform defaulting to square
- **Solution**: Explicitly specify `--ar 9:16` or "vertical portrait orientation" in prompt

**Problem: Missing Panels or Fewer Than 8**

- **Cause**: AI simplifying to fewer views
- **Solution**: Explicitly list "8 panels: 1. full-body front 2. full-body side..." in numbered format

**Problem: Blurry or Out-of-Focus Panels**

- **Cause**: AI focusing on center panels, blurring edges
- **Solution**: Request "sharp focus on all panels, no blur, high detail throughout entire image"

**Problem: Body Proportions Change Between Views**

- **Cause**: AI inconsistency in generating same person
- **Solution**: Lower prompt complexity, use seed locking, or specify "consistent body proportions, same height and build"

### Customization Options

**Different Panel Counts:**

- **4-Panel Basic**: Front, side, back, 3/4 (full-body only)
- **6-Panel Standard**: 4 full-body + 2 front/side portraits
- **8-Panel Complete**: As documented (most comprehensive)
- **12-Panel Extended**: Add expression variations, hand close-ups, detail shots

**Alternative Layouts:**

- **Horizontal 16:9**: Panels arranged horizontally for wide presentation
- **Square Grid**: 3×3 or 4×4 arrangement for social media
- **Circular Turnaround**: Character rotating 360° in animation-style turnaround

**Style Variations:**

- **Fashion Lookbook**: Current default - clean, professional, white background
- **Editorial Style**: More dramatic lighting, colored backgrounds
- **Catalog Style**: Multiple outfit variations of same person
- **Animation Model Sheet**: With construction lines and proportion guides
- **Casting Sheet**: Include name, measurements, agency info (add text in post-production)

**Pose Variations:**

- **Standard Neutral**: Default - natural standing pose, arms at sides
- **Fashion Pose**: More dynamic poses, hand on hip, weight shift
- **Athletic Stance**: For sportswear - active poses, movement
- **Sitting Variations**: Include seated views (chair, floor, stool)
- **Action Poses**: Running, jumping, reaching for dynamic reference

### Advanced Techniques

**Multi-Pass Workflow:**

1. Generate 8-panel sheet (may have inconsistencies)
2. Identify best panels with correct identity
3. Regenerate weak panels separately using best panel as reference
4. Composite perfect panels into final clean 8-panel sheet

**Identity Lock Strategy:**

1. Generate perfect front-facing portrait first
2. Use that portrait as character reference for full 8-panel sheet
3. Result maintains face from step 1 across all panels

**Upscaling Workflow:**

1. Generate 8-panel sheet at native AI resolution
2. Upscale entire sheet using Magnific AI or Topaz Gigapixel
3. Add subtle sharpening to all panels
4. Result: Ultra-high-resolution character sheet with fine detail

**Color Grading:**

- Use Lightroom/Photoshop to ensure consistent color across all panels
- Match white balance between panels
- Ensure skin tone perfectly consistent
- Adjust brightness/contrast so all panels have same exposure level

### Use in AI Video Generation

**For Seedance 2.5:**

- Upload front panel (Panel 5) as face reference
- Use full-body front panel (Panel 1) as body/outfit reference
- Character lock feature maintains consistency in generated video

**For Runway Gen-3 / Pika Labs:**

- Upload multiple angle panels as reference images
- AI learns character features from multiple views
- Better consistency in generated video motion

**For Kling AI:**

- Character lock requires clear front-facing photo (use Panel 5)
- Full-body reference (Panel 1) helps maintain outfit consistency
- Back panel (Panel 3) useful for shots showing character from behind

### Professional Presentation

- **Portfolio Format**: Export high-resolution PNG (300 DPI for print)
- **Digital Presentation**: 4K resolution (2160×3840 for 9:16)
- **Contact Sheet**: Add professional header with model name/info in Photoshop after generation
- **Casting Sheet**: Include measurements text overlay (add in post - not in AI generation)
- **Agency Format**: Follow specific agency guidelines for comp card layout

### Fashion Industry Standards

Character sheets should match industry expectations:

- **Model Comp Cards**: Similar to professional modeling composite cards (digitals)
- **Runway Casting**: Format similar to what casting directors review
- **E-Commerce**: Detailed enough for online retail use (all angles visible)
- **Brand Lookbooks**: Fashion brand seasonal lookbook quality
- **Catalog Photography**: Suitable for print catalog use

### Rights and Ethics

- **Model Release**: If using real person as reference, ensure you have rights to use their likeness
- **Commercial Use**: Verify platform terms allow commercial use of generated character sheets
- **AI Disclosure**: In professional contexts, disclose if character sheet is AI-generated vs. photographed
- **Identity Respect**: Never create character sheets impersonating real people without permission
- **Age Appropriate**: Ensure character age representation is appropriate for intended use
