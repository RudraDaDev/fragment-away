# Main Menu Concept

## Creator direction

- The creator will make the *Fragment Away* logo. Leave its place blank. Do not generate, imitate, or typeset a replacement logo.
- Use the requested game fonts: Whatnot, Dudu Calligraphy, HelvetiHand, and Faraco Hand. Keep their roles and licensing notes in `assets/fonts/NOTICE.md`.
- Make the menu feel like opening a personal journal, not a conventional game dashboard.
- Show Mara sitting in a field of grass at golden sunset, with flowers and grass moving in a changing breeze.

## Current background reference

[Main menu golden field concept](assets/backgrounds/main-menu-golden-field.png)

The selected illustration places Mara on the right and leaves open sky and field to the left for the creator's logo and menu. It follows Mara's supplied design: dark bob, warm tan skin, red jacket, lavender shirt, teal-blue trousers, and red high-top sneakers. This is the static key art beneath the layered motion.

## Menu treatment

The root-level HTML preview in `main-menu-preview.html` places the handwritten menu text directly over the field. There is no paper, card, or opaque panel behind it. The logo area remains blank for the creator's artwork. The button labels and tagline are temporary.

The visible menu uses **Dudu Calligraphy** by Adderou. The `Faraco Hand`, `Helvetihand`, and `Whatnot` CSS family roles are preserved for notes, functional UI, and episode or chapter lettering. The preview falls back when a locally installed font is not available. Font origins, attribution, and unresolved game embedding terms are recorded in `assets/fonts/NOTICE.md`.

The text color is a slightly warmer umber and clay tone, with a soft cream shadow for readability over the sunset. Keep the words directly on the artwork. Do not add a page or panel behind them.

## Wind and movement

The six-second background layer is [main-menu-wind-6s.mp4](assets/videos/main-menu-wind-6s.mp4). It already moves selected foreground grass and flower stems over the still illustration. The root preview adds a synchronized six-second inline SVG and CSS layer: more grass and flower tufts sway across the foreground, Mara's loose bob strands move gently, and she blinks twice per loop. The layer follows the video crop at different viewport sizes and is hidden when reduced motion is requested.

The preview keeps the video and SVG motion separate rather than flattening them into a replacement MP4. This preserves independent layers for the game. For production, use separate hair and eyelid layers or sprite frames plus selected foreground grass and flowers, vary slow wind gusts, and keep the distant sunset still. Do not warp the whole background or Mara to fake wind.

Run the preview with `python3 main-menu-preview-server.py`. It stays at the repository root. This is a visual concept, not a decision to replace Phaser or the planned optional HTML/CSS overlays.
