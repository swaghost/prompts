---
name: Nightclub Booth Flash (half-body, party candids)
description: This prompt generates a photorealistic half-body portrait of a young adult woman in a nightclub setting. The subject is depicted with specific attributes such as dark brown hair, trendy black clothing, and silver hoop jewelry, captured in a candid, nightlife atmosphere. The prompt emphasizes a fun and confident mood, using realistic lighting and camera settings to create an energetic nightlife scene. Constraints include no logos, watermarks, or identifiable faces in the background.
---
{
  "category": "NIGHTCLUB_BOOTH_FLASH",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking, nightlife vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Slightly messy, night-out texture",
      "texture": "Strands visible, slight shine",
      "movement": "Hair slightly displaced as if dancing"
    },
    "face": {
      "eyes": "Bright, playful",
      "skin_details": "Real texture, slight flash shine",
      "makeup": "Night-out natural glam"
    },
    "clothing": {
      "outfit": "Trendy black outfit, no logos",
      "fabric": "Realistic fabric sheen (not plastic)"
    },
    "accessories": {
      "jewelry": ["Silver hoops"],
      "props": ["Simple drink glass (no labels)"]
    }
  },
  "pose": {
    "type": "Half-body candid booth shot",
    "orientation": "Leaning slightly toward camera",
    "hands": "One hand holding glass, other brushing hair back",
    "gaze": "Direct eye contact",
    "expression": "Playful smirk"
  },
  "setting": {
    "environment": "Nightclub booth",
    "background_elements": [
      "Colored lights bokeh",
      "Soft atmospheric haze (not smoke)",
      "Crowd silhouettes blurred (no faces identifiable)"
    ],
    "depth": "Face sharp, background bokeh heavy"
  },
  "camera": {
    "shot_type": "Half-body nightlife portrait",
    "angle": "Eye-level, handheld",
    "focal_length_equivalent": "26mm phone night mode",
    "framing": "4:5",
    "focus": "Eyes sharp, background soft"
  },
  "lighting": {
    "source": "Phone flash + ambient club lights",
    "highlights": "Flash pop on face, realistic shine",
    "shadows": "Soft but contrasty nightlife look"
  },
  "mood_and_expression": {
    "tone": "Fun, confident, candid",
    "atmosphere": "Energetic nightlife"
  },
  "style_and_realism": {
    "style": "Photorealistic party UGC",
    "imperfections": "Grain, slight blur in background"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Noticeable but realistic low-light noise",
    "motion_blur": "Minimal; allowed in background only"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "readable signage", "logos", "watermark",
    "plastic skin", "cgi",
    "extra limbs", "warped hands"
  ]
}