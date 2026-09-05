# AI Luxury Estate Blueprint Build-Up Guide

**By:** @aiwithchad  
**Source:** [Google Docs](https://docs.google.com/document/d/1h68DSDb58OVhUbkVcvY0yGj-gfaTcxGO/mobilebasic?urp=gmail_link)

Turn one empty luxury property into a fully landscaped estate with glowing architectural blueprints, satisfying construction, and a cinematic dusk reveal.

| Stage             | Tool / Method                                                            |
| ----------------- | ------------------------------------------------------------------------ |
| Image generation  | Nano Banana Pro                                                          |
| Video generation  | Seedance 2.0                                                             |
| Video method      | First Frame + Last Frame                                                 |
| Complete examples | Italian Estate Gardens, Tropical Resort Compound, Greek Cliffside Estate |

## Description

This workflow keeps a finished luxury residence as a fixed visual anchor while a glowing white masterplan draws itself across the empty grounds, transforms into physical landscaping and estate features, and resolves into a cinematic sunset or blue-hour lighting reveal. Controlled A/B/C reference frames prevent the house, camera, and completed site geometry from drifting.

## Usage

Use for luxury real-estate reels, landscape-architecture concepts, estate masterplan reveals, resort-development presentations, architectural visualization, and satisfying construction ASMR videos. The workflow is designed for a single locked aerial shot and a 10-second first-frame/last-frame generation.

## The Core Workflow

The effect works because the house stays as a fixed visual anchor while the landscape is designed around it. Instead of asking the video model to invent an entire estate from nothing, first create controlled start and end frames, then let Seedance 2.0 animate the transformation between them.

> **Key idea:** A = empty estate. B = completed daylight masterplan. C = finished dusk / sunset version. Seedance receives A as the FIRST FRAME and C as the LAST FRAME. B is the consistency bridge for creating C.

### Step 1 - Generate Image A: The Empty Estate

Generate a finished luxury residence on a huge, mostly empty property. The camera matters more than almost anything else: use a medium-high drone shot with a strong downward angle, show the complete property, keep the house substantial but not oversized, and leave enormous blank ground for the blueprint animation.

- Keep the full property boundary visible.
- Place the road and centered entrance gate along the bottom of frame.
- Avoid a low drone angle, wide horizon, or extreme satellite view.
- Do not pre-build pools, roads, gardens, or landscaping that you want to animate later.

### Step 2 - Edit A into Image B: The Completed Daylight Estate

Use Image A as the reference in Nano Banana Pro. Lock the camera and house, then build the complete masterplan around it. This is where you decide exactly what the video should construct: driveways, paths, pools, gardens, guest buildings, parking, trees, and other details.

### Step 3 - Edit B into Image C: The Final Lighting State

Use Image B as the reference and make a lighting-only edit. Keep the geometry pixel-consistent wherever possible. Shift the estate into blue hour, dusk, or sunset and activate the final architectural lighting. This gives Seedance a very clear end state.

### Step 4 - Generate in Seedance 2.0

Open Seedance 2.0 and use First Frame + Last Frame. Upload Image A as the FIRST FRAME and Image C as the LAST FRAME. Paste the matching video prompt from the relevant example and generate a 10-second clip.

- First frame: Image A, empty estate.
- Last frame: Image C, fully finished final estate.
- Duration: 10 seconds.
- Keep the camera locked and the house unchanged.
- Use no music; request only synchronized outline and construction ASMR.

### Step 5 - Pick the Cleanest Generation

The best take is the one where the white plan clearly draws first, physical materials follow those exact lines, the house never morphs, and the final lighting transition feels natural. Regenerate if the terrain moves, the camera shifts, or large objects teleport into place.

> **Why B matters:** B is not required as an input to Seedance, but it makes C dramatically more consistent. You are editing the exact finished daylight masterplan into the final dusk frame instead of asking Nano Banana Pro to invent the entire end state again.

## Before You Generate: Quick Checklist

- [ ] House is completely finished in A and stays the visual anchor.
- [ ] Large blank lawn / ground exists around the house.
- [ ] Camera is medium-high, strongly downward, and not too close.
- [ ] Entire estate fits inside frame.
- [ ] Entrance gate and front road are visible at the bottom.
- [ ] No wide horizon unless the concept specifically needs it.
- [ ] B preserves the exact A camera and house.
- [ ] C is a lighting / weather edit of B, not a redesign.
- [ ] Seedance uses A as first frame and C as last frame.
- [ ] Video prompt explicitly says no music and no camera changes.

## Ten-Second Timing

| Time      | Action                                      |
| --------- | ------------------------------------------- |
| 0.0-0.4s  | Hold the empty estate.                      |
| 0.4-1.5s  | Blueprint begins from the gate.             |
| 1.5-3.2s  | Masterplan expands across the property.     |
| 3.2-4.2s  | Final outline details complete.             |
| 4.2-6.9s  | Blueprint turns into physical construction. |
| 6.9-7.8s  | Final landscaping settles.                  |
| 7.8-10.0s | Sunset / blue hour / lighting reveal.       |

# Example 1 - Italian Estate Gardens

Formal cypress avenues, parterre gardens, fountains, and a cinematic blue-hour reveal.

## A - Nano Banana Pro / Empty Estate

```text
Photorealistic luxury real-estate drone photograph, vertical composition.

CAMERA AND COMPOSITION ARE CRITICAL: medium-high elevated drone view looking downward at the complete rectangular estate. The front road and centered gate are visible at the bottom, the rear boundary is visible at the top, and there is no horizon or sky. The camera looks strongly downward while still revealing the villa facade and roof architecture. Not a satellite view and not an extreme top-down shot.

A magnificent finished Italian villa sits centered within the property and occupies about 35-40% of the image width. Timeless architecture: warm ivory stucco, pale limestone details, tall arched windows, refined balconies, terracotta roof tiles and elegant Tuscan character.

The villa is completely finished, but the surrounding estate is intentionally undeveloped. One enormous uninterrupted manicured green lawn fills almost the entire property, leaving huge blank areas in front, behind and on both sides.

NO driveway network, formal gardens, fountains, swimming pool, sculptures, pathways, guest houses, parking areas, cars or elaborate landscaping.

A small elegant wrought-iron gate is centered along the bottom boundary beside a straight country road. Tall manicured evergreen hedges define the property. Show only a modest amount of neighboring Italian countryside around the edges.

Perfect centered composition, strong symmetry, bright natural daylight, realistic grass, premium architectural drone photography, extremely photorealistic. Keep the entire estate visible and the villa substantial but not oversized.
```

## B - Nano Banana Pro / Completed Daylight Masterplan

```text
Use the A image as the reference. Preserve the exact camera position, drone altitude, angle, crop, villa size, road and complete property boundaries. Do not zoom, tilt, move the villa or change perspective.

Transform only the empty lawn into an extraordinary completed Italian formal estate garden.

From the centered gate, create a grand pale-stone driveway leading to a symmetrical arrival court. Add axial and curved gravel paths, clipped boxwood parterres, formal hedge rooms, rows of tall cypress trees, ornamental lawns, classical fountains, restrained statues and elegant planters.

Behind and around the villa, create terraced Italian gardens with Mediterranean planting, citrus trees in planters, refined stone landscaping and a long elegant swimming pool or reflecting pool. Add one or two subtle garden pavilions and discreet premium-car parking. Finish the perimeter with mature privacy trees and cypress-lined edges.

Everything should feel timeless, luxurious, symmetrical and highly photorealistic. CRITICAL: do not redesign, move, enlarge or alter the original villa.
```

## C - Nano Banana Pro / Final End Frame

```text
Use the B image as the reference. LIGHTING-ONLY EDIT. Preserve the composition, camera, villa, driveway, gardens, pool, trees, cars and every object position exactly.

Change bright daylight into elegant blue-hour dusk. Turn on warm interior lighting inside the villa, subtle exterior architectural lighting, path lights, garden uplighting, fountain lighting and soft pool or reflecting-water illumination.

The finished estate should feel romantic, luxurious and cinematic, with realistic blue-hour ambience and warm architectural glow. Do not alter any physical geometry.
```

## Italian Estate Gardens - Seedance 2.0 Video Prompt

Upload A as the first frame and C as the last frame, then paste this prompt.

```text
Single continuous locked aerial drone shot, exactly 10 seconds. No cuts and no camera changes.

The central Italian villa must remain completely unchanged and perfectly stationary throughout the entire video. Its architecture, rooflines, windows, proportions, terraces, position and orientation never morph.

Maintain the exact same aerial composition as the starting image: medium-high luxury real-estate drone view, strong downward angle, entire rectangular property visible, front road and centered gate at the bottom, rear boundary at the top, no horizon.

AUDIO: Absolutely NO MUSIC, NO SCORE and NO VOICEOVER. Use only clean, realistic, highly satisfying synchronized ASMR sounds from blueprint drawing and physical construction.

0.0-0.4 sec: Hold briefly on the finished villa surrounded by enormous empty lawn.

0.4-1.5 sec: Thin brilliant white architectural planning lines draw from the front gate, tracing the driveway, arrival court, axial garden layout and symmetrical pathways. Use soft pencil-like scratching, delicate drafting sounds, tiny clicks and subtle light-trace shimmer.

1.5-3.2 sec: The glowing blueprint expands around and behind the villa, tracing parterre gardens, hedge rooms, cypress rows, fountains, statues, gravel paths, terraced gardens, pool or reflecting-water feature, pavilions and parking areas.

3.2-4.2 sec: Complete the final blueprint details. The lawn remains underneath while the full glowing masterplan is clearly visible.

4.2-6.9 sec: The blueprint transforms smoothly into physical reality through the exact outlines. Pale stone driveway surfaces fill from the gate toward the villa. Gravel paths spread, boxwood hedges rise, cypress trees grow, fountains and terraces materialize, the pool forms and fills with water, pavilions assemble and cars settle into completed parking areas. Use satisfying stone-sliding, granular settling, foliage rustles, water-filling and soft construction ASMR. Nothing randomly appears or teleports.

As each element completes, its glowing outline softly fades away.

6.9-7.8 sec: Final landscaping and small details settle naturally into place.

7.8-10.0 sec: Construction stops. Daylight smoothly transitions into elegant blue-hour dusk. Warm interior lights, path lighting, fountain lighting, garden uplighting and pool lighting activate progressively with tiny subtle activation sounds.

NO MUSIC OF ANY KIND. No camera orbit, pan, zoom, cuts, villa morphing, disappearing objects or random popping elements. Blueprint lines draw first, then transform into the finished estate.
```

# Example 2 - Tropical Resort Compound

A blank tropical estate becomes a five-star private resort with pools, palms, cabanas, and guest villas.

## A - Nano Banana Pro / Empty Estate

```text
Photorealistic luxury real-estate drone photograph, vertical composition.

CAMERA AND COMPOSITION ARE CRITICAL: medium-high elevated drone view looking strongly downward over a huge rectangular tropical estate. The complete property is visible from the front road and centered gate at the bottom to the rear boundary at the top. No horizon or sky. Not an extreme satellite view.

A spectacular finished modern tropical mansion sits centered around the middle of the estate, occupying about 35-40% of the image width. Architecture combines pale limestone, warm natural timber, white stucco, floor-to-ceiling glass, broad shaded terraces, flat roof sections and refined resort-style geometry.

The residence is completely finished, but the entire surrounding estate is intentionally undeveloped. One enormous uninterrupted manicured green lawn creates huge blank areas in front, behind and along both sides.

NO driveway network, pools, tropical gardens, palm clusters, cabanas, guest villas, pathways, parking structures, vehicles, water features or outdoor lounges.

Only a sophisticated centered entrance gate connects to a straight road along the bottom. Tall tropical privacy hedging clearly defines the property. Show only modest lush neighboring context outside the boundary.

Perfect centered composition, strong symmetry, bright daylight, premium drone real-estate photography, highly photorealistic. Keep the entire property visible and the house substantial but not oversized.
```

## B - Nano Banana Pro / Completed Daylight Masterplan

```text
Use the A image as the reference. Preserve the exact camera position, drone altitude, downward angle, framing, mansion scale, road and all property boundaries. Do not zoom, tilt, move or redesign the residence.

Transform only the empty lawn into a spectacular completed luxury tropical resort compound.

From the centered gate, create an elegant pale-stone resort driveway, curved approach roads, landscaped islands and a refined arrival court. Add lush tropical landscaping with palms, flowering plants, layered greenery and manicured resort lawns.

Behind and around the residence, create a large resort-style pool complex with turquoise water, shallow lounging shelves, pool decks, smaller plunge pools, cabanas, lounge pavilions, guest villas or bungalows, outdoor dining areas, spa-style garden zones and winding pedestrian paths.

Add discreet parking with several premium vehicles, stone walkways, tropical garden courts, dense palm clusters and lush perimeter planting. Everything should feel spacious, cohesive, world-class and photorealistic. Keep the existing residence unchanged.
```

## C - Nano Banana Pro / Final End Frame

```text
Use the B image as the reference. LIGHTING-ONLY EDIT. Preserve every structure, pool, path, palm, vehicle and camera detail exactly.

Change bright daylight into luxurious blue-hour dusk. Turn on warm interior lights inside the main residence and guest structures, subtle pathway lighting, garden uplighting, cabana lighting, elegant pool lighting and soft underwater glow in water features.

The final scene should feel cinematic and inviting like a five-star tropical resort at twilight. Do not alter physical geometry or object placement.
```

## Tropical Resort Compound - Seedance 2.0 Video Prompt

Upload A as the first frame and C as the last frame, then paste this prompt.

```text
Single continuous locked aerial drone shot, exactly 10 seconds. No cuts and no camera changes.

The central tropical resort residence must remain completely unchanged and perfectly stationary throughout the video. Its architecture, rooflines, windows, terraces, proportions, position and orientation never morph.

Maintain the exact same aerial composition as the starting image: medium-high luxury real-estate drone view, strong downward angle, entire rectangular property visible, front road and centered gate visible at the bottom, rear boundary visible at the top, no horizon.

AUDIO: Absolutely NO MUSIC, NO SCORE and NO VOICEOVER. Use only clean, realistic, satisfying synchronized ASMR outline and building sounds.

0.0-0.4 sec: Hold briefly on the finished residence surrounded by enormous empty lawn.

0.4-1.5 sec: Thin brilliant white architectural planning lines draw from the front gate, tracing the resort driveway, curved approach roads, landscaped islands and arrival court. Use delicate pencil-like scratching, tracing, tiny clicks and faint light shimmer.

1.5-3.2 sec: The glowing blueprint expands around the residence and across the rear grounds, tracing the pool complex, plunge pools, pool decks, winding paths, cabanas, guest villas, lounge zones, dining areas, spa spaces, parking and planting zones.

3.2-4.2 sec: Complete the final blueprint details while the grass remains visible underneath.

4.2-6.9 sec: The blueprint transforms into physical reality through the exact outlines. Pale stone paving fills the driveway and arrival court. Pool forms become real and fill with turquoise water. Pool decks materialize, guest villas and cabanas assemble, palms and tropical plants grow upward, lounge areas settle into place and cars appear only after parking surfaces complete. Use satisfying stone placement, water-filling, foliage movement, wood fitting and soft structural ASMR. Nothing randomly appears.

As each real element completes, its glowing outline softly fades away.

6.9-7.8 sec: Final landscaping finishes. Palm clusters, tropical plants, privacy hedges and small details settle naturally into place.

7.8-10.0 sec: Construction stops. Daylight transitions into luxurious blue-hour dusk. Warm interior lights, pool lighting, path lights, garden uplighting and cabana lighting illuminate progressively with tiny subtle activation sounds.

NO MUSIC OF ANY KIND. No camera orbit, pan, zoom, cuts, house morphing, disappearing objects or random popping elements. Blueprint lines draw first, then transform into the finished resort.
```

# Example 3 - Greek Cliffside Estate

Cycladic architecture, Mediterranean landscaping, an infinity pool, and a warm sunset-glare transition.

## A - Nano Banana Pro / Empty Estate

```text
Photorealistic luxury real-estate drone photograph, vertical composition.

CAMERA AND COMPOSITION ARE CRITICAL: medium-high elevated drone view looking strongly downward over an enormous rectangular private cliffside estate. Show the complete property from the front road and centered entrance gate at the bottom to the rear cliffside boundary and sea at the top. No wide horizon or sky. Not an extreme satellite view.

A spectacular finished Greek cliffside villa sits centered within the estate, occupying about 35-40% of the image width. Ultra-luxury Greek island architecture: crisp white stucco, soft stone details, elegant cubic Mediterranean forms, flat roofs, arched openings, shaded terraces, pergolas and sea-facing verandas.

The villa is completely finished, but the surrounding property is intentionally undeveloped. One enormous clean lawn and pale natural ground fills almost the entire estate, leaving huge open areas around the villa.

NO driveway network, swimming pool, formal courtyards, pathways, guest pavilions, outdoor lounges, parking, cars or elaborate landscaping.

A refined gate is centered along the bottom boundary beside a straight coastal road. The top of the property ends at a dramatic rocky Greek cliffside with brilliant deep-blue sea immediately beyond it. Low Mediterranean planting defines the side boundaries.

Perfect centered composition, strong symmetry, bright natural daylight, premium architectural drone photography, extremely photorealistic. Keep the entire property visible and the villa substantial but not oversized.
```

## B - Nano Banana Pro / Completed Daylight Masterplan

```text
Use the A image as the reference. Preserve the exact camera, drone altitude, downward angle, framing, villa size, front road, property boundaries, cliff edge and sea. Do not zoom, tilt or redesign the villa.

Transform only the empty grounds into an extraordinary completed Greek cliffside estate.

From the centered gate, create a refined pale-stone driveway leading to a beautiful arrival court. Add Mediterranean pathways, white-stone paving, sculpted courtyards, olive trees, cypress accents, drought-tolerant coastal planting, decorative planters and clean island-style landscape geometry.

Behind and around the villa, create spectacular sea-facing terraces, a cliffside infinity pool, pale-stone decking, sun loungers, shaded pergola lounges and elegant outdoor dining areas. Add one or two tasteful detached guest suites or small pavilions that echo the main villa. Create stepped lounge terraces toward the cliff edge and discreet premium-car parking near the front or side.

Finish with mature olive trees, low Mediterranean planting, ornamental grasses and refined privacy landscaping. Everything should feel serene, sun-drenched, architectural and highly photorealistic. Keep the original villa unchanged.
```

## C - Nano Banana Pro / Final End Frame

```text
Use the B image as the reference. LIGHTING-ONLY EDIT. Preserve the camera, villa, driveway, courtyards, terraces, infinity pool, pavilions, vehicles, trees, cliff edge and sea exactly.

Transform bright daylight into a breathtaking warm Greek-island sunset that transitions into elegant blue-hour dusk. Add a tasteful warm sun glare or lens flare from the sea side, as if the low setting sun is just outside the frame. Golden light should softly highlight the white villa, pale stone terraces, landscaping and pool water.

Then transition naturally into blue hour. Turn on warm interior lights inside the villa and guest suites, subtle pathway lights, terrace lighting, gentle garden uplighting and elegant pool lighting. Keep the glare refined and photorealistic, never overpowering.
```

## Greek Cliffside Estate - Seedance 2.0 Video Prompt

Upload A as the first frame and C as the last frame, then paste this prompt.

```text
Single continuous locked aerial drone shot, exactly 10 seconds. No cuts and no camera changes.

The central Greek cliffside villa must remain completely unchanged and perfectly stationary throughout the entire video. Its architecture, rooflines, windows, terraces, proportions, position and orientation never morph.

Maintain the exact same aerial composition as the starting image: medium-high luxury real-estate drone view, strong downward angle, entire rectangular property visible, front road and centered gate visible at the bottom, rear cliffside boundary and sea visible at the top, no wide horizon.

AUDIO: Absolutely NO MUSIC, NO SCORE and NO VOICEOVER. Use only clean, realistic, satisfying synchronized ASMR outline and building sounds.

0.0-0.4 sec: Hold briefly on the finished villa surrounded by the enormous empty estate grounds.

0.4-1.5 sec: Thin brilliant white architectural planning lines draw from the front gate, tracing the driveway, arrival court, elegant pathways and primary outdoor layout. Use soft drafting scratches, tiny clicks and subtle light-trace shimmer.

1.5-3.2 sec: The luminous blueprint expands around the villa and across the rear cliffside grounds, tracing Mediterranean courtyards, olive-tree placements, sea-facing terraces, stepped lounge platforms, infinity pool, pergolas, dining areas, guest suites and discreet parking.

3.2-4.2 sec: Complete the final blueprint details. The full Greek coastal masterplan glows clearly over the still-empty grounds.

4.2-6.9 sec: The blueprint transforms smoothly into physical reality through the exact outlines. Pale stone driveway surfaces fill from the gate toward the villa. Mediterranean paths and courtyards spread, olive trees and coastal plants grow, terraces and pergolas assemble, the infinity pool forms and fills, furniture settles into place and cars appear only after parking surfaces complete. Use satisfying stone-sliding, granular settling, foliage rustles, water-filling and soft construction ASMR. Nothing randomly appears or teleports.

As each real element completes, its glowing outline softly fades away.

6.9-7.8 sec: Final landscaping completes and the estate becomes fully finished.

7.8-10.0 sec: Construction stops. Daylight smoothly transitions into a warm sunset and then elegant blue-hour dusk. Add a tasteful low golden sun glare from the sea side, creating warm highlights across the villa, terraces and pool, then fade naturally into blue hour. Warm interior lights, path lighting, terrace lights, garden uplighting and pool lighting activate progressively with tiny subtle activation sounds.

NO MUSIC OF ANY KIND. No camera orbit, pan, zoom, cuts, villa morphing, disappearing objects or random popping elements. Blueprint lines draw first, then transform into the finished estate.
```

# Prompting Tips That Make This Work

1. **Camera lock:** Repeat the camera lock in A, B, C, and the video prompt. Camera drift is one of the fastest ways to ruin the effect.
2. **Keep the house static:** The property can transform dramatically, but the main residence should never rebuild or morph. Treat it as the permanent anchor.
3. **Draw first, build second:** The strongest generations visibly trace the white plan before anything physical forms. Explicitly tell Seedance that every physical feature must emerge from its corresponding outline.
4. **Leave negative space:** A huge blank property gives the blueprint somewhere to travel. If A already looks fully landscaped, the reveal loses most of its impact.
5. **Use B to make C:** Always create the finished daylight state first, then turn that same image into dusk / sunset. This is the easiest way to preserve geometry.
6. **Keep audio simple:** No music. Ask for crisp drafting scratches, tiny clicks, stone placement, gravel, foliage rustles, water filling, and soft structural fitting sounds. The sound should follow the visible action.

## Common Problems and Fixes

| Problem                      | Fix                                                                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| House morphs                 | Strengthen: "The central residence remains completely unchanged and perfectly stationary. Architecture never morphs."                           |
| Camera moves                 | Add: "No orbit, pan, zoom, reframing or camera changes."                                                                                        |
| Objects pop in               | Add: "Every physical element must emerge directly from its corresponding blueprint outline. Nothing randomly appears or teleports."             |
| End frame feels different    | Regenerate C from B as a lighting-only edit instead of generating C independently.                                                              |
| Blueprint is weak            | Give the outline phase more specific objects to trace: driveway, arrival court, pool, paths, gardens, pavilions, parking, and planting zones.   |
| Too little construction time | Keep the opening hold short. The proven timing gives roughly 4.2-6.9 seconds to the physical build and 7.8-10.0 seconds to the lighting reveal. |

## Final Quality Check

- The complete estate remains visible in every frame.
- The road and centered gate remain at the bottom of the composition.
- The central residence is unchanged from first frame to last.
- White blueprint lines fully draw before physical construction begins.
- Every physical element emerges from its corresponding outline.
- No element teleports, floats, melts, or randomly appears.
- Image C is a lighting-only edit of Image B.
- The camera never orbits, pans, zooms, reframes, or changes lens.
- Audio contains no music, score, dialogue, or voiceover.
- The final lighting transition is natural and preserves all geometry.

---

_Build the frame. Draw the plan. Watch the estate come to life._
