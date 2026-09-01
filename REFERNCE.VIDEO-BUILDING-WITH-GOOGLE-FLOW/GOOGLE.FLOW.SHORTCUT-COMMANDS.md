In Google Flow (Gemini Flow video generation model), slash (`/`) commands act as quick prompt modifiers to control visual style, camera movement, focus, lighting, and pacing directly inside the prompt box.

The complete list of slash commands categorizes by function:

## Visual Style & Genre Modifiers

Sets the overarching aesthetic, color science, texture, and mood of the output.

- `/cinematic` – Standard movie-grade visual treatment.
- `/filmic` – 35mm motion-picture texture, natural highlights, subtle grain, and organic colors.
- `/commercial` – Clean, polished high-key lighting, vivid color separation, and crisp edges.
- `/luxury` – Deep contrast, rich blacks, warm gold highlights, and opulent surfaces.
- `/documentary` – Cinema-vérité realism with handheld natural motion and unvarnished lighting.
- `/vintagefilm` – Nostalgic 16mm/8mm look with gate weave, soft halation, and subtle color shift.
- `/scifi` – Engineered spec-design, futuristic blue-white geometry, and clean tech surfaces.
- `/cyberpunk` – Wet asphalt, neon glare (cyan/magenta), dense urban decay, and atmospheric steam.
- `/dreamy` – Soft diffusion, blooming light highlights, pastel tones, and surreal atmosphere.

---

## Camera Movement Commands

Directs how the virtual camera navigates through space.

- `/dollyin` – Moves the camera smoothly toward the subject.
- `/dollyout` – Pulls the camera backward away from the subject.
- `/orbit` – Rotates 360 degrees horizontally around the focal point.
- `/steadicam` – Smooth, fluid tracking movement following the motion.
- `/craneup` – Elevates the camera vertically (jib/crane reveal shot).
- `/cranedown` – Drops the camera vertically down toward a scene.
- `/panleft` / `/panright` – Rotates the camera lens left or right horizontally.
- `/tildup` / `/tilt-down` – Angles the camera lens up or down vertically.

---

## Framing & Angles

Defines field of view and camera positioning relative to the subject.

- `/establishing` – Very wide scene opener establishing environment and scale.
- `/wideangle` / `/wide` – Broad field of view showcasing the surroundings.
- `/tight` – Close composition isolating the subject or detail.
- `/pov` – Point-of-view angle, simulating eyes of the subject.
- `/overtheshoulder` – Framing from behind one character looking at another.
- `/lowangle` – Camera positioned low aiming upward for dramatic impact.
- `/overhead` – Bird’s-eye top-down view looking straight down.
- `/leadinglines` – Uses environmental structural lines to lead the viewer's eye.

---

## Focus & Optics

Controls depth-of-field and specialized visual lens behaviors.

- `/shallowdepth` – Narrow focus with heavily blurred background (bokeh).
- `/deepfocus` – Keeps foreground, mid-ground, and background all in sharp focus.
- `/rackfocus` – Shifts focal point dynamically from foreground to background (or vice-versa).
- `/selectivefocus` – Locks sharp clarity strictly onto a chosen object or face.
- `/macro` – Extreme close-up detailing microscopic or fine textures.
- `/bokeh` – Soft, out-of-focus background light orb effect.
- `/zoomblur` – Motion blur resulting from a rapid focal-length change.
- `/lensflare` – Optical light streaks caused by bright light entering the lens edge.
- `/vignette` – Subtle darkening around the frame corners to center focus.

---

## Lighting Setup

Adjusts illuminance, shadows, and atmospheric light sources.

- `/volumetric` – Visible rays or light shafts piercing through haze, dust, or mist.
- `/backlight` – Primary light positioned behind the subject creating a silhouette effect.
- `/rimlight` – Strong edge lighting outlining the silhouette from behind.
- `/spotlight` – Isolated high-key light focusing strictly on the subject.
- `/nightscene` – Low-ambient, high-contrast night setup.

---

## Subject Motion & Action

Controls frame dynamics and subject speed.

- `/speedramp` – Seamless shift between real-time, fast motion, and slow motion within one shot.
- `/timelapse` – Ultra-fast motion showing environmental evolution (clouds, shadows, crowds).
- `/bullettime` – Extremely high-speed action frozen or ultra-slowed while camera orbits.
- `/freeze` – Instantly pauses scene dynamics at a key moment.
- `/entrance` – Focuses specifically on a subject stepping into the frame.
- `/exit` – Focuses on a subject leaving or moving out of frame.

---

## Color & Exposure

Tweaks brightness, color balance, and saturation profiles.

- `/exposure` – Manual lighting bias for high-key bright or low-key dark looks.
- `/saturation` – Heightened, rich, vivid colors.
- `/desaturate` – Muted color palette leaning toward monochrome or muted tones.

> **Pro Tip:** Combine these modularly inside your prompt string (e.g., `/filmic /dollyin /shallowdepth /volumetric A tactical mid-field passer controlling the ball...`) to combine style, motion, and lighting cleanly.
