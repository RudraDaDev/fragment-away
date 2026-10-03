# Main Menu Concept

## Creator direction

- The creator will make the *Fragment Away* logo. Leave its place blank. Do not generate, imitate, or typeset a replacement logo.
- Use a handwriting-style font for the menu labels and journal details.
- Make the menu feel like opening a personal journal, not a conventional game dashboard.
- Show Mara sitting in a field of grass at golden sunset, with flowers and grass moving in a changing breeze.

## Current background reference

[Main menu golden field concept](assets/backgrounds/main-menu-golden-field.png)

The selected illustration places Mara on the right and leaves open sky and field to the left for the creator's logo and menu. It follows Mara's supplied design: dark bob, warm tan skin, red jacket, lavender shirt, teal-blue trousers, and red high-top sneakers. This is a static concept image, not a layered animation asset.

## Menu treatment

The root-level HTML preview in `main-menu-preview.html` places the handwritten menu text directly over the field. There is no paper, card, or opaque panel behind it. The logo area remains blank for the creator's artwork. The button labels and tagline are temporary.

The menu uses **Dudu Calligraphy** by Adderou, from the [DaFont page](https://www.dafont.com/dudu-calligraphy.font). The preview requests the matching TTF from [FontRepo](https://www.fontrepo.com/font/34835/dudu-calligraphy.ttf), which lists the font as Creative Commons Attribution 4.0. The browser needs network access to load that remote font. Keep the author attribution, and bundle a local copy for a production release after confirming the license details.

Use a soft text shadow for readability over the bright sunset, not a panel behind the text. The journal quality should come from the handwritten type, spacing, and gentle hand-drawn details.

## Wind and movement

The six-second background loop is [main-menu-wind-6s.mp4](assets/videos/main-menu-wind-6s.mp4). It layers swaying foreground grass and flower stems over the still concept illustration. The preview loops the clip behind the menu text and respects reduced-motion settings.

For the game, keep Mara and the distant sunset still. Put selected foreground grass blades and flower stems on separate layers, add a little parallax, and vary the direction and strength of slow wind gusts. Do not warp the whole background or Mara to fake wind.

Run the preview with `python3 main-menu-preview-server.py`. The preview server exposes only the HTML, background image, and six-second video. This is a visual concept, not a decision to replace Phaser or the planned optional HTML/CSS overlays.
