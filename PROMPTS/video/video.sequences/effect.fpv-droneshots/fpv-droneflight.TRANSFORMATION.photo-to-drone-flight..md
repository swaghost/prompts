# Photo to Aerial Drone Shot

## Classification

**Product Category:** Photo-to-video transformation

**Reveal Effect:** Aerial reframe and drone movement

**Reveal Mechanism:** Reconstruct the same photographed moment from a high, distant aerial position, then animate the aerial still with natural drone motion

**Sequence Type:** Catalogue-to-film / reference-match sequence

**Filename:** `seq.photo-to-aerial-drone-shot.md`

## Description of Resulting Video or Video Sequence

A two-stage workflow that turns one supplied photo into an aerial-style vertical drone clip. ChatGPT first reconstructs the same moment from a high aerial viewpoint; Seedance, used through VOSU, then animates the selected aerial still into a drone-style video.

## Usage

Perfect for travel, property, venue, landscape, event, and social content where a drone was not available at capture time. Use the original photo as the visual source of truth, select the cleanest aerial reframe, then animate that exact still in Seedance through VOSU.

## Engines/Models

- ChatGPT Images - Stage 1 aerial reframe
- VOSU with Seedance - Stage 2 drone-style video animation

## Prerequisites / Dependencies

- Dependency #1 - Original photograph that establishes the subject, location, pose, objects, architecture, landscape, landmark geometry, lighting, weather, and colors
- Dependency #2 - Selected aerial reframe generated from Dependency #1

## Storyboard Prompt

**Panel 1 (start frame):** Reconstruct the supplied photo from a camera approximately four times farther away and significantly higher, with a natural 30-degree downward angle. Keep the complete original main subject at 10-15% of the vertical frame and let the environment dominate.

**Panel 2 (end frame):** Continue the exact aerial view with an elevated, distant drone composition. Preserve the same identity, pose, clothing, objects, architecture, landscape, landmark geometry, lighting, weather, and colors, extending only the previously unseen surroundings.

Style: Photorealistic 9:16 aerial drone photography with natural perspective, real environmental scale, authentic depth, high detail, and seamless continuity with the original image. No fisheye distortion, altered geometry, text, logos, or watermarks.

## Video Prompt

**Duration:** Choose a short duration supported by the target Seedance model. 9:16 vertical.

**Style:** Photorealistic aerial drone footage with natural perspective, authentic scale, stable geometry, and seamless continuity with the supplied aerial reframe.

**Source Prompt - Stage 1: Aerial Reframe in ChatGPT**

```text
Using the provided image as the visual source of truth, reconstruct the exact same moment and location from a much higher and more distant aerial drone camera position.

Move the virtual camera approximately 4 times farther away and significantly upward, creating an elevated viewpoint with a natural 30-degree downward angle.

Show the complete main subject occupying only about 10-15% of the frame, surrounded by a large amount of environment. The landscape must dominate the composition.

Achieve this through realistic camera repositioning, not by shrinking the original image, adding borders, or using an extreme wide-angle lens. Preserve the exact identity, pose, clothing, objects, architecture, landscape, landmark geometry, lighting, weather, and colors.

Extend only the previously unseen surroundings as a realistic continuation of the same location. Do not introduce any new elements, fisheye distortion, altered geometry, text, logos, or watermarks.

Photorealistic vertical 9:16 aerial drone photograph, natural perspective, realistic environmental scale, authentic depth, high detail, and seamless continuity with the original image.
```

Tip: Prefix the Stage 1 prompt with `N3` to generate three options, then select the cleanest aerial frame.

**Scene Setup/Context:**

Upload the selected Stage 1 aerial reframe into Seedance through VOSU. Treat it as the fixed visual source: preserve the subject, all existing objects, location geometry, lighting, weather, colors, and environmental layout. Extend nothing and introduce nothing new during animation.

**Timeline/Shot Breakdown:**

0:00-end
Aerial drone camera begins at the exact elevated, distant perspective of the supplied reframe. It makes one slow, smooth, natural forward drift with a subtle downward descent, retaining the subject at approximately the same small scale in the environment. Use credible aerial parallax in the landscape without changing geometry or identity. Maintain a steady professional drone feel without sudden acceleration, dramatic zooming, cuts, warping, or artificial motion.

**Camera:**

Single continuous aerial drone shot. High, distant viewpoint; natural approximately 30-degree downward viewing angle; slow forward drift and subtle descent. No extreme wide angle, fisheye effect, fast push-in, orbit, whip movement, or cuts.

**Lighting:**

Keep the lighting, weather, shadows, color, and atmosphere identical to the selected aerial reframe.

**Visual Effects/Technical Details:**

Natural aerial movement and realistic parallax only. Keep the subject, objects, architecture, landscape, and landmark geometry stable. Do not add elements beyond the aerial reframe.

**Quality/Technical Requirements:**

Photorealistic vertical 9:16 output, natural camera motion, realistic environmental scale, authentic depth, high detail, and stable perspective. No new elements, altered geometry, identity drift, fisheye distortion, borders, text, logos, watermarks, camera cuts, glitches, artifacts, or artificial-looking motion.

---

## Source Note

The shared source document supplied the complete Stage 1 ChatGPT prompt but referenced rather than included the exact Stage 2 Seedance prompt. The Stage 2 motion instruction above is a conservative implementation of its stated process: animate the selected aerial image into a drone-style vertical clip using Seedance through VOSU.
