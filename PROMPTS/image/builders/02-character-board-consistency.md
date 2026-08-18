# 02 — Character Board (Multi-Angle Turnaround for Consistency)

**Purpose:** Generate a multi-panel reference sheet showing the same person from multiple angles  
**Use Case:** Ensures facial and body consistency across video shots with different camera positions  
**Platform:** GPT Image 2, Picsart Flow

## What This Builder Does

Creates a composite image with the same character shown from front, side, three-quarter and back views, plus close-up facial detail. All panels use identical wardrobe, lighting and expression — only the camera angle changes.

This locks character identity across shots and prevents "different actor" drift when the video model sees the character from a new angle.

## Template Prompt

```
[PASTE YOUR STYLE BIBLE HERE]

Character turnaround reference sheet, multi-panel composite showing the SAME person from multiple camera angles, evenly spaced with thin white gutters between panels.

CHARACTER: [Detailed physical description — age, gender, ethnicity, hair, eyes, face, skin, distinguishing marks, body type, height]

WARDROBE: [Complete outfit description head to shoes, including fabrics, fit, colors, accessories]

LIGHTING & SETUP: Clean neutral studio lighting, soft frontal key with gentle fill, flat off-white seamless background, consistent lighting intensity and direction across all panels. No background shadows.

PANELS (all panels show the same character in identical wardrobe):

Panel 1 — FRONT VIEW: Full-body standing shot, head to shoes in frame, feet shoulder-width apart, arms relaxed at sides, facing camera directly, neutral calm expression.

Panel 2 — SIDE PROFILE (LEFT): Full-body standing shot, same pose and stance, camera at 90° showing left side of body and face in pure profile, looking straight ahead parallel to lens.

Panel 3 — THREE-QUARTER VIEW: Full-body standing shot, same pose, camera at 45° angle showing front-left of body and face, subject looking slightly toward camera.

Panel 4 — BACK VIEW: Full-body standing shot, same pose, camera behind showing rear view of head, shoulders, back, legs and shoes, subject facing away.

Panel 5 — CLOSE-UP PORTRAIT: Tight head-and-shoulders only, camera at eye level, frontal view, subject looking directly into lens, neutral expression, shallow depth of field sharp on the eyes.

CRITICAL: Identical character identity, identical wardrobe, identical lighting and identical expression across all five panels. Only the camera angle changes. Photorealistic, natural skin texture with visible pores, realistic hair detail, accurate fabric texture, no beauty smoothing, perfect identity match.
```

## Example: Female Lead for Drama

```
Photorealistic natural portrait photography aesthetic with soft studio lighting and subtle film grain. Warm neutral color palette, natural skin tones, visible fabric texture. Mood is calm, approachable and authentic.

Character turnaround reference sheet, multi-panel composite showing the SAME woman from multiple camera angles, evenly spaced with thin white gutters between panels.

CHARACTER: South Asian woman, late 20s, medium-length straight black hair with subtle layering falling just past shoulders, centre part, dark brown eyes, full natural eyebrows, warm medium-brown skin with natural texture, small gold stud earrings, delicate gold chain necklace with a small pendant, calm neutral expression.

WARDROBE: Soft grey oversized knit cardigan worn open with rolled sleeves, cream ribbed fitted tank top underneath, high-waisted straight-leg medium-wash blue jeans with visible denim texture, clean white leather low-profile sneakers, minimal jewelry (only earrings and necklace mentioned above).

LIGHTING & SETUP: Clean neutral studio lighting with soft frontal key and gentle side fill, flat off-white seamless background, consistent soft lighting across all panels with no harsh shadows. No background shadows.

PANELS (all panels show the same woman in identical outfit):

Panel 1 — FRONT VIEW: Full-body standing shot, head to shoes in frame, feet shoulder-width apart, arms hanging relaxed at sides, weight evenly distributed, facing camera directly, calm neutral expression with soft eye contact.

Panel 2 — SIDE PROFILE (LEFT): Full-body standing shot, same standing pose, camera moved 90° to show pure left side profile, body and face in profile, looking straight ahead parallel to camera, same calm expression.

Panel 3 — THREE-QUARTER VIEW: Full-body standing shot, same pose, camera at 45° front-left showing angled view of face and body, subject looking slightly toward camera, same calm expression.

Panel 4 — BACK VIEW: Full-body standing shot, same pose and stance, camera behind showing rear view of head with hair falling down back, cardigan draping down shoulders, jeans and shoes, subject facing completely away from camera.

Panel 5 — CLOSE-UP PORTRAIT: Tight framing from collarbone to top of head, camera at eye level, frontal view, subject looking directly into lens with calm soft expression, shallow depth of field with sharp focus on eyes and face, cardigan and tank visible at bottom of frame.

CRITICAL: Identical face, identical hair length and style, identical outfit and identical lighting across all five panels. Only camera position changes. Photorealistic, visible skin texture and pores, realistic hair strands, natural fabric drape, no beauty filter, perfect identity consistency.
```

## Builder Variables

**Character Variables (Customize These):**

- Age range (early 20s, mid-30s, late 40s, etc.)
- Gender identity
- Ethnicity and skin tone (be specific: "warm medium-brown," "pale olive," etc.)
- Hair: length, texture, color, style (straight, wavy, curly, braided, etc.)
- Eyes: color, shape
- Face: structure, features, marks (freckles, scars, moles, etc.)
- Body type: slim, athletic, curvy, muscular, average, etc.
- Height relative build: tall and lean, short and stocky, etc.

**Wardrobe Variables:**

- Outer layer (jacket, cardigan, coat, vest)
- Mid layer (shirt, blouse, sweater, dress)
- Bottom (jeans, trousers, skirt, shorts)
- Footwear (sneakers, boots, heels, sandals)
- Accessories (jewelry, watch, bag, hat, glasses)
- Fabric callouts (knit, denim, cotton, leather, linen)

**Expression/Mood:**

- Neutral calm (most versatile)
- Slight smile (approachable)
- Serious focused (dramatic)
- Confident direct (assertive)

## Usage Tips

- **Neutral expression > character expression** — Smile/frown locks you into one emotion; neutral lets video do the acting
- **Describe hair from all angles** — "Shoulder-length" from front might read as "short" from back; add "falling down back"
- **Fabric = texture consistency** — "Oversized knit cardigan" prevents cardigan changing material between angles
- **"Same pose" repeated** — Explicitly say "same standing pose" in every panel or model will vary stance
- **Close-up last** — Tight portrait gives face detail that other panels lack; do it as fifth panel

## Integration with Video

Upload to Topview Canvas, name the node @char_lead (or similar), reference in video prompt:

```
REFERENCES: Use @char_lead for the woman's appearance throughout. Face, hair, wardrobe and body proportions must exactly match all angles shown in @char_lead.

0-4s: [Medium Shot] The woman walks into frame from the left, camera tracking her from three-quarter front angle. Her appearance matches @char_lead panel 3.

4-8s: [Close-Up] Camera pushes in to tight portrait as she turns to face lens. Facial detail and expression match @char_lead panel 5.
```

The video model sees the character from multiple angles upfront, reducing morph risk when camera moves.

## When to Use This Builder

✅ **Use Character Board when:**

- Character appears in multiple shots with different camera angles
- Video includes walk-arounds, turning, or orbiting camera moves
- Need rock-solid face and body consistency across a short film
- Character needs to be recognizable from any angle

❌ **Don't use Character Board when:**

- You only need facial expressions (use Expression Sheet)
- You need action poses (use Pose Board)
- Character has multiple costume changes (make separate boards per outfit)
- Scene requires character in specific environment (keep character/location separate)

---

**Builder:** Character Board (Multi-angle turnaround)  
**Panels:** 5 views (front, side, three-quarter, back, close-up portrait)  
**Consistency Anchor:** Identical character and wardrobe; only camera angle changes
