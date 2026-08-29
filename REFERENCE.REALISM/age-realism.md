# Age Realism for Human Image Prompts

## Purpose

Use this guide whenever a prompt specifies a mature, elderly, or older adult subject, especially in a portrait, close-up, or macro image. Age must read through coherent biological detail and lived experience, not through caricature, generic gray hair, or a beauty-retouched face.

## Core Rule

Describe the subject's exact age or age range, then make the visible anatomy, skin, hair, eyes, expression, and lighting agree with that age. Preserve dignity, individuality, and recognizable identity. Do not make an older subject look artificially young, generically elderly, diseased, monstrous, or prosthetic.

## Biological Age Detail

Select details appropriate to the stated age rather than stacking every aging keyword:

- **Skin structure:** visible pores, fine-to-deep wrinkles, natural furrows, uneven pigmentation, age spots, sun damage, and changing texture density across the face
- **Facial anatomy:** reduced cheek volume, subtle temple hollowing, tear troughs, realistic jowls, less defined jawline, and loose neck skin where appropriate
- **Wrinkle anatomy:** forehead lines, crow's feet, eyelid folds, vertical lip lines, nasolabial folds, and marionette lines should follow facial movement and underlying structure, with varied depth and direction
- **Hair:** silver, white, or mixed gray hair and brows only when appropriate to the subject; preserve the original growth pattern, density, hairline, styling, and natural irregularity
- **Eyes:** preserve the subject's real iris color and pattern; do not automatically add cloudy eyes, cataracts, or a lifeless gaze
- **Expression:** keep natural asymmetry, facial tension, gaze, and personality; age does not require a grimace or exaggerated sadness
- **Close-up detail:** retain pores, fine facial hairs, capillaries, scars, piercings, and small asymmetries without inventing distracting marks

## Prompt Formula

```text
[exact age or age range] [subject], unmistakably and biologically consistent with that age, recognizable individual identity, [age-appropriate wrinkle pattern and facial structure], visible pores and natural skin irregularities, realistic pigmentation and age spots where appropriate, [natural hair color/gray transition and growth pattern], exact eye color preserved, authentic expression and asymmetry, raw unretouched photographic skin, no beauty filter, no de-aging, no plastic smoothing
```

## Advanced Elderly Portrait Formula

For an elderly subject or an extreme close-up, add only the details supported by the intended age and lighting:

```text
unretouched close-up of an unmistakably elderly person, dense but anatomically natural wrinkle network with varied depth across the forehead, eyelids, crow's feet, cheeks, lips, and neck, thin delicate skin with visible pores, fine vellus hair, subtle capillaries, uneven pigmentation and age spots, realistic loss of facial volume and skin elasticity, natural gray-white hair following the original growth pattern, exact iris color retained, dignified direct gaze, RAW documentary portrait photography, no airbrushing, no de-aging, no beauty filter, no plastic skin, no CGI
```

## Identity and Dignity Constraints

- Preserve facial proportions, bone structure, eye shape and color, nose, lips, ears, hairline, distinctive marks, piercings, tattoos, and natural asymmetries.
- For age progression, change biological age while locking identity, pose, clothing, lighting, and setting unless the prompt explicitly requests otherwise.
- Let wrinkles and skin folds respond to expression, gravity, and light. Do not draw decorative lines on an otherwise young face.
- Keep the subject healthy and human. Avoid skeletal exaggeration, horror styling, vacant eyes, waxy skin, or “old person” stereotypes.
- Do not use "flawless," "poreless," "youthful," "ageless," or glamorizing retouch language unless the prompt explicitly describes a contradiction that must be avoided.

## Negative Prompt

```text
de-aged face, beauty filter, airbrushed skin, poreless skin, plastic skin, wax figure, generic elderly face, exaggerated caricature wrinkles, randomly placed lines, gray hair pasted onto a young face, cloudy eyes, cataracts unless explicitly requested, sickly or skeletal anatomy, horror makeup, prosthetic appearance, identity drift, altered iris color, excessive smoothing, CGI, illustration
```

## Builder Integration

When a builder receives an age, age range, aging direction, or reference subject with visible mature features, it must:

1. Preserve the stated age as a hard subject constraint.
2. Add age-appropriate anatomy and skin detail from this guide.
3. Lock identity and eye color when a reference image is supplied.
4. Adapt the detail to the camera distance: broad structure for full-body shots, facial anatomy for portraits, and pores/fine hairs/capillaries for macro shots.
5. Add the negative prompt constraints without overriding an explicit user request for a medical condition, injury, makeup, or fantasy transformation.