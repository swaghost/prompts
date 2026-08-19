# THE MATERIAL PACK - Complete Guide

## Overview

The Material Pack is a collection of 12 AI image transformation prompts that convert existing photographs into different materials and fabrication methods. Unlike filters that merely adjust color and tone, these prompts **remake the entire image** as if it were constructed from a completely different substance—cast bronze, machined aluminium, moulded plastic, woven cane, burnt-down wax, matted wool, grown fungus, and more.

**Key Principle:** Same pose, same frame, completely different matter.

## Philosophy: Taste > Tech

> "Anyone can run a preset. Knowing that a mould cannot hold an undercut, that wax passes light an inch deep, that a weave lets the background through, that grown things swell where cast things shrink—that is the part you cannot download."

The power of these prompts lies in **naming the process, not the look**. Instead of asking for "something that looks like bronze," you describe how it was cast in wax, burned out, and poured. The mechanism is what the AI can actually build from, which is why these produce objects instead of textures.

## How to Use These Prompts

### 1. USE IMAGE EDIT, NOT TEXT TO IMAGE

You are **remaking a photo you already have**, not generating a new one.

- **Recommended Platform:** Nano Banana Pro (Gemini 3 Pro Image) on [HIGGSFIELD.AI](https://higgsfield.ai) or [FAL.AI](https://fal.ai)
- **Process:** Upload your image → Paste the prompt → Run

### 2. NEVER DELETE THE LAST LINE

Every prompt ends with: **"Keep the subject, pose, framing and composition exactly as they are."**

This line is the whole trick. It locks your picture in place and changes only what it's made of. Delete it and you'll get a different photo entirely.

### 3. NAME THE PROCESS, NOT THE LOOK

Don't ask for something that "looks like bronze." Say it was:

- Cast in wax, burned out and poured
- CNC-machined from a solid billet
- Shot molten into a steel tool under pressure

The mechanism is what the model can actually build from.

### 4. IF IT COMES BACK TIMID, PUSH IT

If your result looks like your original photo with a color cast, the model played it safe.

**Fix:** Add this line at the beginning:

```
ABANDON THE ORIGINAL RENDERING ENTIRELY
```

Four of these twelve prompts needed exactly that.

## The 12 Materials

### Manufacturing & Metalwork

1. **[Cast Bronze](01.cast-bronze.md)** - Lost-wax bronze sculpture with patina
2. **[Machined Billet](02.machined-billet.md)** - CNC-machined aluminium with anodizing
3. **[Injection-Moulded Plastic](03.injection-moulded-plastic.md)** - Plastic with parting lines and ejector marks

### Natural & Organic Materials

4. **[Woven Rattan](04.woven-rattan.md)** - Hand-woven basketwork with light passing through
5. **[Carved Limewood](05.carved-limewood.md)** - Gothic wood carving with gouge facets
6. **[Votive Beeswax](06.votive-beeswax.md)** - Melted candle with translucent glow
7. **[Needle-Felted Wool](09.needle-felted-wool.md)** - Soft woolly sculpture with fuzzy halo
8. **[Tooled Leather](10.tooled-leather.md)** - Hand-tooled vegetable-tanned hide

### Craft & Construction

9. **[Folded Origami](06.folded-origami.md)** - Single uncut sheet, no glue, only folds
10. **[Etched Circuit Board](07.etched-circuit-board.md)** - PCB routing on FR-4 substrate

### Grown & Natural Processes

11. **[Grown Mycelium](11.grown-mycelium.md)** - Fungal growth on hemp substrate
12. **[Crystal Growth](12.crystal-growth.md)** - Mineral crystal encrustation

## Material Selection Guide

### By Manufacturing Constraint

**Hard edges, precision:**

- Machined Billet (CNC tools)
- Injection-Moulded Plastic (steel mould)
- Etched Circuit Board (routing rules)
- Folded Origami (geometric planes)

**Soft, organic:**

- Needle-Felted Wool (migrated fibres)
- Grown Mycelium (swollen forms)
- Votive Beeswax (melted softness)
- Woven Rattan (follows curves)

**Carved/detailed:**

- Cast Bronze (wax modelling)
- Carved Limewood (gouge facets)
- Tooled Leather (relief depth)
- Crystal Growth (geometric terminations)

### By Visual Effect

**Translucent/light-passing:**

- Votive Beeswax (light travels 1" deep)
- Woven Rattan (background shows through)
- Crystal Growth (internal light bounce)

**Patina & age:**

- Cast Bronze (verdigris, old wax)
- Carved Limewood (candle soot, old polychrome)
- Tooled Leather (darkened handling patina)

**Surface texture:**

- Machined Billet (directional machining grain)
- Injection-Moulded Plastic (mould texture)
- Needle-Felted Wool (fuzzy halo)
- Grown Mycelium (velvety fungal mat)

**Manufacturing marks:**

- Cast Bronze (parting lines, sprue stubs)
- Machined Billet (witness marks, tool paths)
- Injection-Moulded Plastic (ejector pins, flash)
- Etched Circuit Board (fiducials, mouse bites)

## Technical Notes

### Understanding Material Constraints

Each prompt encodes **real manufacturing constraints**:

- **Injection moulding:** Can't have undercuts (must pull from mould)
- **CNC machining:** Can't reach undercuts (cutter can't get there)
- **Origami:** Can't curve (paper only folds in straight lines)
- **Weaving:** Can't be solid (structure requires gaps)
- **Crystal growth:** Grows from edges/points (not uniform)

When you name these constraints, the AI respects them.

### Platform Recommendations

**Primary:** Nano Banana Pro (Gemini 3 Pro Image)

- Available on: HIGGSFIELD.AI, FAL.AI
- Best for: Image-to-image transformations

**Alternative:** Other image editing AI models that support detailed prompts

### Best Practices

1. **Start with clear photos:** High contrast, good lighting
2. **Use full prompt:** Don't shorten or simplify
3. **Preserve last line:** Locks composition
4. **Push if timid:** Add "abandon original rendering" if needed
5. **Iterate:** Try multiple runs with slight variations

## Source & Attribution

Source: [waviboy.com/material-pack](https://www.waviboy.com/material-pack)

Creator: Waviboy
Learn more: [join.waviboy.com](https://join.waviboy.com/)

## File Structure

```
material-pack/
├── INDEX.md (this file)
├── 01.cast-bronze.md
├── 02.machined-billet.md
├── 03.injection-moulded-plastic.md
├── 04.woven-rattan.md
├── 05.carved-limewood.md
├── 06.folded-origami.md
├── 07.etched-circuit-board.md
├── 08.votive-beeswax.md
├── 09.needle-felted-wool.md
├── 10.tooled-leather.md
├── 11.grown-mycelium.md
└── 12.crystal-growth.md
```

---

**Remember:** A filter grades a photo. These remake it out of a different substance.
