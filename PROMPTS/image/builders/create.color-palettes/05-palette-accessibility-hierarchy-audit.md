# Palette Accessibility and Hierarchy Audit

## Description

Audit a palette in context for contrast, value hierarchy, ratio discipline, color-vision resilience, semantic clarity, and real-device legibility. The tool separates palette problems from spacing, hierarchy, or concept problems before recommending changes.

## Best For

- Final design review
- UI and web accessibility
- Brand-system validation
- Mobile and outdoor-use testing
- Diagnosing palettes that look attractive but fail in production

## Inputs

- Palette values and assigned roles
- Screenshot, mockup, or token map showing actual use
- Text sizes, component states, and target accessibility level
- Intended devices and viewing conditions

## Tool Prompt

```text
Audit the supplied palette and design for hierarchy, accessibility, semantic clarity, and real-world use. Do not assume that recoloring is the correct fix; first distinguish color failures from spacing, typography, composition, and interaction-design failures.

CONTRAST FLOORS
Calculate and report contrast ratios for every text-background, icon-background, border-background, and interactive-state pairing.

Use these minimum targets:
- Body text: 4.5:1
- Large text at 24px or larger: 3:1
- Icons, controls, focus indicators, and meaningful UI edges: 3:1
- Decoration only: no required floor, but confirm that it carries no meaning

THREE-CHECK PASS
1. GREYSCALE: Remove hue mentally or computationally. Report whether hierarchy, controls, and focal order survive through value alone.
2. PHONE: Evaluate likely legibility on a phone outdoors at approximately 40% brightness. Flag low-contrast surfaces, thin type, subtle borders, and glare-sensitive combinations.
3. RED-GREEN: Simulate common red-green color-vision deficiencies. Confirm that destructive, success, warning, selection, and action states retain non-color labels, icons, patterns, or shape distinctions.

RATIO AND ROLE AUDIT
Check whether Base, Structure, Signature, and Accent approximately follow 60 / 30 / 7 / 3. Flag:
- equal-volume colors producing multiple competing bases
- pure black or white breaking a warm or hue-biased system
- an accent promoted into a background
- colors at equal value causing vibrating edges or unreadable type
- gradients hiding incompatible colors
- absence of a dark structural anchor
- colors chosen before the purpose and semantic roles were defined

MOTIVATION AUDIT
For every signature or accent use, name its source or semantic job: brand mark, action, status, object, light source, chapter, or human element. Flag arbitrary decoration.

OUTPUT
Return:
1. Pass/fail summary
2. Contrast matrix with exact ratios
3. Greyscale hierarchy findings
4. Outdoor-phone findings
5. Color-vision findings
6. Role and ratio findings
7. Seven highest-priority issues ordered by severity
8. Minimal corrections with old and new values
9. Items that should be fixed through spacing, type, or hierarchy instead of color

Preserve the palette's intent whenever possible. Recommend the smallest value, saturation, ratio, or semantic change that resolves each failure.
```

## Quality Checklist

- [ ] Every meaningful foreground-background pairing has a measured ratio.
- [ ] Body text, large text, icons, and UI edges meet their stated floors.
- [ ] Hierarchy survives in grayscale.
- [ ] Mobile outdoor legibility is assessed.
- [ ] Red-green states include redundant non-color signals.
- [ ] Base, Structure, Signature, and Accent usage is audited.
- [ ] Recommendations separate color issues from layout and typography issues.
- [ ] Corrections are minimal and include exact before-and-after values.

## Source

Adapted from **The Cinema Colour Vault** by [@itsdesignare](https://www.instagram.com/itsdesignare/).
