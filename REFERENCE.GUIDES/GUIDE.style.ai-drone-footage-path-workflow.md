# AI Drone Footage - Path Workflow V1

## Description

A revolutionary workflow for creating hyper-realistic cinematic FPV drone footage using AI. Draw a custom flight path directly on your image, and AI will generate a continuous, uninterrupted drone sequence that follows your exact trajectory. Perfect for architectural reveals, city flyovers, landscape exploration, and dynamic product showcases. Uses Seedance 2.0 or Gemini Omni to transform static images into professional-grade aerial cinematography.

## Tools Required

- **Seedance 2.0 or Gemini Omni** — AI video models with path-following capabilities
- **Access Platforms** — Google Flow, Higgsfield, or Dreamina
- **Image Editing Software** — Photoshop, Figma, or any drawing tool to create path overlay
- **Source Material** — AI-generated image, stock footage frame, or original photograph
- **Optional** — Video editor for post-production color grading

## What You'll Learn

- Creating visual flight path references using overlay drawings
- Using dual-reference system (Environment + Path) for precise camera control
- Writing master prompts that preserve environment while following custom trajectories
- Generating continuous FPV drone sequences without cuts or transitions
- Advanced camera choreography techniques: spirals, pullbacks, altitude changes, banking turns
- Negative prompting to eliminate UI elements and maintain photorealism

---

## The Dual-Reference System

This workflow uses a two-image reference structure to separate environment preservation from camera movement:

### Reference Image 1: Environment Master
**Purpose:** Lock the visual appearance of the scene  
**Contains:** The clean, unmodified image of your location  
**Used for:** Preserving exact environment, skyline, building positions, architecture, lighting, atmosphere, colors, perspective, scale, and composition

### Reference Image 2: Path & Storyboard
**Purpose:** Define camera choreography and trajectory  
**Contains:** Your original image with drawn flight path (arrows, route lines, numbered checkpoints, storyboard panels)  
**Used for:** Camera movement only — these visual guides must NOT appear in final video

**Critical Rule:** Image 2 is treated as a planning document. The AI follows the path but removes all drawing elements from the rendered output.

---

## Complete Workflow

### Phase 1: Prepare Your Source Image

**Step 1: Obtain Your Base Image**

Your source can be:
- **AI-Generated:** Create your ideal scene using Nano Banana, MidJourney, DALL-E, or Flux
- **Stock Footage:** Extract a frame from stock video
- **Original Photography:** Use your own photos or drone stills

**Image Requirements:**
- High resolution (minimum 2K, ideally 4K or higher)
- Clear focal point or subject for the drone to reveal
- Interesting architecture, landscape, or environment to navigate
- Good lighting and contrast for dramatic cinematography

**Recommended Subjects:**
- Modern architecture and skyscrapers
- Natural landscapes (mountains, forests, coastlines)
- Urban environments and city skylines
- Landmarks and monuments
- Real estate properties
- Product showcases in environments

---

### Phase 2: Draw Your Flight Path

**Step 2: Create the Path Overlay**

Using any image editing software (Photoshop, Figma, Procreate, or even MS Paint):

1. **Duplicate your source image**
2. **Draw your flight path** using these elements:
   - **Route line:** A continuous colored line showing the exact camera trajectory
   - **Arrows:** Direction indicators showing movement flow
   - **Numbered checkpoints:** Key moments or position markers (1, 2, 3, etc.)
   - **Storyboard panels (optional):** Small frames showing expected views at key moments
   - **Altitude indicators (optional):** Labels like "Low," "Climb," "High," "Descend"

**Path Drawing Best Practices:**

- **Make the line CONTINUOUS:** No breaks or gaps — the AI interprets this as one seamless flight
- **Use contrasting colors:** Bright colors (red, yellow, cyan) stand out against most backgrounds
- **Show curves and banking:** Curved lines indicate smooth turns; sharp angles create dynamic banking
- **Indicate altitude changes:** Arrows pointing up/down, or written labels
- **Mark key moments:** Numbers at critical positions (entry, apex, finale)
- **Add motion indicators:** Speed lines, spiral arrows for rotation, wide arcs for pullbacks

**Example Flight Path Components:**
```
START (1) → Low foreground entry → 
(2) Sweeping approach around buildings → 
(3) Accelerate toward subject → 
(4) Vertical climb alongside structure → 
(5) Spiral climb around subject → 
(6) Pass above highest point → 
(7) Wide pullback arc → 
END (8) Dramatic aerial reveal
```

**Save both images:**
- **Image 1:** Clean original (no markings)
- **Image 2:** Path overlay version (with all drawings)

---

### Phase 3: Generate AI Drone Footage

**Step 3: Upload to AI Video Platform**

**Platform:** Google Flow, Higgsfield, or Dreamina  
**Model:** Seedance 2.0 or Gemini Omni

**Upload Sequence:**
1. Upload **Image 1** (clean environment reference)
2. Upload **Image 2** (path overlay reference)
3. Paste the Master Prompt (below)
4. Generate video

---

### The Master Prompt Template

```
Image 1 = Environment Reference

Image 2 = Storyboard & Camera Path Reference

Use Image 1 as the master visual reference for the entire video. Preserve the exact environment, skyline, building positions, architecture, roads, lighting, atmosphere, colors, perspective, scale, and composition. Do not modify the environment or introduce new buildings or landmarks.

Use Image 2 ONLY as a storyboard and camera choreography reference. The route lines, arrows, numbered checkpoints, storyboard panels, text, diagrams, graphs, and all UI elements are planning guides only. They must NOT appear in the final video.

Create a hyper-realistic cinematic FPV drone sequence lasting approximately 15 seconds.

The entire sequence must be one continuous uninterrupted FPV drone shot from the first frame to the last. There must be no cuts, hidden transitions, camera resets, teleportation, disconnected movements, or abrupt viewpoint changes.

Treat the route shown in Image 2 as a continuous camera spline. Follow the camera path precisely, preserving every curve, banking turn, climb, descent, spiral, pullback, altitude change, and direction exactly as illustrated. Do not simplify the route, skip sections, reinterpret the movement, or create shortcuts. Every segment of the route must connect seamlessly to the next while maintaining realistic FPV drone momentum and continuous spatial orientation.

Match the timing and progression demonstrated in the storyboard panels.

Flight Sequence

• Begin with a low-altitude entry through the foreground buildings.

• Perform the sweeping approach around the foreground structures while maintaining strong forward momentum.

• Accelerate toward the central subject exactly as shown.

• Transition into a smooth vertical climb while staying close to the structure.

• Continue into a single continuous spiral climb around the structure while maintaining upward momentum.

• Pass above the highest point without stopping.

• Transition into a wide pullback arc while continuing to gain altitude.

• Finish with a dramatic wide aerial reveal matching the final storyboard composition.

Camera Style

Professional FPV drone
First-person perspective
One continuous take
Ultra-high-speed cinematic flight
Physically accurate FPV drone movement
Realistic inertia
Continuous forward momentum
Smooth banking during turns
Natural acceleration and deceleration
Stable horizon
Strong foreground and background parallax
Immersive sense of speed
Continuous spatial continuity

Visual Style

Ultra-photorealistic
Cinematic
HDR
8K quality
Realistic lighting
Natural shadows
Accurate reflections
Atmospheric haze
Highly detailed architecture
Physically accurate scale
Premium drone cinematography

Critical Instructions

The storyboard in Image 2 defines the exact camera choreography.
The route line is a continuous camera trajectory, not a loose direction guide.
Follow the storyboard timing and movement exactly.
Maintain one uninterrupted continuous flight.
Preserve the environment from Image 1 exactly.

Negative Prompt

Do not render the route lines, arrows, numbered markers, storyboard panels, text, graphs, UI elements, overlays, watermarks, or guide marks. Do not duplicate buildings, distort architecture, change the environment, introduce AI artifacts, flickering, camera jumps, unrealistic motion, excessive fisheye distortion, or hidden cuts.
```

---

## Customizing the Flight Sequence

The Master Prompt includes a default 8-step flight sequence. Customize this section to match YOUR specific path drawing:

### Example Flight Sequences

#### **Architectural Spiral Reveal**
```
• Begin at ground level facing the building entrance
• Move forward while slowly rising
• Begin a clockwise spiral around the building
• Maintain consistent distance from facade during spiral
• Continue spiral climb to rooftop level
• Complete 360-degree rotation
• Pull back while continuing to rise
• End with wide aerial view showing building in city context
```

#### **Landscape Flyover**
```
• Start low over foreground terrain (forest, beach, field)
• Accelerate forward with slight altitude gain
• Pass over mid-ground features (hills, rocks, structures)
• Continue smooth ascent while maintaining forward speed
• Bank gently left/right to reveal side valleys or vistas
• Reach peak altitude at horizon line
• Decelerate slightly for final composition
• End with wide panoramic landscape reveal
```

#### **Urban Chase Sequence**
```
• Begin tight between buildings at street level
• Accelerate rapidly through urban canyon
• Bank hard right around building corner
• Thread through narrow alley or archway
• Burst into open plaza or intersection
• Climb steeply while banking left
• Level out above rooftops
• Pull back for sweeping cityscape finale
```

#### **Product Showcase Orbit**
```
• Start with tight close-up of product detail
• Pull back slowly while beginning clockwise orbit
• Maintain constant distance during first 180-degree arc
• Reveal product context and environment
• Continue orbit while slowly rising
• Complete full 360-degree circle
• Pull back to medium-wide shot
• End with product centered in beautiful setting
```

#### **Coastal Approach**
```
• Begin over open ocean with low altitude
• Fly toward coastline with strong forward momentum
• Pass over waves and surf zone
• Accelerate up beach toward cliffs or buildings
• Bank around coastal feature (lighthouse, rock formation)
• Climb rapidly while turning inland
• Reveal full coastal panorama
• End with wide aerial showing ocean-land interface
```

---

## Advanced Techniques

### 1. Multi-Altitude Choreography

**Technique:** Vary altitude dramatically during flight for dynamic reveals

**Path drawing:**
- Draw path with vertical arrows indicating climbs/descents
- Label altitudes: "Ground," "Mid," "High," "Descent"
- Show gradual vs. rapid altitude changes

**Prompt modification:**
```
Begin at ground level (0-5 feet altitude). Climb gradually to 20 feet during forward movement. Rapidly ascend to 100 feet during spiral. Peak at 200 feet for final pullback. All altitude changes must be smooth and continuous.
```

### 2. Speed Variation

**Technique:** Create rhythm by varying flight speed

**Path drawing:**
- Use speed lines or motion blur indicators
- Label sections: "Slow reveal," "Accelerate," "Fast pass," "Decelerate"
- Thicker lines = faster movement

**Prompt modification:**
```
Camera Style: Begin with slow, deliberate movement (5 mph). Accelerate to high-speed flight (40 mph) during approach. Decelerate during spiral (15 mph). Final pullback at medium speed (20 mph).
```

### 3. Proximity Variation

**Technique:** Move closer and farther from subject for dramatic effect

**Path drawing:**
- Show path weaving close to and away from structures
- Label: "Close pass," "Wide arc," "Intimate detail"

**Prompt modification:**
```
Fly within 3 feet of facade during climb. Maintain 15-foot distance during spiral. Pull back to 50+ feet for finale. Preserve sense of scale and danger during close passes.
```

### 4. Banking and Tilting

**Technique:** Add dynamic camera roll during turns

**Path drawing:**
- Curved arrows with rotation indicators
- Tilt symbols showing camera angle

**Prompt modification:**
```
Camera Style: Add realistic FPV banking during all turns. Bank 25-30 degrees during sweeping approach. Bank 15 degrees during spiral. Level horizon during finale. Natural gimbal stabilization.
```

### 5. Subject Framing

**Technique:** Keep subject in specific frame position throughout flight

**Path drawing:**
- Small storyboard frames showing where subject should appear
- Framing guides: "Center frame," "Right third," "Low frame"

**Prompt modification:**
```
Maintain subject in right third of frame during approach. Center subject during spiral climb. Subject should sink to lower third during final pullback.
```

---

## Flight Pattern Library

### The Spiral Ascent
**Description:** Clockwise or counter-clockwise climb around a central subject  
**Best for:** Tall buildings, monuments, trees, towers  
**Path:** Circular arrow spiraling upward around subject  
**Duration:** 10-15 seconds per full rotation

### The Reveal Pullback
**Description:** Start close, pull back while rising to reveal context  
**Best for:** Products, architecture, landscapes  
**Path:** Straight line moving away from subject with upward arrow  
**Duration:** 8-12 seconds

### The Thread-Through
**Description:** Navigate through tight spaces (arches, alleys, forests)  
**Best for:** Urban environments, natural formations  
**Path:** Weaving line through obstacles  
**Duration:** 5-10 seconds per segment

### The Arc Approach
**Description:** Wide banking approach from side angle  
**Best for:** Dramatic entries, establishing shots  
**Path:** Wide curved line ending at subject  
**Duration:** 8-12 seconds

### The Over-Under
**Description:** Fly over obstacle, descend on far side  
**Best for:** Dynamic terrain, architectural features  
**Path:** Line that rises over feature, descends on other side  
**Duration:** 6-10 seconds

### The Orbit
**Description:** Complete circular path around subject at constant altitude  
**Best for:** 360-degree product/location reveals  
**Path:** Perfect circle around subject  
**Duration:** 12-20 seconds per full orbit

### The Diving Entry
**Description:** Start high, descend rapidly while moving forward  
**Best for:** Dramatic openings, action sequences  
**Path:** Diagonal line descending from top corner  
**Duration:** 5-8 seconds

### The Chase Shot
**Description:** Follow behind moving subject or path  
**Best for:** Roads, rivers, valleys, corridors  
**Path:** Straight or gently curving line at consistent altitude  
**Duration:** 10-20 seconds

---

## Prompt Customization Guide

### Modifying Camera Style

**For slower, more cinematic feel:**
```
Camera Style: Slow, contemplative FPV drone movement. Gentle acceleration. Smooth, floating quality. Stabilized gimbal. Deliberate camera positioning.
```

**For aggressive action feel:**
```
Camera Style: High-speed FPV racing drone. Aggressive acceleration. Sharp banking. Rapid movements. Slight camera shake for realism. Extreme forward momentum.
```

**For real estate/commercial:**
```
Camera Style: Professional commercial drone cinematography. Smooth, controlled movements. Stable horizon. Elegant reveals. Premium production quality.
```

### Modifying Visual Style

**For golden hour:**
```
Visual Style: Golden hour lighting. Warm amber tones. Long dramatic shadows. Soft diffused sunlight. HDR with rich highlights. Cinematic color grade.
```

**For moody/dramatic:**
```
Visual Style: Overcast dramatic skies. Deep contrast. Desaturated colors. Volumetric atmospheric fog. Cinematic noir aesthetic. Film grain texture.
```

**For vibrant/commercial:**
```
Visual Style: Vibrant saturated colors. Crystal clear visibility. Perfect lighting. Commercial photography quality. Clean HDR. Pristine detail.
```

### Modifying Duration

**For longer sequences (20-30 seconds):**
```
Create a hyper-realistic cinematic FPV drone sequence lasting approximately 25 seconds. The camera movement should be deliberately paced to allow viewers to absorb environmental details.
```

**For quick cuts (5-10 seconds):**
```
Create a hyper-realistic cinematic FPV drone sequence lasting approximately 8 seconds. The camera movement should be dynamic and fast-paced for high-energy editing.
```

---

## Troubleshooting Common Issues

### Problem: AI renders the path lines/arrows in the video

**Solution:**
- Strengthen the negative prompt: "CRITICAL: Do not render ANY drawn lines, arrows, markers, text, or overlay elements from Image 2"
- Make path lines more obviously illustrative (use bright unnatural colors)
- Regenerate with emphasis: "Image 2 contains only planning guides, not visual elements to render"

### Problem: Camera doesn't follow the path accurately

**Solution:**
- Simplify the path (fewer complex curves)
- Add more detailed flight sequence description matching your path
- Use numbered checkpoints and describe each transition explicitly
- Emphasize: "Follow the camera path precisely, preserving every curve exactly as illustrated"

### Problem: Multiple cuts or transitions appear instead of continuous shot

**Solution:**
- Add to prompt: "Absolutely zero cuts, transitions, or camera resets"
- Reduce path complexity (shorter total flight)
- Emphasize: "One continuous uninterrupted take from first frame to last"
- Check that path is truly continuous with no breaks

### Problem: Environment changes or distorts during flight

**Solution:**
- Upload cleaner environment reference image (Image 1)
- Strengthen preservation language: "Do not modify the environment in any way"
- Add negative prompt: "Do not duplicate buildings, distort architecture, or introduce new structures"
- Use style reference locking if platform supports it

### Problem: Unrealistic physics or motion

**Solution:**
- Specify drone type more clearly: "Consumer DJI drone" vs. "Racing FPV drone"
- Add physics constraints: "Realistic inertia, natural acceleration, physically accurate movement"
- Reduce complexity of maneuvers (slower spirals, wider turns)
- Add: "Obey real-world physics and momentum"

### Problem: Excessive fisheye distortion

**Solution:**
- Add to negative prompt: "No excessive fisheye distortion, lens aberration, or warping"
- Specify camera: "Standard 24mm equivalent lens, natural field of view"
- Avoid extreme close passes if distortion persists

### Problem: Flickering or AI artifacts

**Solution:**
- Regenerate (sometimes model has random artifacts)
- Simplify lighting: "Consistent natural lighting throughout sequence"
- Add negative prompt: "No flickering, morphing, AI artifacts, or temporal instability"
- Try alternative model (Seedance 2.0 vs. Gemini Omni)

### Problem: Path is too fast or too slow

**Solution:**
- Adjust duration: Change "approximately 15 seconds" to desired length
- Add speed descriptors: "Slow reveal," "moderate speed," "high-speed flight"
- Specify: "Camera moves at [X] mph equivalent speed"

---

## Advanced Workflow Variations

### Multi-Shot Sequence Assembly

**Concept:** Create multiple path-based clips and edit together

**Workflow:**
1. Design 3-5 different paths for the same environment
2. Generate each as separate clip
3. Edit together in post-production
4. Match color grade across all clips

**Benefits:**
- More complex storytelling
- Multiple angles of same subject
- Rhythm and pacing control
- Professional multi-camera feel

### Time-of-Day Variations

**Concept:** Generate same path at different times/lighting

**Images needed:**
- Image 1: Environment at dawn/day/dusk/night
- Image 2: Same path overlay for all versions

**Use cases:**
- Real estate day/night showcases
- Time-lapse assembled from multiple clips
- Lighting comparison demonstrations

### Subject Tracking Integration

**Concept:** Combine path with moving subject

**Prompt addition:**
```
A [car/person/boat] moves along the [road/path/water] below. The drone follows the subject while executing the planned flight path, maintaining the subject in [center/right third/left third] of frame throughout.
```

**Path considerations:**
- Draw subject's path as well as drone path
- Match speeds between subject and drone
- Indicate where they sync up

### Environmental Effects Overlay

**Concept:** Add weather or atmosphere

**Prompt additions:**

**Light rain:**
```
Visual Style: Light rain visible in air. Wet surfaces with reflections. Overcast soft lighting. Water droplets occasionally visible near lens.
```

**Fog/mist:**
```
Visual Style: Atmospheric fog in valleys. Mist reduces visibility in distance. Volumetric god rays through clouds. Mysterious ethereal mood.
```

**Particle effects:**
```
Visual Style: [Falling leaves/snow/dust/petals] drift through the air during flight. Subtle particle motion adds life and scale.
```

---

## Model Comparison

| Model | Best For | Strengths | Weaknesses |
|-------|----------|-----------|------------|
| **Seedance 2.0** | Complex path following | Excellent choreography adherence, smooth camera work | May simplify very complex paths |
| **Gemini Omni** | Photorealism | Superior environmental detail, lighting realism | Sometimes less precise path following |
| **Veo 3.1** | Long duration | Can generate 20+ second clips, native audio | Less path-drawing support currently |
| **Kling 2.5** | Physics accuracy | Realistic momentum and inertia | Requires more prompt detail |

---

## Best Practices Summary

### Image Preparation
1. **Use high-resolution source images** (2K minimum, 4K ideal)
2. **Choose scenes with clear focal points** for dramatic reveals
3. **Ensure good lighting and contrast** in source material
4. **Save clean environment reference** (Image 1) without any markings

### Path Design
1. **Draw continuous, unbroken lines** for seamless camera movement
2. **Use contrasting colors** (red, yellow, cyan) so AI can clearly see path
3. **Indicate direction with arrows** and flow indicators
4. **Mark key moments** with numbered checkpoints
5. **Show altitude changes** explicitly with vertical arrows or labels
6. **Keep paths realistic** — don't exceed physical drone capabilities

### Prompt Writing
1. **Clearly separate Image 1 (environment) from Image 2 (path)** in prompt structure
2. **Emphasize continuity** — "one continuous uninterrupted shot"
3. **Describe flight sequence** in detail, matching your drawn path
4. **Specify camera style** (FPV racing vs. commercial cinema vs. slow reveal)
5. **Include strong negative prompts** to remove UI elements
6. **Match timing** — specify duration that fits your path complexity

### Generation
1. **Upload both images** in correct order (environment first, path second)
2. **Start with default 15-second duration** and adjust based on results
3. **Generate 2-3 variations** to compare results
4. **Note successful techniques** for future projects

### Post-Production
1. **Color grade** for cinematic look (LUTs, curves, saturation)
2. **Add motion blur** if needed for smooth fast movements
3. **Stabilize** if any unwanted shake appears
4. **Add sound design** — wind, drone motors, ambient environment
5. **Speed ramp** strategic moments for emphasis or smoothness

---

## Use Case Gallery

### Real Estate Showcases
**Path:** Approach property → orbit → reveal backyard → pullback for context  
**Duration:** 15-20 seconds  
**Style:** Smooth, elegant, premium commercial

### Product Reveals
**Path:** Tight close-up → spiral around product → pull back to environment  
**Duration:** 10-15 seconds  
**Style:** Clean, controlled, advertising quality

### Travel & Tourism
**Path:** Low approach over terrain → climb landmark → wide panoramic finale  
**Duration:** 15-25 seconds  
**Style:** Cinematic, golden hour, inspiring

### Action Sports Context
**Path:** Chase athlete path → bank around terrain → dramatic aerial pullback  
**Duration:** 8-12 seconds  
**Style:** Fast-paced, aggressive, dynamic

### Architectural Walkthroughs
**Path:** Thread through columns → spiral up facade → rooftop reveal  
**Duration:** 18-25 seconds  
**Style:** Measured, contemplative, detail-focused

### Event Coverage
**Path:** Establish venue → descend into crowd → orbit stage → reveal full scene  
**Duration:** 20-30 seconds  
**Style:** Documentary, natural, energetic

---

## Resource Checklist

### Before Starting
- [ ] High-resolution source image acquired
- [ ] Access to Seedance 2.0 or Gemini Omni (via Google Flow/Higgsfield/Dreamina)
- [ ] Image editing software for path drawing
- [ ] Clear vision of desired camera movement

### During Path Design
- [ ] Path is continuous with no breaks
- [ ] Direction arrows clearly show movement flow
- [ ] Altitude changes are marked
- [ ] Key moments have numbered checkpoints
- [ ] Colors contrast well with background
- [ ] Saved as Image 2 (path version)

### During Generation
- [ ] Image 1 (clean) uploaded first
- [ ] Image 2 (path) uploaded second
- [ ] Master prompt customized for your path
- [ ] Flight sequence matches drawn path
- [ ] Negative prompt includes UI element removal
- [ ] Duration appropriate for path complexity

### Post-Generation
- [ ] Video plays smoothly without cuts
- [ ] Path was followed accurately
- [ ] No drawn elements appear in video
- [ ] Environment preserved correctly
- [ ] Motion looks realistic
- [ ] Ready for post-production or use

---

## Final Tips

**The secret to professional AI drone path footage:**

1. **Simplicity wins** — Start with simple paths, add complexity gradually
2. **Continuity is king** — One unbroken line = one unbroken shot
3. **Be specific** — Detailed flight sequence descriptions yield better results
4. **Separate environment from movement** — Dual reference system prevents environment distortion
5. **Negative prompts matter** — Explicitly state what NOT to render
6. **Speed affects quality** — Slower movements are easier for AI to render smoothly
7. **Iterate and refine** — Generate variations, keep what works, adjust what doesn't
8. **Physics matter** — Impossible maneuvers will look artificial

**Pro Tip:** Create a library of successful path patterns. Once you find a path structure that works well, reuse it with different environments for consistent quality.

---

**Ready to create your first AI drone path video?**

1. Find or create your perfect environment image
2. Draw your dream flight path with clear markers
3. Upload both to Seedance 2.0 or Gemini Omni
4. Paste the customized master prompt
5. Generate and refine

Welcome to the future of aerial cinematography. 🚁

---
