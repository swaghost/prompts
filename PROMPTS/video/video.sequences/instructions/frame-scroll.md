[PROMPT: BEFORE/ASSEMBLED]
High-end studio product photograph of [YOUR PRODUCT], fully assembled and intact, floating dead center against a seamless matte light-grey studio background. Straight-on view, perfectly level camera, soft even studio lighting, one subtle soft shadow directly beneath the product, photorealistic, ultra sharp, high detail. Keep the product small enough in frame that there is generous empty space on every side. No text, no watermark, no hands, no props, no brand logos. Landscape 16:9.

[PROMPT: AFTER/EXPLODED]
High-end studio product photograph of the same [YOUR PRODUCT] as a clean exploded view: the outer shell or casing lifted apart and every major part and layer separated and floating in an organized, evenly spaced arrangement along one axis, like a technical teardown render. Same straight-on view, same perfectly level camera, same soft even studio lighting, same seamless matte light-grey studio background, one subtle soft shadow beneath. The core body of the product stays in the exact center at the same size, with the parts spreading outward around it. Photorealistic, ultra sharp, high detail. No text, no watermark, no hands, no props, no brand logos. Landscape 16:9.

[CONSISTENCY TIPS]
Three consistency tips:

1. generate the start frame first and only move on once you love it.
2. If Flow lets you reference or reuse that first image when generating the end frame, do that.
3. And if the two frames come out looking like different products, regenerate the end frame rather than fighting it in the video step, a retry here is cheap.

[PROMPT: MOTION]
The product slowly comes apart into an exploded view: the casing separates and the internal parts spread outward smoothly and evenly. Camera locked in place, background unchanged.

[PROMPT: WEBSITE ASSEMBLY]
Using this folder of image frames, build a scroll-linked image sequence on an HTML canvas. Preload all the frames first, then map the scroll position to the frame index so the animation plays frame by frame as the user scrolls, the same technique Apple uses on the AirPods page. Use GSAP and ScrollTrigger. Pin the canvas while the sequence plays, scrub it smoothly to scroll so there's no stutter, keep it sharp and centered on mobile, and add a graceful fallback if the frames are still loading. Give me a single self-contained file I can drop straight into my site.

How to get the most out of it 🎓

    🎯 Lock your two frames before you animate.
    The whole effect lives or dies on the start and end images. Generate them with the same subject, camera angle, and background so only the motion changes. If frame one and frame two look like two different products, the in-between will look like mush.

    🐢 More frames means smoother, but heavier.
    30fps on a 2 to 4 second clip is the sweet spot. Longer or higher means a buttery animation but a heavier page, so if it feels slow to load, ask the coding tool to compress the images or drop to every second frame.
    🪜 Brand new? Paste the build prompt exactly as-is.
    You do not need to understand the code. Drop the folder, paste the prompt, and ask the tool to "run it and show me a preview" so you can see it working before you touch anything.

    🧠 Power user? Feed it your real page.
    Paste your existing site code or design system first, tell it your section width, fonts, and breakpoints, and have it match your stack (React, Webflow embed, plain HTML) instead of generating a generic file.

The honest bit ✅
This is genuinely how the pro version works, but AI-generated frames can drift, a logo warps, a reflection flickers, an edge wobbles. Generate a couple of clips and pick the cleanest, and keep your animation short and simple (a rotation, an assembly, a single reveal) rather than a complex scene. Simple subjects on clean backgrounds give you the crispest result.
