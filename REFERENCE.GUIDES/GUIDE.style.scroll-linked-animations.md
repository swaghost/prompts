# Scroll-Linked Animation — AI-Generated Website Effects

## Description

Create premium scroll-linked animations for websites using AI — the same $5,000 effect Apple uses on product pages, built in 10 minutes. Generate start and end frames with Google Whisk, animate the transition with Google Veo, extract individual frames, and build the scroll effect with Cursor AI. Perfect for product showcases, interactive storytelling, portfolio pieces, and landing pages. Uses AI for 90% of the work: image generation, animation, and code — you focus on vision and experience.

## Tools Required

- **Google Whisk** — AI image generation for start and end frames
- **Google Veo** — AI video generation (Frames to Video mode)
- **EZGif** — Video-to-JPG converter (extracts frames at 30fps)
- **Cursor AI** — AI-powered code editor with Agent mode
- **Next.js 14** — React framework (App Router)
- **Framer Motion** — Animation library
- **Tailwind CSS** — Styling framework
- **HTML5 Canvas** — Performance-optimized frame rendering

## What You'll Learn

- Creating "exploded view" product animations with AI
- Using Frames-to-Video AI animation (Google Veo)
- Converting videos into frame sequences for scroll interaction
- Building scroll-linked scrubbing with HTML5 Canvas
- Using Cursor AI Agent mode to generate complete components
- Performance optimization for 60fps smooth scrolling
- Seamless background blending techniques
- Creating Awwwards-level "scrollytelling" experiences

---

## Complete Workflow

### Overview

**5-Step Process:**

1. Create start and end frames (Google Whisk)
2. Animate between frames (Google Veo)
3. Extract frames from video (EZGif)
4. Drop frames into project
5. Build scroll effect (Cursor AI)

**Duration:** 10 minutes  
**Difficulty:** Beginner  
**Output:** Apple-style scroll animation

---

## Step 1: Create Your Animation Frames

**Tool:** Google Whisk  
**Goal:** Generate start frame and end frame  
**Link:** [labs.google/fx/tools/whisk](https://labs.google/fx/tools/whisk)

### The Concept

Create **two images**:

1. **Start Frame:** Product in intact state
2. **End Frame:** Product in "exploded view" (components separated)

**Why this works:**

- Veo will animate the transition between states
- Exploded view reveals internal components
- Creates impressive "technical showcase" effect
- Perfect for products with interesting internals

---

### Image Generation Prompt

Paste this prompt into Google Whisk to generate both frames:

```
Ultra-premium product photography of wireless headphones, matte black finish with brushed aluminum accents, soft ambient lighting from top-left, floating on matte black surface. Deep black background with subtle gradient, studio lighting, hyper-realistic 3D render, shallow depth of field, 4k cinematic quality, no text, no logos, luxury tech aesthetic, sharp focus on product, modern minimalist composition.
```

**Generate twice:**

- **First generation:** Intact headphones (start frame)
- **Second generation:** Modify prompt to "exploded view with all components separated — drivers, battery, ear cushions, circuit board floating apart"

---

### Prompt Customization

#### For Different Products

**Smartphone:**

```
Ultra-premium product photography of smartphone, sleek glass and metal design, soft ambient lighting from top-left, floating on matte black surface. Deep black background with subtle gradient, studio lighting, hyper-realistic 3D render, shallow depth of field, 4k cinematic quality, no text, no logos, luxury tech aesthetic, sharp focus on product, modern minimalist composition.
```

**End frame variant:** "exploded view showing screen, battery, circuit boards, camera modules, frame components separated and floating"

**Smartwatch:**

```
Ultra-premium product photography of smartwatch, premium stainless steel and sapphire crystal, soft ambient lighting from top-left, floating on matte black surface. Deep black background with subtle gradient, studio lighting, hyper-realistic 3D render, shallow depth of field, 4k cinematic quality, no text, no logos, luxury tech aesthetic, sharp focus on product, modern minimalist composition.
```

**End frame variant:** "exploded view showing watch face, sensors, battery, band mechanism, internal components separated"

**Camera:**

```
Ultra-premium product photography of professional camera, black and metal finish, soft ambient lighting from top-left, floating on matte black surface. Deep black background with subtle gradient, studio lighting, hyper-realistic 3D render, shallow depth of field, 4k cinematic quality, no text, no logos, luxury tech aesthetic, sharp focus on product, modern minimalist composition.
```

**End frame variant:** "exploded view showing lens assembly, sensor, mirror, shutter mechanism, body parts separated"

---

### Key Prompt Elements

**Always include:**

- **"Ultra-premium product photography"** — Sets quality expectation
- **Specific product description** — Clear subject identification
- **"Floating on [surface]"** — Creates depth separation
- **"Deep black background with subtle gradient"** — Critical for web blending
- **"Soft ambient lighting from top-left"** — Consistent lighting direction
- **"Hyper-realistic 3D render"** — Ensures technical aesthetic
- **"4k cinematic quality"** — High resolution output
- **"No text, no logos"** — Clean product focus
- **"Shallow depth of field"** — Cinematic photography feel

**Critical for web integration:**

- **"Deep black background"** — Enables seamless blending with website background
- **"Subtle gradient"** — Adds depth without harsh edges
- **"Matte black surface"** — Grounds the floating product

---

## Step 2: Animate Your Frames

**Tool:** Google Veo  
**Goal:** Create smooth animation between start and end frames  
**Link:** [deepmind.google/technologies/veo](https://deepmind.google/technologies/veo/)

### Process

1. Open Google Veo
2. Select **"Frames to Video"** mode
3. Upload **start frame** (intact product)
4. Upload **end frame** (exploded view)
5. Generate video

**What Veo does:**

- Analyzes both frames
- Calculates motion path for each component
- Generates smooth in-between frames
- Creates seamless morph animation
- AI fills in all intermediate motion

**Duration:** Veo typically generates 3-10 second videos  
**Quality:** High-resolution, smooth motion

---

### Tips for Best Results

**Frame consistency:**

- Use same lighting in both frames
- Keep camera angle identical
- Match background exactly
- Maintain product scale/position

**Composition:**

- Center product in both frames
- Allow space for components to separate
- Keep exploded parts within frame bounds
- Maintain visual balance

**If animation isn't smooth:**

- Regenerate with more similar frames
- Adjust exploded view to smaller separation distances
- Ensure lighting matches between frames
- Try intermediate step (partially exploded frame)

---

## Step 3: Turn Video Into Scroll Frames

**Tool:** EZGif  
**Goal:** Extract individual frames from video  
**Link:** [ezgif.com/video-to-jpg](https://ezgif.com/video-to-jpg)

### Process

1. Go to EZGif video-to-JPG converter
2. Upload your Veo-generated video
3. Set frame rate to **30fps**
4. Click "Convert to JPG"
5. Download as ZIP file

**What you get:**

- ~240 frames (for 8-second video at 30fps)
- Each frame becomes one "step" in scroll animation
- Higher fps = smoother scrolling (but larger file size)
- Lower fps = more performant (but choppier)

---

### Frame Rate Considerations

**30fps (Recommended):**

- Smooth enough for most scroll interactions
- ~240 frames for 8-second video
- Good balance of quality and performance
- Standard for web animations

**60fps (Premium):**

- Ultra-smooth scrolling
- ~480 frames for 8-second video
- Larger file size
- Best for hero animations

**15fps (Performance):**

- More choppy but very performant
- ~120 frames for 8-second video
- Good for mobile-first projects
- Faster loading

---

### File Management

**After downloading:**

1. Unzip the frame folder
2. Rename files sequentially if needed (frame-001.jpg, frame-002.jpg, etc.)
3. Optimize images (optional):
   - Compress with TinyPNG or similar
   - Convert to WebP for better performance
   - Consider responsive sizing
4. Prepare for upload to project

**File size tips:**

- Compress to 80-85% quality (minimal visual loss)
- Use WebP format for 25-35% smaller files
- Consider lazy loading for frames
- Use CDN for faster delivery

---

## Step 4: Drop It Into Your Project

**Goal:** Organize frames in project structure  
**Location:** Next.js public directory

### File Structure

```
your-project/
├── public/
│   └── frames/
│       ├── frame-001.jpg
│       ├── frame-002.jpg
│       ├── frame-003.jpg
│       └── ... (all 240 frames)
├── src/
│   └── app/
│       └── page.tsx
└── ...
```

**Why `public/`?**

- Static assets accessible at runtime
- No build-time processing needed
- Direct URL access: `/frames/frame-001.jpg`
- Fast loading with Next.js optimization

---

### Alternative Structures

**For multiple animations:**

```
public/
├── frames/
│   ├── headphones/
│   │   ├── frame-001.jpg
│   │   └── ...
│   ├── watch/
│   │   ├── frame-001.jpg
│   │   └── ...
│   └── camera/
│       ├── frame-001.jpg
│       └── ...
```

**For different device sizes:**

```
public/
├── frames/
│   ├── desktop/
│   │   ├── frame-001.jpg (1920px)
│   │   └── ...
│   ├── tablet/
│   │   ├── frame-001.jpg (1024px)
│   │   └── ...
│   └── mobile/
│       ├── frame-001.jpg (640px)
│       └── ...
```

---

## Step 5: Build the Scroll Effect in Cursor

**Tool:** Cursor AI (Agent mode)  
**Goal:** Generate complete scroll component with all code  
**Link:** [cursor.sh](https://cursor.sh/)

### The Master Prompt

Open Cursor AI, activate Agent mode, and paste this complete prompt:

```
ACT AS:
A world-class Creative Developer (Awwwards-level) specializing in Next.js, Framer Motion, and scroll-based animations.

THE TASK:
Build a high-end "Scrollytelling" landing page for fictional premium wireless headphones called "SonicWave Pro".

The core mechanic is a scroll-linked animation that plays an image sequence of headphones "exploding" (disassembling into components) as the user scrolls down.

TECH STACK:
- Framework: Next.js 14 (App Router)
- Styling: Tailwind CSS
- Animation: Framer Motion
- Rendering: HTML5 Canvas (for performance)

VISUAL DIRECTION & COLOR:
- Seamless Blending: The background of the website MUST match the background color of the image sequence exactly so the image edges are invisible. Use an eyedropper on the images to get the exact hex.
- Color Palette: Pure Dark Mode. Use '#050505' or match the image background as the page background. Text should be 'text-white/90' for headings and 'text-white/60' for body.
- Typography: Inter or SF Pro. Clean, tracking-tight, minimalist.

INTERACTION:
- As the user scrolls, the image sequence should scrub forward/backward frame-by-frame, synced to scroll position.
- Smooth, buttery 60fps performance.
- Add subtle parallax text overlays (e.g., "Sound Redefined", "SonicWave Pro") that fade in/out as the user scrolls.

STRUCTURE:
- Hero section with scroll prompt ("Scroll to Explore")
- Scroll-linked animation section (the image sequence)
- Footer with CTA

Use best practices for performance, accessibility, and responsive design.
```

---

### What Cursor Generates

**Complete Next.js component with:**

- Canvas-based frame scrubbing
- Scroll position tracking
- Frame calculation based on scroll percentage
- Image preloading for smooth playback
- Parallax text animations
- Responsive design
- Performance optimizations

**Typical output structure:**

```typescript
"use client";

import { useEffect, useRef, useState } from "react";
import { motion, useScroll, useTransform } from "framer-motion";

export default function ScrollAnimation() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const [images, setImages] = useState<HTMLImageElement[]>([]);

  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"],
  });

  // Frame scrubbing logic
  // Canvas rendering
  // Text animations
  // ...
}
```

---

### Customizing the Generated Code

**Adjust frame path:**

```typescript
// Change this line to match your folder structure
const frameCount = 240;
const currentFrame = (index: number) =>
  `/frames/frame-${(index + 1).toString().padStart(3, "0")}.jpg`;
```

**Change scroll sensitivity:**

```typescript
// Make animation happen over more/less scroll distance
const { scrollYProgress } = useScroll({
  target: containerRef,
  offset: ["start start", "end end"], // Adjust these
});
```

**Modify text overlays:**

```typescript
<motion.h1
  style={{ opacity: useTransform(scrollYProgress, [0, 0.3], [1, 0]) }}
>
  Your Custom Text
</motion.h1>
```

---

## Technical Deep Dive

### How Canvas Rendering Works

**Why Canvas instead of img tags?**

- **Performance:** Direct pixel manipulation, no DOM reflows
- **Smooth playback:** 60fps with hundreds of frames
- **Control:** Precise frame timing and rendering
- **File loading:** Preload all frames, render on demand

**The rendering loop:**

```typescript
useEffect(() => {
  if (!canvasRef.current || images.length === 0) return;

  const canvas = canvasRef.current;
  const context = canvas.getContext("2d");

  const frameIndex = Math.floor(scrollYProgress.get() * (frameCount - 1));
  const img = images[frameIndex];

  if (context && img) {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.drawImage(img, 0, 0, canvas.width, canvas.height);
  }
}, [scrollYProgress, images]);
```

---

### Preloading Strategy

**Load all frames on mount:**

```typescript
useEffect(() => {
  const loadedImages: HTMLImageElement[] = [];

  for (let i = 0; i < frameCount; i++) {
    const img = new Image();
    img.src = currentFrame(i);
    img.onload = () => {
      loadedImages[i] = img;
      if (loadedImages.length === frameCount) {
        setImages(loadedImages);
      }
    };
  }
}, []);
```

**Why preload?**

- Eliminates loading flicker during scroll
- Ensures smooth playback
- No frame skipping or stuttering
- Better user experience

**Trade-offs:**

- Initial load time (show loading state)
- Memory usage (240 images in memory)
- Consider lazy loading for very long sequences

---

### Scroll Mapping

**Convert scroll position to frame index:**

```typescript
const scrollYProgress = useScroll(); // 0 to 1
const frameCount = 240;
const frameIndex = Math.floor(scrollYProgress * (frameCount - 1));
```

**Scroll ranges:**

- `scrollYProgress = 0` → First frame (intact product)
- `scrollYProgress = 0.5` → Middle frame (mid-explosion)
- `scrollYProgress = 1` → Last frame (fully exploded)

**Bidirectional scrubbing:**

- Scroll down → Forward through frames
- Scroll up → Backward through frames
- Natural, intuitive interaction

---

### Parallax Text Animation

**Fade in/out based on scroll:**

```typescript
const opacity = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [1, 0, 0, 1])

<motion.div style={{ opacity }}>
  Your text content
</motion.div>
```

**Multiple text layers:**

```typescript
// Headline: visible at start
const headlineOpacity = useTransform(scrollYProgress, [0, 0.2], [1, 0]);

// Mid-scroll text: visible in middle
const midOpacity = useTransform(scrollYProgress, [0.3, 0.5, 0.7], [0, 1, 0]);

// Footer text: visible at end
const footerOpacity = useTransform(scrollYProgress, [0.8, 1], [0, 1]);
```

---

## Advanced Techniques

### Seamless Background Blending

**Critical for professional look:**

1. Extract exact background color from frames using eyedropper
2. Set website background to match precisely
3. Image edges become invisible
4. Product appears to float in space

**Implementation:**

```css
/* In globals.css or component */
body {
  background: #050505; /* Match your frame background exactly */
}

canvas {
  background: transparent; /* Let body background show through */
}
```

**Testing:**

- View at different scroll positions
- Check on different displays
- Verify no visible edges or boxes
- Ensure seamless integration

---

### Responsive Sizing

**Make canvas responsive:**

```typescript
useEffect(() => {
  const handleResize = () => {
    if (canvasRef.current) {
      const container = canvasRef.current.parentElement;
      canvasRef.current.width = container?.offsetWidth || window.innerWidth;
      canvasRef.current.height = container?.offsetHeight || window.innerHeight;
    }
  };

  handleResize();
  window.addEventListener("resize", handleResize);
  return () => window.removeEventListener("resize", handleResize);
}, []);
```

**Mobile considerations:**

- Reduce frame count for mobile (every other frame)
- Smaller image dimensions for mobile
- Consider touch scroll momentum
- Test on actual devices

---

### Loading State

**Show progress while frames load:**

```typescript
const [loadProgress, setLoadProgress] = useState(0)

// During preload
img.onload = () => {
  loadedImages[i] = img
  setLoadProgress((i + 1) / frameCount * 100)

  if (loadedImages.length === frameCount) {
    setImages(loadedImages)
  }
}

// In render
{loadProgress < 100 && (
  <div className="loading">
    <p>Loading: {Math.floor(loadProgress)}%</p>
  </div>
)}
```

---

### Performance Optimization

**Techniques for smooth 60fps:**

1. **Use requestAnimationFrame:**

```typescript
useEffect(() => {
  let rafId: number;

  const render = () => {
    // Render logic here
    rafId = requestAnimationFrame(render);
  };

  render();
  return () => cancelAnimationFrame(rafId);
}, []);
```

2. **Throttle scroll events:**

```typescript
import { throttle } from "lodash";

const handleScroll = throttle(() => {
  // Scroll logic
}, 16); // ~60fps
```

3. **Optimize image size:**

- Compress frames to reasonable quality
- Use appropriate dimensions (don't use 4K if displaying at 1080p)
- Convert to WebP format

4. **Lazy load frames:**

```typescript
// Load first 20 frames immediately, rest progressively
const priorityFrames = 20;
// Implementation...
```

---

### Multi-Sequence Animations

**Multiple products on one page:**

```typescript
<ScrollAnimation
  frameFolder="/frames/headphones"
  frameCount={240}
  title="SonicWave Pro"
/>

<ScrollAnimation
  frameFolder="/frames/watch"
  frameCount={180}
  title="TimeFlow Elite"
/>

<ScrollAnimation
  frameFolder="/frames/camera"
  frameCount={300}
  title="VisionX Pro"
/>
```

**Reusable component:**

```typescript
interface ScrollAnimationProps {
  frameFolder: string;
  frameCount: number;
  title: string;
  subtitle?: string;
}

export default function ScrollAnimation({
  frameFolder,
  frameCount,
  title,
  subtitle,
}: ScrollAnimationProps) {
  // Implementation with props
}
```

---

## Use Cases and Applications

### Product Launches

**Tech products:**

- Smartphones showing internal components
- Headphones revealing drivers and battery
- Smartwatches displaying sensor technology
- Cameras exploding into lens assemblies

**Why it works:**

- Demonstrates build quality
- Shows advanced engineering
- Creates premium perception
- Engages viewers through interaction

---

### Portfolio Pieces

**For designers/developers:**

- Showcase technical skills
- Demonstrate animation expertise
- Stand out in applications
- Build Awwwards-worthy projects

**For product designers:**

- Explain product assembly
- Highlight material choices
- Show manufacturing process
- Create interactive case studies

---

### Educational Content

**Technical explanations:**

- How products are assembled
- Component identification
- Manufacturing processes
- Engineering principles

**Interactive learning:**

- User controls pace with scrolling
- Can scroll back to review
- Visual + text information
- Engaging alternative to static diagrams

---

### Marketing Campaigns

**Landing pages:**

- Premium product announcements
- Limited edition releases
- Brand storytelling
- Feature highlights

**Social media:**

- Export as video for Instagram/TikTok
- Share scroll animation screen recording
- Drive traffic to interactive version
- Viral-worthy premium content

---

## Troubleshooting

### Problem: Frames not loading or showing broken images

**Solution:**

- Verify frame path is correct: `/frames/frame-001.jpg`
- Check all frames uploaded to `public/frames/`
- Ensure sequential naming (001, 002, 003...)
- Check browser console for 404 errors
- Try absolute path: `${window.location.origin}/frames/...`

---

### Problem: Animation is choppy or stuttering

**Solution:**

- Ensure all frames are preloaded before enabling scroll
- Reduce image file size (compress to 80-85% quality)
- Check frame rate extraction (30fps recommended)
- Verify no memory issues (too many large files)
- Use WebP format for better performance
- Test with fewer frames initially

---

### Problem: Scroll feels too fast or too slow

**Solution:**

- Adjust container height to change scroll distance
- Modify scroll offset in `useScroll`:
  ```typescript
  offset: ["start start", "end end"]; // Default
  offset: ["start start", "end+=100% end"]; // Longer scroll
  offset: ["start start", "end-=50% end"]; // Shorter scroll
  ```
- Change frame count (fewer frames = faster)

---

### Problem: Background doesn't match, visible edges around product

**Solution:**

- Use eyedropper to get exact hex from frame background
- Set body/page background to exact same color
- Ensure gradient in images matches page gradient
- Check color profile consistency
- Regenerate images with darker/cleaner background
- Add subtle shadow under product if needed

---

### Problem: Text overlays not appearing or positioned wrong

**Solution:**

- Check z-index stacking (text should be above canvas)
- Verify scroll progress ranges for opacity transforms
- Test on different screen sizes (responsive positioning)
- Adjust absolute positioning values
- Use Framer Motion's `useTransform` for smooth fades

---

### Problem: High memory usage or browser crash

**Solution:**

- Reduce frame count (use every 2nd frame: 120 instead of 240)
- Compress images more aggressively
- Implement progressive loading (load frames as needed)
- Use smaller image dimensions
- Consider server-side optimization
- Test on target devices (mobile has less memory)

---

### Problem: Cursor AI generates incorrect code structure

**Solution:**

- Provide more specific file structure in prompt
- Specify exact Next.js version and App Router
- Include example of desired component structure
- Ask Cursor to fix specific issues: "Adjust frame path to use..."
- Manually edit generated code for your setup

---

## Best Practices Summary

### Image Generation

1. **Use consistent lighting** across start and end frames
2. **Keep backgrounds pure black** with subtle gradient for seamless blending
3. **Center product** in both frames for balanced animation
4. **Allow space** for exploded components to separate
5. **Match camera angle** exactly between frames
6. **No text or logos** — keep images clean for flexibility

### Video Animation

1. **Upload highest quality frames** to Veo for best results
2. **Check animation smoothness** before proceeding
3. **Regenerate if needed** — AI output varies
4. **Aim for 3-8 second videos** for reasonable frame counts

### Frame Extraction

1. **Use 30fps** for balance of smoothness and performance
2. **Compress frames** to 80-85% quality (minimal visual loss)
3. **Convert to WebP** for better file size
4. **Name sequentially** (001, 002, 003...) for easy loading
5. **Test frame count** — more isn't always better

### Code Development

1. **Preload all frames** before enabling scroll
2. **Use Canvas** for performance with many frames
3. **Show loading state** while frames load
4. **Test on mobile** — different performance characteristics
5. **Optimize scroll calculations** — throttle if needed
6. **Match background color exactly** using eyedropper
7. **Add responsive sizing** for different devices

### Performance

1. **Compress images** aggressively (aim for <100KB per frame)
2. **Use WebP format** (25-35% smaller than JPG)
3. **Consider lazy loading** for very long sequences
4. **Test on actual devices** — don't rely on desktop only
5. **Monitor memory usage** — adjust frame count if needed
6. **Use CDN** for faster global delivery

---

## Resource Checklist

### Before Starting

- [ ] Google Whisk access for image generation
- [ ] Google Veo access for animation
- [ ] EZGif account (free, no signup required)
- [ ] Cursor AI installed
- [ ] Next.js project initialized
- [ ] Product concept decided

### Image Generation Phase

- [ ] Start frame generated (intact product)
- [ ] End frame generated (exploded view)
- [ ] Both frames have matching backgrounds
- [ ] Lighting consistent between frames
- [ ] Product centered in both frames
- [ ] High resolution (2K-4K)

### Animation Phase

- [ ] Both frames uploaded to Veo
- [ ] Frames-to-Video mode selected
- [ ] Animation generated
- [ ] Smooth transition verified
- [ ] Video downloaded

### Frame Extraction Phase

- [ ] Video uploaded to EZGif
- [ ] Frame rate set to 30fps
- [ ] Frames extracted
- [ ] ZIP file downloaded
- [ ] Frames unzipped and renamed if needed

### Project Setup Phase

- [ ] Frames uploaded to `public/frames/`
- [ ] Sequential naming verified
- [ ] File sizes optimized
- [ ] Background color extracted with eyedropper

### Code Development Phase

- [ ] Cursor AI prompt pasted
- [ ] Component generated
- [ ] Frame path adjusted in code
- [ ] Background color matched
- [ ] Loading state added
- [ ] Responsive sizing implemented
- [ ] Text overlays customized

### Testing & Launch

- [ ] All frames loading correctly
- [ ] Smooth scroll interaction
- [ ] No visible edges around product
- [ ] 60fps performance verified
- [ ] Mobile responsive
- [ ] Cross-browser tested
- [ ] Loading state works
- [ ] Memory usage acceptable

---

## Advanced Customization

### Non-Product Animations

**Story-based scrolling:**

- Scene transformations (day to night, seasons changing)
- Character journey through environment
- Abstract transitions (shapes morphing, colors shifting)
- Timeline visualizations (historical events unfolding)

**Example prompt for Whisk:**

```
Cinematic landscape photography of a mountain valley, early morning golden hour, mist in valleys, warm sunrise light, photorealistic, 8K quality, no text, dramatic sky, deep atmospheric perspective.
```

**End frame:** "same valley at sunset, dramatic orange and purple sky, long shadows, golden hour, mist cleared"

---

### Alternative Tech Stacks

**Without Next.js:**

```typescript
// Vanilla JS + HTML5 Canvas
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

window.addEventListener("scroll", () => {
  const scrollPercent =
    window.scrollY / (document.body.scrollHeight - window.innerHeight);
  const frameIndex = Math.floor(scrollPercent * frameCount);
  drawFrame(frameIndex);
});
```

**With React (not Next.js):**

- Same approach, use Create React App
- Store frames in `public/` folder
- Use `react-scroll` or native scroll events

**With Vue:**

- Use Vue's composition API
- `onMounted` for frame loading
- `watch` scroll position
- Canvas rendering identical

---

### Horizontal Scrolling

**Concept:** Scroll horizontally through frames instead of vertically

**Implementation:**

```typescript
const { scrollXProgress } = useScroll({
  target: containerRef,
  axis: 'x' // Horizontal axis
})

// Container needs overflow-x: scroll and large width
<div className="overflow-x-scroll w-[500vw]">
  <canvas ref={canvasRef} />
</div>
```

---

## Final Tips

**The secret to $5,000 scroll animations in 10 minutes:**

1. **Let AI handle the 90%** — Image generation, animation, code
2. **Focus on the 10%** — Vision, concept, product choice, polish
3. **Background matching is critical** — Use eyedropper for exact color
4. **Preload everything** — No frame should load during scroll
5. **Test on real devices** — Desktop performance doesn't predict mobile
6. **Compress aggressively** — File size impacts everything
7. **Start simple** — Single product, 240 frames, 8-second animation
8. **Iterate quickly** — Regenerate images if animation isn't smooth
9. **Match the aesthetic** — Pure black background, luxury tech vibe
10. **Ship it** — Good scroll animation shipped beats perfect one in progress

**Pro Tip:** The most impressive scroll animations don't just show transformation — they tell a story. An exploded view isn't just pretty; it shows engineering, build quality, and attention to detail. Choose products where the internal components are as beautiful as the exterior. The scroll interaction becomes a journey of discovery.

---

**Difficulty:** Beginner  
**Duration:** 10 minutes  
**Pattern:** 90% AI, 10% Human  
**Output:** Awwwards-level scroll animation  
**Cost:** $5,000 agency effect for free

Welcome to the future of web animation. 🚀

---
