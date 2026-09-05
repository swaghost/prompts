# 04 — Location Board (Environment & Set Multi-Angle Reference)

**Purpose:** Generate a multi-panel reference showing the same environment from multiple camera positions  
**Use Case:** Locks spatial layout, lighting and set dressing for multi-shot sequences in the same location  
**Platform:** GPT Image 2, Picsart Flow

## What This Builder Does

Creates a composite image with the same environment shown from wide establishing, medium walk-through, tight corner detail and aerial/overhead views. All panels share identical architecture, lighting, color palette and props — only the camera position changes.

This prevents the "room changes shape between shots" problem and ensures furniture, windows, lighting fixtures and wall colors stay consistent across cuts.

## Template Prompt

```
[PASTE YOUR STYLE BIBLE HERE]

Location reference sheet, multi-panel composite showing the SAME environment from multiple camera positions, evenly spaced with thin white gutters between panels. NO PEOPLE in any panel.

ENVIRONMENT: [Detailed description — type of space, era/style, architecture, dimensions, floor/wall/ceiling materials, color palette, lighting sources, key furniture/props, condition/wear, mood]

LIGHTING: [Describe light sources, color temperature, direction, time of day, natural vs artificial, shadow quality]

PANELS (all panels show the same room with identical layout, dressing and lighting):

Panel 1 — WIDE ESTABLISHING: Wide-angle shot (24mm equivalent), camera at standing chest height, positioned to show maximum spatial depth and layout, full room visible with foreground, mid-ground and background elements, strong perspective leading to vanishing point.

Panel 2 — MEDIUM WALK-THROUGH: Standard lens (35-50mm), camera at eye height walking down central path through space, showing environment at human scale, key furniture and props in mid-ground, natural eyeline view.

Panel 3 — TIGHT CORNER DETAIL: Tighter framing (50-85mm), camera at seated eye height, focused on specific corner or vignette within the space, showing texture detail on walls/surfaces, props and set dressing at close range.

Panel 4 — AERIAL OVERHEAD: Camera directly overhead looking straight down, showing floor plan layout, furniture placement, spatial relationships, symmetry or asymmetry of the space, even overhead lighting.

Panel 5 — LOW ANGLE / HIGH ANGLE [choose one]: [Low: camera near floor looking up, emphasizing ceiling and verticality] OR [High: camera elevated looking down at 45°, showing depth and layers].

CRITICAL: Identical environment, identical furniture placement, identical wall/floor materials, identical lighting color and intensity across all five panels. Only camera position and lens change. Photorealistic, accurate architectural scale, realistic material textures (wood grain, fabric weave, tile grout), natural lighting behavior, no people, no text overlays.
```

## Example: 1990s American Diner Interior

```
Photorealistic 1990s American cinema aesthetic with heavy 35mm film grain and soft halation around highlights. Warm tungsten interior lighting mixed with cool daylight through windows, saturated red and blue neon accents. Palette built on deep reds, black, chrome silver, white tile, checkered floor contrast. Textures emphasize worn vinyl, scuffed laminate, polished chrome. Mood is nostalgic, cinematic, quiet before action.

Location reference sheet, multi-panel composite showing the SAME 1990s American diner interior from multiple camera positions, evenly spaced with thin white gutters between panels. NO PEOPLE in any panel.

ENVIRONMENT: Classic American roadside diner, rectangular space approximately 40 feet deep by 20 feet wide, black-and-white checkered vinyl floor tile with slight wear and scuff marks, rows of deep red buttoned vinyl booths along the left wall beneath large plate-glass windows with thin metal venetian blinds, laminate tables with chrome-edge trim, long laminate service counter with chrome-stemmed red vinyl stools on the right, pressed tin ceiling with subtle metallic sheen, wood-paneled lower walls in dark walnut stain, upper walls in cream paint. Set dressing: stainless napkin dispensers and red squeeze ketchup bottles on each table, glass pie case behind counter, stacked white ceramic mugs, framed black-and-white photographs on walls.

LIGHTING: Mid-afternoon, warm tungsten from ribbed glass pendant lamps down the left side casting pools of amber light, cool daylight bleeding through venetian blinds on left creating striped shadow patterns, red neon rectangle glowing on rear wall, blue neon script sign on right wall above counter, all neon has soft halation glow. Deep shadows under booths and counter, high contrast between lit and shadow areas.

PANELS (all panels show the same diner with identical layout and lighting):

Panel 1 — WIDE ESTABLISHING: Wide-angle 24mm lens, camera at standing chest height positioned at the near end of the aisle, looking straight down the length of the room with strong one-point perspective, booths receding on the left, counter and stools on the right, checkered floor leading to vanishing point at rear wall with glowing red neon, full spatial depth visible.

Panel 2 — MEDIUM WALK-THROUGH: 35mm lens, camera at standing eye height in the centre aisle midway through the room, looking toward the rear, booths in mid-ground on left, counter in mid-ground on right, pendant lights overhead, warm tungsten pools on tables, human-scale view showing environment at natural walking perspective.

Panel 3 — TIGHT CORNER DETAIL: 50mm lens, camera at seated booth eye height, focused on a single booth vignette in the left foreground, showing red vinyl seat back with button detail, chrome table edge, napkin dispenser and ketchup bottle on laminate surface, window with blinds and daylight in soft background bokeh, texture detail visible on vinyl and chrome.

Panel 4 — AERIAL OVERHEAD: Camera directly above looking straight down, showing rectangular floor plan layout with checkered tile pattern, booth arrangement in parallel rows on left side, counter running down right side with stools, spatial symmetry and furniture placement clear, even overhead lighting showing full plan view.

Panel 5 — LOW ANGLE: Camera at floor level near the front entrance, looking up and down the aisle, emphasizing pressed tin ceiling with pendant lights overhead, vertical booth backs rising on left, counter rising on right, checkered floor receding in strong perspective, dramatic verticality and depth.

CRITICAL: Identical diner layout, identical booth count and placement, identical counter and stool arrangement, identical neon signs (same position and color), identical pendant light positions, identical checkered floor pattern across all five panels. Only camera position and lens focal length change. Photorealistic, visible vinyl texture and button stitching, realistic chrome reflections, accurate wood grain, natural light behavior with halation around neon, heavy 35mm grain, no people, no overlays.
```

## Builder Variables

**Environment Variables (Customize These):**

- Type of space (diner, apartment, office, warehouse, forest clearing, alley, rooftop, etc.)
- Era/period (1920s, 1970s, contemporary, futuristic, etc.)
- Architectural style (mid-century modern, industrial, Victorian, minimalist, etc.)
- Dimensions and scale (intimate, expansive, narrow, cavernous, etc.)
- Floor material (tile, wood, concrete, carpet, dirt, etc.)
- Wall treatment (paint, wallpaper, brick, plaster, paneling, etc.)
- Ceiling (exposed beams, drop tiles, vaulted, pressed tin, etc.)
- Color palette (3-5 dominant colors)
- Condition (pristine, lived-in, worn, abandoned, weathered, etc.)

**Lighting Variables:**

- Time of day (dawn, midday, golden hour, night)
- Natural light (window direction, quality, intensity)
- Artificial sources (pendant, neon, fluorescent, candles, practicals)
- Color temperature mix (warm tungsten + cool daylight, single temp, etc.)
- Shadow quality (hard, soft, dappled, dramatic, flat)
- Special lighting (neon glow, firelight, backlighting, rim light)

**Set Dressing & Props:**

- Furniture (tables, chairs, shelves, counter, etc.)
- Practical objects (books, bottles, tools, electronics, plants, etc.)
- Wall decoration (frames, posters, mirrors, signage, etc.)
- Wear details (scuffs, stains, patina, cracks, dust, etc.)

## Usage Tips

- **Dimensions matter** — "40 feet deep by 20 feet wide" gives spatial constraint; without it, room can morph
- **Count repeating elements** — "Rows of booths" becomes "five booths in a row" to prevent booth-count drift
- **Lighting as anchor** — "Red neon rectangle on rear wall" should appear in same spot across all angles
- **Say "NO PEOPLE" twice** — Once at top, once at bottom; location plates with characters bake in wrong poses
- **Wide first, tight last** — Panel order from establishing → detail mirrors film grammar, helps model build context

## Integration with Video

Upload to Topview Canvas, name @location_diner (or similar), reference in video prompt:

```
REFERENCES: Use @location_diner for the diner interior throughout. Layout, booth count, neon placement, floor pattern and lighting must exactly match @location_diner across all shots.

0-4s: [Wide Shot matching @location_diner panel 1] Camera slowly pushes forward down the aisle. Empty diner, warm tungsten glow, checkered floor receding toward red neon on rear wall.

12-16s: [Medium Shot matching @location_diner panel 2] Character walks through the space at human eye level, booths on left, counter on right, pendant lights overhead.
```

The video model knows the room from multiple angles before animating action inside it.

## When to Use This Builder

✅ **Use Location Board when:**

- Multiple shots take place in the same interior or exterior space
- Camera moves through environment (dolly, tracking, orbit)
- Scene requires spatial continuity across cuts
- Lighting setup is complex and must stay consistent
- Architecture/layout is critical to story or action

❌ **Don't use Location Board when:**

- Location only appears in one shot
- Each shot is a different location (make separate boards)
- You need character + environment together (generate separately, reference both)
- Space is generic or unimportant to scene

---

**Builder:** Location Board (Environment multi-angle reference)  
**Panels:** 5 views (wide, medium, tight detail, aerial, low/high angle)  
**Consistency Anchor:** Identical layout, dressing and lighting; only camera position changes
