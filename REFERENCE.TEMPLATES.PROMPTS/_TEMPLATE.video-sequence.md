# [Sequence Name]

## Classification

**Product Category:** [Controlled product category, such as apparel, beverage, food, service-signage, fuel-signage, footwear, or product-set]

**Reveal Effect:** [Controlled reveal effect, such as self-stitching, self-writing, molten-formation, pneumatic-inflation, liquid-formation, rib-growth, component-assembly, or cinematic-light-reveal]

**Reveal Mechanism:** [What physically creates the reveal: thread, liquid, molten material, inflated segments, ribs, product components, light, or another material-specific mechanism]

**Sequence Type:** [Self-build / reference-match reveal / transformation / catalogue-to-film / other]

**Filename:** `reveal.<product>.<effect>.md`

## Description of Resulting Video or Video Sequence

[Brief 1-2 sentence description of what this sequence does, including key visual elements, duration, and style. Example: "A 10-second ultra-cinematic sequence showing X transforming into Y with dramatic camera movement and premium CGI quality."]

## Usage

[Comprehensive description of when and how to use this sequence. Include 2-3 sentences covering:]

[First sentence: Primary use cases and industries] Perfect for [industry/application 1], [industry/application 2], [industry/application 3], and [specific marketing context].

[Second sentence: Ideal scenarios and creative applications] Ideal for [specific scenario 1], [specific scenario 2], [creative approach], and [production type].

[Optional third sentence if needed: Additional context or unique selling points]

## Engines/Models

[Make sure to remember what engines, platforms or models this was orginally applied to, and store any special details that might effective a future reuse.]

## Prerequisites / Dependencies

[List required images, references, or storyboards needed to generate this sequence]

- Option 1: List specific required images (e.g., "Dependency #[number] - Reference image of subject", "Dependency #[number] - Character image", "Dependency #[number] - Storyboard reference")
- Option 2: If generates from scratch, write: "None - generates from scratch"
- Additional Note: If it's an image, and a prompt for the image is supplied, list it as "Dependency #[number] - Prompt"

## Storyboard Prompt

[OPTIONAL: Only include this section if the sequence requires a storyboard reference image to be created first]

[Create a detailed multi-panel storyboard description (typically 5-6 panels) that covers key moments in the sequence:]

**Panel 1 (0:00-X:XX):** [Describe the opening shot: camera position, subject placement, lighting, composition, what's happening visually, mood/atmosphere]

**Panel 2 (X:XX-X:XX):** [Describe the next key moment: camera movement, subject transformation/action, environmental changes, visual effects appearing, composition shifts]

**Panel 3 (X:XX-X:XX):** [Continue describing progression: mid-sequence actions, construction/assembly phases, transitions, dynamic moments]

**Panel 4 (X:XX-X:XX):** [Describe further progression: additional transformations, camera angles changing, effects building, story development]

**Panel 5 (X:XX-X:XX):** [Describe near-completion: elements coming together, final transformations beginning, camera positioning for hero shot]

**Panel 6 (X:XX-X:XX):** [Describe final hero shot: completed state, final camera position, lighting for maximum impact, triumphant/satisfying composition]

Style: [Overall aesthetic guidance - cinematography style, rendering quality, aspect ratio, lighting approach, any specific visual references like "Ultra-realistic CGI, Unreal Engine quality, cinematic composition, 16:9 format, each panel clearly showing camera position and key transformation moments"]

## Video Prompt

[The complete detailed prompt for video generation. This is the main content that will be used to create the sequence.]

**Duration:** [X seconds]. [Additional format specs if needed]

**Style:** [Overall visual style, quality level, rendering approach, cinematography aesthetic]

[STRUCTURE YOUR PROMPT WITH:]

**Scene Setup/Context:**
[Describe the starting environment, subject, lighting, camera position, overall mood]

**Timeline/Shot Breakdown:**
[Provide detailed shot-by-shot or second-by-second breakdown]

0:00-0:XX
[What happens in this time segment, camera movement, subject actions, visual effects, transformations]

0:XX-0:XX
[Continue with precise timing and descriptions]

[Continue for full duration...]

**Camera:**
[Specific camera movement instructions - dolly, orbit, static, handheld, tracking, etc.]

**Lighting:**
[Lighting setup, changes, atmospheric effects, time of day, mood lighting]

**Visual Effects/Technical Details:**
[Any specific VFX, CGI requirements, physics simulations, material properties, rendering notes]

**Quality/Technical Requirements:**
[Resolution, rendering engine, specific quality markers like "8K, HDR, ray tracing, photorealistic, no artifacts, stable motion"]

---

## Template Usage Notes:

1. **Naming Convention:** Use `reveal.<product>.<effect>.[title].md` for reveal sequences. Keep both dimensions explicit: the product or product category comes first, and the visual mechanism/effect comes second (e.g., `reveal.sneaker.component-assembly.nike-tiempo-shoe-assembly.md`, `reveal.beverage.molten-formation.coca-cola.md`). Use `seq.` for non-reveal sequences. If multiple variations of a technique are shown in a single file, extract them as separately-titled video sequence files without losing master or shared information in each file.

2. **Classification Rule:** Classify by the product being revealed and by the mechanism that makes the reveal visually distinctive. Do not use a generic `self-build` label when a material-specific effect is available.

3. **Description Guidelines:** Keep it concise but informative - mention duration, style, and key visual hook

4. **Prerequisites:** Be specific about what images/references are needed, or clearly state "None - generates from scratch"

5. **Storyboard Prompt:** Only include if the sequence is complex enough to benefit from pre-visualization or requires specific reference compositions

6. **Video Prompt:** This is the core content - be extremely detailed with timing, camera work, and visual specifications

7. **Usage Section:** Focus on practical applications, target industries, and marketing contexts to help users understand when to use this sequence

8. **Formatting:** Use consistent heading levels, clear time markers, and structured organization for easy scanning

9. **PROMPT MAINTENANCE:** make sure to ALWAYS add the prompt in totality in the "video prompt" section. I do not want to lose any detail or implied ordering of the original prompt by separating it into parts.
