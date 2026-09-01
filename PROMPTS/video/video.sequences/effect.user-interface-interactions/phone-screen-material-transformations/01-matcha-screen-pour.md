# Matcha Phone Screen Pour - Source Video VFX

## Platform

Image-to-video or video-to-video editor with tracked screen replacement and physically realistic liquid simulation.

## Source Video Lock

Use the uploaded video as the exact base video. Keep the woman, face, body, hands, nails, clothing, background, lighting, camera movement, phone, phone position, framing, original video quality, and original audio completely unchanged. Do not add people or objects.

Only modify the phone screen and create the matcha liquid effect below.

## Video Prompt

```text
The entire effect is photorealistic and physically realistic, as if real matcha is inside the phone screen and can physically pour from it.

MATCHA APPEARANCE AND TEXTURE

Thick, creamy, freshly mixed matcha with natural marbling: rich green ranging from light creamy green to deeper green; slightly viscous consistency; soft cloudy swirls; darker green concentrated areas mixed with lighter milky-green areas; realistic depth, translucency, surface tension, and uneven density. Fluid motion has delicate organic swirling patterns.

Do not make it look like paint, slime, gel, oil, green smoke, glowing liquid, or a flat digital texture.

TIMELINE

00:01.00 TO 00:01.82
The phone screen initially contains its existing words or text. At exactly 00:01.00, matcha begins spreading directly through the existing letter shapes. The letters become wet, blurry, and fluid as if the letters themselves are made of matcha. Matcha visibly originates from those letter shapes, spreads outward across the display, and continuously covers the original words. By exactly 00:01.82, the entire visible display is filled with creamy swirling matcha. The matcha sits physically on the phone-screen surface, never as a detached digital overlay.

00:01.82 TO 00:03.71
When the woman naturally tilts the phone in the original video, the matcha responds to its exact orientation. It flows toward the actual lowest screen edge under gravity, then pours directly over that edge. The stream remains connected to the screen material and follows the direction of the phone tilt.

The liquid has realistic gravity, viscosity, surface tension, continuous flow, subtle splashes, occasional droplets, organic marbling, and naturally varying stream thickness. It must not float, flow from the wrong edge, ignore the tilt, or remain static while the phone moves.

MASS CONSERVATION
The matcha disappears from the screen as it pours. Show a continuous progression: full screen of matcha -> matcha flowing toward edge -> less matcha on screen -> only a small amount remaining -> completely empty screen. The amount remaining on-screen must visibly correspond to the amount that has poured out; never retain a full screen layer while a separate stream pours.

BY EXACTLY 00:03.71
All matcha has left the screen. The display is clean and naturally empty: no matcha, green tint, residue, droplets, stains, remaining texture, original text, or green reflection.

PHYSICAL INTEGRATION
Track the liquid perfectly to the phone screen. Preserve the phone's exact shape, perspective, reflections, borders, bezels, and position. The liquid interacts naturally with edges as if the screen were physically filled. Movement and rotation create correct inertia and gravity. The result is indistinguishable from a practical liquid effect filmed in the original scene.
```

## Technical Specifications

- **Effect window:** 00:01.00 to 00:03.71
- **Screen state:** Existing text -> fully covered matcha -> clean empty display
- **Primary constraint:** Screen-tracked, mass-conserving liquid behavior
- **Audio:** Preserve original audio unchanged

## Negative Prompt

```text
changed woman, altered face, altered hands, altered nails, changed clothing, changed phone, changed background, changed lighting, camera movement changes, new objects, new people, text replacement, UI overlay, floating liquid, wrong pouring direction, liquid pouring from the wrong side, static liquid during phone motion, duplicated liquid mass, paint, slime, gel, oil, green smoke, glowing liquid, flat digital texture, CGI appearance, residue, green tint, droplets left on screen, stains, screen text remaining after 00:03.71
```
