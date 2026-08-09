# Drawing to Life Effect Guide

## Overview

**Effect Name**: Bring Any Drawing to Life  
**Tagline**: Touch a drawing on the page and watch it become real. One photo, two prompts, four seconds.  
**Platforms**: Nano Banana Pro (image generation) + Kling 3.0 (video animation)  
**Creator**: Learn with Kayo  
**Made With**: Higgsfield

Create a magical effect where you touch a drawing on a page and it transforms into a real, three-dimensional object with lifelike motion.

---

## The Workflow

_Four steps, start to finish_

### Step 1: Film the Drawing

Find any drawing. A children's book, an illustrated page, a sketch of your own. Film a short clip of it and touch the drawing with your finger.

**Source Material**:

- Storybooks
- Comics
- Tattoo flash
- Sketch on a napkin
- Old illustration in a book

### Step 2: Take Two Screenshots

Open the clip in your gallery and grab two frames:

1. **Frame 1**: Just the drawing with no hand in shot
2. **Frame 2**: Your finger touching the drawing

**⚠️ CRITICAL**: Same angle, same light, same everything. They must come from the same clip.

### Step 3: Make the Drawing Real

On Higgsfield:

1. Go to **Create Image**
2. Choose **Nano Banana Pro**
3. Upload the screenshot **without your hand** (Frame 1)
4. Paste **Prompt 01** (see below)
5. Generate

**Result**: You now have your end frame (the "real" version).

### Step 4: Animate Between the Two

On Higgsfield:

1. Go to **Create Video**
2. Choose **Kling 3.0**
3. Set the photo **with your hand** as the **start frame** (Frame 2)
4. Set the new generated image as the **end frame**
5. Paste **Prompt 02** (see below)
6. Generate

---

## Settings

### Image Generation (Nano Banana Pro)

- **Image Model**: Nano Banana Pro
- **Aspect Ratio**: 9:16
- **Duration**: N/A (single image)

### Video Animation (Kling 3.0)

- **Video Model**: Kling 3.0
- **Resolution**: 1080p
- **Duration**: 4 seconds
- **Frames**: Start and end

---

## Prompt 01: Nano Banana Pro

_Make the drawing real_

### Instructions

Upload the screenshot **without your hand**. Fill the gold blanks with your own subject.

### Complete Prompt Text

```
Keep everything in the scene exactly the same: the page, its position and angle, the surface it
rests on, the background, the lighting, the colours, the camera angle, the perspective and the
depth of field. Do not change the composition. Keep the page layout exactly as it is, including
every block of text, at the same size, the same font and the same position, with the same
wording.

The only change is the drawing of the [YOUR SUBJECT] on the page. Replace the illustration with a
real, three dimensional [YOUR SUBJECT], at the same size, in the same place on the page, at the
same angle and in the same pose.

It is a real photograph now: [DESCRIBE THE REAL MATERIALS]. A soft contact shadow forms
beneath it where it meets the page, and it feathers out softly where it meets the bare white
paper.

Light it to match the scene. Warm ambient light from above, and a soft cool bounce lifting from
the bright page underneath. A gentle rim of light catches its upper edges. The tones sit in the
same grade as the rest of the photograph.

Keep it at the same focus depth as the page so it carries the same shallow depth of field, sharp
where the page is sharp. Real photograph, real light. No CGI, no illustration, no cartoon, no
plastic, no cut out edges, no glow or halo, no change to the text or the page.
```

### Prompt Breakdown

**Preserve Everything**:

- Page position and angle
- Surface it rests on
- Background
- Lighting
- Colors
- Camera angle
- Perspective and depth of field
- Composition unchanged
- Page layout identical
- Every block of text (same size, font, position, wording)

**The Only Change**:

- Replace drawing with real, three-dimensional version
- Same size
- Same place on page
- Same angle
- Same pose

**Photorealistic Treatment**:

- Describe real materials (not illustrated)
- Soft contact shadow where it meets page
- Shadow feathers out softly at edges
- Meets bare white paper naturally

**Lighting Match**:

- Warm ambient light from above
- **Soft cool bounce lifting from bright page underneath** ⭐
- Gentle rim light on upper edges
- Tones match rest of photograph

**Focus and Depth**:

- Same focus depth as page
- Same shallow depth of field
- Sharp where page is sharp

**Negative Constraints**:

- No CGI
- No illustration
- No cartoon
- No plastic look
- No cut out edges
- No glow or halo
- No change to text or page

### 🔑 The Secret

**The bounce light line is what sells it.** A real object sitting on a bright page catches light from underneath, and that is the detail most versions of this effect miss.

---

## Prompt 02: Kling 3.0

_Animate the transformation_

### Instructions

- **Start frame**: Your finger touching the drawing
- **End frame**: The image you just generated

### Complete Prompt Text

```
The finger presses down on the page, then lifts and the hand pulls straight back out of frame
toward the bottom of the shot within the first second, leaving the page clear.

As it lifts, the illustrated [YOUR SUBJECT] transforms into a real, lifelike [YOUR SUBJECT]. The
transition is smooth and continuous. The drawing gains volume and lifts off the flat page,
becoming solid and three dimensional, with real texture and a soft shadow beneath it. Once
fully real it is alive and moving: [DESCRIBE ITS OWN SMALL MOTION].

The camera remains completely static and the composition stays the same. The page stays in
exactly the same position and angle. The surface, the background and the lighting stay
unchanged. The printed text stays flat and unchanged in the same position. The transformation
feels seamless and believable, as if it naturally belongs in the scene.
```

### Prompt Breakdown

**Hand Movement** (First Second):

- Finger presses down on page
- Hand lifts
- Hand pulls straight back out of frame toward bottom of shot
- Page left clear

**Transformation** (As Hand Lifts):

- Illustrated subject becomes real, lifelike version
- Transition is smooth and continuous
- Drawing gains volume
- Lifts off flat page
- Becomes solid and three-dimensional
- Real texture develops
- Soft shadow forms beneath it
- Once fully real: alive and moving
- Describe its own small motion (tail wag, breathing, wings flutter, etc.)

**Everything Else Stays Still**:

- Camera completely static
- Composition unchanged
- Page position and angle unchanged
- Surface unchanged
- Background unchanged
- Lighting unchanged
- Printed text stays flat and in same position
- Transformation feels seamless and natural

### 🔑 Critical Note

**Name anything that should stay still.** Kling will invent motion in whatever you leave undescribed, so if part of your drawing should remain a flat drawing, say so directly in the prompt.

---

## Make It Yours

_A few suggestions_

### Best Practices

**Shoot at a shallow angle, not flat overhead**

- Around thirty degrees off the surface
- Leaves open air above page for smoke, clouds, or anything that needs to rise
- Without it, the effect flattens back into a screen recording

**Keep the drawing large on the page**

- Roughly a third of the frame height
- Small illustrations give the model too little to hold onto
- It starts animating the text instead

**Do not move between your two screenshots**

- They come from the same clip for a reason
- If the page shifts even slightly, the animation drifts
- The illusion breaks

**Anything that changes will move**

- If a part of your image looks different in start and end frames, the model will animate the difference
- Keep everything identical except the one thing you want to come alive

**Pick subjects that break the edge**

- The strongest versions spill past the page
- Water pouring over the side
- Smoke rising into the air
- Light falling on real surface around it
- That contact with the real world is the whole trick

**Run it several times**

- Generations vary a lot on this effect
- Especially anything involving water or hand leaving frame
- Generate a handful and keep the best one

### Works On Anything Drawn

- Storybooks
- Comics
- Tattoo flash
- Sketch on a napkin
- Old illustration in a book on your shelf

---

## Example Subjects

### Animals

- **Dog/Puppy**: "small golden retriever puppy with soft fur"
- **Motion**: "tilts its head slightly and wags its tail"

### Ships/Vehicles

- **Pirate Ship**: "wooden sailing ship with raised sails and rigging"
- **Motion**: "sails billow gently and the ship rocks slightly on water"

### Nature Elements

- **Cloud**: "small cumulus cloud with soft white edges"
- **Motion**: "drifts slowly upward and disperses slightly at edges"

### Fantasy

- **Dragon**: "small dragon with scales and wings"
- **Motion**: "stretches wings and breathes a small puff of smoke"

---

## Key Success Factors

### Critical Elements

1. **Screenshot Consistency**
   - Both frames from same clip
   - Identical lighting, angle, position
   - Only difference: hand presence

2. **Camera Angle**
   - ~30 degrees off surface (not overhead)
   - Allows vertical space for rising elements
   - Creates dimensional illusion

3. **Drawing Size**
   - Roughly 1/3 of frame height
   - Large enough for model to recognize
   - Prevents text animation issues

4. **Bounce Light Specification**
   - Cool light from bright page underneath
   - This detail sells the realism
   - Most missed element in other versions

5. **Motion Constraints**
   - Explicitly name what should stay still
   - Kling invents motion in undefined areas
   - Prevent unwanted animation

6. **Edge Breaking**
   - Best effects interact with real world
   - Elements spilling past page boundary
   - Contact with physical environment

### Technical Specifications Summary

**Image Generation**:

- **Platform**: Higgsfield (Nano Banana Pro)
- **Input**: Screenshot without hand
- **Output**: Photorealistic version of drawing

**Video Animation**:

- **Platform**: Higgsfield (Kling 3.0)
- **Start Frame**: Hand touching drawing
- **End Frame**: Generated realistic image
- **Duration**: 4 seconds
- **Aspect Ratio**: 9:16
- **Resolution**: 1080p
- **Camera**: Static throughout

**Timing**:

- First second: Hand exits frame
- Remaining time: Transformation and object motion

---

## Troubleshooting

### Drawing stays flat in animation

**Problem**: Object doesn't gain volume or dimensionality  
**Cause**: End frame lacks proper lighting (especially bounce light)  
**Solution**: Regenerate Prompt 01 with emphasis on "soft cool bounce lifting from the bright page underneath"

### Text or other elements animate unexpectedly

**Problem**: Page text moves, warps, or changes  
**Cause**: Drawing too small or elements not explicitly locked in Prompt 02  
**Solution**:

- Make drawing larger (1/3 of frame height)
- Add to Prompt 02: "The printed text stays flat and unchanged in the same position"

### Page position drifts during animation

**Problem**: Page shifts or moves during transformation  
**Cause**: Screenshots not from same clip or slight camera movement  
**Solution**: Retake both screenshots from same continuous clip without any movement

### Hand exit looks unnatural

**Problem**: Hand doesn't smoothly exit frame  
**Cause**: Generation variance in Kling  
**Solution**: Generate 4-5 versions and select cleanest hand exit

### Effect looks like screen recording

**Problem**: Transformation appears flat and digital  
**Cause**: Camera angle too overhead (90 degrees)  
**Solution**: Shoot at ~30 degree angle to create dimensional space above page

### Small details don't transform well

**Problem**: Fine details lost or muddied  
**Cause**: Drawing too small or complex  
**Solution**: Use simpler, larger drawings with clear forms

---

**Touch something and bring it to life.**
