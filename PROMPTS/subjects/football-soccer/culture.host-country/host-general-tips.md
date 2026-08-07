# Host Country Culture Graphics - General Tips & Best Practices

## Overview

Universal principles, AI tool parameters, and best practices for creating authentic host country culture photography and tournament atmosphere imagery. Apply these tips across all host country graphic types for consistent, culturally-sensitive, and visually stunning results.

**Part of:** [Host Country Culture Collection](PROMPT.Host-Country-Culture.txt)

---

## Essential Prompt Phrases

### Core Photography Terms

Use these foundational phrases in prompts:

**Photography Styles:**

- "photorealistic"
- "documentary photography"
- "sports documentary"
- "architectural photography"
- "street photography"
- "photojournalism"
- "authentic"
- "candid"

**Lighting Descriptions:**

- "golden hour light"
- "sunset glow"
- "blue hour twilight"
- "warm afternoon light"
- "atmospheric lighting"
- "natural light"
- "soft overcast"

**Atmosphere & Mood:**

- "tournament atmosphere"
- "cultural fusion"
- "festival energy"
- "authentic atmosphere"
- "celebration mood"
- "atmospheric conditions"

**Quality Descriptors:**

- "professional photography"
- "8k resolution"
- "high detail"
- "cinematic composition"
- "broadcast quality"

---

## AI Tool Parameters

### Midjourney Settings for Host Country Culture

**Aspect Ratios:**

```
--ar 16:9       Wide landscapes, stadiums, urban scenes, training grounds (most versatile)
--ar 9:16       Tall buildings, vertical murals, mobile Stories, portrait orientation
--ar 1:1        Square social media posts, balanced compositions
--ar 21:9       Ultra-wide cinematic landscapes, epic establishing shots
--ar 4:3        Classic documentary photography, traditional photojournalism feel
```

**Stylize Values:**

```
--stylize 250-400   Photorealistic documentary, authentic journalism style
--stylize 400-600   Balanced realism with artistic atmosphere
--stylize 600-800   More atmospheric and artistic interpretation
--stylize 100-250   Minimal interpretation, maximum realism (for data/info graphics)
```

**Quality:**

```
--quality 2     High quality for architectural detail, crowd faces, atmospheric effects (recommended)
--quality 1     Standard quality (acceptable for drafts or budget-conscious projects)
```

**Style Mode:**

```
--style raw     Photorealistic, documentary style (recommended for authentic cultural imagery)
(default)       Midjourney's standard aesthetic (more artistic interpretation)
```

**Recommended Defaults:**

- **Stadium/Architecture:** `--ar 16:9 --stylize 350 --quality 2 --style raw`
- **Urban Atmosphere:** `--ar 16:9 --stylize 450 --quality 2 --style raw`
- **Street Scenes:** `--ar 16:9 --stylize 400 --quality 2 --style raw`
- **Training Grounds:** `--ar 16:9 --stylize 350 --quality 2 --style raw`
- **Tall Murals:** `--ar 9:16 --stylize 500 --quality 2 --style raw`

---

### DALL-E Best Practices

**Prompt Structure:**

1. **Start with photography type:** "Architectural photography," "Street photography," "Documentary photography"
2. **Describe subject:** Stadium, street scene, training ground, celebration
3. **Add environment:** Local landmarks, weather conditions, cultural context
4. **Specify lighting:** "Golden hour," "blue hour," "afternoon light"
5. **Request quality:** "Photorealistic," "professional photography," "8k detail"

**DALL-E Strengths:**

- Specific architectural details
- Photorealistic people and faces
- Cultural authenticity
- Precise environmental conditions
- Weather and atmospheric effects

**DALL-E Tips:**

- Be explicit about weather: "light snowfall," "heat shimmer visible"
- Specify exact locations: "Times Square NYC," "Copacabana Beach Rio"
- Request "authentic" and "candid" for documentary feel
- Mention "photorealistic" for photography quality
- Specify crowd diversity: "diverse international supporters"

---

### Stable Diffusion Recommendations

**Model Selection:**

- **SDXL:** Best for photorealistic environments, architecture, landscapes
- **SD 1.5 with LoRA:** Good for consistent documentary photography style
- **Photorealism LoRA:** Essential for authentic cultural imagery
- **Architectural LoRA:** Helpful for stadium and venue photography

**Prompt Keywords:**

- "professional photography," "8k," "highly detailed"
- "photorealistic," "documentary photography," "photojournalism"
- "golden hour light," "natural lighting," "atmospheric"
- "wide angle lens," "architectural photography," "cinematic composition"

**Negative Prompts (Critical):**

```
no cartoon, no illustration, no painting, no CGI, no rendered, no 3D, no fake, no artificial, no distortion, no warping, photorealistic, natural, authentic, candid
```

**CFG Scale:**

- 7-9: Natural photorealistic results (recommended)
- 10-12: More controlled, less variation
- 13+: Risk of over-processing, artifacts

**Sampling Steps:**

- 30-40: Good quality, efficient
- 50-80: Higher quality, diminishing returns beyond 50

---

## Cultural Authenticity Guidelines

### Research Regional Characteristics

**Visual Research:**

- Study real photography from host country
- Observe authentic color palettes
- Note architectural styles
- Understand regional climate and lighting

**Cultural Sensitivity:**

- Respect local traditions and customs
- Avoid stereotypes and clichés
- Represent diversity authentically
- Consult cultural advisors if possible

**Architectural Accuracy:**

- Research building styles
- Understand urban planning
- Note regional materials and colors
- Capture authentic street life

---

### Color Palettes by Region

**North America:**

**United States:**

```
Urban: Steel, glass, modern, bright signage, diverse architecture
Desert Southwest: Terracotta, desert tones, big sky, wide open spaces
California: Golden light, palm trees, ocean blues, laid-back modern
```

**Mexico:**

```
Vibrant: Terracotta, bright blue, yellow, pink, green, warm colonial colors
Urban: Modern mixed with colonial, colorful painted walls, cultural murals
```

**Canada:**

```
Modern glass architecture, natural landscapes prominent, clean urban design
Winter: White snow, grey skies, cold atmosphere, evergreen forests
```

**Latin America:**

**Brazil:**

```
Tropical: Vibrant carnival colors, beach culture, favela colorful houses
Urban: Mix of modern and informal, tropical greens, ocean blues
```

**Argentina/Chile:**

```
European influence, tango culture, urban sophistication, Andes backdrop
```

**Europe:**

**Western Europe:**

```
Historic architecture, cobblestone streets, cafe culture, old meets modern
```

**Mediterranean:**

```
Whitewashed walls, blue accents, terracotta roofs, coastal light, ancient stones
```

**Eastern Europe:**

```
Soviet-era concrete, colorful street art contrast, post-industrial urban renewal
```

**Asia:**

**East Asia:**

```
Dense urban, neon signs, modern technology, traditional temples mixed in
```

**Southeast Asia:**

```
Tropical, humid atmosphere, market culture, colorful textiles, dense urban
```

**Middle East:**

```
Desert tones, futuristic modern architecture, traditional meets cutting-edge
```

**Africa:**

**North Africa:**

```
Desert, Mediterranean influence, Islamic architecture, warm earth tones
```

**Sub-Saharan Africa:**

```
Earth tones with vibrant textile colors, grassroots community energy
```

---

## Photography Techniques

### Lighting Mastery

**Golden Hour (Best for Most):**

**Timing:**

- 1 hour before sunset
- 1 hour after sunrise

**Characteristics:**

- Warm, glowing light (2500-3500K)
- Long soft shadows
- Flattering for people and architecture
- Romantic and nostalgic mood

**Best For:**

- Stadium exteriors
- Urban celebrations
- Beach scenes
- Training grounds
- Street photography

---

**Blue Hour (Dramatic):**

**Timing:**

- 20-40 minutes after sunset
- 20-40 minutes before sunrise

**Characteristics:**

- Deep blue sky (8000-12000K)
- City lights visible and glowing
- Balanced ambient and artificial light
- Magical twilight atmosphere

**Best For:**

- Urban cityscapes
- Stadiums with lights on
- City celebrations at dusk
- Dramatic establishing shots

---

**Overcast/Soft (Documentary):**

**Characteristics:**

- Even, diffused lighting
- No harsh shadows
- Consistent color temperature
- Professional documentation standard

**Best For:**

- Documentary work
- Training ground coverage
- Street scenes requiring consistency
- When weather dictates

---

**Harsh Midday (Selective):**

**Use When:**

- Documenting extreme heat
- Desert training conditions
- Bright energetic atmosphere needed
- Weather/climate is the story

**Avoid When:**

- Flattering portraits needed
- Architectural detail important
- Shadows would be distracting

---

### Composition Principles

**Rule of Thirds:**

- Place key elements on thirds intersections
- Horizon on upper or lower third
- Creates balanced, professional composition

**Foreground-Midground-Background:**

- **Foreground:** Flags, people, approach elements (close)
- **Midground:** Main subject - stadium, celebration, game (medium)
- **Background:** Landmarks, skyline, mountains, ocean (distant)
- Creates depth and visual layers

**Leading Lines:**

- Roads, boulevards, streets lead to subject
- Architectural lines guide eye
- Creates dynamic movement
- Emphasizes journey or approach

**Framing:**

- Use archways, doorways, windows
- Natural frames draw eye to subject
- Creates depth and context
- Professional storytelling technique

**Symmetry & Balance:**

- Centered subjects with balanced sides
- Formal, monumental feeling
- Works well for iconic venues
- Clean, organized aesthetic

**Recommendation:** Use foreground-midground-background for depth; rule of thirds for balance

---

### Camera Angles & Perspectives

**Wide Angle (16-35mm equivalent):**

- Captures full scene and context
- Ideal for stadiums, urban scenes
- Creates drama and scope
- Shows environment and subject together

**Standard (35-70mm):**

- Natural human perspective
- Balanced environmental context
- Documentary standard
- Versatile and relatable

**Telephoto (70-200mm+):**

- Compresses background
- Isolates subjects
- Good for crowd close-ups
- Flattens perspective

**Aerial/Drone:**

- Bird's-eye unique perspective
- Shows scale and layout
- Cinematic establishing shots
- Infrastructure visible

**Low Angle:**

- Subject looks imposing, grand
- Dramatic sky emphasis
- Heroic, monumental feel
- Good for architecture

**Eye Level:**

- Human, relatable perspective
- Approachable and authentic
- Documentary standard
- Natural storytelling

**Recommendation:** Wide angle for most host country imagery; aerial for special showcase

---

## Platform-Specific Guidelines

### Instagram

**Feed (1:1 Square):**

- Universal format, always visible
- Good for balanced compositions
- Thumbnail visible in profile grid
- Versatile across content types

**Stories (9:16 Vertical):**

- Full-screen mobile experience
- Tall buildings, vertical streets work well
- Time-sensitive urgent content
- Interactive elements possible

**Reels (9:16 Vertical):**

- Video-first but static graphics work
- Dynamic, engaging content
- Under 90 seconds
- Trending audio optional

**Recommendations:**

- Use 16:9 for landscape/stadium posts (crops to 4:5 in feed)
- Use 9:16 for Stories (tall murals, vertical streets)
- Use 1:1 for guaranteed full visibility in feed

---

### Twitter/X

**Standard Post:**

- 16:9 shows fully in timeline
- 1:1 also works well
- Quick scannable content
- Bold, clear imagery

**Recommendations:**

- 16:9 for most content
- 1:1 for guaranteed visibility
- High contrast for timeline scroll

---

### Broadcast/TV (16:9)

**Television & Streaming:**

- 16:9 mandatory standard
- Large screen viewing
- Desktop and TV optimized
- More detail visible

**Considerations:**

- Readable from distance
- Professional broadcast quality
- Safe margins for different TVs
- No critical info in outer 10%

---

### Website Hero Images

**Desktop Hero:**

- 16:9 or 21:9 ultra-wide
- Large, high-resolution
- First impression critical
- Desktop viewing optimized

**Mobile Hero:**

- 9:16 or 4:5 vertical
- Mobile-first responsive
- Smaller file size
- Touch-optimized

---

## Common Issues & Solutions

### Issue: Image Looks Too Staged or Artificial

**Solutions:**

- Add "candid," "authentic," "documentary" to prompt
- Request "photojournalism" style
- Use `--style raw` in Midjourney
- Negative prompt: "no posed, no staged, authentic moments"
- Increase stylize for more realism (paradoxically, for documentary)

---

### Issue: Wrong Cultural Elements or Stereotypes

**Solutions:**

- Research authentic regional characteristics
- Be specific: "Mexico City colonial architecture" not just "Mexican"
- Avoid clichés: "vibrant street art" not "sombreros and cacti"
- Specify modern elements: "contemporary urban Mexico City"
- Consult cultural resources or advisors

---

### Issue: Lighting Doesn't Match Environment

**Solutions:**

- Specify exact time: "golden hour sunset," "midday harsh sun"
- Mention weather: "overcast soft light," "clear blue sky"
- Add atmospheric conditions: "humid tropical atmosphere"
- Be consistent: Desert = harsh sun; Winter = overcast grey

---

### Issue: Landmarks Not Recognizable

**Solutions:**

- Name landmarks explicitly: "Times Square," "Copacabana Beach"
- Describe iconic features: "snow-capped mountain backdrop visible"
- Reference famous architecture: "Art Deco buildings," "colonial facades"
- Use multiple identifying features: "Pacific Ocean + palm trees + modern stadium"

---

### Issue: Crowd or People Look Fake

**Solutions:**

- Request "diverse crowd," "authentic people," "candid moments"
- Specify "photorealistic faces" or "documentary photography"
- Use `--quality 2` for face detail
- Avoid overly perfect symmetry
- Request "natural interactions," "genuine emotions"

---

### Issue: Colors Don't Match Region

**Solutions:**

- Research regional color palettes before prompting
- Specify exact colors: "terracotta and bright blue," "whitewashed walls"
- Reference real places: "Mexico City vibrant painted walls"
- Adjust in post if needed (Photoshop, Lightroom)

---

## Workflow Best Practices

### Pre-Production Planning

**Research Phase:**

1. Study real photography from host country
2. Identify key landmarks and characteristics
3. Understand climate and typical weather
4. Note cultural visual elements
5. Review tournament schedule and timing

**Prompt Development:**

1. Start with base template
2. Add specific cultural elements
3. Specify lighting and weather
4. Include landmark details
5. Request photography style and quality

---

### Production Iteration

**First Pass (3-5 variations):**

- Generate multiple options with different parameters
- Vary stylize values (300, 400, 500)
- Test different times of day
- Explore composition angles

**Second Pass (Refinement):**

- Select best first pass option
- Refine prompt with more specific details
- Adjust parameters for desired mood
- Fine-tune lighting and atmosphere

**Final Polish:**

- Export high-resolution version
- Minor adjustments in photo editor if needed
- Ensure cultural accuracy
- Verify quality standards met

---

### Post-Production Tips

**Color Grading:**

- Enhance but don't alter cultural authenticity
- Warm tones for golden hour
- Cool tones for blue hour or winter
- Consistent palette across series

**Cropping & Framing:**

- Adjust aspect ratio for platform
- Ensure key elements in safe zones
- Maintain rule of thirds
- Don't crop out important context

**Text Overlays (if needed):**

- Use clean sans-serif fonts
- High contrast for readability
- Don't obscure key visual elements
- Maintain cultural sensitivity

---

## Quality Standards

### Professional Checklist

Before publishing any host country culture graphic:

- [ ] **Cultural Authenticity:** Regional characteristics accurate?
- [ ] **Photography Quality:** Photorealistic and professional?
- [ ] **Lighting Appropriate:** Time of day and weather logical?
- [ ] **Composition Strong:** Rule of thirds, depth, balance?
- [ ] **Landmark/Context Clear:** Location recognizable?
- [ ] **No Stereotypes:** Respectful cultural representation?
- [ ] **People Authentic:** Candid, natural, diverse?
- [ ] **Colors Accurate:** Regional palette authentic?
- [ ] **Resolution High:** 8k quality, sharp details?
- [ ] **Aspect Ratio Correct:** Appropriate for platform?
- [ ] **Atmosphere Palpable:** Mood and energy clear?
- [ ] **Storytelling Effective:** Image tells compelling story?

---

## Ethical & Cultural Considerations

### Respectful Representation

**Do:**

- Research cultural norms and values
- Represent diversity authentically
- Show modern and traditional elements
- Celebrate cultural pride respectfully
- Consult with local cultural advisors

**Don't:**

- Use stereotypes or clichés
- Exoticize or "other" cultures
- Ignore local sensitivities
- Appropriate sacred imagery
- Present outdated or false representations

---

### Documentary Ethics

**Authenticity:**

- Represent real conditions honestly
- Don't mislead about locations or contexts
- Show diverse perspectives
- Avoid overly staged or artificial scenes

**Respect:**

- Consider privacy in crowd shots
- Avoid exploitative imagery
- Represent people with dignity
- Show communities in positive light

---

## Advanced Techniques

### Atmospheric Effects

**Weather Integration:**

- Snow, rain, mist, heat shimmer
- Enhances storytelling and mood
- Shows environmental adaptation
- Creates visual interest

**Time-Based Lighting:**

- Golden hour warmth
- Blue hour drama
- Midday intensity
- Night city lights

**Environmental Context:**

- Mountains, oceans, deserts
- Urban density, open spaces
- Natural wonders
- Built environment character

---

### Series Consistency

**Visual Cohesion:**

- Consistent color grading across series
- Similar stylize values
- Unified photography style
- Coherent storytelling

**Brand Identity:**

- Establish visual language
- Maintain across all graphics
- Build recognition
- Professional consistency

---

## Related Host Country Culture Graphics

Explore specialized host country culture types:

- **[Stadium Venue Integration](host-stadium-venue-integration.md)** - Stadiums with local landmarks and natural backdrops
- **[Urban Tournament Atmosphere](host-urban-tournament-atmosphere.md)** - City celebrations, fan zones, public viewing
- **[Cultural Street Scenes](host-cultural-street-scenes.md)** - Street football, murals, grassroots culture
- **[Training Ground Atmosphere](host-training-ground-atmosphere.md)** - Training in local weather and conditions

---

## Quick Reference: Prompt Templates

### Stadium with Landmark

```
[Stadium name] with [landmark] visible in background, golden hour light, architectural photography, tournament flags, photorealistic composition, 16:9 --ar 16:9 --stylize 350 --quality 2 --style raw
```

### Urban Celebration

```
[City name] [landmark] at sunset merged with tournament atmosphere, [screens/digital displays] showing match scores, national supporters filling streets in colors, photorealistic cultural fusion --ar 16:9 --stylize 450 --quality 2 --style raw
```

### Street Culture

```
[Country/city] street football scene, vibrant painted mural backdrop, children playing in colorful alley, warm [regional] cultural palette, afternoon golden light, authentic documentary photography --ar 16:9 --stylize 400 --quality 2 --style raw
```

### Training Ground

```
[Country] [climate condition] training ground, national team players in training kit practicing in [weather], [environmental effect visible], atmospheric sports documentary --ar 16:9 --stylize 350 --quality 2 --style raw
```

---

**Master Collection:** [PROMPT.Host-Country-Culture.txt](PROMPT.Host-Country-Culture.txt) - Complete host country culture prompt library.
