# 03 — Object Board (Product & Prop Multi-Angle Reference)

**Purpose:** Generate a multi-panel reference showing the same object/product from multiple angles  
**Use Case:** Product close-ups, hero prop shots, or any video where an object needs to stay consistent across cuts  
**Platform:** GPT Image 2, Picsart Flow

## What This Builder Does

Creates a composite image with the same object shown from front, top, side, three-quarter and detail views. All panels use identical lighting, material properties and scale — only the camera position changes.

This ensures texture, shape, branding and wear patterns stay consistent when the object is filmed from different angles or held/manipulated by characters.

## Template Prompt

```
[PASTE YOUR STYLE BIBLE HERE]

Product reference sheet, multi-panel composite showing the SAME object from multiple camera angles, evenly spaced with thin white gutters between panels.

OBJECT: [Detailed description — type, shape, size, material, color, texture, surface finish, branding, wear/age, distinguishing marks]

LIGHTING & SETUP: Clean studio lighting with soft frontal key and gentle fill from above, flat off-white seamless background, consistent lighting direction and intensity across all panels, no harsh shadows on background, gentle ambient occlusion shadows under object only.

PANELS (all panels show the same object with identical materials and finish):

Panel 1 — FRONT VIEW: Object centered, camera at object's mid-height, straight-on frontal view showing primary face/surface, shot with 50mm lens, shallow depth of field with sharp focus on object, background softly blurred.

Panel 2 — TOP-DOWN VIEW: Object centered, camera directly overhead looking down, showing top surface and plan view, even lighting, object fills 70% of frame with margin around edges.

Panel 3 — SIDE VIEW (LEFT): Object centered, camera at object's mid-height, 90° profile showing left side, orthographic-style view with parallel lines, object in sharp focus.

Panel 4 — THREE-QUARTER VIEW: Object centered, camera at 45° angle from front-left and slightly above, showing depth and dimensional form, classic product photography angle, soft highlight on top edge.

Panel 5 — DETAIL CLOSE-UP: Extreme macro view of [specific detail — logo, texture, mechanism, edge, surface pattern], shallow depth of field, sharp focus on detail with background falling away, shot with macro lens.

CRITICAL: Identical object, identical material properties (color, texture, reflectivity, wear), identical branding/markings across all five panels. Only camera position changes. Photorealistic, accurate material rendering, visible surface texture, realistic reflections and specularity where appropriate, no inconsistent damage or wear between views.
```

## Example: Vintage Film Camera

```
Photorealistic product photography aesthetic with clean studio lighting and natural material rendering. Neutral color palette, accurate metal and leather texture, soft shadows. Mood is heritage craftsmanship, tangible and authentic.

Product reference sheet, multi-panel composite showing the SAME vintage 35mm film camera from multiple camera angles, evenly spaced with thin white gutters between panels.

OBJECT: Classic 35mm film rangefinder camera, circa 1960s, compact rectangular body in matte black painted aluminum with visible edge wear revealing silver metal underneath, black vulcanite textured leather covering on front and back panels with fine crosshatch pattern, chrome top plate with engraved depth-of-field scale, collapsible 50mm f/2 lens in chrome barrel with black focus ring, small red shutter button on top right, mechanical film advance lever in chrome, serial number engraved on top plate, honest age with minor scuffs but not damaged.

LIGHTING & SETUP: Clean studio lighting with soft frontal key and gentle overhead fill, flat off-white seamless background, consistent soft directionality across all panels, no harsh reflections on chrome, gentle ambient occlusion shadow under camera only.

PANELS (all panels show the same camera with identical wear and finish):

Panel 1 — FRONT VIEW: Camera centered, lens facing directly toward viewer, camera at lens height, frontal view showing lens barrel, vulcanite grip texture, top plate controls, shot with 50mm lens at f/4, shallow depth of field sharp on lens glass, background softly blurred.

Panel 2 — TOP-DOWN VIEW: Camera centered, overhead shot looking straight down, showing top plate with shutter button, film advance lever, rewind knob, accessory shoe, engraved depth scale, camera body outline, even lighting, fills 70% of frame.

Panel 3 — SIDE VIEW (LEFT): Camera centered, 90° left side profile, showing body depth, lens barrel extension, film advance lever, vulcanite side panel texture, strap lug, orthographic-style clean side view, sharp focus throughout.

Panel 4 — THREE-QUARTER VIEW: Camera centered, shot from 45° front-left and slightly above, lens angled toward viewer, showing dimensional form and body depth, classic product photography angle, soft highlight on chrome top plate edge, gentle shadow under base.

Panel 5 — DETAIL CLOSE-UP: Extreme macro of the front lens element, showing circular glass surface with multicoating (subtle purple-blue reflections), aperture blades visible inside, engraved focal length marking on chrome barrel, shallow depth of field, shot with 100mm macro lens, razor-sharp on glass.

CRITICAL: Identical camera body, identical edge wear pattern (silver showing through black paint in same locations), identical vulcanite texture, identical chrome finish across all five panels. Only camera position changes. Photorealistic, accurate metal and leather material, visible texture grain in vulcanite, realistic reflections on chrome and lens glass, consistent age and wear.
```

## Builder Variables

**Object Variables (Customize These):**

- Object type (product, prop, tool, device, package, etc.)
- Size and proportions (compact, oversized, elongated, etc.)
- Primary material (metal, plastic, wood, glass, ceramic, fabric, leather)
- Surface finish (matte, glossy, brushed, polished, textured, coated)
- Color palette (primary color + accent colors)
- Texture detail (smooth, rough, grained, pebbled, woven, etc.)
- Branding (logos, type, labels, engravings, embossed marks)
- Condition (new, vintage, worn, weathered, pristine, distressed)
- Distinguishing marks (scratches, patina, dents, stickers, serial numbers)

**Detail Close-Up Options (Panel 5):**

- Logo or brand mark
- Surface texture or material grain
- Mechanical detail (hinge, clasp, button, dial)
- Edge or seam construction
- Label or engraving
- Wear pattern or patina
- Transparent/translucent element (glass, lens, screen)

## Usage Tips

- **Name materials explicitly** — "Matte black painted aluminum" beats "black metal"
- **Describe wear specifically** — "Edge wear revealing silver underneath" gives model permission to show age without random damage
- **Lighting = material** — Soft light for matte surfaces, harder light for glossy/chrome to show specularity
- **Detail close-up should reveal texture** — Macro shot proves material is real (grain, weave, pores)
- **Orthographic side view** — Saying "orthographic-style" or "parallel lines" prevents perspective distortion on technical views

## Integration with Video

Upload to Topview Canvas, name @prop_camera (or similar), reference in video prompt:

```
REFERENCES: Use @prop_camera for the vintage film camera's appearance. Material, wear pattern, chrome finish and branding must exactly match @prop_camera across all shots.

8-12s: [Macro Shot] Camera slowly tilts down as character's hands rotate the vintage camera, revealing the lens from @prop_camera panel 1, then the top controls from @prop_camera panel 2. Lighting emphasizes chrome highlights.
```

The video model maintains consistent material properties as the object rotates.

## When to Use This Builder

✅ **Use Object Board when:**

- Product is hero element in video (unboxing, review, commercial)
- Prop is handled/manipulated by character (needs consistent look from all angles)
- Close-up shots require texture and material detail
- Object has branding that must stay consistent
- Multiple shots feature the same item (watch, phone, bottle, tool, etc.)

❌ **Don't use Object Board when:**

- Object only appears briefly in background
- You need object + character together (generate separately, composite in video)
- Object changes state during video (full glass → empty glass = two separate boards)
- Scene has multiple similar objects (generate separate boards per unique item)

---

**Builder:** Object Board (Product/prop multi-angle reference)  
**Panels:** 5 views (front, top, side, three-quarter, macro detail)  
**Consistency Anchor:** Identical object and materials; only camera angle changes
