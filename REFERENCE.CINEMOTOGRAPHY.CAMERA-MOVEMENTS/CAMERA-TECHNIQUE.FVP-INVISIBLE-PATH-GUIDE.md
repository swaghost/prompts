# FVP Invisible Path Camera-Movement Guide

## Purpose

Use annotated reference images to direct a smooth cinematic camera movement while ensuring the path, arrow, dot, and glow guides remain invisible in the final video.

## FVP Guide Rules

- The neon-green FVP line, arrow, start point, endpoint, dot, and glow are camera-direction data only.
- Never render, animate, or reveal the guides in the first frame or any later frame.
- Preserve the supplied reference image as the sole visual source for subject identity, wardrobe, architecture, props, lighting, and environment.
- Keep the camera move continuous and physically coherent.
- Use foreground occlusion and parallax deliberately, but do not let them obscure the subject's identity or distort the scene.
- End on the specified framing and subject anchor.
- Exclude text, captions, logos, branding, overlays, UI, and interface graphics.

## Prompt Structure

1. **Reference lock:** State that the attached image is the only visual reference and list what must remain unchanged.
2. **Subject motion:** Describe natural movement, cloth, hair, fire, smoke, reflections, or environmental motion.
3. **FVP camera movement:** State the starting position, path shape, direction, elevation, foreground occlusion, parallax, and final framing.
4. **Guide suppression:** Explicitly ban the neon-green line, arrow, dot, glow, path, and tracking graphic.
5. **Output constraints:** State duration, cinematic quality, continuity, and forbidden overlays.

## Reusable Template

```text
Use @image [NUMBER] as the only visual reference and preserve the exact [SUBJECT, IDENTITY, WARDROBE, PROPS, ENVIRONMENT, LIGHTING AND COMPOSITION].

Create an [DURATION]-second [STYLE] image-to-video shot. [DESCRIBE NATURAL SUBJECT AND ENVIRONMENT MOTION].

### FVP Camera Movement

Start [START POSITION]. Follow a smooth [PATH SHAPE] from [START] through [KEY WAYPOINTS] and finish with [FINAL FRAMING]. Maintain [PARALLAX/OCCLUSION/DEPTH REQUIREMENTS]. The movement must feel like one continuous professional motion-control camera shot.

The neon-green FVP line, arrow, start point, endpoint, dot, glow, path, tracking guide, and any guide graphics are invisible camera instructions only. Do not show, reproduce, animate, or display them in any frame. No text, captions, logos, branding, overlays, or interface elements.
```

## Movement Types Covered

- Spiral path around a foreground object and subject
- Clockwise circular orbit around a couple or seated subject
- Horizontal orbit with close foreground occlusion
- Wide elliptical orbit with a final profile reveal
