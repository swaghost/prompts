# Effect Guide Template Format

## Overview

This document describes the visual and informational structure used in the "Learn with Kayo" effect guides. Use this template when creating new effect guides to maintain consistency and clarity.

---

## Document Structure

### Title Page

```
PLATFORM/VERSION NAME (e.g., "SEEDANCE 2.0")

EFFECT NAME
Large, bold, attention-grabbing

Tagline/Description
Concise explanation of the effect in italics

[Hero image showing the effect]

Creator credit (e.g., "L E A R N W I T H K A Y O")
Platform credit (e.g., "Made with Higgsfield")
```

### Page Layout Pattern

Each step follows this consistent structure:

```
STEP NUMBER (e.g., "S T E P 0 1")
Descriptive subtitle in italics

SECTION TITLE
Bold, uppercase, prominent

- Bulleted instruction list
- Clear, actionable steps
- One concept per bullet

[Supporting image showing the step]

Footer: Creator credit + Page number
```

---

## Content Components

### Step 01: Source Material

_Always the foundation_

**Purpose**: Capture the base footage or image  
**Structure**:

- Title: "YOUR FOOTAGE" (or equivalent)
- Subtitle: "The frame everything hangs on" (or similar metaphor)
- Instructions for capturing source material
- **Critical warnings** in bold about precision requirements
- Visual example of what to capture

### Step 02: Platform Setup

_Configuration and settings_

**Purpose**: Technical setup instructions  
**Structure**:

- Title: Platform/tool name (e.g., "SEEDANCE 2.0")
- Subtitle: "Set it up properly"
- Numbered list of setup steps (01, 02, 03, 04...)
- **Settings box** with key technical specs
  - Duration / Aspect Ratio / Resolution
  - Other critical parameters

### Step 03: The Prompt/Instructions

_The core technique_

**Purpose**: Detailed prompt or technical instructions  
**Structure**:

- Title: "THE PROMPT" (or "THE TECHNIQUE")
- Subtitle: "Paste this in" (or similar action phrase)
- **Code block or indented section** containing full prompt
- If complex, break down into labeled sections:
  - SCENE CONTEXT
  - CAMERA
  - ACTION
  - PHYSICS
  - AUDIO
  - POSITIVE LOCKS (constraints)

### Step 04: Post-Processing

_Where it becomes the final effect_

**Purpose**: Editing and assembly instructions  
**Structure**:

- Title: "THE EDIT" (or equivalent)
- Subtitle: "Where it becomes an effect"
- Numbered editing steps (01, 02, 03, 04...)
- **Optional enhancement box**: "SELL IT FURTHER"
  - Additional tips for polishing
  - "Worth playing with once the cut is working"

### Troubleshooting Section

_Common issues and solutions_

**Purpose**: Help users debug problems  
**Structure**:

- Title: "WHEN IT FIGHTS YOU" (or "TROUBLESHOOTING")
- Multiple problem boxes, each containing:
  - **PROBLEM TITLE IN CAPS**
  - Problem description
  - Cause explanation
  - Solution steps

**Pattern**:

```
THE ISSUE NAME

Description of what's going wrong.
Solution: How to fix it.
```

---

## Design Principles

### Visual Hierarchy

1. **Step Numbers**: Always prominent at top (e.g., "S T E P 0 1")
2. **Section Titles**: Bold, uppercase, large
3. **Subtitles**: Italics, smaller, descriptive
4. **Body Text**: Clear, concise paragraphs
5. **Emphasis**: Bold for critical information
6. **Code/Prompts**: Indented boxes or distinct formatting

### Typography Patterns

- **Main headings**: UPPERCASE BOLD
- **Subheadings**: _Italicized descriptive phrases_
- **Instructions**: Sentence case with clear bullets
- **Technical specs**: Monospace or boxed format
- **Warnings**: Bold inline or in boxes

### Color/Visual Coding

- **Gold/Warm accent**: For headings and decorative elements
- **Neutral background**: Cream/beige for readability
- **Boxed sections**: For settings and important callouts
- **Corner brackets**: Framing design element for pages

### Information Flow

**Progressive Disclosure Pattern**:

1. What to capture (foundation)
2. How to set up (configuration)
3. Core technique (the secret sauce)
4. How to finish (assembly)
5. How to fix (troubleshooting)

---

## Writing Style Guidelines

### Voice and Tone

- **Direct and actionable**: "Film yourself jumping" not "You should film yourself"
- **Conversational but precise**: "Worth playing with once the cut is working"
- **Metaphorical section titles**: "The frame everything hangs on"
- **Encouraging endings**: "Now go and freeze something."

### Instruction Format

**Do**:

- Use imperative verbs (Cut, Upload, Generate)
- Number sequential steps
- Bold critical requirements
- Provide context for why steps matter

**Don't**:

- Use passive voice
- Bury important details
- Skip the "why" when it matters
- Over-explain simple concepts

### Emphasis Patterns

- **Bold**: Critical requirements, warnings, key terms
- _Italics_: Subtitles, metaphorical descriptions, "soft" emphasis
- UPPERCASE: Section titles, settings labels, problem headings
- `Code blocks`: Prompts, technical specifications, exact values

---

## Section-Specific Guidelines

### Settings Boxes

Always include when relevant:

```
S E T T I N G S

Duration / Aspect Ratio / Resolution
Platform-specific parameters
```

### Numbered Lists

Use when steps must be sequential:

```
01  First action with clear outcome
02  Second action building on first
03  Third action completing the sequence
```

### Bulleted Lists

Use for non-sequential information:

```
- Key point about technique
- Important consideration
- Additional detail
```

### Critical Warnings Format

```
- **Critical requirement in bold**: Explanation of why it matters and what happens if you don't follow it.
```

### Code/Prompt Blocks

```
Indent or box all technical content that should be copied exactly.
Use clear section headers within prompts.
Maintain consistent spacing and formatting.
```

---

## Template Usage Example

```markdown
# [Effect Name] Guide

## Overview

**Effect Name**: [Name]
**Tagline**: [One-line description]
**Platform**: [Tool/software name]
**Creator**: [Attribution]

[Brief description of what the effect does and why it's cool]

---

## Step 01: [Foundation Step Name]

_[Descriptive subtitle]_

### [Section Title]

1. **[First action]**
   - [Detail or sub-step]
   - [Important consideration]

2. **[Second action]**
   - [Detail]

3. **⚠️ CRITICAL: [Important warning]**
   - [Why it matters]
   - [Consequence of not following]

---

## Step 02: [Setup Step Name]

_[Descriptive subtitle]_

### [Section Title]

1. [First setup instruction]
2. [Second setup instruction]
3. [Third setup instruction]
4. [Fourth setup instruction]

### Settings

- **Parameter 1**: Value
- **Parameter 2**: Value
- **Parameter 3**: Value

---

## Step 03: [Core Technique]

_[Descriptive subtitle]_

### Complete [Prompt/Instructions]
```

[Full technical content here]
[Organized with clear section headers]
[Specific values and parameters]

```

### [Breakdown if needed]

**Section 1 Name**
- [Explanation]
- [Key points]

**Section 2 Name**
- [Explanation]
- [Key points]

---

## Step 04: [Finishing Step]
*[Descriptive subtitle]*

### [Section Title]

1. [First editing step]
2. [Second editing step]
3. [Third editing step]
4. [Fourth editing step]

### [Optional Enhancement Section]

[Additional polish tips]
[Worth exploring after basics work]

---

## Troubleshooting

### [Problem 1 name]

**Problem**: [What's going wrong]
**Cause**: [Why it's happening]
**Solution**: [How to fix it]

### [Problem 2 name]

**Problem**: [What's going wrong]
**Cause**: [Why it's happening]
**Solution**: [How to fix it]

### [Problem 3 name]

**Problem**: [What's going wrong]
**Cause**: [Why it's happening]
**Solution**: [How to fix it]

---

## Key Success Factors

### Critical Elements

1. **[First critical element]**
   - [Why it matters]
   - [How to ensure success]

2. **[Second critical element]**
   - [Why it matters]
   - [How to ensure success]

### Technical Specifications Summary

- **Platform**: [Name]
- **Duration**: [Time]
- **Aspect Ratio**: [Ratio]
- **Resolution**: [Quality]
- **[Other key spec]**: [Value]
- **[Other key spec]**: [Value]

---

**[Encouraging closing line in italics or bold]**
```

---

## Quick Reference Checklist

When creating a new effect guide, ensure you have:

- [ ] Clear effect name and tagline
- [ ] Hero image showing the effect
- [ ] 4 main steps (source, setup, technique, finish)
- [ ] Settings box with technical specs
- [ ] Complete prompt or core instructions in formatted block
- [ ] Troubleshooting section (3+ common issues)
- [ ] Critical warnings highlighted in bold
- [ ] Sequential numbering where order matters
- [ ] Encouraging closing line
- [ ] Creator and platform credits
- [ ] Consistent visual hierarchy throughout
- [ ] Clear "why this matters" context for critical steps

---

## Adaptation Notes

**When adapting this format**:

- Keep the 4-step structure (foundation → setup → technique → finish)
- Maintain consistent visual hierarchy
- Use metaphorical subtitles for personality
- Bold critical requirements and warnings
- Box or indent technical specifications
- End with troubleshooting section
- Include encouraging closing statement

**Flexibility points**:

- Step count can vary (but 4 is ideal for most effects)
- Prompt structure adapts to the tool being used
- Settings parameters change per platform
- Troubleshooting items specific to the effect
