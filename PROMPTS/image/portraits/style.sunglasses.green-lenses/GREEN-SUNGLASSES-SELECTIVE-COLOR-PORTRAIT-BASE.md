# GREEN SUNGLASSES PORTRAIT - SELECTIVE COLOR DRAMA (BASE PROMPT)

**Prompt Type:** Image Generation - Dramatic Portrait Photography  
**Style:** High-contrast black and white with selective color (green sunglasses only)  
**Technique:** Chiaroscuro lighting, ultra-close crop, cinematic realism  
**Platforms:** Midjourney, DALL-E 3, Stable Diffusion XL, Flux Pro (with reference photo support)  
**Resolution:** 8K ultra-detailed  
**Aspect Ratio:** 2:3 (portrait)

---

> **📚 Full Guide Available:** For detailed variations, customization options, post-processing workflows, and troubleshooting, see **[GREEN-SUNGLASSES-SELECTIVE-COLOR-PORTRAIT.md](GREEN-SUNGLASSES-SELECTIVE-COLOR-PORTRAIT.md)**

---

## CONCEPT

Photorealistic ultra-close portrait with dramatic chiaroscuro lighting. The entire image is rendered in high-contrast black and white except for the vivid green mirrored tint of retro-style round sunglasses, which remain in full color.

**Visual Impact:**

- Mysterious, rebellious, powerful atmosphere
- Selective color technique (ONLY sunglasses in color)
- Extreme close cropping for intimacy
- Chiaroscuro 1:3 light-to-shadow ratio

---

## COMPLETE PROMPT

```
A photorealistic ultra-close angled portrait derived from the provided reference photo, tightly cropped so that only a partial view of the face is visible, with one side submerged in deep cinematic shadow while the opposite side is struck by a powerful directional light that sculpts and emphasizes the sharp jawline, the fine grain of the skin, visible pores, and subtle beard stubble. The image is rendered in dramatic high-contrast black and white with selective color grading that leaves only the vivid green mirrored tint of the retro-style round sunglasses illuminated and reflective. Composition is extremely tight and intimate, locking focus on the eyes behind the lenses and the faint confident smirk playing across the lips. Lighting is pure moody chiaroscuro with a strong 1:3 light-to-shadow ratio, creating intense drama and depth. The subject wears a black shirt. Background is completely dark and softly out of focus, isolating the face and amplifying the powerful, mysterious, rebellious, and intense atmosphere. Captured with the equivalent of an 85 mm portrait lens and extremely shallow depth of field, the entire frame is ultra-detailed, 8K resolution, cinematic realism, with rich skin texture, precise reflective surfaces on the lenses, and an overall tone of high drama and quiet defiance.
```

---

## PLATFORM-SPECIFIC PARAMETERS

### Midjourney v6+

```
[Full prompt above]

Reference image: [upload portrait photo]
--ar 2:3 --style raw --s 750 --v 6.1 --no color except on sunglasses, oversaturated, flat lighting, soft shadows, multiple light sources
```

**Note:** May require post-processing to perfect selective color effect. Generate in full color, then desaturate all except sunglasses in Photoshop/Lightroom.

### DALL-E 3

```
[Full prompt above, add emphasis:]

IMPORTANT: The entire image is in dramatic high-contrast black and white EXCEPT for the sunglasses lenses, which are the ONLY element rendered in vivid green color. All skin, clothing, and background are completely desaturated black and white.
```

### Stable Diffusion XL

**Recommended Workflow:**

1. Generate portrait in full color
2. Post-process: Desaturate entire image
3. Mask sunglasses and restore green color
4. Adjust contrast for dramatic B&W

**Settings:**

- **Checkpoint:** RealVisXL 4.0 or Juggernaut XL
- **Steps:** 40-50
- **Sampler:** DPM++ 2M Karras
- **CFG Scale:** 8-10
- **Resolution:** 768x1152 (2:3 portrait)

### Flux Pro

```
[Full prompt above]

Guidance: 4.0
Steps: 30
Aspect Ratio: 2:3
```

**Note:** Flux handles selective color well with strong prompt emphasis.

---

## KEY ELEMENTS

### What This Creates

- **Cropping:** Ultra-close, partial face view only
- **Lighting:** Chiaroscuro 1:3 ratio (one-third light, two-thirds deep shadow)
- **Color:** High-contrast B&W with ONLY green sunglasses in color
- **Sunglasses:** Retro round style with vivid green mirrored lenses
- **Expression:** Confident smirk, eyes visible behind lenses
- **Texture:** Visible pores, beard stubble, skin grain
- **Background:** Completely dark, softly blurred
- **Mood:** Powerful, mysterious, rebellious, intense

### Technical Specs

- **Lens Equivalent:** 85mm portrait lens
- **Depth of Field:** Extremely shallow (f/1.4-f/2.0 aesthetic)
- **Resolution:** 8K ultra-detailed
- **Lighting Style:** Single directional key light from one side
- **Focus:** Sharp on eyes and front of face, everything else soft

---

## QUICK CUSTOMIZATION

### Change Sunglasses Color

Replace "vivid green" with:

- **Electric Blue** - Modern, tech-forward
- **Purple/Violet** - Mysterious, artistic
- **Amber/Gold** - Classic, sophisticated
- **Red/Ruby** - Dangerous, intense
- **Rose Gold** - Elegant, modern
- **Neon Pink** - Bold, rebellious

### Change Sunglasses Style

Replace "retro-style round" with:

- **Aviator** - Classic, masculine
- **Wayfarer** - Iconic 50s, rectangular
- **Cat-eye** - Vintage, dramatic
- **Geometric hexagonal** - Contemporary
- **Oversized square** - Bold statement

### Change Expression

Replace "faint confident smirk" with:

- **Slight knowing smile** - Mysterious
- **Lips pressed in serious line** - Intense
- **Neutral, expressionless** - Cool, detached
- **One corner of mouth raised** - Cocky, amused

---

## CRITICAL NEGATIVES

```
color on skin, color on clothing, color on background, fully colored image, flat lighting, soft lighting, no contrast, low contrast, overexposed, underexposed, blurry, out of focus, soft focus on eyes, no sunglasses, wrong sunglasses style, clear lenses, no color on lenses, multiple light sources, white background, bright background, visible background details, wide shot, full face visible, standard crop, smiling broadly, smooth skin, airbrushed, beauty filter, no pores, no stubble, plastic skin, digital render, 3D render, illustration, cartoon, oversaturated color, multiple colors, text, logos, watermarks, low resolution, distorted face, wrong proportions
```

---

## POST-PROCESSING QUICK GUIDE

If AI doesn't achieve perfect selective color:

### Photoshop (Quick Method)

1. Open image in Photoshop
2. Desaturate: Cmd/Ctrl + Shift + U
3. Layer > New > Layer via Copy (undo desaturation to get color back)
4. Add black layer mask to color layer
5. Paint white on mask over sunglasses only
6. Adjust green saturation if needed

### Lightroom (Quick Method)

1. Import image
2. Set Saturation to -100 (converts to B&W)
3. Select Adjustment Brush
4. Set brush Saturation to +100
5. Paint over sunglasses only
6. Adjust green luminance/saturation

### Mobile: Snapseed

1. Tools > Selective
2. Desaturate entire image
3. Select sunglasses area
4. Increase saturation to 100

---

## COMMON ISSUES & QUICK FIXES

**Issue: Sunglasses not in color**

- Regenerate with: "CRITICAL: sunglasses lenses are the ONLY element in vivid green color"
- Or post-process to restore color

**Issue: Too much color showing**

- Post-process to remove unwanted color
- Emphasize: "Everything except sunglasses completely desaturated"

**Issue: Lighting too flat**

- Add: "Extreme chiaroscuro with deep blacks on shadow side::2"
- Emphasize 1:3 light-to-shadow ratio

**Issue: Crop not tight enough**

- Add: "Extremely tight ultra-close crop showing only partial face::2"
- Specify: "Frame from mid-forehead to just below lips"

**Issue: Skin too smooth**

- Add: "Visible pores, beard stubble, skin grain texture, NOT smoothed::2"
- Negative: "beauty filter, airbrushed, smooth skin"

---

## USE CASES

- **Album Covers** - Mysterious artist portraits
- **Fashion Editorial** - Eyewear campaigns
- **Personal Branding** - Social media profile pictures
- **Marketing Materials** - Bold attention-grabbing imagery
- **Fine Art Photography** - Gallery-worthy portraits

---

## TIPS FOR BEST RESULTS

1. **Use high-quality reference photo** - Sharp, clear facial features essential
2. **Generate in color first** - Easier to control all elements, then post-process
3. **Check chiaroscuro ratio** - Should be clearly 1/3 light, 2/3 shadow
4. **Verify sunglasses style** - Retro round with visible eyes behind lenses
5. **Boost contrast in post** - Final B&W should be dramatic high-contrast
6. **Perfect selective color in editing** - AI rarely gets it 100% right

---

## VARIATIONS AVAILABLE

See the **[full guide](GREEN-SUNGLASSES-SELECTIVE-COLOR-PORTRAIT.md)** for:

- 7 sunglasses color variations with mood descriptions
- 8 sunglasses style options (aviator, wayfarer, cat-eye, etc.)
- 6 expression variations (confident, serious, playful)
- 4 lighting ratio alternatives
- 9 background options (urban, natural, minimal)
- 6 clothing variations
- Alternative lighting styles (Rembrandt, split, broad, short)
- Multiple selective color element techniques
- Series concept ideas
- Alternative aspect ratios
- Complete post-processing workflows
- Detailed troubleshooting guide

---

**Related Files:**

- **Guide:** [GREEN-SUNGLASSES-SELECTIVE-COLOR-PORTRAIT.md](GREEN-SUNGLASSES-SELECTIVE-COLOR-PORTRAIT.md) - Full comprehensive guide with all variations
- **Similar Techniques:** [FOOTBALL-SOCCER-PLAYER-POSTER-GRAPHIC-TYPE.md](FOOTBALL-SOCCER-PLAYER-POSTER-GRAPHIC-TYPE.md) - Identity lock for face accuracy

---

**Style:** Selective color B&W portrait  
**Key Feature:** ONLY green sunglasses in color, everything else B&W  
**Lighting:** Chiaroscuro 1:3 ratio  
**Mood:** Mysterious, rebellious, powerful, intense  
**Quality:** 8K ultra-detailed cinematic realism
