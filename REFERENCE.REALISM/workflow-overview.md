# AI Realism Workflow - Progressive Zoom Photography

## Overview

This workflow creates ultra-realistic AI-generated images with progressive zoom sequences, focusing on maintaining photographic authenticity and avoiding AI artifacts. The complete process takes approximately **4-6 hours** to produce a final progressive zoom video from reference to finished edit.

### Quick Navigation

- [7-Step Process](#7-step-process)
- [Key Principles for Realism](#key-principles-for-realism)
- [Platform Requirements](#platform-requirements)
- [Time & Cost Estimates](#time--cost-estimates)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
- [Related Documentation](#related-documentation)

---

## 7-Step Process

### Step 1: Find a Realistic Reference Image on Pinterest

**Time**: 15-30 minutes

**What to Look For**:

- Natural lighting, authentic textures, and photographic quality
- Avoid heavily edited or filtered images
- Choose images with clear facial details if creating portraits
- Look for consistent lighting (no harsh mixed light sources)
- Prefer outdoor or natural light scenarios

**Best Search Terms**:

- "natural portrait photography"
- "candid portrait natural light"
- "authentic photography unfiltered"
- "photojournalism portraits"

**Pro Tips**:

- Images with visible skin texture are ideal (not overly smoothed)
- Avoid studio portraits with heavy makeup/retouching
- Look for slight imperfections—this is what makes it realistic

### Step 2: Analyze the Image with Claude

**Time**: 5-10 minutes
**Platform**: Claude (https://claude.ai or via API)

**What Claude Identifies**:

- Key visual elements: lighting, framing, composition, style
- Technical details: depth of field, color temperature, camera angles
- Subject characteristics: pose, expression, wardrobe, setting
- Photographic qualities: lens type, focal length, bokeh style

**Example Prompt to Claude**:

> "Analyze this image in detail and create a comprehensive prompt for AI image generation. Focus on: lighting direction and quality, color temperature, depth of field, framing, composition, subject details, skin texture, background elements, and overall photographic style. The goal is to capture the realism and technical qualities, not to copy the exact image."

**What You Get**:

- Detailed written prompt ready for image generation
- Technical specifications (lighting, camera settings, etc.)
- Style descriptors to guide the AI

### Step 3: Generate Base Image with GPT Image 2 on Deevid AI

**Time**: 5-10 minutes (generation)
**Platform**: Deevid AI - Image Generation (https://deevid.ai/app/image)
**Model**: GPT Image 2

**Process**:

1. Navigate to Deevid AI image generation section
2. Select GPT Image 2 model
3. Paste Claude's analyzed prompt
4. Generate the base image
5. Review and regenerate if needed

**Important**:

- Focus on matching the reference's realism, not copying it exactly
- Goal is to capture the lighting, framing, vibe, and photographic style
- Identity will be different—that's expected and desired
- May need 2-3 attempts to get the right feel

### Step 4: Validate Base Image Quality

**Time**: 5 minutes

**Key Validation Points**:

- ✓ Photographic feel and technical qualities captured
- ✓ Authentic textures and natural appearance maintained
- ✓ No obvious AI-generated artifacts
- ✓ Lighting feels natural and consistent
- ✓ Skin texture shows realistic pores and detail (not smoothed)
- ✓ No plastic or CGI-looking skin
- ✓ Natural color temperature and exposure

**Critical Reminder**:

> The goal is not to copy the reference image—it is to copy the **realism, lighting, framing, vibe, and style**. Your AI-generated subject will have different features, and that's correct.

**If Image Needs Refinement**:

- Adjust prompt to emphasize natural textures
- Add "no beauty filters, no skin smoothing" to prompt
- Emphasize "photographic realism" and "visible pores"
- Try regenerating 1-2 times

### Step 5: Generate Progressive Zoom Sequence

**Time**: 60-90 minutes
**Platform**: Deevid AI - GPT Image 2
**Total Images**: 7 (base portrait + 6 zoom levels)

**Progressive Zoom Sequence**:

1. **Base Portrait** - Full close-up (starting point)
2. **Mouth Macro** - Extreme close-up of lips/teeth
3. **Nose Macro** - Extreme close-up of nose/upper lip
4. **Portrait Close-up** - Tighter portrait crop (70% head)
5. **Eye Macro** - Single eye extreme close-up
6. **Eyebrow Macro** - Eyebrow region with individual hairs
7. **Single Hair Microscopic** - Ultra-extreme zoom on single hair strand

**Critical Success Factors**:

- Maintain complete identity consistency across all zoom levels
- Preserve lighting, color temperature, and atmospheric qualities
- Use specialized prompts for each zoom level (see [realism-image-prompts-progressive-zoom.md](realism-image-prompts-progressive-zoom.md))
- Each subsequent zoom should feel like optical magnification of the previous image
- Lock anatomical features—no drift in nose shape, lip contours, eye structure

**Detailed Prompts**:
Use the comprehensive prompts in [realism-image-prompts-progressive-zoom.md](realism-image-prompts-progressive-zoom.md) for each zoom level. These prompts include specific instructions for maintaining identity consistency and avoiding AI artifacts.

### Step 6: Animate Transitions with Deevid AI Video Generation

**Time**: 60-90 minutes (includes generation wait time)
**Platform**: Deevid AI - Video Generation (https://deevid.ai/app/video)
**Model**: Omni Reference Master V4.0
**Settings**: 720P, 9:16 vertical, 4 seconds per transition
**Total Videos**: 6 transitions

**Video Transitions to Generate**:

1. **Video 1**: Portrait → Mouth zoom
2. **Video 2**: Mouth → Nose upward tilt
3. **Video 3**: Portrait speaking ("Hi, I'm not real")
4. **Video 4**: Portrait → Eye zoom with blink
5. **Video 5**: Eye → Eyebrow upward slide with blink
6. **Video 6**: Eyebrow → Single Hair microscopic zoom

**Process for Each Transition**:

1. Open Deevid AI video generation
2. Select "Omni Reference" mode
3. Choose "Master V4.0" model
4. Set resolution to 720P, aspect ratio 9:16
5. Upload start frame (Image N)
6. Upload end frame (Image N+1)
7. Set duration to 4 seconds
8. Paste transition-specific prompt (see [realism-video-prompts-transitions.md](realism-video-prompts-transitions.md))
9. Generate and download

**Key Requirements**:

- Smooth keyframe-planned camera movements (no handheld feel)
- Zero identity drift during transitions
- No distortion, morphing, or stretching artifacts
- Maintain lighting and color temperature consistency
- Ultra-low motion blur (keep details sharp)

**Detailed Prompts**:
Use the comprehensive video prompts in [realism-video-prompts-transitions.md](realism-video-prompts-transitions.md) for each transition. These include specific authenticity constraints and technical requirements.

### Step 7: Final Assembly in CapCut

**Time**: 60-90 minutes
**Software**: CapCut (free, cross-platform)
**Alternative Software**: Adobe Premiere Pro, Final Cut Pro, DaVinci Resolve

**Assembly Process**:

1. **Import All Assets**
   - 7 images (optional, for reference)
   - 6 video transitions
   - Organize in project bins

2. **Arrange on Timeline**
   - Place all 6 transitions in sequence
   - Ensure no gaps between clips
   - Verify proper order (Portrait→Mouth→Nose→Portrait→Eye→Eyebrow→Hair)

3. **Add Subtle Motion Keyframes**
   - Apply slight zoom-in between transitions for continuity
   - Add gentle camera movement to enhance flow
   - Use ease-in/ease-out curves for smooth acceleration

4. **Fine-Tune Timing**
   - Adjust transition speeds if needed
   - Ensure consistent pacing throughout
   - May speed up or slow down individual sections

5. **Color Grading (Optional)**
   - Ensure consistent exposure across all clips
   - Match color temperature if slight variations exist
   - Avoid heavy grading—maintain photographic realism

6. **Audio (Optional)**
   - Add subtle ambient sound if desired
   - Keep Video 3 audio ("Hi, I'm not real") or replace with cleaner recording
   - Consider atmospheric music or soundscape

7. **Export Settings**
   - Resolution: 1080p minimum (match source)
   - Frame Rate: 30fps or match source
   - Bitrate: High (20-50 Mbps for 1080p)
   - Format: MP4 (H.264 or H.265)
   - Aspect Ratio: 9:16 (vertical)

**Final Result**:
The complete video should feel like **one single, continuous camera zoom** from full portrait to microscopic detail, with no jarring cuts or obvious AI artifacts.

## Key Principles for Realism

### Authenticity Over Perfection

- **Preserve natural imperfections**: pores, freckles, asymmetry, uneven skin tone
- **Avoid beauty filters**: no skin smoothing, no plastic-looking skin, no over-sharpening
- **No CGI feel**: maintain raw, biological texture quality

### Identity Consistency

- **Zero identity drift**: facial structure, features, and proportions must remain identical across all zoom levels
- **Lock anatomical details**: nose shape, lip contours, eye structure, brow position
- **Maintain natural asymmetry**: preserve the subject's unique facial characteristics

### Technical Realism

- **Authentic depth of field**: natural bokeh and focus falloff based on lens physics
- **Consistent lighting**: preserve ambient light direction, color temperature, highlights, and shadows
- **Proper macro behavior**: realistic focus planes, shallow depth of field at extreme magnifications
- **No distortion**: avoid warping, stretching, morphing, or liquefying artifacts

### Micro-Detail Accuracy

- **Visible skin texture**: individual pores of varying sizes, micro-ridges, natural oil sheen
- **Realistic hair rendering**: individual strands with natural direction, thickness variation, stray hairs
- **Authentic surface details**: fine vellus hair (peach fuzz), subtle pigmentation variations
- **Biological accuracy**: follicle openings, skin translucency, capillary color variations

---

## Platform Requirements

### Required Platforms

| Platform      | Purpose                            | Access                | Cost                  |
| ------------- | ---------------------------------- | --------------------- | --------------------- |
| **Pinterest** | Reference image sourcing           | https://pinterest.com | Free                  |
| **Claude**    | Image analysis & prompt generation | https://claude.ai     | Free tier available   |
| **Deevid AI** | Image & video generation           | https://deevid.ai     | Subscription required |
| **CapCut**    | Video editing & assembly           | Download app          | Free                  |

### Deevid AI Specifications

**Image Generation**:

- Model: GPT Image 2
- Access: https://deevid.ai/app/image
- Resolution: Variable (typically 1024x1024 or higher)
- Use Case: Base image + 6 progressive zoom images

**Video Generation**:

- Model: Omni Reference Master V4.0
- Access: https://deevid.ai/app/video
- Resolution: 720P
- Aspect Ratio: 9:16 (vertical)
- Duration: 4 seconds per transition
- Mode: Start Frame + End Frame (keyframe-based)
- Use Case: 6 transition videos

---

## Time & Cost Estimates

### Time Breakdown

| Step                            | Time Required |
| ------------------------------- | ------------- |
| 1. Find reference image         | 15-30 minutes |
| 2. Claude analysis              | 5-10 minutes  |
| 3. Generate base image          | 5-10 minutes  |
| 4. Validate quality             | 5 minutes     |
| 5. Generate 6 zoom images       | 60-90 minutes |
| 6. Generate 6 video transitions | 60-90 minutes |
| 7. Final assembly in CapCut     | 60-90 minutes |
| **Total**                       | **4-6 hours** |

### Cost Estimates

**Deevid AI Subscription**:

- Pricing varies (check https://deevid.ai for current rates)
- Typically requires credits/subscription for GPT Image 2 and video generation
- Estimate: $20-50/month for active usage

**All Other Tools**: Free

---

## Troubleshooting Common Issues

### Identity Drift Between Zoom Levels

**Problem**: Subject looks different at various zoom levels

**Solutions**:

- Use previous image as reference in next prompt
- Emphasize "same person, same features" in prompts
- Lock specific anatomical details (nose shape, lip contours, eye color)
- Generate multiple attempts and select most consistent
- Use phrases like "optical zoom of existing image, not new portrait"

### AI Artifacts or Plastic-Looking Skin

**Problem**: Skin looks too smooth, CGI-like, or has obvious AI artifacts

**Solutions**:

- Add negative prompts: "no beauty filters, no skin smoothing, no plastic skin"
- Emphasize: "visible pores, natural skin texture, raw biological texture"
- Reference: "photographic realism, not illustration"
- Avoid: "perfect skin" or "flawless" in prompts
- Try regenerating with emphasis on imperfections

### Motion Blur or Distortion in Video Transitions

**Problem**: Videos show warping, morphing, or excessive blur during transitions

**Solutions**:

- Emphasize in prompt: "ultra-low motion blur, no distortion"
- Specify: "smooth keyframe-planned movement, not handheld"
- Use Master V4.0 model (better for stable transitions)
- Ensure start and end frames are very similar (avoid extreme angle changes)
- Try shorter duration (3 seconds instead of 4)

### Lighting Inconsistency Across Sequence

**Problem**: Lighting changes between zoom levels or transitions

**Solutions**:

- Lock lighting in every prompt: "same ambient lighting, same color temperature"
- Reference: "exact same lighting as base image"
- Avoid: Studio lighting, HDR, cinematic grading
- Use phrases: "natural daylight consistency throughout"
- Color grade in CapCut to unify if slight variations exist

### Video Generation Taking Too Long

**Problem**: Deevid AI video generation stuck or extremely slow

**Solutions**:

- Check platform status (may be high demand)
- Try different time of day (off-peak hours)
- Verify account/credit status
- Reduce complexity in prompt
- Try alternative model if available

### CapCut Assembly Issues

**Problem**: Transitions don't align smoothly in final edit

**Solutions**:

- Add crossfade transitions (0.5-1 second) between clips
- Use motion blur effect to smooth jarring cuts
- Add subtle zoom keyframes to mask discontinuities
- Adjust speed of individual clips to better match
- Use color grading to unify look across all clips

---

## Related Documentation

### Core Workflow Files

- **[realism-image-prompts-progressive-zoom.md](realism-image-prompts-progressive-zoom.md)**
  Complete image prompt templates for all 7 zoom levels with detailed technical specifications

- **[realism-video-prompts-transitions.md](realism-video-prompts-transitions.md)**
  Video transition prompt templates for all 6 transitions with authenticity constraints

### Universal Realism Principles

- **[PROMPTS/image/builders/realism/realism-for-commercial-and-ugc-photography.md](../../PROMPTS/image/builders/realism/realism-for-commercial-and-ugc-photography.md)**
  The 7 Realism Rules, commercial product photography prompts, UGC techniques, troubleshooting guide for AI tells

  **Key Content**: Destroy perfection principle, phone camera logic, physical evidence techniques, natural lighting strategies, micro-detail examples (chrome nails, eyes macro, ice cube mouth), influencer realism stack formula

### Quick Reference

**Image Sequence** (7 images):

1. Base Portrait → 2. Mouth Macro → 3. Nose Macro → 4. Portrait Close-up → 5. Eye Macro → 6. Eyebrow Macro → 7. Single Hair Microscopic

**Video Sequence** (6 transitions):

1. Portrait→Mouth → 2. Mouth→Nose → 3. Portrait Speaking → 4. Portrait→Eye → 5. Eye→Eyebrow → 6. Eyebrow→Hair

---

## Version History

- **v2.0** (2026-08-07) - Enhanced with detailed step breakdowns, platform specifications, troubleshooting guide
- **v1.0** - Initial workflow documentation

---

**Document Type**: Master Workflow Guide  
**Technique**: Progressive Zoom Realism Photography  
**Platforms**: Claude, GPT Image 2 (Deevid AI), CapCut  
**Output**: Ultra-realistic progressive zoom video sequence  
**Last Updated**: 2026-08-07
