Adding telestrator graphics, vector arrows, and spotlight rings onto AI-generated soccer video clips bridges the gap between raw visual generation and professional tactical analysis (ideal for platforms like soccr.org). Because AI-generated clips can occasionally feature subtle camera drift or dynamic lighting shifts, standard editing rules require a few specialized adjustments.

---

## 1. Prepare AI Video Assets for Graphic Tracking

Before dropping graphics onto AI video, ensure the source footage is optimized for motion tracking:

- **Bake In Stability Commands:** Always use stabilizing slash commands (`/overhead`, `/deepfocus`, `/steadicam`) in Google Flow. High-angle static shots or linear dolly movements create clean feature points for video editors to track.
- **Avoid Aggressive Lens Distortion:** Steer clear of `/wideangle` or extreme `/vignette` on clips intended for precise telestration; barrel distortion bends straight passing vectors into unnatural curves.
- **Pre-Render Stabilized Passes:** If your AI clip has slight micro-jitter or warping, run a subtle 3D camera warp stabilizer in your editor (Premiere Pro, DaVinci Resolve, or Final Cut) _before_ attaching graphics.

---

## 2. Graphic Overlay Design Principles

Tactical graphics should enhance understanding without cluttering the visual frame.

### Color Coding Standards

- **Attacking Passing Vectors:** Glowing Cyan or Bright Yellow (`#00FFFF` / `#FFFF00`) for high contrast against green turf.
- **Defensive Movement & Press Lines:** Crimson or Neon Coral (`#FF3366`).
- **Open Spatial Zones:** Semi-transparent White or Amber heatmaps (`30%–40% opacity`).
- **Player Spotlight Rings:** Solid White or Gold rings anchored around the player’s feet.

### Geometry & Perspective Alignment

- **Match the Pitch Angle:** Never lay flat 2D lines over a 3D perspective shot. Use 3D plane mapping (or corner-pinning) so vector arrows lie flat on the grass plane, conforming to the pitch's vanishing points.
- **Stroke & Glow Layering:** Give vector arrows a subtle dark drop-shadow (or 2-pixel black border) and a soft outer glow. This prevents graphics from bleeding into bright stadium floodlights or light-colored jerseys.

---

## 3. Step-by-Step Telestration Workflow

### Phase A: Spatial & Player Spotlights (Freeze or Slow-Mo)

1. **The Freeze Frame Hook:** When the key tactical moment occurs (e.g., a midfielder turning into open space), pause the AI footage for 1.5–2 seconds.
2. **Anchor the Player Ring:** Animate a spotlight ring scaling up around the key player's cleats.
3. **Occlusion Masking (The Pro Touch):** If another player or ball passes _in front_ of your telestrator line, mask out that segment of the graphic. Having the arrow sit _behind_ a player's leg rather than plastered over top makes the overlay feel embedded in the actual 3D environment.

### Phase B: Dynamic Vector Tracking (Motion)

1. **Planar Motion Tracking:** Track the pitch surface (using point tracking or planar tracking like Mocha) rather than the player. This anchors passing lines and shaded spatial boxes directly to the grass grid.
2. **Path Animation:** Animate vector lines drawing forward in sync with the ball or player sprint (using write-on path effects or trim paths in After Effects).
3. **Space Shading:** To highlight an open pocket (e.g., the half-space), draw a 4-point polygon anchored to pitch markers, filling it with a 25% opacity colored accent.

---

## 4. Recommended Software Stack

| Tool / Software                 | Best Used For                               | Key Feature for AI Video                                                     |
| ------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------- |
| **DaVinci Resolve (Fusion)**    | Advanced planar tracking & 3D space mapping | Built-in planar tracker locks arrows flat to AI turf effortlessly.           |
| **Adobe After Effects**         | Motion graphics, trim paths, glow effects   | Mocha AE plugin handles complex camera motion tracking.                      |
| **ScreenFlow / Camtasia**       | Rapid tactical coaching commentary          | Quick built-in arrow/circle tools for lightweight tutorial creation.         |
| **CoachPaint / Keyframe Alpha** | Dedicated sports graphics software          | Specialized sports telestrator tools with automatic field-plane recognition. |

---

## Example Sequence Layout

```text
[0:00 - 0:02] AI Video Runs at 100% Speed (Midfielder receives ball)
                     ↓
[0:02 - 0:04] FREEZE FRAME / SLOW-MO (10% Speed)
  ├── 1. White Spotlight Ring expands around Midfielder (Player Anchor)
  ├── 2. Shaded Amber Zone fills the half-space channel (Space Highlight)
  └── 3. Cyan Arrow draws along the run path of the Winger (Vector Target)
                     ↓
[0:04 - 0:07] AI Video Resumes at 100% Speed (Pass is delivered along the drawn vector line)

```
