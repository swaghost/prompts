# Influencer Persona 1: Fitness Lounge Aesthetic - iPhone Selfie

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

## Persona 1: Fitness Lounge Aesthetic

### Demographics

**Gender:** Female  
**Age:** Adult (21+)  
**Ethnicity:** Latina/Mediterranean appearance  
**Skin Tone:** Tanned/bronzed  
**Body Type:** Athletic, toned, defined muscles

### Physical Appearance

**Face:**

- Oval face shape
- Defined cheekbones
- Tanned skin
- Dark brown eyes
- Arched and well-defined eyebrows
- Straight nose
- Full lips with natural nude finish
- Natural asymmetry maintained

**Hair:**

- Long, straight, black
- Parted in the middle

**Skin Texture:**

- Natural visible texture
- Subtle pores on face and abdomen
- Slight natural oiliness on forehead
- Realistic micro-variations of human skin

**Distinctive Marks:**

- Stylized tattoo on sternum (between chest and neck)
- Small skin mark on lower right abdomen
- Dark red/wine colored painted nails

### Style & Vibe

**Aesthetic:** Fitness-vain, lounge aesthetic, self-confident  
**Energy:** Confident, casual-fitness, home lounge atmosphere

**Outfit:**

- Black ribbed long-sleeve crop top with chest cutout
- Tight and form-fitting
- Ribbed black fabric with strategic cutout revealing sternum tattoo
- Matching black ribbed bikini/lingerie bottoms
- Dark red/wine nail polish

**Accessories:**

- None specified

### Scene & Setting

**Location:** Modern, well-decorated bedroom

**Environment:**

- Large bed with white textured comforter and pillows (fluffy white, black and white checkered)
- Floor-to-ceiling mirrored wardrobe doors reflecting the room
- Vanity with items and ceiling spotlights visible in reflection

**Lighting:**

- Interior ceiling lighting (LED spots)
- Diffuse neutral ceiling light from above and front, evenly illuminating body
- Ambient light reflected by bright space and mirrors
- Medium contrast, highlighting muscle definition and ribbed fabric texture

### Camera & Pose

**POV:** Mirror selfie  
**Angle:** Chest-height angle, frontal view of body  
**Distance:** Full body framing (from hips up) in mirror  
**Phone Visibility:** Phone with gold/bronze case visible, held in left hand, partially covering flash

**Pose:**

- Standing in front of mirror
- Body slightly turned to right
- Supported on bedroom floor (out of view)
- Left hand holding phone with painted dark red nails
- Right hand relaxed at side of body

**Expression:**

- Eyes staring directly at camera lens in mirror
- Full lips with natural nude finish, slightly parted
- Emotion: Confident, neutral-seductive

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
      "Oval face shape with defined cheekbones",
      "Dark brown eyes with arched well-defined eyebrows",
      "Straight nose",
      "Full lips with natural nude finish",
      "Tanned skin",
      "natural asymmetry maintained",
      "NO face alteration",
      "NO face swap errors",
      "NO generic AI face"
    ],
    "appearance_rules": {
      "general_description": "Long straight black hair parted in middle, tanned/bronzed skin, natural visible texture with subtle pores, slight natural oiliness on forehead, athletic toned body with defined muscles",
      "specific_marks": "Stylized tattoo on sternum between chest and neck, small skin mark on lower right abdomen, dark red/wine colored painted nails"
    }
  },
  "scene": {
    "location": "Modern well-decorated bedroom",
    "environment": [
      "Large bed with white textured comforter and pillows (fluffy white, black and white checkered)",
      "Floor-to-ceiling mirrored wardrobe doors reflecting the room",
      "Vanity with items and ceiling spotlights visible in reflection"
    ],
    "atmosphere": "Confident, casual-fitness, home lounge atmosphere"
  },
  "lighting": {
    "type": "Interior ceiling lighting (LED spots)",
    "main_light": "Diffuse neutral ceiling light from above and front, evenly illuminating body",
    "fill_light": "Ambient light reflected by bright space and mirrors",
    "contrast": "Medium contrast, highlighting muscle definition and ribbed fabric texture",
    "avoid": [
      "studio lighting",
      "ring light",
      "professional appearance",
      "warm/orange tones",
      "blown flash"
    ]
  },
  "camera_perspective": {
    "pov": "Mirror selfie",
    "angle": "Chest-height angle, frontal view of body",
    "distance": "Full body framing (from hips up) in mirror",
    "phone_visibility": "Phone with gold/bronze case visible, held in left hand, partially covering flash"
  },
  "subject": {
    "gender": "Female",
    "age": "adult (21+)",
    "ethnicity": "Latina/Mediterranean appearance",
    "body_type": "Athletic, toned, defined muscles",
    "vibe": "Fitness-vain, lounge aesthetic, self-confident",
    "skin_texture": "Natural visible texture, subtle pores on face and abdomen, slight natural oiliness on forehead, realistic micro-variations of human skin",
    "expression": {
      "eyes": "Staring directly at camera lens in mirror",
      "mouth": "Full lips with natural nude finish, slightly parted",
      "emotion": "Confident, neutral-seductive"
    },
    "pose": {
      "position": "Standing in front of mirror, body slightly turned to right",
      "support": "Supported on bedroom floor (out of view)",
      "hand": "Left hand holding phone with painted dark red nails, right hand relaxed at side of body"
    },
    "outfit": {
      "top": {
        "type": "Black ribbed long-sleeve crop top with chest cutout",
        "fit": "Tight and form-fitting",
        "details": "Ribbed black fabric with strategic cutout revealing sternum tattoo"
      },
      "bottom": {
        "type": "Matching black ribbed bikini/lingerie bottoms"
      },
      "extra": ["Dark red/wine nail polish on nails"]
    }
  },
  "image_quality": {
    "focus": "Subject's face, body, and ribbed fabric texture in sharp focus",
    "grain": "visible noise in low light",
    "sharpness": "NOT extremely sharp, more lo-fi",
    "realism": "looks like real iPhone selfie posted online",
    "sensor_artifacts": "Light chromatic noise in shadow areas, sensor artifacts in darker areas",
    "lens_distortion": "slight 24mm barrel distortion, slightly stretching edges",
    "post_processing": "artificial sharpening (oversharpening) typical of iOS algorithm"
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

- Visible pores (subtle on face, abdomen)
- Natural oiliness/hydration glow (forehead, nose tip, cheekbones)
- Realistic micro-variations of human skin
- NO overly smooth or filtered appearance

### Image Quality

- Lo-fi iPhone quality, not professional studio
- Visible grain/noise in shadows
- Barrel distortion from 24mm lens
- iOS oversharpening artifacts
- Chromatic noise in dark areas
- Looks authentic to social media posts

### Lighting

- Natural or practical artificial light sources
- NO studio lighting setups
- NO ring lights
- Medium to medium-high contrast
- Realistic shadows and highlights

---

## Source

**Document:** "Prompts Gratuitos #13 Influencer de I.A" (Portuguese/Brazilian)  
**Platform:** Notion page with free realistic influencer AI prompts  
**Recommended AI Tools:** Nano Banana 2, GPT Image (ChatGPT)  
**Format:** Ultra-realistic iPhone 15 Pro Max selfie style, 4:5 vertical, 8K resolution
