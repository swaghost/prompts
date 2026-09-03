# AI Luxury Room Transformation Guide - Google Flow

## Purpose

Create cinematic before-to-after room transformations with Nano Banana and Gemini Omni Flash in Google Flow. The workflow produces a polished final room image, turns it into a locked-camera furnishing animation, adds satisfying diegetic ASMR, and packages the result as a client-ready service.

## The Simple Formula

Create the finished room first, then use that finished image as the exact final-state reference for the video. The animation begins with the same architecture stripped of removable furnishings and builds itself back to the reference image.

- **Image generation:** Nano Banana 2 or Nano Banana Pro inside Google Flow
- **Video generation:** Gemini Omni Flash inside Google Flow
- **Best format:** One locked camera, one continuous shot, 7-8 seconds, no cuts
- **Audio style:** Realistic diegetic ASMR only; no music inside the generation
- **Final goal:** The last frame looks exactly like the original reference image

## Step-by-Step Workflow

1. **Choose a room concept.** Pick one visually distinctive room with a clear focal point: fireplace, dramatic bed wall, library, glass view, statement art, or sculptural furniture.
2. **Generate the final room image first.** Use Nano Banana 2 or Pro to create a finished architectural interior containing every object wanted in the final frame.
3. **Inspect the reference.** Check furniture count, object placement, lighting, windows, artwork, plants, and small decor. Fix the still before animating.
4. **Upload the image to Omni Flash.** Use the final still as the reference image and state that it is the complete and exact final state, not the opening frame.
5. **Lock camera and architecture.** Freeze camera position, lens, framing, windows, floors, walls, ceiling, and built-ins. Only removable objects animate.
6. **Build a timed transformation.** Split 7-8 seconds into clear stages: curtains and lights, rug, main furniture, smaller decor, greenery, hero reveal, and final hold.
7. **Give every object physical motion.** Use slide, roll, lower, rise, rotate, unfold, settle, or grow. Avoid fade-ins and teleportation.
8. **Design the ASMR.** Tie one subtle sound to each visible action: textile rustle, leather compression, wood slides, crystal clinks, fireplace ambience, and clean light-switch clicks.
9. **Add a negative prompt.** Block camera movement, object duplication, architecture warping, floating objects, unwanted text, music, extra decor, and temporal artifacts.
10. **Generate, inspect, and revise.** If one part is wrong, change only that part while keeping successful timing and movement intact.

## Prompt Structure

A strong transformation prompt prioritizes control over poetic description:

1. Duration and single locked shot
2. Exact-reference rule
3. Camera rule
4. Architecture rule
5. Bare opening-frame definition
6. Timestamped object assembly
7. Final hold
8. Diegetic sound design
9. Negative prompt

The reference image is the source of truth. If Omni invents extra furniture or changes the room, strengthen the reference, camera, and architecture rules before adding descriptive language.

## Example 1 - The Fireside Den

A warm cinematic den built around a green-marble fireplace, smoked-oak shelving, forest-green mohair, and cognac leather. It demonstrates how built-in architecture can remain stable while removable objects assemble around it.

### Image Prompt - Nano Banana Pro

```text
Photorealistic interior photograph for a luxury private-residence listing. Scene: an intimate fireside den inside a high-end contemporary country house. The room feels warm, sophisticated and deeply comfortable rather than formal.

The far wall is clad in floor-to-ceiling dark smoked-oak paneling with integrated built-in bookshelves spanning both sides of a central fireplace. The fireplace is framed in heavily veined dark green marble with a wide low firebox burning softly. Above the fireplace hangs one restrained abstract painting in warm cream, deep forest green, charcoal and muted brown.

The built-in shelving is dark walnut with subtle integrated warm lighting concealed beneath selected shelves. Shelves contain carefully arranged cloth-bound books, a few ceramic vessels, small sculptural objects and several empty areas for visual breathing room. The floor is wide-plank aged oak in a medium-dark natural finish. The ceiling is smooth warm ivory plaster with simple recessed perimeter detailing, completely solid and uninterrupted.

On the right is one large black-framed picture window looking onto mature trees and a softly blurred garden beneath cool overcast afternoon light. Full-height heavyweight wool curtains in muted tobacco brown frame the window.

Centered in the room is a large deep sofa upholstered in rich forest-green mohair, facing the fireplace. Two oversized cognac-leather lounge chairs sit angled toward the sofa and fireplace. Between them sits a substantial low rectangular dark-walnut coffee table with softly rounded corners. A large hand-knotted wool rug in muted cream, brown, olive and charcoal anchors the seating group. A small camel-wool upholstered ottoman sits beside one chair.

Furnishings and decor: sofa cushions in moss green, warm taupe and deep brown; one thick oatmeal wool throw over the sofa arm; a shallow handmade ceramic bowl and three oversized art books on the coffee table; an aged-brass tray holding a crystal tumbler and decanter; a slim brass reading lamp beside one leather chair; one small dark-walnut side table with a linen-shaded lamp; one tall indoor ficus tree in an aged terracotta planter near the window; and one low woven basket beside the fireplace containing neatly stacked firewood.

Camera: eye level, straight-on architectural composition, 26mm equivalent, perfectly parallel verticals. Frame the full fireplace wall, both shelving units, sofa, leather chairs, rug, coffee table, window, ceiling and floor. Fireplace is the primary visual anchor.

Light: cool soft overcast daylight from the right window as key. Warm fireplace glow, concealed shelf illumination and small lamps create layered secondary pools of light. Deep but soft shadows. Cozy, elegant and cinematic without becoming excessively dark.

Real material texture - smoked oak grain, green marble veining, mohair pile, aged leather creasing, wool fibers, tarnished brass, handmade ceramic imperfections, cloth-bound books and natural timber variation.

Ultra-realistic premium private-residence photography with subtle English country-house influence.

Constraints: no people, no pets, no television, no readable book titles, no readable text, no captions, no watermark, no logos, no brand names, no signage, no skylights, no ceiling openings, no RGB lighting, no oversized chandelier, no excessive clutter, no HDR halos, no oversaturation, no strong orange grade, no fisheye, no tilted verticals, no plastic CGI appearance.
```

### Transformation Prompt - Gemini Omni Flash

```text
Single continuous locked-off shot, 8 seconds, no cuts, one fixed camera position. Photorealistic luxury interior transformation.

The attached reference image is the COMPLETE AND EXACT FINAL STATE of the den. It is NOT the opening frame. Begin with the same architectural room stripped almost completely bare and furnish it until the final frame matches the reference exactly.

REFERENCE RULE - ABSOLUTE: every object must end at the same position, scale, orientation, spacing, material, colour and count shown in the reference. Nothing additional may appear. No extra furniture, books, lamps, chairs, plants, artwork, decor, duplicates or substitutions.

CAMERA RULE - ABSOLUTE: same camera position, height, framing, lens, focal length and perspective throughout. No pan, tilt, zoom, push-in, dolly, orbit, crane, handheld shake, reframing or perspective drift.

ARCHITECTURE RULE - ABSOLUTE: smoked-oak paneling, built-in shelving structures, central green-marble fireplace surround, firebox opening, plaster ceiling, oak flooring, right-side picture window, exterior garden and room dimensions remain rigid. Shelves are structurally present but start empty. Fireplace is present but dark.

OPENING FRAME: exact same den, fully built but unfurnished. Shelves empty; fireplace dark. No sofa, chairs, coffee table, rug, ottoman, curtains, lamps, books, artwork, tree, firewood basket, tabletop decor, cushions or throw.

0.0-0.8s - FIRE: flame grows naturally inside the fireplace and settles into the low warm reference fire.
0.8-1.7s - CURTAINS + SHELF LIGHT: tobacco wool curtains descend along the window and settle with realistic heavy cloth physics. Concealed shelf lights illuminate progressively at low warm intensity.
1.7-2.6s - RUG: the hand-knotted rug rolls across the center of the oak floor and settles at the exact reference angle, position and scale.
2.6-3.8s - MAIN FURNITURE: the forest-green sofa glides into position facing the fireplace. Two cognac leather lounge chairs slide in from opposite sides and rotate to their exact angles. The dark-walnut coffee table lowers between them. The camel ottoman settles beside the correct chair.
3.8-4.8s - BOOKSHELVES FILL: cloth-bound books move onto shelves section-by-section. Some stand vertically, some form short horizontal stacks, matching the reference exactly. Ceramic vessels and sculptural objects settle into remaining shelf positions while preserving intentional empty spaces.
4.8-5.6s - LIGHTING: the brass reading lamp rises beside the leather chair. The side table slides into position and the linen-shaded table lamp settles on it. Both lamps illuminate gently one after another.
5.6-6.3s - TEXTILES: sofa cushions settle one by one into the exact visible locations. The oatmeal throw unfolds and drapes over the sofa arm with realistic wool physics.
6.3-6.9s - FINAL DECOR + GREENERY: the abstract painting locks into place above the fireplace. Bowl, art books, brass tray, decanter and tumbler settle onto the coffee table. The woven firewood basket slides beside the fireplace and logs arrange inside. The terracotta planter moves near the window and the ficus grows until it matches the reference shape and density.
6.9-8.0s - FINAL HOLD: every movement stops. The den matches the reference exactly. Hold still like a premium luxury interior photograph.

Sound design: realistic diegetic room sounds only - furniture contact, leather compression, heavy textile rustle, quiet book movement, crystal clink, fireplace ambience and low indoor room tone. No music, soundtrack, voiceover or subtitles.
```

### Fireside Negative Prompt

```text
Camera movement, pan, tilt, zoom, dolly, orbit, reframing, changing perspective, changing focal length, fisheye, architecture changing, shelves warping, fireplace shifting, moving window, changing garden, ceiling openings, skylight appearing, extra sofa, extra chairs, extra tables, extra lamps, extra plants, excessive books, random books, extra artwork, extra cushions, duplicate furniture, substituted furniture, shelves overfilling, wrong object placement, fade-in, teleportation, cross-dissolve, floating objects, people, hands, workers, tools, pets, television, readable titles, text, logos, captions, watermark, neon, RGB, flicker, ghosting, smearing, orange lighting, oversaturation, HDR halos, cartoon, plastic CGI, jump cut, scene change, music.
```

## Example 2 - The Coastal Primary Bedroom

An expansive oceanfront primary bedroom built around pale limestone, natural white oak, soft boucle, aged brass, and a calm coastal view. It demonstrates coordinated curtains, bedding, pendants, lounge furniture, decor, and greenery while keeping the architecture locked.

### Image Prompt - Nano Banana Pro

```text
Photorealistic interior photograph for a luxury private-residence listing. Scene: an expansive primary bedroom inside a contemporary oceanfront villa. The far wall is almost entirely floor-to-ceiling frameless glazing overlooking a calm ocean, pale rocky coastline and distant horizon beneath soft neutral morning light.

The floor is wide-plank natural white oak with subtle grain and matte finish. Walls are hand-troweled warm ivory lime plaster. The ceiling is flat, continuous and finished in matching ivory plaster with a narrow recessed shadow gap and no skylights or visible ceiling fixtures.

A floor-to-ceiling slab of softly veined pale limestone creates a feature wall behind a centered low-profile king bed with an oversized oatmeal-boucle upholstered headboard. The bed is dressed in crisp ivory linen sheets, a thick cream duvet, two large sleeping pillows, two oversized textured sand pillows, two smaller muted caramel cushions and a soft taupe linen throw folded loosely across the foot.

On each side is a sculptural floating dark-walnut nightstand. Above each hangs one slim aged-brass pendant with a frosted glass shade. At the foot of the bed sits a long rounded caramel-leather bench with dark walnut legs. A large hand-knotted cream-and-sand wool rug extends beneath the bed and bench.

On the right near the glazing are two low ivory-boucle lounge chairs facing the ocean with a small round travertine table between them. A tall olive tree in a weathered stone planter stands in the far-right corner.

On the left wall, a low floating dark-walnut console holds a handmade ceramic vessel, a small stack of art books and a sculptural stone object. Above it hangs one oversized abstract artwork in sand, clay, cream and muted charcoal. Full-height sheer off-white linen curtains frame the glazing and lightly touch the floor.

Camera: eye level, straight-on architectural composition, 25mm equivalent, perfectly parallel verticals. Frame the entire bed wall, full bed and bench, both nightstands and pendants, lounge area, glazing, ceiling and floor. The bed is the dominant visual anchor.

Light: soft diffused morning daylight from the glazing, with small warm pendant pools as secondary light. Neutral coastal illumination, no harsh direct sun and no strong golden-hour orange grade.

Real material texture - limestone veining, lime plaster grain, linen weave, boucle fibers, walnut pores, leather creasing, wool pile, aged brass and handmade ceramics.

Ultra-realistic premium architectural photography. Sophisticated, tranquil contemporary coastal luxury. Expensive but restrained; clearly a private residence, not a hotel.

Constraints: no people, no pets, no television, no readable text, no captions, no watermark, no logos, no brand names, no skylights, no ceiling openings, no oversized chandelier, no HDR halos, no oversaturation, no fisheye, no tilted verticals, no plastic CGI appearance.
```

### Transformation Prompt - Gemini Omni Flash

```text
Single continuous locked-off shot, 8 seconds, no cuts, one fixed camera position. Photorealistic architectural interior transformation.

The attached reference image is the COMPLETE AND EXACT FINAL STATE of the bedroom. It is NOT the opening frame. Begin with this exact bedroom stripped almost completely bare and progressively furnish it until the final frame matches the reference precisely.

REFERENCE RULE - ABSOLUTE: every object must end at the exact position, size, orientation, spacing, material and colour shown in the reference. Nothing additional may appear. No alternative furniture designs, extra decor, extra pillows, extra lamps, extra plants or duplicates.

CAMERA RULE - ABSOLUTE: same camera position, height, framing, angle, lens, focal length and perspective throughout. No pan, tilt, zoom, dolly, push-in, orbit, handheld movement, reframing or perspective drift.

ARCHITECTURE RULE - ABSOLUTE: the pale limestone feature wall, plaster walls, ceiling, shadow gap, white-oak floor, glazing, window framing, ocean horizon, rocky coastline and room dimensions remain rigid and unchanged. Only furniture, curtains, lighting, textiles, artwork, decorative objects and greenery assemble.

OPENING FRAME: same bedroom, architecture complete but no bed, rug, nightstands, pendants, bench, lounge chairs, table, curtains, console, artwork, plant or decor.

0.0-1.0s - CURTAINS: sheer linen curtains descend from both sides of the glazing and settle into the exact reference folds.
1.0-2.0s - RUG: the large cream-and-sand wool rug rolls across the oak floor and lands precisely centered beneath the future bed and bench.
2.0-3.5s - BED ASSEMBLY: the low bed platform slides into the exact center. The boucle headboard rises against the limestone wall. The mattress lowers into place. Bedding spreads smoothly; pillows arrange in the exact reference order; the taupe throw unfolds across the foot.
3.5-4.3s - NIGHTSTANDS + LIGHTS: two floating walnut nightstands slide into their exact positions. Brass pendant lights descend to their exact lengths and illuminate one after another.
4.3-4.9s - BENCH: the long caramel leather bench glides to the foot of the bed and stops parallel at the exact reference distance.
4.9-5.7s - OCEAN LOUNGE: two ivory boucle chairs glide beside the glazing and rotate to the exact angles. The round travertine table lowers between them.
5.7-6.5s - CONSOLE + ART: the dark-walnut console slides onto the left wall. The oversized artwork locks into position. Ceramic vessel, books, sculptural stone object and bedside decor settle exactly where visible in the reference.
6.5-6.9s - GREENERY: the planter moves into the far-right corner and the olive tree grows upward until its height, width and density match the reference.
6.9-8.0s - FINAL HOLD: all assembly motion stops. The final room matches the reference exactly - furniture, bedding, pillow placement, bench, chairs, curtains, pendants, console, artwork, tree, decor, lighting and ocean composition. Hold still like a premium interior photograph.

Sound design: soft textile movement, muted furniture contact, quiet wood and stone settling, subtle pendant illumination and faint distant ocean ambience. No music, soundtrack, voiceover or subtitles.
```

### Coastal Bedroom Negative Prompt

```text
Camera movement, pan, tilt, zoom, dolly, orbit, reframing, perspective drift, changing lens, fisheye, warped architecture, shifting limestone wall, moving windows, changing ocean horizon, skylight appearing, wrong bed placement, wrong bed size, wrong headboard, wrong bedding, incorrect pillow arrangement, extra pillows, extra nightstands, extra lamps, extra chairs, extra plants, extra tables, different artwork, duplicate objects, furniture morphing, floating furniture, fade-in, teleportation, cross-dissolve, people, hands, workers, tools, pets, text, logos, captions, watermark, flicker, ghosting, smearing, orange grading, oversaturation, HDR halos, cartoon, plastic CGI, jump cut, scene change, music.
```

## Make Transformations More Satisfying

- Give the biggest pieces the slowest, heaviest movement. Sofas, beds, stone tables, and rugs should feel weighted.
- Use sequential assembly instead of having everything appear at once so the viewer always knows where to look.
- Make textiles unfold, drape, and compress.
- Keep lighting changes subtle. Lamps should illuminate only after reaching their final position.
- Use one hero finishing move near the end: artwork sliding into place, a tree growing, a fireplace igniting, or a chandelier descending.
- End with a short still hold so the viewer can register the completed room.
- When a generation is almost right, revise only the bad moment. Do not rebuild the whole prompt unless the structure failed.

## ASMR Formula

| Visible action         | Sound                                                       |
| ---------------------- | ----------------------------------------------------------- |
| Rug                    | Soft heavy wool roll                                        |
| Sofa or bed            | Deep upholstered settle                                     |
| Leather chair or bench | Soft leather compression                                    |
| Wood furniture         | Low muted slide                                             |
| Books                  | Light dry page movement                                     |
| Stone or ceramic       | Gentle solid contact                                        |
| Crystal                | Small refined clink                                         |
| Plant growth           | Restrained leaf rustle                                      |
| Lamp                   | Subtle placement sound, then one clean tactile switch click |
| Fireplace              | Soft low crackle after ignition                             |

### Avoid

Footsteps, random impacts, loud thuds, repeated tapping, cinematic booms, aggressive whooshes, music, voiceover, or sounds that happen before the matching object moves.

## Troubleshooting

- **Furniture appears from nowhere:** Replace vague "appears" language with a physical action: slides in, lowers, rolls, unfolds, rotates, rises, or grows.
- **Camera starts drifting:** Repeat the fixed-camera rule and remove cinematic camera language such as push-in, orbit, parallax, or reveal shot.
- **Architecture changes:** List structural elements that must remain rigid: walls, ceiling, floor, windows, built-ins, fireplace, and exterior view.
- **Extra furniture appears:** State that the reference is the only source of truth and explicitly forbid extra objects, duplicates, and substitutions.
- **Lighting makes weird sounds:** Separate movement from illumination: object settles first, then one clean switch click, then the light turns on.
- **Artwork animates:** State that the image inside the artwork is a completely static physical painting and nothing inside it may move.
- **Prompt behaves strangely:** Shorten repetitive wording. Keep the reference rule, camera rule, architecture rule, timestamps, sound design, and negative prompt, but remove duplicate instructions.

## Client Service Packaging

Treat the transformation as a deliverable, not an AI experiment. Clients buy attention-grabbing property content, faster design visualization, or a reusable short-form asset.

### Buyers and Use Cases

- **Real estate agents and brokerages:** Listing teasers, vacant-room staging concepts, before/after Reels, and paid social creative.
- **Interior designers and home stagers:** Finished renders, moodboards, or empty rooms turning into presentation videos.
- **Airbnb and vacation-rental hosts:** Room reveals for listing launches, renovations, and social posts.
- **Builders, architects, and developers:** Finished concepts animated for presales, project announcements, and development marketing.
- **Furniture, lighting, and decor brands:** Room transformations built around a hero product or coordinated collection.
- **Content agencies and property media teams:** A repeatable white-label add-on to photo, video, and social packages.

### Example Offers

- **Starter Reveal:** One room transformation, one revision, vertical social export. Starting framework: $75-$150.
- **Property Mini Pack:** Three room transformations from one property or project, matching visual style. Starting framework: $200-$400.
- **Listing Launch Pack:** Five to eight transformations plus branded end card and hooks/captions supplied as text. Starting framework: $400-$800.
- **Monthly Content Retainer:** Recurring batch of room transformations for social posting. Starting framework: $500-$1,500+ per month.

Pricing is only a starting framework, not a market guarantee. Adjust for quality, revisions, turnaround, client size, strategy, and editing.

### Easy Upsells

- Additional room or alternate design version
- Branded end card, logo treatment, or property call-to-action
- 9:16, 1:1, and 16:9 exports from the same concept
- Voiceover script, caption copy, and hook options
- Before/after cover image or Reel thumbnail
- Rush turnaround or extra revision rounds
- Monthly content calendar for multiple listings

### Outreach Pitch

> Hey [Name] - I create short room-transformation videos from property photos and interior renders. They are built for Reels and TikTok and show the space furnishing itself in a single cinematic shot. I can make a sample using one of your rooms, and if you like it I can package several for a listing or monthly content.

### Client Workflow

1. Get the client's room photo, render, or approved reference image and confirm usage rights.
2. Agree on the final visual direction before generating video. Fix the still first.
3. Create the final reference image, then run the locked-camera Omni Flash transformation.
4. Deliver a watermarked preview if appropriate, collect one clear revision list, and make targeted prompt changes.
5. Deliver the final video plus purchased crops, branded ending cards, or copy.
6. Ask for the next room or turn the project into a recurring package.

The business angle is the outcome: turn a room, listing, or design into a short-form transformation people will stop to watch.

## Final Checklist

- Final still image looks exactly how the last frame should look.
- Camera is explicitly locked.
- Architecture is explicitly frozen.
- Opening frame lists what is absent.
- Each timestamp has a clear visual action.
- No object needs to do two conflicting things at once.
- ASMR sounds match visible actions.
- No music or voiceover is requested inside the generation.
- Negative prompt blocks duplicates, camera movement, warping, and teleportation.
- Final 0.2-1.0 seconds holds completely still.

**Create the final room. Lock the reference. Animate the build.**
