# The Consistent Character Pack Guide

One character across a whole world — 9 scenes, each shot from a different camera angle.

## What This Is

One character, kept perfectly consistent across nine completely different scenes of the same world — same face, same wardrobe, same mud on her shoes, same light and grade — and each scene shot from a different camera angle. This is how you build a whole photo story around one AI character instead of one lonely image. The trick is a two-reference setup plus a set of "locks" that stop the model drifting.

**Platform:** GPT Image 2 · Picsart Flow

---

## The Two-Reference Method

The whole system runs on **two references** and **four locks**. Get the master frame right first — everything after inherits from it:

### Two References

- **Image 1 = the character** — a clean reference of her face, hair, jewellery and wardrobe. Used ONLY for who she is, never for the background or light.
- **Image 2 = the world** — the master frame you generate first. It sets the location, the light and the colour grade, and becomes the reference every later scene points back to.

### Four Locks

- **Character lock** — her exact face, hair and wardrobe named again in every prompt, down to the mud on her socks, so she never changes.
- **Scene lock** — "the same country as image 2 — same materials, same weather, same hour" keeps every location in one believable world.
- **Grade lock** — "identical exposure and white balance to image 2" keeps the colour and light matched across the whole set.
- **Pose lock** — her body described in physical detail per scene so the action reads and can't drift.

> ✦ **The master frame is image 2.** Generate it first from your character reference, then point every new scene back at it — that's what keeps nine images looking like one shoot on one day.

---

## The 9 Camera Angles

Each scene is shot from a different angle — this is the camera vocabulary built into the prompts. Drop any of these lines into any scene to reframe it:

| Angle                   | Where the camera goes                                           |
| ----------------------- | --------------------------------------------------------------- |
| **Wide shot**           | Back and slightly up — she's smaller, the whole location shows. |
| **Close-up**            | Tight on the face, head to base of neck, background soft.       |
| **Three-quarter front** | 45° off her front — face plane and shoulder turn both read.     |
| **Over the shoulder**   | Behind her, past her shoulder, looking into the scene ahead.    |
| **Low angle**           | Knee height, tilted up — she rises tall against the sky.        |
| **Cowboy shot**         | Knees to head — holds the face and what the hands are doing.    |
| **Extreme wide shot**   | Far back and raised — she's a small figure in the landscape.    |
| **Dutch angle**         | Horizon tilted ~20° — everything runs on a diagonal.            |
| **High angle**          | Raised above, tilted down — looking down onto her.              |

---

## How To Use

Runs in **Picsart Flow** with **GPT Image 2** as image-to-image.

1. **Get a character ref** — A clean sheet of your character's face, hair and wardrobe — this is image 1.
2. **Build the master frame** — Run scene 1 with image 1 to create the establishing shot. This becomes image 2.
3. **Feed both refs** — For every new scene, feed image 1 (character) + image 2 (the master frame).
4. **Swap scene + angle** — Change the scene, pose and camera-angle line; keep all the lock lines.
5. **Build the story** — Repeat for all 9 to get one character across a whole consistent world.

---

## Tips for Best Results

- **Master frame first, always.** It sets the world and becomes image 2 — if it's off, every scene inherits the problem. Get it clean before moving on.
- **Never drop the lock lines.** Character lock, scene lock and grade lock are what hold consistency — they're repetitive on purpose, so keep them in every prompt.
- **Re-name the wardrobe every time.** Spelling out the exact clothes and the mud in each prompt is what stops her outfit drifting between scenes.
- **Match the angle to the moment.** Low angle for the sword swing, extreme wide for the landscape, high angle for the huddled doorway — the camera should serve the beat.
- **Detail the pose physically.** Name the weight, the limbs, the head direction — vague poses drift, specific ones hold.
- **Keep two references loaded.** Image 1 for who she is, image 2 for the world — both every time, or the model loses one or the other.
- **Swap the whole character.** The medieval world is just an example — drop in any character, wardrobe and setting and keep the two-reference lock system.

---

## The 9 Scene Prompts

1. Master Frame — Wide Shot (muddy street, water pail)
2. Stable, Brushing — Close-up
3. Leading the Horse — Over the Shoulder
4. Stable, Brushing — Three-Quarter Front
5. Sword Training — Low Angle
6. On the Cart — Extreme Wide Shot
7. Fish Market — Cowboy Shot
8. Grain Sack — Dutch Angle
9. Tavern Doorway — High Angle

Each prompt is available as a separate file in this directory.
