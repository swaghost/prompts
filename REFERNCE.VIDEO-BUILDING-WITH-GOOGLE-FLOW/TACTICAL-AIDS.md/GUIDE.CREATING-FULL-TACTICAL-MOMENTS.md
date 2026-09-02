Building a full tactical training module (for platforms like **soccr.org**) requires stitching individual AI-generated video clips into a coherent, instructional narrative. To ensure seamless transitions when editing, the prompt architecture must maintain strict visual continuity (kits, lighting, pitch conditions) while altering only the camera perspectives and tactical focus across scenes.

Here is the complete blueprint for structuring a 4-part animated tactical lesson, using a concrete scenario: **Beating a 4-4-2 Low Block via Midfield Dismarking & Third-Man Runs.**

---

## 1. The Global Scene Setup (Establish Continuity Anchors)

Before writing individual prompts, define your **Global Scene Anchors**. Every prompt in the sequence _must_ share these exact visual variables:

- **Attacking Team:** Blue shirts, white shorts
- **Defensive Team:** Red shirts, dark shorts
- **Key Player Focus:** Blue #8 (Central Playmaker) & Blue #9 (Striker)
- **Environment:** Evening match, bright stadium floodlights, crisp green turf, light atmospheric haze

---

## 2. The 4-Act Prompt Structure

### Act 1: Tactical Setup (The Problem)

- **Goal:** Introduce the opponent's defensive structure (e.g., rigid 4-4-2 low block) and highlight spatial constraints.
- **Camera Style:** High, static overhead master-shot to establish geometry.

```text
/cinematic /overhead /deepfocus /nightscene Tactical overview looking straight down on a full soccer pitch. A team in red shirts is organized in a compact, rigid 4-4-2 low-block inside their own defensive third, locking down central space. The attacking team in blue shirts holds possession at the midfield line, probing for an opening. Long floodlight shadows stretch across the turf.

```

---

### Act 2: Individual Dismarking & Separation (The Mechanic)

- **Goal:** Zoom in on Blue #8 creating separation from his marker to open a passing lane (micro-mechanic).
- **Camera Style:** Pitch-level tracking shot with shallow depth of field to isolate player movement.

```text
/filmic /lowangle /steadicam /selectivefocus /volumetric Close tracking shot on the blue #8 midfielder. Blue #8 executes a sharp two-step dismarking run—checking toward the defender before exploding backward into the half-space. The red marker is caught flat-footed. Blue #8 receives a firm ground pass on the half-turn, with the surrounding players blurred softly in the background.

```

---

### Act 3: The Third-Man Combination (The Breakdown)

- **Goal:** Show the multi-player execution—Blue #8 plays into Blue #9 (the wall), who cushions a lay-off for Blue #11 sprinting through the seam.
- **Camera Style:** Mid-wide sideline shot with a dynamic focal shift.

```text
/documentary /wideangle /panright /rackfocus /rimlight Sideline tactical view. Blue #8 plays a crisp vertical line-breaking pass to blue #9 (striker). As two red center-backs collapse on blue #9, he cushions a blind one-touch layoff into the central seam. Camera rack-focuses to blue #11 arriving from deep in full stride to collect the ball behind the defensive line.

```

---

### Act 4: Match-Speed Execution & Outcome (The Solution)

- **Goal:** Demonstrate the entire sequence at full speed, ending with a shot on goal or cross, reinforcing tactical success.
- **Camera Style:** Dynamic cinematic angle following the play to its climax.

```text
/cinematic /wide /craneup /shallowdepth /volumetric Dynamic high-angle tracking shot at full match speed. The blue team executes a rapid three-pass combination to breach the red team's 4-4-2 low block. Blue #11 collects the lay-off inside the 18-yard box and strikes a low curling shot toward the far post, stadium lights illuminating mist kicked up from the turf.

```

---

## 3. Editing & Module Production Tips

| Production Stage        | Execution Strategy                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Clip Duration**       | Generate 4- to 8-second clips per act. Short, focused dynamic movements are easier for the model to render cleanly without physics degradation.                                                              |
| **Voiceover Alignment** | Write your voiceover narration _before_ generating video. Use Act 1 for tactical theory, Act 2 for technique coaching points, Act 3 for timing/cues, and Act 4 for summary.                                  |
| **On-Screen Graphics**  | Render clean video clips first in Google Flow, then use post-production software (ScreenFlow, Premiere, or DaVinci) to overlay tactical telestrator lines, player spotlight rings, or passing vector arrows. |
| **Pacing Control**      | Use slash commands like `/bullettime` or `/shallowdepth` specifically in Act 2/Act 3 to slow down critical coaching moments (like the moment of first touch or dismarking feint).                            |
