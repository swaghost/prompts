# Multi-Angle Talking-Head Video Sequence

## Description

A professional talking-head video system that enables clean multi-angle cuts, background transformations, and humanized motion in a single AI-generated continuous take. Features stable camera angles, realistic human gestures, and precise lip-sync without distortion or character duplication.

## Usage

Perfect for content creator videos, talking-head presentations, educational content, tutorial videos, and professional speaking videos. Ideal for YouTube creators, course instructors, brand ambassadors, and social media influencers who need professional multi-angle content without manual editing. This system excels at creating natural-looking presenter videos with dynamic camera cuts while maintaining body proportions and preventing AI glitches.

## Prerequisites

- Reference image of the subject (@img1 or similar)
- Audio track for lip-sync (uploaded separately in generator)
- Script text matching the audio track
- Subject description (appearance, outfit, characteristics)

## The Three Rules That Keep It Clean

Most glitches in multi-angle AI video trace back to three critical issues. Follow these rules for stable output:

1. **Limit the angles** — Cut between 4 stable, named angles, not 6+ vague ones. Fewer clean cuts = far fewer glitches.

2. **Never use "over-the-shoulder"** — This implies a second person in the foreground, which makes the model spawn a duplicate of the character facing herself.

3. **Lock the frame on the reveal** — Swap the background with the camera fully locked. A background change plus a zoom-out at the same time is what breaks the body proportions.

## Master Prompt Structure

### Complete Full Prompt

A [SUBJECT_DESCRIPTION], matching the face reference in @img1 exactly, wearing [FULL_OUTFIT_HEAD_TO_TOE]. She is the only person in the video, completely alone in the frame at all times, with no other people, no duplicates, and no reflections of her anywhere. Her body has correct realistic human proportions and a consistent natural size in every shot. She stands and speaks to camera in one continuous take, her mouth movement precisely synced to the uploaded audio track, matching its rhythm, pacing, and emphasis. She moves like a real person talking rather than a smooth animation: her gestures come in short natural bursts that settle between phrases instead of moving constantly — an open palm turning outward on a point, a small counting motion, hands dropping loosely to her sides between sentences, occasionally one hand gesturing while the other rests still. Her weight shifts subtly from one foot to the other, shoulders relaxed and asymmetric. Her face carries light natural expression — irregular blinking, small eyebrow lifts on emphasis, a slight squint when making a point, and a brief genuine half-smile that fades naturally. Her head moves in small conversational tilts and nods following the rhythm of the audio. Subtle, grounded, human, like unscripted spontaneous delivery. The camera cuts cleanly between four steady angles, each a stable locked shot with no distortion: a straight-on waist-up medium shot, a slightly low three-quarter angle from her left, a tight close-up on her face, and a slightly wider chest-up shot. On the cut to the tight close-up, she naturally turns her head and shifts her eyeline toward the new camera position, settling her gaze into the lens as she continues speaking — a single subtle adjustment that happens only once. For the first two-thirds she stands in [SCENE_DESCRIPTION]. She says: "[SCRIPT]". Exactly as she says "[REVEAL_CUE_LINE]," the background behind her transforms into [REVEAL_BACKGROUND] while the camera stays completely locked in the same waist-up half-body framing — no zoom, no pull-back, no camera movement at all, her position and size in the frame staying exactly the same as the background changes behind her, as she gives a knowing playful half-smile and a light presenting gesture. Cinematic editorial lighting, natural skin texture, realistic anatomy and body proportions, shallow depth of field, photorealistic, consistent identity, size, and outfit across every angle.

### Negative Prompt

zoom out, pull back, camera movement, full body shot, two people, duplicate person, clone, twin, second character, mirrored person, reflection, distorted body, wrong proportions, deformed anatomy, stretched body, size change, warped limbs, extra limbs, shorts, bare legs, outfit change, scene glitch, flickering, morphing

## Reusable Building Blocks

### A. Multi-Angle in One Continuous Shot

Makes a single generation cut between angles while the subject keeps talking. Four named angles + one look-to-lens beat.

**Angle Direction Block:**

The camera cuts cleanly between four steady angles, each a stable locked shot with no distortion: a straight-on waist-up medium shot, a slightly low three-quarter angle from her left, a tight close-up on her face, and a slightly wider chest-up shot. On the cut to the tight close-up, she naturally turns her head and shifts her eyeline toward the new camera position, settling her gaze into the lens as she continues speaking — a single subtle adjustment that happens only once.

### B. Background Change (Locked Frame, No Zoom)

Swaps the background on the spoken cue without moving the camera — the version that stops body distortion.

**Background Reveal Block:**

Exactly as she says "[CUE_LINE]," the background behind her transforms into [NEW_BACKGROUND] while the camera stays completely locked in the same waist-up half-body framing — no zoom, no pull-back, no camera movement at all, her position and size in the frame staying exactly the same as the background changes behind her.

### C. Humanized Motion Block

The single most important line for realism is "gestures settle between phrases." AI video defaults to constant, floaty motion because it interpolates every frame; real people move in bursts and then stop. This block forces that rhythm.

**Motion Block:**

She moves like a real person talking rather than a smooth animation: her gestures come in short natural bursts that settle between phrases instead of moving constantly — an open palm turning outward on a point, a small counting motion, hands dropping loosely to her sides between sentences, occasionally one hand gesturing while the other rests still. Her weight shifts subtly from one foot to the other, shoulders relaxed and asymmetric. Her face carries light natural expression — irregular blinking, small eyebrow lifts on emphasis, a slight squint when making a point, and a brief genuine half-smile that fades naturally.

## Generator Settings

| Setting            | Value                                | Notes                                     |
| ------------------ | ------------------------------------ | ----------------------------------------- |
| Mode               | Image-to-Video (start image = @img1) | Use reference image                       |
| Duration           | Match uploaded audio length exactly  | Mismatch = drifting sync                  |
| Aspect ratio       | 16:9 horizontal (1280×720)           | Standard video format                     |
| Lip-sync           | On                                   | Source = uploaded audio track             |
| Motion strength    | Low–medium                           | Too high = puppet motion, too low = stiff |
| Identity/face lock | On                                   | Maintains consistent face                 |

## Reusable Template (Swap the Slots)

Replace the bracketed slots to reuse the whole system for a new video.

**Slots:**

- [SUBJECT] — subject description + reference tag (e.g. @img1)
- [OUTFIT] — full head-to-toe outfit, including lower body
- [SCENE] — the starting scene/room
- [SCRIPT] — the spoken script (also uploaded as audio)
- [REVEAL_BG] — the background it reveals at the end

**Template:**

[SUBJECT], wearing [OUTFIT], the only person in the frame at all times with no duplicates or reflections, correct realistic human proportions and consistent size in every shot. She stands and speaks to camera in one continuous take, mouth movement precisely synced to the uploaded audio track. She moves like a real person talking: gestures come in short natural bursts that settle between phrases, one hand resting while the other gestures, subtle weight shifts, relaxed asymmetric shoulders. Light natural expression — irregular blinking, small eyebrow lifts on emphasis, a half-smile that fades naturally. The camera cuts cleanly between four steady, locked, undistorted angles: straight-on waist-up, a slightly low three-quarter from her left, a tight close-up, and a wider chest-up shot. On the close-up cut she turns her head and settles her gaze into the lens once. She stands in [SCENE]. She says: "[SCRIPT]". On the final line, the background transforms into [REVEAL_BG] while the camera stays completely locked in the same half-body framing — no zoom, no camera movement, her position and size unchanged. Cinematic lighting, natural skin texture, realistic anatomy, photorealistic, consistent identity and outfit across every angle.

## Troubleshooting — Cause & Fix

| Problem                                  | Cause & Fix                                                                                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Duplicate character facing herself       | "Over-the-shoulder" angle implies a second person. Remove it; add "only person, no duplicates" and load negatives with clone/twin/two people. |
| Weird body size / bad proportions at end | The full-body zoom-out on the reveal. Keep the camera locked at half-body; change only the background.                                        |
| Motion feels AI / floaty                 | Add "gestures settle between phrases." Real people move in bursts and stop. Keep motion strength low–medium.                                  |
| Outfit shows shorts on wide shots        | Model pulls shorts from the reference sheet. State the full head-to-toe outfit (matching trousers) explicitly; negative: shorts, bare legs.   |
| Lip-sync drifts                          | Set generation duration equal to the audio length. Keep the script text in the prompt as a phonetic anchor.                                   |
| Neon text or graphics garbled            | AI models garble rendered text. Add text/graphics as overlays in post (After Effects / CapCut).                                               |

## Example Implementation

**Subject:** A blonde woman in her late twenties with long wavy blonde hair, grey-blue eyes, light freckles, and fair skin

**Outfit:** Complete tailored tan camel suit — single-button camel blazer over a white ribbed tank top, with matching tailored camel trousers

**Scene:** Professional content-creator studio with glowing neon RGB nameplate reading "CLARA AI", warm ambient LED lighting, desk with microphone, headphones, monitor, plants and tasteful personal items

**Script:** "This whole video was made by AI. The angles, the background, the cuts. I didn't add any B-roll, and I didn't do a single second of manual editing. In fact, this entire setup isn't even real — my actual background looks like this."

**Reveal:** Plain neutral grey studio wall (transforms on the final line)

## Technical Notes

- The four-angle limit is critical for stability
- "Gestures settle between phrases" is the key phrase that creates realistic motion
- Lock the camera frame completely when changing backgrounds
- Always specify full head-to-toe outfit to prevent AI adding unexpected clothing
- Keep motion strength low-medium to avoid puppet-like movements
- Match audio duration exactly for proper lip-sync

---
