# Camera Angle Board Guide

**Platform:** GPT Image 2 via [Picsart AI Playground](https://picsart.com/ai-playground)  
**Method:** Image-to-image, one labelled multi-angle sheet  
**Source:** [Google Docs](https://docs.google.com/document/d/1FwAhtzrkCm_jdnmJu3qHfy29P_hZMyoZ0t7G8C5FbNU/mobilebasic?urp=gmail_link)

## Purpose

Turn one clear reference portrait into a labelled catalogue of the same person, pose, wardrobe, room, and daylight photographed from multiple camera setups. Choose either a 12-angle 3x4 catalogue or a tighter 9-angle 3x3 board.

## Why It Works

- **Four-number rhythm:** Every panel fixes camera height, tilt, focal length, and subject size. Adjacent panels alternate scale instead of resembling frames from a slow orbit.
- **Identity and fixed-world locks:** Facial structure, pose, wardrobe, architecture, and one building-fixed daylight source remain constant. Only camera position and framing change.

## Workflow

1. Choose the 12-angle catalogue or 9-angle board.
2. Attach one sharp, front-facing identity photograph.
3. Select GPT Image 2 and generate at high resolution in 4:5.
4. Verify identity consistency and exact `/slash-tag:` spelling.
5. Regenerate if neighboring panels converge on similar framing or subject size.

## Angle Reference

| Tag                  | Camera setup                                      | Availability |
| -------------------- | ------------------------------------------------- | ------------ |
| `/droneview:`        | 9 m high, down 55 degrees, 24mm                   | Both         |
| `/extremecloseup:`   | 1.65 m, level, 100mm macro                        | Both         |
| `/lowangle:`         | 0.9 m, up 30 degrees, 28mm                        | 12 only      |
| `/highangle:`        | 2.4 m, down 35 degrees, 35mm                      | Both         |
| `/topdown:`          | 4 m directly overhead, 24mm                       | Both         |
| `/profile:`          | 1.65 m, 90-degree side view, 85mm                 | Both         |
| `/wormseye:`         | 0.15 m, up 70 degrees, 18mm                       | Both         |
| `/threequarterback:` | 1.65 m, 135 degrees behind, 50mm                  | 12 only      |
| `/widefull:`         | 1.65 m, level, 24mm, well back                    | Both         |
| `/eyelevel:`         | 1.65 m, level, 50mm                               | 12 only      |
| `/overshoulder:`     | 1.8 m behind left shoulder, down 10 degrees, 35mm | Both         |
| `/closeup:`          | 1.65 m, level, 85mm                               | 12 only      |
| `/lowthreequarter:`  | 0.9 m, up 25 degrees, 28mm, 45 degrees left       | 9 only       |

## 12-Angle Catalogue Prompt

```text
PURPOSE: Create a camera-angle catalogue showing one person in one location across twelve named camera setups arranged for maximum visual spread.

OUTPUT: One high-resolution 4:5 vertical sheet, 1152x1440, divided into a 3-column by 4-row grid of twelve equal portrait panels. Separate panels with even gutters of flat matte-black card and use the same black card as the outer border. Give every panel rounded corners.

IMAGE 1: This source portrait shows one specific real person. Every panel must photograph THIS SAME PERSON in THIS SAME LOCATION on the same day. If any panel could depict a different person, that panel is wrong.

RHYTHM RULE - ABSOLUTE: This catalogue must not read as a camera slowly circling a standing figure. Every panel is fixed by camera height, tilt in degrees, focal length, and the fraction of frame height occupied by the subject. Hold all four values exactly. No two neighboring panels, horizontally or vertically, may share the same subject size. No row or column may form a smooth progression of camera height. Jump deliberately between a face filling the frame and a figure lost in the architecture.

IDENTITY RULE - ABSOLUTE: Keep the same person in all twelve panels. Preserve from Image 1 the exact skull proportions; cheekbone-to-jaw width relationship; eye shape and pupil spacing; nose-bridge angle and width; nostril outline; lip shape and mouth width; ear outline and set; brow line; hairline; beard or stubble edge when present; skin tone and undertone; and every mole, freckle, birthmark, and scar in its true position. In distant panels the face remains unmistakably this person. In profile and rear views, preserve identity through the nose bridge, chin outline, ear, and hairline.

POSE RULE: Hold one pose through every panel: standing upright, weight even on both feet, arms folded across the chest with the left forearm over the right, chin level. The body never changes. Only camera and framing change. Gaze changes only where explicitly stated below.

WARDROBE RULE: Replicate the clothing from Image 1 exactly in every panel: same garment, color, fit, and fabric fall. Preserve every accessory, including glasses, watch, rings, chains, and piercings. Add nothing and remove nothing.

LOCATION RULE - ABSOLUTE: Use one fixed interior in all twelve panels: a large empty hall in board-formed exposed concrete, polished concrete floor, one tall window wall along one side, and a concrete stair with a steel handrail set back across the space. Each angle reveals only the portion of THIS building physically visible from that camera position. Never use a different room, studio backdrop, or neutral void.

LIGHTING RULE - ABSOLUTE: Use one soft daylight source from the window wall, fixed in the building and never attached to the camera. Its direction relative to the subject remains identical, so facial light changes honestly as the camera moves. Keep exposure, white balance, and color grade identical across the sheet. Never relight a panel to flatter the face.

PANELS - READ LEFT TO RIGHT, TOP ROW FIRST:

1. DRONE VIEW: Camera 9 m high and well back, tilted down 55 degrees, 24mm. Subject occupies about one fifth of frame height, small against the architecture. Stair and full hall span dominate. Gaze straight ahead, never up at camera.

2. EXTREME CLOSE UP: Camera at 1.65 m, level, 100mm macro. Crop to brow, both eyes, and nose bridge, above the brow and below the cheekbones. Resolve lashes, iris pattern, and pores. Eyes directly into lens.

3. LOW ANGLE: Camera at 0.9 m, tilted up 30 degrees, 28mm. Subject occupies about nine tenths of frame height. Ceiling edge enters at top. Gaze level past camera.

4. HIGH ANGLE: Camera at 2.4 m, tilted down 35 degrees, 35mm, directly in front. Frame from knees up. Subject occupies about two thirds of frame height; floor occupies lower half. Gaze lifted to lens.

5. TOP DOWN: Camera directly overhead at 4 m, pointing straight down 90 degrees, 24mm. Foreshortened figure occupies about half the frame, surrounded by polished concrete. Head tilts up and eyes find lens.

6. PROFILE: Camera at 1.65 m, level, 90 degrees to the subject's side, 85mm. Frame chest up; head occupies about half the frame height. True unbroken side profile with window wall at one edge. Gaze follows profile line, never toward lens.

7. WORM'S EYE: Camera on floor at 0.15 m, tilted up 70 degrees, 18mm. Subject fills full frame height, towering and foreshortened with strong wide-angle convergence. Concrete ceiling fills upper third. Gaze straight ahead above lens.

8. THREE-QUARTER BACK: Camera at 1.65 m, level, 135 degrees around and behind, 50mm. Frame waist up; subject occupies about two thirds of frame height. Back of head and one shoulder lead, with cheekbone and brow edge barely visible. Head does not turn back.

9. WIDE FULL: Camera at 1.65 m, level, 24mm, well back. Whole figure small and off-center, occupying about one third of frame height. Full hall height and stair visible. Gaze level and straight ahead.

10. EYE LEVEL: Camera at 1.65 m, level at 0 degrees, 50mm, directly in front. Frame waist up; subject occupies about three quarters of frame height. Neutral, undistorted room view. Eyes directly into lens.

11. OVER SHOULDER: Camera at 1.8 m just behind and above the left shoulder, tilted down 10 degrees, 35mm. Shoulder is large and soft in the lower foreground; cheekbone and brow edge appear beyond it; hall depth runs away sharply.

12. CLOSE UP: Camera at 1.65 m, level, 85mm. Head and shoulders, face filling most of frame, background gently out of focus. Eyes directly into lens.

LABELS: Place one white rounded rectangular plate centered on the bottom edge of each panel, overlapping panel and gutter. Use black lowercase monospace text. Exact row-order labels: "/droneview:" "/extremecloseup:" "/lowangle:" "/highangle:" "/topdown:" "/profile:" "/wormseye:" "/threequarterback:" "/widefull:" "/eyelevel:" "/overshoulder:" "/closeup:". Render every label verbatim, including leading slash and trailing colon. No extra or duplicate text.

RENDERING: Photorealistic editorial photography, natural skin with visible pores and real texture, individual hair strands, true fabric weave, and correct optics for every focal length. Show wide-angle stretch at 18mm and 24mm and natural compression at 85mm and 100mm. No retouching, smoothing, face slimming, beautification, or symmetry correction.

CONSTRAINTS: Same person in every panel; no generic or substituted faces; no changes to skull width, eye spacing, nose bridge, mouth width, ear outline, or chin. No pose drift, unfolded arms, weight shift, wardrobe change, missing accessories, building change, studio backdrop, empty background, or camera-relative relighting. No two panels may resolve to the same camera or subject size. Drone, high-angle, and top-down views must remain plainly different in height, tilt, and scale. Only top-down tilts the head toward lens. Use only the exact labels above. No captions, title, watermark, logo, extra borders, second person, illustration, painterly effect, or CGI appearance.
```

## 9-Angle Board Prompt

```text
PURPOSE: Create a camera-angle board showing one person, one pose, one location, and one moment from nine camera positions selected for maximum visual spread.

OUTPUT: One high-resolution 4:5 vertical sheet, 1152x1440, divided into a 3-column by 3-row grid of nine equal portrait panels. Separate panels with even gutters of flat matte-black card and use the same black card as the outer border. Give every panel rounded corners.

IMAGE 1: This source portrait shows one specific real person. Every panel must photograph THIS SAME PERSON in THIS SAME MOMENT. If any panel could show a different person or a different take, that panel is wrong.

RHYTHM RULE - ABSOLUTE: This board must not resemble a camera slowly circling a standing figure. Every panel is fixed by camera height, tilt, focal length, and the fraction of frame height occupied by the subject. Hold all four values exactly. No two neighboring panels, horizontally or vertically, may share the same subject size or resemble consecutive frames from one camera move. Jump between face-filling detail and a small figure within architecture.

IDENTITY RULE - ABSOLUTE: Preserve the same person in all nine panels. Hold the exact skull proportions; cheekbone-to-jaw width relationship; eye shape and pupil spacing; nose-bridge angle and width; nostril outline; lip shape and mouth width; ear outline and set; brow line; hairline; beard or stubble edge when present; skin tone and undertone; and every mole, freckle, birthmark, and scar from Image 1. Preserve recognizability at distance, in profile, and from behind.

POSE RULE: Hold one pose throughout: upright, weight even on both feet, arms folded across the chest with left forearm over right, chin level. Only camera and framing change. Gaze changes only where specified.

WARDROBE RULE: Use the exact clothing and accessories from Image 1 in every panel, with identical color, fit, fabric fall, glasses, watch, rings, chains, and piercings. Nothing added or removed.

LOCATION RULE - ABSOLUTE: Use one fixed building: a large empty hall in board-formed exposed concrete, polished concrete floor, one tall window wall along one side, and a concrete stair with steel handrail set back across the space. Reveal only the physically correct part of THIS room from each viewpoint. Looking down reveals floor; looking up reveals ceiling; wide view reveals full hall and stair. Never change rooms or use a studio void.

LIGHTING RULE - ABSOLUTE: Use one soft daylight source from the window wall, fixed in the building rather than attached to camera. Keep its direction relative to subject, exposure, white balance, and grade consistent. Allow honest changes in facial modeling as viewpoint moves. Never relight to flatter the face.

PANELS - READ LEFT TO RIGHT, TOP ROW FIRST:

1. WORM'S EYE: Camera on floor at 0.15 m, tilted up 70 degrees, 18mm. Subject fills full frame height, towering and foreshortened, with concrete ceiling in upper third. Gaze straight into room above lens.

2. EXTREME CLOSE UP: Camera at 1.65 m, level, 100mm macro. Crop to brow, both eyes, and nose bridge. Resolve lashes, iris pattern, and pores. Eyes directly into lens.

3. DRONE VIEW: Camera 9 m high and well back, tilted down 55 degrees, 24mm. Subject occupies about one fifth of frame height, small against hall and stair. Gaze straight ahead, not upward.

4. PROFILE: Camera at 1.65 m, level, 90 degrees to side, 85mm. Frame chest up with head about half frame height. True unbroken profile and window wall at edge. Gaze follows profile line.

5. TOP DOWN: Camera directly overhead at 4 m, pointing down 90 degrees, 24mm. Foreshortened figure occupies about half frame, polished floor all around. This is the only panel where head tilts up and eyes find lens.

6. LOW THREE-QUARTER: Camera at 0.9 m, tilted up 25 degrees, 28mm, positioned 45 degrees around to subject's left. Frame thighs up; subject occupies about four fifths of frame height. Gaze level past camera.

7. WIDE FULL: Camera at 1.65 m, level, 24mm, well back. Whole figure small and off-center at about one third frame height. Full hall and stair visible. Gaze level and straight ahead.

8. OVER SHOULDER: Camera at 1.8 m just behind and above left shoulder, tilted down 10 degrees, 35mm. Shoulder large and soft in lower foreground; cheekbone and brow edge visible beyond it; hall depth sharp.

9. HIGH ANGLE: Camera at 2.4 m, tilted down 35 degrees, 35mm, directly in front. Frame knees up; subject occupies about two thirds of frame height with floor in lower half. Gaze lifted to lens while chin stays level.

LABELS: Place one white rounded rectangular plate centered on each panel's bottom edge, overlapping panel and gutter. Use black lowercase monospace. Exact row-order labels: "/wormseye:" "/extremecloseup:" "/droneview:" "/profile:" "/topdown:" "/lowthreequarter:" "/widefull:" "/overshoulder:" "/highangle:". Render them verbatim with leading slash and trailing colon. No extra or duplicate text.

RENDERING: Photorealistic editorial photography, natural skin with visible pores, individual hair strands, true fabric weave, and optically correct focal-length behavior. Show wide-angle stretch at 18mm and 24mm and natural compression at 85mm and 100mm. No retouching, smoothing, face slimming, beautification, or symmetry correction.

CONSTRAINTS: Same identity, pose, clothing, accessories, building, daylight source, exposure, white balance, and grade in every panel. No generic faces, identity drift, altered facial geometry, pose drift, unfolded arms, weight shift, wardrobe drift, missing accessories, room changes, neutral void, camera-relative relighting, duplicate viewpoints, neighboring panels with equal subject size, or smooth camera sweeps. Only top-down looks up at lens. Use only the exact labels above. No captions, titles, watermark, logo, extra border drawings, second person, illustration, painterly effect, or CGI look.
```

## Best-Practice Checks

- Use a sharp, unobstructed, front-facing identity photo.
- Keep the full identity lock; distant and rear angles depend on it.
- Keep all four camera numbers and the neighboring-size rule.
- Keep lighting fixed to the room, not the camera.
- Preserve lowercase `/slash-tags:` exactly.
- Regenerate if `/highangle:`, `/topdown:`, and `/droneview:` become visually similar.
- The example concrete hall may be replaced, but every panel must use one fixed building.
