# Curitiba Botanical Garden Greenhouse Flight

## Classification

**Product Category:** Architecture and landscape

**Reveal Effect:** Continuous FPV traversal

**Reveal Mechanism:** Forward camera movement through architectural thresholds, using full-frame darkness, light, and reference-matched compositions to join independently generated shots

**Sequence Type:** Multi-generation architectural fly-through

**Filename:** `seq.curitiba-botanical-garden-greenhouse-flight.md`

## Description of Resulting Video or Video Sequence

A 21-second cinematic FPV flight through the Curitiba Botanical Garden, from the formal French garden into the glass greenhouse, up through its white steel structure and central oculus, then back into the open air for a symmetrical final view.

The finished film is assembled from four independent generations. Each block remains in one spatial environment, lasts no more than eight seconds, and joins the next through a full-frame visual threshold.

## Usage

Perfect for botanical garden promotion, architectural films, destination campaigns, cultural tourism, landscape showcases, and cinematic venue introductions. Ideal when a long spatial journey must be divided into short image-to-video generations while preserving the impression of one continuous FPV flight.

## Engines/Models

Platform-agnostic. Use an image-to-video model that supports 4-8 second clips, first-frame references, optional first-and-last-frame guidance, strong camera-motion prompting, and photorealistic architectural continuity. Prompt C specifically requires first-frame and last-frame reference support.

## Prerequisites / Dependencies

- **Dependency 1 - Required exterior reference:** Head-on view of the white glass greenhouse from slightly above, including its broad steps and ornamental fountain. Used as Prompt A's first frame and reusable as the exterior appearance reference.
- **Dependency 2 - Required interior reference:** Interior view looking upward at the white steel ribs, arched glass panes, and palm crowns. Used as Prompt B's first frame.
- **Dependency 3 - Generated transition frame:** Prompt B's final oculus frame becomes Prompt C's first frame.
- **Dependency 4 - Generated transition frame:** Prompt C's final centered greenhouse frame becomes Prompt D's first frame.
- Keep all reference images free of watermarks and preserve the same greenhouse geometry across exterior views.

## Sequence Structure

| Block | Name           | Generate | Use | Transition                                   |
| ----- | -------------- | -------: | --: | -------------------------------------------- |
| A     | The Entrance   |       4s |  3s | The dark doorway fills the frame             |
| B     | The Greenhouse |       8s |  8s | The bright oculus and sky fill the frame     |
| C     | The Oculus     |       6s |  6s | Arrives at a centered exterior composition   |
| D     | The Landing    |       4s |  4s | Ends in an almost imperceptible upward drift |

## Architectural Concept

The Curitiba Botanical Garden is organized around a central axis. Its symmetrical French garden leads directly to the greenhouse, encouraging a horizontal journey in a straight line. The sequence follows that axis, enters the greenhouse, then turns the journey from horizontal to vertical. It climbs along the white steel ribs, passes through the oculus, and enters the sky before returning to a centered view of the building.

## Video Prompt

**Duration:** 21 seconds in the final assembly from four separately generated clips; 22 seconds of source generation before trimming Prompt A to 3 seconds.

**Style:** Cinematic, photographic, realistic FPV drone footage with an ultra-wide lens, controlled barrel distortion, subtle grain, continuous forward travel, strong architectural parallax, and diegetic audio only.

Generate each JSON object as an independent clip. Preserve every prompt in full and assemble the clips in A-B-C-D order using the specified full-frame transitions.

### Generation A - The Entrance

**Reference frame:** Exterior of the greenhouse, viewed head-on and slightly from above.

**Action:** Dive from facade height, descend close to the glass panels, level out at the entrance, and pass through it. End in darkness with the doorway filling the frame.

```json
{
  "shot_structure": "single continuous FPV drone shot, 4 seconds, no cuts",
  "reference_usage": "the attached image is the FIRST FRAME only: the white glass greenhouse seen from in front and slightly above, with the broad steps and the fountain below it. Do not return to this framing.",
  "camera_motion": [
    "0.0-1.0s: already diving FAST toward the building, the white arched glass facade rushing up to fill the frame, the steps and the fountain sweeping past beneath",
    "1.0-2.2s: drops down the face of the building at speed, the tall arched glass panels and white steel columns flashing past close, then levels out hard at the entrance",
    "2.2-3.2s: the dark open doorway grows and FILLS THE WHOLE FRAME and the camera goes through it, the door frame flashing past on both sides",
    "3.2-4.0s: the darkness inside fills the entire frame"
  ],
  "pov_character": "an FPV drone",
  "environment": "the front of a large white art-nouveau glass greenhouse with three domes: tall arched glass panels, slender white steel columns, a broad flight of steps and an ornamental fountain below it, clipped hedges and lawn around",
  "lighting": "bright afternoon, warm sun from the side, clear sky, crisp shadows",
  "audio": "wind rushing, water, birds, no music",
  "style": "ultra-wide drone lens with strong barrel distortion, cinematic, photographic and realistic, subtle grain. FAST and urgent from the very first frame - this is the fastest shot of the film. Something is passing close to the lens at every moment",
  "negative": "starting far away, a wide establishing shot, flying over the garden first, an approach across open ground, slow drifting, calm pace, camera stopping, hovering, orbiting, circling, nothing passing close to the lens, stopping at the door, cutting around the doorway, a second greenhouse, cut, dissolve, fade, transition, watermark, crowds close to the lens, distorted faces, night, text overlay, letterbox bars"
}
```

### Generation B - The Greenhouse

**Reference frame:** Interior of the greenhouse, looking upward at the white ribs, arched glass panes, and palm crowns.

**Action:** Rush low through the hall, skim past the bronze statue, climb hard along the columns, bank beneath the domes, and continue upward until the oculus and sky fill the frame.

```json
{
  "shot_structure": "single continuous FPV drone shot, 8 seconds, no cuts",
  "reference_usage": "the attached image is the FIRST FRAME only: inside the glass greenhouse looking up, the white steel ribs and arched glass panes overhead with palm crowns against them. Keep the architecture exactly as it is.",
  "camera_motion": [
    "0.0-1.0s: already moving forward fast with the glass roof wheeling overhead, the nose dropping from the domes down toward the floor, palm crowns sweeping past close above the lens",
    "1.0-2.2s: levels out low and rushes forward through the hall, tropical planting and palm trunks flashing past close on both sides, and passes right beside a dark bronze statue standing on a stone plinth, the figure sweeping past",
    "2.2-3.5s: CLIMBS hard and fast, the planting dropping away beneath, the tall slender white steel columns rushing down past the lens",
    "3.5-5.5s: high up under the domes now, banks through one wide turn between the white steel arches and ribs, passing close between two columns, palm crowns just below, sunlight through the glass",
    "5.5-7.0s: keeps rising toward the crown of the central dome, the white ribs converging overhead",
    "7.0-8.0s: the glass of the dome and the open sky beyond fill the entire frame, the camera still rising as the shot ends"
  ],
  "pov_character": "an FPV drone",
  "environment": "the interior of a large white art-nouveau glass greenhouse: slender white steel ribs and arched glass panes, three domes, tall palms and dense tropical planting, a dark bronze statue on a stone plinth, paved paths, sunlight pouring through the glass",
  "lighting": "daylight pouring through the glass roof, hard shafts of light and cool shadow below, the white steel glowing against the sky",
  "audio": "birds, water, footsteps echoing, no music",
  "style": "ultra-wide drone lens with strong barrel distortion, cinematic, photographic and realistic, subtle grain. Fast and fluid. The camera TRAVELS fast but ROTATES slowly, so the architecture never smears or jumps to a new angle. It uses the FULL HEIGHT of the building - down to the floor and up to the crown of the dome. Something is passing close to the lens at every moment",
  "negative": "staying low, flying only at ground level, never reaching the roof, staying high, never coming down to the floor, going outside, exiting the building, a second greenhouse, duplicated architecture, repeating arches, a looping path, arriving at the same place twice, camera stopping, hovering, holding still, orbiting in place, rotating on the spot, rotating too fast, blurring into a new angle, slow drifting, calm pace, touching the glass, watermark, stock photo watermark, crowds close to the lens, distorted faces, statue with a distorted face, night, cut, dissolve, fade, transition, text overlay, letterbox bars"
}
```

### Generation C - The Oculus

**Reference frames:** The oculus is the first frame. A centered aerial view of the greenhouse facade is the last frame.

**Action:** Rise through the circular opening, climb above the roof, bank forward in a wide arc over the garden, and descend toward a centered frontal view of the greenhouse.

```json
{
  "shot_structure": "single continuous FPV drone shot, 6 seconds, no cuts",
  "reference_usage": "Image 1 is the FIRST FRAME: directly beneath the circular opening at the crown of the glass dome, its ring and radiating spokes filling the frame with blue sky through it. Image 2 is the LAST FRAME: the white glass greenhouse seen head-on from the air, with its fountain, steps and wings below it. The shot travels continuously from one to the other. The camera only ever travels FORWARDS - it never reverses.",
  "camera_motion": [
    "0.0-1.0s: rises straight up through the circular opening, the ring of the oculus and its radiating spokes sweeping past close all around the lens",
    "1.0-2.0s: out into the open air above the roof, still climbing, the three white glass domes falling away below and behind",
    "2.0-3.5s: noses over and travels FORWARD away from the building, banking into one wide arc out over the garden",
    "3.5-5.0s: carries the arc around toward the front of the greenhouse, easing down a little as it comes, the building turning into view ahead",
    "5.0-6.0s: settles head-on facing the greenhouse with its fountain and steps laid out below, still drifting gently forward as the shot ends"
  ],
  "pov_character": "an FPV drone",
  "environment": "the crown of a white art-nouveau glass greenhouse with three domes, then open sky above it, then the building seen from the air head-on: its white steel and glass front, a stepped ornamental fountain and broad staircase below it, low glazed wings on either side, clipped hedges, lawn, paths and trees",
  "lighting": "bright daylight through the glass, then full afternoon sun in the open air, soft high cloud, even light",
  "audio": "wind, birds, no music",
  "style": "ultra-wide drone lens with slight barrel distortion, cinematic, photographic and realistic, subtle grain. THE CAMERA ALWAYS TRAVELS FORWARDS - it climbs, it banks, it descends, but it never moves backwards and never retreats from anything. This is the final approach: it eases as it arrives at the last framing but never fully stops",
  "negative": "flying backwards, reversing, retreating, pulling back away from the building, backing away, receding, drifting backward, passing sideways through a glass wall, exiting through the side of the building, appearing suddenly outside, touching the structure, a second greenhouse, duplicated buildings, camera stopping dead, holding still, orbiting in place, rotating on the spot, blurring into a new angle, a full 360 degree orbit, landing, ending motionless, a frozen final frame, watermark, people close to the lens, distorted faces, night, cut, dissolve, fade, transition, text overlay, letterbox bars"
}
```

### Generation D - The Landing

**Reference frame:** The final frame from Prompt C, with the greenhouse centered above the fountain, staircase, and symmetrical hedge parterres.

**Action:** Continue forward slowly while rising. Reveal more of the geometric garden, preserve the centered axis, and end with a nearly imperceptible upward drift rather than a frozen frame.

```json
{
  "shot_structure": "single continuous FPV drone shot, 4 seconds, no cuts",
  "reference_usage": "the attached image is the FIRST FRAME: the white glass greenhouse seen head-on and centred, its stepped fountain and staircase on the axis below it, the geometric hedge parterres opening symmetrically in the foreground, clear sky above. Keep this composition and continue very gently from it.",
  "camera_motion": [
    "0.0-1.5s: continues drifting SLOWLY forward and rising, the hedge parterres opening out beneath the lens, the greenhouse holding dead centre and level",
    "1.5-3.0s: keeps rising slowly and steadily, more of the symmetrical garden coming into frame below, the building staying centred on the axis, the sky above it staying clear and uncluttered",
    "3.0-4.0s: eases into that wide symmetrical framing and holds it, drifting only very slightly upward - almost still but never completely frozen - the greenhouse centred, the axis running straight down the middle, open sky across the top of the frame"
  ],
  "pov_character": "an FPV drone",
  "environment": "the white art-nouveau glass greenhouse with three domes seen head-on from the air at the end of the day: a stepped ornamental fountain and broad staircase on the central axis below it, clipped geometric hedge parterres opening symmetrically in the foreground, low glazed wings on either side, a tall conical tree to the left, a white steel sculpture to the right, lawn and trees beyond",
  "lighting": "late afternoon, warm low sun, long soft shadows across the hedges, clear blue sky",
  "audio": "wind, distant birds, no music",
  "style": "ultra-wide drone lens with slight barrel distortion, cinematic, photographic and realistic, subtle grain. This is the FINAL shot of the film and the only one that is allowed to slow down. It moves calmly and eases as it opens out, but it NEVER fully stops and it is still drifting on the last frame. The composition stays symmetrical and centred on the building throughout, with the sky above the domes left clear",
  "negative": "moving fast, racing, accelerating, jerky motion, shaky handheld, a completely frozen final frame, a still image at the end, the drift stopping dead, descending, dropping down, flying backwards, reversing, pulling away, closing in at the end, pushing in, the greenhouse off centre, a tilted or crooked horizon, reframing away from the axis, the building cropped, orbiting, rotating on the spot, banking, clutter across the top of the frame, birds or aircraft in the sky, people close to the lens, distorted faces, a second greenhouse, duplicated buildings, night, overcast, cut, dissolve, fade, transition, text overlay, watermark, letterbox bars"
}
```

## Assembly Notes

- Use one first frame per block and no more than one additional appearance reference.
- Join A to B through the dark doorway occupying the full frame.
- Join B to C through the bright oculus and open sky occupying the full frame.
- Use Prompt C's last frame as Prompt D's first frame.
- Describe objects passing close to the lens instead of fixing the camera to exact coordinates; rigid positional instructions reduce perceived movement.
- Keep every source image free of watermarks because the model may reproduce them as scene texture.
- Avoid a single generation that changes locations. Long takes remain more spatially coherent when each generation stays within one environment.

## Source

Translated and adapted from the Portuguese case study **Voo pelo Jardim Botanico**, Swell Filmes. The generation prompts were already supplied in English and are preserved here.
