# 📦 CGI PRODUCT — COMMERCIAL ADS WORKFLOW GUIDE

**A Complete Step-by-Step Guide for Creating CGI Ads, Adapting Visuals, and Engineering Multimodal AI Prompts**

---

## 1. Overview & Core Concept

This master guide provides a complete, step-by-step workflow for transforming static product photos or advertisement concepts into high-impact 3D CGI commercial ads using AI models.

### Why This Workflow Works (The 2-Stage Method)

High-end AI video models often fail when asked to generate complex scenes from scratch. To ensure high stability, spatial consistency, and exact product preservation, we separate the process into two distinct stages:

- **Stage 1 (Still Image Generation)**: Spend 80% of your effort generating a photorealistic, razor-sharp still image.
- **Stage 2 (Video Motion Control)**: Use an image-to-video model driven by a timeline script to animate motion without altering the base product or scene geometry.

---

## 2. Step-by-Step Execution Workflow

### Step 1: Asset Preparation

Before writing any prompts, collect two base visual reference assets:

- **Asset 1 (Product Reference)**: A clean, sharp photo of your hero product, packaging, bottle, or logo.
- **Asset 2 (Environment Reference)**: A clear background photo where your ad will be staged (e.g., a roadside billboard, a city building wall, or an urban plaza).

### Step 2: Anatomy of a CGI Prompt

A professional AI prompt consists of structured blocks rather than random descriptions:

- **Hero Subject Description**: Exact product geometry, materials, labels, colors, and branding details.
- **Spatial & Depth Illusion**: Forced-perspective cues, studio background gradients inside the display, and rim lighting.
- **Camera Behaviors & Constraints**: Explicit locked-camera statements (locked camera, no zoom, no pan).
- **Timeline Controls**: Micro-breakdowns (0:00-0:02, 0:02-0:05) that direct motion chronologically.
- **Negative Prompts**: Essential exclusion tags that prevent texture warping, text distortion, or unwanted camera drift.

### Step 3: Prompt Generation & Execution

Populate your visual details directly into the Master Templates below using your preferred text-to-image generator (e.g., ChatGPT, Midjourney) for Stage 1, followed by an image-to-video generator (e.g., Luma, Runway, Google Flow) for Stage 2.

---

## 3. Master Prompt Blueprints

### 📄 PROMPT MASTER 1: 3D Billboard Breakout (Stage 1 - Text-To-Image)

**Use this prompt in an image generator to render a photorealistic 3D product breaking out of a 2D display.**

```
A hyper-realistic CGI commercial scene where [YOUR PRODUCT DESCRIPTION] breaks out from a flat 2D billboard display into 3D space.

HERO PRODUCT DETAILS:
[Describe exact product geometry, materials, textures, labels, brand colors, and any text/logos that must remain sharp and readable]

DISPLAY MECHANICS:
- The billboard frame contains a forced-perspective gradient background that creates depth illusion
- The [product] protrudes 30-40% out of the frame boundary, casting realistic shadows onto the billboard surface
- Sharp rim lighting highlights the edges where the product crosses the frame plane

SPATIAL SETTING:
[Describe the environment: urban plaza, highway roadside, building facade, etc.]
- Billboard is mounted on [wall/pole structure]
- Atmospheric context: [time of day, weather, lighting conditions]

CAMERA & LIGHTING:
- Camera angle: [slight low angle / eye level / high angle]
- Primary light source: [direction and quality]
- Secondary fill lights to ensure product readability
- Depth of field: Sharp focus on product, slight blur on distant background

LOCKED CAMERA CONSTRAINT:
Camera remains completely locked. No zoom, no pan, no rotation. Static frame only.

NEGATIVE PROMPTS:
distorted text, warped labels, blurry product, morphed geometry, smeared brand names, camera movement, zooming, panning, multiple products, duplicated items
```

---

### 📄 PROMPT MASTER 2: Timeline-Driven Video Motion (Stage 2 - Image-To-Video)

**Use this prompt in a video generator along with your Stage 1 still image to control motion using a precise timeline.**

```
Transform this still CGI billboard scene into an 8-second video animation with precise timeline control.

CORE ANIMATION DIRECTIVE:
The [product] performs [specific motion: rotation, float, pulse, etc.] while maintaining perfect spatial relationship with the billboard frame.

TIMELINE BREAKDOWN:
0:00-0:02 — [Initial state/setup motion]
0:02-0:05 — [Primary product motion/action]
0:05-0:08 — [Secondary motion/settle]

SPATIAL CONSTRAINTS:
- The product remains anchored to its breakout position from the billboard
- The billboard frame stays completely static
- Environment (buildings, sky, ground) remains locked in position
- No morphing or warping of product geometry

CAMERA & MOTION LOCK:
- Camera remains completely locked throughout entire sequence
- No camera zoom, pan, tilt, or rotation
- No environmental camera drift
- Locked horizon line

ATMOSPHERE & EFFECTS:
[Any atmospheric elements: light rays, subtle dust particles, soft shadows, etc.]
Keep all effects subtle and secondary to product motion.

NEGATIVE PROMPTS:
camera movement, zooming, panning, camera drift, morphing product, warped text, distorted labels, multiple products appearing, frame breaking, glitching, environmental changes, shifting perspective, wobbly motion
```

---

### 📄 PROMPT MASTER 3: Universal VFX Logo Reveal (Omni Flash / Google Flow)

**Use this prompt to animate static signs, leather patches, or store logos from an empty surface into a full reveal.**

```
A clean VFX logo reveal animation showing [brand name/logo] materializing onto [surface type: leather patch, metal sign, fabric banner, store facade].

REFERENCE SETUP:
- Reference Image 1: Empty [surface] with clean texture, no logo present
- Reference Image 2: Final state with [logo/brand] fully visible and integrated

ANIMATION SEQUENCE:
The logo appears through [method: gradual fade-in, light painting, material etching, embossing effect, etc.]

TIMELINE (8 seconds):
0:00-0:02 — Empty surface, establish texture and lighting
0:02-0:05 — Logo gradually materializes/reveals from [start method]
0:05-0:08 — Final logo fully formed, settled, and stable

VISUAL QUALITIES:
- Logo maintains perfect legibility throughout reveal
- Surface texture and material properties remain consistent
- Lighting stays natural and locked to environment
- No morphing, warping, or distortion of logo geometry

CAMERA CONSTRAINTS:
Camera completely locked. No movement, no zoom, no pan. Static frame throughout entire sequence.

NEGATIVE PROMPTS:
camera movement, logo distortion, warped text, morphing letters, changing surface texture, environmental drift, multiple logos, duplicated elements, glitching, flickering text
```

---

## 4. Best Practices & Pro Tips

- **80/20 Rule**: Never try to fix bad product details during the video stage. Ensure the Stage 1 still image is 100% accurate before animating.

- **Strict Camera Anchors**: AI models tend to drift spatially. Always include explicit anchor commands like "camera remains completely locked" and "lock environment."

- **Preserve Negative Prompts**: Negative prompts act as safety bounds. Omitting them increases the risk of text corruption, morphing, and motion artifacts.

- **Test Stage 1 Multiple Times**: Generate 3-5 variations of your still image and pick the best one before moving to animation.

- **Timeline Precision**: Break your motion into 2-3 second chunks rather than describing "smooth motion throughout." This gives the AI clear checkpoints.

- **Product Readability First**: All text, logos, and brand elements must be crystal clear in Stage 1. If they're blurry in the still image, they'll be worse in video.

---

## 5. Recommended Tools

### Stage 1 (Still Image Generation):

- ChatGPT (DALL-E 3)
- Midjourney
- Stable Diffusion
- Leonardo AI

### Stage 2 (Image-to-Video):

- Luma AI
- Runway Gen-3
- Google Flow
- Pika Labs

### Logo/VFX Animation:

- Omni Flash (via pollo.ai)
- Google Flow
- Runway Gen-3

---

**Source**: [Notion Guide](https://efficient-mink-952.notion.site/CGI-Product-3b39502993ae801e8602ee7ef9b4f6b8)
