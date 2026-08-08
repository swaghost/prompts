# Pattern Interruption Hook Guide

**Social Media Pattern Interruption Campaigns** — Creating viral scroll-stopping content where physical objects break through and interact with the Instagram interface.

---

## What is Pattern Interruption?

**Pattern Interruption** is a viral social media advertising technique where real-world objects (cars, products, vehicles, planes) physically interact with, cross over, crash through, or transform the Instagram interface itself. The post UI (likes, comments, shares, captions) becomes a **physical surface** that objects can drive across, spill onto, smash through, or tear open.

### The Core Concept

Instead of traditional static posts, pattern interruption campaigns create **unexpected physical interactions** between content and interface:

- A luxury car drifts across the feed, leaving tire marks on the like counter
- Lip gloss spills across the comment section like a liquid surface
- A delivery scooter jumps the interface while a police car crashes through it
- An airplane tears through the post, revealing clouds beneath the UI

The **Instagram interface remains readable** but becomes a tangible physical layer that the subject interacts with, creating a scroll-stopping "wait, what?" moment.

---

## Why Pattern Interruption Works

### 1. **Breaks Visual Expectations**

Users scroll Instagram on autopilot. When a car literally drives across the interface or a plane tears it open, it **disrupts the pattern** and forces attention.

### 2. **Creates Curiosity & Shares**

"How did they do that?" — Pattern interruption posts get saved, shared, and discussed because they feel novel and technically impressive.

### 3. **Platform-Native Viral Format**

The content is **designed for social media** — it uses the platform's own UI as part of the creative concept, making it feel native while being disruptive.

### 4. **Brand Storytelling Through Action**

- Mercedes: "Entering the weekend sideways" → luxury performance
- Fenty Beauty: "Gloss so good it stops the scroll" → premium beauty
- Domino's: "Delivered before you finished scrolling" → speed
- Emirates: "Stop scrolling. Start flying." → travel aspiration

The physical action **embodies the brand message**.

---

## Production Workflow

Pattern interruption campaigns use a **two-step production system**:

### Step 1: Generate Clean Base Image (First Frame)

Create a **photorealistic static image** with:

- Top-down aerial perspective (9:16 vertical format)
- Instagram-style interface strip running horizontally through center
- Subject (car/product/vehicle) positioned at starting point
- **No action yet** — completely clean, no tire marks, spills, crashes, or portals
- Interface text must be sharp, correctly spelled, no wrapping

**Platform:** Nano Banana Pro, GPT Image, Flux, MidJourney

**Critical:** The base image establishes identity lock, composition, lighting, and interface accuracy. All text must be pixel-perfect before animation.

### Step 2: Animate in Seedance 2.0

Upload the approved base image and generate animation with:

- **Camera locked** — perfect top-down view maintained throughout
- Subject performs action (drift, spill, chase, portal tear)
- Physical interaction with interface (crossing over, covering, crashing through, tearing)
- **Interface remains fixed** — no flicker, regeneration, or text changes
- Sound effects appropriate to action (engine, gloss flow, crash, whoosh)

**Platform:** Seedance 2.0 (video generation from first-frame reference)

**Critical:** The interface must remain readable and unchanged. The physical action must clearly interact with the UI layer.

---

## Technical Requirements

### Camera & Composition

**Top-Down Aerial Perspective:**

- Perfect 9:16 vertical format (Instagram Reels/Stories)
- Camera locked at 90° looking straight down
- No camera movement, zoom, pan, or tilt
- Subject enters from top, crosses interface, exits bottom
- Instagram UI strip runs horizontally through exact center

### Instagram Interface Strip

**Must Include (Sharp & Correctly Spelled):**

- Engagement numbers: `X.XM likes`, `X,XXX comments`, `XX.XK shares`
- Attribution: `Liked by [username] and others`
- Account name with verified badge
- Caption text (brand message, call to action)
- Timestamp: `X hours ago`

**Critical Requirements:**

- Single-line rendering, no text wrapping
- Correct spelling throughout
- No broken letters, duplicated icons, or extra text
- Interface appears physically printed/built into the surface
- Remains readable even when partially covered or broken

### Physical Interaction Rules

**The interface must behave like a physical layer:**

1. **Crossing (Mercedes, Domino's scooter):** Object passes ABOVE interface, temporarily covering parts of it, not behind or underneath

2. **Spilling (Fenty Beauty):** Liquid flows OVER interface surface, partially covering text while keeping layout recognizable

3. **Crashing (Domino's police car):** Interface cracks and breaks like physical material with debris, but remaining text stays readable

4. **Tearing (Emirates):** Interface bends under weight, then tears open revealing space beneath (clouds), edges flutter like material

**Key Principle:** Interface is a tangible surface, not a transparent overlay.

---

## Campaign Types & Examples

### 01 — Mercedes: Automotive Drift

**Concept:** Silver Mercedes performance sedan drifts across weathered concrete parking surface, leaving fresh curved tire marks that cross the Instagram interface strip.

**Physical Interaction:** Car drives over interface, tire marks appear progressively behind moving tires, continuing seamlessly from upper concrete → across interface → onto lower concrete.

**Brand Message:** "Entering the weekend sideways..." — luxury performance, automotive excitement

**Best For:** Automotive brands, luxury cars, performance vehicles, motorsports

**Surface:** Weathered grey concrete with parking lines

---

### 02 — Fenty Beauty: Luxury Lip-Gloss Spill

**Concept:** Thick shiny nude-pink lip gloss spills from tube, flowing across warm beige stone vanity surface and spreading over Instagram interface.

**Physical Interaction:** Glossy viscous liquid flows in smooth ribbon, partially covers interface as physical layer while keeping overall layout recognizable.

**Brand Message:** "Gloss so good it stops the scroll." — premium beauty product, tactile luxury

**Best For:** Beauty brands, cosmetics, skincare, luxury personal care

**Surface:** Refined warm beige stone vanity with natural veining

---

### 03 — Domino's: Scooter Chase & Interface Crash

**Concept:** Domino's delivery scooter speeds across asphalt intersection and clears the interface safely, while pursuing police car crashes through it with dramatic impact.

**Physical Interaction:** Scooter crosses cleanly over interface, police car smashes through creating cracks, debris, dust burst. Scooter stops, rider looks back, then accelerates away.

**Brand Message:** "Delivered before you finished scrolling." — delivery speed, playful rebellion

**Best For:** Food delivery, quick service, brands emphasizing speed, playful brands

**Surface:** Realistic asphalt city intersection with lane markings and zebra crossings

---

### 04 — Emirates: Runway Portal

**Concept:** Emirates aircraft accelerates down runway toward Instagram interface. Interface bends under aircraft's weight, then tears open revealing bright cloud-filled sky beneath like a portal. Plane passes through and emerges into lower half.

**Physical Interaction:** Interface behaves like tensioned physical surface that bends downward, then tears through middle revealing clouds beneath. Torn edges flutter like heavy material.

**Brand Message:** "Stop scrolling. Start flying." — travel aspiration, escape, adventure

**Best For:** Airlines, travel brands, tourism, hospitality, aspirational luxury

**Surface:** Airport runway with centerline markings and threshold details

---

## Quality Control Checklist

### Base Image (First Frame) Validation

**Before Animation:**

- [ ] 9:16 vertical format, top-down aerial perspective
- [ ] Instagram interface strip runs horizontally through exact center
- [ ] All engagement numbers correctly formatted and spelled
- [ ] Username, verified badge, caption text, timestamp all present and correct
- [ ] No text wrapping — everything on single lines
- [ ] Subject positioned at starting point (slightly entering from top)
- [ ] Scene completely clean — no tire marks, spills, crashes, tears, or motion
- [ ] Surface texture photorealistic (concrete, stone, asphalt, runway)
- [ ] No people, no extra objects, no added text beyond specified interface
- [ ] High contrast, crisp detail, professional lighting

### Animation Validation

**After Seedance 2.0 Generation:**

- [ ] Camera remains locked in perfect top-down view throughout
- [ ] Subject performs action smoothly (drift, spill, chase, portal)
- [ ] Physical interaction clearly visible — object affects interface
- [ ] Interface text remains fixed, readable, no flicker or regeneration
- [ ] No spelling changes, broken letters, duplicated icons
- [ ] No text wrapping or layout shifts during animation
- [ ] Appropriate sound effects (engine, liquid flow, crash, whoosh)
- [ ] Realistic physics for action (tire marks, viscosity, impact, tearing)
- [ ] Final frame shows completed action with interface still recognizable
- [ ] Duration appropriate (typically 3-6 seconds for viral impact)

### Brand Safety Review

**Before Publishing:**

- [ ] Brand name spelled correctly throughout
- [ ] Product/vehicle accurately represented
- [ ] Caption message aligns with brand voice
- [ ] Engagement numbers look realistic (not absurdly high or low)
- [ ] No unintended text errors introduced by AI
- [ ] Interface elements don't obscure critical brand details
- [ ] Action doesn't create unintended negative associations

---

## Customization Framework

### Adapting Pattern Interruption to Any Brand

**Core Elements to Customize:**

1. **Subject/Product**
   - Your branded product, vehicle, or object
   - Must have clear visual identity
   - Should be recognizable from top-down view

2. **Surface/Background**
   - Matches brand aesthetic (luxury stone, urban asphalt, natural wood, etc.)
   - Provides realistic texture for physical interaction
   - Creates appropriate mood (premium, playful, dramatic, aspirational)

3. **Physical Action**
   - Drift/drive across (automotive, speed, performance)
   - Spill/flow over (liquids, beauty, food, beverages)
   - Crash/smash through (impact, power, disruption, rebellion)
   - Tear/portal open (transformation, escape, revelation, aspiration)

4. **Interface Text**
   - Engagement numbers (realistic for your brand size)
   - Username (your brand account)
   - Caption (your brand message, CTA, or tagline)
   - Timestamp (creates urgency and realism)

5. **Brand Message**
   - Caption should embody the physical action
   - Action should demonstrate brand value proposition
   - Create connection between interaction and brand story

---

## Advanced Prompt Engineering Tips

### Strengthening Physical Interaction

**Layer interaction descriptors:**

- "The [object] must physically pass ABOVE and cover parts of the interface while crossing"
- "It must not appear behind or underneath it"
- "The interface is a physical surface that [subject] interacts with"

**Emphasize surface behavior:**

- "Interface appears physically printed onto the [surface]"
- "Interface strip integrated into the surface"
- "Interface behaves like [tensioned fabric/rigid material/liquid surface]"

### Protecting Interface Text Accuracy

**Add preservation instructions:**

- "Keep the Instagram interface fixed and readable"
- "No movement, distortion, flicker, regeneration, or text wrapping"
- "Preserve exactly: [list all text elements]"
- "No spelling changes, broken letters, duplicated icons, or extra text"

**Use negative prompts:**

- "No text wrapping, no regenerated text, no letter distortion"
- "No duplicated UI elements, no extra interface layers"

### Enhancing Realism

**For automotive drift:**

- "Fresh curved black tire marks appear progressively only behind moving tires"
- "Realistic drift physics, body roll, steering correction"
- "Premium silver-body reflections, engine rev, tire squeal"

**For liquid spills:**

- "Thick, shiny, reflective, viscous and luxurious"
- "Realistic thickness, surface tension, soft highlights"
- "Smooth fluid physics, controlled ribbon flow"

**For crashes/impacts:**

- "Sharp impact with cracking, interface fragments, small debris"
- "Brief burst of dust while keeping remaining layout recognizable"
- "Realistic impact physics, material behavior"

**For tears/portals:**

- "Interface bends downward under weight like physical tensioned surface"
- "Tears open through middle revealing [space/clouds/environment] beneath"
- "Torn edges flutter briefly like heavy material"

### Camera Stability

**Critical for all pattern interruption:**

- "Keep the camera locked in a perfect top-down aerial view"
- "Camera must remain completely stationary throughout"
- "No camera movement, zoom, pan, tilt, or shake"
- "Maintain exact 90-degree overhead perspective"

---

## Platform & Tool Specifications

### Base Image Generation

**Recommended Platforms:**

- **Nano Banana Pro** (primary for photorealistic detail)
- **GPT Image** (ChatGPT — good for interface text accuracy)
- **Flux** (fast iteration for testing compositions)
- **MidJourney** (artistic quality but may struggle with text)

**Image Specifications:**

- **Format:** 9:16 vertical (1080x1920px or 1440x2560px)
- **Perspective:** Perfect 90° top-down aerial view
- **Quality:** Photorealistic, high detail, professional lighting
- **Output:** Single static image (first frame for animation)

### Video Animation

**Platform:**

- **Seedance 2.0** (first-frame reference video generation)

**Video Specifications:**

- **Duration:** 3-6 seconds (optimal for social media viral impact)
- **Format:** 9:16 vertical video
- **First Frame:** Upload approved base image as exact starting point
- **Camera:** Locked perspective maintained throughout
- **Quality:** High resolution, smooth motion, realistic physics

**Input Method:**

1. Upload approved base image as first-frame reference
2. Paste complete video generation prompt
3. Generate with interface preservation emphasis

### Post-Production (If Needed)

**Text Correction:**

- AI may slightly alter interface text during animation
- For branded publishing, inspect frame-by-frame
- Replace incorrect text in post-production using:
  - Adobe After Effects (tracking and text replacement)
  - DaVinci Resolve (text overlay and compositing)
  - Final Cut Pro (text layer corrections)

**Audio Enhancement:**

- Add or enhance sound effects (engine, liquid, crash, whoosh)
- Layer audio for impact timing
- Mix background ambience if needed

---

## Troubleshooting Common Issues

### Issue 1: Interface Text Wraps or Breaks Across Lines

**Problem:** Engagement numbers, caption, or username appear on multiple lines instead of single clean lines.

**Solutions:**

- Strengthen single-line instruction: "Render interface sharply and correctly on single lines with no wrapping"
- Specify each element separately: "1.2M likes | 8,431 comments | 12.6K shares — each on separate single line"
- Add negative prompt: "No text wrapping, no line breaks within individual elements"
- Try different image generation platform (GPT Image often better for text)
- Regenerate with simpler, shorter text if problem persists

### Issue 2: Spelling Errors in Interface Text

**Problem:** Brand name, username, or caption words misspelled in generated image.

**Solutions:**

- List critical text in ALL CAPS in prompt: "MERCEDES with verified badge"
- Spell out phonetically for difficult words: "emirates (E-M-I-R-A-T-E-S)"
- Regenerate multiple times and select cleanest version
- Fix in post-production using text replacement tools
- Verify text accuracy before moving to animation step

### Issue 3: Subject Appears Behind Interface Instead of Above

**Problem:** Car, product, or vehicle looks like it's underneath the interface layer instead of crossing over it.

**Solutions:**

- Strengthen layering language: "The [subject] must physically pass ABOVE and cover parts of the interface while crossing; it must not appear behind or underneath it"
- Add: "Interface is a physical surface layer that [subject] crosses over, temporarily covering portions of it"
- Emphasize: "Subject should obscure parts of interface text as it passes over, proving it's on top"
- Regenerate with stronger spatial hierarchy description

### Issue 4: Interface Flickers or Regenerates During Animation

**Problem:** Interface text changes, flickers, disappears, or regenerates with different content during video animation.

**Solutions:**

- Add preservation instruction to video prompt: "Keep the Instagram interface completely fixed and readable. Do not move, distort, regenerate, flicker, or wrap the text."
- List exact text to preserve: "Preserve exactly: [copy all interface text]"
- Emphasize: "No spelling changes, broken letters, duplicated icons, or extra text"
- Upload highest quality base image (more detail helps AI maintain consistency)
- Try multiple generations — AI consistency varies

### Issue 5: Physical Interaction Not Clear or Convincing

**Problem:** Tire marks don't cross interface, liquid doesn't flow properly, crash lacks impact, tear doesn't reveal beneath.

**Solutions:**

- Describe interaction progression step-by-step: "Tire marks begin on upper surface → continue seamlessly across Instagram strip → extend onto lower surface"
- Add physics descriptors: "Realistic drift physics, progressive tire marking, continuous path"
- Emphasize physical behavior: "Interface cracks like physical material" or "Interface tears like tensioned fabric revealing clouds beneath"
- Reference real-world equivalents: "Like driving on painted concrete" or "Like tearing paper to reveal another layer"

### Issue 6: Action Completes Too Fast or Too Slow

**Problem:** Animation pacing doesn't match viral social media timing (should be 3-6 seconds).

**Solutions:**

- Specify timing in video prompt: "Action should complete in approximately 5 seconds"
- Describe pacing: "The [subject] enters fast, performs action smoothly, and continues with confident motion"
- Add beat moments for emphasis: "The scooter stops briefly, rider looks back for one beat, then accelerates away"
- Request speed variations: "Add speed blur during fast sections, slow slightly during key interaction moment"

---

## Usage Scenarios

### 1. Social Media Advertising Campaigns

**Primary Use Case:**

- Instagram Reels, Stories, Feed posts
- TikTok promotional content
- Facebook short-form video ads
- Twitter/X video posts

**Benefits:**

- High engagement and share rates
- Scroll-stopping pattern disruption
- Platform-native viral format
- Memorable brand moment

### 2. Product Launches

**Launch Announcement:**

- New car model (automotive drift)
- New beauty product (gloss spill, makeup flow)
- New menu item (food/drink spill or crash)
- New service announcement (vehicle interaction)

**Creates:**

- Buzz and curiosity
- "How did they do that?" conversation
- Shareability and reach
- Premium brand perception

### 3. Brand Awareness Campaigns

**Ongoing Content:**

- Regular pattern interruption series
- Seasonal variations (same concept, different details)
- Multiple products using same interaction style
- Consistent brand aesthetic with viral format

**Establishes:**

- Signature content style
- Brand recognition through format
- Ongoing engagement loop
- Social media presence

### 4. Event Promotion

**Special Events:**

- Grand opening (doors/portals opening)
- Sale announcement (products crashing through)
- Festival/concert (stage breaking through feed)
- Travel destination reveal (plane portal effect)

**Generates:**

- Immediate attention
- Time-sensitive urgency
- Event excitement and anticipation
- Shareable announcement format

### 5. Influencer & Creator Content

**Collaboration Opportunities:**

- Branded creator partnerships
- Influencer product reviews with pattern interruption
- UGC campaigns using template format
- Ambassador content series

**Enables:**

- Authentic creator voice + viral format
- Scalable campaign across multiple influencers
- Cross-promotion and amplification
- Performance tracking across creators

---

## Pattern Interruption Series Ideas

### Concept Variations for Extended Campaigns

**1. Progressive Damage Series**

- Week 1: Object crosses interface cleanly
- Week 2: Object leaves marks/traces on interface
- Week 3: Object cracks interface partially
- Week 4: Object completely shatters interface

**2. Multi-Product Series**

- Use same interaction concept across product line
- Example: Different lip gloss shades spilling in different colors
- Example: Various car models performing different drift patterns
- Maintains brand consistency while showcasing variety

**3. Seasonal Pattern Interruption**

- Summer: Product emerging from water splash through interface
- Fall: Leaves blowing across and covering interface
- Winter: Ice/snow cracking through interface
- Spring: Flowers growing through interface tears

**4. Environmental Variations**

- Same product, different surfaces (concrete, marble, wood, sand, water)
- Showcases versatility or different use cases
- Creates visual variety within consistent format

**5. Escalating Intensity**

- Start subtle (small product crossing quietly)
- Build intensity (faster, more dramatic interactions)
- Climax (massive disruption, full interface transformation)
- Creates narrative arc across campaign

---

## Brand Category Applications

### Automotive

- **Actions:** Drift, burnout, drag race start, parking, car reveal
- **Surfaces:** Parking lot, racetrack, showroom floor, urban street
- **Messages:** Performance, luxury, innovation, lifestyle

### Beauty & Cosmetics

- **Actions:** Product spill, makeup brush stroke, powder explosion, cream spread
- **Surfaces:** Vanity counter, marble table, beauty station, mirror surface
- **Messages:** Premium quality, texture, luxury, self-care

### Food & Beverage

- **Actions:** Pizza toss, drink pour, food slide, ingredient drop
- **Surfaces:** Kitchen counter, restaurant table, bar top, food truck platform
- **Messages:** Fresh, fast, delicious, quality ingredients

### Travel & Hospitality

- **Actions:** Plane takeoff portal, suitcase roll, passport stamp, door opening reveal
- **Surfaces:** Airport runway, hotel lobby, beach sand, mountain path
- **Messages:** Adventure, escape, luxury, experience

### Fashion & Apparel

- **Actions:** Runway walk crossing, fabric unfold, shoe step, bag swing
- **Surfaces:** Runway, store floor, urban sidewalk, fashion studio
- **Messages:** Style, confidence, trend-setting, premium

### Technology & Electronics

- **Actions:** Device slide, screen swipe reveal, charging spark, unbox reveal
- **Surfaces:** Desk surface, tech lab table, retail display, modern workspace
- **Messages:** Innovation, cutting-edge, seamless, powerful

### Sports & Fitness

- **Actions:** Ball roll/bounce, athlete run, equipment drop, victory celebration
- **Surfaces:** Court, track, gym floor, field, outdoor terrain
- **Messages:** Performance, determination, victory, lifestyle

### Real Estate & Architecture

- **Actions:** Door opening, building rise, blueprint unfold, key drop
- **Surfaces:** Property grounds, architectural plans, construction site, luxury interior
- **Messages:** Opportunity, luxury, home, investment

---

## Legal & Brand Safety Considerations

### Copyright & Trademark

**Protect Your Brand:**

- Ensure brand name, logo, and trademarks are accurately represented
- Review interface text for any unintended trademark infringement
- Verify product/vehicle appearance matches official brand assets

**Third-Party Elements:**

- Instagram interface mockup is stylistic reference, not actual Instagram property
- Don't imply official Instagram endorsement unless partnered
- Consider custom interface design for brand safety

### Platform Guidelines

**Instagram/Meta Policies:**

- Check current advertising policies for pattern interruption content
- Ensure content doesn't violate community guidelines
- Verify any special effects don't trigger sensitive content filters

**Disclosure Requirements:**

- Include "Paid partnership" tag if required
- Add creative disclaimers if needed ("Dramatization" or "Visual effect")
- Follow FTC guidelines for advertising transparency

### AI-Generated Content Disclosure

**Transparency Options:**

- Some platforms require disclosure of AI-generated content
- Consider adding small text: "Created with AI" if needed
- Follow evolving platform policies on synthetic media

---

## Source Attribution

**Original Concept Source:** prompts.ig Pattern Interruption Campaign Prompts
**Campaigns Included:** Mercedes (Automotive Drift), Fenty Beauty (Luxury Gloss Spill), Domino's (Scooter Chase & Interface Crash), Emirates (Runway Portal)
**Production Workflow:** Two-step system — Base image generation + Seedance 2.0 animation
**Documentation Created:** 2026-08-07

---

## Related Files in This Library

**Individual Campaign Prompt Files:**

- [pattern-interruption-mercedes-drift.md](../PROMPTS/video/pattern-interruption-mercedes-drift.md) — Complete Mercedes automotive drift campaign
- [pattern-interruption-fenty-beauty-gloss-spill.md](../PROMPTS/video/pattern-interruption-fenty-beauty-gloss-spill.md) — Complete Fenty Beauty gloss spill campaign
- [pattern-interruption-dominos-chase.md](../PROMPTS/video/pattern-interruption-dominos-chase.md) — Complete Domino's delivery chase campaign
- [pattern-interruption-emirates-portal.md](../PROMPTS/video/pattern-interruption-emirates-portal.md) — Complete Emirates runway portal campaign

**Each file contains:**

- Complete base image generation prompt
- Complete Seedance 2.0 animation prompt
- Technical specifications
- Quality control checklist
- Customization options
- Troubleshooting
- Variations and series ideas

---

## Notes

- **Platform Evolution:** AI video generation capabilities improve rapidly. These prompts may need updates as Seedance 2.0 or alternative platforms evolve.
- **Text Accuracy Challenge:** AI models can struggle with small text. Always verify interface accuracy before animation and be prepared for post-production text correction.
- **Creative Experimentation:** Pattern interruption is a flexible concept. Use these 4 campaigns as templates, then innovate with your own brand-specific interactions.
- **Viral Potential:** Pattern interruption works best when the physical action genuinely embodies the brand message. The more clever and unexpected the connection, the higher the shareability.
- **Test and Iterate:** Generate multiple versions of base images, test different physical interactions, and refine based on engagement data.

---

**Total Lines:** ~680
