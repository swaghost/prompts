# Desk Maquette

## Workflow Overview

This workflow converts project reference images into a photorealistic architectural desk-maquette image, enhances the generated image, and then animates it as a slow camera orbit.

### Required Inputs

- At least two clear images of the same architectural project
- Images that collectively show the building design, materials, massing, landscaping, and important facade details
- Prompt 1 for image generation
- Prompt 2 for image-to-video animation

## Step 1 - Create the Image with Nano Banana

1. Open the image-generation website or platform that provides Nano Banana.
2. Select Nano Banana as the image model.
3. Upload at least two images of the same architectural project.
4. Use **Prompt 1** below as one complete prompt.
5. Generate the desk-maquette image.
6. Check that the physical model, monitor wireframe, monitor render, and tablet floor plan all depict the same building.
7. Save the strongest generated image to your device.

## Step 2 - Upscale the Image with Free Enhance

1. Open the Free Enhance image-upscaling website or equivalent enhancement tool.
2. Upload the generated desk-maquette image.
3. Select the Enhance or Upscale action.
4. Preserve the original aspect ratio, composition, architecture, screen content, and material details.
5. Avoid generative redesign, added objects, altered typography, or invented building details.
6. Save the enhanced image to your device.

## Step 3 - Create the Animation with Veo 3 Fast

1. Open the video-generation website or platform.
2. Enter its **Generate Media** section.
3. Choose **Veo** from the left-side model or media tab.
4. Select **Veo 3 Fast** from the available model options.
5. Upload the enhanced image created in Step 2 as the image-to-video reference.
6. Use **Prompt 2** below as one complete prompt.
7. Generate the video and inspect architecture, screen, object, lighting, and camera continuity.
8. Regenerate only if the orbit changes objects, warps the model, or invents architectural details.

## Prompt 1 - Generate the Desk Maquette Image

```text
Create a hyper-realistic architectural design workspace scene.

Use all uploaded project images together as the sole architectural reference. They depict the same building and must be reconciled into one exact, consistent design. Preserve its geometry, proportions, facade layout, roof, openings, materials, landscaping, and distinctive details. Do not blend in unrelated architecture or invent missing design features.

On a wooden desk, place a detailed physical scale model of the provided building with landscaping and miniature cars, centered as the main focus.

Behind it, place two large monitors:

- The left monitor displays a precise 3D wireframe or blueprint view of the same building.
- The right monitor displays a high-quality photorealistic daylight render of the same building.

Place a tablet on the desk displaying the top-down architectural floor plan of the same building. The plan must correspond logically to the model's footprint and visible spatial organization.

Arrange realistic architectural model-making tools around the desk: glue, cutting blades, pens, model fragments, scale rulers, and two side lamps casting warm light. Keep the tools secondary and do not obstruct the model, monitors, or tablet.

Use mixed lighting from warm indoor desk lamps and natural daylight entering through a large rear window. Show a softly blurred modern city skyline outside.

Camera: eye-level view, slightly wide lens, centered on the desk, with the building model in sharp focus and the background gently softer.

Style: photorealistic, cinematic, premium professional architecture studio, realistic wood, paper, screen, plastic, card, metal, glass, vegetation, and model-making textures.

CRITICAL CONSISTENCY:
The physical model, wireframe, photorealistic monitor render, and tablet floor plan must all represent the exact same provided building. Keep every other scene element coherent and physically plausible. No mismatched facade, alternate roof, changed materials, inconsistent window positions, impossible floor plan, random architecture, text errors, logos, watermark, duplicated tools, malformed miniature cars, or distorted screens.
```

## Prompt 2 - Animate the Enhanced Image

```text
Use the uploaded enhanced desk-maquette image as the only visual reference and exact starting composition.

Create a hyper-realistic image-to-video animation of the architect's workspace with the building preserved as a physical scale model on the desk. The model must remain detailed, sharp, and identical to the uploaded image throughout the video.

PRESERVATION LOCK:
Keep the physical model, architecture, facade, roof, materials, landscaping, miniature cars, desk, tools, lamps, monitors, tablet, floor plan, window, skyline, lighting, shadows, reflections, colors, and object positions unchanged. Do not regenerate, redesign, rotate, slide, replace, or distort any object.

The left monitor must continue displaying the same fixed wireframe or blueprint image. The right monitor must continue displaying the same fixed photorealistic render. The tablet must continue displaying the same fixed floor plan. Screen images remain static and attached to their displays with no animation, flicker, scrolling, warping, or content change.

CAMERA MOVEMENT:
- Simulate a carefully controlled handheld or steadicam recording of the desk.
- Begin from the exact frontal perspective of the uploaded image.
- Slowly orbit the camera approximately 90 degrees around the building model in one smooth continuous arc toward the side.
- Keep the camera at desk level, slightly above the desk surface.
- Use a subtle wide-angle lens with natural perspective and restrained parallax.
- Maintain slow, steady, physically believable movement without jitter, wobble, sudden acceleration, cuts, zooms, or distortion.

FOCUS:
- Keep the building model as the primary point of interest throughout the orbit.
- Maintain sharp focus on the scale model.
- Let the monitors, tools, lamps, and distant skyline remain slightly softer but recognizable.
- Use natural focus behavior with no autofocus hunting or focus breathing.

LIGHTING:
- Preserve the exact natural daylight and warm desk-lamp balance from the uploaded image.
- Keep light direction, intensity, color temperature, screen brightness, shadows, and reflections consistent for the entire movement.

Only the camera moves. Nothing else moves or rotates. Do not invent or modify any architectural detail absent from the uploaded reference.

NEGATIVE:
moving model, rotating building, sliding objects, animated monitor images, changing floor plan, flickering screens, distorted architecture, altered facade, changed roof, added floors, changed materials, moved landscaping, duplicate tools, floating objects, warped tablet, malformed miniature cars, changing skyline, lighting drift, color drift, camera cut, jump, zoom, excessive shake, motion-smear transition, text, logo, watermark
```

## Quality Checklist

- [ ] At least two project references were used for image generation.
- [ ] All architectural representations show the same building.
- [ ] The model, wireframe, render, and floor plan agree.
- [ ] The generated image was enhanced without redesigning it.
- [ ] The enhanced image was uploaded to Veo 3 Fast.
- [ ] The animation begins from the uploaded image composition.
- [ ] The camera completes one smooth approximately 90-degree orbit.
- [ ] Only the camera moves.
- [ ] All desk objects remain fixed.
- [ ] Screen contents remain static and unchanged.
- [ ] Architecture and landscaping remain exact.
- [ ] Lighting remains stable throughout.
