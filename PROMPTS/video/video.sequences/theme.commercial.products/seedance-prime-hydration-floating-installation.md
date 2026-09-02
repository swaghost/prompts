# Seedance 2.5 - Prime Hydration Floating Product Installation

## Description of Resulting Video or Video Sequence

A 5-second vertical commercial showing five exact Prime Hydration bottles suspended motionless in a modern city canyon while the camera glides forward through the crowd. Camera parallax supplies all apparent object movement; every bottle remains fixed in count, tilt, color, and product identity.

## Usage

Perfect for beverage launches, sports-drink advertising, urban product installations, and social-first commercial content. Ideal for depth-map workflows where a product must occupy several spatial layers without spinning, tumbling, or changing design. The sequence creates a graphic hero arrangement that resolves on one readable front-facing bottle.

## Engines/Models

- **Video model:** Seedance 2.5
- **Interface:** CapCut Web or compatible Seedance workflow
- **Duration:** 5 seconds
- **Frame rate:** 30fps
- **Aspect ratio:** 9:16

## Prerequisites / Dependencies

- **@DEPTH:** Uploaded depth-map video; sole geometry reference
- **@PRODUCT:** Exact Prime Hydration bottle reference image
- **@FLOAT:** Floating-bottle arrangement reference or depth geometry
- **@ENV:** Modern city-plaza environment reference or description

## Video Prompt

```text
[SEEDANCE 2.5 - DEPTH-DRIVEN FLOATING PRODUCT | 5s | 9:16 | 30fps]

REFERENCE CONTROL (HIGHEST PRIORITY)
@DEPTH is the uploaded depth map video. Use @DEPTH as the single source of truth for the entire shot: camera movement, camera height, camera tilt, focal length, framing, object count, object scale, object screen position, object tilt angle, spatial layering, parallax, and depth falloff. Every frame's geometry must match @DEPTH 1:1. Do not reinterpret, retime, smooth, or improvise the camera path. @DEPTH controls geometry only, not lighting, color, or time of day. Final render is full-color photorealistic bright daylight footage.

@PRODUCT is the uploaded product reference image. Reproduce the product exactly: identical shape, proportions, cap geometry, surface finish, color, label layout, and logo placement. Pixel-faithful identity. Do not redesign, restyle, simplify, re-letter, or reinterpret packaging. Do not generate the product from description; the reference image overrides text interpretation. Map @PRODUCT onto every floating volume in @DEPTH: exactly five bottles, matching @DEPTH in count, scale, position, and tilt. The narrow protruding element on each volume maps to the bottle neck and cap, not a straw. Use glossy plastic with hard daylight, crisp specular edges, and a sunlit rim along the top edge.

LOCK REFERENCES
@FLOAT: The five bottles hang frozen in world space like a suspended installation. Each holds one fixed tilt angle for the entire shot. No self-rotation, spinning, tumbling, bobbing, or swaying. All apparent movement comes only from camera parallax as the camera dollies forward. Bottles are solid and opaque, not glowing or translucent.

@ENV: Dense modern city plaza in bright cold winter midday. Tall glass-and-stone towers rise on both sides as a vertical canyon. Clear deep-blue sky above, sun high behind buildings creating strong backlight and subtle lens flare. Large LED advertising screens on building faces glow vivid blue, red, and magenta with abstract color gradients only, no readable text or real brand logos. A crowd of pedestrians in colorful winter coats fills the lower quarter, seen from behind walking away from camera, softly out of focus with no recognizable faces. Traffic-light poles and a white delivery truck sit in the mid-ground. Generic global metropolis, not a real named landmark.

SHOT
Camera at pedestrian eye level, tilted upward, gliding forward through the crowd. Five giant Prime bottles hang motionless overhead while the city slides past behind them.

BEATS (timestamps reset to zero)
0.00-1.00 - Full arrangement already in frame: large hero bottle in centre, two above, one lower-left, one small to the right. Crowd flows below. Camera begins a slow forward push with strong depth separation.
1.00-2.30 - Parallax builds. Hero bottle slides across the towers while far bottles barely shift. LED screens drift through frame at right. All tilt angles remain locked.
2.30-3.60 - Camera continues forward and slightly up. Hero bottle grows larger as distance closes and settles toward centre-left. Upper bottles drift toward the top edge. Sky opens between the towers.
3.60-5.00 - Final hold. Hero bottle is front-facing, with pink body and PRIME label razor sharp and fully readable. Gentle forward drift only.

CAMERA PATH RULE
Camera path, height, tilt, lens compression, and every object screen position are inherited entirely from @DEPTH. No added shake, handheld wobble, extra orbit, crash zoom, or rotation not present in @DEPTH. Motion blur affects crowd and background only, never @PRODUCT.

GRADE LOCK
Full-color photorealistic live-action footage. Bright cold winter midday, clear blue sky, strong backlight, neutral-to-cool white balance, full natural saturation, natural skin tones, realistic photographic contrast, mild ambient occlusion beneath each bottle, and light atmospheric haze with distance. Bottles remain tack sharp while the background falls off softly. No warm golden cast, orange tint, or sunset.

AUDIO
No background music, soundtrack, BGM, score, vocals, or voiceover. Silent or minimal natural street ambience only.

PACING
Single continuous take. Hard cut in and hard cut out. No fades, dissolves, speed ramps, or transitions.

NEGATIVE
background music, BGM, soundtrack, score, voiceover, grayscale, monochrome, black and white, desaturated, colorless, depth map appearance, depth pass render, clay render, untextured, matte grey material, black void background, glowing objects, emissive bottles, white bottles, translucent bottles, silhouettes, rotating bottles, spinning, tumbling, swaying, bobbing, falling, straws, paper cups, coffee cups, disposable cups, lids, product redesign, altered packaging, wrong bottle shape, wrong cap, misspelled or invented logo text, wrong color, extra bottles, fewer than five bottles, liquid spilling, deforming geometry, night, sunset, warm golden hour, orange cast, dark scene, rain, neon, real brand logos, readable billboard text, recognizable landmark, recognizable faces, text overlays, watermark, subtitles, UI elements, fisheye distortion, warped geometry, camera shake, handheld jitter, fade in, fade out, cross dissolve, slow motion, low resolution, oversharpened halos
```

## Technical Specifications

- **Duration:** 5 seconds
- **Format:** 9:16 vertical
- **Frame rate:** 30fps
- **Camera:** Depth-driven forward dolly, pedestrian eye level, tilted upward
- **Objects:** Exactly five opaque bottles with fixed tilt angles
- **Lighting:** Bright cold winter midday backlight
- **Audio:** Natural street ambience only
- **Edit:** Continuous take with hard in/out, no transitions
