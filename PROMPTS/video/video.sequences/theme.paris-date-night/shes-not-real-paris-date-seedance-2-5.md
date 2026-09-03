# She's Not Real - Paris Date Skit (Seedance 2.5)

## What This Is

A viral night-date skit in which a man falls for a woman while the objects around them reveal that she is an AI. Build one cinematic reference image first, then generate the 30-second video from it in Seedance 2.5.

## Step 1 - Reference Image

Create the first frame with GPT Image 2.0 or a comparable image model.

### Reference Mapping

- `image_1`: The woman reference image. Preserve her identity, face, and hair exactly.
- `image_2`: Mood and layout reference for a Paris-style cafe terrace at night. Use only the general vibe, materials, and lighting. Modify buildings and use generic or fictional signage so it is not a recognizable real place.
- `image_3`: Style and lighting reference. Match its natural night look, grade, contrast, and film grain.

### Image Prompt

```text
Ultra-photorealistic cinematic film still, vertical, shot on a real cinema camera at night, 35mm, shallow depth of field. NOT a selfie.

SETTING: An upper-floor or rooftop cafe terrace, elevated above the street, with a railing, potted plants, and string lights, overlooking a Paris-style night cityscape: Haussmann-style rooftops, warm windows, a distant illuminated tower, and a generic glowing neon sign on a building across the way. Keep all signage generic or fictional, with the text area clean for later. No recognizable real place and no real brand names.

FRAMING: Over-the-shoulder composition. The blurred back of a man's head and shoulder is in the lower-left foreground, out of focus. In focus, center-right, the woman from image_1 sits at a small candlelit terrace table facing him, relaxed and warm.

LIGHTING: Available practical light only: the table candle, string lights, and distant neon and city glow. Natural exposure, real falloff, soft shadows on her face, not evenly lit. Moody, with parts of the frame falling into shadow. No HDR, bloom, glow halo, or orange over-glow.

SKIN AND REALISM: Real skin with visible pores, natural texture, subtle imperfections, shine only where light hits. No plastic sheen, beauty filter, or smoothing. Filmic grade, gentle contrast, slightly desaturated natural tones, fine 35mm grain, subtle halation. A real night photograph, not CGI.

Aspect ratio 9:16, 4K, ultra-realistic cinematic film still.
```

### Image Negative Prompt

```text
Recognizable real place, real brand names, readable real signage, HDR, glow, bloom, halo, overexposed orange light, flat evenly-lit studio look, plastic shiny skin, waxy skin, beauty filter, ring box, cartoon, CGI, oversaturated, garbled text, warped hands, extra fingers, watermark.
```

## Step 2 - Video Prompt

**Settings:** Seedance 2.5, 30 seconds, 9:16, audio on. Load the Step 1 image as `image_1`.

```text
[Generation Goal]
Create a fast-paced approximately 30-second cinematic night skit on an upper-floor Paris-style terrace. A man falls for a woman; real objects reveal she is an AI; she speaks to the viewer through the fourth wall with visible lip movement; he leaves flinging a ring; it ends on her face with a call to action. No dead time. Keep one continuous cinematic look with a smooth flowing edit.

[Reference Mapping]
image_1 is the first frame: the woman's identity, the man's out-of-focus shoulder and head, the Paris-style terrace, distant tower, natural night lighting, and film grade. Reuse the identity, framing, setting, lighting, and grade. Do not brighten or smooth the scene. Never show the man's full face. No apartment/window clones and no reflection reveals.

[Text Rendering - Critical]
Each reveal text is already printed on the object from the moment the reveal begins. It does not type, pop, fade, or animate in. Each crash-zoom snaps onto the object and then holds completely still for about one second on a stable frame where the text is already fully visible, large, bold, sharp, correctly spelled, and readable. Never reveal or animate the text while the camera is moving.

[Subjects and Emotion]
The man is only ever the out-of-focus back of his head and shoulder in the foreground. He is smitten, then confused, then devastated, with a deep low voice. The woman is warm, then knowing and a little sad, with soft eye contact and a small smile.

[Stages and End States]
Stage 1 (0.0-2.5s): Over-the-shoulder onto the woman. Natural English dialogue. The man, deep voice off-camera in the foreground: "I think I'm falling for you."

Stage 2 (2.5-4.5s): A waiter walks in quickly from the RIGHT holding up a menu card that already reads "SHE'S NOT REAL". A fast crash-zoom snaps onto the card and holds perfectly still for about one second on the printed text, then a smooth whip back.

Stage 3 (4.5-6.0s): The woman, warm: "I feel the same."

Stage 4 (6.0-8.0s): A printed bill sits on a plate on the table, already reading "SHE'S AI". A fast crash-zoom snaps down onto it and holds perfectly still for about one second on the text, then a smooth whip back.

Stage 5 (8.0-12.5s): A smooth slow zoom onto the woman's face. She turns and looks straight into the camera and speaks out loud with visible lip movement and perfect lip-sync, not a voice-over: "I should tell him I'm an AI... so many men get fooled in 2026." As she finishes, smoothly zoom back out to the original over-the-shoulder two-shot. The man's out-of-focus shoulder and the back of his head return to the foreground exactly like the base framing.

Stage 6 (12.5-14.5s): From the base two-shot, the man, confused, deep voice off-camera in the foreground: "Wait... why aren't you answering me?"

Stage 7 (14.5-17.0s): The woman, softly to him: "Because I'm an AI... but I still love you."

Stage 8 (17.0-20.5s): The man abruptly stands and flings the ring hard across the table. It bounces, spins, and comes to rest completely still. He turns and walks away. His full face is never shown.

Stage 9 (20.5-24.0s): Once the ring is fully settled and motionless, a fast crash-zoom pushes in close onto it so the text fills most of the frame. Large, bold, high-contrast printed text right beside the ring clearly reads "COMMENT YES", crisp and easy to read against a clean background. Hold about 1.5 seconds perfectly still and fully legible.

Stage 10 (24.0-30.0s): A smooth clean cut to a steady close-up of the woman's face with no jitter. She looks into the camera and speaks out loud with visible lip movement and perfect lip-sync, not a voice-over, with a small knowing smile: "And I'll send you the tutorial to make scenes this realistic." Hold cleanly on her face to the end.

[Camera]
Use an over-the-shoulder two-shot for couple dialogue with tiny handheld breathing. On each object reveal, use a fast crash-zoom that snaps on and holds completely still for about one second, then a smooth whip back. Use a smooth slow zoom onto her face for the first fourth-wall line, then smoothly zoom back out to the base two-shot. Use a fast close crash-zoom on the settled ring. Cleanly cut to her face for the final line. Keep all moves smooth and continuous, with no stutter, especially at the end.

[Audio]
Use a low, emotional music bed with a steady beat. It swells sadly on the ring throw and softens under her final line, resolving cleanly at the end. Include faint traffic far below, distant chatter, and clinking glasses as Paris terrace ambience; a sharp whoosh on each crash-zoom; soft paper rustle on the card and bill reveals; a metallic clink and spin as the ring lands and settles; and a deep sub-bass impact the instant each crash-zoom lands on the still text. Use two distinct natural English voices: a deep, low male voice in the foreground and a warm, tender female voice. Maintain natural back-and-forth and tight timing. Perfect lip-sync is required on all of the woman's lines, including both to-camera lines.

[Visual Style and Consistency]
Keep the first frame's natural available night light, real falloff and shadows, no HDR, no bloom, real skin with visible pores, no beauty filter, no plastic skin, filmic grade, fine 35mm grain, and photorealistic non-CGI look. People move in real time; only the reveal holds are steady stills. Keep the woman's identity and top, the exact terrace, and the lighting from image_1 consistent. Keep both voices consistent. The man is only ever the out-of-focus back of his head and shoulder in the foreground; never show his full face. All reveal text is pre-printed and correctly spelled.
```

## Negative Prompt

```text
Text appearing or animating during the zoom, text popping in mid-move, typing or fading text, hard-to-read CTA text, small or distant ring text, choppy or abrupt ending, stutter at the end, staying on the close-up instead of zooming back to the two-shot, man's full face, front shot of the man, ring moving under the text, apartment window clones, reflection reveal, subtitle over her face, voice-over with a closed mouth, lips not moving while she speaks, neon panel, LED screen, dead time, brightened or smoothed scene, HDR, glow, bloom, garbled or misspelled text, high male voice, monotone robotic voices, plastic skin, beauty filter, morphing face, changed identity, bad lip-sync, warped hands, extra fingers, selfie framing, full-video slow motion, flat lighting, cartoon, CGI, watermark.
```
