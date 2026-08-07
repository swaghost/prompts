# Matchday Graphics - General Tips & Best Practices

## Overview

Universal principles, AI tool parameters, and best practices for creating effective matchday sports graphics. Apply these tips across all matchday graphic types for consistent, professional results.

**Part of:** [Matchday Graphics Collection](PROMPT.MATCHDAY.txt)

---

## Essential Prompt Phrases

### Core Matchday Terms

Use these foundational phrases in prompts:

**Sports Graphic Aesthetics:**

- "modern sports graphic"
- "professional broadcast style"
- "clean sports design"
- "stadium energy"
- "live sports aesthetic"

**Typography Emphasis:**

- "bold typography"
- "clean sans-serif"
- "condensed type"
- "high contrast text"
- "modern geometric fonts"

**Quality Descriptors:**

- "professional quality"
- "broadcast standard"
- "shareable social media format"
- "high-impact design"
- "premium sports graphic"

**Layout Terms:**

- "clean layout"
- "organized grid"
- "minimalist design"
- "typographic hierarchy"
- "data visualization"

---

## AI Tool Parameters

### Midjourney Settings for Matchday Graphics

**Aspect Ratios:**

```
--ar 1:1        Universal social media (Instagram, Twitter) - most versatile
--ar 9:16       Instagram/Facebook Stories, mobile-first, vertical
--ar 16:9       Broadcast, YouTube, website hero, horizontal
--ar 4:5        Instagram feed portrait, taller than square
```

**Stylize Values:**

```
--stylize 100-250   Clean, data-focused, minimal interpretation (brackets, tables)
--stylize 250-500   Balanced, professional sports graphics (most matchday content)
--stylize 500-750   Stylized, celebration graphics, energetic designs
--stylize 750+      Artistic, highly stylized (use sparingly for matchday)
```

**Quality:**

```
--quality 2     High quality for text clarity and fine details (recommended for all matchday graphics)
--quality 1     Standard quality (acceptable for quick drafts)
```

**Style Mode:**

```
--style raw     More literal interpretation, less artistic (better for info-heavy graphics)
(default)       Midjourney's standard aesthetic interpretation
```

**Recommended Defaults:**

- Info graphics (brackets, lineups): `--ar 1:1 --stylize 200 --quality 2 --style raw`
- Announcements: `--ar 9:16 --stylize 400 --quality 2`
- Celebrations: `--ar 1:1 --stylize 600 --quality 2`

---

### DALL-E Best Practices

**Prompt Structure:**

1. **Start with graphic type:** "Fixture announcement graphic," "Score update graphic"
2. **Describe layout:** "Bold scoreboard layout," "Clean typographic design"
3. **Specify details:** Team names, colors, aspect ratio
4. **Request quality:** "Professional sports graphic," "Shareable social format"

**DALL-E Strengths:**

- Typography integration
- Text rendering (better than Midjourney in some cases)
- Specific team colors
- Clean layouts
- Precise aspect ratio control

**DALL-E Tips:**

- Be explicit about text content: "text reads 'FINAL'"
- Specify exact colors: "royal blue background," "gold accents"
- Request "clean design" for minimal clutter
- Mention "readable text" for clarity

---

### Stable Diffusion Recommendations

**Model Selection:**

- SDXL: Best for photorealistic stadium backgrounds
- SD 1.5 with LoRA: Good for consistent branded styles
- Custom training: For specific team branding consistency

**Prompt Keywords:**

- "sports graphic," "match graphic," "tournament graphic"
- "broadcast quality," "TV sports aesthetic"
- "clean design," "modern typography"
- "high contrast," "bold layout"

**Negative Prompts (Essential):**

```
no action, no players playing, no match footage, no blurry text, no cluttered design, no distorted text
```

**CFG Scale:**

- 7-10: Clean, organized graphics
- 10-12: More stylized, energetic
- 12+: Risk of over-processing

**Sampling Steps:**

- 30-50 steps: Good quality
- 50+: Diminishing returns for graphic design

---

## Typography Best Practices

### Font Selection

**Sans-Serif Fonts (Primary):**

- Modern, clean, professional
- Best for: Team names, scores, headers
- Examples: Helvetica, Arial, Futura, DIN, Roboto

**Condensed Fonts (Scores/Headers):**

- Bold, impactful, space-efficient
- Best for: Large scores, "GOAL!", "FINAL"
- Examples: Bebas Neue, Impact, Oswald

**Geometric Fonts (Modern Brands):**

- Contemporary, tech-forward
- Best for: Modern teams, esports aesthetic
- Examples: Montserrat, Gotham, Circular

**Avoid:**

- Script or handwritten fonts (poor readability)
- Serif fonts (too traditional for most matchday graphics)
- Overly decorative typefaces

---

### Text Hierarchy

**Level 1 (Primary) - Scores, Main Info:**

- Size: Extra large (XL)
- Weight: Black (900)
- Purpose: Immediate visual focus
- Example: Final score numbers

**Level 2 (Secondary) - Team Names, Labels:**

- Size: Large (L)
- Weight: Bold (700)
- Purpose: Key identification
- Example: Team names, "HALFTIME"

**Level 3 (Tertiary) - Details:**

- Size: Medium (M)
- Weight: Medium to Bold (500-700)
- Purpose: Supporting information
- Example: Match date, venue, time

**Level 4 (Supplementary):**

- Size: Small (S)
- Weight: Regular to Medium (400-500)
- Purpose: Fine print, extra details
- Example: Competition name, matchday number

---

### Readability Rules

**Contrast:**

- Minimum 4.5:1 contrast ratio (WCAG AA)
- 7:1 for AAA accessibility
- Test: Can you read it on a phone at arm's length?

**Size:**

- Mobile viewing: Minimum 14pt for body text
- Headers: 24pt+ for readability
- Scores: 48pt+ for impact

**Spacing:**

- Letter spacing (tracking): Slightly open for all caps
- Line spacing (leading): 1.2-1.5x font size
- Don't cram: White space improves readability

**Alignment:**

- Centered: Best for symmetrical designs, scores
- Left-aligned: Good for lists, lineups
- Right-aligned: Rarely used, special cases
- Justified: Avoid (creates awkward spacing)

---

## Color Guidelines

### Team Color Application

**Dominant Team Color:**

- Use as background for single team graphics
- 70-80% of graphic area
- Establishes clear identity

**Split Team Colors (vs graphics):**

- 50/50 split for balanced matchups
- Vertical or horizontal division
- "VS" centered between

**Accent Colors:**

- Gold: Victory, celebration, premium
- Red: Urgency, live updates, alerts
- White/Black: Neutral, professional

**Background Options:**

- Solid team color
- Gradient (darker to lighter)
- Team color + neutral (color block + white)
- Full neutral (white/black) with color accents

---

### Color Psychology

**Red:**

- Urgency, live, breaking news
- Goal alerts, urgent countdowns
- Energy, excitement

**Gold/Yellow:**

- Victory, celebration, premium
- Trophy graphics, final winners
- Success, achievement

**Blue:**

- Trust, professional, calm
- Informational graphics
- Traditional broadcast aesthetic

**Green:**

- Positive status (qualified teams)
- Confirmation, success
- Field/pitch representation

**Black/White:**

- Minimal, elegant, modern
- High contrast, clarity
- Professional, serious

---

### Accessibility Considerations

**Color Blindness:**

- Don't rely on color alone for information
- Use labels, icons, patterns in addition to color
- Test with color blindness simulators

**High Contrast:**

- Ensure text readable on colored backgrounds
- Use white text on dark, dark text on light
- Avoid low-contrast color combinations (grey on grey)

**Text Size:**

- Large enough for mobile viewing
- Consider older audiences
- Test on actual phone screen

---

## Platform-Specific Guidelines

### Instagram

**Feed (1:1 Square):**

- Most versatile format
- Good for scores, brackets, countdowns
- Thumbnail visible in profile grid

**Stories (9:16 Vertical):**

- Full-screen mobile experience
- Best for urgent updates, countdowns
- Time-sensitive content
- Interactive elements possible (polls, quizzes)

**Reels (9:16 Vertical):**

- Video-first but can use static graphics
- Under 90 seconds
- Engaging, dynamic content

**Recommendations:**

- Use 1:1 for feed posts (tournament info, results)
- Use 9:16 Stories for live updates, countdowns
- Consistent branding across formats

---

### Twitter/X

**Standard Post (1:1 or 16:9):**

- 1:1 shows fully in feed
- 16:9 crops slightly but works
- Clean, quick information

**Recommendations:**

- 1:1 square for most matchday graphics
- Bold text for timeline visibility
- Quick, scannable information

---

### Broadcast / TV (16:9)

**Landscape Format:**

- 16:9 standard for TV
- Horizontal information layout
- Desktop and TV viewing

**Considerations:**

- Larger screens = more detail possible
- Readable from distance
- Professional broadcast quality

---

### Mobile Apps

**Variable Aspect Ratios:**

- Consider various screen sizes
- 9:16 or 4:5 for mobile-first
- Scrollable content acceptable

**Thumb-Friendly:**

- Readable at phone viewing distance
- Large touch targets if interactive
- Fast-loading graphics

---

## Common Issues & Solutions

### Issue: Text Too Small or Unreadable

**Solutions:**

- Increase font size in prompt: "large bold typography"
- Request "readable text" explicitly
- Use `--quality 2` in Midjourney
- Simplify design, fewer text elements
- Increase contrast: "high contrast white text on dark background"

---

### Issue: Cluttered or Busy Design

**Solutions:**

- Add "minimal," "clean," "organized" to prompt
- Reduce number of elements: focus on key information only
- Request "white space," "breathing room"
- Use "Swiss design" or "brutalist" for extreme minimalism
- Negative prompt: "no clutter, no decoration, simple design"

---

### Issue: Wrong Aspect Ratio or Cropping

**Solutions:**

- Explicitly specify aspect ratio: `--ar 9:16` or "9:16 Story format"
- Mention format in prompt: "Instagram Story format," "square social post"
- Check preview before finalizing
- Re-generate with correct AR specified

---

### Issue: Colors Don't Match Team

**Solutions:**

- Specify exact colors: "royal blue," "bright red," "gold"
- Reference real teams if possible: "Barcelona red and blue stripes"
- Use hex codes if tool supports
- Iterate with color adjustments

---

### Issue: Information Hierarchy Unclear

**Solutions:**

- Specify hierarchy in prompt: "score largest, team names secondary, details small"
- Request "clear visual hierarchy"
- Use "bold score numbers, smaller team names"
- Simplify: reduce competing elements

---

### Issue: Text Content Incorrect (AI Hallucination)

**Solutions:**

- Be very explicit about text: "text reads 'FINAL SCORE'"
- Specify exact wording needed
- Accept that AI may not render exact text perfectly
- Plan to overlay text manually in design tool if critical
- Use DALL-E (sometimes better at text than Midjourney)

---

## Workflow Optimization

### Batch Creation Approach

**Morning of Match Day:**

1. Generate fixture/countdown graphics early
2. Prepare lineup templates (add real names later)
3. Create score update templates

**During Match:**

1. Update live scores in real-time
2. Goal alerts immediately
3. Halftime score update

**After Match:**

1. Full-time result graphic
2. Celebration content (if victory)
3. Match recap summary

---

### Template System

**Create Reusable Templates:**

- Standard score layouts
- Fixture announcement formats
- Countdown designs
- Lineup formations

**Customize Per Match:**

- Update team names/colors
- Insert scores/times
- Adjust for specific match importance

**Benefits:**

- Faster turnaround
- Consistent branding
- Less repetitive work

---

### Iteration Strategy

**First Pass:**

- Generate multiple variations with different prompts
- Review for layout, readability, aesthetic

**Second Pass:**

- Refine best option with adjusted parameters
- Test different colors, aspect ratios

**Final Polish:**

- Manually adjust if needed (Photoshop, Figma)
- Add exact text overlays
- Export in correct formats

---

## Quality Standards

### Professional Checklist

Before publishing any matchday graphic:

- [ ] **Readability:** Text clear on mobile screen?
- [ ] **Accuracy:** All info (scores, names, times) correct?
- [ ] **Branding:** Consistent with team/league identity?
- [ ] **Aspect Ratio:** Correct for platform?
- [ ] **Contrast:** Sufficient for accessibility?
- [ ] **Hierarchy:** Clear visual priority of information?
- [ ] **Spelling:** All names and text spelled correctly?
- [ ] **Color:** Team colors accurate?
- [ ] **Alignment:** Elements properly aligned?
- [ ] **White Space:** Breathing room, not cluttered?
- [ ] **Quality:** High-resolution, sharp, professional?
- [ ] **Timely:** Relevant and current information?

---

## Advanced Techniques

### Layering for Flexibility

**Background Layer:**

- Team colors, gradients, patterns
- Easy to swap for different teams

**Content Layer:**

- Scores, text, information
- Template-based, reusable structure

**Accent Layer:**

- Confetti, effects, celebration elements
- Add/remove based on context

---

### Animation Preparation

If planning motion graphics:

**Static to Animated:**

- Design with animation in mind
- Leave space for motion
- Plan enter/exit animations

**Staggered Elements:**

- Score appears first
- Then team names
- Then supporting details

**Transition Frames:**

- Create variations for different match stages
- Halftime → full-time transition

---

### Brand Consistency

**Color Palette:**

- Define 3-5 core colors
- Use consistently across all graphics
- Team primary, secondary, accent

**Typography System:**

- Choose 1-2 font families
- Define usage rules (headers, body, scores)
- Maintain across all matchday content

**Layout Grid:**

- Establish spacing system
- Consistent margins and padding
- Reusable grid structure

**Visual Style:**

- Minimal vs. bold vs. photographic
- Choose and stick with it
- Builds recognition

---

## Related Matchday Graphics

Explore specialized matchday graphic types:

- **[Fixture Announcement Graphics](matchday-fixture-announcement.md)** - Match announcements and previews
- **[Countdown & Schedule Graphics](matchday-countdown-schedule.md)** - Match timing and schedules
- **[Tournament Bracket Graphics](matchday-tournament-bracket.md)** - Tournament structure and standings
- **[Squad Lineup Graphics](matchday-squad-lineup.md)** - Team formation and lineup displays
- **[Score Updates Graphics](matchday-score-updates.md)** - Live scores and final results

---

## Quick Reference: Prompt Templates

### Minimal Info Graphic

```
[Graphic type], clean typographic layout, [team colors], modern sports graphic, minimal design, [aspect ratio] format --ar [ratio] --stylize 200 --quality 2 --style raw
```

### Bold Celebration Graphic

```
[Graphic type], [winning team] colors dominant, bold typography, celebration energy, gold confetti overlay, shareable social format --ar 1:1 --stylize 600 --quality 2
```

### Live Urgent Update

```
[Graphic type], "LIVE" in red, urgent breaking news aesthetic, high contrast, bold score display, modern sports broadcast style, 9:16 Story --ar 9:16 --stylize 400 --quality 2
```

### Professional Broadcast Style

```
[Graphic type], professional broadcast quality, clean layout, [team colors], modern typography, TV sports aesthetic, 16:9 horizontal --ar 16:9 --stylize 350 --quality 2
```

---

**Master Collection:** [PROMPT.MATCHDAY.txt](PROMPT.MATCHDAY.txt) - Complete matchday graphics prompt library.
