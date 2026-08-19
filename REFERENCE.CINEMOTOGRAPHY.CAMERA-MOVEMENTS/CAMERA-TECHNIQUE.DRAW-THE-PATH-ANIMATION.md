# Draw-the-Path AI Animation Technique

> **⚠️ LANGUAGE NOTE:** This document was originally written in Ukrainian. Some technical terms may retain Ukrainian/Russian terminology.

**Technique:** Animating still images with camera movement paths  
**Applications:** Orbit shots, spiral climbs, FPV flyovers, following moving subjects

## Overview

Draw-the-Path is a camera animation technique where you draw a line on a static image to define the camera's movement trajectory. Video generators (Seedance, etc.) read the drawn line as a 3D camera path through the scene.

**Key Principle:** The line is NOT visible in the final video — it's purely a directional guide for the AI.

---

## How It Works

### Two Types of Motion

1. **Frozen Scene:** The subject/scene is completely still, ONLY the camera moves (orbit, spiral, flyover)
   - Examples: Painting orbit, statue spiral, city flyover

2. **Moving Subject:** A living subject (person, animal) moves through the scene while the camera follows
   - Example: Cat walking through a room while people react

### General Workflow

**STEP 1:** Prepare your image  
Get a high-quality painting/photo, or generate a scene designed for the motion

**STEP 2:** Draw the camera path  
Use any image editor (Preview, Canva, Paint, phone markup) to draw ONE continuous line

- Place a thick dot at the start
- Add direction arrows along the path
- End with a final arrow

**STEP 3:** Insert prompt and generate  
Upload the marked image (for moving subjects: also upload the clean version separately) to your generator, paste the prompt from this guide, and run

---

## Golden Rules for Drawing Paths

### Line Quality

- **One continuous unbroken line** — no branches, no intersections
- **Never cross the line with itself** — causes glitches
- **Never reverse direction** — draws are read forward only
- **Wide smooth curves** generate cleanly; sharp corners cause distortion

### Line Color

Choose a **bright color NOT in your image**:

- ✅ Neon green, cyan, magenta (if no reds in scene)
- ❌ Colors that blend with the subject

### Path Design

- Start with a **thick dot** to mark beginning
- Add **directional arrows** along the path
- Keep line smooth and flowing
- For complex moves, break into 3-4 shorter clips and edit together

---

## Case Studies

### 1. ORBIT SHOT - "Kateryna" Painting

**Goal:** Camera orbits a stationary figure in a 270° arc

**Setup:**

- Source: High-quality reproduction of painting
- Line: Wide arc from lower right → around figure → to left front
- Duration: 8 seconds minimum (270° orbit needs time)

**Critical Challenge:** When orbiting beyond 180°, camera goes BEHIND the figure  
**Solution:** Prompt includes "CROSSING BEHIND HER" block to build the back view once and hold it stable

**Technical Notes:**

- Use neon green or cyan line (NOT magenta — conflicts with red skirt/ribbons)
- If back view morphs: reduce arc to 150-180° OR increase duration to 10s
- Full prompt included in tutorial (page 3-5 of original PDF)

---

### 2. RISING SPIRAL - "Motherland Mother" Statue

**Goal:** Camera spirals upward around tall statue from base to face

**Setup:**

- Source: Full-height statue photo with sky/city background
- Line: Helical path coiling upward: base → waist → chest → shoulders → face
- Duration: 8-10 seconds (full vertical spiral needs 10s minimum)

**Critical Challenge:** Model tends to split into "first orbit, then climb"  
**Solution:** Prompt enforces "It BOTH climbs and orbits at the same time" + "never descends, never stalls"

**Technical Notes:**

- Line color: gold, white, or neon (contrast with metal statue)
- This is an ambitious move — may require 2-3 generations
- Full prompt included in tutorial (page 6-7 of original PDF)

---

### 3. FPV FLYOVER - Lviv Panorama

**Goal:** Fast FPV drone flight weaving through old city rooftops

**Setup:**

- Source: Aerial photo or generated panorama of city from above
- Line: Winding path through architecture: low rooftops → around town hall tower → over roofs → toward horizon
- Duration: 8-10 seconds for long routes

**Critical Challenge:** Long/dynamic routes can cause mid-shot "teleport" cuts  
**Solution:**

1. Simplify line (fewer nodes, wider curves)
2. Increase duration
3. Prompt includes "ONE SINGLE UNBROKEN TAKE" block against cuts

**Technical Notes:**

- Line color: red or neon (contrast with warm rooftops)
- Smooth wide banks, not sharp angles
- Full prompt included in tutorial (page 8-9 of original PDF)

---

### 4. FOLLOW MOVING SUBJECT - Ukrainian Classics + Cat

**Goal:** MOST COMPLEX — Ginger cat walks through salon past 5 historical figures who react; camera follows cat

**Setup:**

- **TWO images required:**
  - `image_1` = Clean starting frame (no markup)
  - `image_2` = Same frame WITH path drawn on cat's route
- Line: Cat's path through room: start on cat → past Shevchenko → onto Franko's desk → past Hrushevsky → to Lesya → finish at Krushelnytska by piano
- Path drawn LOW (floor level, furniture legs, skirt edges) — NOT through faces

**Secret:** Draw-the-Path only provides SEQUENCE  
For cat to jump/climb, you must WRITE the actions at each node:

- "JUMPS UP onto his lap"
- "WALKS ALONG THE DESK"
- "leaps down"

For people to react: write "ALIVE AND REACT"

**Risk with Real Faces:** Historical figures are real people; faces can distort more during motion  
**Mitigation:** Prompt has triple face protection; if faces still drift, break into 3-4 short clips per interaction and edit

**Technical Notes:**

- Line color: yellow/green (not through faces)
- Requires TWO prompts:
  1. Frame generation prompt (creates the setup)
  2. Video generation prompt (animates with both images)
- Full prompts included in tutorial (page 10-12 of original PDF)

---

## Troubleshooting Guide

### ❌ **Drawn line remains visible in video**

- **Fix:** Redraw with color NOT in scene (neon green/cyan). Move "remove the line" instruction to TOP of prompt and duplicate in NEGATIVE section. Make line thinner.

### ❌ **Camera just moves up-down, doesn't orbit**

- **Fix:** Your line is an arch ABOVE the scene — model reads only vertical. Redraw as arc FROM THE SIDE around object. Add to prompt: "PRIMARY motion is horizontal orbit, NOT vertical"

### ❌ **Mid-shot cut/teleport**

- **Fix:** Route too long for duration. Simplify line (fewer nodes, wider curves) OR increase duration. Block "ONE SINGLE UNBROKEN TAKE" already in prompt

### ❌ **Face/back morphs during orbit**

- **Fix:** Camera went behind figure with no back view on source. Reduce arc angle to 150-180° OR increase duration to 10s. Block "build the back once and keep it stable" in prompt

### ❌ **Spiral "sags" or separates into orbit-then-climb**

- **Fix:** Model splitting helix into two moves. Keep line "BOTH climbs and orbits at the same time" + "never descends, never stalls"

### ❌ **Cat just walks, doesn't jump**

- **Fix:** WRITE the actions at each node (JUMPS UP, WALKS ALONG). Line alone doesn't specify actions — only sequence

### ❌ **People frozen, don't react**

- **Fix:** Add "THE PEOPLE ARE ALIVE AND REACT" + describe each reaction (turns head, reaches hand toward cat)

### ❌ **Object "floats" in air (car/character)**

- **Fix:** Emphasize 3x that it "keeps moving, never hovers" + add to NEGATIVE "no frozen, no floating"

### ❌ **Style shifts to cartoon/3D**

- **Fix:** At TOP of prompt: "photorealistic, NOT animated, NOT cartoon, NOT 3D". Add "35mm film, realistic photography"

### ❌ **Too dark/depressing result**

- **Fix:** In generation prompt: "BRIGHT SUNNY DAYTIME, high-key, cheerful" + direct negation "NOT dark, NOT moody, NOT gloomy"

---

## General Principle

**Scene is frozen OR has one moving subject · Camera follows the drawn line · Motion is described with words**

---

## Full Example Prompts

Due to length, the complete ready-to-copy prompts for each case study are included in the original Ukrainian tutorial document (pages 3-12). Each includes:

- Complete scene description
- Camera movement specification
- Parallax and depth instructions
- Stability and consistency rules
- Negative prompts
- Technical settings

---

**Source:** Draw-the-Path Ukrainian Tutorial - AI Animation of Paintings & Photos  
**Original Language:** Ukrainian  
**Date:** 2026  
**Compatible Platforms:** Seedance 2.0, Higgsfield, similar path-based video generators
