# 01 — Pose Board (Animation & Video Reference)

**Purpose:** Generate a single composite image showing the same character in 9 different action poses  
**Use Case:** Reference sheet for animation sequences, action scenes, or video tutorials where one character performs multiple movements  
**Platform:** GPT Image 2, Picsart Flow

## What This Builder Does

Creates a 3×3 grid with 9 identical views of the same character, each in a different action pose. All panels share the same character design, wardrobe, lighting and camera distance — only the pose changes.

This prevents character drift across multiple shots and ensures consistent body proportions, face structure and clothing during action sequences.

## Template Prompt

```
[PASTE YOUR STYLE BIBLE HERE]

Character pose reference sheet, 3×3 grid, 9 identical views of the SAME character shown from the same camera angle in 9 different action poses, evenly spaced with thin white gutters between cells.

CHARACTER: [Detailed physical description — age, gender, ethnicity, hair, face, body type, height, build]

WARDROBE: [Complete clothing description from head to shoes, including fabric types and fit]

LIGHTING & SETUP: Clean studio lighting, soft frontal key with gentle fill, flat off-white seamless background, identical camera distance (full-body head-to-shoes framing), identical lighting in every cell. No shadows on the background.

POSES, reading left to right, top to bottom:

Row 1 — (1) [Pose 1 description]; (2) [Pose 2 description]; (3) [Pose 3 description].
Row 2 — (4) [Pose 4 description]; (5) [Pose 5 description]; (6) [Pose 6 description].
Row 3 — (7) [Pose 7 description]; (8) [Pose 8 description]; (9) [Pose 9 description].

CRITICAL: Identical character identity, identical wardrobe, identical camera framing and identical lighting in all nine cells. Only the body pose changes. Photorealistic, natural body proportions, realistic fabric physics and clothing drape, no beauty smoothing, no pose repetition.
```

## Example: Martial Arts Tutorial

```
Photorealistic contemporary sports photography aesthetic with clean studio lighting and shallow depth of field on seamless white. Crisp focus, natural skin texture, visible fabric weave. Mood is instructional, energetic and precise.

Character pose reference sheet, 3×3 grid, 9 identical views of the SAME man shown from the same frontal camera angle in 9 different martial arts defensive poses, evenly spaced with thin white gutters between cells.

CHARACTER: East Asian man, early 30s, athletic build, short black hair in a textured crew cut, strong jawline, focused serious expression, medium-brown skin with natural texture.

WARDROBE: Traditional white cotton gi with black belt tied at the waist, sleeves rolled to mid-forearm, bare feet, no shoes.

LIGHTING & SETUP: Clean studio lighting with soft frontal key and gentle side fill, flat off-white seamless background, camera at chest height with 50mm lens, full-body framing from head to feet with headroom and floor space, identical distance in all cells. No background shadows.

POSES, reading left to right, top to bottom:

Row 1 — (1) Standing neutral ready position, feet shoulder-width, fists up at chest level; (2) High block, left arm raised overhead, right fist at ribs; (3) Low block, right arm sweeping down across body, left fist at shoulder.

Row 2 — (4) Side kick extension, left leg raised horizontal to the side, arms in guard; (5) Knife-hand strike, right hand extended palm-down at shoulder height, left hand pulled back; (6) Front stance punch, deep lunge forward on right leg, left fist extending straight ahead.

Row 3 — (7) Roundhouse kick, right leg raised and bent, turning torso, arms tucked; (8) Double-hand block, both forearms crossed in front of chest; (9) Back stance, weight on rear leg, front leg light, both fists in chamber at ribs.

CRITICAL: Identical face, identical gi, identical camera framing and identical lighting in all nine cells. Only the body pose changes. Photorealistic, realistic human proportions, natural fabric drape and fold, sharp detail on hands and feet, no pose duplication.
```

## Builder Variables

**Character Variables (Customize These):**

- Age, gender, ethnicity
- Hair style, color and length
- Facial features (eyes, nose, mouth, brows, marks)
- Body type (athletic, slim, muscular, average, etc.)
- Expression (neutral, focused, joyful, intense)

**Wardrobe Variables:**

- Complete outfit from head to shoes
- Fabric types (cotton, leather, denim, etc.)
- Fit and style (loose, fitted, oversized, etc.)
- Accessories (jewelry, hats, gloves, etc.)

**Pose Variables (Choose Theme):**

- Martial arts defensive/offensive moves
- Yoga asanas or stretching positions
- Dance steps or choreography beats
- Sports actions (throwing, catching, jumping)
- Everyday actions (sitting, walking, reaching, lifting)
- Performance gestures (conducting, singing, playing instrument)

## Usage Tips

- **Keep one variable changing** — If you change pose + expression + wardrobe, the model loses consistency
- **Describe poses with body part specificity** — "Left arm raised overhead, right fist at ribs" beats "blocking"
- **Action > mood** — "Leg extended horizontal, toes pointed" works better than "powerful kick"
- **Use anatomical terms** — Front leg, rear leg, left forearm, right shoulder (not vague "arm up")
- **Studio lighting = consistency** — Dramatic lighting causes shadows that read as different characters

## Integration with Video

Once generated, upload to Topview Canvas and reference in video prompts:

```
REFERENCES: Use @poses_hero for character appearance and body proportions throughout.

0-5s: Character performs the high block from @poses_hero cell 2, then transitions smoothly into the low block from @poses_hero cell 3.
```

The video model will interpolate between the static poses while maintaining character consistency.

## When to Use This Builder

✅ **Use Pose Board when:**

- Animating a single character through multiple actions
- Creating video tutorials (yoga, dance, martial arts, fitness)
- Blocking out fight choreography or action sequences
- Need consistent character across multiple action beats

❌ **Don't use Pose Board when:**

- You need facial expressions (use Expression Sheet instead)
- You need multiple camera angles (use Character Turnaround instead)
- You need character + environment (generate separately, reference both)

---

**Builder:** Pose Board (9-panel action reference)  
**Grid:** 3×3, full-body views, studio lighting  
**Consistency Anchor:** Identical character, wardrobe and camera; only pose changes
