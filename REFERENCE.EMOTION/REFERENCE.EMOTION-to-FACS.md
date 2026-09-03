# Emotion-To-FACS Cross-Reference

Use this reference with [FACS Cheat Sheet](../REFERENCE.EMOTION.FACS/FACS-cheat-sheet.md) to translate the emotion vocabulary in [Complete Human Emotion Reference List](REFERENCE.EMOTION-LIST.MD) into facial-action direction.

> **Interpretation boundary:** FACS codes observable facial movement, not a person's internal state. The AU combinations below describe common _displayed-emotion_ prototypes or useful creative starting points. Read timing, asymmetry, intensity, baseline, culture, situation, voice, posture, and gaze before inferring emotion.

## Core Displayed-Emotion Signatures

These seven combinations are adapted from [iMotions' FACS visual guidebook](https://imotions.com/blog/learning/research-fundamentals/facial-action-coding-system/). They are the highest-confidence mappings in this reference.

| Emotion group from list | Signature AU combination                  | Visual reading                                                                         |
| ----------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------- |
| Joy / happiness         | AU6 + AU12                                | Cheeks lift; lip corners pull up and back.                                             |
| Sadness                 | AU1 + AU4 + AU15                          | Inner brows raise and draw together; lip corners depress.                              |
| Surprise                | AU1 + AU2 + AU5 + AU26                    | Brows raise, eyes widen, jaw drops.                                                    |
| Fear                    | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26 | Raised/drawn brows, widened and tightened eyes, laterally stretched lips, dropped jaw. |
| Anger                   | AU4 + AU5 + AU7 + AU23                    | Lowered brow, intense eyes, tightened lids and lips.                                   |
| Disgust                 | AU9 + AU15 + AU16                         | Nose wrinkles; lip corners and lower lip draw downward.                                |
| Contempt / disdain      | AU12 + AU14, unilateral                   | One-sided lip-corner pull and dimpling.                                                |

## Category Cross-Reference

**Confidence key:** `Prototype` is an iMotions-listed displayed-emotion signature. `Direction` is a creative facial-direction starting point, not a validated one-to-one FACS emotion label. `No fixed facial code` means use narrative and performance context rather than forcing an AU recipe.

| Emotion-list category       | FACS starting point                                                  | Confidence           | Direction for performance or prompting                                                                                              |
| --------------------------- | -------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Joy / Happiness             | AU6 + AU12; optionally AU25 or AU26 for an open smile/laugh          | Prototype            | Scale AU6/AU12 from warm, restrained enjoyment to broad delight.                                                                    |
| Sadness                     | AU1 + AU4 + AU15                                                     | Prototype            | For grief or anguish, increase duration and intensity; avoid assuming tears from AUs alone.                                         |
| Anger                       | AU4 + AU5 + AU7 + AU23                                               | Prototype            | Add AU25/AU26 only when speech, shouting, or threat context calls for mouth opening.                                                |
| Fear                        | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 + AU26                            | Prototype            | Use a brief onset for startle; sustained, lower-intensity tension can support worry or dread.                                       |
| Disgust                     | AU9 + AU15 + AU16                                                    | Prototype            | Use AU9 as the primary rejection cue; keep the pattern distinct from contempt.                                                      |
| Surprise                    | AU1 + AU2 + AU5 + AU26                                               | Prototype            | A rapid onset and short hold reads more like startle or astonishment.                                                               |
| Love & Affection            | AU6 + AU12 at low-to-moderate intensity; soft gaze and context       | Direction            | Use a gentle smile rather than a fixed "love" face; intimacy is mainly contextual.                                                  |
| Loneliness & Isolation      | AU1 + AU4 + AU15 may support sadness                                 | Direction            | Favor a subdued or sad display; isolation itself has no unique facial signature.                                                    |
| Shame & Guilt               | No fixed facial code                                                 | No fixed facial code | Consider gaze/head lowering (AU54/eye direction) with restrained sadness or tension; do not equate either state with a single face. |
| Pride & Confidence          | AU6 + AU12 may support positive pride                                | Direction            | Couple a controlled smile with head/posture direction; confidence is not encoded by a fixed AU set.                                 |
| Jealousy & Envy             | Blend anger, sadness, fear, or contempt cues as context requires     | Direction            | Choose the dominant appraisal first: threat, loss, rivalry, or resentment.                                                          |
| Hope & Optimism             | AU6 + AU12 may support positive expectation                          | Direction            | Use a light, anticipatory smile; distinguish from surprise by avoiding wide-eyed AU5/AU26.                                          |
| Despair & Hopelessness      | AU1 + AU4 + AU15 may support sadness                                 | Direction            | A sustained, low-energy sad display can support despair; hopelessness is contextual.                                                |
| Nostalgia & Wistfulness     | AU6 + AU12 or AU1 + AU4 + AU15, often mixed                          | Direction            | Use a small smile with softened sadness for bittersweet recollection.                                                               |
| Calm & Peace                | Neutral baseline; minimize high-arousal AUs                          | Direction            | Avoid rigid stillness; relaxed eyelids, jaw, and lips plus breath and gaze carry the state.                                         |
| Anxiety & Unease            | Partial fear cues, especially AU4 + AU5/AU7; optional AU20           | Direction            | Keep the pattern incomplete or fluctuating rather than presenting the full fear prototype.                                          |
| Confusion & Uncertainty     | No fixed facial code                                                 | No fixed facial code | Use temporal shifts, gaze changes, and selective brow/lid movement; context decides the reading.                                    |
| Anticipation & Expectation  | AU1 + AU2 + AU5 may support alert anticipation                       | Direction            | Add a restrained AU12 for positive expectation or partial AU4/AU7 for apprehension.                                                 |
| Boredom & Apathy            | No fixed facial code                                                 | No fixed facial code | Use neutral or reduced activation; distinguish emotional apathy from fatigue through context.                                       |
| Curiosity & Interest        | AU1 + AU2 + AU5 may support attentive interest                       | Direction            | Keep jaw closed unless surprise is intended; direct gaze and head orientation matter strongly.                                      |
| Gratitude & Appreciation    | AU6 + AU12                                                           | Direction            | A warm AU6/AU12 smile can support appreciation, but gratitude needs interaction context.                                            |
| Relief & Release            | Fear or tension cues resolving toward AU6 + AU12                     | Direction            | Make the transition visible: release AU4/AU7/AU23, then introduce a small smile or relaxed mouth.                                   |
| Trust & Safety              | AU6 + AU12 at low intensity; neutral relaxation                      | Direction            | Use a non-defensive baseline and subtle positive affect; trust is primarily relational.                                             |
| Betrayal & Distrust         | Partial anger, sadness, fear, or contempt cues                       | Direction            | Let the narrative choose the dominant response; no universal distrust configuration exists.                                         |
| Empathy & Understanding     | AU6 + AU12 or a restrained sad display, depending on target emotion  | Direction            | Match the other person's affect first; empathy is shown by responsive timing and context.                                           |
| Rejection & Exclusion       | Sadness, anger, or contempt cues depending on role                   | Direction            | Separate the rejected person's likely sadness from the rejecter's possible contempt or anger.                                       |
| Admiration & Respect        | AU1 + AU2 + AU5 may support awe/attention; optional AU6 + AU12       | Direction            | Use widened attention with a soft positive expression; respect is not a fixed facial prototype.                                     |
| Contempt & Disdain          | AU12 + AU14, unilateral                                              | Prototype            | Preserve asymmetry; a bilateral smile changes the reading.                                                                          |
| Success & Accomplishment    | AU6 + AU12                                                           | Direction            | A stronger, more sustained positive smile can support success; posture and action establish achievement.                            |
| Failure & Inadequacy        | Sadness prototype or shame-related direction                         | Direction            | Choose loss (sadness), self-evaluation (shame/guilt), or frustration (anger) rather than conflating them.                           |
| Determination & Resolve     | AU4 + AU7 + AU23 may support effortful focus                         | Direction            | Use carefully: the pattern overlaps anger. Direction of gaze, context, and controlled intensity differentiate resolve.              |
| Frustration & Stagnation    | Anger prototype at lower intensity; optional partial sadness         | Direction            | Favor AU4 and AU7 tension before escalating to the full anger pattern.                                                              |
| Awe & Wonder                | AU1 + AU2 + AU5; optional AU26 for astonishment                      | Direction            | Begin with surprise-like attention, then soften into a sustained, reflective state.                                                 |
| Dread & Existential Fear    | Partial fear pattern or subdued sadness                              | Direction            | Use incomplete fear with sustained tension; existential content is conveyed through story, not a unique face.                       |
| Acceptance & Surrender      | Neutral relaxation; optional low-intensity AU6 + AU12 or sad residue | Direction            | Show release of facial tension rather than a mandatory positive smile.                                                              |
| Energy & Vitality           | AU6 + AU12; optional AU5 for alertness                               | Direction            | Keep intensity buoyant without drifting into surprise.                                                                              |
| Exhaustion & Depletion      | No fixed facial code                                                 | No fixed facial code | Reduced activation, lid changes, posture, blink rate, and pacing are more informative than a fixed AU recipe.                       |
| Tension & Pressure          | AU4 + AU7 + AU23; optional AU20                                      | Direction            | This overlaps anger and fear; specify whether pressure is effort, threat, or irritation.                                            |
| Comfort & Ease              | Neutral relaxation; low-intensity AU6 + AU12                         | Direction            | Relax jaw and lips; avoid high-intensity cheek lift unless joy is intended.                                                         |
| Inspiration & Creativity    | AU1 + AU2 + AU5 may support attentiveness                            | Direction            | Use gaze, pacing, and task context; inspiration has no dedicated FACS signature.                                                    |
| Beauty & Aesthetic Pleasure | AU6 + AU12; optional AU1 + AU2 + AU5 for wonder                      | Direction            | Combine soft joy with attentive openness when the experience is awe-like.                                                           |
| Premium & Luxury            | No fixed facial code                                                 | No fixed facial code | This is a product or social-value descriptor, not an emotion; use the intended viewer response instead.                             |
| Present-Focused             | Neutral relaxation; attentive AU1/AU2/AU5 if engaged                 | Direction            | Mindfulness is better expressed through stable gaze, breathing, and low facial tension.                                             |
| Past-Focused                | Sadness or mixed nostalgia direction                                 | Direction            | Choose regret, warmth, grief, or longing rather than treating past-focus as a facial expression.                                    |
| Future-Focused              | Anticipation direction; partial fear or joy as appropriate           | Direction            | Use the valence of the expectation to select the cues.                                                                              |
| Light & Bright              | Low-to-moderate AU6 + AU12                                           | Direction            | This is an atmospheric label; keep the display positive and open without overacting.                                                |
| Dark & Heavy                | Sadness, anger, or fear direction                                    | Direction            | Select a concrete emotion; mood descriptors alone cannot determine an AU set.                                                       |
| Quiet & Still               | Neutral relaxation                                                   | Direction            | Favor stillness with micro-movements rather than an inert expression.                                                               |
| Intense & Dramatic          | Increase intensity and duration of the chosen base pattern           | Direction            | Pick the underlying emotion first; intensity modifies it rather than supplying its own AUs.                                         |
| Calm Before Storm           | Neutral or partial tension cues                                      | Direction            | Hold a calm baseline with subtle AU4/AU7/AU23 tension only when foreshadowing is desired.                                           |
| Belonging & Community       | AU6 + AU12                                                           | Direction            | Shared smiles and reciprocal timing communicate belonging more reliably than a single face.                                         |
| Alienation & Otherness      | Sadness, fear, or neutral withdrawal depending on context            | Direction            | Do not treat identity or social status as a facial code.                                                                            |
| Collective Joy              | AU6 + AU12                                                           | Direction            | Synchrony, gaze, body orientation, and scene context establish the collective dimension.                                            |
| Collective Grief            | Sadness prototype                                                    | Direction            | Vary the display across people; collective grief should not look facially uniform.                                                  |
| Righteousness & Justice     | Anger, pride, or joy direction depending on appraisal                | Direction            | Separate moral outrage from satisfaction or confidence.                                                                             |
| Injustice & Wrongdoing      | Anger, fear, sadness, or disgust direction                           | Direction            | Assign the affected person's response and the observer's response separately.                                                       |
| Altruism & Generosity       | AU6 + AU12 at low intensity; neutral warmth                          | Direction            | Helping behavior and interaction provide the stronger evidence.                                                                     |
| Growth & Evolution          | No fixed facial code                                                 | No fixed facial code | Use the emotion produced by change, such as hope, pride, fear, or relief.                                                           |
| Loss & Endings              | Sadness prototype; optional mixed nostalgia direction                | Direction            | Choose grief, relief, regret, or acceptance based on narrative meaning.                                                             |
| New Beginnings              | Anticipation or joy direction                                        | Direction            | Use attentive openness for uncertainty; add AU6/AU12 for positive renewal.                                                          |

## Intensity, Asymmetry, And Mixed States

- **Intensity modifiers:** Apply `slightly` through `overwhelmingly` to the amplitude, onset speed, and hold duration of the selected AU pattern. They do not require new AU codes.
- **Mixed emotions:** Build each component as a readable, time-separated or asymmetric pattern. For example, `bittersweet` can move between low-intensity AU6 + AU12 and AU1 + AU4 + AU15; `excited and nervous` can pair anticipation with partial fear cues.
- **Ambivalence:** Avoid presenting two full prototypes at the same instant unless the ambiguity is intentional. Alternation, asymmetry, and a held neutral baseline usually read more naturally.
- **Atmospheric labels:** Terms such as `premium`, `dark`, `quiet`, and `electric` describe tone or design direction. They should modify lighting, pacing, camera, setting, and performance rather than be treated as FACS labels.

## Working Method

1. Choose the precise emotion term from the source list.
2. Locate its category above and begin with the listed AU direction.
3. Set intensity, symmetry, onset, and release based on the scene beat.
4. Add gaze, head movement, voice, posture, and situational context before assigning emotional meaning.
5. For emotion AI or research, treat these as hypotheses and validate against the specific coding scheme, population, and task.

## Sources

- [Complete Human Emotion Reference List](REFERENCE.EMOTION-LIST.MD)
- [FACS Cheat Sheet](../REFERENCE.EMOTION.FACS/FACS-cheat-sheet.md)
- [iMotions: Facial Action Coding System (FACS) - A Visual Guidebook](https://imotions.com/blog/learning/research-fundamentals/facial-action-coding-system/)
