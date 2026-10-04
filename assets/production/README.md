# Episode 1 visual export set

This folder contains the current polished export pass for the main-menu still and Episode 1 environments, plus standardized transparent character sprite exports. The original reference art remains unchanged under `assets/backgrounds/` and `assets/characters/episode-1/`.

## Backgrounds

`backgrounds/` contains nine 1920 by 1080 PNGs: the golden-field still, bedroom day and night, Bennett home hallway, kitchen morning, Morrow street morning, college hallway, seminar room, and common room. They are intended as static in-game scene backgrounds or key-art candidates. They are flattened images, not layered source paintings.

## Cutscene keyframes

`keyframes/` contains 1920 by 1080 exports of Mara with her phone on the bed and Mara pausing at the front door. These are useful composition and staging candidates, but they are flattened scene illustrations, not transparent sprites or layered cutscenes.

## Character sprites

`sprites/` contains eight 1024 by 1024 transparent PNGs. Each character is centered on a shared bottom anchor near y=1008 so a Phaser scene can use a consistent foot baseline.

- `mara-idle.png` is the newly refined Mara phone pose, with the generated checkerboard matte removed.
- `mara-walk.png`, `mara-recording.png`, `claire.png`, `david.png`, `jules.png`, `professor.png`, and `aunt.png` are cleaned, speck-reduced, high-quality resampled exports of the existing transparent prototypes. They still need their own full illustration polish pass before release.

## Not release-final yet

This is a meaningful quality and export pass, not a claim that the entire game's art is approved for release. Before calling the set final:

1. Give the seven carried-over sprites the same illustration polish as Mara's new idle pose, then check identity, hands, clothing, and edge mattes at actual game scale.
2. The seated-phone and bag-at-the-door concepts are exported as flattened keyframe candidates in `keyframes/`. They still need a final art pass and, if the scenes require movement, separate character and background layers.
3. Replace any pseudo-writing on papers, certificates, notices, and phone screens with blank painted marks or real runtime UI text.
4. Test the backgrounds and foot anchors in the Phaser camera. Split props into layers only where an object must animate, change state, or move in front of Mara.
5. Check that the new golden-field still is an acceptable static companion to the existing loop before using it as a poster. The eight-second video itself has not been changed.

The creator-supplied logo at `fragment-away-logo.png` and `assets/videos/golden-field-wind-8s.mp4` are intentionally excluded and unchanged.
