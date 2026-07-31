----------------------------------------------
IMAGE PROMPT — Double‑Exposure Silhouette Mask (True Detective‑style optional)
----------------------------------------------

---

Use this when you want a still image where the foreground is a mask and the background plate fills the interior.

Prompt:  
Double‑exposure silhouette composite. Create a clean foreground mask of the subject with crisp edges and no background. Fill the interior of the silhouette with the background plate, blending the textures seamlessly. Maintain strong contrast between the silhouette outline and the external background. Use soft internal blending, subtle film grain, muted noir tones, and atmospheric haze for a True Detective mood. Ensure the background plate is fully contained inside the silhouette with no spill outside the mask.

Add‑ons:

“high‑contrast rim lighting on silhouette”

“grainy analog noir palette”

“soft internal glow inside mask”

“desaturated Southern‑Gothic color grade”

---

## VIDEO WORKFLOW — Double‑Exposure Silhouette Mask (Foreground + Background Plate)

Video requires a multi‑step pipeline. Here’s the clean version you can follow:

STEP 1 — Generate Foreground Subject Cutout (Seedance Prompt)
You need a clean silhouette or subject mask.

Prompt:  
Hyper‑realistic photoreal foreground extraction. Isolate the subject cleanly with perfect contour accuracy, no background, and crisp edges. Neutral lighting for clean compositing. Output as a solid silhouette or high‑contrast cutout suitable for double‑exposure masking.

STEP 2 — Generate Background Plate (Seedance Prompt)
This is the internal fill (ocean, city, smoke, crime‑scene textures, etc.).

Prompt:  
Hyper‑realistic photoreal background plate with strong texture and atmospheric depth. High contrast, moody lighting, subtle film grain, and noir tone. Designed to be composited inside a silhouette mask.

STEP 3 — Composite the Two Layers (Editing Step)
Do this in Resolve, AE, Premiere, or CapCut.

Process:

Place foreground silhouette on top layer.

Place background plate on layer below.

Set the foreground layer as a mask (Luma Matte or Alpha Matte).

Invert if needed so the background fills the silhouette.

Add:

film grain

vignette

chromatic aberration

desaturation

soft glow inside mask

Add a neutral or textured external background behind everything.

This creates the double‑exposure effect.

STEP 4 — Add True Detective Mood (Optional)
If you want the gritty noir vibe:

Desaturate 20–40%

Warm highlights, cool shadows

Add cigarette‑smoke haze

Add analog film grain

Slight lens distortion

Slow, moody camera movement

Dust & scratches overlays

Soft amber + teal grade

This gives you the Season‑1 Rust Cohle aesthetic.

STEP 5 — Final Output
Export with:

Grain intact

Soft contrast

Clean silhouette edges

Background plate fully contained inside mask

ONE‑PROMPT DOUBLE‑EXPOSURE VIDEO (Foreground Mask + Internal Background Plate)
Prompt:  
Hyper‑realistic photoreal double‑exposure video. Create a clean, high‑contrast silhouette of the foreground subject with perfectly defined edges, no background, and neutral studio lighting. Fill the interior of the silhouette with a dynamic background plate that remains fully contained inside the mask — ocean waves, city lights, smoke, or textured landscapes — blending seamlessly with soft internal glow, analog film grain, and atmospheric depth. Maintain strong contrast between the silhouette outline and the external background, which should remain minimal, neutral, and unobtrusive. Use smooth camera motion, subtle haze, muted noir tones, and True‑Detective‑style desaturation. Ensure the background plate animates naturally inside the silhouette while the outer silhouette stays stable and crisp. Produce a cohesive double‑exposure composite entirely within a single generation pass.

🔧 Optional modifiers you can append
These let you tune the vibe without breaking the one‑prompt structure:

“Southern‑Gothic noir palette”

“grainy analog film texture”

“soft amber highlights, cool blue shadows”

“slow dolly‑in camera movement”

“crime‑scene investigation mood”

“VHS distortion and tape noise”

“high‑contrast rim lighting on silhouette”
