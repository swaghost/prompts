# Multi-Subject 

Here is that complete guide:

---

## Writing Multi-Subject Prompts with Slash Commands

When directing scenes with two or more subjects (such as a defender closing in on an attacker, or two players competing for a 50/50 ball), standard tracking commands can cause camera confusion or default focus onto the wrong character.

To maintain clarity and prevent the AI engine from blending the subjects together, follow these structural rules:

### 1. Establish the Primary Focal Subject First

Always identify who the camera is primary on _before_ bringing in the second subject. Use directional position or role labels (e.g., _"the winger in blue"_ vs. _"the pressing defender"_).

### 2. Match Camera Movement to the Interaction Vector

- **For opposing motion (tackles, press):** Use forward/backward dynamics like `/dollyin` or high-angle views (`/overhead`).
- **For side-by-side motion (chasing down the wing):** Use lateral movements like `/steadicam` or `/panright`.
- **For shift in focus (passer to receiver):** Use optical commands like `/rackfocus`.

---

## Multi-Subject Template Examples

### A. The 1v1 Defender vs. Attacker (Lateral Tracking)

```text
/filmic /lowangle /steadicam /shallowdepth /volumetric Tracking shot moving laterally with an attacking winger in a blue jersey as he executes a step-over to unbalance a trailing defender, defenders legs reaching in for a slide tackle as the ball rolls past, stadium floodlights illuminating the wet grass.

```

### B. The 50/50 Aerial Duel (Vertical Crane & Frozen Focus)

```text
/cinematic /wide /craneup /selectivefocus /rimlight Camera tilting upward as a striker and a central defender leap simultaneously into the air for a high cross, dramatic mid-air clash of headers, ball hovering between their heads under heavy stadium lighting, crowd blurred in the background.

```

### C. The Pass & Receive Sequence (Dynamic Focal Shift)

```text
/documentary /tight /rackfocus /shallowdepth /nightscene Camera starts in sharp focus on a midfielder’s boot striking a diagonal pass, then smoothly rack-focuses across the pitch to isolate the winger who traps the ball on their chest in full stride.

```

---

### Pro-Tips for Multi-Subject Prompts

1. **Use Distinct Visual Identifiers:** Contrast kit colors (_"blue jersey"_ vs. _"red kit"_) or distinct physical positions (_"foreground runner"_ vs. _"background defender"_) so the model distinguishes between the entities.
2. **Avoid Dual Camera Commands:** Never use two positional tracking commands together (like `/panleft /panright`) to capture both players. Instead, pick one primary camera vector and let the natural language describe the relative movement of the second subject inside that frame.
