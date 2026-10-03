# Fragment Away: Episode 1 Art List

> A beginner-friendly drawing plan for the free episode. The list follows the proposed hand-drawn 2D side-view style. It is a guide, not a requirement to finish all art before making a prototype. Ready-to-copy prompts for each location, character, and cutscene are in [episode-1-drawing-prompts.md](episode-1-drawing-prompts.md).

## Recommended drawing style

Use **soft, hand-painted graphic-novel illustration**. Think of a quiet contemporary indie film translated into simple 2D drawings. Keep the people and locations recognizable, but do not chase realism or tiny detail.

- **Shapes:** Clear silhouettes and simple, readable forms. Use natural adult proportions with gently stylized faces and restrained expressions.
- **Linework:** Selective pencil or ink lines. Avoid thick black outlines around everything.
- **Color and texture:** Mostly flat color shapes with one broad shadow layer and a little paper or brush texture. Avoid noisy texture that makes the scenes hard to read.
- **Detail level:** Put the most detail on faces, hands, and objects the player can inspect. Simplify items in the distance.
- **Palette:** Morrow can use warm cream, soft gray, dusty blue, muted green, and a small amber accent. At night, reuse the same painting with a cool blue-green light overlay.
- **Composition:** Mara's early rooms are tidy and centered. Jules's moment can feel slightly looser and warmer. Save more dramatic lighting and framing for the cutscenes.

Do not make it pixel art, anime, 3D, photorealistic, or extremely detailed. Still backgrounds with a few animated layers are enough. Indoors, use a mostly fixed camera and one shallow floor area where Mara can walk between interactable objects. Streets can scroll a short distance from one screen to the next. Animate only what helps the story.

**Style prompt for a first reference sketch:**

> A contemporary psychological indie drama as a hand-painted 2D graphic-novel illustration. Natural adult proportions, simple readable faces, clean large shapes, selective pencil linework, muted cream, dusty blue, sage green, soft brush texture, cinematic but gentle lighting. Quiet and melancholic, not horror. No pixel art, anime, 3D, or photorealism.

A practical first artboard is **16:9 at 1920 by 1080 pixels**. This is a working size, not a final platform requirement. Keep faces and important objects away from the extreme edges so the scene can still work on a smaller window.

For each location, make only a few layers:

1. **Background:** Walls, windows, buildings, sky, and large furniture.
2. **Playable layer:** Floor, tables, doors, and other objects Mara walks up to.
3. **Foreground:** One or two near-camera shapes, such as a desk edge or plant, for subtle depth.
4. **Separate interactables:** Only draw these separately when they need a highlight, animation, or state change. Most hotspot hitboxes are invisible and do not need art.

## Episode 1 backgrounds

Seven reusable locations are enough for the first episode. Lighting and prop changes can turn one background into several scenes.

### 1. Mara's bedroom

**Reuse for:** Morning routine, the mask moment, phone messages, searching, and packing.

Draw one detailed base room, then reuse it with a warm morning light and a cooler night tint. Do not paint a separate room for every scene.

Include:

- Bed, desk, chair, window, bedroom door, and a clear path for Mara to walk.
- A neat calendar, study sheet, certificates, family photo, and packed college bag.
- A small phone with a sound-recorder app. Keep the screen separate if it will be shown close-up.
- A few personal details that feel like Mara's, not another person's idea of success.

Useful interactive hotspots: calendar, certificate, family photo, study sheet, bag, window, and recording folder. The hotspot outlines can be drawn in Phaser or HTML/CSS. They do not need to be painted into the background.

### 2. Kitchen and dining area

**Reuse for:** Breakfast and dinner with the aunt.

Draw one family eating area that can be dressed for both times of day. Use the same camera angle and swap a small number of props.

- **Morning props:** Coffee, lunch container, study sheet, jacket.
- **Evening props:** Plates, water jug, serving dish, and a fourth place setting.
- Keep the room warm and cared for, but arranged neatly enough to feel controlled.

### 3. Home hallway and front door

**Reuse for:** Walking between the bedroom and kitchen, plus Mara's departure.

Draw a straight, tidy hallway with a few family pictures, a small table or shoe rack, and a clearly visible front door. The centered hallway composition can echo the controlled look of Mara's bedroom. Make one night-lit version with a porch light or street light; use a color overlay rather than repainting everything.

### 4. Morrow street route

**Reuse for:** The morning trip to college, the trip home, and the final glimpse of town at night.

Do not draw an entire town map. Make a short strip or two connected screens with:

- A row of ordinary houses.
- A bus stop and route timetable.
- A crosswalk with a signal.
- One small shop or bakery.
- The college visible in the distance.

Reuse the same art for morning and afternoon by changing the lighting and a few background details. A night version can be a darker color grade with a few lit windows.

### 5. College hallway

**Reuse for:** Arrival, the squeaking door, and walking to class.

Draw one long corridor with classroom doors, a noticeboard, a bench, and an identifiable squeaky door. Keep the hallway simple. Put posters and schedules on separate layers if they contain readable text.

### 6. Seminar classroom

Draw rows of chairs, a whiteboard or projector screen, the Professor's desk, and a clear speaking area. Keep the board content vague until the course subject is chosen. The same room can support the seminar choice and the Professor's conversation afterward.

### 7. College common room

Draw a small, relaxed room with a couch, a table, a window, and a few flyers or student belongings. It should feel less formal than the classroom, but not like a magical safe space. This is the backdrop for Mara and Jules sharing a small, ordinary laugh.

## Characters and animation

Start with simple transparent character art over the background. You do not need a full animation set for everyone.

### Mara

First pass:

- One side-view standing pose.
- A short walk cycle, around four to six drawings if using frame animation.
- One phone or recorder pose.
- One inspect or reach pose.
- One sitting pose for the bedroom.
- One bag-carrying pose for the final scene.

Some poses can be made by swapping the arm or phone layer instead of redrawing the whole character. Keep her proportions and clothing consistent across all scenes.

### Other characters

For Claire, David, Jules, the Professor, and the aunt, begin with one standing or seated pose and one simple gesture each. A blink, head turn, hand movement, or change of expression can carry most dialogue. Save full animation for key scenes.

If character animation is difficult, use in-world portraits for dialogue and keep the bodies still. Try not to mix several different presentation styles in one scene.

## Cutscene art to prioritize

Reuse the backgrounds above. The three Episode 1 cutscenes mainly need new poses and careful framing, not entirely new locations.

1. **The Smile:** Family dinner pose, Mara smiling, Mara entering the hallway, then a close view after the bedroom door shuts.
2. **The Stack:** Phone close-up with message notifications, Mara's hand turning it face-down, and the room after the sound stops.
3. **Out the Door:** Mara with her bag, a hallway view, the front door opening, and Mara outside in Morrow at night.

These can be built from a few illustrated poses, slow camera pans, close-ups, fades, and limited animation. Do not animate every frame. The door, hand, eyes, and posture are the important movements.

## UI and props

The phone, dialogue choices, and message history can be made as HTML/CSS overlays above the Phaser canvas. If you use overlays, draw only the art that belongs inside them:

- A simple wallpaper or lock-screen image.
- Small contact avatars, if needed.
- A few app icons and notification symbols.
- Any photo or voice-note waveform that matters to a clue.

The message text itself should be real text, not part of a painted image. That makes it easier to change, scale, translate, and read. Keep the game world and character movement in Phaser.

## Best order to draw

1. **Rough bedroom thumbnail:** Test the camera, Mara's scale, and where the hotspots go.
2. **Bedroom background and Mara placeholder:** Make a basic Phaser scene before polishing the art.
3. **Kitchen/dining room:** Reuse it for morning and evening.
4. **Morrow street and bus stop:** Make a short route, not a full map.
5. **College hallway, classroom, and common room:** Keep the architecture simple and reuse colors and props.
6. **Character poses:** Add Mara first, then the rest of the cast.
7. **Cutscene poses and lighting variants:** Finish these after the playable scenes are readable.

Draw rough shapes first. If Mara's route and interactions work with placeholders, then spend time polishing the paintings. The first goal is a small playable episode, not a complete art portfolio.
