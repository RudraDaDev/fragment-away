# Fragment Away Project Memory

> Persistent continuity notes. Last updated: 2026-10-04.

## Source of truth

- `fullgame.md` now reflects the creator's detailed project brief supplied on 2026-10-03.
- This brief supersedes the earlier speculative draft about Ari, a lighthouse archipelago, and collectible memories. **That premise is not part of the current project.**
- Keep creator-provided facts separate from design suggestions. Anything marked potential, recommended, or open in `fullgame.md` is not locked canon.

## Workflow preference

- After each completed change, record relevant continuity notes here, then commit and push the work to `arena/01a100cc-fragment-away`.
- Never commit or push this project work to `main`.

## Project identity

- **Title:** *Fragment Away*
- **Developer / studio:** BrokenHour Studio
- **Genre:** 2D narrative adventure / psychological drama
- **Format and tone:** Cinematic, atmospheric, melancholic indie narrative; branching choices and multiple outcomes; phone/UI and environmental storytelling; original OST.
- **Distinct from:** *SmallHours*, a procedural narrative life-sim. Do not merge the two projects' formats or creative identities.

## Canonical story facts

- **Mara Bennett** is a young adult college student raised under a “perfect kid” identity: smart, responsible, polite, successful, well-behaved, and never disappointing. She leaves, but physical distance does not give her an identity automatically.
- Mara's current visual reference comes from the creator's concept art: short dark bob, warm tan skin, red jacket, lavender shirt, teal-blue trousers, and red high-top sneakers. Her faces should include simple, natural, readable eyes, brows, nose, and mouth.
- The story begins in **Morrow**, a fictional, contemporary college town and Mara's hometown. Its name suggests the uncertain tomorrow ahead. The town is named; region, landmarks, and Episode 2 destination are still open.
- Mara is human and contradictory: uncertain, angry, impulsive, awkward, funny, emotional, sometimes selfish, sometimes kind. Her problem is lack of room to discover herself, not a hidden flaw to expose.
- **David Bennett**, her father, is achievement-focused and believes pressure prepares Mara for adulthood. **Claire Bennett**, her mother, cares about Mara while worrying about stability, reputation, and doing the “right” thing. Their love can coexist with harmful expectations; do not make them cartoonishly abusive by default.
- **Ethan Mercer** is a world-famous indie/alternative musician with a thoughtful, empathetic public image and private emotional disconnection. He is fascinated by the sound and musical qualities of Mara's voice notes. His interest may be genuine but is unhealthy; he gradually manipulates her and undermines her best-friend relationship.
- Mara's best friend (name/details still open) gives her room to be imperfect and spontaneous. The friend disappears near the ending. The reveal is that **Ethan kidnapped them**; this should recontextualize earlier clues and dialogue.
- The player should have reason to trust Ethan at first. Suspicion grows gradually through inconsistencies; the intended realization is that the player may have trusted him too.
- **Central theme:** identity and the freedom to define oneself. No single “correct” version of Mara is prescribed.

## Experience and craft

- **Framework:** Phaser is chosen for the game. HTML and CSS DOM overlays are optional for phone, dialogue, or settings UI when they improve readability or accessibility. Version, JavaScript or TypeScript, build tooling, and the exact division between Phaser UI and DOM overlays remain undecided.
- **Gameplay visual style proposal:** hand-drawn 2D side-on walk-and-interact, mostly fixed camera indoors and short scrolling streets, with no 3D, combat, jumping, or platforming. This is a recommendation for the beginner-friendly prototype, not yet user-approved.
- **Drawing style proposal:** soft hand-painted graphic-novel illustration with simplified natural proportions, clear shapes, selective pencil linework, muted colors, and light brush texture. Awaiting user approval.
- **Main menu direction, creator-specified:** the creator supplied the *Fragment Away* logo at `fragment-away-logo.png`. Use the original transparent image unchanged and do not generate a substitute. The root preview now displays it above the menu. Keep the text panel-free over the golden-hour field. The current background is the looping eight-second MP4 `assets/videos/golden-field-wind-8s.mp4`; the earlier six-second `main-menu-wind-6s.mp4` remains as a smaller draft. The preview layers a matching eight-second inline SVG/CSS loop over the video for broader grass and flower sway, moving bob strands, and two blinks. Menu options use the local Dudu Calligraphy TTF at `assets/fonts/Dudu_Calligraphy.ttf`. The text color is warmer umber and clay. The requested game fonts are Whatnot, Dudu Calligraphy, Helvetihand, and Faraco Hand. Check `assets/fonts/NOTICE.md` for source and license notes, especially the unresolved Whatnot edition and Faraco Hand archive terms. See `main-menu-concept.md` for the design. This remains a visual mockup rather than a locked game architecture.
- `episode-1-art-list.md` is the Episode 1 drawing checklist and links to generated concept art. `episode-1-drawing-prompts.md` contains detailed prompts for backgrounds, characters, props, and cutscene images. Eight first-pass background references and ten character concept images remain preserved in `assets/backgrounds/` and `assets/characters/episode-1/`.
- A visual refinement/export pass now lives in `assets/production/`: nine 1920 by 1080 environment and main-menu still candidates, plus eight 1024 by 1024 transparent sprite canvases with a shared foot anchor. Mara idle is the only newly re-rendered sprite. Mara walk, recording, and the five supporting-character sprites are cleaned and normalized exports from the previous prototype cutouts, not fully polished new illustrations. Mara seated with phone and Mara bag-at-door are still concepts rather than production sprites. See `assets/production/README.md` and `assets/production/manifest.json` for exact status and outstanding review items.
- The image-generation service hit its per-turn limit after the nine backgrounds and Mara idle were generated. Do not say the full art set is release-ready. The next art pass should re-render the other seven sprite poses and create game-ready seated-phone and bag-at-door art. Original concept images remain preserved. The supplied logo and `assets/videos/golden-field-wind-8s.mp4` were left unchanged.
- Target balance is approximately 70% narrative / 30% gameplay. It should include a small explorable 2D world, dialogue and choices, relationships, object interaction, investigation, revisiting locations, and consequences, not be a pure visual novel.
- Mara's phone supports messages, voice notes, contacts, photos, conversations, notifications, and possibly browser/social-style information. Voice notes are especially important.
- Visual direction: illustrated/hand-drawn 2D, stylized realistic proportions, muted and atmospheric, cinematic but not hyper-realistic, pixel-art-dependent, anime, or over-detailed.
- The visual language evolves: controlled early compositions; more variety after leaving; Ethan's polished, almost-too-perfect spaces; later subtle fragmentation. Avoid generic glitch-horror effects.
- Regular gameplay uses limited animation; major scenes receive more. Current estimate: roughly 5 to 10 key cinematic scenes (not a locked count).
- OST must be original. “Flaws” by Daughter is a mood reference for one scene, not a confirmed track or permission to use it. A recurring melody can change from warm and complete to sparse, fragmented, then reharmonized.
- The creator's five-episode outline is the current proposed structure, not a locked production plan. **PERFECT** is the free first episode, targets at least 30 minutes, and ends with Mara leaving Morrow. **AWAY** explores freedom and loneliness, builds the friendship, introduces Ethan, and ends with him privately replaying her voice note. **SOMEONE** makes the player care about the friend, deepens Ethan's influence, and ends with the disappearance and Mara realizing something is wrong. **FRAGMENTS** lets the player revisit phone and environment clues, suspect Ethan before Mara, and ends with proof of the kidnapping and Mara confronting him. **WHO AM I?** resolves the friend's situation and centers Mara's agency, boundaries, and possible endings.
- Episode design guidance: give each episode an emotional turn, playable exploration/investigation, phone/environment storytelling, and a strong closing beat. Make the free first episode emotionally complete as an introduction but end on the specific hook “I don't know where I'm going. I just know I can't stay.” Let clues reinforce one another rather than hinge on one obscure find. Keep the friend's agency visible; do not gate their safety behind a hidden “good choices” score.
- A provisional Episode 1 playable-screenplay draft is in `episode-1-perfect.md`. It targets 32 to 36 minutes, with a 30-minute minimum goal and scene-by-scene estimates. It has three key cutscenes: “The Smile,” “The Stack,” and “Out the Door.” The OST direction uses room tone, felt piano, muted guitar harmonics, Mara's recorded town sounds, and an unresolved departure motif. Morrow is the chosen town name; sound recording as Mara's hobby and “Jules” as the classmate name are still draft choices. Small choices reconverge and do not determine whether Mara leaves.
- Writing preference: avoid long dash punctuation in story scripts. Use commas, colons, or periods instead.

## Decisions intentionally open

- Confirm or change Mara's private interest (the script draft uses sound recording), decide whether the player chooses it, and confirm/replace the classmate placeholder name “Jules.”
- Best friend's name, identity, and post-reveal resolution.
- Morrow's region, landmarks, and layout; the exact location where Mara wakes at the start of Episode 2.
- Ethan's backstory and the precise progression/mechanics of his manipulation.
- Investigation sequence after the disappearance and how the kidnapping is discovered.
- Final choice/ending set and how branching is tracked. Candidate themes include self-definition, bittersweet freedom, reconnection, repeating learned behavior, ambiguity, and identity-shaped outcomes. Do not reduce endings to a good/bad morality score.
- Confirm the side-on walk-and-interact proposal or choose another 2D view; decide controls and the amount of world scrolling.
- Phaser version, JavaScript or TypeScript, build tooling, target platform, scope, production schedule, and UI architecture, including where HTML/CSS overlays are useful.
- Exact camera orientation for the noted low “Southeast/ground-to-head” cinematic angle.
- Whether to make the possible prequel *Before Away*; it is not required for the main game.

## Next useful steps

1. Continue the Episode 1 production-art pass: re-render Mara walk and recording plus Claire, David, Jules, Professor, and Aunt as clean, consistent transparent sprites; create isolated Mara seated-phone and bag-at-door poses. The current candidates and exact remaining issues are listed in `assets/production/README.md`.
2. Review the nine polished 1920 by 1080 environment/key-art candidates in `assets/production/backgrounds/`; blank or replace pseudo-writing on papers and certificates before calling them final, then validate composition and sprite scale in a Phaser scene.
3. Review the root-level menu preview with the creator-supplied logo and Dudu Calligraphy options. Menu labels remain temporary. Once the Phaser project is scaffolded, adapt the design and unchanged eight-second background video to the game.
3. Review the Episode 1 draft together: adjust the dialogue voice and approve/change Mara's hobby, Morrow's atmosphere, and the classmate placeholder.
4. Name the best friend and define their personality and friendship with Mara beyond the later disappearance.
5. Build Episode 4's fair clue trail and decide how the kidnapping is uncovered without a single missable clue.
6. Decide what player-choice patterns meaningfully shape Mara, then design ending conditions without a simple morality meter.
7. Confirm the side-on gameplay proposal, choose Phaser version and JavaScript or TypeScript, then graybox Mara's bedroom using `episode-1-art-list.md` and prototype movement, hotspots, dialogue, and a phone overlay.
