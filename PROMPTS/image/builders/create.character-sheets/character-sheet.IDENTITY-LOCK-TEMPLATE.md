# Character Sheet - Identity Lock Fill-in-the-Blank Template

**Tool:** `[IMAGE_GENERATION_TOOL_OR_MODEL]`  
**Purpose:** Create a consistent character reference with locked facial identity

---

## Variable Worksheet

Complete these fields before using the prompt:

- `[SUBJECT_NAME_OR_ID]`
- `[AGE_OR_AGE_RANGE]`
- `[GENDER_PRESENTATION]`
- `[ETHNICITY_OR_ANCESTRY]`
- `[SKIN_TONE]`
- `[SKIN_TEXTURE_AND_MARKS]`
- `[FACE_SHAPE_AND_BONE_STRUCTURE]`
- `[EYE_SHAPE_AND_COLOR]`
- `[EYE_MAKEUP_OR_NO_MAKEUP]`
- `[EYEBROW_SHAPE]`
- `[NOSE_DESCRIPTION]`
- `[LIP_SHAPE_AND_COLOR]`
- `[DISTINCTIVE_FEATURES]`
- `[EARRINGS_OR_ACCESSORIES]`
- `[HAIR_LENGTH]`
- `[HAIR_COLOR]`
- `[HAIR_TEXTURE]`
- `[HAIRSTYLE_AND_VOLUME]`
- `[TOP_OR_UPPER_GARMENT]`
- `[BOTTOM_OR_LOWER_GARMENT]`
- `[FOOTWEAR]`
- `[JEWELRY_AND_ACCESSORIES]`
- `[WARDROBE_STYLE_INTENT]`
- `[LOCATION_TYPE]`
- `[KEY_FURNITURE_OR_PROP]`
- `[INTERIOR_OR_ENVIRONMENT_STYLE]`
- `[TIME_OF_DAY]`
- `[PRIMARY_LIGHT_SOURCE]`
- `[SECONDARY_LIGHT_SOURCE]`
- `[LIGHTING_CONTRAST]`
- `[BODY_ORIENTATION]`
- `[HEAD_DIRECTION]`
- `[ARM_POSITION]`
- `[HAND_OR_PROP_ACTION]`
- `[EXPRESSION_DESCRIPTION]`
- `[EXPRESSION_ENERGY_OR_SUBTEXT]`
- `[COLOR_GRADE]`
- `[CAMERA_FRAMING]`
- `[CAMERA_HEIGHT_AND_ANGLE]`
- `[LENS_OR_DEPTH_CHARACTER]`
- `[NEGATIVE_SPACE_DIRECTION]`
- `[RENDER_STYLE]`
- `[FILM_OR_COLOR_SCIENCE]`
- `[GRAIN_AND_FINISH]`
- `[ASPECT_RATIO]`
- `[RESOLUTION]`

---

## Model Prompt

```text
Create a professional identity-locked character reference image using the uploaded reference as the exact source of truth. Maintain the same facial identity, bone structure, apparent age, skin texture, hair, body proportions, and defining features.

CHARACTER LOCK:
[SUBJECT_NAME_OR_ID], [GENDER_PRESENTATION], [AGE_OR_AGE_RANGE], [ETHNICITY_OR_ANCESTRY]. [SKIN_TONE] skin with [SKIN_TEXTURE_AND_MARKS]. [FACE_SHAPE_AND_BONE_STRUCTURE]. [EYE_SHAPE_AND_COLOR], [EYE_MAKEUP_OR_NO_MAKEUP]. [EYEBROW_SHAPE]. [NOSE_DESCRIPTION]. [LIP_SHAPE_AND_COLOR]. [DISTINCTIVE_FEATURES]. [EARRINGS_OR_ACCESSORIES].

Do not beautify, redesign, merge, reinterpret, or average the face. Preserve all asymmetry and distinctive identity features visible in the uploaded reference.

HAIR:
[HAIR_LENGTH], [HAIR_COLOR], [HAIR_TEXTURE], styled as [HAIRSTYLE_AND_VOLUME]. Preserve the exact hairline, part, density, texture, length, and color throughout. Do not change the hair to a different texture, shade, length, or style.

WARDROBE:
[TOP_OR_UPPER_GARMENT]. [BOTTOM_OR_LOWER_GARMENT]. [FOOTWEAR]. [JEWELRY_AND_ACCESSORIES]. The wardrobe should communicate [WARDROBE_STYLE_INTENT]. Preserve garment construction, fit, fabric, colors, accessories, and footwear exactly.

SCENE:
[LOCATION_TYPE] during [TIME_OF_DAY]. Include [KEY_FURNITURE_OR_PROP] inside a [INTERIOR_OR_ENVIRONMENT_STYLE] environment. Keep the setting coherent, physically believable, uncluttered, and subordinate to the subject.

SUBJECT:
Body [BODY_ORIENTATION], head [HEAD_DIRECTION]. [ARM_POSITION]. [HAND_OR_PROP_ACTION]. The pose feels caught naturally between movements rather than held for a formal portrait. Preserve anatomically correct shoulders, elbows, wrists, hands, fingers, spine, hips, and seated or standing weight distribution.

EXPRESSION:
[EXPRESSION_DESCRIPTION]. The emotional subtext is [EXPRESSION_ENERGY_OR_SUBTEXT]. Keep the expression subtle, anatomically believable, and consistent with natural facial-muscle behavior. Do not substitute a generic smile or neutral face.

LIGHT:
[PRIMARY_LIGHT_SOURCE]. [SECONDARY_LIGHT_SOURCE]. Create [LIGHTING_CONTRAST]. Preserve realistic light direction, shadow logic, catchlights, skin response, hair highlights, and practical-source falloff. No unrequested ring light or generic studio illumination.

GRADE:
[COLOR_GRADE]. Keep skin tone accurate and prevent unwanted orange, magenta, cyan, or green shifts.

CAMERA:
[CAMERA_FRAMING], camera at [CAMERA_HEIGHT_AND_ANGLE], using [LENS_OR_DEPTH_CHARACTER]. Place negative space toward [NEGATIVE_SPACE_DIRECTION]. Keep the subject sharply recognizable while the background separation remains optically believable.

RENDER:
[RENDER_STYLE]. Use [FILM_OR_COLOR_SCIENCE] with [GRAIN_AND_FINISH]. Preserve visible pores, natural skin variation, fine facial hair or peach fuzz, individual hair strands, fabric weave, garment folds, and realistic material response. The result must look like a real frame from a real camera, not a beauty-filter portrait, glossy CGI render, or synthetic fashion mockup.

FORMAT:
[ASPECT_RATIO]. [RESOLUTION].

CRITICAL IDENTITY REQUIREMENTS:
- Exact same face, bone structure, age, ethnicity, skin tone, hairline, and defining marks as the uploaded reference.
- Natural skin texture with no smoothing, airbrushing, or beauty filter.
- Exact hair color, length, texture, and volume.
- Exact wardrobe construction, fit, materials, and accessories.
- Natural facial expression matching the specified subtext.
- Realistic anatomy, hands, fingers, posture, contact, and weight distribution.
- Coherent light direction, camera perspective, background, and color grade.

AVOID:
Identity drift, different person, altered age, altered ethnicity, changed facial proportions, beautification, face averaging, symmetrical redesign, hairstyle change, hair-color shift, wardrobe drift, extra accessories, malformed hands, extra fingers, fused fingers, duplicate limbs, warped furniture, floating props, inconsistent shadows, plastic skin, wax skin, excessive makeup, studio glamour, ring light, oversharpening, fake bokeh, unreadable details, text, logo, watermark.
```

---

## Section-by-Section Fill Template

Use this shorter format when the target tool accepts structured sections better than one long prompt.

## Character Lock

`[SUBJECT_NAME_OR_ID], [GENDER_PRESENTATION], [AGE_OR_AGE_RANGE], [ETHNICITY_OR_ANCESTRY]. [SKIN_TONE]. [SKIN_TEXTURE_AND_MARKS]. [FACE_SHAPE_AND_BONE_STRUCTURE]. [EYE_SHAPE_AND_COLOR]. [EYEBROW_SHAPE]. [NOSE_DESCRIPTION]. [LIP_SHAPE_AND_COLOR]. [DISTINCTIVE_FEATURES].`

## Hair

`[HAIR_LENGTH], [HAIR_COLOR], [HAIR_TEXTURE], [HAIRSTYLE_AND_VOLUME]. Preserve exact hairline, part, density, length, and texture.`

## Wardrobe

`[TOP_OR_UPPER_GARMENT]. [BOTTOM_OR_LOWER_GARMENT]. [FOOTWEAR]. [JEWELRY_AND_ACCESSORIES]. Style intent: [WARDROBE_STYLE_INTENT].`

## Scene

`[LOCATION_TYPE], [TIME_OF_DAY], [INTERIOR_OR_ENVIRONMENT_STYLE], featuring [KEY_FURNITURE_OR_PROP].`

## Subject

`[BODY_ORIENTATION]. [HEAD_DIRECTION]. [ARM_POSITION]. [HAND_OR_PROP_ACTION].`

## Expression

`[EXPRESSION_DESCRIPTION]. Emotional subtext: [EXPRESSION_ENERGY_OR_SUBTEXT].`

## Light

`Primary: [PRIMARY_LIGHT_SOURCE]. Secondary: [SECONDARY_LIGHT_SOURCE]. Contrast: [LIGHTING_CONTRAST].`

## Grade

`[COLOR_GRADE]. Preserve accurate skin tone.`

## Camera

`[CAMERA_FRAMING], [CAMERA_HEIGHT_AND_ANGLE], [LENS_OR_DEPTH_CHARACTER], negative space toward [NEGATIVE_SPACE_DIRECTION].`

## Render

`[RENDER_STYLE], [FILM_OR_COLOR_SCIENCE], [GRAIN_AND_FINISH], visible pores, natural hair strands, readable fabric texture, no retouching.`

## Format

`[ASPECT_RATIO], [RESOLUTION].`

---

## Quality Checklist

- [ ] Uploaded reference is sharp and unobstructed.
- [ ] Face, age, ancestry, and bone structure remain unchanged.
- [ ] Skin texture and distinctive marks remain visible.
- [ ] Hairline, color, length, and texture remain exact.
- [ ] Wardrobe, footwear, and accessories remain exact.
- [ ] Pose and hand action are physically coherent.
- [ ] Expression matches the requested emotional subtext.
- [ ] Light sources and shadows agree.
- [ ] Grade preserves true skin tone.
- [ ] Camera framing and negative space match the plan.
- [ ] Output uses the requested aspect ratio and resolution.
- [ ] No text, logos, watermark, or anatomy artifacts appear.

---

**Derived From:** [Higgsfield Character Sheet - Identity Lock Example](character-sheet.IDENTITY-LOCK-EXAMPLE.md)
