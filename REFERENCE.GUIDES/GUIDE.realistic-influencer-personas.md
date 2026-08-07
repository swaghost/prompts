# Realistic Influencer Personas - Quick Reference Guide

## Platform Settings (Universal)

**AI Tools:** Nano Banana 2, GPT Image (ChatGPT)  
**Aspect Ratio:** 4:5 vertical  
**Resolution:** 8K  
**Camera:** iPhone 15 Pro Max front camera, 24mm wide-angle  
**Style:** Ultra-realistic iPhone selfie, NOT studio/professional

---

## 4 Persona Profiles

### Persona 1: Fitness Lounge Queen

**Demographics:**

- Gender: Female
- Age: 21+
- Ethnicity: Latina/Mediterranean
- Skin: Tanned/bronzed
- Build: Athletic, toned, defined muscles

**Key Features:**

- Long straight black hair (middle part)
- Dark brown eyes, arched eyebrows
- Full lips with nude finish
- Oval face, defined cheekbones
- Sternum tattoo (stylized)
- Small abdomen mark
- Dark red/wine nails

**Style:** Fitness-vain, lounge aesthetic, self-confident

**Outfit:** Black ribbed crop top with chest cutout + black ribbed bikini bottoms

**Setting:** Modern bedroom, mirror selfie, LED spot ceiling lights

**Vibe:** Confident casual-fitness, home lounge atmosphere

---

### Persona 2: UGC Urban Creator

**Demographics:**

- Gender: Female
- Age: 21+
- Ethnicity: Latina/Mediterranean
- Skin: Tanned/olive
- Build: Slim, defined waist

**Key Features:**

- Long extremely straight dark brown hair (middle part, falls over left shoulder)
- Deep dark eyes, slightly arched dark brows
- Full lips with natural pink gloss
- Straight nose, rounded tip
- Defined jawline, rosy cheeks
- Butterfly + text tattoo (right forearm)
- Smiley face + stars tattoos (right hand)
- Small delicate tattoos (left wrist/hand)

**Style:** UGC creator, casual urban, confident

**Outfit:** White strapless crop top with beaded thin straps + low-rise medium wash jeans (unbuttoned)

**Accessories:** Thin gold necklace, dangling earrings, multiple bracelets, rings

**Setting:** Bathroom with dark marble walls, mirror selfie

**Vibe:** Confident, serene, blasé

---

### Persona 3: Urban Raw Masculine

**Demographics:**

- Gender: Male
- Age: 21+
- Ethnicity: Diverse/universal
- Skin: Not specified
- Build: Not fully visible (extreme close-up)

**Key Features:**

- Short dark hair
- Stubble beard (sparse, textured)
- Extensive detailed dark tattoos (entire neck and shoulders)
- Natural skin texture with visible pores and oiliness
- Fixed gaze, slightly half-closed eyes with expression lines

**Style:** Urban, raw, masculine

**Outfit:** Shirtless (bare shoulders and neck exposed)

**Setting:** Modern interior (possibly kitchen), close-up selfie, warm LED background lighting

**Vibe:** Confident, serious, relaxed

---

### Persona 4: Clean Girl Aesthetic

**Demographics:**

- Gender: Female
- Age: 21+
- Ethnicity: Caucasian/Mediterranean
- Skin: Tanned
- Build: Slim, toned

**Key Features:**

- Long straight brown hair with blonde balayage highlights (side-parted)
- Dark brown almond-shaped eyes
- Arched well-filled eyebrows
- Full voluminous lips with transparent shiny gloss
- Straight symmetrical nose
- Oval face, defined tapered jawline
- Multiple gold hoop earrings (right ear, lined up)

**Style:** Clean girl aesthetic influencer, confident, casual elegant

**Outfit:** White strapless tube top with horizontal ruched texture

**Accessories:** Thin gold chain with cross pendant, multiple bracelets, rings

**Setting:** Indoor area with natural skylight, connected to garden, sitting on sisal rug

**Vibe:** Confident, relaxed, neutral

---

## Universal Realism Standards

### Identity Lock Requirements

✅ Same person from reference image  
✅ Natural asymmetry maintained  
✅ NO face alteration  
✅ NO face swap errors  
✅ NO generic AI face

### Skin Texture (Critical)

- Visible subtle pores (face, abdomen)
- Natural oiliness/hydration glow (forehead, nose tip, cheekbones)
- Realistic micro-variations
- NO overly smooth/filtered

### Image Quality

- Lo-fi iPhone quality, NOT professional
- Visible grain/noise in shadows
- 24mm barrel distortion
- iOS oversharpening artifacts
- Chromatic noise in dark areas
- Authentic social media aesthetic

### Lighting to Avoid

❌ Studio lighting  
❌ Ring lights  
❌ Professional setups  
❌ Warm/orange tones (unless specified)  
❌ Blown-out flash

### Lighting to Use

✅ Natural daylight  
✅ Practical ceiling lights (LED spots)  
✅ Soft diffuse light  
✅ Medium to medium-high contrast  
✅ Realistic shadows and highlights

---

## Pose Types

### Mirror Selfie

- Full body or upper body
- Phone visible in reflection
- Direct eye contact through mirror
- Casual relaxed posture

### Arm-Length Selfie

- Face and upper body
- Phone out of frame
- Slightly high angle looking down
- Natural pose

### Extreme Close-Up

- Face only
- Phone not visible
- Eye-level or very close
- Intense detail on skin texture

---

## Quick Demographic Comparison

| #   | Gender | Age | Skin Tone | Hair                     | Style Vibe           | Setting                |
| --- | ------ | --- | --------- | ------------------------ | -------------------- | ---------------------- |
| 1   | F      | 21+ | Tanned    | Long black straight      | Fitness lounge       | Bedroom mirror         |
| 2   | F      | 21+ | Olive/tan | Long dark brown straight | UGC urban casual     | Bathroom mirror        |
| 3   | M      | 21+ | Various   | Short dark               | Urban raw masculine  | Kitchen close-up       |
| 4   | F      | 21+ | Tanned    | Brown + blonde balayage  | Clean girl aesthetic | Natural light interior |

---

## Key Style Categories

### Fitness/Active

- **Persona 1:** Athletic body, ribbed activewear, confident lounge vibe
- Toned muscles visible, form-fitting clothes, home gym/bedroom aesthetic

### Urban Casual

- **Persona 2:** Street style, jeans + crop top, UGC creator energy
- Tattoos visible, layered accessories, bathroom/casual settings

### Raw Masculine

- **Persona 3:** Shirtless, heavily tattooed, intense close-up
- Minimal styling, direct gaze, modern urban interior

### Clean Girl

- **Persona 4:** Minimalist elegant, natural glam, soft aesthetic
- Balayage hair, dewy skin, subtle jewelry, natural lighting

---

## Technical Prompt Structure (Copy-Paste Base)

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
    "identity_source": "[reference image URL or description]",
    "face_identity": [
      "[specific facial features from Persona]",
      "natural asymmetry maintained",
      "NO face alteration",
      "NO face swap errors",
      "NO generic AI face"
    ]
  },
  "scene": {
    "location": "[from Persona setting]",
    "environment": ["[detail 1]", "[detail 2]"],
    "atmosphere": "[from Persona vibe]"
  },
  "lighting": {
    "type": "[natural/artificial from setting]",
    "main_light": "[description]",
    "contrast": "[level]",
    "avoid": [
      "studio lighting",
      "ring light",
      "professional appearance",
      "warm/orange tones",
      "blown flash"
    ]
  },
  "camera_perspective": {
    "pov": "[mirror selfie/arm-length selfie/close-up]",
    "angle": "[from Persona]",
    "distance": "[framing]",
    "phone_visibility": "[visible or not]"
  },
  "subject": {
    "gender": "[from Persona]",
    "age": "adult (21+)",
    "vibe": "[from Persona style]",
    "skin_texture": "visible pores, natural oiliness/glow, realistic micro-variations",
    "expression": {
      "eyes": "[from Persona]",
      "mouth": "[from Persona]",
      "emotion": "[from Persona vibe]"
    },
    "pose": {
      "position": "[from Persona]",
      "hand": "[hand positions]"
    },
    "outfit": {
      "top": {
        "type": "[from Persona]",
        "fit": "[description]",
        "details": "[specific details]"
      },
      "extra": ["[accessories from Persona]"]
    }
  },
  "image_quality": {
    "focus": "sharp on face/eyes",
    "grain": "visible noise in low light",
    "sharpness": "NOT extremely sharp, more lo-fi",
    "realism": "looks like real iPhone selfie posted online",
    "sensor_artifacts": "light chromatic noise in shadow areas",
    "lens_distortion": "slight 24mm barrel distortion, slightly stretching edges",
    "post_processing": "artificial sharpening (oversharpening) typical of iOS algorithm"
  }
}
```

---

## Common Attributes Across All Personas

### Always Include

- Natural asymmetry in face
- Visible skin pores (subtle)
- Natural oiliness/glow on T-zone
- Realistic human skin micro-variations
- Lo-fi iPhone quality (not professional)
- Visible grain in shadows
- iOS oversharpening artifacts
- 24mm barrel distortion

### Never Include

- Perfect smooth skin
- Studio lighting
- Ring light effects
- Professional retouching
- Generic AI face
- Face swap errors
- Unrealistic perfection

---

## Customization Tips

### To Create Your Own Persona

1. **Choose demographic base** (gender, age range, ethnicity)
2. **Define physical features** (face shape, hair, eyes, skin tone, body type)
3. **Add distinctive marks** (tattoos, piercings, beauty marks, scars)
4. **Select style aesthetic** (fitness, urban, masculine, clean girl, etc.)
5. **Design outfit** (match style aesthetic, include accessories)
6. **Choose setting** (bedroom, bathroom, kitchen, outdoor, etc.)
7. **Pick lighting** (natural daylight, LED spots, mixed artificial)
8. **Decide pose type** (mirror selfie, arm-length, close-up)
9. **Define vibe/emotion** (confident, relaxed, serious, playful)
10. **Apply realism standards** (skin texture, image quality, lo-fi iPhone aesthetic)

### Mixing Elements

You can mix and match elements from different personas:

- Persona 1's fitness vibe + Persona 4's natural lighting
- Persona 2's urban casual + Persona 1's bedroom setting
- Persona 3's raw intensity + Persona 2's tattoo aesthetic
- Persona 4's clean girl style + Persona 1's mirror selfie pose

---

## Source

**Original:** "Prompts Gratuitos #13 Influencer de I.A" (Portuguese)  
**Translated & Structured:** English comprehensive guide  
**Format:** Ultra-realistic iPhone 15 Pro Max selfie prompts  
**See also:** realistic-influencer-personas.md (full detailed prompts)
