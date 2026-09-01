# Music-Cover Flight Guide

## Purpose

Animate a square, wide, or collage-style music cover with one smooth continuous aerial camera flight while keeping the artwork itself completely static and unchanged.

## Requirements

- **Base image:** Music cover, photo, artwork, or AI frame. Square (1:1) works well.
- **Annotation:** One red line drawn directly on the cover for the camera route.
- **Viewing guides:** Two or three white arrows placed along the red line to show camera viewing direction.
- **Video tool:** Google Flow with the Omni Flash model.
- **Mode:** Single Continuous.

## Two-Line System

- **Red line:** Camera flight waypoints and trajectory, including curves, direction, and endpoint.
- **White arrows:** Camera viewing direction at the start, middle, and end of the route.
- **Guides vanish:** Red and white marks are production guides only. They must be removed before animation begins and must never appear in the finished footage.

## Workflow

### Step 1: Draw the Path

1. Open the cover as an image.
2. Draw one continuous red flight route with curves, direction of travel, and endpoint.
3. Add two or three white arrows along the route from start to middle to end.
4. Point the arrows in the intended viewing direction and keep the main subject in frame.

### Step 2: Generate in Flow

1. Open Google Flow and select Omni Flash.
2. Upload the annotated cover.
3. Paste the prompt below.
4. Select **Single Continuous**.
5. Generate and inspect the result for guide removal, static artwork, camera continuity, and framing.

## Universal Video Sequence Prompt

```text
Use the attached image as the starting frame: a single flat, static 2D artwork.

The red line represents the camera flight waypoints and trajectory. The white arrows represent the camera viewing direction. These are production guides, not scene elements. Remove all guides before the animation begins and reveal the clean artwork underneath.

HARD RULE - the artwork stays unchanged. The cover remains the SAME flat picture in every frame. Nothing inside it moves, separates, morphs, animates, re-animates, or changes position. Do not add objects.

Camera POV: create one continuous aerial flight along the exact path defined by the red line:
[INSERT PATH: Start -> Curve -> Key elements -> Endpoint]

Match the route, curves, direction, and endpoint as closely as possible. Throughout the flight, orient the camera according to the white arrows and keep the artwork's main subject framed at all times.

Motion: smooth, cinematic, and physically believable, with realistic inertia, gentle banking, natural acceleration, and natural deceleration. No cuts, edits, teleports, sudden swings, or discontinuities. No vehicle, drone, or camera body is ever visible; show only the flying point of view.

Preserve the artwork exactly: colors, subjects, typography, composition, lighting, and texture must remain unchanged.

Produce clean, realistic footage with no visible guides, red lines, white arrows, overlays, graphics, extra text, or watermarks in any frame.
```

## Path Examples

- **Horizontal or wide cover:** Use a horizontal route with the subject centered.
- **Square cover:** Use a circular loop or diagonal route.
- **Complex collage:** Name the key visual elements in the path block in the order the camera should pass them.

## Troubleshooting Rules

- Never describe a physical drone in the prompt; use **POV camera** and **no vehicle visible**.
- If the artwork changes, strengthen the static-artwork hard rule and regenerate.
- If the camera loses the subject, add the subject's location to the path and viewing-direction description.
- If the guides remain visible, state that they are temporary production annotations that must be erased before frame one.
- If the route jumps, simplify it to one continuous line with fewer waypoints.
- Covers using real artists, albums, or copyrighted characters may trigger platform restrictions. Use an original or invented cover in the desired visual style when necessary.
