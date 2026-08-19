# The UI Tracking Effect

## Overview

Create Apple Vision Pro-style floating interfaces with AI—no VFX software required. Multiple independent glass cards hover above your laptop, perfectly tracked to its movement in 3D space with realistic glass materials, translucency, and depth.

**Models Used:**

- **Nano Banana Pro** (Floating interface generation)
- **Seedance 2.0 4K** (Animation and motion tracking)

**Platform:** Higgsfield.ai

**Collaboration:** Higgsfield x Diditee Creator Guide

**Visual Concept:** iPhone Control Center reimagined as spatial computing interface—multiple glass cards floating above laptop with liquid glass materials, proper perspective, and perfect tracking as the laptop moves.

---

## Introduction

This is the UI Tracking Effect.

It creates the illusion of a floating Apple Vision Pro style interface that emerges from your laptop and stays perfectly tracked to it as you move.

**And the best part is - you do not need any VFX software.**

**The process is simple:**

1. Generate the floating interface
2. Animate it
3. Track it naturally onto the laptop

---

## Step 1 — Capture Your Shot

Record the movement first, then extract the two reference images that will drive the effect.

### Prepare Your References

First, grab a video of yourself holding a laptop.

**Tilt and move it naturally throughout the shot.**

**Then:**

- Take a screenshot of the first frame of your video

**Next:**

- Take a screenshot of your iPhone Control Centre and crop away all the excess so only the interface remains

---

### Two Reference Images

**REFERENCE 01:** Laptop first frame

- Screenshot from your video
- Shows laptop with your hands
- This is the base scene

**REFERENCE 02:** Cropped Control Centre

- Screenshot of iPhone Control Center
- Cropped to show only the UI elements
- This becomes the style reference for floating cards

**These will become your two reference images.**

---

### Recording Tips

**Laptop movement:**

- Hold laptop naturally
- Tilt and rotate smoothly
- Move gradually throughout shot
- Keep laptop visible in frame
- 5-10 seconds duration

**Camera setup:**

- Stable camera position
- Good lighting
- Clean background
- Focus on laptop
- Capture natural movement

**Hand positioning:**

- Hold laptop securely
- Natural, relaxed grip
- Keep hands visible
- Consistent throughout

---

## Step 2 — Generate the Floating Interface

Build the finished spatial UI as a still image before asking the video model to animate it.

### Navigation

Go to:
**Higgsfield.ai → Create → Images → Nano Banana Pro**

### Upload Requirements

Upload:

- Your laptop screenshot
- Your cropped Control Centre screenshot

**NEXT:** Paste in the exact image prompt below.

---

### Exact Prompt (Nano Banana Pro)

```
Using the uploaded laptop photo and the provided iPhone Control Center as references, transform the Control Center into an Apple Vision Pro-style spatial interface floating above the laptop.

The interface must not be a single panel. Recreate it as multiple independent floating glass cards, exactly matching Apple's original layout. Every module should remain its own separate glass panel with identical spacing, proportions, hierarchy, icons, colors, typography, and arrangement.

Scale the entire interface to be larger than the laptop, extending beyond the display in both width and height. The floating workspace should feel expansive, with the combined arrangement occupying roughly 140% of the laptop's footprint, while keeping every module perfectly balanced.

Each glass card should feel like a physical object suspended in space. Use premium Apple's liquid glass materials with translucency, soft background blur, realistic glass thickness, subtle edge highlights, gentle internal reflections, light refraction, and soft natural shadows. The interface should look identical to Apple's glass UI found in Vision Pro.

The glass must remain visually independent. Do not allow the laptop wallpaper, desktop, or surrounding environment to blend into, tint, or affect the interface. Each card should maintain its own clean frosted appearance regardless of what is behind it.

Every card should be anchored to the laptop in 3D space, floating naturally several inches in front of the screen with accurate perspective and depth. The interface should feel like it originates from the laptop while remaining suspended in mid-air.

Do not merge cards together. Do not redesign, simplify, stretch, crop, rearrange, or modify any UI elements. Preserve every detail exactly.

Avoid sci-fi holograms, neon glows, projection beams, blue lighting, or futuristic visual effects. This should resemble Apple's spatial computing interface, not a hologram.

Keep the laptop, wallpaper, camera angle, lighting, composition, and background completely unchanged.

Transparent glass see through, like liquid glass.
```

---

### Prompt Breakdown

**Primary objective:**

- Transform Control Center into Apple Vision Pro-style spatial interface

**Interface structure:**

- **Multiple independent cards** (not single panel)
- Exactly match Apple's original layout
- Each module = separate glass panel
- Preserve spacing, proportions, hierarchy, icons, colors, typography, arrangement

**Scale:**

- Larger than laptop
- Extend beyond display (width and height)
- ~140% of laptop's footprint
- Every module perfectly balanced

**Glass material requirements:**

- Premium Apple liquid glass materials
- Translucency
- Soft background blur
- Realistic glass thickness
- Subtle edge highlights
- Gentle internal reflections
- Light refraction
- Soft natural shadows
- Identical to Apple's Vision Pro glass UI

**Visual independence:**

- Glass must remain visually independent
- Do NOT allow laptop wallpaper/desktop/environment to blend in
- Each card maintains clean frosted appearance
- Not affected by background

**3D spatial positioning:**

- Every card anchored to laptop in 3D space
- Floating several inches in front of screen
- Accurate perspective and depth
- Originates from laptop
- Remains suspended in mid-air

**Preservation requirements:**

- Do NOT merge cards together
- Do NOT redesign, simplify, stretch, crop, rearrange, or modify
- Preserve every detail exactly

**What to avoid:**

- Sci-fi holograms
- Neon glows
- Projection beams
- Blue lighting
- Futuristic visual effects
- This is Apple spatial computing, NOT a hologram

**What to preserve:**

- Laptop, wallpaper, camera angle, lighting, composition, background completely unchanged

**Final note:** Transparent glass see through, like liquid glass

---

## Step 3 — Animate The Interface

Use the finished image as the visual target, then track the floating cards naturally to the laptop movement.

### Navigate to Video Generation

Go back to:
**Create → Videos**

Select:
**Seedance 2.0 4K**

### Important Setting Change

**Before generating:**
Change the bitrate from:
**STANDARD → HIGH**

This gives you a much sharper and less compressed result, which is especially useful for heavy visual effects like this.

---

### Upload Requirements

Upload:

- Your original laptop video
- The AI-generated floating interface image

---

### Exact Prompt (Seedance 2.0 4K)

```
Use the uploaded video as the base video and the uploaded image as the visual reference.

At the beginning of the video, only the laptop is visible. The floating glass interface gradually appears from the laptop screen, with each card smoothly animating into place one after another.

Once fully visible, keep the interface perfectly attached to the laptop for the rest of the video. As the laptop moves, rotates, and tilts, the interface follows naturally with accurate tracking.

Keep the layout, glass appearance, and positioning similar to the reference image. Do not change the video or background.
```

---

### Prompt Breakdown

**Base inputs:**

- Uploaded video = base video
- Uploaded image = visual reference

**Animation sequence:**

- **Beginning:** Only laptop visible
- **Appearance:** Floating glass interface gradually appears from laptop screen
- **Sequential animation:** Each card smoothly animates into place one after another

**Tracking behavior:**

- Once fully visible: interface perfectly attached to laptop
- As laptop moves, rotates, tilts: interface follows naturally
- Accurate tracking throughout

**Preservation:**

- Keep layout, glass appearance, positioning similar to reference image
- Do NOT change the video or background

---

## Why This Workflow Works

### Stable. Controlled. Believable.

**Nano Banana Pro** is used to generate the final interface exactly how you want it to look.

**Seedance 2.0 4K** then uses that generated image as a visual target and animates the interface while keeping it perfectly attached to the laptop throughout the shot.

**Because the animation is driven from your generated image, the final result feels much more stable and believable than trying to generate everything in a single step.**

---

### Two-Step Advantage

**Step 1 (Nano Banana Pro):**

- Full control over final appearance
- Precise glass material specification
- Exact card layout and spacing
- Perfect Control Center replication
- Time to refine and regenerate

**Step 2 (Seedance 2.0 4K):**

- Uses perfect reference as target
- Focuses only on animation and tracking
- Maintains visual quality from Step 1
- Natural motion tracking
- Smooth card appearance animation

**Result:**

- Much more stable than single-step generation
- Believable spatial computing effect
- Professional-quality tracking
- Consistent glass materials throughout

---

## Complete Workflow Summary

### Pre-Production

1. Plan your laptop movement
2. Set up camera and lighting
3. Prepare clean background
4. Screenshot iPhone Control Center

### Production (Recording)

1. Position camera with stable mount
2. Hold laptop naturally
3. Record 5-10 seconds with natural tilting/movement
4. Screenshot first frame of video

### Preparation

1. Crop Control Center screenshot (remove excess)
2. Verify laptop screenshot quality
3. Have both reference images ready

### Generation (Nano Banana Pro)

1. Upload laptop screenshot + cropped Control Center
2. Use exact Nano Banana prompt
3. Generate floating interface image
4. Review for proper glass materials and card separation
5. Regenerate if needed

### Animation (Seedance 2.0 4K)

1. Upload original laptop video + generated interface image
2. Change bitrate: STANDARD → HIGH
3. Use exact Seedance 2.0 prompt
4. Generate animated tracking video
5. Download result

### Post-Production (Optional)

1. Import to video editor if needed
2. Add sound effects (UI sounds, ambient)
3. Color grade if desired
4. Add background music
5. Export final video

---

## Tips for Best Results

### Recording Tips

- **Smooth movement:** Gradual tilts and rotations
- **Stable camera:** Tripod or solid surface
- **Good lighting:** Soft, even lighting on laptop
- **Clean background:** Less cluttered = better tracking
- **Laptop visibility:** Keep entire laptop in frame
- **Natural motion:** Don't move too quickly

### Control Center Screenshot Tips

- **High resolution:** Use highest quality screenshot
- **Careful cropping:** Remove all excess (status bar, edges)
- **Clean capture:** No notifications blocking elements
- **Complete UI:** All cards visible and accessible
- **Sharp image:** No blur or compression

### Generation Tips

- **Read prompt carefully:** Every detail matters
- **Verify card separation:** Should see individual glass cards
- **Check glass materials:** Translucent, frosted, liquid glass
- **Proper scale:** Interface should be ~140% of laptop size
- **Regenerate if needed:** Don't settle for poor result
- **Use HIGH bitrate:** Essential for Seedance 2.0 4K quality

### Tracking Tips

- **Shorter clips track better:** 5-10 seconds ideal
- **Smooth motion helps:** Jerky movement = tracking issues
- **Laptop always visible:** Must be in frame entire duration
- **Reference quality matters:** Better Nano Banana result = better tracking

---

## Troubleshooting

### Problem: Cards merge into single panel

**Solution:**

- Re-emphasize in Nano Banana prompt: "must not be a single panel"
- Add: "Every module should remain its own separate glass panel"
- Verify Control Center screenshot shows clear card separation
- Regenerate with emphasis on "multiple independent floating glass cards"

### Problem: Glass doesn't look like Vision Pro

**Solution:**

- Emphasize "liquid glass materials"
- Request "translucency, soft background blur, realistic glass thickness"
- Add "identical to Apple's glass UI found in Vision Pro"
- Specify "avoid sci-fi holograms, neon glows"
- Show clearer reference if possible

### Problem: Laptop wallpaper/desktop bleeds into glass

**Solution:**

- Emphasize: "glass must remain visually independent"
- Add: "clean frosted appearance regardless of what is behind it"
- Specify: "do not allow laptop wallpaper, desktop, or environment to blend in"
- Regenerate with stronger independence language

### Problem: Interface looks flat, not 3D

**Solution:**

- Request "accurate perspective and depth"
- Emphasize "floating several inches in front of screen"
- Add "feel like physical objects suspended in space"
- Specify "anchored to laptop in 3D space"

### Problem: Tracking drifts or slides

**Solution:**

- Use HIGH bitrate in Seedance 2.0 4K
- Record shorter video clip (5 seconds vs 10)
- Ensure laptop stays clearly visible
- Smoother movement helps tracking
- Regenerate with emphasis on "perfectly attached to laptop"

### Problem: Cards don't animate in sequentially

**Solution:**

- Emphasize in Seedance prompt: "each card smoothly animating into place one after another"
- Add: "gradually appears from the laptop screen"
- Specify timing: "sequential animation"
- Regenerate if simultaneous appearance occurs

### Problem: Interface changes from reference image

**Solution:**

- Emphasize: "keep layout, glass appearance, and positioning similar to reference image"
- Add: "use uploaded image as exact visual reference"
- Verify you uploaded correct generated image
- Regenerate with stronger adherence language

---

## Creative Variations

### Different UI Sources

**iPhone Control Center (Default):**

- Quick settings interface
- Multiple modular cards
- iOS design language

**macOS Control Center:**

- Mac-specific controls
- Different card layout
- macOS aesthetic

**Android Quick Settings:**

- Material You design
- Tile-based layout
- Google design language

**Custom Dashboard:**

- Create your own card layout in Figma
- Personal app icons
- Custom information cards

### Different Scale Options

**Compact (100%):**

- Same size as laptop screen
- More contained look
- Less dramatic

**Standard (140%):**

- Extends beyond laptop
- Recommended size
- Balanced and dramatic

**Expansive (180%):**

- Much larger than laptop
- Very dramatic
- Workspace takeover feel

### Different Glass Styles

**Apple Vision Pro (Default):**

- Liquid glass
- Subtle frost
- Premium look

**Futuristic:**

- More transparency
- Glowing edges
- Sci-fi aesthetic

**Minimal:**

- Very subtle glass
- Less frost
- Clean and simple

**Bold:**

- Stronger frosting
- More visible edges
- Pronounced depth

---

## Advanced Techniques

### Multi-Stage Interaction

**Stage 1:** Laptop with no interface (plain video)
**Stage 2:** Interface appears and tracks (Seedance output)
**Stage 3:** Interface disappears or changes (additional generation)

Edit together for full interaction sequence.

### Multiple Interface Configurations

Generate multiple interface variations:

1. Control Center
2. App windows
3. Notification center
4. Custom widgets

Cut between different interface states.

### Camera Perspective Changes

Record from different angles:

- Eye-level view
- Top-down perspective
- Side angle
- Close-up

Each shows interface depth differently.

### Environmental Integration

Add elements that enhance spatial computing feel:

- Hand gestures interacting with cards
- Shadows cast by interface
- Lighting changes
- Desk objects for depth reference

---

## Content Applications

### Product Demos

- **Laptop marketing:** Showcase capabilities
- **Software demos:** Visualize interfaces
- **AR/VR content:** Spatial computing concepts
- **Tech reviews:** Future interface previews

### Social Media Content

- **Instagram Reels:** Quick tech showcases
- **TikTok:** Viral spatial computing demos
- **YouTube Shorts:** Interface reveals
- **LinkedIn:** Professional tech content

### Creative Projects

- **Sci-fi concepts:** Future workspace visions
- **UI/UX demos:** Interface design presentations
- **Tech storytelling:** Innovation narratives
- **Art projects:** Digital/physical blending

### Educational Content

- **Spatial computing tutorials:** Explain concepts
- **Vision Pro content:** Preview experiences
- **Design education:** Interface design principles
- **Technology explainers:** Future tech demos

---

## Technical Specifications

### Recording Settings

- **Resolution:** 1080p or 4K
- **Frame rate:** 24fps, 30fps, or 60fps
- **Lighting:** Soft, even lighting
- **Camera:** Stable position (tripod)
- **Duration:** 5-10 seconds optimal

### Screenshot Requirements

- **Laptop frame:** First frame of video, high resolution
- **Control Center:** High quality, carefully cropped
- **Format:** JPG or PNG
- **Quality:** No compression artifacts

### Nano Banana Pro Settings

- **Model:** Nano Banana Pro
- **Input:** Laptop screenshot + Control Center screenshot
- **Prompt:** Full detailed prompt
- **Output:** High-resolution interface image

### Seedance 2.0 4K Settings

- **Model:** Seedance 2.0 4K
- **Bitrate:** HIGH (not Standard)
- **Input:** Original video + generated interface image
- **Prompt:** Animation and tracking prompt
- **Output:** 4K video with tracked interface

### Export Settings

- **Resolution:** Match source (1080p or 4K)
- **Frame rate:** Match source
- **Format:** MP4 (H.264)
- **Bitrate:** High quality

---

## Platform-Specific Optimization

### Instagram Reels / TikTok

- **Format:** 9:16 vertical (may need to reframe)
- **Duration:** 7-15 seconds ideal
- **Hook:** Show plain laptop first, then interface appears
- **Captions:** Explain what viewers are seeing

### YouTube Shorts

- **Format:** 9:16 vertical
- **Duration:** 15-60 seconds
- **Context:** Brief explanation of effect
- **Thumbnail:** Frame showing floating interface

### Instagram Feed

- **Format:** 4:5 or 1:1
- **Duration:** 15-30 seconds
- **Style:** Polished, professional
- **Caption:** Explain Vision Pro concept

### YouTube (Standard)

- **Format:** 16:9 horizontal
- **Duration:** Can be part of longer video
- **Context:** Full tutorial or tech showcase
- **Behind-the-scenes:** Show workflow

### LinkedIn

- **Format:** 16:9 or 1:1
- **Tone:** Professional, innovative
- **Context:** Future of work, spatial computing
- **Message:** Technology advancement focus

---

## Cost Considerations

**Higgsfield.ai:**

- Nano Banana Pro: Requires credits
- Seedance 2.0 4K: Requires credits
- HIGH bitrate: May cost more credits
- Check current pricing at higgsfield.ai

**Total Workflow:**

- 1-2 Nano Banana generations (refining interface)
- 1-2 Seedance generations (getting tracking right)
- Typical total: 2-4 credits

**Project Time:**

- Recording: 10-15 minutes
- Screenshot prep: 5 minutes
- Nano Banana generation: 5-10 minutes
- Seedance generation: 10-20 minutes
- Optional editing: 10-20 minutes
- **Total: 45-90 minutes**

---

## Learning Resources

**Similar Effects:**

- Apple Vision Pro spatial computing demos
- AR interface mockups
- Holographic UI concepts
- Glass morphism design

**Skills to Develop:**

- AI prompt engineering
- Understanding spatial computing
- Glass material design
- Motion tracking concepts

**Related Tutorials:**

- Apple Vision Pro interface design
- Glass morphism in UI design
- Motion graphics basics
- AR/VR interface principles

---

## Credits

**Collaboration:** Higgsfield x Diditee

**Creator:** @**diditee**

**Platform:** Higgsfield.ai

**Models:** Nano Banana Pro + Seedance 2.0 4K

---

## Thank You

And that's the UI Tracking Effect.

Create Apple Vision Pro-style floating glass interfaces that emerge from your laptop and track perfectly to its movement—all without VFX software.

**Follow @**diditee** for more creator guides.**

---

## Quick Reference

**Workflow:** Record → Screenshot → Generate Interface (Nano Banana) → Animate & Track (Seedance)

**Tools:** Higgsfield.ai (Nano Banana Pro + Seedance 2.0 4K)

**Key Settings:** HIGH bitrate for Seedance 2.0 4K

**Reference Images:** Laptop first frame + Cropped Control Center

**Duration:** 45-90 minutes total

**Difficulty:** Intermediate

**Best For:** Tech demos, spatial computing content, AR/VR concepts, product marketing

**Pro Tip:** Two-step workflow (generate then animate) produces much more stable and believable results than single-step generation
