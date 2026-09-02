When directing two-player combinations (such as give-and-gos, wall passes, overlapping runs, or third-man combinations), the prompt must explicitly define **Player A (the initiator/passer)**, **Player B (the wall/wall-passer)**, and the **spatial vector** (where the ball and players move relative to each other).

Use optical commands like `/rackfocus` or dynamic tracking like `/steadicam` to seamlessly transfer viewer focus from the setup to the final pass into space.

---

## 1. The Classic One-Two / Give-and-Go (Give $\rightarrow$ Run $\rightarrow$ Receive)

- **Mechanic:** Player A passes to Player B, immediately sprints past their defender into space, and receives the return pass in stride.
- **Camera Strategy:** Focus on the initial pass, track Player A’s sprint, and zoom/focus on the return touch.

```text
/cinematic /lowangle /steadicam /rackfocus /volumetric Camera tracks blue #10 playing a crisp low pass into the feet of blue #9 who acts as a wall. Blue #10 immediately explodes forward into space past a flat-footed red defender. Blue #9 lays off a single-touch return pass into the path of blue #10. Camera rack-focuses from the wall player to blue #10 collecting the ball in full stride inside the penalty box.

```

---

## 2. The Wall Pass Around a Pressing Defender (Tight Space Combination)

- **Mechanic:** Player A uses Player B as a stationary anchor to bypass an aggressive, tightly-marking defender in congested central space.
- **Camera Strategy:** Low-angle, tight tracking shot to capture the sharp angle of the ball bouncing off the wall player.

```text
/filmic /tight /dollyin /shallowdepth /spotlight Close tactical tracking of blue #8 dribbling under tight pressure from a red defender. Blue #8 plays a firm, angled pass into the feet of blue #6, who stands firm as a wall player. Blue #6 uses the inside of his boot to cushion a dynamic one-touch lay-off into the open half-space. Blue #8 collects the return pass without breaking stride, leaving the defender behind.

```

---

## 3. The Overlapping Fullback & Winger Combination

- **Mechanic:** The winger (Player A) holds the ball inside to draw the fullback, while the fullback (Player B) sprints around the outside line to receive a pass into the corner space.
- **Camera Strategy:** Wide tracking shot moving laterally along the touchline.

```text
/commercial /wideangle /panright /selectivefocus /rimlight Sideline view of blue #7 winger holding the ball on the right flank, luring a red defender inward. Blue #2 right-back executes a high-speed overlapping run down the outside touchline. Blue #7 plays a soft, weighted diagonal pass through the defensive seam into the running path of blue #2, who hits the ball on the run to whip in a low cross.

```

---

## 4. The Third-Man Run (Passing A $\rightarrow$ B, Movement C)

- **Mechanic:** Player A passes to Player B, but instead of Player A running, Player C (the third man) makes an untracked run into space to receive Player B's lay-off.
- **Camera Strategy:** High-angle overview shifting focus from the decoy pass to the third-man attacker breaking through the defensive line.

```text
/documentary /establishing /panleft /deepfocus /nightscene High master-shot tracking a three-player combination. Blue #4 center-back plays a vertical line-breaking pass to blue #9 striker (the second man). As red defenders collapse on blue #9, he cushions a blind one-touch layoff into space for blue #11 (the third man), who arrives from deep out of frame to smash the ball past the defensive line.

```

---

## 5. The Underlapping Midfield Run (Inside Pocket Overload)

- **Mechanic:** The winger (Player A) stays wide on the touchline with the ball, while an attacking midfielder (Player B) runs through the channel _inside_ the defender (underlap).
- **Camera Strategy:** Crane down / low angle following the vertical channel opening up.

```text
/scifi /lowangle /cranedown /rackfocus /volumetric Low-angle camera positioned near the corner flag. Blue #11 winger holds wide possession, pinning the opponent's right-back to the touchline. Blue #10 midfielder makes an aggressive underlapping run through the interior half-space channel. Blue #11 slides a pin-point through-ball into the interior pocket for blue #10 to collect inside the 18-yard box.

```

---

### Formula for Custom 2-Player Prompts

To write your own, plug your parameters into this breakdown:

$$\text{[Slash Commands]} + \text{[Player A Action]} + \text{[Player B Wall/Lay-off]} + \text{[Spatial Outcome/Return]} + \text{[Lighting/Turf Details]}$$

- **Example:**
  > `/filmic /lowangle /steadicam` **(Commands)** + `blue #10 plays a low pass into feet` **(Player A)** + `and blue #9 cushions a one-touch lay-off` **(Player B)** + `allowing blue #10 to collect the ball behind the defensive line` **(Outcome)** + `stadium lights reflecting on wet turf` **(Atmosphere)**.
