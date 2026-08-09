# Influencer Persona 3: Urban Raw Masculine - iPhone Selfie

## Platform & Settings

**Recommended AI Platforms:**

- Nano Banana 2 (within Flow, Gemini, Magnific, etc.)
- GPT Image (within ChatGPT)

**Universal Technical Specifications:**

- Aspect Ratio: 4:5 (vertical)
- Quality: ultra_photorealistic
- Resolution: 8K
- Camera: iPhone 15 Pro Max front camera
- Lens: 24mm wide-angle
- Style: iPhone camera realism, not studio, not professional, visible natural texture

**Image Quality Standards:**

- Visible noise in low light (grain)
- NOT extremely sharp, more lo-fi
- Looks like real iPhone selfie posted online
- Slight barrel distortion from 24mm lens, slightly stretching edges
- Artificial sharpening (oversharpening) typical of iOS algorithm
- Light chromatic noise in shadow areas
- Sensor artifacts in darker areas

**Lighting to Avoid:**

- Studio lighting
- Ring light artificial
- Professional appearance
- Warm/orange tones (unless specified)
- Blown-out flash

---

## Persona 3: Urban Raw Masculine

### Demographics

**Gender:** Male  
**Age:** Adult (21+)  
**Ethnicity:** Not specified (diverse/universal)  
**Skin Tone:** Not explicitly specified  
**Body Type:** Not fully visible (close-up)

### Physical Appearance

**Face:**

- Face and facial structure from reference image only
- Same jaw line and bone structure
- Same nose, lips, eyes and facial features
- Natural asymmetry maintained

**Hair:**

- Short dark hair

**Facial Hair:**

- Stubble (sparse and textured)

**Skin Texture:**

- Visible pores
- Natural oiliness
- Realistic texture

**Distinctive Marks:**

- Extensive detailed dark tattoos covering entire neck and shoulders

### Style & Vibe

**Aesthetic:** Urban, raw, masculine  
**Energy:** Confident, serious and relaxed

**Outfit:**

- Shirtless (bare shoulders and exposed neck)
- No visible clothing in frame

**Accessories:**

- None visible

### Scene & Setting

**Location:** Interior of modern environment, possibly residential kitchen

**Environment:**

- Dark cabinets in background with built-in lighting
- Visible pendant lights and warm light strip (LED) blurred in background
- Clean and organized environment with shallow depth of field

**Lighting:**

- Mixed indoor artificial light
- Soft, diffuse light from above/front, intensely highlighting natural texture, pores and skin oiliness
- Warm ambient light (yellowish) composing background
- Medium-high contrast with natural shadows marking bone structure and bright highlights (specular highlights) on forehead and nose

### Camera & Pose

**POV:** Front selfie  
**Angle:** Eye level, very close to face  
**Distance:** Extreme close-up, framing focused entirely on face and neck  
**Phone Visibility:** Not visible, camera acts as subject's phone perspective itself

**Pose:**

- Face and shoulders directly facing camera
- Support: not visible
- Hand: not visible, holding device out of frame

**Expression:**

- Eyes looking directly at lens, fixed gaze, slightly half-closed with visible expression lines
- Mouth: closed, relaxed lips, neutral to slightly confident expression
- Emotion: Confident, serious and relaxed

---

## Universal Prompt Structure Template

```json
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "iPhone 15 Pro Max front camera",
    "lens": "24mm wide-angle",
    "style": "iPhone camera realism, not studio, not professional, visible natural texture"
  },
  "character_lock": {
    "identity_source": "[reference image]",
    "face_identity": [
      "Face and facial structure from reference image only",
      "Same jaw line and bone structure",
      "Same nose, lips, eyes and facial features",
      "natural asymmetry maintained",
      "NO face alteration",
      "NO face swap errors",
      "NO generic AI face"
    ],
    "appearance_rules": {
      "general_description": "Short dark hair, sparse textured stubble beard, visible pores and natural oiliness, realistic skin texture",
      "specific_marks": "Extensive detailed dark tattoos covering entire neck and shoulders"
    }
  },
  "scene": {
    "location": "Interior of modern environment, possibly residential kitchen",
    "environment": [
      "Dark cabinets in background with built-in lighting",
      "Visible pendant lights and warm light strip (LED) blurred in background",
      "Clean and organized environment with shallow depth of field"
    ],
    "atmosphere": "Confident, serious and relaxed"
  },
  "lighting": {
    "type": "Mixed indoor artificial light",
    "main_light": "Soft diffuse light from above/front, intensely highlighting natural texture, pores and skin oiliness",
    "fill_light": "Warm ambient light (yellowish) composing background",
    "contrast": "Medium-high contrast with natural shadows marking bone structure and bright highlights (specular highlights) on forehead and nose",
    "avoid": [
      "studio lighting",
      "ring light",
      "professional appearance",
      "blown flash"
    ]
  },
  "camera_perspective": {
    "pov": "Front selfie (arm-length)",
    "angle": "Eye level, very close to face",
    "distance": "Extreme close-up, framing focused entirely on face and neck",
    "phone_visibility": "Not visible, camera acts as subject's phone perspective itself"
  },
  "subject": {
    "gender": "Male",
    "age": "adult (21+)",
    "ethnicity": "Not specified (diverse/universal)",
    "body_type": "Not fully visible (close-up shot)",
    "vibe": "Urban, raw, masculine",
    "skin_texture": "Visible pores, natural oiliness on forehead and nose, realistic texture with specular highlights",
    "expression": {
      "eyes": "Looking directly at lens, fixed gaze, slightly half-closed with visible expression lines",
      "mouth": "Closed, relaxed lips, neutral to slightly confident expression",
      "emotion": "Confident, serious and relaxed"
    },
    "pose": {
      "position": "Face and shoulders directly facing camera",
      "support": "Not visible",
      "hand": "Not visible, holding device out of frame"
    },
    "outfit": {
      "top": {
        "type": "Shirtless",
        "fit": "Bare shoulders and exposed neck",
        "details": "No visible clothing in frame, extensive neck and shoulder tattoos fully visible"
      },
      "extra": []
    }
  },
  "image_quality": {
    "focus": "Face and neck tattoos in sharp focus, background heavily blurred (shallow depth of field)",
    "grain": "visible noise in low light, especially in background",
    "sharpness": "NOT extremely sharp, more lo-fi",
    "realism": "looks like real iPhone selfie posted online",
    "sensor_artifacts": "Light chromatic noise in shadow areas under jaw and neck, sensor artifacts in darker background",
    "lens_distortion": "slight 24mm barrel distortion, slightly stretching edges",
    "post_processing": "artificial sharpening (oversharpening) typical of iOS algorithm, highlighting skin texture and pores"
  }
}
```

---

## Realism Standards

### Identity Lock (Critical)

- Same person from reference image
- Same facial proportions, jawline and bone structure
- Same nose, lips, eyes and facial features
- Natural asymmetry maintained
- NO face alteration
- NO face swap errors
- NO generic AI face

### Appearance Rules

- Hair, skin tone, skin texture, facial imperfections, facial characteristics and overall appearance must come ONLY from reference image
- DO NOT alter skin color or characteristics
- Include tattoos, piercings or marks ONLY if they exist in reference

### Skin Texture

- Visible pores (prominent in extreme close-up)
- Natural oiliness/shine (forehead, nose)
- Realistic micro-variations of human skin
- NO overly smooth or filtered appearance
- Specular highlights on oily areas

### Image Quality

- Lo-fi iPhone quality, not professional studio
- Visible grain/noise in shadows and background
- Slight barrel distortion from 24mm lens
- iOS oversharpening artifacts
- Chromatic noise in dark areas
- Looks authentic to social media posts

### Lighting

- Mixed artificial light sources
- NO studio lighting setups
- NO ring lights
- Medium-high contrast
- Natural shadows on face
- Warm ambient background light

---

## Source

**Document:** "Prompts Gratuitos #13 Influencer de I.A" (Portuguese/Brazilian)  
**Platform:** Notion page with free realistic influencer AI prompts  
**Recommended AI Tools:** Nano Banana 2, GPT Image (ChatGPT)  
**Format:** Ultra-realistic iPhone 15 Pro Max selfie style, 4:5 vertical, 8K resolution
