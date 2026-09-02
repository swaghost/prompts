When directing individual players within a team system in Google Flow, the model needs clear visual anchors to prevent "entity blending"—where the AI accidentally merges two players or gives the wrong instruction to the wrong athlete.

To direct individual players precisely while keeping the broader team in motion, use these four core prompt strategies:

---

## 1. Assign Visual & Positional Anchors

Never refer to a player as just "the player" or "he." Name their **kit color**, **shirt number**, or **tactical position relative to the spatial grid**.

- **Vague:** `A midfielder passes to a winger.`
- **Precise:** `The blue #8 central midfielder turns and plays a low diagonal ball to the left winger in blue.`

---

## 2. Use Tactical Roles as Movement Directives

Instead of describing every muscle movement, give the AI established tactical behavior terms for the individual's role.

- **For Attackers:** `dismarking run`, `blind-side double-move`, `overlapping run`, `peeling off the back of the center-back`.
- **For Midfielders:** `scanning over the shoulder`, `dropping into the half-spaces`, `receiving on the half-turn`.
- **For Defenders:** `stepping out of the line to press`, `holding the offside trap`, `jockeying laterally`.

---

## 3. Apply Selective Optics (`/selectivefocus` & `/rackfocus`)

When directing one player within an 11v11 shape, use optical slash commands to visually isolate their specific action while keeping the rest of the team as a contextual backdrop.

- **Single Player Focus (`/selectivefocus`):** Isolates the key actor in sharp detail while the surrounding tactical block remains soft in the background.
- **Player-to-Player Transfer (`/rackfocus`):** Shifts the visual focus from the initiating player (e.g., the passer) to the receiving player as the action unfolds.

---

## Directing Templates for Individual Roles

### Template A: Directing an Individual Dismarking Run (Attacker)

```text
/filmic /lowangle /steadicam /selectivefocus /volumetric Camera tracks the blue #9 striker as he executes a sharp two-step dismarking run—first faking a sprint into the box, then checking back into the half-space to receive a feet-pass. The surrounding red defensive block shifts behind him in soft focus as he traps the ball on the half-turn.

```

### Template B: Directing a Specific Defender Stepping Out of Line

```text
/documentary /wideangle /dollyin /shallowdepth High-angle view following the red #4 center-back. As the opponent's midfielder turns, the red #4 steps aggressively out of the back four line to press the ball carrier, while the remaining three defenders narrow their spacing to cover the open gap behind him.

```

### Template C: Directing a Playmaker Scanning and Switching Play

```text
/cinematic /tight /rackfocus /rimlight Camera starts close on the blue #10 central playmaker constantly scanning over both shoulders. He takes a single soft touch to set the ball, then plays a sweeping 40-yard diagonal switch. The camera rack-focuses across the pitch to isolate the right winger taking the ball down in full stride on the touchline.

```

---

## Dynamic Prompt Structure for Individual Directives

```text
[Slash Commands] -> [Primary Player Anchor: Kit # / Position] -> [Specific Tactical Movement] -> [Secondary Player / Defensive Reaction] -> [Environment Details]

```

### Pro-Tip: Layering Action Verbs

To make individual motion look fluid rather than robotic, layer **preparation $\rightarrow$ execution $\rightarrow$ outcome** in the natural language section:

> `"...the winger slows his pace (preparation), suddenly explodes down the line past his marker (execution), and cuts back a low cross to the edge of the 18-yard box (outcome)."`
