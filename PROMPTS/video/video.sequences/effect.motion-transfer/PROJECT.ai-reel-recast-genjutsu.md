# AI Reel Recast Project

**Workflow:** GPT Image 2 character sheet (4K) -> approve reference -> Genjutsu video-to-video motion transfer

## Global Recast Contract

Apply these rules to every reel.

- **Format:** Preserve each source clip's native vertical 9:16 aspect ratio.
- **Motion transfer only:** Preserve camera movement, framing, edits, timing, pace, performance blocking, dialogue, and on-screen text exactly. Replace only the named on-screen character(s).
- **Original characters only:** Do not use a real celebrity, public figure, or person from a styling reference as the generated character.
- **Reference workflow:** Build and approve a 3-panel character sheet before the video pass. Attach the source clip and the approved sheet(s) to Genjutsu.
- **Prompt discipline:** Do not introduce new cuts, camera moves, scene elements, actions, dialogue, text, or VFX that are not in the source clip.

## Universal Genjutsu Closing Constraint

Append this block to every reel prompt.

```text
MOTION TRANSFER ONLY: preserve the source video's camera movement, lens, framing, shot scale, edit points, timing, pacing, blocking, dialogue, on-screen text, environment, lighting, and sound exactly. Replace only the specified character(s). No new camera angles, cuts, props, actions, text, or background changes.

IDENTITY LOCK: approved character-sheet identity and wardrobe remain stable in every frame, including profile, motion-blur, overlap, and back-facing frames. No celebrity or public-figure likeness, no reversion to the source performer, no face drift, body morphing, cross-contamination between characters, duplicated limbs, warped hands, clothing-color drift, background wobble, or watermark.
```

---

## Reel 1 - NYC Street Walk

**Source clip:** A woman walks on a New York street in hair curlers and a fur coat, using the source track and timing.

**Reference input:** `@image1` - approved 3-panel sheet for the original character.

### Genjutsu Prompt

```text
Replace the walking woman in the source video with the original character from @image1: an East Asian woman wearing an orange fur jacket, orange mini dress, and blue heels. Keep her approved facial identity, build, hairstyle, and wardrobe stable across every frame.

Transfer the original walking motion, arm swing, head movement, pace, timing, camera movement, dialogue, on-screen text, and source audio exactly. Preserve the New York street, all background people, buildings, lighting, and the source clip's full edit rhythm without modification. Her jacket, dress, and hair respond naturally to the original movement while retaining the character-sheet styling.

MOTION TRANSFER ONLY: preserve the source video's camera movement, lens, framing, shot scale, edit points, timing, pacing, blocking, dialogue, on-screen text, environment, lighting, and sound exactly. Replace only the specified character(s). No new camera angles, cuts, props, actions, text, or background changes.

IDENTITY LOCK: approved character-sheet identity and wardrobe remain stable in every frame, including profile, motion-blur, overlap, and back-facing frames. No celebrity or public-figure likeness, no reversion to the source performer, no face drift, body morphing, cross-contamination between characters, duplicated limbs, warped hands, clothing-color drift, background wobble, or watermark.
```

---

## Reel 2 - Cliff Vehicle-Stunt Action

**Source clip:** A two-performer stunt sequence: the lead jumps between a falling bus and a car at a cliff edge; a woman remains seated in the car.

**Reference inputs:**

- `@image1` - original male lead character sheet
- `@image2` - approved female character sheet

### Character Direction

- **Male lead:** Original action-hero character, early 30s, tan-brown skin, short slicked-back black hair, light stubble; deep-brown leather jacket, charcoal-gray tee, black jeans, tan boots, thin silver chain, and black aviators.
- **Female character:** Original woman from `@image2`; rust/terracotta tailored blazer-dress with gold buttons, gold hoop earrings, thin gold necklace, gold bracelet or watch, nude block-heel pumps, and wavy dark-brown hair.
- **Do not use:** A red jacket, an Om pendant, or any real celebrity likeness.

### Genjutsu Prompt

```text
Replace exactly two source performers in the stunt clip. The roof-jumping lead becomes the original male character from @image1: tan-brown skin, short slicked-back black hair, light stubble, deep-brown leather jacket, charcoal-gray tee, black jeans, tan boots, thin silver chain, and black aviators. The woman seated in the car becomes the original character from @image2: rust/terracotta tailored blazer-dress with gold buttons, gold hoop earrings, thin gold necklace, gold bracelet or watch, nude block-heel pumps, and wavy dark-brown hair.

Preserve the stunt choreography, bus and car positions, cliff environment, physics, impacts, motion blur, camera movement, timing, edit points, dialogue, on-screen text, lighting, and sound exactly. The male lead performs the exact jump and the female character keeps the exact seated performance from the source. Maintain natural leather, hair, clothing, and jewelry motion under the source stunt forces. Do not use a red jacket, an Om pendant, or a real celebrity likeness.

MOTION TRANSFER ONLY: preserve the source video's camera movement, lens, framing, shot scale, edit points, timing, pacing, blocking, dialogue, on-screen text, environment, lighting, and sound exactly. Replace only the specified character(s). No new camera angles, cuts, props, actions, text, or background changes.

IDENTITY LOCK: approved character-sheet identity and wardrobe remain stable in every frame, including profile, motion-blur, overlap, and back-facing frames. No celebrity or public-figure likeness, no reversion to the source performer, no face drift, body morphing, cross-contamination between characters, duplicated limbs, warped hands, clothing-color drift, background wobble, or watermark.
```

---

## Reel 3 - Cyber-Mythology Prophecy

**Source clip:** A multi-armed deity-like statue, an ash-covered sage delivering the source dialogue, a baby, and a goddess holding the baby amid skull imagery.

**Reference inputs:**

- `@image1` - original cyber-samurai sheet
- `@image2` - cyber-mythology character and material reference sheet

### Recast Assignments

| Source role        | Replacement                                           | Preserve exactly                                     |
| ------------------ | ----------------------------------------------------- | ---------------------------------------------------- |
| Warrior            | Original cyber-samurai                                | Source motion, body position, timing, and action.    |
| Multi-armed statue | AI war-deity mech                                     | Exact source pose and arm count.                     |
| Sage               | Cyber-Viking Monk                                     | Source performance, dialogue, and on-screen text.    |
| Goddess            | Chrome-gold empress with organic human face and hands | Source pose, emotional warmth, and baby interaction. |
| Baby               | Fully human, unchanged                                | Original appearance and action.                      |

### Genjutsu Prompt

```text
Replace only the named characters in the source prophecy clip with an original cyber-mythology recast. The warrior becomes the original cyber-samurai from @image1. The multi-armed deity-like statue becomes an AI war-deity mech that preserves the exact source multi-arm pose and exact arm count. The sage becomes an original Cyber-Viking Monk: pale weathered ceramic-metal plating with glowing blue circuit cracks; braided iron-gray segmented-metal beard; horned iron crown or helm with one glowing red rune at the third-eye position; fur-and-metal shoulder pauldron; rune-etched vambraces; weathered leather-and-dark-metal robe with glowing Norse-rune embroidery; rune-etched war staff. Keep the source dialogue and on-screen text exactly unchanged.

Replace the goddess with an original chrome-gold empress who retains a soft organic human face and hands, preserving emotional warmth rather than becoming fully robotic. Keep the baby completely unchanged and fully human. Preserve the source skull imagery, setting, lighting, positions, motions, pacing, camera movement, edit points, dialogue, on-screen text, and sound exactly.

MOTION TRANSFER ONLY: preserve the source video's camera movement, lens, framing, shot scale, edit points, timing, pacing, blocking, dialogue, on-screen text, environment, lighting, and sound exactly. Replace only the specified character(s). No new camera angles, cuts, props, actions, text, or background changes.

IDENTITY LOCK: approved character-sheet identity and wardrobe remain stable in every frame, including profile, motion-blur, overlap, and back-facing frames. No celebrity or public-figure likeness, no reversion to the source performer, no face drift, body morphing, cross-contamination between characters, duplicated limbs, warped hands, clothing-color drift, background wobble, or watermark.
```

---

## Reel 4 - Desi Glam Red Gown Street Walk

**Source clip:** Approximately 13 seconds, vertical 9:16. A woman with long dark wavy hair walks a European cobblestone street and crosswalk, ending with an over-the-shoulder look-back.

**Reference input:** `@image1` - approved final 3-panel character sheet for the original character.

### Final Recast Direction

Original Indian/South Asian female model with a sultry confident expression, long open wavy dark hair, smoky eye makeup, defined brows, and a deep red-berry lip. She wears a deep-red embellished saree-gown hybrid: fitted beaded bustier bodice, cutout waist, flowing pleated draped skirt, and sheer matching dupatta/pallu diagonally over one shoulder. Jewelry: statement ruby-red beaded choker, matching ruby drop earrings, and one or two delicate rings. No bag. Bare feet or nude strappy heels.

### Genjutsu Prompt

```text
Video-to-video motion transfer. Keep all original camera movement, motion, timing, and pacing of the source clip exactly unchanged: 9:16 vertical, approximately 13 seconds, street walk and final over-the-shoulder look-back on a cobblestone crosswalk.

Replace the subject with the original character from @image1, never a real celebrity likeness. She is an Indian/South Asian female model with a sultry confident expression, long wavy dark hair worn loose and flowing with the source video's original hair movement, bold smoky eye makeup, defined brows, and a deep red-berry lip. She wears a deep-red embellished saree-gown hybrid: fitted bustier-style beaded bodice, cutout waist detail, and flowing pleated draped skirt. A sheer dupatta/pallu drapes diagonally over one shoulder and moves naturally with her stride. Add a statement ruby-red beaded choker, matching ruby drop earrings, and delicate rings. No bag; keep her hands free, with one hand allowed near the waist wrap only where it matches the source pose. Bare feet or nude strappy heels.

Preserve the street, buildings, lighting, walking pace, and final look-back exactly as in the source footage. No changes to camera angle, cuts, duration, or background. The skirt and pallu move with natural stride-driven cloth physics, echoing the flow of the source trousers without changing the choreography.

MOTION TRANSFER ONLY: preserve the source video's camera movement, lens, framing, shot scale, edit points, timing, pacing, blocking, dialogue, on-screen text, environment, lighting, and sound exactly. Replace only the specified character(s). No new camera angles, cuts, props, actions, text, or background changes.

IDENTITY LOCK: approved character-sheet identity and wardrobe remain stable in every frame, including profile, motion-blur, overlap, and back-facing frames. No celebrity or public-figure likeness, no reversion to the source performer, no face drift, body morphing, cross-contamination between characters, duplicated limbs, warped hands, clothing-color drift, background wobble, or watermark.
```

### GPT Image 2 Character-Sheet Prompt (4K)

```text
Create a professional 3-panel character sheet for the original woman in the attached face reference. Preserve her exact facial identity in every panel: same bone structure, skin tone, hair texture, eye shape, and age. The same person appears in all three frames with no identity drift. Do not replicate a real celebrity or public figure.

BACKGROUND, ALL PANELS: Natural off-white or warm-ivory seamless studio cyclorama. Soft, clean, gently graduated backdrop with a gentle floor shadow under the feet. No gray, black, props, or clutter.

LAYOUT: One wide horizontal image divided into three equal vertical panels, with identical scale and lighting, separated by thin clean white dividers.

PANEL 1, LEFT, FACE CLOSE-UP: Head and shoulders; face camera straight on; chin level; sultry confident expression. 85mm lens, soft large-source key from camera left, subtle fill, natural catchlights. Sharp natural skin texture, smoky-eye detail, jewelry sparkle at ears and neck.

PANEL 2, CENTER, FULL BODY RIGHT-SIDE PROFILE: Full length, head to feet entirely in frame, standing tall with weight on the back foot. The camera sees her right ear, right cheek, and right shoulder; her nose points toward the right frame edge; her left arm is hidden behind her torso. 50mm lens, even studio light.

PANEL 3, RIGHT, FULL BODY LEFT-SIDE PROFILE: Exact mirror of panel 2. The camera sees her left ear, left cheek, and left shoulder; her nose points toward the left frame edge; her right arm is hidden behind her torso. Full length, head to feet in frame, same scale and lighting as panel 2. Panels 2 and 3 are a true opposing turnaround pair, never the same profile direction twice.

WARDROBE, IDENTICAL IN ALL PANELS: Deep-red embellished saree-gown hybrid with a fitted beaded bustier-style bodice, cutout waist detail, flowing pleated draped skirt, and sheer matching dupatta/pallu diagonally over one shoulder. Bare feet or nude strappy heels visible in full-body panels.

HAIR AND MAKEUP: Long dark hair, loose, wavy, and worn open; bold smoky eye makeup; defined brows; deep red-berry lip.

JEWELRY: Statement ruby-red beaded choker at the base of the neck, matching ruby drop earrings, and one or two delicate rings. No oversized or iced-out pieces.

RENDER: Hyper-real editorial studio photography, ultra-sharp 4K detail, natural skin texture with visible pores, realistic beadwork and fabric sheen, accurate ruby/gemstone refraction, clean high-key color grade, no heavy contrast.

NEGATIVE: Do not repeat the same profile direction in both full-body panels. No face morphing or age change between panels. No black or gray background. No warped hands or extra fingers. No cropped feet or head. No text, watermark, plastic AI skin, or real-person/celebrity identity replication.
```

### Superseded Direction (Archive Only)

**Glam Boss-Lady:** Emerald-green oversized pantsuit, sharp winged eyeliner, gold hoop earrings, slicked-back high ponytail, thin gold chain instead of tie, and black shoulder bag. This direction is replaced by the approved red-gown recast and should not be used for the final output.
