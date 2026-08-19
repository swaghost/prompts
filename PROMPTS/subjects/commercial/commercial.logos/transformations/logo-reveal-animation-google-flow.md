# Logo Reveal Animation Prompt Library (Google Flow / Veo 2)

## Description

Transform static photography of signs, logos, or brand emblems into high-impact cinematic reveal animations while keeping the base scene, lighting, and camera positioning completely intact. This workflow uses Google's Flow (Veo 2) to create VFX-style reveal effects where only the logo/sign animates into place while everything else in the frame remains fixed—like motion graphics overlaid on a still photo. The technique works for acrylic letters, painted murals, backlit signage, embossed patches, embroidered badges, neon signs, and any physical brand installation captured in high-quality photography.

## Usage

Perfect for brand reveal videos, logo animation intros, signage showcase reels, storefront opening sequences, interior design brand displays, architectural branding reveals, event space branding videos, retail environment brand showcases, coffee shop signage animations, restaurant identity reveals, gallery installation videos, corporate office branding displays, trade show booth reveals, pop-up store opening videos, hotel lobby branding sequences, gym and fitness center logos, real estate property branding, hospitality venue reveals, co-working space identity videos, museum and cultural space signage, transportation hub branding, educational institution displays, healthcare facility signage, technology office environments, fashion retail brand reveals, automotive showroom branding, sports venue signage animations, entertainment venue logos, and any scenario requiring cinematic reveal animation of physical signage while maintaining photographic realism and scene integrity.

## Prerequisites

- **AI Video Platform**: Google Flow (labs.google/fx/tools/flow) or flow.google
- **Model**: Veo 2 (Omni Flash recommended for speed and quality)
- **Authentication**: Google account credentials
- **Input Requirements**: High-resolution, well-lit photo of target logo shot straight-on or at slight angle
- **Image Quality**: Sharp, clear photography with good lighting and minimal blur
- **Duration**: 10 seconds (standard output)
- **Aspect Ratio**: Matches input image (typically 16:9 landscape or 4:5 vertical)

## Technical Specifications

- **Animation Type**: VFX reveal effect on static scene (not scene regeneration)
- **Camera Behavior**: Fixed position with optional gentle zoom/pan (minimal movement only)
- **Scene Stability**: Background, surface, lighting remain completely unchanged
- **Reveal Duration**: Typically 2-6 seconds (with 2-4 second hold at end)
- **Final Frame**: Must look identical to uploaded reference image
- **Movement Style**: Subtle, micro-sized camera motion to prevent AI spatial drift
- **Negative Prompts**: Critical for preventing unwanted cuts, angle changes, or style modifications

## Universal Prompt Architecture

### **Master Template Structure**

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is [SUBJECT/LOGO] itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with [SURFACE/AREA] empty, no [SUBJECT/LOGO] present. [CAMERA MOVEMENT e.g., "Slight camera zoom-in begins, a gentle and minimal movement" or "Slight camera tilt left and right begins, a gentle and minimal side-to-side motion"].

[0:02-0:0X] [REVEAL STYLE matching the subject's real material e.g., extrude/pop-out for raised acrylic letters, emboss/stamp for a leather patch, embroidery stitch for fabric badges, neon flicker for lightbox signage, glow emerge for backlit circular signs].

[0:0X-0:10] [SUBJECT/LOGO] fully in place, matching the reference image. Camera continues its movement from above and holds until the end.
```

### **Universal Negative Prompt**

```
Do not change the camera angle or framing beyond the specified movement. Do not change where [SUBJECT/LOGO] sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

## Material-Specific Reveal Blueprints

### **Case Study 1: 3D Acrylic Letters (Raised Letter Signs)**

**Scenario**: Red 3D script wordmark lettering mounted on off-white textured wall.

**Full Prompt**:

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the red 3D "SHOW TIME" lettering itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the off-white textured wall panel empty, no red lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The primary red "SHOW" wordmark extrudes/pops out from flat against the wall into its full 3D raised depth, letters building into place from left to right, with a soft drop shadow forming as it extrudes outward.

[0:04-0:06] The secondary red "TIME" wordmark extrudes the same way, positioned right below the primary wordmark.

[0:06-0:10] Red 3D "SHOW TIME" logo fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.
```

**Negative Prompt**:

```
Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

### **Case Study 2: Wall Mural Typography (Gallery/Interior Wall Graphics)**

**Scenario**: Dark red typography wrapped across 90-degree outer corner of white gallery wall.

**Full Prompt**:

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the dark red "PEOPLE MAKE THIS PLACE" typography itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the corner white gallery wall empty, no red text present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The primary words "PEOPLE" and "MAKE" extrude/pop out from flat against the corner wall into their full depth, wrapping around the wall corner, building into place from top to bottom with soft subtle shadows forming.

[0:04-0:06] The secondary words "THIS" and "PLACE" extrude the same way below, wrapping smoothly around the vertical edge.

[0:06-0:10] Dark red wall graphic "PEOPLE MAKE THIS PLACE" fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.
```

**Negative Prompt**:

```
Do not change the camera angle or framing beyond the specified push-in. Do not change where the text sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

### **Case Study 3: Outdoor Painted Wall Graphics (Street Art/Signage)**

**Scenario**: White painted wall lettering and directional arrow graphics on exterior sage green building wall.

**Full Prompt**:

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the white painted wall graphics and text itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the sage green wall panel empty, no white text or arrows present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The main white text "HAVE YOU HAD COFFEE YET?" extrudes/pops out from flat against the wall into its full shape, letters building into place line by line from top to bottom.

[0:04-0:06] The white directional arrow icon and the smaller "BLANK STREET" text extrude the same way into their exact respective positions.

[0:06-0:10] All white text and graphic elements fully in place on the sage green wall, matching the reference image. Camera continues its slight zoom-in and holds until the end.
```

**Negative Prompt**:

```
Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

### **Case Study 4: 3D Signage on Textured Background (Fluted/Ribbed Glass)**

**Scenario**: Black 3D lettering mounted on green ribbed/fluted glass background panel.

**Full Prompt**:

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the black "altr ego" 3D signage itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the green fluted glass panel empty, no black lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:04] The primary black "altr" wordmark extrudes/pops out from flat against the green ribbed panel into its full 3D raised depth, with soft drop shadows forming on the textured surface.

[0:04-0:06] The secondary black "ego" wordmark and "Speciality Café" text extrude the same way right into their exact original positions.

[0:06-0:10] Black 3D "altr ego" logo fully extruded and in place, matching the reference image. Camera continues its slight zoom-in and holds until the end.
```

**Negative Prompt**:

```
Do not change the camera angle or framing beyond the specified push-in. Do not change where the logo sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

### **Case Study 5: Backlit Lightbox Signage (Halo Lighting Effect)**

**Scenario**: Black raised lettering featuring halo backlighting on indoor coffee shop wall.

**Full Prompt**:

```
This is a VFX reveal effect on a static scene, not a redesign or regeneration of the scene. The camera position, angle, and framing stay exactly the same as the uploaded reference image throughout the entire clip. The only thing that animates is the sign itself appearing gradually in its exact original place—everything else in the frame (background, surface, lighting) stays fixed and unchanged, like a motion graphics overlay on a still photo. The final frame should look identical to the uploaded reference image.

[0:00-0:02] Start with the wall panel empty, no backlit lettering present. Slight camera zoom-in begins, a gentle and minimal movement.

[0:02-0:06] The black "finally, good coffee" lettering flickers on line by line from top to bottom, with the bright white backlighting powering on, each phrase flickering once or twice before settling into a steady glow.

[0:06-0:10] Signboard fully lit with its cool white halo glow, matching the reference image. Camera continues its slight zoom-in and holds until the end.
```

**Negative Prompt**:

```
Do not change the camera angle or framing beyond the specified push-in. Do not change where the sign sits in the frame. Do not add extra text or objects. No sudden cuts or transitions. No talking, exactly 10 seconds.
```

---

## Reveal Style Guide by Material Type

### **Acrylic/Raised Letters**:

- **Effect**: Extrude/pop-out from flat to full 3D depth
- **Timing**: Letter by letter or word by word, left to right or top to bottom
- **Details**: Drop shadows form as letters extrude outward

### **Painted/Flat Wall Graphics**:

- **Effect**: Extrude/pop-out or paint-brush-on appearance
- **Timing**: Line by line, word by word, or full graphic at once
- **Details**: Subtle shadows form as graphics appear

### **Embossed/Stamped Leather or Fabric**:

- **Effect**: Press/emboss/stamp into surface
- **Timing**: Gradual impression forming, section by section
- **Details**: Surface indent deepens, shadows in recessed areas

### **Embroidered Patches/Badges**:

- **Effect**: Stitch-by-stitch or thread-by-thread appearance
- **Timing**: Following natural embroidery path, outline to fill
- **Details**: Thread texture and dimensional quality build up

### **Neon/LED Signage**:

- **Effect**: Flicker on, power up, glow emerge
- **Timing**: Section by section, letter by letter, or full sign at once
- **Details**: Light flickers once or twice before steady glow, bloom/glow expands

### **Backlit/Halo Lighting**:

- **Effect**: Backlight powers on, halo glow emerges
- **Timing**: Light gradually brightens, letter by letter or all at once
- **Details**: Halo expands from letters, warm or cool glow diffuses

### **Metallic/Chrome**:

- **Effect**: Shine/gleam/reflect reveal
- **Timing**: Light sweep across surface, reflections build
- **Details**: Specular highlights streak across metal, reflections intensify

### **Engraved/Etched**:

- **Effect**: Carve/etch into surface
- **Timing**: Line by line etching, following path
- **Details**: Depth and shadows form in carved areas

---

## Best Practices for Optimal Results

### **Image Quality Requirements**

- Always start with **sharp, well-lit photography**
- Avoid extreme angles or blurry imagery
- Ensure logo/sign is clearly visible and well-defined
- High contrast between logo and background works best
- Natural or studio lighting preferred over harsh shadows

### **Camera Movement Guidelines**

- Keep camera motion **micro-sized** (gentle zoom or pan)
- Aggressive camera motion forces the model to invent new geometry
- Recommended movements:
  - **Slight zoom-in**: Gentle push toward subject
  - **Slight tilt left/right**: Minimal side-to-side motion
  - **Slight pan left/right**: Subtle horizontal drift
  - Avoid: Fast movements, dramatic angle changes, orbits

### **Prompt Anchoring**

- **Explicitly state** "the camera position, angle, and framing stay exactly the same as the reference image" in every prompt
- This is the **anchor lock phrase** that prevents AI spatial drift
- Repeat that only the logo/sign animates, everything else stays fixed
- Emphasize "like a motion graphics overlay on a still photo"

### **Negative Prompt Enforcement**

- **Never skip the negative prompt**—it is critical for preventing:
  - Unwanted camera cuts or transitions
  - Style modifications or scene redesign
  - Adding extra text or objects
  - Changing logo position or framing
- The negative prompt is the **single factor** preventing spatial drift

### **Timing Structure**

- **[0:00-0:02]**: Empty scene, camera movement begins
- **[0:02-0:0X]**: Logo reveal animation (2-4 seconds typical)
- **[0:0X-0:10]**: Fully revealed, camera holds and continues gentle movement
- Total duration: Exactly 10 seconds

### **Material Matching**

- Match reveal style to the **actual physical material** of the logo
- Acrylic letters → extrude/pop-out
- Lightbox signage → flicker/power-on
- Painted walls → paint-brush-on or extrude
- Embroidered → stitch-by-stitch
- Consistency with real-world physics enhances believability

---

## Common Use Cases & Applications

### **Retail & Hospitality**

- Coffee shop interior signage reveals
- Restaurant brand wall graphics
- Hotel lobby branding animations
- Retail storefront signage showcases
- Bar and nightlife venue logos

### **Corporate & Office**

- Office reception area branding
- Conference room identity displays
- Corporate headquarters logos
- Co-working space brand reveals
- Tech startup office environments

### **Events & Exhibitions**

- Trade show booth branding
- Pop-up store opening sequences
- Gallery exhibition signage
- Museum installation reveals
- Event space branding videos

### **Architecture & Real Estate**

- Building facade signage reveals
- Property branding sequences
- Architectural identity showcases
- Real estate marketing videos
- Development project branding

### **Sports & Entertainment**

- Sports venue signage animations
- Stadium branding reveals
- Entertainment venue logos
- Gym and fitness center displays
- Arena and coliseum branding

---

## Platform Access & Setup

**Access Google Flow:**

1. Navigate to **labs.google/fx/tools/flow** or **flow.google**
2. Sign in with Google account credentials
3. Select **Veo 2** model (Omni Flash recommended)
4. Upload high-resolution reference photo
5. Input prompt following templates above
6. Add negative prompt (critical!)
7. Generate 10-second reveal animation

**Model Selection:**

- **Omni Flash**: Faster generation, excellent quality
- **Veo 2 Standard**: Higher fidelity, longer processing

**Output:**

- 10-second video clip
- Matches input image dimensions
- Ready for download and use in marketing materials

---

## Advanced Techniques

### **Multi-Element Sequences**

For logos with multiple components:

- Primary element: [0:02-0:04]
- Secondary element: [0:04-0:06]
- Tertiary details: [0:06-0:08]
- Full hold: [0:08-0:10]

### **Color-Specific Reveals**

When logo has distinct color sections:

- Reveal by color group (all red elements, then blue, then yellow)
- Or reveal spatially (left to right, top to bottom)

### **Lighting Emphasis**

Add micro lighting cues:

- "Soft spotlight subtly brightens logo area as it appears"
- "Ambient light increases slightly during reveal"
- Keeps focus on reveal without changing scene lighting

### **Background Hold Verification**

Emphasize repeatedly:

- "Background wall texture stays completely frozen"
- "Surface material remains static throughout"
- "No camera angle or perspective shift"

---

## Troubleshooting

**Problem**: Logo changes position or design  
**Solution**: Strengthen anchor phrases, emphasize "exact original place" and "matching reference image"

**Problem**: Background moves or changes  
**Solution**: Add "background stays completely frozen/static/unchanged" multiple times

**Problem**: Camera angle shifts  
**Solution**: Reduce camera movement intensity, use only "slight" descriptors

**Problem**: AI adds extra elements  
**Solution**: Strengthen negative prompt, explicitly list what NOT to add

**Problem**: Reveal timing is off  
**Solution**: Adjust timestamp ranges, ensure clear progression markers

---

## Source Reference

Based on the **Logo Reveal Animation Prompt Library & Workflow Guide** by efficient-mink-952 (Notion).  
Original documentation: https://efficient-mink-952.notion.site/Logo-Reveal-Animation-Prompt-Library-Workflow-Guide-3b59502993ae800fb32bd99217aeceb1

Adapted for the A7 ai.prompts library structure and expanded with additional use cases and technical specifications.

---

## Related Files

- See also: [3d-metallic-logo-transformation.md](./3d-metallic-logo-transformation.md) for static 3D logo rendering
- See also: [logos.active-stitch.video.md](../../../video/sequences/logos/logos.active-stitch.video.md) for alternative logo animation styles
