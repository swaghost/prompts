# AI Furniture Reveal for Real Estate & Interior Visualizations

## Concept Overview

The AI Furniture Reveal technique transforms a single, fully furnished architectural interior or exterior photograph into a high-end 8-second video animation. Instead of generating a new room from scratch, this workflow uses a reverse-engineering methodology.

## Two-Step Architecture

### Step 1: Asset Cleansing / Object Removal (Nano Banana)

An AI image generator removes all non-structural, loose furniture and decorative props to create a completely bare room shell.

### Step 2: Controlled Sequential Reassembly (Omni Flash - pollo.ai)

An AI video generator takes the bare room as the starting frame (0s) and the original furnished photograph as the final frame (6s–8s), animating the furnishings back into place sequentially using physics-based motion.

## Foundational Rules & Failure Preventions

### 1. Geometric Identity & Identical Cropping

The empty room image and the furnished photo must maintain identical aspect ratios, camera angles, perspective vanishing points, and focal lengths. Any framing discrepancy forces the AI model to morph and distort the architectural envelope.

### 2. Separation of Architectural Assets vs. Loose Props

Never instruct the AI to remove built-in cabinetry, recessed shelving niches, architectural columns, wall tiles, or permanent structural frameworks. Only loose furnishings (seating, tables, pendant lamps, rugs, and tabletop decor) should be cleared.

### 3. Discrete State Handling

Video generation models naturally attempt to cross-fade or morph between two reference images. Strict negative prompting and explicit timeline structuring are required to force discrete, object-by-object appearances.

### 4. Natural Impact Physics

Furnishings must not float arbitrarily into the scene. Heavy floor furniture must land firmly, wall elements must descend, textiles must settle, and small decor accessories must land with micro-impact vibrations.

## Reveal Motion Types

### POP-IN - Heavy Floor Furniture

Appears directly at its final position, slightly undersized for about two frames, overshoots very slightly, then settles to exact final size. Roughly 0.2 seconds. Silhouette and proportions never change, only overall scale. No travel, no rotation.

### DROP - Mid-Weight Furniture and Cabinets

Falls in from just above its final position and lands with a firm settle.

### DESCEND - Wall-Mounted and Hanging Objects

Lowers from above and stops at final height, with one short swing that damps out.

### SETTLE - Textiles, Cushions, Rugs, Bedding

Falls in from just above and flattens onto the surface on contact.

### INSTANT - Small Decor and Accessories

Appear in place in a single frame, no motion at all.

### FILL - Water

If the space contains an empty pool or basin, clear water rises from the bottom until it reaches the edge and settles into gentle ripples.

## Core Master Script Template (Omni Flash - 8 Seconds)

**Camera & Lock Instructions:**

```
Static real estate furniture reveal, 8 seconds. Locked-off camera. The only camera movement allowed is a subtle continuous drift of a few degrees that eases to a stop at 6s, small enough that the composition stays recognisably the same shot from start to finish. No dolly, no zoom, no whip pan.

CAMERA LOCK - ANGLE AND PERSPECTIVE NEVER CHANGE:
The camera position, height, angle, focal length, field of view, and perspective are exactly those of the reference images and stay fixed for the entire 8 seconds. All vanishing points, wall lines, floor lines, ceiling lines, and edges of openings remain in the same directions throughout. Do not reframe, re-angle, re-render, or re-photograph the room from a different viewpoint. Do not change lens compression or widen the view. Do not reveal any part of the room not visible in the reference images. The composition at every frame must overlay onto the reference images with the architecture in the same place.
```

**Reference Image Usage:**

```
HOW TO USE THE TWO REFERENCE IMAGES - READ CAREFULLY:
The first reference image is the state of the room at 0s. The second reference image is the state of the room at 6s. These are two discrete states, NOT two ends of a blend. Do not interpolate between them. Do not cross-fade, morph, or gradually transform the first image into the second. Do not compute intermediate frames by mixing the two images together. Instead, the first image stays exactly as it is, unchanged, and the objects from the second image are placed onto it one group at a time until the second image is complete. At every moment the frame shows the first image plus whichever objects have already arrived, never a partial blend of the two.
```

**Strict Object Inventory:**

```
STRICT OBJECT INVENTORY - NOTHING NEW:
The complete and final set of objects is defined entirely by the second reference image. Every object that appears must already be visible in the second reference image, in the same position, at the same scale, in the same orientation, in the same material, colour, and finish. Do not add, invent, substitute, duplicate, restyle, or embellish anything. No extra furniture, no extra cushions, no extra plants, no extra decor, no styling props, no additional lamps, no rugs, no artwork, no books, no bottles, no flowers, no candles, no trays, no towels, and no accessories beyond exactly what the second reference image shows. If an object is absent from the second reference image, it must never appear at any point in the video.
```

**Architecture Lock:**

```
ABSOLUTE LOCK:
All architecture, walls, ceilings, structures, openings, built-in surfaces, floor patterns, and lighting direction are identical in both reference images and must stay identical for the entire 8 seconds, never redrawn, warped, shifted, or reinterpreted.
```

**Reveal Method:**

```
REVEAL METHOD - MIXED MOTION:
Objects arrive in groups using different movements suited to their type, never all the same way. Every object is fully opaque, complete, and correctly proportioned from the first frame it is visible. An object either does not exist yet or exists fully, there is no in-between state for any object.

Each arrival takes about 0.2 to 0.3 seconds. Objects travel only a short distance, no long flight paths, no crossing the frame. Contact shadows appear the moment an object lands or pops.
```

**Standard Negative Prompt:**

```
Negative: changing camera angle, changing perspective, new viewpoint, reframing, re-angling, rotating camera, orbiting, arc shot, crane move, changing camera height, changing focal length, changing field of view, lens distortion, wide angle shift, perspective warp, shifting vanishing point, tilting horizon, revealing unseen areas of the room, added furniture, extra furniture, invented objects, new decor, additional props, styling props, duplicated objects, restyled furniture, changed furniture colour, changed furniture material, objects not present in the reference, interpolation between reference images, blending two images, image morph, cross-fade between frames, gradual transformation, morphing, object morphing, shape shifting, transforming, geometry changing, slow growth, gradual scaling, growing from zero, unfolding, assembling from parts, dissolving in, fading in, transparency, ghost objects, semi-transparent, floating objects, levitating, flying across frame, sliding across frame, people, humans, animals.
```

---

## Implementation Blueprint 1: Warm Minimalist Wood Bedroom

### Step 1: Nano Banana Object Removal Prompt

```
Remove only the loose furniture and decor from this bedroom. Remove the light wood bed frame, mattress, pillows, duvet, beige throw blanket, woven area rug, two matching wood bedside nightstands, two table lamps, three-drawer wood dresser, round wall mirror, vase with dried grass, perfume bottles on the tray, large light wood wardrobe with mirrored doors, small potted plant on the nightstand, and the two framed landscape art prints on the wall.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep all beige plaster walls, ceiling, sheer white window curtain on the left, recessed ceiling spotlight, and light wood plank flooring completely unchanged. Fill emptied areas with clean matching plaster and flooring in the same materials already visible. Same warm natural daylight lighting, same shadow direction, same time of day.
```

### Step 2: Omni Flash Animation Prompt (8 Seconds)

```
[Insert Core Master Script sections: Camera Lock, Reference Usage, Object Inventory, Architecture Lock, Reveal Method]

TIMELINE:
0-2s: The frame is exactly the first reference image, unchanged. Camera begins its slow drift. Room is completely empty of loose furniture.

2-3.5s: The light wood bed frame arrives via POP-IN; the large mirrored wardrobe, three-drawer dresser, and two nightstands DROP into position. Everything else in the frame is unchanged.

3.5-5s: The two framed landscape art prints and round wall mirror DESCEND to final height on the wall; twin table lamps DROP onto nightstands. Everything else is unchanged.

5-6s: Woven area rug, mattress, pillows, duvet, and beige throw blanket SETTLE; vase with dried grass, tray with bottles, books, and small plant appear INSTANT; all contact shadows land; camera drift eases to a stop. The frame now equals the second reference image exactly.

6-8s: The frame is exactly the second reference image, completely static, no new objects, no repositioning, no further changes. Only stable ambient warm light.

Photorealistic architectural interior photography, natural daylight, no people.

[Insert Standard Negative Prompt]
```

---

## Implementation Blueprint 2: Tropical Spa Bathroom

### Step 1: Nano Banana Object Removal Prompt

```
Remove only the loose furniture and decor from this tropical modern bathroom. Remove the freestanding white oval bathtub, chrome floor faucet, grey bath mat rug, large potted tropical broadleaf plants in ceramic planters, smaller potted plants near the glass divider, and small decorative items.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep all beige wall tiles, wood slat ceiling with recessed spotlights, glass sliding doors leading to the garden on the left, glass shower partition, wall-hung white toilet, backlit wall niche on the right, and light beige tiled flooring completely unchanged. Fill emptied areas with clean matching tile and wall textures in the same materials already visible. Same warm natural sunlight streaming in, same shadow direction, same time of day.
```

### Step 2: Omni Flash Animation Prompt (8 Seconds)

```
[Insert Core Master Script sections: Camera Lock, Reference Usage, Object Inventory, Architecture Lock, Reveal Method]

TIMELINE:
0-2s: The frame is exactly the first reference image, unchanged. Camera begins its slow drift. The bathroom space is completely empty of loose objects.

2-3.5s: The freestanding white oval bathtub arrives centered via POP-IN; the large potted tropical plants DROP into position on the left and right. Everything else in the frame is unchanged.

3.5-5s: Standing floor faucet and secondary smaller potted greenery arrive into place. Everything else is unchanged.

5-6s: Grey bath mat rug SETTLES onto the floor; small accessories appear INSTANT; all contact shadows land; camera drift eases to a stop. The frame now equals the second reference image exactly.

6-8s: The frame is exactly the second reference image, completely static, no new objects, no repositioning, no further changes. Only gentle leaf movement on the potted plants and stable sunlight.

Photorealistic architectural interior photography, natural daylight, no people.

[Insert Standard Negative Prompt]
```

---

## Implementation Blueprint 3: Modern Luxury Villa Pool Patio

### Step 1: Nano Banana Object Removal Prompt

```
Remove only the loose furniture and decor from this outdoor pool patio. Remove all beige cushioned sun loungers, woven rattan daybeds, low lounge chairs, side tables, small rugs, and decorative seating on the patio deck.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep all minimalist beige villa walls, cantilevered concrete overhangs, glass sliding doors, stone privacy walls in the background, surrounding trees and shrubs, natural rock boulders at the pool edge, and light beige stone deck tiles completely unchanged. Empty the swimming pool completely of water and show a dry bare basin. Keep the pool shape and coping edge unchanged. Fill emptied areas with clean matching tile and stone textures in the same materials already visible. Same bright clear daylight lighting, same shadow direction, same time of day.
```

### Step 2: Omni Flash Animation Prompt (8 Seconds)

```
[Insert Core Master Script sections: Camera Lock, Reference Usage, Object Inventory, Architecture Lock, Reveal Method]

TIMELINE:
0-2s: The frame is exactly the first reference image, unchanged. Camera begins its slow drift. FILL runs here: clear water rises smoothly from the bottom of the empty pool until it reaches the coping edge and settles into gentle ripples.

2-3.5s: The beige cushioned sun loungers and large daybeds arrive along the pool deck via POP-IN; rattan lounge chairs DROP into position. Everything else in the frame is unchanged.

3.5-5s: Secondary patio seating, background outdoor chairs, and low tables DROP into position. Everything else is unchanged.

5-6s: Outdoor cushions and mats SETTLE onto surfaces; all contact shadows land; camera drift eases to a stop. The frame now equals the second reference image exactly.

6-8s: The frame is exactly the second reference image, completely static, no new objects, no repositioning, no further changes. Only faint water ripples and stable ambient daylight.

Photorealistic architectural exterior photography, natural daylight, no people.

[Insert Standard Negative Prompt]
```

---

## Implementation Blueprint 4: Japandi Floating Console Living Room

### Step 1: Nano Banana Object Removal Prompt

```
Remove only the loose furniture and decor from this room. Remove the cream sofa, cushions, round wooden coffee table, white ceramic vases, small ceramic bowls, books, white vase with dried pampas grass, floating wooden TV console, large wall-mounted TV screen, indoor potted green tree in a woven basket, and woven area rug.

Keep everything else exactly as it is: identical camera angle, identical field of view, identical crop, identical framing. Keep all warm beige plaster walls, ceiling, sheer white window curtains on the left, and light wood flooring completely unchanged. Fill emptied areas with clean matching plaster and flooring in the same materials already visible. Same soft natural daylight lighting, same shadow direction, same time of day.
```

### Step 2: Omni Flash Animation Prompt (8 Seconds)

```
[Insert Core Master Script sections: Camera Lock, Reference Usage, Object Inventory, Architecture Lock, Reveal Method]

TIMELINE:
0-2s: The frame is exactly the first reference image, unchanged. Camera begins its slow drift. The room is completely empty of loose furniture.

2-3.5s: The cream sofa and round wooden coffee table arrive via POP-IN; the potted tree in a basket and floating wooden TV console DROP into position. Everything else in the frame is unchanged.

3.5-5s: Large wall-mounted TV screen with landscape art DESCENDS to final height on the main wall. Everything else is unchanged.

5-6s: Woven area rug and cushions SETTLE onto their surfaces; white ceramic vases, books, dried pampas grass, and tabletop bowls appear INSTANT; all contact shadows land; camera drift eases to a stop. The frame now equals the second reference image exactly.

6-8s: The frame is exactly the second reference image, completely static, no new objects, no repositioning, no further changes. Only faint ambient daylight stability.

Photorealistic architectural interior photography, natural daylight, no people.

[Insert Standard Negative Prompt]
```

---

## Technical Requirements

### Tools Required

- **Nano Banana** - AI object removal tool
- **Omni Flash (pollo.ai)** - 8-second AI video generation platform

### Key Success Factors

1. **Identical Framing:** Empty and furnished images must have perfectly matching camera angles and crops
2. **Structural Preservation:** Never remove built-in architectural elements
3. **Discrete States:** Avoid morphing/blending between reference images
4. **Physics-Based Motion:** Use appropriate motion types for each furniture category
5. **Timeline Discipline:** Follow strict 0-2s empty, 2-6s reveal, 6-8s static structure
6. **Object Fidelity:** Only animate objects visible in the furnished reference

## Usage Notes

- Perfect for real estate marketing videos
- Creates high-end luxury property presentations
- 8-second duration ideal for social media and property listings
- Works for interior and exterior spaces
- Requires two high-quality reference images per animation
- Camera lock is critical - no reframing or perspective changes
- Motion types should match furniture weight and mounting type

## File Under

- Video prompts
- Real estate marketing
- Interior visualization
- Furniture reveal
- AI video generation
- Architecture animation
- Property presentation
- Luxury staging
