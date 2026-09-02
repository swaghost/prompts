# AI Influencer Realism Lighting Guide

## Purpose

Create a consistent AI character who remains recognizable across multiple photos without looking synthetic. The key is to lock identity once and vary the lighting situation, not to ask for generic "beautiful, ultra-realistic, 8K" images.

## Workflow

1. Generate one full-body reference image of the character standing against a plain background.
2. Use that full-body image as the identity reference for every scene.
3. Use image-to-image editing with the reference image, not text-to-image alone.
4. Use a 4:5 vertical format.
5. Keep the identity block unchanged across all prompts.
6. Change only the scene, clothing, action, and lighting block.

## Shared Identity Block

Paste this at the beginning of every prompt and replace the character-specific details once:

```text
USE THE UPLOADED REFERENCE IMAGE AS THE ONLY SOURCE OF IDENTITY. DO NOT CREATE A NEW PERSON. ABSOLUTE IDENTITY LOCK.

Preserve 100% of the person's face shape, skull structure, forehead, hairline, hair color, eyebrows, eyes, eyelids, eye spacing, nose, nostrils, lips, mouth width, teeth, jawline, chin, cheekbones, ears, skin tone, skin texture, freckles, moles, facial asymmetry, body proportions, build, and age. The generated person MUST be instantly recognizable as the exact same individual from the uploaded reference image.

DO NOT beautify the face, stylize the face, generate another person, modify facial proportions, slim the face or body, enlarge the eyes, change the nose or lips, smooth the skin, remove freckles or moles, change hair color, alter skin tone, change age, or change ethnicity. Identity preservation has the highest priority over composition, clothing, or lighting.
```

## Shared Realism Block

```text
SKIN: authentic real skin with visible open pores across the nose and cheeks, uneven texture, freckles clearly present, natural sweat and shine on the forehead, nose, and collarbones, fine flyaway hairs, faint tan lines, small blemishes left in place, and visible fine hair on the forearms. NOT airbrushed, NOT smoothed, NOT plastic, NOT retouched, NOT beautified.

FOCUS: everything is tack sharp from the subject to the far background. Use a small aperture. NO bokeh, NO defocused background, NO shallow depth of field.

Photorealistic, editorial sportswear campaign, raw realistic style, vertical 4:5. No text, logos, or watermarks anywhere in the image.
```

## The Six Lighting Situations

1. Turquoise lagoon: upward bounce from shallow water under high midday sun.
2. Muay Thai ring: hard, irregular dappled palm shadow.
3. Paddleboard: backlight rescued by sand and water bounce.
4. Wooden jungle stairs: a hard hat shadow cuts across the face.
5. Infinity pool: flat, directionless overcast light over the sea.
6. Waterfall: glowing backlit water curtain against dark wet rock.

## Practical Rules

- Change the location, but keep the lighting paragraph intact when testing the same look.
- Do not default to "golden hour"; specify the actual light behavior.
- Do not accept fake bokeh; require a sharp subject and readable background.
- Name visible imperfections specifically instead of saying only "natural imperfections."
- If a result is wrong, change one sentence at a time because long prompts are sensitive to broad edits.
