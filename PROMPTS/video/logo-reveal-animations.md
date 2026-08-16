# Logo Reveal Animation Prompt Library & Workflow Guide

## Overview

Transform static photography of signs, logos, or brand emblems into high-impact cinematic reveal animations while keeping the base scene, lighting, and camera positioning completely intact—creating professional VFX-style reveals where only the logo/text animates into place.

**Platform:** Google Flow (labs.google/fx/tools/flow or flow.google)  
**Model:** Omni Flash  
**Duration:** 10 seconds  
**Method:** VFX overlay reveal on locked camera  
**Aesthetic:** Photorealistic logo animation with material-specific reveal styles

---

## 1. Platform Setup & Access

### 1.1 Accessing Google Flow

**Direct URL:**
- Primary: labs.google/fx/tools/flow
- Alternative: flow.google

**Authentication:**
- Sign in with Google credentials
- Use primary Google account

**Model Selection:**
- Open parameters panel
- Set generation engine to **Omni Flash**

---

### 1.2 Input Requirements

**Image Specifications:**
- High-resolution photography
- Well-lit, clear lighting
- Sharp focus on logo/sign
- Shot straight-on or slight angle
- Clean composition

**Subject Types:**
- Wall-mounted signage
- 3D lettering
- Painted graphics
- Backlit lightbox signs
- Acrylic/raised letters
- Embossed/stamped logos
- Neon signage
- Fabric/embroidered badges

---

## 2. Universal Prompt Architecture

### 2.1 Master Template

**Copy and paste this framework, replacing bracketed placeholders with your specific details:**

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is [SUBJECT/LOGO] itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with [SURFACE/AREA] empty, no [SUBJECT/LOGO] present. [CAMERA MOVEMENT e.g., "Slight camera zoom-in begins, a gentle and minimal movement" or "Slight camera tilt left and right begins, a gentle and minimal side-to-side motion"].

[0:02-0:0X] [REVEAL STYLE matching the subject's real material—e.g., extrude/pop-out for raised acrylic letters, emboss/stamp for a leather patch, embroidery stitch for fabric badges, neon flicker for lightbox signage, glow emerge for backlit circular signs].

[0:0X-0:10] [SUBJECT/LOGO] fully in place, matching the reference image. Camera continues its movement from above and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified movement. Do not change where [SUBJECT/LOGO] sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

### 2.2 Template Breakdown

**Opening Lock Statement:**
- "This is a VFX reveal effect on a static scene"
- Prevents AI from regenerating or redesigning
- Establishes overlay approach
- Critical for preventing spatial drift

**Camera Lock Instructions:**
- "Camera position, angle, and framing stay exactly the same"
- Only specified logo/text animates
- Background, surface, lighting remain fixed
- "Like a motion graphics overlay on a still photo"

**Timeline Structure:**
- **0:00-0:02:** Empty starting state + camera movement begins
- **0:02-0:0X:** Main reveal sequence (material-specific animation)
- **0:0X-0:10:** Fully revealed + hold final frame

**Final Frame Match:**
- "The final frame should look identical to the uploaded reference image"
- Ensures completion accuracy
- No additions or modifications

---

### 2.3 Universal Negative Prompt

**Always include:**
```
Do not change the camera angle or framing beyond the specified movement. Do not change where [SUBJECT/LOGO] sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

**Why It's Critical:**
- Prevents unwanted camera changes
- Blocks style modifications
- Stops AI from adding extra elements
- Enforces timeline duration
- Single most important factor for clean results

---

## 3. Material-Specific Reveal Blueprints

### 3.1 Case Study: Red Acrylic 3D Letters (Raised Signage)

**Example:** "SHOW TIME" red 3D script lettering on off-white textured wall

**Complete Prompt:**
```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the red 3D "SHOW TIME" lettering itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the off-white textured wall panel empty, no red lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The primary red "SHOW" wordmark extrudes/pops out from flat against the wall into its full 3D raised depth, letters building into place from left to right, with a soft drop shadow forming as it extrudes outward.

[0:04-0:06] The secondary red "TIME" wordmark extrudes the same way, positioned right below the primary wordmark.

[0:06-0:10] Red 3D "SHOW TIME" logo fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

**Key Elements:**
- **Reveal Style:** Extrude/pop-out from flat to 3D raised depth
- **Direction:** Left to right letter building
- **Shadow Detail:** Drop shadows form as letters extrude
- **Camera Movement:** Slight zoom-in (gentle push-in)

---

### 3.2 Case Study: Gallery Corner Mural (Wrapped Typography)

**Example:** "PEOPLE MAKE THIS PLACE" dark red text wrapped across 90-degree corner of white gallery wall

**Complete Prompt:**
```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the dark red "PEOPLE MAKE THIS PLACE" typography itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the corner white gallery wall empty, no red text present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The primary words "PEOPLE" and "MAKE" extrude/pop out from flat against the corner wall into their full depth, wrapping around the wall corner, building into place from top to bottom with soft subtle shadows forming.

[0:04-0:06] The secondary words "THIS" and "PLACE" extrude the same way below, wrapping smoothly around the vertical edge.

[0:06-0:10] Dark red wall graphic "PEOPLE MAKE THIS PLACE" fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified push-in. Do not change where the text sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

**Key Elements:**
- **Reveal Style:** Extrude/pop-out with corner wrapping
- **Direction:** Top to bottom word sequence
- **Corner Challenge:** Typography wraps around 90-degree corner smoothly
- **Shadow Detail:** Subtle shadows form on corner geometry

---

### 3.3 Case Study: Outdoor Street Wall Graphic (Painted Lettering)

**Example:** "HAVE YOU HAD COFFEE YET?" white painted text with directional arrow on sage green exterior wall

**Complete Prompt:**
```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the white painted wall graphics and text itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the sage green wall panel empty, no white text or arrows present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The main white text "HAVE YOU HAD COFFEE YET?" extrudes/pops out from flat against the wall into its full shape, letters building into place line by line from top to bottom.

[0:04-0:06] The white directional arrow icon and the smaller "BLANK STREET" text extrude the same way into their exact respective positions.

[0:06-0:10] All white text and graphic elements fully in place on the sage green wall, matching the reference image. Camera continues its slight zoom-in and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

**Key Elements:**
- **Reveal Style:** Painted text extrusion (flat to slightly raised)
- **Direction:** Line by line from top to bottom
- **Multiple Elements:** Main text + icon + secondary text in sequence
- **Outdoor Context:** Street wall with natural lighting

---

### 3.4 Case Study: Fluted Glass 3D Signage

**Example:** "altr ego" black 3D lettering on green ribbed/fluted glass background panel

**Complete Prompt:**
```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the black "altr ego" 3D signage itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the green fluted glass panel empty, no black lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The primary black "altr" wordmark extrudes/pops out from flat against the green ribbed panel into its full 3D raised depth, with soft drop shadows forming on the textured surface.

[0:04-0:06] The secondary black "ego" wordmark and "Speciality Café" text extrude the same way right into their exact original positions.

[0:06-0:10] Black 3D "altr ego" logo fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

**Key Elements:**
- **Reveal Style:** 3D extrusion with textured surface interaction
- **Background Texture:** Ribbed/fluted glass requires shadow detail
- **Shadow Detail:** Shadows form on textured surface (critical for depth)
- **Multi-Level Text:** Primary wordmark + secondary text + descriptor

---

### 3.5 Case Study: Backlit Lightbox Signage (Halo Lighting)

**Example:** "finally, good coffee" black raised lettering with bright white halo backlighting

**Complete Prompt:**
```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the sign itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the wall panel empty, no backlit lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:06] The black "finally, good coffee" lettering flickers on line by line from top to bottom, with the bright white backlighting powering on, each phrase flickering once or twice before settling into a steady glow.

[0:06-0:10] Signboard fully lit with its cool white halo glow, matching the reference image. Camera continues its slight zoom-in and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified push-in. Do not change where the sign sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

**Key Elements:**
- **Reveal Style:** Flicker-on (neon/lightbox effect)
- **Lighting Animation:** Backlighting powers on simultaneously with letters
- **Flicker Detail:** Each line flickers once or twice before steady state
- **Halo Glow:** White backlighting creates luminous halo around letters
- **Different from Previous:** Not extrusion—electrical power-on effect

---

## 4. Reveal Style Reference Guide

### Material-Based Reveal Styles

**Extrude/Pop-Out:**
- **Use For:** Raised acrylic letters, 3D signage, mounted lettering
- **Effect:** Flat to full 3D depth
- **Details:** Drop shadows form as letters rise
- **Direction:** Left-to-right, top-to-bottom, or center-out

**Emboss/Stamp:**
- **Use For:** Leather patches, debossed signage, pressed metal
- **Effect:** Impression appears/deepens into surface
- **Details:** Shadows in recessed areas
- **Direction:** Usually all-at-once or center-out

**Embroidery Stitch:**
- **Use For:** Fabric badges, embroidered logos, textile signage
- **Effect:** Thread stitches into place
- **Details:** Follow stitch pattern/direction
- **Direction:** Outline-first or fill-progression

**Neon Flicker:**
- **Use For:** Neon tube signage, electric signs
- **Effect:** Flickers on letter-by-letter or section-by-section
- **Details:** Warm neon glow, slight buzz/flicker
- **Direction:** Typically left-to-right or top-to-bottom

**Glow Emerge (Backlit):**
- **Use For:** Lightbox signage, halo-lit letters, LED signs
- **Effect:** Backlighting powers on, letters glow into visibility
- **Details:** Halo glow around edges
- **Direction:** Simultaneous or phrase-by-phrase

**Painted Stroke:**
- **Use For:** Hand-painted murals, spray-painted graphics
- **Effect:** Paint strokes build letter forms
- **Details:** Brush or spray texture visible
- **Direction:** Stroke order (natural painting direction)

---

## 5. Camera Movement Options

### Subtle Movements (Recommended)

**Slight Zoom-In (Push-In):**
- "Slight camera zoom-in begins, a gentle and minimal movement"
- Most common choice
- Adds drama without distraction
- Focuses attention on reveal

**Slight Zoom-Out (Pull-Back):**
- "Slight camera zoom-out begins, a gentle and minimal movement"
- Reveals context gradually
- Less common but effective

**Slight Tilt Left/Right:**
- "Slight camera tilt left and right begins, a gentle and minimal side-to-side motion"
- Subtle sway effect
- Adds organic feel
- Keep motion very small

**Slight Pan Left/Right:**
- "Slight camera pan [direction] begins, a gentle and minimal movement"
- Horizontal drift
- Use sparingly

**Static (No Movement):**
- Omit camera movement line
- Pure VFX overlay
- Maximum stability

---

### Movement Best Practices

**Keep It Micro:**
- Use words like "gentle," "minimal," "slight," "subtle"
- Aggressive motion forces AI to invent new geometry
- Goal: composition recognizably the same throughout

**Match to Subject:**
- Zoom-in: Creates focus, intimacy
- Zoom-out: Reveals scale, context
- Static: Maximum control, simplest results

**Avoid:**
- Orbiting/arc shots
- Crane movements
- Whip pans
- Rotating camera
- Changing angles

---

## 6. Prompt Customization Guide

### Step-by-Step Customization

**1. Identify Your Subject:**
- What is the logo/sign? (text content, brand name)
- Material? (acrylic, painted, neon, fabric)
- Color? (be specific)
- 3D or flat?

**2. Describe the Surface/Background:**
- What is the logo mounted on?
- Color and texture
- Indoor/outdoor?

**3. Choose Reveal Style:**
- Match to material (see Section 4)
- Extrude, flicker, emboss, stitch, etc.

**4. Select Camera Movement:**
- Slight zoom-in (most common)
- Or static
- Or subtle alternative

**5. Fill Template:**
- Replace [SUBJECT/LOGO] with your text/brand
- Replace [SURFACE/AREA] with background description
- Replace [REVEAL STYLE] with chosen animation
- Replace [CAMERA MOVEMENT] with selected motion

**6. Customize Timeline:**
- Adjust 0:02-0:04, 0:04-0:06 timing if needed
- Multi-line text may need longer reveal window
- Simple logos can be faster

---

### Example Customization Walkthrough

**Subject:** "BREW & CO" gold metallic letters on dark navy wall

**Step 1 - Identify:**
- Logo: "BREW & CO"
- Material: Metallic (gold)
- Color: Gold/brass
- Style: 3D raised letters

**Step 2 - Surface:**
- Background: Dark navy blue wall
- Texture: Matte painted surface
- Location: Indoor cafe

**Step 3 - Reveal Style:**
- Extrude/pop-out (matches 3D raised metal)

**Step 4 - Camera Movement:**
- Slight zoom-in (standard)

**Step 5 - Fill Template:**

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the gold "BREW & CO" 3D lettering itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the dark navy blue wall empty, no gold lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:05] The gold metallic "BREW & CO" letters extrude/pop out from flat against the wall into their full 3D raised depth, building into place from left to right, with soft shadows forming as the metallic surface catches the light.

[0:05-0:10] Gold 3D "BREW & CO" logo fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.

Negative prompt: Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

## 7. Best Practices for Best Results

### Image Quality Requirements

**Always Start With:**
- Sharp, well-lit photography
- High resolution (1080p minimum, 4K preferred)
- Clear focus on logo/sign
- Good contrast between logo and background
- Even lighting (no harsh shadows obscuring letters)

**Avoid:**
- Extreme angles (shoot straight-on or slight angle only)
- Blurry imagery
- Backlit photos where logo is in shadow
- Heavy vignetting or filters
- Severe barrel distortion

---

### Anchor Lock Phrase (Critical)

**Always Include:**
"The camera position, angle, and framing stay exactly the same as the reference image"

**Why This Matters:**
- Prevents AI spatial drift
- Locks camera perspective
- Ensures VFX overlay approach
- Single most important phrase for stability

**Placement:**
- In opening paragraph of every prompt
- Repeated in negative prompt (angle/framing)

---

### Subtle Motion Only

**Camera Movement Guidelines:**
- Keep motion micro-sized (gentle zoom or pan)
- Use descriptors: "slight," "gentle," "minimal"
- Never exceed subtle drift
- Stop motion at 6-second mark, hold final frame

**Why Limited Motion:**
- Aggressive camera motion forces model to invent new geometry
- Large movements break the "VFX overlay" illusion
- Static backgrounds require minimal camera change

---

### Negative Prompt Enforcement

**Never Skip the Negative Prompt:**
- Single most important factor preventing unwanted changes
- Blocks style modifications
- Prevents camera angle shifts
- Stops AI from adding extra elements
- Enforces 10-second duration

**Essential Elements:**
- Do not change camera angle/framing
- Do not change logo position
- Do not add extra text/objects
- No sudden cuts/transitions
- No talking
- Exactly 10 seconds

---

### Timeline Precision

**Structure:**
- **0:00-0:02:** Empty + camera movement starts
- **0:02-0:06 (or split):** Main reveal animation
- **0:06-0:10:** Fully revealed + hold

**Flexibility:**
- Simple single-word logos: Can reveal faster (0:02-0:04)
- Multi-line complex text: May need full 0:02-0:06 or split into phases
- Always end at 0:06 for hold

**Hold Final Frame:**
- Critical for professional polish
- Shows completed result
- Allows viewer to appreciate final state
- Matches reference image exactly

---

## 8. Common Issues & Troubleshooting

### Problem: Camera angle changes or scene regenerates

**Root Cause:**
- Missing or weak anchor lock phrase
- Camera movement too aggressive

**Solution:**
- Ensure "camera position, angle, and framing stay exactly the same" is in opening paragraph
- Reduce camera movement to "slight" and "gentle"
- Strengthen negative prompt with "Do not change camera angle"

---

### Problem: Logo morphs or cross-fades instead of discrete reveal

**Root Cause:**
- Reveal style not specific enough
- Timeline too compressed

**Solution:**
- Use precise reveal language: "extrudes/pops out," "flickers on," "stitches into place"
- Extend timeline for reveal phase (0:02-0:06 instead of 0:02-0:04)
- Specify direction: "left to right," "top to bottom"

---

### Problem: Extra text, objects, or design elements appear

**Root Cause:**
- AI attempting to fill space or enhance design
- Weak negative prompt

**Solution:**
- Strengthen negative prompt: "Do not add extra text or objects"
- Emphasize "everything else stays fixed and unchanged"
- Specify "only thing that animates is [SUBJECT]"

---

### Problem: Final frame doesn't match reference image

**Root Cause:**
- Logo position shifted
- Colors changed
- Elements added/removed

**Solution:**
- Add "The final frame should look identical to the uploaded reference image" to opening paragraph
- Specify exact colors in prompt
- Lock logo position in negative prompt

---

### Problem: Animation too fast or too slow

**Root Cause:**
- Timeline doesn't match content complexity

**Solution:**
- **Too Fast:** Extend reveal window (0:02-0:06 or split into 0:02-0:04, 0:04-0:06)
- **Too Slow:** Tighten reveal window (0:02-0:04 for simple logos)
- Adjust based on number of words/elements

---

### Problem: Shadows missing or incorrect

**Root Cause:**
- Shadow detail not specified for 3D reveals
- Lighting inconsistent

**Solution:**
- Add "with soft drop shadows forming" to extrusion descriptions
- Specify shadow direction if critical
- Ensure reference image has clear lighting

---

### Problem: Backlit/neon effect not glowing properly

**Root Cause:**
- Flicker/glow language not specific enough
- Lighting effect not described

**Solution:**
- Use "flickers on" language for electrical reveals
- Specify "bright white backlighting powering on"
- Describe glow: "cool white halo glow," "warm neon glow"
- Add "each phrase flickering once or twice before settling"

---

## 9. Advanced Techniques

### Multi-Element Sequencing

**Stagger Complex Logos:**
- Primary wordmark first (0:02-0:04)
- Secondary text/tagline (0:04-0:05)
- Icon/graphic element (0:05-0:06)
- Creates visual hierarchy
- Guides viewer's eye

**Example Timeline:**
```
[0:02-0:03] Main brand name appears
[0:03-0:04] Tagline text appears below
[0:04-0:05] Circular icon/emblem appears
[0:05-0:10] All elements fully in place, hold
```

---

### Directional Variations

**Build Direction Options:**
- **Left-to-Right:** Western reading order, natural flow
- **Top-to-Bottom:** Stacked text, vertical compositions
- **Center-Out:** Radial reveals, circular logos
- **Bottom-to-Top:** Rising/ascending effect, powerful impact
- **Right-to-Left:** Unique, unexpected, artistic choice

**Specify Clearly:**
"letters building into place from [DIRECTION]"

---

### Material Texture Emphasis

**For Premium Results, Specify:**
- Surface texture interaction
- Material properties
- Lighting catch details

**Examples:**
- "with the metallic surface catching the warm cafe lighting"
- "on the textured concrete surface with subtle shadows"
- "glass reflections showing in the glossy acrylic"
- "fabric weave visible in the embroidered stitching"

---

### Camera Movement Combinations

**Advanced (Use Carefully):**
- "Slight zoom-in combined with minimal left drift"
- "Gentle zoom-out with subtle vertical tilt"

**Keep Total Movement Minimal:**
- Combined movements must still be "slight" and "gentle"
- Test simple version first
- Only add complexity if needed

---

## 10. Use Cases & Applications

### Brand Marketing

**Social Media Content:**
- Instagram Reels logo reveals
- TikTok brand intros
- LinkedIn company page headers
- Facebook video ads

**Website Integration:**
- Homepage hero animations
- About page brand story
- Landing page headers
- Portfolio showcases

**Email Marketing:**
- Animated email headers
- Product launch announcements
- Newsletter branding

---

### Business Applications

**Real Estate:**
- Property signage reveals
- Building name animations
- Development brand intros

**Retail:**
- Storefront sign animations
- Grand opening content
- Seasonal campaign intros

**Restaurants & Cafes:**
- Menu board reveals
- Brand identity content
- Location showcase videos

**Corporate:**
- Office signage animations
- Conference branding
- Presentation openers

---

### Creative Projects

**Portfolio Pieces:**
- Designer portfolio intros
- Photographer branding
- Creative agency reels

**Video Production:**
- Title card animations
- Lower third reveals
- End credit sequences

**Documentary/Film:**
- Location title cards
- Establishing shot enhancements
- Chapter markers

---

### Event & Entertainment

**Events:**
- Conference stage displays
- Wedding venue signage
- Concert venue animations

**Trade Shows:**
- Booth display content
- Product launch reveals
- Brand activation screens

---

## 11. Technical Specifications

### Input Image Specs

**Resolution:**
- Minimum: 1920x1080 (1080p)
- Recommended: 3840x2160 (4K)
- Maximum: Platform-dependent

**Aspect Ratio:**
- 16:9 (landscape - most common)
- 9:16 (vertical - mobile-first)
- 1:1 (square - social media)
- 4:5 (portrait - Instagram feed)

**File Format:**
- JPG/JPEG (most common)
- PNG (supports transparency, if needed)
- High quality, minimal compression

**Lighting:**
- Even, well-balanced lighting
- Avoid harsh shadows on logo
- Good contrast between logo and background
- Natural or artificial light both work

---

### Output Specifications

**Duration:** 10 seconds (fixed)  
**Frame Rate:** Platform default (typically 24-30fps)  
**Resolution:** Matches input  
**Format:** MP4 or platform default  
**Quality:** High bitrate

---

### Platform Requirements

**Google Flow (Omni Flash):**
- Google account required
- Browser-based (Chrome recommended)
- No downloads needed
- Cloud processing

---

## 12. Workflow Checklist

**Before Generation:**
- ☐ High-quality reference image prepared
- ☐ Logo/sign clearly visible and sharp
- ☐ Good lighting and contrast
- ☐ Straight-on or slight angle shot
- ☐ Template copied

**During Customization:**
- ☐ [SUBJECT/LOGO] replaced with actual text
- ☐ [SURFACE/AREA] replaced with background description
- ☐ [REVEAL STYLE] chosen and specified
- ☐ [CAMERA MOVEMENT] selected
- ☐ Timeline adjusted for content complexity
- ☐ Colors specified accurately
- ☐ Material details included

**Prompt Review:**
- ☐ Anchor lock phrase present ("camera position...stay exactly the same")
- ☐ "VFX reveal effect on a static scene" in opening
- ☐ "Final frame should look identical" included
- ☐ Negative prompt complete and pasted
- ☐ Duration ends at 0:10
- ☐ Camera movement ends at 0:06

**After Generation:**
- ☐ Camera stays locked (no warping)
- ☐ Logo reveals with specified style
- ☐ Background remains unchanged
- ☐ Final frame matches reference
- ☐ No extra elements added
- ☐ 10-second duration correct

---

## Quick Reference

**Platform:** Google Flow (labs.google/fx/tools/flow)  
**Model:** Omni Flash  
**Duration:** 10 seconds  
**Structure:** Empty (0-2s) → Reveal (2-6s) → Hold (6-10s)

**Key Phrases:**
- "VFX reveal effect on a static scene"
- "Camera position, angle, and framing stay exactly the same"
- "Only thing that animates is [SUBJECT]"
- "Final frame should look identical to the uploaded reference image"

**Reveal Styles:**
- Extrude/pop-out (3D signage)
- Flicker on (backlit/neon)
- Emboss/stamp (pressed/debossed)
- Embroidery stitch (fabric)
- Painted stroke (murals)

**Camera Movement:**
- Slight zoom-in (most common)
- Static (maximum control)
- Subtle alternatives (minimal)

**Never Skip:**
- Negative prompt (prevents unwanted changes)
- Anchor lock phrase (prevents spatial drift)
- Final frame match statement (ensures accuracy)

---

## Summary

Create professional logo reveal animations by treating your static photo as a locked VFX canvas—only the logo/sign animates into place while everything else remains perfectly still. Choose material-appropriate reveal styles, keep camera movement minimal, and always include the anchor lock phrase and negative prompt for best results.

**Result:** High-impact cinematic logo reveals that look professionally animated while maintaining photographic authenticity.
