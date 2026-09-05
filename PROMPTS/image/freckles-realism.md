# Freckles Realism for Human Image Prompts

## Purpose

Use this guide when freckles are a defining identity feature or when a prompt requests natural, visible, or dense freckles. Freckles should read as individual pigmentation within real skin, not as a repeated texture overlay or decorative pattern.

## Core Rule

Describe freckles by density, distribution, scale, color, and relationship to the subject's skin tone. Preserve natural asymmetry and variation. Combine freckles with pores, vellus hair, redness, and uneven pigmentation so they belong to a living face.

## Specificity Beats Resolution

An `8K` or high-resolution request does not create realistic freckles by itself. Name the visible imperfections and their behavior instead of relying on generic phrases such as "beautiful," "ultra realistic," or "8K." Specify freckle density, placement, variation, pores, fine hairs, tonal shifts, and natural light response.

## Freckle Construction

- Use varied sizes, opacity, spacing, and edge softness; do not repeat identical dots.
- Follow natural sun-exposed zones: nose bridge, upper cheeks, temples, forehead, shoulders, and arms where appropriate.
- Allow areas of clear skin between clusters and make the distribution asymmetrical.
- Vary color from pale honey and warm tan to muted cinnamon or soft brown according to the subject's complexion.
- Let freckles sit within the skin surface with believable light response, not above it like paint, makeup, or a filter.
- Keep freckles visible at the requested camera distance without enlarging them beyond anatomical scale.
- For dense freckles, retain individual marks while preserving the underlying pores, skin folds, and natural tonal variation.

## Identity and Skin Realism

- If a reference is supplied, preserve the exact freckle map, density, clusters, moles, scars, eye color, facial proportions, and natural asymmetries.
- Do not add freckles to change ethnicity, age, or identity.
- Keep natural pores, fine facial hairs, subtle redness, under-eye texture, and realistic oil or moisture response.
- Match freckle visibility to lighting: stronger in direct daylight, softer in shade, and naturally varied under mixed light.
- Do not erase freckles with beauty retouching, foundation, airbrushing, or skin smoothing.

## Prompt Formula

```text
[subject] with [light/subtle/dense] natural freckles distributed asymmetrically across [specific zones], varied in size, opacity, and warm [color] tones embedded in realistic skin, visible pores, fine vellus hair, natural redness and tonal variation, unretouched photographic texture, no makeup mask, no repeated dot pattern, no airbrushing
```

## Close-Up and Macro Formula

```text
extreme close-up of authentic freckled skin, individual freckles with varied size, spacing, opacity, and soft natural edges, freckles integrated into visible pores and fine skin ridges across the nose and upper cheeks, tiny vellus hairs, subtle redness, realistic moisture and light response, no duplicated marks, no painted dots, no smoothing
```

## Negative Prompt

```text
painted freckles, makeup freckles, repeated dot pattern, identical freckles, perfectly symmetrical freckles, sticker-like marks, floating pigment, artificial overlay, airbrushed skin, plastic skin, poreless skin, beauty filter, excessive smoothing, erased freckles, distorted face, identity drift
```

## Builder Integration

When freckles are specified or visible in a reference, builders must:

1. Treat the freckle pattern as part of identity, not optional styling.
2. State density and anatomical distribution rather than using only "freckled skin."
3. Scale freckle detail to the framing: zones for full-body, clusters for portraits, individual marks for macro shots.
4. Preserve pores, vellus hair, redness, and tonal variation around the freckles.
5. Add the negative prompt constraints unless the user explicitly requests makeup, paint, prosthetics, or a graphic treatment.

## Quick Quality Check

Before generation, confirm that the prompt describes the freckles themselves and not only the output quality. A strong prompt includes:

- Where the freckles appear
- How dense and asymmetrical they are
- Variation in size, opacity, color, and spacing
- Pores, vellus hair, redness, and surrounding texture
- How light changes their visibility
- Anti-smoothing constraints
