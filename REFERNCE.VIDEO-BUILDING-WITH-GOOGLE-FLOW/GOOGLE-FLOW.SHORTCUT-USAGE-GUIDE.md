To achieve maximum rendering precision and avoid instruction conflict when using slash commands in Google Flow, structure your prompts using a **front-loaded hierarchy**. The generation model processes parameters in sequence: broad aesthetic foundation first, followed by camera geometry, motion parameters, optical focus, lighting, and finally the concrete subject narrative.

---

## The Command Ordering Hierarchy

Follow this precise 6-tier order within your prompt line:

```text
[1. Visual Style] -> [2. Framing & Angle] -> [3. Camera Movement] -> [4. Optics & Focus] -> [5. Lighting & Atmosphere] -> [Subject & Narrative Description]

```

### 1. Visual Style & Genre (The Foundation)

- **Purpose:** Sets global color grading, grain structure, and rendering style. Place these at the absolute beginning so the engine establishes the canvas first.
- **Commands:** `/filmic`, `/cinematic`, `/commercial`, `/documentary`, `/cyberpunk`

### 2. Framing & Camera Angles (The Setup)

- **Purpose:** Establishes spatial dimensions, field of view, and camera position relative to the scene.
- **Commands:** `/lowangle`, `/establishing`, `/wideangle`, `/tight`, `/overhead`, `/pov`

### 3. Camera Movement (The Dynamic Vector)

- **Purpose:** Directs spatial translation and tracking trajectory. Placing motion after framing ensures the camera moves _from_ and _along_ a well-defined angle.
- **Commands:** `/dollyin`, `/dollyout`, `/steadicam`, `/orbit`, `/craneup`, `/panleft`

### 4. Optics & Focus (The Lens Characteristics)

- **Purpose:** Fine-tunes depth of field, focal shifts, and lens artifacts onto the framing setup.
- **Commands:** `/shallowdepth`, `/rackfocus`, `/macro`, `/deepfocus`, `/bokeh`

### 5. Lighting & Atmosphere (The Environment Layer)

- **Purpose:** Illuminates the established camera composition and sets atmospheric depth.
- **Commands:** `/volumetric`, `/rimlight`, `/backlight`, `/spotlight`, `/nightscene`

### 6. Subject & Action Narrative (The Core Scene Description)

- **Purpose:** Detailed prose defining the central subject, action, context, and environment.

---

## Practical Example Breakdown

### ❌ Sub-optimal Prompt (Unstructured & Conflicting)

> A midfielder picking up the ball in open space, high contrast lighting, `/shallowdepth`, `/cinematic`, `/dollyin`, stadium lights beaming through fog, `/lowangle`, fast action, `/volumetric`.

_Why it degrades quality:_ Mixing style (`/cinematic`), motion (`/dollyin`), and lighting (`/volumetric`) throughout natural language causes token confusion, leading to camera jitter, washed-out lighting, or ignored parameters.

---

### ✅ Optimized Structure Example

> `/filmic /lowangle /dollyin /shallowdepth /volumetric` A soccer midfielder scanning the pitch, receiving a crisp ground pass under glowing stadium floodlights, smooth first touch into open space, subtle rain glistening on the turf.

---

### Breakdown of the Structure

| Command Tier        | Applied Command        | Function in Video Render                                                      |
| ------------------- | ---------------------- | ----------------------------------------------------------------------------- |
| **1. Visual Style** | `/filmic`              | Applies natural film grain and high-dynamic-range color science.              |
| **2. Framing**      | `/lowangle`            | Mounts the virtual camera low near turf level facing slightly upward.         |
| **3. Movement**     | `/dollyin`             | Smoothly advances the camera forward toward the midfielder during the action. |
| **4. Optics**       | `/shallowdepth`        | Blurs the background crowd and opposing players, isolating the main subject.  |
| **5. Atmosphere**   | `/volumetric`          | Renders visible light beams piercing through the stadium moisture/haze.       |
| **6. Narrative**    | _Soccer midfielder..._ | Ground truth prompt describing actual subjects, movement, and environment.    |

---

## Key Best Practices

1. **Limit to 3–5 Slash Commands:** Stack maximum one command per category. Combining conflicting camera movements (e.g., `/dollyin /dollyout` or `/steadicam /orbit`) will cause render errors or visual distortion.
2. **Keep Modifiers Grouped at the Front:** Never bury slash commands inside natural language sentences. Keeping commands grouped at the start creates a clean separation between technical parameters and scene descriptive text.
3. **Use Descriptive Text for Details Slash Commands Can't Specify:** Use slash commands for structural directives (`/shallowdepth`), but rely on natural prose for fine details (e.g., "glistening rain on the turf" or "sweat on the player's forehead").
