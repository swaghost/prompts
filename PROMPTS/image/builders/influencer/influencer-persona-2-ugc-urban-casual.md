# Influencer Persona 2: UGC Creator Urban Casual - iPhone Selfie

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

## Persona 2: UGC Creator Urban Casual

### Demographics

**Gender:** Female  
**Age:** Adult (21+)  
**Ethnicity:** Latina/Mediterranean appearance  
**Skin Tone:** Tanned/olive  
**Body Type:** Slim, defined waist

### Physical Appearance

**Face:**

- Oval face shape
- Tanned/olive skin
- Dark eyebrows, slightly arched
- Deep dark eyes
- Straight nose with slightly rounded tip
- Full lips with natural pink gloss
- Defined jawline
- Slightly rosy cheeks
- Natural asymmetry maintained

**Hair:**

- Long, extremely straight
- Dark brown
- Parted in the middle
- Falling over left shoulder

**Skin Texture:**

- Smooth skin with natural hydration glow
- Glow on forehead and cheekbones
- Subtle visible pores
- Realistic texture typical of smartphone capture

**Distinctive Marks:**

- Butterfly and text tattoo on right forearm
- Smiley face and small stars/dots on right hand
- Small delicate tattoos on left wrist and hand

### Style & Vibe

**Aesthetic:** UGC creator, casual urban style, confident  
**Energy:** Confident, serene, blasé

**Outfit:**

- White strapless crop top with thin straps
- Tight to body, showing silhouette
- Gathered in center of bust
- Smooth fabric (jersey/cotton)
- Very thin straps decorated with small orange and white beads/sequins
- Medium wash blue jeans, low-rise
- Top button open and zipper slightly down

**Accessories:**

- Thin gold necklace with small pendant
- Delicate dangling earrings
- Multiple thin bracelets on left wrist
- Metal rings on hands

### Scene & Setting

**Location:** Bathroom with dark marble/porcelain wall covering with white veins

**Environment:**

- Standard white toilet partially visible in background
- Silver metal towel holder fixed to dark wall
- Clean, minimalist environment
- Light reflections on dark tiles

**Lighting:**

- Artificial bathroom ceiling light
- White/neutral light from above and bounced, illuminating face and neck evenly
- Natural medium-intensity shadows under neck and in corners against dark tile
- Medium-high contrast, highlighting white blouse and illuminated skin against dark background

### Camera & Pose

**POV:** Mirror selfie  
**Angle:** Frontal, positioned at chest/shoulder height  
**Distance:** Medium shot, framing from top of head to hip line  
**Phone Visibility:** Phone visible in mirror, dark iPhone model (appears dark purple/graphite) with three cameras, held in left hand, covering part of left chest

**Pose:**

- Standing
- Body slightly angled
- Hip shifted to left, emphasizing waist
- Weight distributed relaxed, casual posture
- Left hand raised holding phone
- Right hand lowered with thumb resting in pocket/waistband of jeans

**Expression:**

- Eyes looking directly and fixedly at camera lens through mirror reflection
- Lips relaxed, slightly parted, neutral
- Emotion: Confident, serene, blasé

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
      "Oval face shape with tanned/olive skin",
      "Deep dark eyes with dark slightly arched eyebrows",
      "Straight nose with slightly rounded tip",
      "Full lips with natural pink gloss",
      "Defined jawline with slightly rosy cheeks",
      "natural asymmetry maintained",
      "NO face alteration",
      "NO face swap errors",
      "NO generic AI face"
    ],
    "appearance_rules": {
      "general_description": "Long extremely straight dark brown hair parted in middle falling over left shoulder, tanned/olive skin, smooth skin with natural hydration glow on forehead and cheekbones, slim body with defined waist",
      "specific_marks": "Butterfly and text tattoo on right forearm, smiley face and small stars/dots on right hand, small delicate tattoos on left wrist and hand"
    }
  },
  "scene": {
    "location": "Bathroom with dark marble/porcelain wall covering with white veins",
    "environment": [
      "Standard white toilet partially visible in background",
      "Silver metal towel holder fixed to dark wall",
      "Clean minimalist environment",
      "Light reflections on dark tiles"
    ],
    "atmosphere": "Confident, serene, blasé"
  },
  "lighting": {
    "type": "Artificial bathroom ceiling light",
    "main_light": "White/neutral light from above and bounced, illuminating face and neck evenly",
    "fill_light": "Light reflections on dark marble tiles",
    "contrast": "Medium-high contrast, highlighting white blouse and illuminated skin against dark background",
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
    "angle": "Frontal, positioned at chest/shoulder height",
    "distance": "Medium shot, framing from top of head to hip line",
    "phone_visibility": "Phone visible in mirror, dark iPhone model (appears dark purple/graphite) with three cameras, held in left hand, covering part of left chest"
  },
  "subject": {
    "gender": "Female",
    "age": "adult (21+)",
    "ethnicity": "Latina/Mediterranean appearance",
    "body_type": "Slim, defined waist",
    "vibe": "UGC creator, casual urban style, confident",
    "skin_texture": "Smooth skin with natural hydration glow on forehead and cheekbones, subtle visible pores, realistic texture typical of smartphone capture",
    "expression": {
      "eyes": "Looking directly and fixedly at camera lens through mirror reflection",
      "mouth": "Lips relaxed, slightly parted, neutral with natural pink gloss",
      "emotion": "Confident, serene, blasé"
    },
    "pose": {
      "position": "Standing, body slightly angled, hip shifted to left emphasizing waist",
      "support": "Weight distributed relaxed, casual posture",
      "hand": "Left hand raised holding phone, right hand lowered with thumb resting in pocket/waistband of jeans"
    },
    "outfit": {
      "top": {
        "type": "White strapless crop top with thin straps",
        "fit": "Tight to body, showing silhouette",
        "details": "Gathered in center of bust, smooth fabric (jersey/cotton), very thin straps decorated with small orange and white beads/sequins"
      },
      "bottom": {
        "type": "Medium wash blue jeans, low-rise",
        "details": "Top button open and zipper slightly down"
      },
      "extra": [
        "Thin gold necklace with small pendant",
        "Delicate dangling earrings",
        "Multiple thin bracelets on left wrist",
        "Metal rings on hands"
      ]
    }
  },
  "image_quality": {
    "focus": "Subject's face and upper body in sharp focus, tattoos visible",
    "grain": "visible noise in low light, especially in dark background areas",
    "sharpness": "NOT extremely sharp, more lo-fi",
    "realism": "looks like real iPhone selfie posted online",
    "sensor_artifacts": "Light chromatic noise in shadow areas, sensor artifacts in darker marble background",
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

- Visible pores (subtle on face)
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
