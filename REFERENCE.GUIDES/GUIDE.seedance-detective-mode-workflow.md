# 🔍 SEEDANCE: DETECTIVE MODE WORKFLOW GUIDE

**A complete, step-by-step workflow for creating cinematic detective investigation scenes using identity-preserved face swaps and motion transfer. Transform yourself into a detective working on complex cases with realistic investigation materials, cinematic lighting, and professional film quality.**

---

## Overview

This workflow uses **Nano Banana Pro** (image generation) and **Seedance 2.0** (motion transfer video) to create professional detective investigation scenes across three different setups:

1. **Clip 1**: Detective examining wall of missing persons evidence
2. **Clip 2**: Detective working at desk with investigation materials (overhead view)
3. **Clip 3**: Detective surrounded by investigation materials on floor (overhead view)

Each clip follows a two-step process:

- **Step 1**: Generate a cinematic still image with Nano Banana Pro
- **Step 2**: Animate using your recorded motion with Seedance 2.0

---

## Required Tools

- **[OpenArt](https://openart.ai/home)** (All-in-One AI platform)
  - Use code **SKAI25** for 25% off for 3 months
  - Access to Nano Banana Pro (image generation)
  - Access to Seedance 2.0 (video motion transfer)

---

## General Workflow (All Clips)

### Preparation

1. **Record a video** of yourself performing the action for the scene
2. **Take a screenshot** from your video (this becomes your identity reference)

### Step 1: Generate Still Image (Nano Banana Pro)

1. Go to [Nano Banana Pro in OpenArt](https://openart.ai/suite/create-image/nano-banana-2)
2. Upload your screenshot
3. Paste the appropriate **Nano Banana prompt** for your chosen clip
4. Generate the image

### Step 2: Animate with Motion Transfer (Seedance 2.0)

1. Go to [Seedance 2.0 in OpenArt](https://openart.ai/suite/create-video/byte-plus-seedance-2)
2. Upload your **Nano Banana generated image** (Reference Image 1)
3. Upload your **original recorded video** (Source Video 1)
4. Paste the appropriate **Seedance 2.0 prompt** for your clip
5. Generate the animation

---

## Clip 1: Wall Investigation Scene

**Setup**: Detective examining a wall covered with missing person photos, newspaper clippings, maps, and red string connections.

**Recording Instructions**: Record yourself looking at a blank wall, turning your head, examining details.

### Technical Specs

- **Camera**: ARRI Alexa cinematic rendering
- **Depth of Field**: Shallow (subject in focus, wall slightly out of focus)
- **Lighting**: Warm wall-mounted lamp above photos, dark ambient background
- **Atmosphere**: Nighttime interior, investigative mood

**See Full Prompts**: [PROMPT.detective-wall-investigation.md](../REFERENCE.PROMPT-TEMPLATES/PROMPT.detective-wall-investigation.md)

---

## Clip 2: Desk Investigation Scene (Overhead)

**Setup**: Overhead view of detective working at a walnut table covered with investigation materials—map, photos, newspapers, evidence folders, coffee mug, magnifying glass.

**Recording Instructions**: Record yourself from above working at a table—examining documents, moving hands, pointing at items, thinking.

### Key Details

- **Camera**: Fixed overhead ceiling camera perspective
- **Orientation**: ALL materials oriented toward the woman (not the camera)
- **Props**: City map, photographs, newspapers, sticky notes, manila folders, coffee mug, magnifying glass, forensic gloves, paper clips
- **Lighting**: Single warm tungsten desk lamp (outside frame), creating concentrated pool of light
- **Atmosphere**: Nighttime residential interior, intimate investigative workspace

**See Full Prompts**: [PROMPT.detective-desk-investigation-overhead.md](../REFERENCE.PROMPT-TEMPLATES/PROMPT.detective-desk-investigation-overhead.md)

---

## Clip 3: Floor Investigation Scene (Overhead)

**Setup**: Overhead view of detective standing on rug completely covered with investigation materials spreading in all directions—maps, reports, photos, clippings creating an immersive crime-analysis workspace.

**Recording Instructions**: Record yourself from above standing on a rug, moving naturally, shifting weight, examining materials on the floor around you.

### Key Details

- **Camera**: Fixed overhead perspective
- **Coverage**: 85-90% of rug covered with investigation materials
- **Props**: Folded city maps, police reports, case files, newspaper clippings, photographs, evidence folders, handwritten notes, sticky notes
- **Lighting**: Single warm tungsten floor lamp (outside frame), concentrated center light fading to edges
- **Atmosphere**: Late-night residential interior, obsessive investigation feel

**See Full Prompts**: [PROMPT.detective-floor-investigation-overhead.md](../REFERENCE.PROMPT-TEMPLATES/PROMPT.detective-floor-investigation-overhead.md)

---

## Key Principles Across All Clips

### Identity Preservation

- **Face must remain 100% identical** to reference screenshot
- Preserve exact facial features, eyes, nose, lips, face shape, skin texture, expression
- Do NOT modify, beautify, retouch, or regenerate the face
- Keep hair, clothing, body proportions unchanged

### Motion Transfer

- Transfer movements **100% one-to-one** from source video
- Identical timing, gestures, body language, head turns, pose changes
- Frame-by-frame accuracy
- Do NOT add, remove, speed up, slow down, or alter motion

### Cinematic Quality

- **ARRI Alexa** rendering style
- Soft organic image (not oversharpened)
- Filmic highlight and shadow roll-off
- Subtle analog film grain
- Muted true-to-life colors with gentle warmth
- Accurate skin tones

### Lighting Approach

- **Single practical light source** (lamp) as primary illumination
- Warm tungsten color temperature
- Concentrated pool of light with natural falloff
- Deep shadows in background
- No daylight, no ceiling lights, no flat lighting
- Intimate, cinematic atmosphere

### Investigation Materials

- **Authentic physical textures**: Paper fibers, creased corners, handling marks, coffee stains
- Realistic wear and tear on all props
- Organic arrangement (not perfectly aligned)
- Materials oriented naturally for the detective's use
- Contact shadows on all objects

---

## Best Practices

✅ **Record clean source video**: Stable camera, good lighting on your face, clear motion  
✅ **Screenshot quality**: Use the best frame where your face is clear and well-lit  
✅ **Match the setup**: If clip requires overhead view, record from overhead angle  
✅ **Natural motion**: Perform realistic detective actions—don't overact  
✅ **Review Nano Banana output**: Make sure identity is preserved before moving to Seedance  
✅ **Exact prompt copying**: Use the full prompts exactly as written for best results

⚠️ **Avoid**:

- Harsh lighting in source video
- Blurry or pixelated screenshots
- Exaggerated or theatrical movements
- Modifying prompts significantly (they're precisely tuned)
- Rushing through Nano Banana generation (quality matters)

---

## Cinematic Reference Style

These prompts are designed to emulate the aesthetic of premium psychological crime thrillers:

- **Mindhunter** (Netflix series)
- **Zodiac** (David Fincher)
- **Prisoners** (Denis Villeneuve)
- **True Detective** (Season 1)

Expect: Dark, moody, realistic, tactile, obsessive investigation atmosphere with professional film cinematography.

---

## Troubleshooting

**Issue**: Face doesn't match reference in Nano Banana output  
**Solution**: Regenerate with emphasis on identity preservation. Ensure your reference screenshot is high quality and well-lit.

**Issue**: Motion feels stiff or doesn't match in Seedance  
**Solution**: Check that your source video has smooth, natural motion. Avoid jerky camera movements.

**Issue**: Investigation materials look fake or CGI  
**Solution**: The prompts specifically call for realistic textures. Try regenerating or ensure you're using the full unmodified prompts.

**Issue**: Lighting too bright or flat  
**Solution**: The prompts specify nighttime single-lamp lighting. Don't modify lighting instructions—they're carefully balanced.

**Issue**: Objects floating or incorrect orientation (Clips 2 & 3)  
**Solution**: The prompts specify proper contact shadows and orientation. Regenerate if this occurs.

---

## Workflow Summary

```
1. RECORD source video (perform detective actions)
   ↓
2. SCREENSHOT from video (identity reference)
   ↓
3. NANO BANANA PRO (generate still image)
   - Upload screenshot
   - Paste Nano Banana prompt
   - Generate
   ↓
4. SEEDANCE 2.0 (animate with motion)
   - Upload Nano Banana image
   - Upload source video
   - Paste Seedance prompt
   - Generate
   ↓
5. RESULT: Cinematic detective investigation scene
```

Repeat for all three clips to create a complete detective investigation sequence.

---

**Source**: [Google Docs Guide](https://docs.google.com/document/d/1s1ovJ8VzbkXEH_umi7or7YJgoAvclAlRP92_EsTbPKw/mobilebasic?urp=gmail_link)
