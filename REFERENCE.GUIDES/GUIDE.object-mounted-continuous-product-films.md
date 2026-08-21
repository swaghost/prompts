# Object-Mounted Continuous Product Films

## Purpose

Generate hyper-dynamic single-take product films in which the virtual camera is mounted directly to the moving machinery, tool, or product instead of floating independently. The typical sequence moves from raw material through fabrication and ends with a wearable or presented product.

## Universal Prompt Architecture

Every prompt should include:

1. **Lock Reference:** Match the uploaded product image frame-for-frame: silhouette, colors, textures, typography, logos, and proportions.
2. **Shot Specification:** One continuous 10-second take, no cuts, fades, or artificial transitions.
3. **Setting:** A readable, lived-in workshop or production environment, never an empty void.
4. **Build State:** Start with incomplete raw material or disassembled components, not a finished product.
5. **Object:** Name the product and the exact visual features that must remain unchanged.
6. **Actions:** Describe the mechanical fabrication, assembly, handoff, and final presentation.
7. **Timecoded Timeline:** Assign camera angles, tool actions, and movement beats to exact time ranges.
8. **Camera Path Rule:** Make the object-mounted camera follow the literal geometry of the stitch, print, seam, hardware, or tool path.
9. **Style and Grade Lock:** Use crisp, neutral daylight and tactile documentary clarity; forbid unrequested color grades.
10. **Pacing, Audio, and Negative:** Specify fast percussive motion, diegetic manufacturing sounds, and artifact exclusions.

## Execution Workflow

1. Prepare a clean, high-resolution front-facing product reference with sharp brand marks and no compression artifacts or watermarks.
2. Use Image-to-Video mode and treat the reference as the absolute visual anchor.
3. Set the generation to 10 seconds and select 9:16, 16:9, or 1:1 as required.
4. Paste the complete prompt without truncating the architecture blocks.
5. Generate two to four variations and select the cleanest mechanical-to-wearer handoff.
6. Add subtle speed ramps at whip-pan points and layer diegetic sound aligned to the mechanical beats.

## Non-Negotiable Rules

- The camera is object-mounted for the entire duration. Never free-floating.
- No cuts, fades, morphing, or artificial transitions.
- Do not render a finished product before the fabrication action occurs.
- The camera follows literal geometry rather than using a generic straight dolly or flat pan.
- Preserve reference typography, logos, colors, textures, silhouette, and position.
- If the model cannot complete the 8-to-10-second handoff, split production into an 8-second fabrication/handoff pass and a 2-second wearer presentation pass using the exact final frame as the next seed.
