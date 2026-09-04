# Camera Movements Reference Guide

Use this guide as the navigation layer for the camera-movement library in this folder. Select one primary camera movement, then specify direction, speed, path, subject relationship, framing, and the final camera state.

## Prompt Construction

Use this order when writing a camera-movement prompt:

`camera movement` + `direction and path` + `speed and acceleration` + `relationship to subject` + `framing and lens behavior` + `start and end state` + `continuity constraints`.

Example:

`Smooth dolly in toward the character from a medium shot to a close-up, constant eye-level camera height, 85mm lens, maintain eye contact and facial identity, slow controlled acceleration, settle gently at the end, no orbit, no zoom, no unintended camera shake.`

## Motion Families

### Static And Rotational

| Movement                            | Use                                                                           | Reference                                                                                                                    |
| ----------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Static shot                         | Intentional stillness, observation, tension, or a stable emotional baseline.  | [Static Shot](CAMERA-MOVEMENT.STATIC-SHOT.MD)                                                                                |
| Pan left / right                    | Horizontal reveal or following action from a fixed camera position.           | [Pan Left](CAMERA-MOVEMENT.PAN-LEFT.MD), [Pan Right](CAMERA-MOVEMENT.PAN-RIGHT.MD)                                           |
| Tilt up / down                      | Vertical reveal or emphasis while the camera remains in place.                | [Tilt Up](CAMERA-MOVEMENT.TILT-UP.MD), [Tilt Down](CAMERA-MOVEMENT.TILT-DOWN.MD)                                             |
| Whip pan left / right               | Fast directional transition, energy, urgency, or hidden cut.                  | [Whip Pan Left](CAMERA-MOVEMENT.WHIP-PAN-LEFT.MD), [Whip Pan Right](CAMERA-MOVEMENT.WHIP-PAN-RIGHT.MD)                       |
| Arc left / right                    | Camera curves around the subject to reveal changing perspective.              | [Arc Left](CAMERA-MOVEMENT.ARC-LEFT.MD), [Arc Right](CAMERA-MOVEMENT.ARC-RIGHT.MD)                                           |
| Orbit clockwise / counter-clockwise | Camera circles the subject while preserving the subject as the visual anchor. | [Orbit Clockwise](CAMERA-MOVEMENT.ORBIT-CLOCKWISE.MD), [Orbit Counter-Clockwise](CAMERA-MOVEMENT.ORBIT-COUNTER-CLOCKWISE.MD) |

### Physical Camera Movement

| Movement            | Use                                                                                                    | Reference                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Dolly in / out      | Physically closes or increases distance from the subject; changes perspective and emotional proximity. | [Dolly In](CAMERA-MOVEMENT.DOLLY-IN.MD), [Dolly Out](CAMERA-MOVEMENT.DOLLY-OUT.MD)                     |
| Slow zoom in / out  | Changes focal length without physically moving the camera; creates optical emphasis or distance.       | [Slow Zoom In](CAMERA-MOVEMENT.SLOW-ZOOM-IN.MD), [Slow Zoom Out](CAMERA-MOVEMENT.SLOW-ZOOM-OUT.MD)     |
| Fast zoom in / out  | Abrupt optical emphasis, shock, discovery, or comic punctuation.                                       | [Fast Zoom In](CAMERA-MOVEMENT.FAST-ZOOM-IN.MD), [Fast Zoom Out](CAMERA-MOVEMENT.FAST-ZOOM-OUT.MD)     |
| Crash zoom in / out | Aggressive rapid zoom used for heightened impact or disorientation.                                    | [Crash Zoom In](CAMERA-MOVEMENT.CRASH-ZOOM-IN.MD), [Crash Zoom Out](CAMERA-MOVEMENT.CRASH-ZOOM-OUT.MD) |
| Slider left / right | Controlled short lateral camera move with precise product, portrait, or environmental framing.         | [Slider Left](CAMERA-MOVEMENT.SLIDER-LEFT.MD), [Slider Right](CAMERA-MOVEMENT.SLIDER-RIGHT.MD)         |
| Truck left / right  | Larger lateral physical camera move, often parallel to a subject or environment.                       | [Truck Left](CAMERA-MOVEMENT.TRUCK-LEFT.MD), [Truck Right](CAMERA-MOVEMENT.TRUCK-RIGHT.MD)             |
| Pedestal up / down  | Raises or lowers the entire camera while maintaining its orientation.                                  | [Pedestal Up](CAMERA-MOVEMENT.PEDESTAL-UP.MD), [Pedestal Down](CAMERA-MOVEMENT.PEDESTAL-DOWN.MD)       |
| Crane up / down     | Sweeping vertical movement that changes height and spatial scale.                                      | [Crane Up](CAMERA-MOVEMENT.CRANE-UP.MD), [Crane Down](CAMERA-MOVEMENT.CRANE-DOWN.MD)                   |

### Tracking And Pursuit

| Movement                        | Use                                                                      | Reference                                                                           |
| ------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Tracking shot                   | Camera travels with or alongside a subject.                              | [Tracking Shot](CAMERA-MOVEMENT.TRACKING-SHOT.MD)                                   |
| Low tracking shot               | Ground-level pursuit, power, speed, or physically heightened movement.   | [Low Tracking Shot](CAMERA-MOVEMENT.LOW-TRACKING-SHOT.MD)                           |
| Side tracking shot              | Lateral movement synchronized with a subject crossing the frame.         | [Side Tracking Shot](CAMERA-MOVEMENT.SIDE-TRACKING-SHOT.MD)                         |
| Reverse tracking shot           | Camera moves backward while the subject advances toward it.              | [Reverse Tracking Shot](CAMERA-MOVEMENT.REVERSE-TRACKING-SHOT.MD)                   |
| Follow shot / over-the-shoulder | Camera follows behind a subject and preserves their direction of travel. | [Follow Shot / Over-the-Shoulder](CAMERA-MOVEMENT.FOLLOW-SHOT-OVER-THE-SHOULDER.MD) |
| Chase shot                      | Aggressive pursuit movement with urgency and environmental motion.       | [Chase Shot](CAMERA-MOVEMENT.CHASE-SHOT.MD)                                         |
| Vehicle tracking shot           | Camera tracks a moving vehicle or is mounted on a moving vehicle.        | [Vehicle Tracking Shot](CAMERA-MOVEMENT.VEHICLE-TRACKING-SHOT.MD)                   |
| Push-past / pass-by             | Camera passes the subject or foreground obstruction to reveal new space. | [Push-Past / Pass-By](CAMERA-MOVEMENT.PUSH-PAST-PASS-BY.MD)                         |

### Aerial And Immersive

| Movement                        | Use                                                                             | Reference                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Drone push in / pull back       | Aerial approach or retreat that changes scale and spatial context.              | [Drone Push In](CAMERA-MOVEMENT.DRONE-PUSH-IN.MD), [Drone Pull Back](CAMERA-MOVEMENT.DRONE-PULL-BACK.MD) |
| Helicopter shot                 | Broad aerial movement with large-scale environmental perspective.               | [Helicopter](CAMERA-MOVEMENT.HELICOPTER.MD)                                                              |
| First-person POV                | Camera becomes the character's visual point of view.                            | [First-Person / POV](CAMERA-MOVEMENT.FIRST-PERSON-POV.MD), [POV](CAMERA-MOVEMENT.POV.MD)                 |
| Body-mounted camera / Snorricam | Camera stays rigidly attached to the subject while the world moves around them. | [Body-Mounted Camera / Snorricam](CAMERA-MOVEMENT.BODY-MOUNTED-CAM-SNORRICAM.MD)                         |

### Optical And Time-Based

| Movement                   | Use                                                                               | Reference                                                                 |
| -------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Earth zoom out             | Extreme scale transition from a local subject to a planetary or cosmic view.      | [Earth Zoom Out](CAMERA-MOVEMENT.EARTH-ZOOM-OUT.MD)                       |
| Infinite zoom              | Continuous nested zoom through images, spaces, or visual layers.                  | [Infinite Zoom](CAMERA-MOVEMENT.INFINITE-ZOOM.MD)                         |
| Tilt-shift movement        | Stylized focus and scale effect combined with a controlled camera or lens shift.  | [Tilt-Shift](CAMERA-MOVEMENT.TILT-SHIFT.MD)                               |
| Time-lapse                 | Compresses long-duration environmental or subject change into accelerated motion. | [Time-Lapse](CAMERA-MOVEMENT.TIME-LAPSE.MD)                               |
| Pass-through / penetration | Camera travels through an opening, object, surface, or visual barrier.            | [Pass-Through / Penetration](CAMERA-MOVEMENT.PASS-THROUGH-PENETRATION.MD) |

### Combined And Variant Examples

| Movement              | Use                                                                               | Reference                                                              |
| --------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Aggressive dolly in   | High-pressure physical approach with stronger acceleration than a standard dolly. | MP4 example only: `CAMERA-MOVEMENT.AGGRESSIVE-DOLLY-IN.MP4`            |
| Gentle push in        | Subtle emotional approach for realization, intimacy, or attention.                | MP4 example only: `CAMERA-MOVEMENT.GENTLE-PUSH-IN.MP4`                 |
| Camera rise to face   | Vertical reveal that arrives at the subject's face.                               | MP4 example only: `CAMERA-MOVEMENT.CAMERA-RISE-TO-FACE.MP4`            |
| Low lateral slide     | Low-angle lateral movement with restrained glide.                                 | MP4 example only: `CAMERA-MOVEMENT.LOW-LATERAL-SLIDE.MP4`              |
| Slow lateral drift    | Nearly floating side movement for quiet unease or atmosphere.                     | MP4 example only: `CAMERA-MOVEMENT.SLOW-LATERAL-DRIFT.MP4`             |
| Slow rising curve     | Vertical movement combined with a curving path.                                   | MP4 example only: `CAMERA-MOVEMENT.SLOW-RISING-CURVE.MP4`              |
| Smooth quarter-circle | Partial orbit or arc around a subject.                                            | MP4 example only: `CAMERA-MOVEMENT.SMOOTH-QUARTER-CIRCLE.MP4`          |
| Vertigo / contra-zoom | Dolly and zoom move in opposite directions to distort perceived depth.            | MP4 example only: `CAMERA-MOVEMENT.VERTIGO.ZOOM-DOLLY.CONTRA-ZOOM.MP4` |

## Playable Video Examples

The following local MP4 examples use HTML5 video controls. In VS Code, open the Markdown preview and click the play button. Renderers that do not allow embedded video can still use the filenames in the table above.

### Aggressive Dolly In

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.AGGRESSIVE-DOLLY-IN.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.AGGRESSIVE-DOLLY-IN.MP4).
</video>

### Gentle Push In

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.GENTLE-PUSH-IN.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.GENTLE-PUSH-IN.MP4).
</video>

### Camera Rise To Face

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.CAMERA-RISE-TO-FACE.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.CAMERA-RISE-TO-FACE.MP4).
</video>

### Low Lateral Slide

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.LOW-LATERAL-SLIDE.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.LOW-LATERAL-SLIDE.MP4).
</video>

### Slow Lateral Drift

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.SLOW-LATERAL-DRIFT.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.SLOW-LATERAL-DRIFT.MP4).
</video>

### Slow Rising Curve

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.SLOW-RISING-CURVE.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.SLOW-RISING-CURVE.MP4).
</video>

### Smooth Quarter-Circle

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.SMOOTH-QUARTER-CIRCLE.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.SMOOTH-QUARTER-CIRCLE.MP4).
</video>

### Vertigo / Contra-Zoom

<video controls preload="metadata" width="640">
	<source src="CAMERA-MOVEMENT.VERTIGO.ZOOM-DOLLY.CONTRA-ZOOM.MP4" type="video/mp4">
	Your Markdown renderer does not support embedded video. [Open the MP4](CAMERA-MOVEMENT.VERTIGO.ZOOM-DOLLY.CONTRA-ZOOM.MP4).
</video>

## Complete Local Asset Inventory

The following assets are present in this folder and are listed here so the guide accounts for every movement file. The primary Markdown references are linked in the movement-family tables above; these entries cover companion videos and alternate media variants.

### Companion MP4 Examples

- [Arc Left](CAMERA-MOVEMENT.ARC-LEFT.MP4)
- [Arc Right](CAMERA-MOVEMENT.ARC-RIGHT.MP4)
- [Base Tracking Shot](CAMERA-MOVEMENT.BASE-TRACKING-SHOT.MP4)
- [Chase Shot](CAMERA-MOVEMENT.CHASE-SHOT.MP4)
- [Crane Down](CAMERA-MOVEMENT.CRANE-DOWN.MP4)
- [Crane Up](CAMERA-MOVEMENT.CRANE-UP.MP4)
- [Dolly In](CAMERA-MOVEMENT.DOLLY-IN.MP4)
- [Dolly Out](CAMERA-MOVEMENT.DOLLY-OUT.MP4)
- [Drone Pull Back](CAMERA-MOVEMENT.DRONE-PULL-BACK.MP4)
- [Drone Push In](CAMERA-MOVEMENT.DRONE-PUSH-IN.MP4)
- [Earth Zoom Out](CAMERA-MOVEMENT.EARTH-ZOOM-OUT.MP4)
- [Fast Tracking](CAMERA-MOVEMENT.FAST-TRACKING.MP4)
- [First-Person View](CAMERA-MOVEMENT.FIRST-PERSON-VIEW.MP4)
- [Follow Shot / Over-the-Shoulder](CAMERA-MOVEMENT.FOLLOW-SHOT-OVER-THE-SHOULDER.MP4)
- [Handheld Shot](CAMERA-MOVEMENT.HANDHELD-SHOT.MP4)
- [Helicopter Shot](CAMERA-MOVEMENT.HELICOPTER-SHOT.MP4)
- [Infinite Zoom](CAMERA-MOVEMENT.INFINITE-ZOOM.MP4)
- [Low Tracking V2](CAMERA-MOVEMENT.LOW-TRACKING-V2.MP4)
- [Orbit Clockwise](CAMERA-MOVEMENT.ORBIT-CLOCKWISE.MP4)
- [Orbit Counter-Clockwise](CAMERA-MOVEMENT.ORBIT.COUNTCLOCKWISE.MP4)
- [Pan Left](CAMERA-MOVEMENT.PAN-LEFT.MP4)
- [Pan Right](CAMERA-MOVEMENT.PAN-RIGHT.MP4)
- [Pass Through Objects](CAMERA-MOVEMENT.PASS-PENETRATE-THROUGH-OBJECTS.MP4)
- [Pedestal Down](CAMERA-MOVEMENT.PEDESTAL-DOWN.MP4)
- [Pedestal Up](CAMERA-MOVEMENT.PEDESTAL-UP.MP4)
- [Push-Past / Pass-By](CAMERA-MOVEMENT.PUSH-PAST-PASS-BY-SHOT.MP4)
- [Reverse Tracking Walk-and-Talk](CAMERA-MOVEMENT.REVERSE-TRACKING-WALK-AND-TALK.MP4)
- [Slider Left](CAMERA-MOVEMENT.SLIDER-LEFT.MP4)
- [Slider Right](CAMERA-MOVEMENT.SLIDER-RIGHT.MP4)
- [Slow Zoom In](CAMERA-MOVEMENT.SLOW-ZOOM-IN.MP4)
- [Slow Zoom Out](CAMERA-MOVEMENT.SLOW-ZOOM-OUT.MP4)
- [Snorricam V2](CAMERA-MOVEMENT.SNORRICAM-V2.MP4)
- [Static Shot](CAMERA-MOVEMENT.STATIC-SHOT.MP4)
- [Tilt Down](CAMERA-MOVEMENT.TILT-DOWN.MP4)
- [Tilt-Shift](CAMERA-MOVEMENT.TILT-SHIFT.MP4)
- [Tilt Up](CAMERA-MOVEMENT.TILT-UP.MP4)
- [Time-Lapse](CAMERA-MOVEMENT.TIME-LAPSE.MP4)
- [Truck Left](CAMERA-MOVEMENT.TRUCK-LEFT.MP4)
- [Truck Right](CAMERA-MOVEMENT.TRUCK-RIGHT.MP4)
- [Vehicle Tracking](CAMERA-MOVEMENT.VEHICLE-TRACKING.MP4)
- [Whip Pan Left](CAMERA-MOVEMENT.WHIP-PAN-LEFT.MP4)
- [Whip Pan Right](CAMERA-MOVEMENT.WHIP-PAN-RIGHT.MP4)

### Alternate And Versioned Assets

- [Crash Zoom In Vertical](CAMERA-MOVEMENT.CRASH-ZOOM-IN-V.MP4)
- [Crash Zoom Out Vertical](CAMERA-MOVEMENT.CRASH-ZOOM-OUT-V.MP4)
- [Fast Tracking Alternate](<CAMERA-MOVEMENT.FAST-TRACKING(1).MP4>)
- [Fast Zoom In Vertical](CAMERA-MOVEMENT.FAST-ZOOM-IN-V.MP4)
- [Fast Zoom Out Vertical](CAMERA-MOVEMENT.FAST-ZOOM-OUT-V.MP4)
- [Handheld Shot Markdown Reference](CAMERA-MOVEMENT.HANDHELD-SHOT.MD)

## Asset Coverage Note

The inventory includes both descriptive Markdown references and media-only examples. A media file may show a variation of a technique without having a dedicated Markdown explanation; use the closest linked Markdown reference for prompt construction and the media file for visual timing and motion study.

## Obvious Omissions And Placeholders

These are common camera-movement references that are not currently represented by a dedicated Markdown guide in this folder. They are placeholders for future entries, not claims that the folder already contains them.

| Placeholder                | Definition                                                                               | Suggested prompt seed                                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Camera roll / Dutch tilt   | Camera rotates around the lens axis, tilting the horizon.                                | `Slow controlled camera roll into a Dutch angle, keep the subject readable, increase the angle only as tension rises.`                                 |
| 360-degree orbit           | Camera completes a full circle around a stationary or moving subject.                    | `Complete a smooth 360-degree orbit around the subject, maintain consistent distance and eye-line, reveal the environment continuously.`               |
| Standard zoom in / out     | Neutral optical zoom without the extreme speed of a crash zoom.                          | `Perform a smooth optical zoom from [starting frame] to [ending frame], keep the camera physically stationary and preserve perspective.`               |
| Camera shake               | Deliberate vibration or instability applied to the camera, distinct from handheld drift. | `Add controlled motivated camera shake caused by [impact/run/earthquake], preserve subject identity and avoid random frame tearing.`                   |
| Dolly-zoom / Vertigo guide | Dedicated Markdown explanation of the contra-zoom already represented by an MP4.         | `Dolly [forward/backward] while zooming [out/in] at the matched rate, keep the subject's apparent size stable while the background depth warps.`       |
| Spiral / helical move      | Camera rises or descends while orbiting around the subject.                              | `Execute a smooth ascending spiral around the subject, combine vertical lift with a consistent orbit and cinematic stabilization.`                     |
| Sub360 / wraparound move   | Camera travels around only part of the subject, usually 180 to 270 degrees.              | `Perform a controlled wraparound arc from front three-quarter to rear three-quarter, preserve subject orientation and reveal the changing background.` |

## Supporting References

- [Cinematic Motion Taxonomy](CHEATSHEET.CINEMATIC-MOTION-TAXONOMY.MD)
- [Prompt-Engineering Guide](CHEATSHEET.PROMPT-ENGINEERING-GUIDE.MD)
- [Camera Path Planning Workflow](REFERENCE.camera-path-planning-workflow.md)
- [Draw-the-Path AI Animation Technique](CAMERA-TECHNIQUE.DRAW-THE-PATH-ANIMATION.md)
- [FVP Invisible Path Camera-Movement Guide](CAMERA-TECHNIQUE.FVP-INVISIBLE-PATH-GUIDE.md)
- [Subject Direction Reference](SUBJECT-DIRECTION-REFERENCE.MD)
- [Tracking Shot Reference](TRACKING-SHOT-REFERENCE.MD)

## Hard Negatives

`No unintended zoom, no random orbit, no direction reversal, no impossible camera path, no subject duplication, no frame tearing, no accidental camera shake, no loss of subject identity, no exposure or lighting changes unless explicitly requested.`
