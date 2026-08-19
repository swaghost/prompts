# 3D Logo Reveal Workflow — Empty Fascia to Premium Signage

**Platform:** Nano Banana / ChatGPT (removal) → Higgsfield Seedance 2.5 (reveal)  
**Duration:** 8 seconds  
**Technique:** Two-frame reveal (empty start → full end)  
**Use Case:** Real estate & brand reveal, premium 3D logo assembly

---

## Overview

**The Concept:** Turn a single photo of a finished sign into an 8-second cinematic reveal, where the logo's 3D elements assemble themselves onto an empty panel. No morphing, camera locked.

**The Idea:** Treat the original image as the **end point**, generate an empty version of it (Reference 1), and let the video model build the transition between the two, placing one element at a time without ever blending them.

**Workflow:**

1. Use Nano Banana or ChatGPT to remove 3D signage (create empty state)
2. Upload both frames to Seedance 2.5 (empty first, full second)
3. Use reveal prompt to animate 3D elements appearing one by one

---

## Step-by-Step Workflow

### Step 1: Open Higgsfield

Open [Higgsfield AI — AI-native creative suite](https://higgsfield.ai). This is the platform you'll use to build the reveal video.

---

### Step 2: Build Reference 1 — Remove the 3D Signage

**Tools:** Nano Banana or ChatGPT (image edit)

**Action:** Upload your original property/sign photo, paste the Removal Prompt below and generate. Remove every mounted 3D element — letters, arrows, arc, signs — leaving only the clean empty panel or plot.

**Verify:** Open the result. If any trace of signage remains or the angle shifted, regenerate until the panel is clean.

---

## Removal Prompt — Nano Banana / ChatGPT

```
Remove all 3D signage from this image: the white "Stepz" letters, the "FITNESS" text, the "24/7" numbers, all white arrows, and the grey clock arc. Show a completely empty clean orange fascia panel with nothing mounted on it.

Keep everything else exactly as it is: identical camera angle, identical low-angle upward perspective, identical field of view, identical crop, identical framing. Keep the deep blue sky, the orange fascia colour and texture, the underside soffit with ceiling downlights, and the same bright daylight completely unchanged. Fill the cleared area with clean matching orange fascia surface in the same colour and finish already visible. Same lighting, same shadow direction, same time of day.
```

**What This Does:**

- Removes all 3D mounted elements
- Preserves background exactly
- Keeps camera angle identical
- Maintains lighting and perspective
- Fills removed area with matching surface

**Result:** Reference 1 (the empty state)

---

### Step 3: Go to Higgsfield & Select Seedance 2.5

Open Higgsfield, switch to image-to-video mode, and choose the **Seedance 2.5** model. Set the duration to **8s**.

---

### Step 4: Upload Both Images (in the Correct Order)

A reveal needs two frames — a start and an end:

**Reference 1 (First / Start frame):** The empty panel — your output from Step 2  
**Reference 2 (End frame):** The original full sign photo

**Order matters:** Empty first, full second. Reverse it and the reveal runs backwards (the sign will disappear instead of build).

---

### Step 5: Add the Reveal Prompt & Generate

Paste the **Reveal Prompt** below and hit generate. That's it — an 8-second premium 3D logo reveal is ready.

---

## Reveal Prompt — Higgsfield / Seedance 2.5

```
Static 3D signage reveal, 8 seconds. Locked-off low-angle upward camera. Only a subtle continuous drift of a few degrees that eases to a stop at 6s; composition stays the same recognisable shot from start to finish. No dolly, no zoom, no whip pan.

CAMERA LOCK: The camera position, height, angle, focal length, field of view, and perspective are exactly those of the reference images and stay fixed for the entire 8 seconds. The orange fascia edges, the blue sky line, and the soffit below all stay in the same directions. Do not reframe, re-angle, or reveal any area not visible in the references.

TWO STATES, NOT A BLEND: The first image is the empty orange fascia at 0s. The second image is the fully mounted 3D sign at 6s. Do not interpolate, cross-fade, or morph one into the other. The first image stays exactly as it is; the 3D sign elements from the second image are placed onto it one group at a time until the sign is complete. At every moment the frame shows the empty fascia plus whichever elements have already arrived, never a partial blend.

STRICT INVENTORY - NOTHING NEW: Every element - the grey clock arc, the four white arrows, the "24/7" numbers, the white 3D "Stepz" lettering, and the "FITNESS" text - must already be visible in the second reference image, in the same position, scale, orientation, depth, material, and colour. Do not add, invent, duplicate, restyle, or recolour anything. If an element is absent from the second image, it must never appear.

ABSOLUTE LOCK: Orange fascia, blue sky, soffit, downlights, and daylight direction are identical in both references and stay identical for the full 8 seconds, never redrawn or warped.

REVEAL METHOD - MIXED MOTION: Elements arrive in groups with different motion by type. Every element is fully opaque, complete, and correctly proportioned from the first frame it appears - it either does not exist yet or exists fully, no in-between.

POP-IN - white 3D "Stepz" letters and "FITNESS" text: appear directly at final mounted position, slightly undersized for two frames, overshoot very slightly, settle to exact size. ~0.2s. Extruded 3D depth and drop shadow snap in with each letter.

DROP - the grey clock arc and the "24/7" numbers: fall from just above final position and land with a firm settle onto the fascia.

DESCEND - the four white arrows: lower into their final angled positions along the arc, one after another.

INSTANT - small details and cast shadows: appear in a single frame.

Each arrival ~0.2-0.3s, short travel only, no long flight paths. Contact shadows on the orange fascia appear the moment an element lands.

TIMELINE:
0-2s: Frame is exactly the first reference (empty orange fascia). Camera begins slow drift.
2-3.5s: "Stepz" and "FITNESS" 3D letters POP-IN onto the fascia with extruded depth and shadow.
3.5-5s: Grey clock arc and "24/7" numbers DROP in; the four white arrows DESCEND into position along the arc.
5-6s: Final small details and all contact shadows land INSTANT; camera drift eases to a stop. Frame now equals the second reference exactly.
6-8s: Frame is exactly the second reference, completely static - no new elements, no repositioning. Stable daylight.

Photorealistic 3D exterior signage, bright natural daylight, glossy white channel-letter finish, no people.

Negative: changing camera angle, new viewpoint, reframing, rotating camera, orbiting, crane move, changing focal length, lens distortion, perspective warp, tilting horizon, revealing unseen areas, added elements, invented signage, restyled letters, changed colours, changed materials, interpolation between references, blending two images, morph, cross-fade, gradual transformation, slow growth, gradual scaling, growing from zero, unfolding, dissolving in, fade in, fade out, ghosting, double exposure, translucent objects, glowing particles, warping, melting, stretching, flying across frame, floating elements, people, watermark, redrawn fascia, altered lighting, dolly, zoom, whip pan.
```

---

## 4 Golden Rules — Avoid Failure

### 1. Identical Framing

Both images must share the exact resolution, angle, crop and framing. Otherwise the model warps or stretches the architecture.

### 2. Clean, Well-Lit Photos

Use high-res images with crisp lighting. Blurry or dim photos produce messy boundaries.

### 3. Preserve the Background

In Step 2 remove only the sign — keep the ground, sky, panel colour and curbs fully intact.

### 4. Verify Step 2

Before moving on, inspect the empty image — if the perspective or boundaries changed, regenerate.

---

## Detailed Timeline Breakdown

### 0-2 seconds: Empty State

**Frame Content:**

- Exactly the first reference (empty orange fascia)
- No elements visible yet

**Camera:**

- Begins slow drift (subtle, few degrees)
- Maintains recognizable composition

---

### 2-3.5 seconds: Main Lettering Arrives

**POP-IN Animation:**

- "Stepz" and "FITNESS" 3D letters
- Appear directly at final mounted position
- Slightly undersized for two frames
- Overshoot very slightly
- Settle to exact size
- Duration: ~0.2s per element

**Technical:**

- Extruded 3D depth snaps in
- Drop shadow snaps in with each letter
- Fully opaque from first frame

---

### 3.5-5 seconds: Secondary Elements

**DROP Animation:**

- Grey clock arc falls from just above final position
- "24/7" numbers fall and land
- Firm settle onto fascia

**DESCEND Animation:**

- Four white arrows lower into position
- Along the arc
- One after another
- Short travel distance

**Duration:**

- Each arrival ~0.2-0.3s
- No long flight paths

---

### 5-6 seconds: Final Details

**INSTANT Animation:**

- Small details appear in single frame
- All contact shadows appear
- Camera drift eases to stop

**Result:**

- Frame now equals second reference exactly
- All elements in place
- Static composition achieved

---

### 6-8 seconds: Hold

**Completely Static:**

- Frame is exactly the second reference
- No new elements
- No repositioning
- Stable daylight
- Hold for impact

---

## Element Animation Types Explained

### POP-IN (Letters)

**Best For:** 3D channel letters, main text elements  
**Motion:** Direct appearance at final position with slight scale bounce  
**Why:** Mimics professional motion graphics, feels premium

**Sequence:**

1. Element doesn't exist
2. Appears slightly undersized at exact position (2 frames)
3. Overshoots slightly larger
4. Settles to exact final size
5. 3D depth and shadow snap in simultaneously

---

### DROP (Shapes)

**Best For:** Arcs, circles, solid shapes, numbers  
**Motion:** Fall from just above final position  
**Why:** Gives weight and physicality

**Sequence:**

1. Element doesn't exist
2. Appears just above final position (few inches)
3. Falls with gravity
4. Lands with firm settle
5. Contact shadow appears on impact

---

### DESCEND (Arrows/Directional)

**Best For:** Arrows, pointers, small icons  
**Motion:** Lower smoothly into angled positions  
**Why:** Emphasizes direction and flow

**Sequence:**

1. Element doesn't exist
2. Appears above and lowers
3. Descends into exact angled position
4. One after another (sequential)
5. Short travel only

---

### INSTANT (Details)

**Best For:** Small details, shadows, textures  
**Motion:** Appear in single frame  
**Why:** Keeps focus on main elements

**Sequence:**

1. Element doesn't exist
2. Appears fully in one frame
3. No animation, just presence

---

## Key Principles

### 1. Two States, Not a Blend

**Critical Concept:** This is NOT a morph or cross-fade.

**Instead:**

- First image stays exactly as it is
- 3D elements from second image are placed onto it
- One group at a time
- Until sign is complete

**At Every Moment:**

- Frame shows empty fascia + elements that have arrived
- Never a partial blend
- Elements either don't exist or exist fully

---

### 2. Strict Inventory — Nothing New

**Every Element Must:**

- Already be visible in second reference image
- Same position
- Same scale
- Same orientation
- Same depth
- Same material
- Same colour

**Prohibited:**

- Do not add elements
- Do not invent elements
- Do not duplicate elements
- Do not restyle elements
- Do not recolour elements

**Rule:** If element is absent from second image, it must never appear

---

### 3. Absolute Lock

**These Never Change:**

- Orange fascia colour and texture
- Blue sky position and colour
- Soffit structure
- Downlight positions
- Daylight direction

**Duration:** Identical for full 8 seconds, never redrawn or warped

---

### 4. Camera Lock with Subtle Drift

**Camera Stays Fixed:**

- Position
- Height
- Angle
- Focal length
- Field of view
- Perspective

**But:**

- Subtle continuous drift of a few degrees
- Eases to stop at 6s
- Composition stays recognizable
- No dolly, no zoom, no whip pan

---

## Customization Guide

### Adapt for Different Signage Types

**Channel Letters:**

- Use POP-IN animation
- Glossy white finish
- 3D extrusion visible
- Drop shadows

**Flat Graphics:**

- Use INSTANT or POP-IN
- No 3D depth
- Sharp edges
- Vinyl or painted appearance

**Backlit Signs:**

- Use POP-IN with glow
- Light-up sequence
- Illumination snaps on
- Halo effects

**Monument Signs:**

- Use DROP for heavy elements
- Stone or concrete base
- Metal letters
- Ground shadows

---

### Timing Adjustments

**Faster Reveal (6 seconds):**

```
TIMELINE:
0-1s: Empty state
1-2.5s: Main letters POP-IN
2.5-4s: Secondary elements DROP/DESCEND
4-5s: Details INSTANT, camera stops
5-6s: Hold
```

**Slower Reveal (10 seconds):**

```
TIMELINE:
0-3s: Empty state with slow drift
3-5s: Main letters POP-IN
5-7s: Secondary elements DROP/DESCEND
7-8s: Details INSTANT, camera stops
8-10s: Hold
```

---

### Different Sign Types

**Neon Sign:**

```
...GLOW-ON - letters: appear dark, then neon tubes light up sequentially from one end to the other, bright glow blooming outward, buzz sound implied...
```

**Painted Mural:**

```
...PAINT-IN - artwork: appears in painted strokes from left to right, brush texture visible, slight paint drips, as if artist just finished...
```

**Metal Letters:**

```
...MAGNETIZE - letters: appear to snap onto metal panel from scattered positions nearby, slight metallic clang, settling into grid alignment...
```

---

## Troubleshooting

### Problem: Elements Morph or Blend

**Cause:** Model interpreting as image interpolation  
**Solution:**

- Emphasize in prompt: "Do not interpolate, cross-fade, or morph"
- Add: "Elements either do not exist yet or exist fully, no in-between"
- Specify animation types explicitly (POP-IN, DROP, etc.)

---

### Problem: Background Changes

**Cause:** Model redrawing background during reveal  
**Solution:**

- Emphasize: "ABSOLUTE LOCK: [background elements] stay identical for full 8 seconds"
- Verify both reference images have identical backgrounds
- Add to negative prompt: "redrawn fascia, altered lighting, warped background"

---

### Problem: Camera Moves Too Much

**Cause:** "Drift" interpreted as dolly or orbit  
**Solution:**

- Specify: "Only a subtle continuous drift of a few degrees"
- Add: "composition stays the same recognisable shot"
- Negative prompt: "dolly, zoom, whip pan, orbiting, crane move"

---

### Problem: Elements Appear Wrong

**Cause:** Model inventing elements not in reference  
**Solution:**

- Use "STRICT INVENTORY" section
- Add: "Every element must already be visible in the second reference image"
- Negative prompt: "added elements, invented signage, duplicated elements"

---

### Problem: Framing Doesn't Match

**Cause:** Reference 1 (empty) has different framing than original  
**Solution:**

- Regenerate Reference 1 with stronger framing instructions
- Verify both references side-by-side before generating video
- Use identical resolution for both references

---

## Use Cases

### Real Estate Signage

**Perfect For:**

- Property development reveals
- Grand opening announcements
- New location unveilings
- Construction completion showcases

**Why It Works:**

- Shows professional finished signage
- Premium feel with 3D elements
- Before/after storytelling

---

### Brand Identity Reveals

**Perfect For:**

- New brand launches
- Rebranding announcements
- Corporate identity showcases
- Franchise locations

**Why It Works:**

- Logo assembly feels intentional
- Premium production value
- Emphasizes craftsmanship

---

### Commercial Real Estate

**Perfect For:**

- Shopping center tenant reveals
- Office building directory signs
- Retail storefront launches
- Restaurant opening announcements

**Why It Works:**

- Professional polish
- Highlights quality materials
- Cinematic presentation

---

### Social Media Content

**Perfect For:**

- "Coming soon" announcements
- Business milestone celebrations
- Location expansion reveals
- Behind-the-scenes style content

**Why It Works:**

- 8 seconds perfect for social
- High engagement potential
- Shareable and repostable

---

## Pro Tips

### Photography Tips

**For Best Results:**

- Shoot in bright daylight (10am-2pm)
- Use wide angle to capture full sign
- Ensure sign is sharp and in focus
- Avoid overcast days (flat lighting)
- Level horizon and verticals
- High resolution (at least 1080p)

**Ideal Angles:**

- Low-angle upward perspective (dramatic)
- Straight-on eye level (clean)
- Slight side angle (shows 3D depth)

---

### Removal Quality

**Verify Your Empty Plate:**

- Zoom in to check edges
- Verify no ghost outlines remain
- Check lighting matches
- Confirm perspective unchanged
- Look for color continuity

**If Not Perfect:**

- Try different removal prompt wording
- Generate 3-4 options, pick best
- May need manual touch-up in Photoshop

---

### Element Sequencing

**Strategic Order:**

- Largest/main elements first (brand name)
- Secondary text next (tagline, hours)
- Decorative elements last (arrows, shapes)
- Shadows always with their elements

**Why This Order:**

- Builds hierarchy naturally
- Most important info appears first
- Creates professional flow
- Mimics actual installation process

---

### Camera Drift Direction

**Subtle Upward Drift:**

- Emphasizes grandness
- "Looking up" at signage
- Premium/aspirational feel

**Subtle Sideways Drift:**

- Shows dimension
- Reveals 3D depth
- More dynamic

**Minimal Drift:**

- Most stable
- Professional/corporate feel
- Safe choice

---

## Platform Information

**Workflow:**

- Nano Banana / ChatGPT (removal)
- Higgsfield Seedance 2.5 (reveal)

**Duration:** 8-second premium 3D logo reveal

**Current Promotion:**

- Get 33 DAYS of UNLIMITED Seedance 2.5 on Higgsfield
- Available for a LIMITED TIME

**Website:** [Higgsfield.ai](https://higgsfield.ai)

---

## Final Checklist

Before generating, verify:

- [ ] Original photo is high-res and well-lit
- [ ] Original photo has clear 3D signage visible
- [ ] Removal prompt generated clean empty state
- [ ] Empty state has identical framing to original
- [ ] Empty state has no ghost outlines or artifacts
- [ ] Both references uploaded in correct order (empty first, full second)
- [ ] Duration set to 8 seconds
- [ ] Reveal prompt includes CAMERA LOCK section
- [ ] Reveal prompt includes TWO STATES, NOT A BLEND section
- [ ] Reveal prompt includes animation type descriptions
- [ ] Reveal prompt includes detailed TIMELINE
- [ ] Reveal prompt includes comprehensive negative prompts
- [ ] Element inventory matches original photo exactly

---

## Conclusion

The 3D Logo Reveal workflow transforms a simple finished sign photo into a cinematic 8-second reveal sequence. By treating the original as the end point and generating a clean empty state, you create a reveal that feels intentional, premium, and professional.

The key is in the details: precise framing match between references, specific animation types for different elements, locked camera with subtle drift, and explicit instructions that elements appear fully rather than morphing in.

When executed correctly, the result looks like high-end motion graphics, perfect for real estate reveals, brand launches, and commercial announcements — all from a single photograph.

**Workflow:** Nano Banana / ChatGPT (remove) → Higgsfield · Seedance 2.5 (reveal)  
**Result:** 8-second premium 3D logo reveal
