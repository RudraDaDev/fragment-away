# FRAGMENT AWAY
## Episode 1: PERFECT

### First Script Draft

> **Status:** Draft for discussion, not final canon. This is an engine-agnostic playable screenplay with scene direction, player actions, dialogue, phone text, and audio and visual notes. Episode 1 is intended to be free and must run for at least 30 minutes on a normal first playthrough.

## Runtime target

- **Minimum first-play runtime:** 30 minutes.
- **Expected first-play runtime:** 32 to 36 minutes, depending on how much the player inspects and listens to.
- **Approximate balance:** 22 to 25 minutes of dialogue and cinematic story, plus 9 to 11 minutes of player-controlled exploration, phone interactions, and choices.
- The time should come from meaningful interactions and paced scenes, not forced waiting or repeated dialogue. Treat these numbers as a design target until a first-playtest confirms them. If a normal first playthrough lands under 30 minutes, add character moments or playable material rather than padding.

| Scene | Target time |
|---|---:|
| 1. Morning, on schedule | 3 to 4 min |
| 2. Breakfast | 3 to 4 min |
| 3. Across Morrow | 4 to 5 min |
| 4. A small sound | 4 to 5 min |
| 5. Good work | 4 to 5 min |
| 6. The way home | 2 to 3 min |
| 7. Dinner | 4 to 5 min |
| 8. The door closes | 4 to 5 min |
| 9. How do I leave? | 4 to 5 min |

## Temporary choices for this draft

- **Setting:** Present day in **Morrow**, a fictional college town and Mara's hometown. Episode 1 moves between her family home, streets around town, and college. The region, architecture, and exact landmarks remain open.
- **Mara's private interest:** She records little everyday sounds on her phone. It is not professional and does not need to become a career. This connects to the game's voice and audio themes, but can be changed.
- **Classmate:** “Jules” is a placeholder name for a brief warm connection, not necessarily the best friend from later episodes.
- **Choices:** Small choices change Mara's words, expression, or later callbacks. They do not decide whether she leaves.

## Cast in this episode

- **Mara Bennett:** College student and player character.
- **Claire Bennett:** Mara's mother.
- **David Bennett:** Mara's father.
- **Jules:** Classmate, working name.
- **Professor:** Appears briefly at college and through a message.
- **Aunt:** Appears at dinner. Name not chosen.

## Script conventions

- **PLAY:** The player moves Mara or interacts with the space.
- **CHOICE:** A dialogue or action choice. Unless noted, branches return to the main scene.
- **PHONE:** An on-screen phone interaction or notification.
- **VISUAL / SOUND:** Direction for framing, animation, ambience, and music.

**Implementation note:** The game will be built in Phaser. Keep world movement, cameras, and environmental interactions in Phaser. Phone or dialogue panels can use HTML and CSS overlays if that is useful for responsive layout or readable text. The UI architecture is still open.

## Episode 1 cutscenes

Episode 1 has three key cinematic scenes. They are included in the runtime estimates above. Regular exploration stays lightly animated, so these moments can receive more detailed staging without requiring full animation throughout the episode.

| Cutscene | Approximate length | Dramatic purpose |
|---|---:|---|
| **The Smile** | 45 to 60 sec | Show Mara's public smile disappear once she is alone. |
| **The Stack** | 45 to 60 sec | Turn ordinary messages into an overwhelming pattern without using horror effects. |
| **Out the Door** | 90 to 120 sec | Make Mara's choice to leave the free episode's emotional cliffhanger. |

### OST direction for Episode 1

The score is original and intimate. It should feel like melancholic indie music heard from inside Mara's day, not a constant emotional instruction telling the player what to feel.

- **Palette:** Felt piano, muted electric guitar harmonics, soft low strings or synth, and real-feeling room and town ambience. Keep percussion rare in Episode 1.
- **Mara's motif:** A short, simple three or four note idea. It first appears incomplete and quiet, then briefly warms when Mara has an unguarded moment, then becomes sparse again. Do not lock a key or exact notes until the composer tests it against the game.
- **Sound recordings:** Let the radiator, crosswalk, bus, and kettle recordings sometimes sit inside the score. Keep them recognizable as sounds Mara chose to keep.
- **Music and silence:** Use room tone as part of the score. The door closing and the phone turning face-down should create real silence. Do not use glitch effects or aggressive stingers.
- **No licensed temp song is required for this episode.** Any reference track is mood only. The released music must be original or properly licensed.

| Cue | Scene | Direction |
|---|---|---|
| **Room Tone** | Bedroom, morning | One soft piano note and quiet room ambience. Let Mara's first recording be louder than the score. |
| **Morrow Morning** | Walk to college | Muted guitar harmonics join the morning recording. Keep the rhythm open and unhurried. |
| **A Small Sound** | Jules and Mara | Add one warm layer. Let the motif resolve briefly, but keep it modest rather than romantic or triumphant. |
| **The List** | Dinner and messages | Return to the morning motif in shorter phrases. A restrained pulse can echo the growing notification rhythm. Stop before it becomes suspense-horror music. |
| **Leaving** | Search and departure | Strip the motif back to a few notes. Let Mara's recorded sounds join it. Hold an unresolved tone through her voiceover, then cut to silence before the title card. |

The cutscene timings and cues can change during implementation. Playtest the full episode for pacing and confirm the runtime before promising a precise duration.

## Scene 1: Morning, on schedule

**EXT. MORROW, EARLY MORNING**

A modest college town wakes up. A bus eases to a stop, a shop lifts its shutter, and the college buildings sit beyond a row of houses. Keep it grounded and familiar. Morrow should feel like a place people live, not a gothic postcard.

**INT. MARA'S BEDROOM, MORNING**

**VISUAL:** A neat room. The camera frames Mara's desk almost symmetrically: books stacked by size, a calendar with blocks of color, a few certificates. At the edge of the desk, half-hidden beneath a notebook, is Mara's phone with its sound-recorder app open.

**SOUND:** Alarm. A soft original music motif begins, almost covered by room tone.

**PHONE, 7:04 AM**

- Exam: tomorrow
- Seminar: 9:00 AM
- Reminder: bring draft

**PLAY, 3 to 4 minutes:** Mara silences the alarm and explores her room before getting ready. The main path asks the player to get her ready, record one sound, choose what fills the room, and respond to Claire. Inspectable objects include her calendar, a certificate, her packed college bag, a family photo, and a small folder of sound recordings. Each gives one brief detail or animation. Nothing requires a long text explanation.

At the window, traffic hisses over wet pavement. A radiator clicks twice.

**INTERACTION, RECORD A SOUND**

Mara holds the phone still. The recording lasts a few seconds: radiator, distant traffic, then quiet.

**MARA** *(under her breath)*<br>
Again.

She plays it back. A small smile, almost involuntary.

**PHONE, NEW RECORDING**<br>
`Tuesday morning, 7:04`

**CHOICE, WHAT FILLS THE ROOM WHILE MARA GETS READY?**

1. **Her saved playlist:** A few bars of a fictional, soft instrumental track.
2. **Campus radio:** Indistinct voices and a weather report.
3. **Nothing:** Only the radiator and the house waking up.

The choice changes the room's sound, not the plot.

A text arrives.

**PHONE, CLAIRE**<br>
Coffee's ready. Come down when you're up?

**CHOICE, MARA REPLIES**

- “On my way.”
- “Two minutes.”
- Leave it unread for now.

Mara picks up her bag. Before leaving, she looks once at the sound-recording folder, then puts the phone away.

## Scene 2: Breakfast

**INT. BENNETT FAMILY KITCHEN, MORNING**

**VISUAL:** The kitchen is warm and orderly. A lunch container is already set beside Mara's bag. Claire has poured coffee. David is looking over a printed study sheet.

**CLAIRE**<br>
You're wearing that?

Mara glances down at her clothes.

**MARA**<br>
Good morning to you too.

Claire pauses, realizing how it sounded.

**CLAIRE**<br>
I meant the weather. It's going to rain. Take the other jacket.

She reaches for the jacket and sets it beside Mara. It is a caring gesture, but it still assumes Claire knows what Mara should wear.

**DAVID**<br>
Your exam is tomorrow, right?

**MARA**<br>
I know.

**DAVID**<br>
I know you know. Just checking.

He slides the study sheet across the table.

**DAVID**<br>
Chapter four's the part people usually miss.

**MARA**<br>
I'll look at it.

Claire sits across from her.

**CLAIRE**<br>
How are you holding up?

**CHOICE, MARA ANSWERS**

- **“I'm fine.”**<br>
  **MARA:** I'm fine.<br>
  **CLAIRE:** Good. You seem on top of things.
- **“I'm exhausted.”**<br>
  **MARA:** I'm exhausted.<br>
  **CLAIRE:** I know, honey. You've had a lot on. Just get through today, okay?
- **“Can we talk later?”**<br>
  **MARA:** Can we talk later?<br>
  **CLAIRE:** Of course. After your exam, if you want.

The responses reconverge. Claire puts a piece of toast on Mara's plate.

**CLAIRE**<br>
Your aunt is coming for dinner. She's been asking how college is going.

**MARA**<br>
Of course she has.

David looks up. Not angry, just alert to her tone.

**DAVID**<br>
She cares about you.

**MARA**<br>
I know.

A small pause. Claire reaches across and straightens the collar of Mara's jacket.

**CLAIRE**<br>
Text me when you get there?

**MARA**<br>
I will.

**CLAIRE**<br>
Love you.

**MARA**<br>
Love you too.

Mara leaves with the study sheet in her bag.

## Scene 3: Across Morrow

**EXT. MORROW, MORNING**

**PLAY, 4 to 5 minutes:** Mara makes her way from home to college. This is the first small explorable stretch. The player walks the main route through a few connected screens. Keep the map compact and legible, but let the town feel larger than the family home.

**CORE ROUTE BEATS:**

1. Pass the bus stop and inspect the timetable. It lists the campus route and routes beyond Morrow. Mara looks at it, then continues toward college.
2. Cross the main street. The signal has a short repeating tone. The player can record it or simply listen while traffic moves past.
3. Reach the college gates and check in by phone, as Claire asked.

**OPTIONAL STOPS:**

- A community board with tutoring notices, club announcements, and a missing-cat flyer.
- A bakery window where Mara can stop, look at the options, and decide whether anything sounds good.
- A small side street that offers a quieter route and different ambient sounds.

The route takes several minutes at normal movement speed. Optional stops add detail but are not required to understand the story. The bus and crosswalk sounds can join Mara's private recordings.

**PHONE, CLAIRE**<br>
Made it out the door?

**CHOICE, MARA REPLIES**

- “Yes. On my way.”
- “Almost there.”
- Send a photo of the rainy street instead of text.

Any response satisfies Claire's request. Her concern is real, but Mara is already reporting in.

As Mara reaches the college gates, the soundscape narrows. The street noise fades into the orderly rhythm of footsteps and a clock chime.

## Scene 4: A small sound

**INT. COLLEGE BUILDING, MORROW, LATE MORNING**

**VISUAL:** Long straight corridors, noticeboards in tidy rows, classroom doors with printed schedules. The compositions remain centered and orderly, echoing Mara's bedroom.

**PLAY:** The player crosses the corridor. Optional interactions include checking the exam room, reading an honors-program flyer, or inspecting a door that squeaks when it closes.

Mara stops at the door and opens the recorder app.

**JULES (O.S.)**<br>
Are you recording the door?

Mara turns. Jules, carrying a folder, looks amused rather than judgmental.

**MARA**<br>
It makes a weird sound.

**JULES**<br>
It sounds like a door.

**MARA**<br>
Wait until it closes.

Mara lets the door swing shut. It gives a low, almost musical groan.

Jules raises an eyebrow.

**JULES**<br>
Okay. It sounds like a haunted door.

**MARA**<br>
It's not haunted. It needs oil.

**JULES**<br>
You have a whole collection of things that sound like things?

**MARA**<br>
Kind of.

**JULES**<br>
That's strange.

A beat. Mara starts to put her phone away.

**JULES**<br>
I mean that in a good way.

**MARA**<br>
You can keep the compliment.

They laugh. The moment is small and easy. Mara's posture relaxes; the camera drifts slightly off its precise center.

**JULES**<br>
I've got five minutes before seminar. Show me your best one?

**CHOICE, WHICH RECORDING DOES MARA PLAY?**

- **The radiator:** A dry double click, followed by the quiet hum of the room.
- **The crosswalk:** A repeating chirp with traffic passing behind it.
- **The kettle:** A click, a brief hiss, then silence.

Jules listens without rushing her.

**JULES**<br>
I can hear why you kept that one.

**MARA**<br>
You can?

**JULES**<br>
No. But I can tell you like it.

Mara laughs. It is one of the warmest moments in the episode because Jules is interested without asking Mara to justify the sound or turn it into an achievement.

**JULES**<br>
Are you going to the common room after seminar?

**CHOICE, MARA ANSWERS**

- “Maybe. I have a lot to do.”
- “If you're going, sure.”
- “I don't know yet.”

Jules accepts any answer without pressing.

**JULES**<br>
Okay. See you around, then.

**MARA**<br>
See you.

Jules heads down the hall. Mara replays the recording once before following.

## Scene 5: Good work

**INT. COLLEGE CLASSROOM, DAY**

The seminar is ending. The Professor has asked the class to respond to a reading. The exact subject can be decided when Mara's course is developed; keep this question broad enough not to turn the scene into a lecture.

**PROFESSOR**<br>
What do you think the writer is leaving out?

A few students look down at their notes. Mara has an answer in the margin of her paper.

**CHOICE, MARA RESPONDS**

- **Give the polished answer:** She points to a detail in the reading and explains how it supports the writer's conclusion.
- **Offer a disagreement:** She says the conclusion is too neat and leaves out the people affected by it.
- **Admit she is unsure:** She says she cannot tell if the omission is deliberate or if she is reading too much into it.

Each response starts differently. In every version, the Professor listens and thanks her for being specific. The point is not that one answer is correct. The player chooses how much Mara shows of her own thinking in front of the room.

The bell or class-change sound cuts through the conversation. Students pack their bags. The Professor waits until the room is almost empty.

**PROFESSOR**<br>
Mara, do you have a second?

Mara stays.

**PROFESSOR**<br>
I read your paper. The argument is clear, and the last section is especially strong.

**MARA**<br>
Thank you.

**PROFESSOR**<br>
You should consider submitting it to the student journal. And the advanced seminar next term.

**MARA**<br>
I haven't really thought about next term yet.

**PROFESSOR**<br>
You don't have to decide today. But you should think about it. You have a lot of potential.

**MARA**<br>
Right.

**PROFESSOR**<br>
I'm not trying to add pressure. I just don't want you to miss an opportunity.

**MARA**<br>
I know.

The Professor gives her a kind, encouraging smile. Mara smiles back, on cue.

**PHONE, PROFESSOR**<br>
Your work was excellent. Keep it up. The journal deadline is Friday if you decide to submit.

Mara looks at the message for a moment, then locks the phone.

Jules waits near the classroom door, rolling a pen between their fingers.

**JULES**<br>
I was going to ask if you wanted to sit for a few minutes, but you looked busy being excellent.

**MARA**<br>
I don't think anyone's ever looked busy being excellent.

**JULES**<br>
You'd be surprised. You have the face.

**MARA**<br>
What face?

**JULES**<br>
The one where you're already thinking about the next thing.

Mara starts to answer, then stops. Jules notices and immediately softens.

**JULES**<br>
Sorry. That sounded more serious than I meant it.

**CHOICE, MARA RESPONDS**

- **“It's fine.”** Mara makes the familiar, reassuring smile.
- **“Maybe I am.”** Mara admits it, then glances at her phone.
- **“Let's sit for five minutes.”** Mara lets herself pause.

The branches reconverge in the common room. Jules is there for a few minutes, not trying to fix Mara or pull a confession out of her.

**JULES**<br>
I like the recordings, by the way. The hallway sounds less like a hallway when you play it back.

**MARA**<br>
That's a lot to ask of a hallway.

**JULES**<br>
It can handle it.

Mara laughs. A small moment of connection, with no big promise attached.

**JULES**<br>
See you around?

**MARA**<br>
Yeah. See you.

Jules leaves first. Mara looks at the Professor's message once more, then puts the phone away.

## Scene 6: The way home

**EXT. MORROW, LATE AFTERNOON**

**PLAY, 2 to 3 minutes:** Mara walks from the college toward home. The player can take a short route through the town square or stay on the direct route. Both paths rejoin before the bus stop.

On the way, the town sounds different from the morning. A shop door chimes. A bus brakes. Somebody waters plants on a balcony. Mara records one sound if the player chooses, but she does not have to collect everything.

**PHONE, CLASS GROUP CHAT**

**CLASSMATE:** Does anyone have the notes from today?<br>
**CLASSMATE:** Mara, you usually write everything down. Could you send them?

**CHOICE, MARA RESPONDS**

- Send a photo of her notes now.
- Reply, “Later, I'm on my way home.”
- Leave the messages unread.

The response changes a later phone detail, not the main story. The request shows how people rely on Mara's competence as if it is always available to them.

At the bus stop, a bus heading out of Morrow pulls away. The timetable lists destinations beyond the town. Mara watches for a moment, then the phone vibrates again.

**PHONE, CLAIRE**<br>
Aunt's nearly here. See you soon.

Mara pockets the phone and heads home.

## Scene 7: Dinner

**INT. BENNETT FAMILY DINING ROOM, EVENING**

**VISUAL:** The table is set for four. The family photo on the sideboard is straight; the framed certificates in the hall are visible from this angle. The scene feels warm, but every object has its place.

**AUNT**<br>
Your mother told me about the paper. That's wonderful, Mara.

**MARA**<br>
It was just an assignment.

**CLAIRE**<br>
It was a very good assignment.

**AUNT**<br>
You always were the one we never had to worry about.

Mara smiles.

**MARA**<br>
That's good, I guess.

**AUNT**<br>
You used to have your bag ready the night before school. Even when you were little.

**MARA**<br>
I didn't want to forget anything.

**DAVID**<br>
You never did.

**CLAIRE**<br>
You were so little. You'd check the list three times.

The family shares a fond laugh. Mara joins in, but her eyes briefly go to the phone beside her plate.

**AUNT**<br>
Have you thought about what you'll do after college?

**MARA**<br>
Not really.

**DAVID**<br>
She has time. We're looking at some options.

**CLAIRE**<br>
There are a couple of good programs we thought she might like.

Aunt nods, already imagining the plan.

**AUNT**<br>
You're lucky to have so many choices.

Mara takes a sip of water instead of answering.

Claire notices Mara's phone recorder open beside her plate.

**CLAIRE**<br>
Is that one of your little recordings?

Mara reaches to close the screen, but Claire has already seen it.

**MARA**<br>
It's the kettle. It clicks after it turns off.

**AUNT**<br>
You recorded the kettle?

**MARA**<br>
It makes a nice sound.

Claire's expression is affectionate, but distracted by worry.

**CLAIRE**<br>
That's nice, sweetheart. I just don't want you wasting time on it when you've got an exam tomorrow and applications coming up.

**MARA**<br>
It doesn't take that long.

**CLAIRE**<br>
I know. I just want you to have every option.

David looks from Claire to Mara.

**DAVID**<br>
She can do both.

**CLAIRE**<br>
I know she can. That's why I want her to stay focused.

No one raises their voice. The conversation moves on to the exam.

**CHOICE, WHAT DOES MARA DO WITH THE RECORDER?**

- Close the app without answering.
- Say, “I like doing it.”
- Say, “I'll do it after the exam.”

The replies vary slightly, but the moment ends with Mara locking the phone and putting it face-down by her plate.

Aunt lifts her glass.

**AUNT**<br>
We're all proud of you.

Mara smiles.

**MARA**<br>
Thanks.

**TRANSITION:** Hold on the smile. This shot continues directly into Cutscene 1, “The Smile,” in the next scene.

## Scene 8: The door closes

**INT. MARA'S BEDROOM, NIGHT**

**CUTSCENE 1: THE SMILE, 45 to 60 seconds**

This cutscene begins on the final toast in Scene 7.

1. Continue from the held shot and widen to include the family. The frame is neat and balanced. Claire reaches for the serving plate; David pours water. Their affection is real.
2. Follow Mara from behind as she leaves the table. Family voices continue from the dining room.

**CLAIRE (O.S.)**<br>
She's doing so well.

**AUNT (O.S.)**<br>
You must be proud.

3. Mara enters her room and closes the door. The latch clicks. The family voices stop as if they were behind glass.
4. Hold on Mara's face. A blink, a slow breath, and the smile disappears. No tears and no dialogue. The camera stays still.

The cutscene ends. Return control to the player.

**PLAY, 4 to 5 minutes:** The player can inspect four things in the room. Each provides a short visual or text beat, not a long exposition dump.

- **Certificates:** The camera frames their neat edges. Mara straightens one without thinking.
- **Family photo:** Mara smiles faintly, then looks away.
- **Study sheet:** Chapter four is highlighted in three colors.
- **Sound recordings:** She reopens the folder and plays the kettle recording. She listens all the way to the end.

A message arrives.

**PHONE, DAD**<br>
Don't forget to review chapter four.

Another.

**PHONE, MOM**<br>
Please don't disappoint everyone tomorrow. You've worked so hard.

Another.

**PHONE, PROFESSOR**<br>
Your work was excellent. Keep it up.

Another.

**PHONE, AUNT**<br>
We're all so proud of you.

The player can open and close each conversation. A family group chat has more praise, a reminder about tomorrow, and a photo from dinner. No message is a threat. The volume and repetition make them feel heavy.

**CUTSCENE 2: THE STACK, 45 to 60 seconds**

After the player closes the last main message thread, the phone lights up once more. The camera holds close to the screen. A message preview appears, but there is no new information, only another reminder.

The score's quiet motif repeats as the notification sounds arrive. Each tone is ordinary. Together, they begin to crowd the space. Do not distort the screen, add flashing effects, or make the messages sound like a horror cue.

Mara turns the phone face-down. The sounds and score cut to room tone. Hold for a breath, then return control to Mara.

## Scene 9: How do I leave?

**INT. MARA'S BEDROOM, LATE NIGHT**

Mara sits on the floor beside her bed. The room is dim. The score returns as a few quiet notes, with space between them.

She picks up the phone, opens the browser, and types:

**SEARCH:** How do I leave?

She does not press a suggested result. The question sits there. The game does not explain whether she means home, college, the expectations, or all of it.

Mara looks around the room: certificates, photos, neatly stacked books, tomorrow's study sheet. She opens her sound-recording folder and plays the morning recording. The radiator clicks; a bus passes outside.

She begins packing a small bag: phone charger, wallet, a change of clothes, keys, and the phone with her recordings. She stops at the certificates and family photos.

**PLAY, 4 to 5 minutes:** The player can inspect or leave each object, then help Mara decide what to pack. The departure itself is not a branching outcome. Mara leaves in every route.

**CUTSCENE 3: OUT THE DOOR, 90 to 120 seconds**

1. Mara looks back at the room once. Hold on the study sheet and certificates, then on the small recorder in her bag.
2. She opens the bedroom door. The hallway is framed in the same tidy symmetry as the morning scene. The family is out of view. We hear a faucet turn off, a floorboard settle, and the distant television. Home is still home.
3. Mara walks to the front door. No score yet. Her bag strap slips; she adjusts it and takes one more breath.
4. She opens the door and steps into Morrow's night air. The camera remains inside for a moment, then moves to the threshold. For the first time, Mara is not centered in the frame.
5. The door closes softly behind her. The opening notes of the Leaving cue begin, using a few sounds from her recordings.

Cut to black.

**MARA (V.O.)**<br>
I don't know where I'm going.

A pause.

**MARA (V.O.)**<br>
I just know I can't stay.

The music holds one unresolved note, then cuts to silence.

**TITLE CARD:**

# FRAGMENT AWAY
## EPISODE 1: PERFECT

**END OF FREE EPISODE.**

## Episode 1 intent checklist

- The first-play target is at least 30 minutes, with meaningful play and exploration rather than forced waiting.
- The pressure comes from many small expectations, not one villainous event.
- Claire and David show care as well as pressure.
- Mara's private interest is modest, personal, and provisional in this draft.
- The classmate interaction gives the player a glimpse of Mara's humor and ease.
- The choices invite the player to notice how Mara adapts; they are not morality tests.
- The visual language begins controlled and becomes slightly less centered as Mara acts for herself.
- The free episode ends on the departure cliffhanger. Mara leaves, but the player does not yet know where she is going.
