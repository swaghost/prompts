# Hyperreal AI Characters - Arcads Influencer Fashion Workflow

## Purpose

A production workflow for creating a consistent hyperreal influencer-fashion character and animating her through an unposed, phone-shot editorial sequence. The workflow combines a GPT Image 2 character sheet, a locked opening still, multiple visual references, and Seedance 2.5 image-to-video generation.

## Recommended Tools

- **Character and still generation:** GPT Image 2
- **Video generation:** Seedance 2.5 through Arcads or another compatible platform
- **Output:** Generate at 1080p, then upscale to 2K when needed
- **Image format:** 3:4 for the still portrait; adapt the video framing to the chosen platform

## Production Workflow

1. Generate a clean character reference sheet from the subject references.
2. Create the opening influencer-fashion still with the character and look locked.
3. Build a reference map that separates identity, wardrobe, prop, location, and aesthetic references.
4. Upload the opening still as the exact first frame to Seedance 2.5.
5. Add the character sheet and any supporting references without allowing them to override the opening frame.
6. Generate the single continuous sequence.
7. Inspect face, hair, jewelry, clothing, hand anatomy, lip-sync, autofocus, exposure, and final-frame continuity.
8. Combine selected generations in an editor only when an individual take needs replacement.

## Character Sheet Prompt

```text
A 2x2 grid character reference sheet of the woman from the reference images. Preserve her exact facial identity from the provided references: sun-kissed tanned skin, long straight light-brown to blonde hair worn down, thick soft brows, brown eyes, full glossy lips, and a small beauty mark on her right cheek. Four separate portrait panels, evenly divided by thin clean white gutters, all shot at the same camera height, same distance, same lens, and same lighting so the head is identical in scale and vertical position across every panel.

Top-left panel: straight-on frontal view, head and shoulders, facing the lens directly, neutral relaxed expression, lips softly closed, eyes to camera.

Top-right panel: her right side, full 90-degree profile facing frame-left, jawline, nose bridge, and ear cleanly readable.

Bottom-left panel: her left side, full 90-degree profile facing frame-right.

Bottom-right panel: back of the head with shoulders square to camera, showing the fall and parting of her hair down her back, no face visible.

Keep the exact same center-parted straight hairstyle worn down over the shoulders, a few natural flyaway strands, and slightly sun-lightened ends in all four views. Same plain white strapless top and layered thin gold necklaces with small cross and coin pendants in every panel. Bare natural glowing makeup exactly as in the references. Clean seamless pure white studio backdrop, soft even studio lighting from a large frontal softbox with fill on both sides, no harsh shadows, only a faint soft shadow under the jaw, neutral color temperature, flattering but honest.

Shot on a full-frame camera with an 85mm lens at f/5.6, everything sharp from front to back. Photographic realism: visible skin texture and pores, natural sheen on cheekbones and nose, fine facial hair catching light, subtle asymmetry, individual hair strands. No skin smoothing, no plastic retouching, no beauty filter, no text, no labels, no watermarks. Ultra-detailed, high resolution, consistent identity across all four panels.
```

## Opening Still Prompt

```text
Horizontal 3:2 handheld selfie, phone front camera around 26mm, held slightly above eye level and angled down, one bare arm sweeping out of the lower-right corner toward the lens. Use the subject identity from the provided character references: preserve her exact bone structure, feathered brows, hooded hazel eyes, full glossy lips, sun-streaked centre-parted long hair, natural pores, and recognizable face.

She stands on a wrought-iron balcony above a cliffside bay, filling the right half of the frame. Her other hand rests on the top of a green-painted iron scrollwork rail at frame-left, with gold rings on two fingers and a slim bangle at the wrist. She wears a white strapless bandeau top and three layered fine gold chains with a small oval medallion and a slim cross pendant beside a tiny coin charm. Damp windblown strands cross her cheek and catch at her lips. She gazes down past the camera with a soft pout, lips slightly parted, red-brown gloss, flushed sun-warmed cheeks and nose.

Behind her: a broad banana leaf and red-orange bougainvillea over a whitewashed plaster balcony wall, pastel pink, cream and terracotta houses stacked down the cliff, pines on a rocky headland, pale hazy water far below. Colour, grain and mood from sun-bleached coastal film photos: bright milky haze, blown highlights on the water, lifted blacks, faded warm color, fine grain, low contrast, overhead midday light.

Real skin with visible pores, sun sheen across forehead, cheekbones and nose bridge, faint freckles, natural asymmetry, no smoothing, no plastic retouch. Candid amateur holiday capture, not a polished studio portrait.
```

## Reference Map Rules

- **Opening still:** Visual anchor for face, hair, jewelry, wardrobe, environment, light, grade, and framing. It is the exact first frame.
- **Character sheet:** Identity and angle consistency only. Ignore its white studio background and studio lighting.
- **Wardrobe reference:** Clothing only. Ignore the reference model and location.
- **Location reference:** Architecture and geography only. Do not transfer its color grade or camera look unless explicitly requested.
- **Prop reference:** Prop shape, material, and hand interaction only.
- **Video reference:** Continuity of character, style, voices, and movement only; do not force its location or shot into the new sequence.

## Realism Rules

- Keep the same face, hair, jewelry, and outfit in every frame.
- Use real phone behavior: handheld micro-shake, small arm corrections, autofocus breathing, exposure adaptation, and imperfect framing.
- Preserve natural skin: visible pores, sheen, fine facial hairs, faint freckles, and no beauty smoothing.
- Keep wind physically coherent: hair ends, leaves, flowers, and loose jewelry respond together.
- Use exact lip-sync and natural visemes for spoken lines.
- Avoid cinematic gimbal smoothness, artificial HDR, crushed blacks, or a polished commercial finish when the target is candid phone footage.

## Common Failure Controls

- **Identity drift:** Attach the character sheet and opening still; state that the opening still is the identity and visual anchor.
- **Over-stabilized footage:** Request arm-held phone sway, breathing corrections, and natural autofocus behavior.
- **Plastic skin:** Name pores, sheen, freckles, fine hairs, and asymmetry; explicitly reject smoothing.
- **Reference contamination:** Assign every reference a role and state what to ignore.
- **Frozen environment:** Add subtle wind, waves, leaves, distant birds, and small background life.
- **Over-directed performance:** Use casual gestures, natural pauses, imperfect timing, and unposed language.

## Source

Adapted from the Hyperreal AI Characters - Arcads Notion workflow. The source emphasizes Seedance 2.5, Arcads, GPT Image 2, multi-reference continuity, and natural phone-camera realism.
