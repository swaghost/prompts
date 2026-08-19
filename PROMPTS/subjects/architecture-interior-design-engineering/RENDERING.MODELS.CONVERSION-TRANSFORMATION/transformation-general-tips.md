# General Transformation Tips - Architectural Image Transformations

## Overview

Universal principles, essential phrases, parameters, and strategies for all architectural image transformation prompts. Use these guidelines to enhance any transformation type and improve AI generation results.

**Part of:** [Architectural Transformations Collection](architectural-transformations-image.md)

---

## Essential Phrases for All Transformations

### Preservation Phrases

These phrases ensure the AI maintains your original design intent while performing the transformation.

**Form and Composition:**

```
Preserving the original massing
Preserve the original building form
Maintain exact proportions
Original composition preserved
Preserve building's original form
Keep exact building form and proportions
```

**Layout and Arrangement:**

```
Preserving the original layout exactly
Maintain exact layout and dimensions
Preserve exact floor plan layout
Original layout preserved
Keep original spatial arrangement
```

**Materials and Finishes:**

```
Preserving the original materials
Maintain original material palette
Original materials and finishes preserved
Keep original design materials
Preserve façade materials exactly
```

**Design Intent:**

```
Preserve design intent
Maintain architectural character
Original design maintained
Preserve aesthetic quality
Keep design integrity
```

**Usage Tips:**

- Use preservation phrases early in prompt (first or second sentence)
- Repeat preservation phrases if generation doesn't respect original
- Be specific about what to preserve (massing, layout, materials, or all)
- Combine multiple preservation phrases for emphasis

---

## Quality Level Phrases

### Professional Standards

**Architectural Presentation:**

```
Professional architectural presentation
Professional architectural visualization
Architectural rendering quality
Professional architecture documentation
High-quality architectural presentation
```

**Technical Precision:**

```
Technical precision
Technical accuracy
Construction-accurate details
Technically precise
Engineering quality
```

**Rendering Quality:**

```
Professional rendering quality
Photorealistic rendering
High-quality visualization
4K quality visualization
Professional 3D rendering
```

**Document Standards:**

```
Professional construction document style
CAD-quality line work
Technical illustration quality
Construction document standards
Professional technical drawing
```

**Usage Tips:**

- Match quality phrase to transformation type
- "Professional architectural" works for most cases
- Add "photorealistic" only when realistic materials needed
- Use "technical" for construction and detail documents

---

## Specific Requirements

### View and Projection

**Isometric/Axonometric:**

```
Isometric projection
Isometric view
Axonometric view
Isometric axonometric drawing
True isometric (30°/30°)
Dimetric projection
```

**Perspective:**

```
Slight perspective
One-point perspective
Two-point perspective
Aerial perspective view
Eye-level perspective
```

**Orthographic:**

```
Orthographic projection
Elevation view
Section view
Plan view
No perspective distortion
```

**Camera Angles:**

```
Aerial view
Bird's eye view
Eye-level view
Aerial oblique
Elevated view
Ground-level view
```

**Usage Tips:**

- Specify projection type explicitly to avoid unwanted perspective
- "Isometric" is clear for technical diagrams
- "Slight perspective" acceptable for marketing images
- Avoid perspective terms if you want true isometric/axonometric

---

### Material Specifications

**Realistic Materials:**

```
Realistic materials
Photorealistic materials
PBR materials (physically based rendering)
Realistic material textures
Accurate material rendering
Material realism
```

**Simplified/Abstract:**

```
Without realistic textures
No texture detail
Simplified materials
Flat colors
Minimal texture
Clean abstract materials
```

**Specific Materials:**

```
Hardwood flooring
Marble countertops
Glass curtain wall
Brick veneer
Metal panels
Concrete structure
Natural stone cladding
```

**Usage Tips:**

- Be specific about material types when needed
- "Realistic materials" for photorealistic transformations
- "Without realistic textures" for massing studies
- Name specific materials for construction details

---

### Lighting Conditions

**Natural Lighting:**

```
Soft natural lighting
Natural lighting through windows
Daylight illumination
Sunlight from [direction]
Overcast daylight
Golden hour lighting
```

**Studio/Ambient:**

```
Studio lighting
Soft ambient lighting
Even illumination
Professional lighting
Neutral lighting
Soft shadows for depth
```

**Dramatic:**

```
Dramatic lighting
Directional lighting
Strong shadows
High contrast lighting
Cinematic lighting
```

**Shadow Control:**

```
Soft shadows
Gentle shadows for depth
Minimal shadows
No shadows (pure diagram)
Shadow emphasis
```

**Usage Tips:**

- "Soft natural lighting" works well for most visualizations
- "Studio lighting" for analytical studies and massing
- Specify shadow needs: "soft shadows for depth without drama"
- Mention sun direction for shadow studies

---

### Background Treatment

**Clean Backgrounds:**

```
White background
Light grey background
Neutral background
Clean background
Transparent background
Gradient background (light to darker grey)
```

**Contextual:**

```
Include urban context
Show site context
Surrounding buildings shown
Street and landscape context
Aerial view with surroundings
```

**Background Control:**

```
No distracting background
Clean presentation
Isolated on white
Context removed
Focus on building only
```

**Usage Tips:**

- "White background" or "light grey background" safest default
- Specify "no distracting elements" if AI adds unwanted context
- Request "transparent background" for compositing flexibility
- Include context only when analysis requires it

---

### Annotation Needs

**Dimensional:**

```
Include dimensions
Dimension strings
Dimensioned for construction
Overall and component dimensions
Critical dimensions shown
```

**Material Callouts:**

```
Material labels
Material specifications
Material keynotes
Material schedule
Product specifications
```

**Technical Notes:**

```
Technical annotations
Installation notes
Construction notes
Assembly notes
Specification callouts
```

**Minimal/None:**

```
No annotations
Clean presentation without text
Unlabeled diagram
Visual only
```

**Usage Tips:**

- Specify annotation needs in initial prompt
- "Include dimensional callouts" for construction documents
- "No annotations" or omit mention for clean presentations
- Can add annotations in post-processing if needed

---

## Common AI Tool Parameters

### Midjourney Parameters

**Aspect Ratios:**

```
--ar 4:5        Vertical portrait (common for elevations)
--ar 16:9       Horizontal landscape (common for detail boards)
--ar 3:2        Classic photo ratio (versatile)
--ar 1:1        Square format (social media, portfolio)
--ar 9:16       Vertical video format
--ar 2:3        Vertical alternative
```

**Stylization:**

```
--stylize 50        Very literal, minimal AI interpretation
--stylize 150       Low stylization, technical precision
--stylize 250       Moderate-low (good for architectural diagrams)
--stylize 500       Balanced (Midjourney default)
--stylize 750       Moderate-high, more artistic
--stylize 1000      Very artistic, heavy interpretation
```

**Quality:**

```
--quality 1         Standard quality (default)
--quality 2         Higher quality, more GPU time, more detail
```

**Style:**

```
--style raw         More photographic, literal, less stylized
--style            Standard Midjourney aesthetic (default)
```

**Other Useful:**

```
--chaos 0-100       Variation amount (0 = consistent, 100 = very varied)
--weird 0-3000      Experimental unusual results
--tile              Seamless tiling pattern
--no [element]      Avoid specific elements
```

**Recommendation by Transformation Type:**

**Exploded Isometric:**

- `--ar 4:5 --stylize 250-500 --quality 2`

**Floor Plan to 3D:**

- `--ar 4:5 --stylize 500-750 --quality 2 --style raw` (for photorealism)

**Simplified Massing:**

- `--ar 4:5 --stylize 50-250 --quality 2 --style raw`

**Construction Details:**

- `--ar 4:5 --stylize 250-500 --quality 2`

**Technical Boards:**

- `--ar 16:9 --stylize 50-250 --quality 2 --style raw`

---

### DALL-E Guidelines

DALL-E 3 (via ChatGPT or API) doesn't use command-line parameters. Instead, control output through detailed natural language prompts.

**Key Strategies:**

**Be Very Specific:**

- DALL-E interprets literally, so detailed descriptions work well
- Specify materials, colors, lighting, view angle explicitly
- Mention "architectural visualization" or "technical illustration"

**Style Control:**

- Request "photorealistic" for realistic output
- Use "technical diagram" or "architectural drawing" for line work
- Mention "CAD-quality" for technical precision

**Aspect Ratio:**

- Request format: "vertical format" or "horizontal format"
- DALL-E supports square (1024x1024), landscape (1792x1024), portrait (1024x1792)

**Preservation:**

- Emphasize "maintaining exact proportions"
- Repeat design preservation multiple times
- Very explicit about what must be preserved

**Example DALL-E Prompt:**

```
Transform this architectural façade into an exploded isometric view, preserving the original building massing exactly. Separate the floors vertically to reveal internal organization. Use realistic materials: concrete, steel, glass. Professional architectural presentation style with clean lines and soft shadows. White background. Vertical format. Technical illustration quality.
```

---

### Stable Diffusion Tips

Stable Diffusion (including SDXL) uses prompts plus negative prompts and various parameters.

**Prompt Structure:**

- Put most important elements first
- Use commas to separate concepts
- Emphasize with parentheses: `(important concept:1.2)` or `((very important))`
- Use keywords from training data

**Architectural Keywords:**

```
architectural visualization
architectural rendering
professional architecture
3D architectural model
isometric architectural drawing
technical illustration
construction detail
CAD drawing
```

**Style Keywords:**

```
V-Ray rendering
Corona renderer
Unreal Engine
photorealistic
technical diagram
line drawing
architectural photography
```

**Negative Prompts:**

```
Negative: distorted, low quality, blurry, cartoon, anime, people, watermark, text, signature, amateur, unrealistic proportions, wrong perspective
```

**Key Parameters:**

**CFG Scale (Classifier Free Guidance):**

- Low (5-8): Loose interpretation, creative
- Medium (9-12): Balanced
- High (13-20): Very literal, can be rigid
- Recommendation: 7-10 for architectural work

**Steps:**

- 20-30 steps usually sufficient
- More steps = more refinement (diminishing returns)
- 40-50 for final high-quality renders

**Sampling Method:**

- DPM++ 2M Karras (good balance)
- Euler A (fast, creative)
- DDIM (deterministic, reproducible)

**Checkpoints/Models:**

- Use architectural or realistic checkpoints
- "Realistic Vision" or "DreamShaper" for photorealism
- Specialized architecture models if available

**LoRAs (Low-Rank Adaptations):**

- Architectural LoRAs for style
- Isometric view LoRAs
- Technical drawing LoRAs
- Combine multiple LoRAs (keep weights reasonable, 0.5-1.0)

---

## Prompt Construction Framework

### Basic Structure

```
[ACTION] + [SOURCE] + [OUTPUT TYPE] + [PRESERVATION CLAUSE] + [SPECIFIC REQUIREMENTS] + [STYLE/QUALITY]
```

**Breakdown:**

1. **ACTION:** What transformation to perform
   - Transform, convert, create, generate, etc.

2. **SOURCE:** What you're transforming
   - "this architectural façade"
   - "this floor plan"
   - "the building elevation"

3. **OUTPUT TYPE:** What you want to create
   - "exploded isometric view"
   - "fully furnished 3D model"
   - "technical detail board"

4. **PRESERVATION CLAUSE:** What must be maintained
   - "preserving the original massing"
   - "maintaining exact layout"
   - "preserving design intent"

5. **SPECIFIC REQUIREMENTS:** Details about the output
   - Materials, lighting, view angle, components to show, etc.

6. **STYLE/QUALITY:** Presentation quality and aesthetic
   - "professional architectural presentation"
   - "photorealistic rendering"
   - "technical illustration quality"

---

### Example Breakdown

**Prompt:**

```
Transform this architectural façade into an exploded isometric view, preserving the original massing. Separate the floors and building components to reveal internal organization, using realistic materials and a professional architectural presentation style.
```

**Analysis:**

- **ACTION:** Transform
- **SOURCE:** this architectural façade
- **OUTPUT TYPE:** exploded isometric view
- **PRESERVATION:** preserving the original massing
- **REQUIREMENTS:** Separate floors and components, reveal organization, realistic materials
- **STYLE:** professional architectural presentation style

---

### Building Complex Prompts

**Start Simple:**

```
Transform this façade into a 3D isometric view preserving the original form.
```

**Add Specifics:**

```
Transform this façade into an exploded 3D isometric view preserving the original building form. Separate floors vertically to show internal organization.
```

**Add Materials:**

```
Transform this façade into an exploded 3D isometric view preserving the original building form. Separate floors vertically to show internal organization. Use realistic materials: concrete structure, glass windows, metal panels.
```

**Add Lighting and Background:**

```
Transform this façade into an exploded 3D isometric view preserving the original building form. Separate floors vertically to show internal organization. Use realistic materials: concrete structure, glass windows, metal panels. Soft studio lighting, subtle shadows, white background.
```

**Add Style and Quality:**

```
Transform this façade into an exploded 3D isometric view preserving the original building form. Separate floors vertically to show internal organization. Use realistic materials: concrete structure, glass windows, metal panels. Soft studio lighting, subtle shadows, white background. Professional architectural presentation style, technical illustration quality.
```

**Principle:** Build prompt incrementally, adding layers of detail

---

## Iteration Strategy

### General Iteration Workflow

**Generation 1 - Establish Foundation:**

- **Goal:** Basic transformation successful
- **Focus:** Output type correct, general composition acceptable
- **Prompt:** Base template with key requirements
- **Evaluate:** Is this the right transformation type? General direction correct?

**Generation 2 - Refine Specifics:**

- **Goal:** Improve accuracy and detail
- **Focus:** Preservation of original, materials, view angle, technical accuracy
- **Prompt:** Add specific material, lighting, and technical requirements
- **Evaluate:** Is original design preserved? Materials realistic? View optimal?

**Generation 3 - Polish and Perfect:**

- **Goal:** Final presentation quality
- **Focus:** Annotations (if needed), final quality, minor adjustments
- **Prompt:** Fine-tune all parameters, add quality specifications
- **Evaluate:** Professional quality? Ready for intended use? Client/audience appropriate?

**Generation 4+ - Optional Refinements:**

- Adjust specific elements that didn't work
- Try alternative views or presentations
- Explore variations (different materials, lighting, etc.)

---

### When to Iterate vs. Start Over

**Iterate (Refine Existing):**

- Basic transformation is correct
- Original design preserved
- Output type appropriate
- Just needs refinement (materials, lighting, detail level)

**Start Over (New Generation):**

- Wrong transformation type
- Original design not preserved
- Fundamental composition wrong
- Misunderstood prompt intent

**Tips:**

- Be patient - allow 2-3 iterations before judging
- Change one major element at a time (easier to identify what works)
- Save successful prompts for reuse
- Document what works for different transformation types

---

## Use Case Matrix

Quick reference for which transformation type best fits your project phase and purpose.

| Transformation Type     | Conceptual | Design Dev | Construction | Marketing | Education |
| ----------------------- | ---------- | ---------- | ------------ | --------- | --------- |
| **Exploded Isometric**  | ✓✓✓        | ✓✓         | ✓            | ✓✓        | ✓✓✓       |
| **Floor Plan to 3D**    | ✓          | ✓✓✓        | ✓            | ✓✓✓       | ✓✓        |
| **Simplified Massing**  | ✓✓✓        | ✓✓✓        | -            | ✓         | ✓✓        |
| **Construction Detail** | -          | ✓✓         | ✓✓✓          | ✓         | ✓✓✓       |
| **Technical Board**     | -          | ✓          | ✓✓✓          | -         | ✓         |

**Legend:**

- ✓✓✓ = Excellent fit, primary use case
- ✓✓ = Very good fit, common use
- ✓ = Suitable, occasional use
- - = Not typically used for this purpose

---

## Workflow Integration

### Design Process Workflow

**1. Conceptual Phase:**

- Use: Simplified Massing Studies
- Purpose: Explore form and volume options
- Output: Multiple massing alternatives for comparison
- Quality Level: Clean diagram quality

**2. Design Development:**

- Use: Floor Plan to 3D, Exploded Isometric
- Purpose: Communicate spatial design, explain building organization
- Output: Client presentation materials, design review boards
- Quality Level: High-quality visualization

**3. Construction Documents:**

- Use: Exploded Construction Details, Technical Detail Boards
- Purpose: Construction documentation, specifications
- Output: Permit drawings, contractor bid documents
- Quality Level: Technical precision, CAD quality

**4. Marketing and Sales:**

- Use: Floor Plan to 3D (furnished)
- Purpose: Property marketing, sales materials
- Output: Brochures, websites, signage
- Quality Level: Photorealistic, aspirational

**5. Education and Training:**

- Use: All types depending on lesson
- Purpose: Teach design principles, construction methods
- Output: Educational diagrams, textbooks, presentations
- Quality Level: Clarity and accuracy over photorealism

---

### Document Set Integration

**Permit Submittal Package:**

1. Technical Detail Boards - Code compliance documentation
2. Simplified Massing - Zoning compliance, shadow studies
3. (Traditional drawings for remainder of set)

**Construction Bid Package:**

1. Technical Detail Boards - Scope definition
2. Exploded Construction Details - Assembly methodology
3. (Specifications and schedules)

**Client Presentation:**

1. Floor Plan to 3D - Interior visualization
2. Exploded Isometric - Building organization explanation
3. Simplified Massing - Design alternatives comparison

**Shop Drawings / Submittals:**

1. Technical Detail Boards - Fabrication details
2. Exploded Construction Details - Assembly verification
3. (Material samples and specifications)

---

## Quality Checklist for All Transformations

Universal quality criteria applicable to any transformation type:

**Design Preservation:**

- [ ] Original building form/layout accurately preserved
- [ ] Proportions maintained correctly
- [ ] Design intent communicated clearly
- [ ] Character and aesthetic consistent with original

**Technical Accuracy:**

- [ ] Appropriate for intended use and audience
- [ ] Materials represented accurately (if applicable)
- [ ] Construction methodology realistic (if applicable)
- [ ] Dimensions and scale appear correct

**Presentation Quality:**

- [ ] Professional presentation standards
- [ ] Clean and clear visual communication
- [ ] Appropriate detail level for purpose
- [ ] No distracting or erroneous elements

**View and Composition:**

- [ ] View angle optimal for content
- [ ] Projection type appropriate (isometric, perspective, etc.)
- [ ] Composition balanced and clear
- [ ] Background appropriate (clean or contextual as intended)

**Materials and Lighting:**

- [ ] Materials rendered appropriately for transformation type
- [ ] Lighting enhances understanding without distraction
- [ ] Shadows provide depth without drama (unless intended)
- [ ] Material realism matches intent (realistic vs. diagrammatic)

**Annotations (if applicable):**

- [ ] Dimensions accurate and complete
- [ ] Material callouts clear and correct
- [ ] Notes and specifications readable
- [ ] Annotations don't clutter or obscure content

**Output Quality:**

- [ ] Resolution adequate for intended use
- [ ] File format appropriate
- [ ] Color/line work prints clearly
- [ ] Meets project or industry standards

---

## Common Problems and Universal Solutions

### Problem: AI Doesn't Preserve Original Design

**Symptoms:**

- Form or proportions change
- Layout doesn't match source
- Materials altered incorrectly
- Design intent lost

**Solutions:**

1. Use preservation phrases early in prompt (first or second sentence)
2. Repeat preservation multiple times: "Preserve original form. Maintain exact proportions. Original design must be maintained."
3. Be specific: "Preserve the three-story massing with corner tower exactly as shown"
4. Add reference: "Match original proportions precisely"
5. Use seed locking (Midjourney) for consistency if one result is close

---

### Problem: Wrong Output Type or Transformation

**Symptoms:**

- Get perspective when wanted isometric
- Get massing when wanted detailed model
- Get artistic interpretation instead of technical diagram

**Solutions:**

1. Be very explicit about output type in prompt
2. Use correct terminology: "isometric projection" not just "3D view"
3. Add style qualifiers: "technical diagram," "architectural visualization," "construction document"
4. Use negative prompts (Stable Diffusion) to exclude unwanted styles
5. Lower stylization (Midjourney) for more literal interpretation

---

### Problem: Materials Look Wrong or Unrealistic

**Symptoms:**

- Materials too simplified or too detailed
- Wrong material types
- Unrealistic textures
- Materials don't match architectural intent

**Solutions:**

1. Specify material realism level: "photorealistic materials" or "simplified without textures"
2. Name specific materials: "brick veneer," "aluminum curtain wall," "hardwood flooring"
3. Add material quality: "high-end materials," "premium finishes," "realistic PBR materials"
4. Reference rendering engines: "V-Ray quality," "Unreal Engine materials"
5. Describe material characteristics: "matte concrete," "brushed metal," "clear glass"

---

### Problem: Lighting or Shadows Wrong

**Symptoms:**

- Too dark or too bright
- Dramatic shadows when not wanted
- No depth perception
- Wrong lighting mood

**Solutions:**

1. Specify lighting type: "soft natural lighting," "studio lighting," "ambient lighting"
2. Control shadows: "soft shadows for depth," "minimal shadows," "no harsh shadows"
3. Describe mood: "bright and airy," "warm and inviting," "neutral technical lighting"
4. Specify light source: "natural daylight through windows," "even overhead lighting"
5. Reference photography style: "architectural photography lighting"

---

### Problem: Busy or Distracting Background

**Symptoms:**

- Unwanted context or environment
- Distracting elements
- Background competes with subject
- Unprofessional presentation

**Solutions:**

1. Explicitly request background type: "white background," "light grey background"
2. Add "no distracting elements," "clean background," "isolated"
3. Use negative prompts (SD): "no context, no environment, no landscape"
4. Request "professional presentation on neutral background"
5. Specify "transparent background" if needed for compositing

---

### Problem: Wrong Scale or Proportions

**Symptoms:**

- Elements too large or small
- Furniture doesn't fit space
- Building proportions distorted
- Unrealistic dimensions

**Solutions:**

1. Add "accurate scale and proportions," "realistic human scale"
2. Include scale references: "show human figures for scale" (if appropriate)
3. Emphasize proportion preservation: "maintain exact proportions from original"
4. Specify dimensions if critical: "8-foot ceiling height," "standard door widths"
5. Reference standards: "architectural scale," "construction standard proportions"

---

## Combining Transformations

Sometimes multiple transformation types can be combined or used in sequence:

**Exploded Isometric + Simplified Massing:**

```
Create simplified massing exploded isometric. Preserve building form. Separate floors vertically in pure white material without detail. Show volumetric composition and spatial organization in clean diagram style.
```

**Floor Plan to 3D + Exploded Isometric:**

```
Transform floor plan to fully furnished 3D isometric model and separate floors slightly to show multi-level organization while maintaining furnished interior visibility.
```

**Construction Detail + Technical Board:**

```
Create technical detail board with exploded 3D construction detail as primary image, supplemented by elevation, sections, dimensions, and material schedule.
```

**Multiple Massing Options:**

```
Show three simplified massing alternatives side by side for comparison. Same style, lighting, and view angle. Label Option A, B, C.
```

---

## Professional Tips

### For Architects and Designers

1. **Start with best source material:** High-quality images yield better transformations
2. **Build prompt library:** Save successful prompts for reuse and modification
3. **Test parameters:** Experiment with stylization and quality settings
4. **Iterate systematically:** Change one variable at a time to learn what works
5. **Post-process if needed:** AI generation + Photoshop/CAD touch-up often best workflow
6. **Respect original design:** Always credit original architects if sharing

### For Contractors and Builders

1. **Focus on technical accuracy:** Emphasize construction-accurate details and methods
2. **Request realistic materials:** Photorealistic materials help visualize actual products
3. **Show assembly sequences:** Numbered sequence helps communicate installation order
4. **Include annotations:** Dimensions and material callouts reduce RFIs
5. **Create installation guides:** Visual sequence documentation trains crews
6. **Verify before building:** Always check AI output against engineering and specs

### For Educators

1. **Prioritize clarity:** Diagram quality and clear communication over photorealism
2. **Use consistent style:** Students learn better with consistent visual language
3. **Label everything:** Annotations and callouts essential for learning
4. **Show sequences:** Step-by-step transformations teach processes
5. **Compare alternatives:** Side-by-side comparisons teach design decision-making
6. **Iterate with students:** Show prompt refinement process as lesson

### For Marketing and Sales

1. **Photorealism sells:** Invest in high-quality, realistic materials and lighting
2. **Show lifestyle:** Furnished spaces with warm lighting create emotional connection
3. **Multiple views:** Provide various angles and perspectives
4. **Context matters:** Show building in neighborhood context for some views
5. **Consistent brand:** Match visualizations to brand aesthetic and target audience
6. **High resolution:** Always request maximum quality for print and large displays

---

## Specialized Transformation Types

### Quick Reference Guide

**Need to show internal organization?**
→ [Exploded Isometric Views](transformation-exploded-isometric.md)

**Need to furnish and visualize interior spaces?**
→ [Floor Plan to 3D Model](transformation-floor-plan-to-3d.md)

**Need to study building form without detail?**
→ [Simplified Massing Studies](transformation-simplified-massing.md)

**Need to show construction assembly?**
→ [Exploded Construction Details](transformation-exploded-construction.md)

**Need construction documentation with dimensions?**
→ [Technical Detail Boards](transformation-technical-boards.md)

---

**See Also:** [Main Transformations Guide](architectural-transformations-image.md) for complete transformation collection and specific type details.
