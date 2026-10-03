# Main Menu Concept

## Creator direction

- The creator has supplied the *Fragment Away* logo artwork. Use that original image unchanged. Do not generate, imitate, or typeset a replacement. The attachment is not yet available in the repository workspace, so keep the logo slot blank until the original file can be added.
- Use the requested game fonts: Whatnot, Dudu Calligraphy, Helvetihand, and Faraco Hand. Keep their roles and licensing notes in `assets/fonts/NOTICE.md`.
- Make the menu feel like opening a personal journal, not a conventional game dashboard.
- Show Mara sitting in a field of grass at golden sunset, with flowers and grass moving in a changing breeze.

## Current background reference

[Main menu golden field concept](assets/backgrounds/main-menu-golden-field.png)

The selected illustration places Mara on the right and leaves open sky and field to the left for the creator's logo and menu. It follows Mara's supplied design: dark bob, warm tan skin, red jacket, lavender shirt, teal-blue trousers, and red high-top sneakers. This is the static key art beneath the layered motion.

## Menu treatment

The root-level HTML preview in `main-menu-preview.html` places the handwritten menu text directly over the field. There is no paper, card, or opaque panel behind it. The logo area remains blank only until the creator-supplied image is added to the repository. The button labels and tagline are temporary.

The visible menu uses **Dudu Calligraphy** by Adderou from the local file `assets/fonts/Dudu_Calligraphy.ttf`, served by the root preview. The `Faraco Hand`, `Helvetihand`, and `Whatnot` CSS family roles are preserved for notes, functional UI, and episode or chapter lettering. Font origins, attribution, and unresolved game embedding terms are recorded in `assets/fonts/NOTICE.md`.

The text color is a slightly warmer umber and clay tone, with a soft cream shadow for readability over the sunset. Keep the words directly on the artwork. Do not add a page or panel behind them.

## Wind and movement

The current background loop is [golden-field-wind-8s.mp4](assets/videos/golden-field-wind-8s.mp4), an eight-second clip that loops. The earlier [main-menu-wind-6s.mp4](assets/videos/main-menu-wind-6s.mp4) remains as a smaller draft. The root preview adds a synchronized eight-second inline SVG and CSS layer: more grass and flower tufts sway across the foreground, Mara's loose bob strands move gently, and she blinks twice per loop. The layer follows the video crop at different viewport sizes and is hidden when reduced motion is requested.

The preview keeps the video and SVG motion separate rather than flattening them into a replacement MP4. This preserves independent layers for the game. For production, use separate hair and eyelid layers or sprite frames plus selected foreground grass and flowers, vary slow wind gusts, and keep the distant sunset still. Do not warp the whole background or Mara to fake wind.

Run the preview with `python3 main-menu-preview-server.py`. It stays at the repository root. This is a visual concept, not a decision to replace Phaser or the planned optional HTML/CSS overlays.
