# Influencer Persona 4: Clean Girl Aesthetic - iPhone Selfie

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

## Persona 4: Clean Girl Aesthetic Influencer

### Demographics

**Gender:** Female  
**Age:** Adult (21+)  
**Ethnicity:** Caucasian/Mediterranean appearance  
**Skin Tone:** Tanned  
**Body Type:** Slim, toned

### Physical Appearance

**Face:**

- Oval face shape
- Well-defined and tapered jawline
- Straight and symmetrical nose
- Full and voluminous lips with transparent shiny lip gloss
- Dark brown almond-shaped eyes
- Arched and well-filled eyebrows
- Natural asymmetry maintained

**Hair:**

- Long straight brown hair with blonde highlights (balayage)
- Loose and slightly side-parted

**Skin Texture:**

- Tanned skin
- Subtle pores on cheeks
- Natural hydration/oiliness glow on forehead and tip of nose
- Smooth but realistic and human skin

**Distinctive Marks:**

- Multiple gold hoop earrings lined up on right ear

### Style & Vibe

**Aesthetic:** Clean girl aesthetic influencer, confident, casual elegant  
**Energy:** Confident, relaxed and neutral

**Outfit:**

- White strapless tube top
- Tight to body, adherent to bust
- White fabric with horizontal gathered texture throughout length (smocked/ruched)

**Accessories:**

- Thin gold chain with small cross pendant on neck
- Multiple thin bracelets on left wrist
- Metal rings on hands

### Scene & Setting

**Location:** Indoor area with natural lighting connected to garden, possibly veranda or room with skylight

**Environment:**

- Vertical wood slat wall on left
- Lush green tropical plants and wicker/rattan chair in background on right
- Floor covered with sisal or natural weave rug
- Clean, well-decorated and aesthetically pleasing environment

**Lighting:**

- Soft natural daylight
- Diffuse natural light from front and slightly from above, illuminating face and neck very evenly
- Ambient light reflected by bright space, creating very soft shadows under neck and chin
- Low to medium contrast
- Very illuminated and warm skin tones

### Camera & Pose

**POV:** Hand-held selfie (arm-length selfie)  
**Angle:** Slightly high angle (high angle), camera looking slightly down toward face, with face tilted upward  
**Distance:** Framing from chest up (medium close-up)  
**Phone Visibility:** Phone does not appear, is out of frame being held by outstretched right hand

**Pose:**

- Sitting on floor
- Torso slightly leaning toward camera
- Supported sitting on braided texture rug
- Right arm stretched out of frame holding camera
- Left arm relaxed downward

**Expression:**

- Eyes staring fixedly and relaxed directly at camera lens
- Lips slightly relaxed making very subtle pout, quite shiny from gloss
- Emotion: Confident, relaxed and neutral

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
      "Oval face shape with well-defined tapered jawline",
      "Straight and symmetrical nose",
      "Full and voluminous lips with transparent shiny lip gloss",
      "Dark brown almond-shaped eyes",
      "Arched and well-filled eyebrows",
      "Tanned skin",
      "natural asymmetry maintained",
      "NO face alteration",
      "NO face swap errors",
      "NO generic AI face"
    ],
    "appearance_rules": {
      "general_description": "Long straight brown hair with blonde highlights (balayage), loose and slightly side-parted, tanned skin with subtle pores on cheeks, natural hydration/oiliness glow on forehead and tip of nose, slim toned body",
      "specific_marks": "Multiple gold hoop earrings lined up on right ear"
    }
  },
  "scene": {
    "location": "Indoor area with natural lighting connected to garden, possibly veranda or room with skylight",
    "environment": [
      "Vertical wood slat wall on left",
      "Lush green tropical plants and wicker/rattan chair in background on right",
      "Floor covered with sisal or natural weave rug",
      "Clean, well-decorated and aesthetically pleasing environment"
    ],
    "atmosphere": "Confident, relaxed and neutral"
  },
  "lighting": {
    "type": "Soft natural daylight",
    "main_light": "Diffuse natural light from front and slightly from above, illuminating face and neck very evenly",
    "fill_light": "Ambient light reflected by bright space",
    "contrast": "Low to medium contrast, very illuminated and warm skin tones",
    "avoid": [
      "studio lighting",
      "ring light",
      "professional appearance",
      "blown flash"
    ]
  },
  "camera_perspective": {
    "pov": "Hand-held selfie (arm-length selfie)",
    "angle": "Slightly high angle (high angle), camera looking slightly down toward face, with face tilted upward",
    "distance": "Framing from chest up (medium close-up)",
    "phone_visibility": "Phone does not appear, is out of frame being held by outstretched right hand"
  },
  "subject": {
    "gender": "Female",
    "age": "adult (21+)",
    "ethnicity": "Caucasian/Mediterranean appearance",
    "body_type": "Slim, toned",
    "vibe": "Clean girl aesthetic influencer, confident, casual elegant",
    "skin_texture": "Tanned skin, subtle pores on cheeks, natural hydration/oiliness glow on forehead and tip of nose, smooth but realistic and human skin",
    "expression": {
      "eyes": "Staring fixedly and relaxed directly at camera lens",
      "mouth": "Lips slightly relaxed making very subtle pout, quite shiny from transparent lip gloss",
      "emotion": "Confident, relaxed and neutral"
    },
    "pose": {
      "position": "Sitting on floor, torso slightly leaning toward camera",
      "support": "Supported sitting on braided texture rug",
      "hand": "Right arm stretched out of frame holding camera, left arm relaxed downward"
    },
    "outfit": {
      "top": {
        "type": "White strapless tube top",
        "fit": "Tight to body, adherent to bust",
        "details": "White fabric with horizontal gathered texture throughout length (smocked/ruched)"
      },
      "extra": [
        "Thin gold chain with small cross pendant on neck",
        "Multiple thin bracelets on left wrist",
        "Metal rings on hands",
        "Multiple gold hoop earrings lined up on right ear"
      ]
    }
  },
  "image_quality": {
    "focus": "Subject's face and upper body in sharp focus, background slightly soft",
    "grain": "visible noise in low light, minimal due to bright natural lighting",
    "sharpness": "NOT extremely sharp, more lo-fi",
    "realism": "looks like real iPhone selfie posted online",
    "sensor_artifacts": "Light chromatic noise in shadow areas under neck, sensor artifacts minimal in well-lit scene",
    "lens_distortion": "slight 24mm barrel distortion, slightly stretching edges",
    "post_processing": "artificial sharpening (oversharpening) typical of iOS algorithm, warm color grading"
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

- Visible pores (subtle on cheeks)
- Natural oiliness/hydration glow (forehead, nose tip)
- Realistic micro-variations of human skin
- NO overly smooth or filtered appearance
- Dewy clean girl aesthetic but still realistic

### Image Quality

- Lo-fi iPhone quality, not professional studio
- Minimal grain/noise due to bright natural light
- Slight barrel distortion from 24mm lens
- iOS oversharpening artifacts
- Warm color grading typical of natural light
- Looks authentic to social media posts

### Lighting

- Soft natural daylight (window or skylight)
- NO studio lighting setups
- NO ring lights
- Low to medium contrast
- Even illumination
- Warm skin tones

---

## Source

**Document:** "Prompts Gratuitos #13 Influencer de I.A" (Portuguese/Brazilian)  
**Platform:** Notion page with free realistic influencer AI prompts  
**Recommended AI Tools:** Nano Banana 2, GPT Image (ChatGPT)  
**Format:** Ultra-realistic iPhone 15 Pro Max selfie style, 4:5 vertical, 8K resolution
