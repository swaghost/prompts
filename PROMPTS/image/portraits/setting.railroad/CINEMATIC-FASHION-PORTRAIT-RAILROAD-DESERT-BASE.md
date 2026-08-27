# CINEMATIC FASHION PORTRAIT: RAILROAD DESERT - BASE PROMPT

**Prompt Type:** Image Generation  
**Style:** Ultra-Photorealistic Cinematic Fashion  
**Setting:** Desert Railroad Tracks  
**Platforms:** Midjourney v6+, DALL-E 3, Stable Diffusion XL, Flux Pro  
**Aspect Ratio:** 2:3 or 4:5 (vertical portrait)  
**Estimated Word Count:** 547 words

---

## THE COMPLETE PROMPT

```
A cinematic film still, ultra-photorealistic. Camera: extreme ground-level low angle. The main subject is a person with a calm, relaxed, friendly expression and subtle natural smile, maintaining direct eye contact with the camera. Natural human realism—no filters, no retouching, no artificial smoothing.

Outfit: elegant matte-black high-fashion evening gown with a sculptural couture silhouette. Strapless sweetheart neckline with a tightly structured corset-style bodice defining the torso. Dramatic oversized off-the-shoulder sculptural sleeves forming bold architectural volumes around the upper arms. Long weighted skirt with a high thigh slit revealing the leg naturally while seated. Long matte-black opera gloves extending above the elbows. A classic multi-row pearl choker necklace fitted close to the neck. A wide-brim black hat with a flat crown and rigid structure, worn slightly tilted for logos, no embellishments.

Scene: the subject is sitting on a simple, worn wooden chair placed directly on railroad tracks, centered between the rails, in the middle of a vast desert. Posture relaxed and poised. In one gloved hand the subject holds a lipstick, gently pressing it to the lips mid-application; in the other a small handheld mirror, actively applying lipstick while maintaining eye contact with the camera. The chair casts a sharp shadow across dusty wooden sleepers and steel rails.

Behind the subject, perfectly aligned with the tracks, a freight train is far in the distance, small in scale, with faint headlights diffused by heat haze, emphasizing delayed danger rather than immediacy.

Environment: endless desert landscape with pale sand, scattered stones, dry shrubs, cracked earth, distant mesas and low mountains on the horizon. Dust and heat shimmer dance in the air, dry wind carrying fine dust.

Camera: cinematic film-still aesthetic, extreme ground-level low angle—camera placed directly on the ground between the rails, almost touching gravel and steel, looking steeply upward. 35mm lens, perspective exaggerated by proximity. The ground-level vantage point dominates the foreground; converging rails powerfully upward into the seated figure, body, dress, gloves, pearls, and hat rise above the horizon line, giving monumental scale and dominance. Camera clearly below knee level, well under eye height, sky occupying a significant portion of the upper frame. Strong foreground-middleground-background layering with depth of field shallow but realistic: key details tack-sharp, foreground rails slightly soft due to proximity, distant train very soft and atmospheric.

Lighting: late-afternoon desert sun, hard but motivated, softened by airborne dust, warm directional side light creating crisp micro-highlights and deep shadow on subject, gloves, dress, pearls, rails—warm vs. cool highlights contrasted with cooler shadows. Color science: restrained cinematic teal-and-amber balance, natural desert tones, deep blacks in the dress preserved with texture. Atmosphere: heat haze, suspended dust particles, very subtle natural film grain, no bloom or glow.

Mood: high-fashion cinematic power and tension—dominance, elegance, calm defiance, danger held at a distance. Ultra-detailed, photorealistic, true-to-life human proportions, documentary realism, cinematic composition.
```

---

## NEGATIVE PROMPT

```
CGI, 3D render, illustration, anime, stylized, beauty filter, airbrushed or flawless skin, plastic or waxy face, AI skin smoothing, glam retouching, crushed blacks, over-sharpening halos, excessive HDR, fake bokeh, bloom, studio lighting, fog machine, eye-level camera, chest-level camera, shallow fashion-angle clichés, distorted anatomy, flat posture, missing fingers, warped hands, floating chair, incorrect rails, warped chair, floating chair, incorrect rails, oversized or too-close train, duplicated objects, logos, text, watermark, oversaturated colors, low resolution, compression artifacts.
```

---

## PLATFORM-SPECIFIC PARAMETERS

### Midjourney v6+ (Recommended)

```
[Your full prompt above]

--ar 2:3 --style raw --s 250 --v 6.1 --no beauty filter, CGI, studio lighting, eye-level camera
```

**Alternative Aspect Ratios:**

- `--ar 4:5` for Instagram portrait format
- `--ar 9:16` for full mobile screen

### DALL-E 3

- **Resolution:** 1024x1792 (portrait)
- **Method:** Paste prompt directly, or use ChatGPT to refine
- **Note:** Include negative prompt elements in main prompt as "Make sure to avoid: beauty filters, AI skin smoothing..."

### Stable Diffusion XL

**Settings:**

- **Checkpoint:** RealVisXL 4.0 or Juggernaut XL
- **Steps:** 30-50
- **Sampler:** DPM++ 2M Karras or Euler a
- **CFG Scale:** 7-9
- **Resolution:** 832x1216 or 896x1152
- **Negative Prompt:** Use full negative prompt in dedicated field

### Flux Pro

**Settings:**

- **Guidance:** 3-4 (Flux uses lower guidance)
- **Steps:** 20-30
- **Aspect Ratio:** 2:3 or custom
- **Note:** Flux needs less aggressive negative prompting

---

## PROMPT STATISTICS

- **Total Words:** 547
- **Character Count:** 3,584
- **Recommended Platform:** Midjourney v6+, Flux Pro
- **Estimated Generation Time:** 60-120 seconds
- **Quality Level:** Professional editorial/commercial

---

## WHAT THIS PROMPT CREATES

**Visual Output:**

- Ultra-photorealistic cinematic fashion portrait
- Dramatic ground-level perspective creating monumental presence
- Subject in elegant black couture seated on railroad tracks
- Vast desert landscape with distant approaching train
- Late afternoon golden light with cinematic color grading
- High-fashion editorial quality suitable for professional use

**Key Elements:**

- **Subject:** Person in black evening gown applying lipstick while maintaining eye contact
- **Setting:** Railroad tracks in desert, worn wooden chair, distant train
- **Camera:** Extreme ground-level low angle (worm's eye view)
- **Lighting:** Late afternoon sun with warm/cool teal-amber balance
- **Mood:** Power, elegance, calm defiance, controlled danger

**Use Cases:**

- Fashion editorial spreads
- Social media carousel content
- Advertising campaigns
- Portfolio pieces
- Mood boards
- Concept development

---

## VARIATIONS & CUSTOMIZATION

For detailed variations and customization options (different outfits, scenes, lighting, moods, camera angles), see the comprehensive guide:

**[cinematic-fashion-portrait-railroad.md](cinematic-fashion-portrait-railroad.md)**

The guide includes:

- 6 outfit style variations
- 7 scene/setting variations
- 7 environment variations (different deserts)
- 6 camera technique variations
- 7 lighting setup variations
- 7 mood/aesthetic variations
- Platform-specific workflows
- Troubleshooting common issues
- Quality optimization techniques

---

## QUICK TIPS

1. **Consistency for Carousels:** Use same `--seed` value (Midjourney) for multiple related images
2. **Emphasis:** If camera angle wrong, add `::2` weight: "extreme ground-level low angle::2"
3. **Hands Issue:** If hand anatomy incorrect, regenerate or simplify hand positioning
4. **Scale:** Ensure distant train stays small by emphasizing "far in distance, small scale"
5. **Skin Texture:** If too smooth, strengthen negative: "absolutely no beauty filters or skin smoothing"

---

## LICENSE & USAGE

- Check your AI platform's terms of service for commercial usage rights
- Consider disclosure requirements for AI-generated content
- Watermark/protect your generated work as needed
- No copyrighted elements included in this prompt

---

**Related Files:**

- **Guide:** [cinematic-fashion-portrait-railroad.md](cinematic-fashion-portrait-railroad.md) - Full 28,000+ word comprehensive guide
- **Variations:** See guide for component libraries to create custom variations
