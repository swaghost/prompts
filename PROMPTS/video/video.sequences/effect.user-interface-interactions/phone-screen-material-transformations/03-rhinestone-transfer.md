# Rhinestone Phone-to-Body Transfer - Source Video VFX

## Platform

Video-to-video editor with object tracking, body-surface tracking, and photorealistic material replacement.

## Source Video Lock

Edit the uploaded video while preserving it as accurately as possible. Do not change the subject's face, body, skin, hair, clothing, hands, pose, proportions, movements, or appearance. Do not change the phone's shape, size, position, or movement. Preserve background, lighting, framing, camera movement, composition, original video quality, and original audio.

Do not add or remove anything except the rhinestone transfer effect.

## Video Prompt

```text
RHINESTONE TRANSFER EFFECT

The phone in the subject's hand has visible rhinestones on its surface. As the subject moves the phone across different parts of their body, create a realistic magical transfer effect: rhinestones transfer from the phone onto the exact body areas the phone has just passed.

TIMING

Before 00:03.48, no rhinestones appear on the subject's body. Keep the original video unchanged.

At exactly 00:03.48, the transfer begins. From 00:03.48 to 00:05.14, rhinestones appear on the exact area immediately after the phone physically touches or passes over it. They follow the precise path and timing of the phone movement. Never place rhinestones ahead of the phone.

By exactly 00:05.14, every area the phone passed over during the effect is covered with transferred rhinestones.

MATERIAL AND INTEGRATION

Transferred rhinestones are identical to the rhinestones originally attached to the phone: same size, shape, color, sparkle, texture, and density. Make the transfer physically convincing and seamless. Rhinestones remain naturally attached to the body surface and follow the body correctly afterward.

Do not create random rhinestones elsewhere. Do not let them float. Do not change their appearance after transfer.
```

## Technical Specifications

- **Effect window:** 00:03.48 to 00:05.14
- **Path rule:** Rhinestones appear only behind the phone's observed travel path
- **End state:** Transferred stones remain surface-attached and body-tracked
- **Audio:** Preserve original audio unchanged

## Negative Prompt

```text
changed subject, altered face, altered skin, altered hair, altered clothing, changed hands, changed phone, changed background, changed lighting, camera changes, new people, new objects, text, graphics, rhinestones ahead of phone, random rhinestones, floating rhinestones, wrong transfer path, delayed transfer, altered rhinestone color, altered rhinestone density, rhinestones sliding off body, untracked rhinestones, CGI overlay
```
