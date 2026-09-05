# Interior Photos to 360 Equirectangular Panorama

## Purpose

Reconstruct one continuous monoscopic 360-degree interior panorama from several photographs of the same space.

## Prerequisites

Upload four to eight photographs from complementary angles, ideally including front, right, left, back, wide, ceiling, and floor views.

## Prompt

```text
Use these uploaded images of the same interior space to create one true monoscopic 360° equirectangular panorama.

Preserve the original architecture, furniture, materials, lighting, proportions, and camera height as accurately as possible.

Use the photos to reconstruct the full environment around the camera and generate the missing unseen areas in a physically plausible way.

OUTPUT REQUIREMENTS:

- True 2:1 equirectangular panorama
- Full 360° horizontal and 180° vertical view
- Camera at the center of the space
- Level horizon
- Complete ceiling and floor
- Seamless left and right edges
- No visible seams
- No duplicated furniture
- No mirrored architecture
- No fisheye
- No little-planet effect
- No collage
- No multi-panel layout

The result must be one continuous 360° panoramic image directly compatible with a VR or 360 viewer.
```

## Workflow

1. Upload four to eight overlapping views of the same room.
2. Paste the prompt and generate one image.
3. Open the result in a 360 viewer and inspect the wrap seam, horizon, ceiling, floor, and object continuity.

## Validation Checklist

- [ ] Output is exactly 2:1.
- [ ] Left and right edges wrap seamlessly.
- [ ] Horizon is level.
- [ ] Ceiling and floor are complete.
- [ ] Furniture is neither duplicated nor mirrored.
- [ ] Architecture matches across all source views.
