# Reference Board Builders — Image-to-Image Workflow

**Platform:** GPT Image 2, Picsart Flow  
**Workflow:** Image-to-image inside Topview Canvas  
**Purpose:** Pre-generate reference boards that can be @-referenced in Seedance 2.0/2.5 video prompts for consistency

## What Are Reference Boards?

Reference boards are single composite images containing multiple angles, views or stages of a subject, all generated in one prompt. They serve as visual anchors for video generation, ensuring consistency across shots or sequences.

Instead of generating 12 separate character portraits and hoping they look like the same person, you generate one board with 12 views of the same character, then @-reference that board when prompting video.

## When to Use These Builders

- **Before starting any video project** — Generate boards first, video second
- **For multi-shot sequences** — Storyboards and shot boards maintain scene continuity
- **For character/creature consistency** — Expression sheets and turn-arounds prevent morphing
- **For object/product close-ups** — Object boards lock shape and texture
- **For location matching** — Environment boards ensure spatial consistency

## How Image-to-Image Works

1. Generate the board in GPT Image 2 or Picsart Flow
2. Upload to Topview Canvas as a node
3. Name the node with @ prefix (e.g., @char_hero, @creature_design, @location_plate)
4. Reference it in your video prompt: "Character appearance follows @char_hero"
5. The video model uses the board as a visual constraint

## Collection Contents

This collection contains 6 builder prompts:

1. **[Pose Board](01-pose-board-animation-reference.md)** — 3×3 grid of identical character in 9 different action poses
2. **[Character Board](02-character-board-consistency.md)** — Multi-angle turnaround for person identity consistency
3. **[Object Board](03-object-board-product-reference.md)** — Product/prop from multiple angles for close-up shots
4. **[Location Board](04-location-board-environment-set.md)** — Environment/set from multiple camera positions
5. **[Creature Board](05-creature-board-growth-stages.md)** — Creature design with growth/evolution stages
6. **[Shot Board](06-shot-board-storyboard-12-panel.md)** — 12-shot storyboard for narrative sequences

## Technical Specifications

- **Format:** All prompts generate single composite images with multiple panels/cells
- **Grid Layouts:** 3×3 (9 cells), 4×3 (12 cells), or multi-panel custom arrangements
- **Consistency Rule:** "Identical [subject]" + "only [specified variable] changes" in every prompt
- **Lighting:** Studio lighting for character/object boards, cinematic lighting for location/shot boards
- **Background:** Seamless neutral for turnarounds, contextual for narrative boards

## Workflow Tips

- **Generate boards before writing video prompts** — Gives you visual constraints upfront
- **Use descriptive node names** — @hero_angry tells you more than @char01
- **Keep one board per asset type** — Don't combine character + location on same board
- **Studio lighting > dramatic lighting** — For consistency boards; save drama for final video
- **Name materials explicitly** — "matte cotton," "polished chrome," "leather with grain" prevent texture drift

## Integration with 5-Layer Method

Reference boards map directly to the 5-layer video consistency method:

- **Layer 1: Style Bible** → Pasted into every board prompt
- **Layer 2: Character Sheets** → Character Board + Pose Board builders
- **Layer 3: Location Plate** → Location Board builder
- **Layer 4: Key Beat** → Shot Board builder (single critical frame)
- **Layer 5: Master Video** → References all boards generated with these builders

---

**Collection:** 6 builder prompts for reference board generation  
**Source:** Reference 2.0 documentation  
**Compatible with:** GPT Image 2, Picsart Flow, Topview Canvas node-based workflow
