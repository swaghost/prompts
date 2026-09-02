# Prompt Engineering Patterns & Techniques

## Overview

This document extracts common patterns, techniques, and best practices from professional AI image/video generation prompts.

---

## Core Structural Patterns

### 1. Technical Specifications Block

Every professional prompt includes precise technical parameters:

- **Aspect Ratio**: Vertical 4:5, Horizontal 3:2, Landscape 16:9, etc.
- **Resolution**: Exact pixel dimensions (e.g., 1920x1080 px)
- **Camera/Lens**: Specific equipment (Leica Q2, 50mm lens, Kodak Portra 400)
- **Composition**: Grid layouts (4×3, 2×2), viewing angles, framing

**Example:**

```
Aspect Ratio: Vertical 4:5
Camera: Leica Q2
Lens: 28mm
Resolution: 1920x1080 px
```

### 2. Progressive Detail Hierarchy

Structure prompts from general to specific:

1. **Category/Style** (opening context)
2. **Main Subject/Composition** (what and where)
3. **Detailed Elements** (clothing, props, environment)
4. **Technical Qualities** (lighting, texture, depth)
5. **Style Keywords** (aesthetic descriptors)
6. **Critical Avoidances** (what NOT to include)

### 3. Identity Preservation Protocols

For character consistency across multiple images:

- Explicit instruction to use reference image
- List exact features to preserve (face, proportions, skin tone, eyes)
- Warning against beautification or genericization
- Instruction not to merge or alter features

**Pattern:**

```
Use the uploaded [portrait/image] as strict identity reference.
Preserve exact recognizable [face/appearance]: natural [proportions/features],
[skin tone], [age], [distinctive characteristics].
Do NOT [merge faces/beautify/make generic].
```

### 4. Negative Prompting (Critical Avoidances)

Always include what NOT to generate:

- **Common Exclusions**: CGI, plastic skin, text, logos, people (when unwanted)
- **Quality Issues**: blurry details, garbled text, floating products
- **Style Violations**: beauty filters, oversized figures, duplicate views
- **Composition Issues**: cropped products, empty space, overlapping fragments

---

## Lighting Techniques

### 1. Directional Lighting Patterns

- **"Strong directional light passes through gaps"** - Creates drama
- **"Casting sharp horizontal bands"** - Geometric light patterns
- **"Bright white linear lights and warm golden-orange reflections"** - Mixed color temperatures

### 2. Natural Environmental Lighting

- **"Natural orange sunset light mixed with cool blue shadows"** - Time-of-day specificity
- **"Warm peach and amber sunset"** - Emotional warmth
- **"Neutral soft diffused lighting"** - Studio product photography
- **"Warm natural light"** - Architectural visualization

### 3. Studio Lighting

- **"Soft diffused light"** - Character/fashion photography
- **"Neutral soft diffused lighting"** - Product consistency
- **"Controlled reflections, natural contact shadows"** - Physical accuracy

---

## Composition Techniques

### 1. Camera Angles

- **Low Angle**: "Extremely low street-level angle, looking almost straight upward"
- **High Angle**: "Shot from a HIGH ANGLE looking down"
- **Eye Level**: "Framed from mid-torso up, slightly right of center"
- **Drone Perspective**: "Smooth luxury drone shot with gentle cinematic push"

### 2. Negative Space Usage

- **"Triangular wedge of open sky creates the negative space"** - Geometric composition
- **"Emphasizing a dramatic sense of confinement and towering verticality"** - Emotional impact

### 3. Scale Manipulation

- **"Colossal young woman... approximately 15-20 stories tall"** - Surreal scale
- **"Impossibly large in the urban environment"** - Out-of-bounds effect
- **"Foreshortening and high angle create surreal effect"** - Perspective distortion

### 4. Grid Layouts

- **4×3 Grid** (12 panels): Product consistency sheets
- **2×2 Grid** (4 quadrants): Character reference sheets
- **2×3 Sub-grids**: Detailed expression studies

---

## Realism & Detail Techniques

### 1. Photorealistic Descriptors

**Skin:**

- "Realistic skin texture, visible pores"
- "Natural skin texture and pores"
- "Authentic skin tones"
- "No plastic skin, no beauty-filter skin"

**Materials:**

- "Physically accurate materials"
- "Realistic hair and fabric"
- "True-to-life colors"
- "Natural texture"

**Technical:**

- "Deep depth of field"
- "Sharp edges and clear surface details"
- "Ultra-detailed reflections"
- "Every fragment sharp"

### 2. Imperfection as Authenticity

- **"Subtle unevenness in clothing"** - Realistic fabric behavior
- **"Slight imperfect framing"** - Documentary feel
- **"Natural hands"** - Avoiding AI hand artifacts
- **"Relaxed, imperfect posture"** - Anti-fashion-pose
- **"Gentle film grain"** - Analog texture
- **"Subtle motion blur in legs and clothing"** - Movement authenticity

### 3. Environmental Realism

- **"Small puddles on the road reflect warm orange sunset light"** - Environmental interaction
- **"Wet asphalt"** - Surface condition specificity
- **"Sea wind moves her blonde hair"** - Natural forces
- **"Several strands crossing her cheek"** - Realistic hair physics

---

## Motion & Animation Techniques

### 1. Transitional Moments

- **"Caught in a real, transitional movement"** - Not static pose
- **"Just turning toward each other after stepping from car"** - Mid-action
- **"Walking rhythm is slightly uneven"** - Natural gait
- **"Their bodies are caught in a real, transitional movement"** - Authentic motion

### 2. Progressive Transformation

**Blueprint to Building sequence:**

1. Empty land
2. Glowing blueprint lines appear
3. Blueprint rises and transforms to 3D
4. Walls grow, floor plates form
5. Materials gradually fill in
6. Landscaping grows naturally
7. Lights turn on
8. Final photorealistic scene

**Pattern: Gradual → Complete**

### 3. Camera Movement

- **"Gentle cinematic push"** - Slow zoom in
- **"Slight glide to showcase"** - Smooth lateral movement
- **"Handheld photography"** - Authentic documentary feel
- **Static to dynamic** - Evolution within shot

---

## Identity Consistency Strategies

### 1. Reference Image Protocol

```
Use uploaded [image/portrait] as:
- Only reference
- Strict identity reference
- Final design target and visual match
```

### 2. Feature Preservation Lists

Explicitly state what must remain identical:

- Face, proportions, skin tone, eyes
- Hairstyle, makeup, body proportions
- Outfit, accessories, shoes
- Shape, dimensions, color, materials, finish
- Logo, label, typography, hardware

### 3. Multi-View Consistency

**For Products:** 12 views showing same product from all angles
**For Characters:** Turnarounds, expressions, poses, detail crops
**For Architectural:** Same design across transformation phases

---

## Style & Aesthetic Patterns

### 1. Cinematic Aesthetic

Keywords that create cinematic quality:

- "Cinematic contrast"
- "Dramatic lighting"
- "Shallow depth of field"
- "Deep blacks"
- "Sharp horizontal bands of light and shadow"
- "Cinematic push or slight glide"

### 2. Documentary/Candid Aesthetic

Keywords for natural, unposed quality:

- "Candid color photograph"
- "Accidentally captured moment"
- "Documentary photography"
- "Handheld photography"
- "Neither person is posing"
- "Realistic handheld photography"

### 3. Studio/Commercial Aesthetic

Keywords for polished product imagery:

- "Professional studio product photography"
- "Neutral soft diffused lighting"
- "Controlled reflections"
- "Clean editorial layout"
- "Seamless background"
- "Ultra-high detail"

### 4. Architectural/Technical Aesthetic

Keywords for precision and professionalism:

- "Premium architectural visualization"
- "Professional architectural elevation"
- "Technical drawing"
- "Precise dimension lines"
- "Modern typography"
- "Clean, elegant motion"

---

## Emotional & Narrative Techniques

### 1. Expression Specificity

Don't just say "smiling" - be specific:

- "Calm, intense expression"
- "Curious, playful, or slightly mischievous"
- "Lively, teasing expression"
- "Subtle half-smile"
- "Faint amused expression"
- "Thoughtful and mildly annoyed"

### 2. Implied Narrative

Create story through details:

- "Just turning toward each other after stepping from car"
- "As if reacting to something she just said"
- "The moment feels accidentally captured during a real road trip"
- "Watching her with a subtle half-smile"

### 3. Environmental Storytelling

Setting details that add context:

- "Black vintage convertible"
- "Quiet coastal road during warm sunset"
- "Wet asphalt"
- "Small puddles reflecting sunset"

---

## Grid & Layout Patterns

### 1. Product Consistency Sheet (4×3 Grid)

**Row 1:** Primary views (front, 3/4 front, side, back)
**Row 2:** Additional views (opposite side, top, underside, hero)
**Row 3:** Detail crops (logo, material, construction, distinctive feature)

**Requirements:**

- Narrow equal gaps
- Identical lighting
- Consistent scale
- No text or labels

### 2. Character Reference Sheet (2×2 Grid)

**Top Left:** Full-body turnaround (5 views in one row)
**Top Right:** Head-and-shoulders grid (6 expressions in 2×3)
**Bottom Left:** Full-body poses (3 dynamic poses)
**Bottom Right:** Circular detail crops (4 close-ups)

**Requirements:**

- Thin dividers
- Warm studio background
- No text
- Identity consistency across all panels

### 3. Architectural Presentation (Two-Section Vertical)

**Top Section:** Technical drawing with dimensions and annotations
**Bottom Section:** Full-color photorealistic reference image

**Requirements:**

- 100% design preservation
- Monochrome technical drawing
- Color photograph below
- Minimal typography

---

## Material & Texture Descriptors

### 1. Fabric & Clothing

- "Fitted black button-up shirt"
- "Washed cotton work jacket"
- "White ribbed tank top"
- "Opaque fabric"
- "Relaxed white linen shirt with rolled-up sleeves"
- "Natural fabric movement in wind"

### 2. Metals & Reflective Surfaces

- "Reflective chrome/glass metallic strips"
- "Glossy chrome"
- "Polished reflections"
- "Large oval polished silver buckle"
- "Chunky silver rings"

### 3. Architectural Materials

- "Concrete, stone, wood, metal"
- "Realistic facade finishes"
- "Large glass windows with polished reflections"
- "Walnut veneer"
- "Marble slab"

### 4. Leather & Accessories

- "Black knee-high leather boots"
- "Chunky black leather lug-sole loafers"
- "Black belt with polished silver buckle"

---

## Color & Tone Strategies

### 1. Warm/Cool Contrast

- "Warm golden-orange reflections" + "bright white linear lights"
- "Natural orange sunset light" + "cool blue shadows"
- "Warm peach and amber sunset" + "soft violet clouds"

### 2. Restrained Color Palettes

- "Restrained colors, documentary photography"
- "Neutral true-to-life colors"
- "True-to-life colors"
- "Natural contact shadows"

### 3. Monochrome Technical

- "Monochrome beige/grey architectural style"
- "Soft off-white paper texture background"
- "Thin light-grey dividers"

---

## Film & Camera Simulation

### 1. Film Stock References

- "Kodak Portra 400" - Warm film aesthetic
- "Leica Q2, 28mm lens" - Premium documentary look
- "50mm lens, Kodak Portra 400, horizontal 3:2" - Classic portrait format

### 2. Film Characteristics

- "Gentle film grain"
- "Subtle analog grain"
- "Restrained cinematic color"
- "Slightly off-center composition"
- "Handheld photography"

### 3. Lens Specifications

- "28mm lens" - Wide environmental context
- "35mm lens" - Natural perspective
- "50mm lens" - Classic portrait compression
- "Shallow depth of field" - Subject isolation
- "Deep depth of field" - Everything sharp

---

## Best Practices Summary

### DO:

✅ Be extremely specific with technical details
✅ Use progressive detail hierarchy (general → specific)
✅ Include explicit negative prompts
✅ Specify exact dimensions and aspect ratios
✅ Reference real camera equipment and film stocks
✅ Describe lighting direction and color temperature
✅ Preserve identity through explicit instruction
✅ Emphasize natural imperfections for realism
✅ Use emotional and narrative descriptors
✅ Specify materials and textures precisely

### DON'T:

❌ Leave aspect ratios or dimensions unspecified
❌ Use vague descriptors like "nice lighting"
❌ Forget negative prompts (critical avoidances)
❌ Mix incompatible styles (e.g., candid + beauty filter)
❌ Request impossible camera angles without clarification
❌ Omit identity preservation instructions for consistency work
❌ Use generic expressions like "happy" without specificity
❌ Forget to specify what should NOT appear in image

---

## Prompt Structure Template

```
[OPENING: Category/Style Statement]

[MAIN DESCRIPTION: Subject, composition, primary elements]

[DETAILED ELEMENTS: Clothing, props, environment, specific features]

[LIGHTING: Direction, color temperature, quality, shadows]

[TECHNICAL QUALITIES: Texture, depth of field, realism markers]

[CAMERA/TECHNICAL SPECS: Equipment, lens, aspect ratio, resolution]

[STYLE KEYWORDS: Aesthetic descriptors, 5-10 comma-separated terms]

[CRITICAL AVOIDANCES: Explicit list of what NOT to include]
```

---

## Advanced Techniques

### 1. Layered Lighting Descriptions

Instead of "good lighting," layer multiple lighting elements:

- Base: "Warm natural light"
- Accent: "Golden-orange reflections"
- Shadow: "Cool blue shadows"
- Effect: "Casting sharp horizontal bands"

### 2. Material-Specific Realism

For each material, add surface quality:

- Glass: "polished reflections"
- Metal: "glossy chrome, ultra-detailed reflections"
- Fabric: "realistic folds, natural movement"
- Skin: "visible pores, natural texture"

### 3. Micro-Moment Narratives

Capture specific transitional seconds:

- "Just turning toward each other"
- "Mid-step with a lively expression"
- "As if reacting to something she just said"
- "Caught in a real, transitional movement"

### 4. Scale & Proportion Control

Be explicit about relative sizes:

- "Approximately 15-20 stories tall"
- "Large hands in the foreground"
- "Identical scale and camera height"
- "Complete figure visible from head to shoes"

---

## Application Guidelines

### For Character Work:

- Always use reference image protocol
- List all features to preserve
- Include multiple views if creating reference sheet
- Specify expressions with emotional nuance
- Add natural imperfections

### For Product Photography:

- Specify exact grid layout
- Consistent lighting across all views
- Material and finish details
- Avoid creative styling that changes product
- Include detail crops

### For Architectural:

- Reference image as design target
- Specify transformation sequence if animated
- Include material callouts
- Warm natural light typically preferred
- Clean, professional aesthetic

### For Composite Photography:

- Be explicit about scale relationships
- Describe viewing angle precisely
- Specify depth and focus relationships
- Use hyper-realistic descriptors
- Create clear spatial hierarchy

---

## Conclusion

Professional prompt engineering combines:

1. **Technical precision** (specs, measurements, equipment)
2. **Visual hierarchy** (composition, negative space, scale)
3. **Material specificity** (textures, finishes, reflections)
4. **Emotional intelligence** (expressions, narrative, mood)
5. **Negative constraints** (explicit avoidances)

The most effective prompts balance creative vision with technical constraint, using precise language to guide AI generation while leaving room for natural variation and realism.
