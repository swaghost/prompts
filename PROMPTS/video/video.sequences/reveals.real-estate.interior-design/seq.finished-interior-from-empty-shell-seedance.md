# Finished Interior from Empty Shell - Seedance 2.0

## Description

A two-stage reference workflow: remove every non-structural element from a completed interior to create an empty shell, then animate the exact finished project assembling back into place with a locked camera.

## Source

Pedro Enrriques, `@enrriquesdesign`. Tool: [Morphix AI](https://morphix.pro?ref=2fbdd59d). Model: Seedance 2.0.

## Prerequisites

- One completed-project reference image
- Morphix AI or another image editor for the empty-shell frame
- Seedance 2.0 or another first/last-frame video model

## Empty Environment Prompt

```text
Remove all non-structural elements from this interior, leaving only the original architectural structure. This is a removal task, NOT a redesign.

Remove all furniture, built-in cabinetry, decorations, plants, artwork, lighting, electrical accessories, aluminum window frames, glass, and all floor, wall, and ceiling finishes.

Keep the city skyline background exactly unchanged. Do NOT modify, replace, regenerate, blur, or alter the exterior view.

The result must show the space in its raw construction phase, with only exposed structural surfaces such as concrete, masonry, or plaster.

Preserve 100% of the original geometry, architecture, proportions, camera angle, perspective, framing, composition, image dimensions, and aspect ratio. Do NOT crop, zoom, rotate, distort, redesign, reinterpret, or change any architectural element.

Do NOT add anything. No construction materials, workers, tools, debris, dust, temporary objects, or replacement elements.

Highest priority: the removal must be complete. No furniture, cabinetry, lighting, finishes, aluminum frames, or glass may remain. The only allowed modification is the complete removal of these elements while preserving the original architecture and city view exactly as shown.
```

## Animation Prompt

```text
Create a 10-second ultra-realistic architectural construction animation in vertical 9:16 format. Begin with the unfinished concrete shell and gradually transform it into the finished interior shown in the reference image.

Keep the camera completely locked, preserving 100% of the original angle, framing, perspective, geometry, proportions, and composition.

The construction should happen organically, with materials naturally forming from the existing structure: marble flooring, plastered walls, gypsum ceiling, integrated lighting, custom millwork, window frame, curtains, furniture, decorative objects, artwork, and plants should assemble smoothly in a logical sequence until the space is fully completed.

Every element must appear only in its exact final position, with no redesign or repositioning. The daylight should gradually evolve into the warm golden-hour atmosphere while the architectural lighting softly turns on near the end.

Use cinematic architectural visualization, ultra-realistic materials, physically accurate lighting, soft global illumination, subtle reflections, and DSLR-quality rendering.

Do not add, remove, or modify any architectural elements, furniture, decorations, materials, openings, or textures that are not present in the finished project. Avoid particles, dust, construction workers, tools, exaggerated morphing, or unrealistic visual effects. The final frame must perfectly match the finished reference image.
```

## Technical Specifications

- **Duration:** 10 seconds
- **Format:** Vertical 9:16
- **Camera:** Completely locked
- **Start:** Raw empty structural shell
- **End:** Exact completed-project reference
- **Lighting arc:** Daylight to warm golden hour with architectural lights activating near the end

## Negative Prompt

```text
camera movement, crop change, zoom, reframing, geometry change, altered skyline, redesigned architecture, invented furniture, misplaced decor, workers, tools, debris, dust, particles, magical effects, exaggerated morphing, liquid surfaces, warped windows, duplicate objects, missing objects, final-frame mismatch
```
