# Photographic Relighting Prompts

**Platform:** GPT Image 2, Picsart Flow  
**Workflow:** Image-to-image relighting  
**Purpose:** Transform existing portraits with authentic photographic lighting techniques while preserving subject identity and composition

## What Are Relighting Prompts?

Relighting prompts are specialized image-to-image instructions that change only the lighting in an existing photograph while preserving everything else — subject identity, facial features, expression, pose, hairstyle, clothing, composition, background, and camera perspective.

Unlike generating new images from scratch, relighting takes an uploaded portrait and applies professional studio lighting techniques as if the original photo had been captured under different lighting conditions.

## When to Use Relighting

- **Transform amateur photos** — Turn smartphone snapshots into studio-quality portraits
- **Explore lighting variations** — Test different moods on the same subject without reshooting
- **Match reference lighting** — Apply specific cinematic or editorial lighting to existing images
- **Consistency across sets** — Unify lighting across portraits shot under different conditions
- **Learn lighting techniques** — Visualize how professional lighting setups affect facial structure

## How Image-to-Image Relighting Works

1. Upload your portrait to GPT Image 2 or Picsart Flow
2. Paste the appropriate relighting prompt (choose from 8 lighting types)
3. The model preserves identity, pose, and composition while recalculating light and shadow
4. Result: Same subject, same angle, new lighting as if captured with professional setup

## Core Relighting Principles

**Every prompt in this collection follows these rules:**

- **Preserve identity** — Face, body, expression, pose stay identical
- **Preserve composition** — Camera angle, framing, background unchanged
- **Preserve wardrobe** — Clothing, jewelry, accessories untouched
- **Realistic physics** — Light behaves according to photography, not fantasy effects
- **No beauty retouching** — Skin texture, pores, natural detail maintained
- **No visible sources** — No lamps, light beams, or equipment in frame

## Collection Contents

This collection contains 8 photographic relighting techniques:

1. **[Split Lighting](01-split-lighting.md)** — Dramatic side light, one half illuminated, one half shadow
2. **[Underlighting](02-underlighting.md)** — Light from below, upward shadows, cinematic/horror mood
3. **[Rembrandt Lighting](03-rembrandt-lighting.md)** — Classic portrait, inverted triangle under shadow-side eye
4. **[Rim Lighting](04-rim-lighting.md)** — Backlight tracing edges, separating subject from background
5. **[Silhouette Lighting](05-silhouette-lighting.md)** — Backlit silhouette, subject dark against bright background
6. **[Hard Lighting](06-hard-lighting.md)** — Small focused source, crisp shadows, strong contrast
7. **[Soft Lighting](07-soft-lighting.md)** — Large diffused source, gentle transitions, flattering
8. **[High-Key Lighting](08-high-key-lighting.md)** — Bright even illumination, low contrast, clean whites

## Technical Specifications

- **Input:** Existing portrait photograph (headshot, half-body, or full-body)
- **Output:** Same composition with professional lighting applied
- **Preservation:** Identity, pose, expression, wardrobe, background, framing all locked
- **Change:** Only light direction, quality, intensity, shadow placement
- **Style:** Photographic realism, no fantasy or graphic effects

## Usage Tips

- **Start with clean source images** — Well-exposed originals produce better results
- **Front-facing works best** — Portraits looking toward camera easier than extreme profiles
- **Avoid cluttered backgrounds** — Simple backgrounds let lighting shine
- **One subject at a time** — Multi-person portraits may have inconsistent relighting
- **Specify "no beauty retouching"** — All prompts preserve natural skin texture

## Lighting Quick Reference

| Lighting Type | Mood                   | Use Case                                   | Shadow Character     |
| ------------- | ---------------------- | ------------------------------------------ | -------------------- |
| Split         | Dramatic, mysterious   | Editorial, character portraits             | Hard vertical divide |
| Underlighting | Unsettling, theatrical | Horror, villain shots, dramatic effect     | Upward shadows       |
| Rembrandt     | Classic, dimensional   | Traditional portraits, corporate headshots | Triangle under eye   |
| Rim           | Cinematic, separated   | Music videos, fashion, depth               | Edge highlights      |
| Silhouette    | Bold, graphic          | Storytelling, mystery, minimal detail      | Entire subject dark  |
| Hard          | Sculptural, defined    | Fashion editorial, masculine portraits     | Crisp edges          |
| Soft          | Flattering, gentle     | Beauty, lifestyle, approachable portraits  | Gradual transitions  |
| High-Key      | Bright, optimistic     | Commercial, beauty, clean aesthetic        | Minimal shadows      |

## Integration with Video Projects

While these prompts are designed for still images, relit portraits can serve as reference boards for video:

```
Generate character headshot with your existing tools, then relight using prompts from this collection.
Upload relit portrait to Topview Canvas as @char_hero_lit.
Reference in video prompt: "Lighting on character's face matches @char_hero_lit throughout — Rembrandt lighting with triangle under left eye, warm key from right, cinematic contrast."
```

## Common Mistakes to Avoid

❌ **Adding new instructions** — Prompts are complete; adding "make them smile" or "change background" breaks preservation  
❌ **Applying to non-portraits** — Relighting works on faces/people, not landscapes or architecture  
❌ **Expecting identical lighting on different faces** — Same prompt on two portraits = consistent technique, not identical shadows  
❌ **Using on already-lit studio portraits** — Works best on naturally lit or flat-lit originals; studio portraits may conflict  
❌ **Combining multiple lighting types** — Each prompt is one technique; don't merge split + rim in same instruction

## Advanced: Lighting Chains

For experimental results, apply relighting techniques sequentially:

1. Upload original portrait
2. Apply **Soft Lighting** → save result
3. Upload softly-lit result
4. Apply **Rim Lighting** → save result
5. Result: Soft frontal light + rim separation (composite technique)

**Note:** Each generation compounds small changes; limit to 2-3 steps maximum.

---

**Collection:** 8 photographic relighting prompts  
**Workflow:** Image-to-image transformation  
**Principle:** Preserve everything except lighting
