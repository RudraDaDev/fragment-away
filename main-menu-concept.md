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

The root-level HTML preview in `main-menu-preview.html` places the menu on a warm paper panel with faint ruled lines, an ink-like margin, and a blank logo area. The button labels are temporary. The preview uses Caveat as a handwriting-font sample with cursive fallbacks. The final font and exact menu labels remain open.

Keep the paper translucent enough that the sunset still feels present. Use dark, readable ink, generous spacing, and restrained decoration. The journal styling should feel personal and handmade, not distressed or horror-themed.

## Wind and movement

The background illustration already suggests a breeze, but its grass and flowers are painted into one image. For the game, keep Mara and the distant sunset still. Put selected foreground grass blades and flower stems on separate layers, add a little parallax, and animate their lean with wind that varies in direction and strength. Use slow gusts rather than a rigid loop. Do not warp the whole background or Mara to fake wind. Respect reduced-motion settings.

The standalone preview demonstrates this with a small SVG foreground and variable CSS transitions. Run it with `python3 main-menu-preview-server.py`. The preview server exposes only the mockup and its background image. This is a visual concept, not a decision to replace Phaser or the planned optional HTML/CSS overlays.
