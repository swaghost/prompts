# From Google Map to Drone Photograph

**Step-by-step workflow for converting Google Maps satellite imagery into cinematic drone photography**

Transform flat, top-down satellite screenshots into realistic aerial photographs with dramatic lighting, atmospheric depth, and photographic quality.

---

## Workflow Overview

**Input**: Google Maps satellite screenshot (top-down view)  
**Output**: Cinematic drone photograph with realistic lighting and depth  
**Platform**: Nano Banana or similar image-to-image AI

---

## Step 1: Clean Up the Source Image

**Remove UI elements:**
- Search bar
- Location pins
- Labels list
- Navigation controls
- Any text overlays

**Keep only**: The clean satellite terrain view

---

## Step 2: Upload as Reference Image

Upload your cleaned screenshot into your AI tool as a **reference image** (not just text description).

The AI will use this to maintain the exact geography, road layout, and spatial relationships.

---

## Step 3: Use This Prompt

```
A hyper-realistic, cinematic drone photograph based strictly on the geography and layout of the provided satellite image. 

Transform the flat, top-down satellite view into a slight oblique angle (high-angle shot) to create three-dimensional depth. The ground should not look flat; it must show realistic elevation changes and topography based on the image's features. 

Apply dramatic Golden Hour (sunrise/sunset) lighting. The low sun angle must cast long, distinct, directional shadows from every tree, building, and hill, defining their shapes on the ground. The light should be warm and rich. 

Add atmospheric haze and perspective, making distant elements slightly bluer and softer. 

Enhance environmental textures: trees must be volumetric with individual leaves, water surfaces must be reflective, and roads/buildings must show realistic weathering and material textures. 

Shot on a high-resolution aerial cinema camera, incredible detail, ultra-sharp focus across the frame, natural cinematic color grading, realistic scale, 8K quality. 

Remove all text, labels, icons, map markings, and UI elements from the original Google Earth/Google Maps image while preserving the exact road geometry and site layout.
```

---

## Key Elements Explained

### Perspective Transformation
- **From**: Flat orthographic satellite view
- **To**: Slight oblique angle (15-30° from vertical)
- Creates three-dimensional depth while maintaining geographic accuracy

### Lighting Requirements
- **Golden Hour**: Warm, rich light (sunrise or sunset)
- **Low Sun Angle**: Creates long, dramatic shadows
- **Directional Shadows**: Define shapes and topography
- **Shadow Direction**: Consistent across entire image

### Atmospheric Effects
- **Distance Haze**: Bluish atmospheric perspective
- **Depth Cues**: Distant elements softer and less saturated
- **Natural Gradient**: Clear in foreground to hazy at horizon

### Material & Texture Enhancement
- **Trees**: Volumetric with visible individual leaves
- **Water**: Reflective surfaces (lakes, rivers, ocean)
- **Roads**: Realistic weathering, tire marks, line painting
- **Buildings**: Material textures, weathering, roof details

### Technical Quality
- **Resolution**: 8K quality output
- **Sharpness**: Ultra-sharp focus throughout frame
- **Color Grading**: Natural cinematic color (not oversaturated)
- **Scale**: Maintain realistic proportions

### Clean Output
- Remove all Google Maps UI elements:
  - Text labels
  - Location markers
  - Icons
  - Compass
  - Scale bar
  - Copyright notices

---

## Before & After Comparison

**Before (Google Maps Satellite)**:
- Flat orthographic view
- Even lighting
- UI elements visible
- Limited texture detail
- Blue/green color palette

**After (Drone Photograph)**:
- Slight oblique angle
- Dramatic golden hour lighting
- No UI elements
- Rich material textures
- Warm cinematic color grading

---

## Tips for Best Results

1. **Crop Tightly**: Focus on area of interest before cleaning
2. **High Zoom Level**: Use highest resolution satellite view available
3. **Clear Features**: Works best with distinct landmarks and geography
4. **Lighting Choice**: Specify sunrise for east-lit or sunset for west-lit scenes
5. **Urban vs Nature**: Works for both cityscapes and natural landscapes
6. **Iteration**: May need 2-3 generations to get perfect lighting

---

## Use Cases

- **Architecture**: Transform site plans into realistic aerial views
- **Real Estate**: Create marketing imagery from property locations
- **Urban Planning**: Visualize developments with realistic lighting
- **Film/VFX**: Establish shots matching real locations
- **Travel Content**: Create dramatic aerial photography of any location
- **Before/After**: Show potential of locations under ideal conditions

---

## Platform Recommendations

**Best For**:
- Nano Banana
- Midjourney with image prompts
- Stable Diffusion with ControlNet
- Other image-to-image AI tools

**Settings**:
- Image weight: High (to maintain geography)
- Style strength: Medium (to allow realistic transformation)
- Quality: Maximum available

---

## Variations

You can modify the prompt for different looks:

**Blue Hour Version**: Replace "Golden Hour" with "Blue Hour (dusk)" for cooler tones

**Midday Version**: Replace with "harsh midday sun, short shadows, bright clear light"

**Stormy Version**: Add "dramatic storm clouds, dark moody lighting, pre-storm atmosphere"

**Night Version**: Replace with "night aerial, city lights, long exposure, light trails"

---

## Credits

Workflow developed for architectural visualization and location-based content creation. Maintains geographic accuracy while adding photographic realism and atmosphere.
