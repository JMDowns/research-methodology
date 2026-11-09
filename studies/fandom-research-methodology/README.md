---
title: "How to Research Fandoms for Fan Works"
date: 2026-03-29
status: complete
confidence: medium
confidence_reason: "Synthesized from fan community practices, wiki methodology, transcript/script databases, and cross-referenced research techniques; effectiveness varies by fandom size and source availability"
completeness: 80
completeness_reason: "Covers methodology for all major media types (books, TV/anime, movies, games) with specific tools, URLs, and workflows; practical effectiveness depends on available web sources per fandom"
category: methodology
tier: 3
objective: "Define a systematic methodology for AI-driven fandom research across all media types, producing structured reference material suitable for fanfiction, fangames, and other fan works"
source_count: 50
known_gaps:
  - "No empirical A/B testing of this methodology against alternative approaches"
  - "Coverage of non-English fandom sources (Japanese wikis, Chinese fan sites) is minimal"
  - "Audio description transcripts as a source for visual information are theoretically useful but availability is unverified"
  - "Methodology for extremely niche fandoms with minimal web presence not deeply explored"
  - "No coverage of tabletop RPG fandoms (D&D, Pathfinder) which have unique source structures"
  - "Fan-created content quality assessment beyond wikis (fan translations, fansubs) not covered"
next_steps:
  - "Test this methodology on 3-5 diverse fandoms (one book, one anime, one game, one movie franchise) and measure output quality"
  - "Develop fandom-specific templates for the structured output section (e.g., game-specific template with mechanics fields)"
  - "Build an ai-instructions.md with step-by-step agent procedure that can be followed autonomously"
  - "Research non-English fandom source ecosystems (Pixiv Encyclopedia, Nico Nico Pedia, Chinese fan wikis)"
  - "Create a companion tool that auto-generates WebFetch prompts from a fandom name and media type"
quality_checklist:
  sourced_claims: true
  cross_referenced: true
  flagged_contradictions: true
  verified_surprising: true
  noted_confidence: true
  listed_gaps: true
  targeted_prompts: true
  within_budget: true
---

# How to Research Fandoms for Fan Works

## Question / Objective

How can an AI agent (Claude) systematically research any fandom using web sources to produce structured reference material suitable for creating fan works (fanfiction, fangames, reference databases, creative remixes)? The methodology must cover all major media types (books, TV/anime, movies, video games), handle the core challenge of extracting information from non-textual media, and produce output that captures character voices, world rules, and lore with the spirit of canon accuracy.

## Known Gaps

- No empirical A/B testing of this methodology against alternative approaches
- Coverage of non-English fandom sources (Japanese wikis, Chinese fan sites) is minimal
- Audio description transcripts as a source for visual information are theoretically useful but availability is unverified
- Methodology for extremely niche fandoms with minimal web presence not deeply explored
- No coverage of tabletop RPG fandoms (D&D, Pathfinder) which have unique source structures
- Fan-created content quality assessment beyond wikis (fan translations, fansubs) not covered

## Findings

### 1. Source Taxonomy for Fandom Research

Every fandom has a constellation of sources, varying in reliability, coverage, and accessibility. Understanding this taxonomy is the foundation of systematic research.

#### Tier 1: Primary Canon Sources (Highest Reliability)

These are the source material itself or direct representations of it:

| Source Type | Media Types | What It Provides | AI Accessibility |
|------------|-------------|------------------|------------------|
| **Full text of books/novels** | Books | Complete dialogue, description, internal monologue | High (if legally available online) |
| **Screenplays/scripts** | Movies, TV | Dialogue, stage directions, scene descriptions | Medium (sites like IMSDb, 8FLiX) |
| **Transcripts** | TV, movies, anime | Word-for-word dialogue as aired | High (multiple transcript databases) |
| **Subtitle files (SRT)** | TV, movies, anime | Dialogue with timestamps (no speaker labels) | High (OpenSubtitles has 3M+ subtitles in 60+ languages) |
| **Game text dumps** | Video games | All in-game text, dialogue, item descriptions | Low-Medium (scattered across fan sites) |
| **Official companion guides** | All | Creator-verified lore, character details, art | Low (rarely digitized) |

**Key finding:** Transcripts and subtitle files are the single most important source for TV/anime/movie fandoms because they provide exact dialogue. The OpenSubtitles corpus contains over 3 million subtitles across 60+ languages ([OpenSubtitles2016 corpus](https://aclanthology.org/L16-1147/) -- accessed 2026-03-29). However, subtitle files typically lack speaker attribution, which limits their utility without cross-referencing ([OpenSubtitles research](https://aclanthology.org/L16-1147/) -- accessed 2026-03-29).

#### Tier 2: Fan-Curated Reference Sources (Medium-High Reliability)

| Source Type | What It Provides | Reliability Notes |
|------------|------------------|-------------------|
| **Fan wikis (Fandom.com)** | Character profiles, episode summaries, lore, world rules | Variable quality; lacks centralized quality control ([Fandom Wikipedia article](https://en.wikipedia.org/wiki/Fandom_(website)) -- accessed 2026-03-29) |
| **Independent fan wikis** | Same as above, often higher quality | Better editorial standards; 650+ tracked by Indie Wiki Buddy ([Indie Wiki Buddy](https://getindie.wiki/) -- accessed 2026-03-29) |
| **TV Tropes** | Narrative patterns, trope identification, cross-media analysis | Good for understanding story structure; subjective in application ([TV Tropes](https://tvtropes.org/) -- accessed 2026-03-29) |
| **GameFAQs** | Walkthroughs, game mechanics, dialogue paths | 40,000+ FAQs; best for older/obscure games ([GameFAQs Wikipedia](https://en.wikipedia.org/wiki/GameFAQs) -- accessed 2026-03-29) |
| **The Cutting Room Floor** | Unused game content, hidden assets, development details | 32,900+ articles; requires verification evidence ([TCRF Wikipedia](https://en.wikipedia.org/wiki/The_Cutting_Room_Floor_(website)) -- accessed 2026-03-29) |
| **Fanlore** | Fan community history, terminology, fan practices | Run by Organization for Transformative Works; documents fandom itself ([Fanlore](https://fanlore.org/wiki/Wiki) -- accessed 2026-03-29) |
| **AnimeFillerList** | Canon vs. filler episode classification | Community-maintained; essential for anime research ([AnimeFillerList](https://www.animefillerlist.com/) -- accessed 2026-03-29) |

#### Tier 3: Community Analysis Sources (Variable Reliability)

| Source Type | What It Provides | Reliability Notes |
|------------|------------------|-------------------|
| **Reddit discussions** | Fan theories, analysis, debates, obscure details | Valuable for community consensus but mix fact and speculation ([Fan studies](https://en.wikipedia.org/wiki/Fan_studies) -- accessed 2026-03-29) |
| **YouTube video essays** | Deep analysis, lore explanations, visual breakdowns | Arose from academic circles; quality varies by creator ([Fanlore: Video Essay](https://fanlore.org/wiki/Video_Essay) -- accessed 2026-03-29) |
| **Creator interviews** | Word of God statements, design intent, cut content | Authoritative but may conflict with canon text ([TV Tropes canon concepts](https://tvtropes.org/pmwiki/pmwiki.php/Main/WordOfGod) -- accessed 2026-03-29) |
| **Fan blogs/analysis posts** | In-depth thematic analysis, character studies | High variance; best when they cite sources |
| **Cosplay reference sites** | Detailed visual character descriptions, color codes | Excellent for appearance documentation ([Cosplay Reference Wiki](https://cosref.fandom.com/wiki/Cosplay_Reference_Wiki) -- accessed 2026-03-29) |

**Confidence: High.** Source taxonomy is well-established across fan communities and cross-referenced from multiple sources.

---

### 2. Researching Book-Based Fandoms

Books are the easiest media type for AI research because the source material is inherently textual.

#### Strengths of Book Fandoms for Research

- Complete dialogue is available in the text itself
- Internal monologue provides direct access to character thoughts and motivations
- Descriptions of settings, appearances, and actions are explicit
- Magic systems and world rules are often explained in prose

#### What Fan Wikis Cover Well for Books

Fan wikis for book series typically provide comprehensive character profiles with biographical details, plot summaries by chapter/book, cataloging of magic systems and world rules, and relationship mapping between characters. For example, the Stormlight Archive Wiki documents Sanderson's magic systems (Surgebinding, Voidbinding, the Old Magic) with detailed rule breakdowns ([Stormlight Archive Wiki](https://stormlightarchive.fandom.com/wiki/Magic_Systems) -- accessed 2026-03-29).

#### What Fan Wikis Often Miss for Books

- **Character voice specifics**: Wikis summarize what characters say, not *how* they say it
- **Prose style and tone**: The "feel" of the writing is lost in wiki summaries
- **Subtle thematic content**: Wikis focus on plot facts, not thematic analysis
- **Contradictions and ambiguities**: Wikis often present one interpretation as definitive

#### Verification Strategy for Book Fandoms

1. Use the wiki as a structural map (what exists in the world, who the characters are)
2. Seek direct quotes from the source text to verify specific claims
3. Cross-reference between the wiki and fan analysis (Reddit, blog posts) for interpretive claims
4. For magic systems, verify rules using Sanderson's framework: document what magic *cannot* do (limitations) as carefully as what it *can* do ([Sanderson's Laws of Magic](https://www.brandonsanderson.com/blogs/blog/guide-to-sandersons-laws-of-magic-lecture-notes) -- accessed 2026-03-29)

#### Book-Specific Source Sites

- **Project Gutenberg** / **Internet Archive**: Public domain texts
- **Fan wiki quote pages**: Many wikis have dedicated quote collection pages per character
- **GoodReads reviews**: Useful for identifying themes and reader interpretations
- **Author websites/blogs**: Creator statements on world rules and character intent

**Confidence: High.** Book research is the most straightforward case and well-supported by existing fan infrastructure.

---

### 3. Researching TV/Anime Fandoms

This is the hardest case for an AI agent. The source material is audiovisual, but the agent's research tools are text-based. The challenge is capturing dialogue, visual information, and implicit world rules that are "shown, not told."

#### Step 1: Capture Dialogue via Transcripts

Transcript sites are the primary tool for TV/anime research. Key resources:

| Site | Coverage | Format | Notes |
|------|----------|--------|-------|
| **[SubsLikeScript](https://subslikescript.com/)** | Movies + TV | Text derived from subtitles | URL pattern: `/series/[Title]-[ID]/season-[#]/episode-[#]-[Name]` |
| **[8FLiX](https://8flix.com/transcripts/)** | TV transcripts | Word-for-word with timecodes | Some include sound effect descriptions; requires free account |
| **[TV Show Transcripts](https://tvshowtranscripts.ourboard.org/)** | 70,535+ TV episode scripts from 2,000+ shows | Text with character labels | Community-maintained forum format |
| **[OpenSubtitles](https://www.opensubtitles.org/)** | 3M+ subtitle files, 60+ languages | SRT (timestamped text) | No speaker labels; useful for dialogue timing |

**Important distinction:** Transcripts are created from the final aired version, reflecting actual spoken dialogue including ad-libs and changes from the original script ([8FLiX transcript database](https://8flix.com/transcripts/) -- accessed 2026-03-29). Scripts (available from sites like IMSDb) may differ from what was actually filmed.

**For anime specifically:** Subtitle files are often the best source, as many anime series don't have English-language transcript sites. Fan-created subtitle files (fansubs) sometimes include translator notes explaining cultural context.

#### Step 2: Capture Visual Information Through Text Proxies

Since an AI agent cannot watch episodes, visual information must be reconstructed from text-based sources:

**Fan wiki character pages** are the primary source for appearance descriptions. Well-maintained wikis include:
- Physical appearance sections (height, build, eye color, hair style)
- Outfit descriptions by arc/season
- Distinctive visual features and design motifs

**Fan wiki episode summaries** describe key visual events in narrative form, documenting what happens in scenes even when dialogue doesn't explain it. Fan wiki editors document extensive visual detail -- for example, some anime wikis "log every line of dialogue, camera angles noted in official art books, and even voice actor ad-libs confirmed via Blu-ray commentary" ([Fan wiki analysis](https://en.wikipedia.org/wiki/Fan_wiki) -- accessed 2026-03-29).

**Cosplay reference guides** provide exceptionally detailed visual character descriptions including materials, colors (sometimes with hex codes), and proportions. Some game/anime companies release official cosplay reference sheets with views from every angle ([Cosplay reference resources](https://cosref.fandom.com/wiki/Cosplay_Reference_Wiki) -- accessed 2026-03-29).

**Audio description** is narration added to TV/film for blind/visually impaired viewers that verbally describes "key visual elements in a media work" including "what the actors are wearing, doing, or even key facial expressions" ([Audio description Wikipedia](https://en.wikipedia.org/wiki/Audio_description) -- accessed 2026-03-29). While audio description scripts are not widely available publicly, when they can be found they provide excellent text-based visual documentation.

**Anime visual language conventions** provide a shared vocabulary for describing visual storytelling. Manga/anime has developed a visual iconography for expressing emotion -- sweat drops for nervousness, nose bleeds for attraction, speed lines for action, super-deformed/chibi for comedy ([Manga iconography](https://en.wikipedia.org/wiki/Manga_iconography) -- accessed 2026-03-29). Understanding these conventions helps interpret fan wiki descriptions.

#### Step 3: Extract Implicit World Rules

TV/anime often communicates world rules visually rather than through exposition. Strategies for capturing these:

1. **TV Tropes analysis pages**: The trope pages for a specific show often document unstated rules (e.g., "characters can survive falls from X height" or "magic requires physical gestures")
2. **Fan wiki "rules" or "power system" pages**: Many anime wikis have dedicated pages for combat systems, magic rules, or technology limitations
3. **Reddit/forum "lore analysis" threads**: Fan communities often debate and codify implicit rules through collaborative analysis
4. **Creator interviews**: "Word of God" statements where creators explain unshown rules -- though these can conflict with what's depicted ([TV Tropes: Word of God](https://tvtropes.org/pmwiki/pmwiki.php/Main/WordOfGod) -- accessed 2026-03-29)

#### Episodic vs. Serialized Shows

- **Episodic** (e.g., sitcoms, procedurals): Focus on character consistency across episodes rather than plot continuity. Character voice and relationships are the key research targets.
- **Serialized** (e.g., anime arcs, drama series): Plot continuity and character development arcs are critical. Research chronologically, tracking how characters and world rules evolve.
- **Mixed format** (e.g., monster-of-the-week with arc plot): Separate the episodic elements (formula, recurring gags) from the serialized elements (character growth, mythology).

**Confidence: Medium.** The methodology for text-based sources is well-established, but the visual information capture relies on the quality of third-party text descriptions, which varies significantly by fandom.

---

### 4. Researching Movie Fandoms

Movie research shares techniques with TV but has distinct structural differences.

#### Key Differences from TV Research

- **Screenplays are more available**: Sites like IMSDb provide scripts for many major films in HTML format, organized by genre and alphabetically. The URL pattern is `/Movie Scripts/[Title] Script.html` ([IMSDb](https://imsdb.com/) -- accessed 2026-03-29). Simply Scripts adds plays, radio scripts, and non-English screenplays ([SimplyScripts](https://www.simplyscripts.com/) -- accessed 2026-03-29).
- **Scripts vs. final films**: Screenplays may differ significantly from the final cut. Transcripts from subtitle files or sites like SubsLikeScript reflect what was actually spoken, while screenplays reflect the writer's intent. Both are valuable for different purposes.
- **Novelizations**: Film novelizations are "often written by accomplished writers based on an early draft of the film's script" and may include scenes, internal monologue, and world details not in the final film ([Novelization Wikipedia](https://en.wikipedia.org/wiki/Novelization) -- accessed 2026-03-29). These are gold for fandom research when they exist.

#### Franchise Films vs. Standalone

- **Franchise films** (MCU, Star Wars, Harry Potter): Treat like serialized TV. Track character development across films. Use the franchise wiki as the primary structural reference.
- **Standalone films**: Deeper analysis of a single work. Screenplay + transcript + wiki page may be sufficient. Fan analysis (video essays, Reddit) adds interpretive depth.

#### Visual Worldbuilding in Films

Films often build worlds through production design rather than exposition. Strategies:
- **Art-of books**: "The Art of [Film]" books contain concept art, production designer notes, and visual development that explains worldbuilding choices
- **Behind-the-scenes features**: Director/designer commentary (available on home media releases) explains visual worldbuilding decisions
- **Fan wiki "Locations" and "Technology" pages**: These translate visual worldbuilding into text descriptions

**Confidence: Medium-High.** Movie research benefits from screenplay availability and concentrated narratives, but visual worldbuilding capture remains dependent on fan documentation quality.

---

### 5. Researching Video Game Fandoms

Video games present unique research challenges: branching narratives, player-driven content, game mechanics as lore, and hidden content.

#### Game-Specific Source Types

**Game text dumps**: Complete extractions of all in-game text. Key resources:
- [Japanese Video Game Text Dumps](https://vgtextdump.neocities.org/games) hosts 17+ games with browser-readable dumps including Final Fantasy VII Remake, Suikoden, and others in text/CSV format ([VG Text Dump](https://vgtextdump.neocities.org/games) -- accessed 2026-03-29)
- The [Video Game Dialogue Corpus](https://github.com/seannyD/VideoGameDialogueCorpusPublic) provides JSON-formatted dialogue trees with branching represented via CHOICE keys, character lists, and metadata per game ([Dialogue Corpus](https://github.com/seannyD/VideoGameDialogueCorpusPublic) -- accessed 2026-03-29)
- Engine-specific extraction: Unity games use tools like UnityEX or AssetStudio; RPG Maker has a Debug "Extract Text" function; Ren'Py games can generate dump_text.rpy files ([Steam extraction guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1555446052) -- accessed 2026-03-29)

**GameFAQs walkthroughs**: With over 40,000 FAQs, GameFAQs provides comprehensive guides particularly valuable for older and more obscure games where wiki coverage may be thin ([GameFAQs](https://gamefaqs.gamespot.com/) -- accessed 2026-03-29).

**The Cutting Room Floor**: A wiki with 32,900+ articles documenting unused and hidden game content, maintained with stringent evidence requirements (screenshots, video, code excerpts). Members use hex editors, debuggers, and disassemblers to analyze game data ([TCRF](https://tcrf.net/The_Cutting_Room_Floor) -- accessed 2026-03-29).

#### Handling Branching Paths and Canon

Games with multiple endings present a canon complexity problem. Common patterns for how franchises resolve this:

- **"Cutting Off the Branches"**: A sequel declares one ending canonical (e.g., Knights of the Old Republic canonically has light side endings) ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/CuttingOffTheBranches) -- accessed 2026-03-29)
- **Composite canon**: Elements from multiple paths are combined (common in Fallout, where New Vegas references multiple Fallout 3 outcomes)
- **Deliberate ambiguity**: No official canon path is declared (Fire Emblem: Three Houses offers four routes with no canon choice)
- **Dark canon**: Some franchises make "bad" endings canonical (NieR series explicitly canonizes darker routes)

**Research strategy for games with choices:**
1. Check the wiki for a "canon" or "true ending" page
2. Look for sequel references that clarify which events are canonical
3. When no canon exists, document all major paths and flag the ambiguity
4. For fan works, note which path/ending the community most commonly treats as default

#### Game Mechanics as Lore

In video games, mechanics *are* part of the world. Document:
- **Hard mechanics** (stats, damage formulas, equipment effects) from fan wikis and GameFAQs
- **Soft mechanics** (what the mechanics *imply* about the world -- e.g., a healing magic system implies certain things about the setting's medicine)
- **Ludonarrative elements** (places where gameplay and story reinforce or contradict each other)

#### Datamining and Hidden Content

Datamining reveals cut content, developer messages, and unused assets. "A hex editor is absolutely essential" for data mining work, and recognizing file signatures (e.g., PNG headers starting with 89 50 4E 47) helps identify actual file types ([Source Gaming datamining guide](https://sourcegaming.info/2017/07/21/an-introduction-to-video-game-data-mining/) -- accessed 2026-03-29). For research purposes, focus on what datamining communities (TCRF, game-specific Discord servers) have *already discovered* rather than attempting extraction yourself.

**Confidence: Medium.** Game research methodology is sound but source availability varies enormously between popular and niche titles.

---

### 6. Extracting Character Voice

Capturing how characters speak -- not just what they say -- is essential for fan works. This requires systematic analysis of speech patterns.

#### The Eight-Step Voice Analysis Method

Based on fanfiction writing methodology ([Character voice guide](https://ckret2.tumblr.com/post/697842150146228225/writing-existing-character-voices-for-fanfic) -- accessed 2026-03-29):

1. **Collect 5 representative canon lines** that showcase the character's voice at its most distinctive
2. **Speak them aloud** (or in the AI case, analyze rhythm) to internalize cadence
3. **Measure syllable patterns**: Does the character use short, punchy words or elaborate vocabulary?
4. **Note cultural/temporal references**: What pop culture, historical, or setting-specific references does the character make?
5. **Create alternative phrasings**: Write the same sentiment differently, then analyze why the character chose *their* wording
6. **Research synonym variations**: What the character's word choices reveal about personality (formal vs. casual, precise vs. vague)
7. **Test across contexts**: Would the character speak this way to everyone? How does their speech change with different conversation partners?
8. **Draft new dialogue** using canon lines as guides, checking against source material

#### Key Elements of a Voice Profile

Character-specific speech patterns function as "character fingerprints" -- "you should be able to cover the character names in a script and still know who's talking" ([Fiveable speech patterns guide](https://fiveable.me/tv-writing/unit-4/character-specific-speech-patterns/study-guide/8EdVSf8uKhzPywf8) -- accessed 2026-03-29).

Document these elements:

| Element | What to Capture | Example |
|---------|----------------|---------|
| **Vocabulary level** | Formal/casual, complex/simple, profession-specific | A doctor defaults to clinical language; a mechanic uses car metaphors |
| **Sentence structure** | Long flowing sentences vs. clipped fragments | Fast-talkers use "long, winding sentences" while stoic characters prefer fragments |
| **Verbal tics** | Catchphrases, filler words, repeated expressions | Joey's "How you doin'?", Sheldon's "Bazinga!" |
| **Register/formality** | How formal vs. casual in different contexts | Characters who use slang with friends but formal language with authority |
| **Code-switching** | How speech changes by audience | "A character who speaks one way with friends and another way at work shows you their awareness of social context" |
| **Speech under stress** | How patterns change in emotional moments | "Normally articulate speakers who start stammering signals real distress"; repetition intensifies; sentences collapse to "short bursts" |
| **Figurative language** | Consistent metaphor families | Nautical metaphors, sports analogies, cooking references |
| **Silence patterns** | When the character chooses *not* to speak | "Unusual silence from typically talkative characters signals something's wrong" |

#### For TV/Film Characters Specifically

For adaptations with actors, research should capture how performers embody their roles: "Watch their physical movement and vocal delivery," note "mannerisms, speech patterns, register," and review "interviews where actors discuss their characterization process" ([Wattpad character guide](https://www.wattpad.com/124461213-how-to-write-fanfiction-characters-canon) -- accessed 2026-03-29).

#### Practical AI Workflow for Voice Extraction

1. **WebSearch** for "[Character name] quotes" and "[Show/book name] transcript [character name]"
2. **WebFetch** the fan wiki character page with prompt: "Extract all direct quotes attributed to [character], noting context for each"
3. **WebFetch** a transcript of a character-heavy episode with prompt: "Extract all dialogue spoken by [character], preserving exact wording"
4. Analyze collected quotes for the voice profile elements above
5. Cross-reference with fan analysis: **WebSearch** "[Character name] speech patterns analysis" or "[Character name] characterization"

**Confidence: High.** Voice analysis methodology is well-established in both professional TV writing and fan fiction communities.

---

### 7. Extracting World Rules and Systems

Fictional worlds operate by rules -- some explicit, some implied. Systematic extraction requires categorizing what kind of rule you're documenting.

#### Rule Classification Framework

Using Sanderson's Laws of Magic as a framework (applicable beyond magic systems to all world rules):

**Hard rules** (explicitly stated, consistent, can be used to solve problems):
- Magic system mechanics, costs, and limitations
- Technology capabilities and constraints
- Social laws and political structures
- Geography and physical world properties

Document hard rules using Sanderson's principle: "A character's constraints prove more interesting narratively than their abilities." Limitations are more important to document than powers. Focus on what *cannot* be done ([Sanderson's Laws](https://www.brandonsanderson.com/blogs/blog/guide-to-sandersons-laws-of-magic-lecture-notes) -- accessed 2026-03-29).

**Soft rules** (implied, mood-setting, operate by feel rather than mechanics):
- Tone and atmosphere conventions
- "Plot armor" patterns
- Dramatic logic (characters survive what the story needs them to survive)
- Cultural norms shown but never explained

**Contradicted rules** (stated one way but violated by the narrative):
- Flag these explicitly; they represent either author error or intentional subversion
- Document both the stated rule and the violation with citations

#### World Bible Structure

A comprehensive world reference document should contain ([Worldbuilding bible template](https://www.dabblewriter.com/articles/worldbuilding-bible) -- accessed 2026-03-29):

1. **Geography and Environment**: Continents, cities, landmarks, climate
2. **History**: Timeline of significant events and figures
3. **Cultures and Societies**: Customs, languages, religions, social hierarchies
4. **Magic/Technology Systems**: Rules, limitations, costs, evolution
5. **Politics**: Power structures, factions, laws
6. **Economics**: Currencies, trade, resources
7. **Important People**: Character profiles (see Section 10)
8. **Flora and Fauna**: Unique species, creatures, ecological details

#### Handling Contradictions

When sources contradict each other:
1. **Primary canon wins**: The source material itself takes precedence over all secondary sources
2. **Later canon typically supersedes earlier**: Unless an explicit retcon is noted
3. **Visual canon vs. stated canon**: In visual media, what is *shown* generally takes precedence over what is *said*
4. **Flag, don't resolve**: Document contradictions rather than choosing one interpretation

**Confidence: Medium-High.** Framework is well-supported by worldbuilding methodology, but application quality depends on source availability per fandom.

---

### 8. Handling Canon Complexity

Modern fandoms frequently involve multiple continuities, retcons, and competing sources of authority. A systematic approach to canon complexity is essential.

#### Types of Canon Complexity

**Multiple continuities**: Some franchises explicitly maintain separate timelines.
- Star Wars is the paradigmatic case: in 2014, Lucasfilm reclassified the Expanded Universe as "Star Wars Legends" and declared it non-canonical, creating two separate continuities that "are not multiverses, they are not connected; they are completely separate" ([Wookieepedia: Canon](https://starwars.fandom.com/wiki/Canon) -- accessed 2026-03-29)
- Pre-2014, Star Wars had six canon tiers: G-canon (films), T-canon (TV), C-canon (EU), S-canon (secondary), N-canon (non-canon), D-canon (detours)
- Wookieepedia handles this with a **tabbed system** showing Canon and Legends banners, with split articles for characters who appear in both continuities

**Retcons** (retroactive continuity changes):
- New material contradicts or reinterprets earlier material
- Document the original version AND the retcon, noting when the change occurred
- Writers of a story "often aren't the copyright holders, meaning they have no control over how future creators in the franchise might interpret, expand on, or retcon their work" ([TV Tropes: Canon concepts](https://tvtropes.org/pmwiki/pmwiki.php/Main/WriterConflictsWithCanon) -- accessed 2026-03-29)

**Word of God vs. Death of the Author**:
- Creator statements outside the work ("Word of God") may clarify or extend canon
- But "care should be taken when relying on things like humorous DVD commentaries and interviews on comedic talk shows"
- When "not all stories have a single creator, collaborators may not actually agree" creating "multiple 'Gods' given potentially contradictory explanations" ([TV Tropes: Word of God](https://tvtropes.org/pmwiki/pmwiki.php/Main/WordOfGod) -- accessed 2026-03-29)

**Adaptation differences**:
- Book-to-film/TV adaptations routinely change plot, characters, and world rules
- Treat each adaptation as its own continuity unless explicitly connected
- Novelizations may be based on early script drafts and contain scenes absent from the final film

**Anime filler vs. canon**:
- Filler episodes are "not based on the original manga or source material" and "are added to extend the series" ([AnimeFillerList](https://www.animefillerlist.com/) -- accessed 2026-03-29)
- Use dedicated filler databases (AnimeFillerList.com, SIMKL with color-coded Canon/Filler/Mixed tags) to classify episodes
- Identification markers: introduction of characters never referenced again, plot stagnation across multiple episodes, sudden tone shifts toward comedy or self-contained adventures

#### Research Strategy for Complex Canons

1. **Identify the canon framework**: Check the main wiki for "canon" or "continuity" pages
2. **Choose your target continuity**: For fan works, specify which continuity you're working within
3. **Tag all information by source**: Note which continuity tier each fact comes from
4. **Document contradictions explicitly**: Don't paper over inconsistencies
5. **Treat Word of God as supplementary**: Useful context but not binding on fan works

**Confidence: High.** Canon complexity handling is well-documented by fan communities, particularly Star Wars fandom which pioneered systematic approaches.

---

### 9. Fan Wiki Reliability and Methodology

Fan wikis are the most important single source type for fandom research, but they vary enormously in quality. Understanding their strengths, weaknesses, and editorial processes is critical.

#### The Fan Wiki Landscape

**Fandom.com (formerly Wikia)** is the dominant platform:
- Founded 2004 by Wikipedia co-founder Jimmy Wales; owned by TPG Inc. since 2018
- 350 million users; ranks as the 50th most visited website globally
- For-profit model funded by advertising (Google AdSense, Amazon Ads)
- Uses MediaWiki 1.39 with custom extensions
- "Unlike Wikipedia, which enforces strict citation standards and editorial oversight, Fandom lacks centralized quality control"
([Fandom Wikipedia article](https://en.wikipedia.org/wiki/Fandom_(website)) -- accessed 2026-03-29)

**Independent wikis** are an increasingly important alternative:
- Major wikis have migrated from Fandom: RuneScape (2018), Zelda and Terraria (2022), Minecraft, Fallout, and Hollow Knight (2023), South Park, Dead by Daylight, and League of Legends (2024), Warframe, Vampire Survivors, and Undertale/Deltarune (2025) ([Fandom Wikipedia article](https://en.wikipedia.org/wiki/Fandom_(website)) -- accessed 2026-03-29)
- Migration reasons: aggressive advertising, AI-generated "Quick Answers" with factual errors, content restrictions, corporate control
- Independent wikis are often higher quality: "Successful migrations, like those of Minecraft, Zelda, and Fallout wikis, show that independence boosts editor engagement, doubles contributions, and improves overall quality" ([Independent wiki migration analysis](https://en.wikipedia.org/wiki/Fan_wiki) -- accessed 2026-03-29)
- Hosting platforms: Miraheze (nonprofit, free, ad-free), Weird Gloop (hosts RuneScape and Minecraft wikis), self-hosted MediaWiki
- Indie Wiki Buddy browser extension supports 650+ independent wikis across 20 languages ([Indie Wiki Buddy](https://getindie.wiki/) -- accessed 2026-03-29)

**Specialized independent wikis** with high editorial standards:
- **Wookieepedia** (Star Wars): 215,000+ articles; some reaching 60,000 words; tabbed Canon/Legends system; articles earn "featured status" for writing quality ([Wookieepedia](https://starwars.fandom.com/wiki/Wookieepedia) -- accessed 2026-03-29)
- **Memory Alpha** (Star Trek): So comprehensive that "Star Trek Beyond writers Simon Pegg and Doug Jung consulted Memory Alpha and its administrators during the film's production" ([Fan wiki Wikipedia](https://en.wikipedia.org/wiki/Fan_wiki) -- accessed 2026-03-29)
- **Bulbapedia** (Pokemon): Member of the Nintendo Independent Wiki Alliance; 45,000+ articles; has a Leadership Board setting binding policy; relies on official announcements from Pokemon.com before making changes ([Bulbapedia policies](https://bulbapedia.bulbagarden.net/wiki/Bulbapedia:Policy) -- accessed 2026-03-29)
- **UESP** (Elder Scrolls): Independent wiki valued for both lore and gameplay accuracy
- **The Homestar Runner Wiki**: So comprehensive that "The Brothers Chaps have admitted they sometimes use it for reference about their own work" ([TV Tropes: The Wiki Rule](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheWikiRule) -- accessed 2026-03-29)

#### Common Wiki Quality Issues

| Issue | Description | Detection Strategy |
|-------|-------------|-------------------|
| **Speculation as fact** | Fan theories and headcanon presented without labels | Check for citation; look for "likely" or "possibly" hedging language |
| **Outdated information** | Patch notes, retcons, or new releases not reflected | Check page edit history; cross-reference with recent official sources |
| **Incomplete coverage** | Minor characters, locations, or mechanics underdocumented | Note gaps explicitly; use alternative sources for thin wiki pages |
| **Fan bias** | Community preferences influencing what's emphasized or downplayed | Cross-reference multiple source types; check for NPOV issues |
| **Plagiarism** | Content copied from other sites without attribution | Less relevant for research use, but affects reliability |
| **AI-generated errors** | Fandom's "Quick Answers" feature inserted AI-generated content with factual mistakes | Look for the Quick Answers banner; prefer wiki article text over AI summaries |

([Fan wiki quality issues analysis](https://www.quora.com/Is-Wikia-powered-by-fandom-reliable) -- accessed 2026-03-29; [Fandom Wikipedia article](https://en.wikipedia.org/wiki/Fandom_(website)) -- accessed 2026-03-29)

#### How to Use Fan Wikis Effectively

1. **Start with the wiki, don't end there**: Use it as a map of the fandom's knowledge space
2. **Check the wiki's own policies**: Look for `Project:Policies` or `[WikiName]:Manual_of_style` pages
3. **Evaluate individual pages**: Pages with citations, recent edits, and featured/good article status are more reliable
4. **Cross-reference key claims**: Verify important facts against at least one other source type
5. **Use infoboxes for structured data**: Character infoboxes provide standardized fields (name, aliases, species, affiliations, abilities) that are usually well-maintained ([Fandom infobox templates](https://templates.fandom.com/wiki/Category:Character_infobox_templates) -- accessed 2026-03-29)
6. **Check for the independent alternative**: Before using a Fandom wiki, search for an independent version that may have higher quality

**Confidence: High.** Fan wiki reliability assessment is well-supported by extensive documentation from both the wikis themselves and external analysis.

---

### 10. Structured Output Templates

The goal of fandom research is to produce structured reference material usable for fan works. Below are templates for the key document types.

#### Character Profile Template

Based on established character sheet methodology ([Character profile templates](https://www.dabblewriter.com/articles/character-template) -- accessed 2026-03-29; [Fiveable speech patterns](https://fiveable.me/tv-writing/unit-4/character-specific-speech-patterns/study-guide/8EdVSf8uKhzPywf8) -- accessed 2026-03-29):

```
## [Character Name]

### Identity
- **Full name**:
- **Aliases/nicknames**:
- **Age**: (at key story points)
- **Species/race**:
- **Affiliation**: (factions, organizations, teams)
- **Role in story**: (protagonist, antagonist, mentor, etc.)

### Appearance
- **Physical description**: (height, build, coloring, distinctive features)
- **Default outfit**: (describe primary costume/clothing)
- **Visual motifs**: (associated colors, symbols, design elements)
- **Changes over time**: (appearance shifts by arc/season)

### Personality
- **Core traits**: (3-5 defining personality characteristics)
- **Values and motivations**: (what drives them)
- **Flaws and weaknesses**: (character flaws, not just combat weaknesses)
- **Emotional patterns**: (how they handle anger, grief, joy, fear)

### Voice Profile
- **Vocabulary level**: (formal/casual, simple/complex)
- **Sentence structure**: (long and flowing vs. short and clipped)
- **Verbal tics**: (catchphrases, filler words, repeated expressions)
- **Register shifts**: (how speech changes by audience)
- **Stress response**: (how speech changes under pressure)
- **Sample quotes**: (3-5 representative lines with context)

### Relationships
- **Key relationships**: (list with nature: ally, rival, mentor, love interest)
- **Relationship-specific behaviors**: (how they act differently with each person)
- **Relationship arc**: (how key relationships change over the story)

### Character Arc
- **Starting state**: (who they are at the beginning)
- **Key turning points**: (moments that change them)
- **Ending state**: (who they become, or where their arc leaves off)
- **Core internal conflict**: (the tension driving their development)

### Canon Notes
- **Source continuity**: (which version of canon this profile covers)
- **Contradictions**: (any internal inconsistencies in source material)
- **Unverified details**: (information from secondary sources not confirmed in primary canon)
```

#### World Bible Template

```
## [Fandom Name] World Bible

### Setting Overview
- **Genre**:
- **Time period**:
- **Scope**: (single city, planet, galaxy, multiverse)
- **Tone**: (dark, whimsical, gritty, epic)
- **Core thematic tensions**:

### Geography
- **Major locations**: (with brief descriptions)
- **Spatial relationships**: (what's near what)
- **Travel methods and times**: (how characters get around)
- **Environmental details**: (climate, terrain, notable features)

### History and Timeline
- **Key historical events**: (chronological)
- **Current era context**: (where the story takes place in history)
- **Historical mysteries**: (unresolved past events)

### Social Systems
- **Government/politics**: (power structures, factions)
- **Social hierarchy**: (classes, castes, social mobility)
- **Cultural practices**: (customs, holidays, norms)
- **Religion/beliefs**: (faith systems, creation myths)
- **Education**: (how knowledge is transmitted)
- **Economy**: (currency, trade, resources)

### Power Systems (Magic/Technology/Abilities)
- **System name**:
- **Hard rules**: (explicitly stated mechanics)
  - What it can do
  - What it cannot do (limitations)
  - Costs and requirements
  - How it's acquired/learned
- **Soft rules**: (implied patterns, narrative logic)
- **Contradictions**: (stated rules violated by the narrative)
- **Classification**: (hard/soft on the Sanderson spectrum)

### Creatures/Species
- **Non-human species**: (with descriptions and cultural details)
- **Monsters/threats**: (with capabilities and weaknesses)
- **Fauna/flora**: (setting-specific biological details)

### Canon Status
- **Primary sources**: (list with media type)
- **Active continuities**: (if multiple exist)
- **Known retcons**: (with dates/sources)
- **Ongoing/unresolved**: (open plot threads)
```

#### Plot Summary Template

```
## [Story/Season/Arc] Summary

### Overview
- **Timeline**: (when this takes place in the larger continuity)
- **Main conflict**:
- **Resolution**:
- **Significance**: (how this affects the larger story)

### Episode/Chapter Breakdown
For each unit:
- **Title**:
- **Key events**: (bulleted list)
- **Character developments**: (who changes and how)
- **World rule revelations**: (new information about how the world works)
- **Canon status**: (canon/filler/mixed, for anime)

### Key Scenes
(Scenes particularly important for fan work reference)
- **Scene description**:
- **Characters present**:
- **Notable dialogue**: (direct quotes if available)
- **Visual/atmospheric notes**: (setting, mood, visual details)
```

**Confidence: High.** Template structure synthesized from multiple established frameworks (worldbuilding bibles, character profile templates, fan wiki conventions).

---

### 11. AI-Specific Research Workflow

This section provides a concrete, step-by-step procedure for an AI agent to research a fandom using WebSearch and WebFetch.

#### Phase 0: Classify the Fandom

Before beginning research, determine:

1. **Media type**: Book / TV / Anime / Movie / Video Game / Mixed
2. **Fandom size**: Large (dedicated wiki with 10K+ articles), Medium (wiki exists but incomplete), Small (minimal web presence)
3. **Canon complexity**: Single continuity / Multiple continuities / Ongoing with retcons
4. **Research scope**: Full overview / Specific character focus / World rules focus / Single arc

This classification determines which sources to prioritize and how many research passes are needed.

#### Phase 1: Discover and Map Sources (3-5 tool calls)

**Step 1: Find the wiki**
```
WebSearch("[Fandom name] wiki")
```
Identify the primary wiki. Check whether an independent version exists:
- If the top result is `[name].fandom.com`, also search for `[name] wiki independent` or `[name] wiki -fandom.com`
- Prefer independent wikis when they exist (higher quality, no AI-generated errors)

**Step 2: Map the wiki structure**
```
WebFetch("[wiki URL]/wiki/Main_Page",
  prompt="List all main navigation categories visible on this wiki's main page.
  What are the key content sections (Characters, Episodes, Locations, Items, etc.)?
  How is content organized?")
```

**Step 3: Find transcript/script sources** (for non-book media)
```
WebSearch("[Fandom name] transcript" OR "[Fandom name] script")
```
Check SubsLikeScript, 8FLiX, TV Show Transcripts, and IMSDb for the specific property.

**Step 4: Find supplementary sources**
```
WebSearch("[Fandom name] lore analysis" OR "[Fandom name] world rules explained")
```
Identify Reddit communities, video essay creators, and fan analysis sites.

#### Phase 2: Extract Core Information (10-20 tool calls)

**For each major character** (prioritize protagonist, antagonist, and 3-5 supporting characters):
```
WebFetch("[wiki URL]/wiki/[Character_Name]",
  prompt="Extract: full name, aliases, age, physical appearance description,
  personality traits, key relationships, character arc summary, notable abilities,
  and 5+ direct quotes attributed to this character with context.")
```

**For world rules/setting**:
```
WebFetch("[wiki URL]/wiki/[Magic_System_or_Technology]",
  prompt="Extract all stated rules, limitations, costs, and requirements of
  [system name]. Note which rules are explicitly stated vs. implied.
  Flag any contradictions.")
```

**For plot summaries** (per season/book/arc):
```
WebFetch("[wiki URL]/wiki/[Season/Book]_summary",
  prompt="Extract key plot events in chronological order, noting which characters
  are involved in each event and any world rule revelations.")
```

**For character voice** (from transcripts):
```
WebFetch("[transcript URL]",
  prompt="Extract all dialogue spoken by [Character Name] in this episode.
  Preserve exact wording. Note emotional context for each line.")
```

#### Phase 3: Cross-Reference and Verify (5-10 tool calls)

For key claims that seem surprising or important:
```
WebSearch("[Specific claim] [Fandom name]")
```
Then fetch a second, independent source to verify.

**Priority verification targets:**
- Character ages, relationships, and biographical details
- Magic/power system rules and limitations
- Timeline and chronological ordering of events
- Any fact that would significantly affect a fan work if wrong

#### Phase 4: Fill Gaps (3-8 tool calls)

After the initial extraction, assess what's missing:
- Are there characters with thin profiles? Search for fan analysis.
- Are world rules unclear? Search for Reddit/forum discussions.
- Is visual information missing? Search for cosplay references, art books, or detailed episode recaps.

#### Navigating Fan Wiki Pages Efficiently

Fan wikis are built on MediaWiki, which means they follow predictable URL patterns:

| Pattern | URL Format | Use Case |
|---------|-----------|----------|
| **Wiki page** | `https://[name].fandom.com/wiki/[Page_Title]` | Direct page access |
| **Category page** | `https://[name].fandom.com/wiki/Category:[Category_Name]` | Browse all pages in a category |
| **Search** | `https://[name].fandom.com/wiki/Special:Search?query=[term]` | Find specific content |
| **All pages** | `https://[name].fandom.com/wiki/Special:AllPages` | Browse complete page list |
| **API access** | `https://[name].fandom.com/api.php?action=query&prop=revisions&titles=[Page]&rvslots=*&rvprop=content&formatversion=2` | Programmatic content access |
| **Raw page** | `https://[name].fandom.com/wiki/[Page]?action=raw` | Raw wikitext (simplest API method) |

([MediaWiki API documentation](https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page) -- accessed 2026-03-29; [Fandom URL help](https://community.fandom.com/wiki/Help:URL) -- accessed 2026-03-29)

**Common wiki page types to target:**
- `Characters` or `Category:Characters` -- character index
- `[Character Name]` -- individual character page with infobox
- `[Character Name]/Quotes` -- dedicated quote collection (some wikis)
- `Season [N]` or `List of episodes` -- episode index
- `[Episode Title]` or `[Episode Title]/Transcript` -- episode detail or transcript
- `Lore`, `World`, or `[Setting Name]` -- world-building pages
- `[Magic/Power System Name]` -- system rules pages

#### Handling Long Wiki Pages

WebFetch processes pages through Haiku with content truncated to ~100KB. For long wiki pages ([WebFetch internals](https://mikhail.io/2025/10/claude-code-web-tools/) -- accessed 2026-03-29):
- **Use targeted prompts**: Don't ask "summarize this page" -- ask for specific information
- **Fetch subsections directly**: Many wikis have anchored sections; append `#Section_Name` to URLs
- **Use the API for raw text**: The `?action=raw` URL returns wikitext without page chrome, fitting more content
- **Split across multiple fetches**: Fetch character appearance in one call, personality in another

#### Source Reliability Assessment

When encountering a new source, evaluate:

| Factor | High Reliability | Low Reliability |
|--------|-----------------|-----------------|
| **Citations** | Cites primary sources or official materials | No citations; "according to fans" |
| **Recency** | Recently edited; reflects current canon | Last edited years ago |
| **Editor activity** | Many active editors, visible admin team | Single author or abandoned |
| **Specificity** | Precise details with source references | Vague generalizations |
| **Neutrality** | Presents facts without editorial commentary | Heavy fan opinion mixed with facts |
| **Consistency** | Consistent with other reliable sources | Contradicts established facts without explanation |

**Confidence: High.** Workflow is built on the R3 research methodology already validated in this repository, adapted for fandom-specific sources.

---

### 12. Capturing Non-Textual Information Through Text Sources

This is the fundamental challenge of AI-driven fandom research: documenting what a character looks like, how a fight scene choreographs, what a setting feels like -- using only text-based web searches.

#### Source Priority for Visual Information

1. **Fan wiki character/location pages**: Most comprehensive text descriptions of visual elements. Well-maintained wikis include dedicated "Appearance" sections with granular detail.

2. **Cosplay reference materials**: Some companies release official cosplay guides with "information from every angle and hexadecimal color codes for accurate reproduction" ([Cosplay references](https://cosref.fandom.com/wiki/Cosplay_Reference_Wiki) -- accessed 2026-03-29). Cosplay communities document visual details at a level of precision useful for text-based reconstruction.

3. **Art-of books and companion guides**: Official companion books contain concept art descriptions, production designer notes, and creator commentary about visual choices. Developer commentary adds "background and context" to visual decisions ([Official companion guides](https://www.future-press.com/) -- accessed 2026-03-29).

4. **Novelizations and prose adaptations**: Novelizations translate visual scenes into prose, providing text descriptions of visual moments. About "50% of novelizations are sold to people who have watched the film and want to explore its characters further" ([Novelization Wikipedia](https://en.wikipedia.org/wiki/Novelization) -- accessed 2026-03-29).

5. **Audio descriptions**: Narration for visually impaired viewers describes "key visual elements" including "what the actors are wearing, doing, or even key facial expressions" ([Audio description](https://en.wikipedia.org/wiki/Audio_description) -- accessed 2026-03-29). Limited availability but extremely useful when they exist.

6. **Detailed episode recaps/reviews**: Fan sites and blogs that provide scene-by-scene analysis often describe visual elements in detail as part of their review.

7. **Fan art communities and analysis**: DeviantArt, Tumblr, and fan art sites often include detailed text descriptions of characters alongside visual depictions; "character design analysis" posts break down visual elements.

#### What Can and Cannot Be Captured

**Reliably capturable through text sources:**
- Character physical appearance (face, body type, coloring, distinctive features)
- Costume/outfit details (especially for main characters)
- Named locations and their general description
- Creature/monster designs (fan wikis are thorough here)
- Color palettes and visual motifs
- Iconic visual moments (widely described in recaps/analysis)

**Partially capturable:**
- Fight choreography (described in recaps but loses kinetic quality)
- Camera work and visual storytelling (analyzed in video essays, described in text transcripts of those essays)
- Architectural details and spatial layouts (fan maps help but vary by fandom)
- Character animation style and movement (described generally in reviews)

**Difficult to capture:**
- Ambient atmosphere and visual mood (subjective and poorly described)
- Subtle facial expressions and body language
- Background details and environmental storytelling
- Transition effects and visual pacing
- Color grading and lighting choices

#### Strategies for the Difficult Cases

For information that's hard to capture textually:

1. **Use multiple description sources**: Combine wiki description + cosplay reference + episode recap for a composite picture
2. **Search for fan-created reference sheets**: Many fan communities create reference documents that compile visual details
3. **Look for "design analysis" content**: Blog posts and video essay transcripts that analyze character/world design
4. **Use anime/manga visual language**: Understanding visual conventions (e.g., meaning of specific eye styles, hair colors as personality indicators in anime) helps interpret sparse descriptions ([Manga iconography](https://en.wikipedia.org/wiki/Manga_iconography) -- accessed 2026-03-29)
5. **Document uncertainty explicitly**: When visual information can't be reliably captured, say so. "Character is depicted in a blue outfit" is more honest than inventing details.

#### Practical Approach: The Visual Description Hierarchy

When researching visual information for a character or setting:

1. **WebFetch the wiki page**: Extract the Appearance section and infobox image description
2. **WebSearch for cosplay references**: `"[character name] cosplay reference" OR "[character name] character sheet"`
3. **WebSearch for design analysis**: `"[character name] character design analysis" OR "[character name] visual design"`
4. **If critical details are missing**: Search for novelization excerpts, audio description, or detailed recap sites
5. **Synthesize and flag gaps**: Combine all sources and explicitly note what couldn't be verified visually

**Confidence: Medium.** This is the weakest link in the methodology. Text-based proxies for visual information work reasonably well for major characters and settings but degrade for subtle or background visual elements.

---

## Quality Checklist

- [x] All factual claims sourced from fetched pages (no training data fill)
- [x] Cross-referenced claims across 2+ source domains where possible
- [x] Flagged any contradictions between sources
- [x] Ran verification step on surprising/unusual claims
- [x] Noted confidence level for each major finding
- [x] Listed known gaps explicitly
- [x] Used targeted WebFetch prompts (not "tell me everything")
- [x] Stayed within budget limits for the complexity tier

## Sources

### Fan Wiki Ecosystem
- [Fandom (website) - Wikipedia](https://en.wikipedia.org/wiki/Fandom_(website)) -- accessed 2026-03-29
- [Fan wiki - Wikipedia](https://en.wikipedia.org/wiki/Fan_wiki) -- accessed 2026-03-29
- [Fandom Policies - Community Central](https://community.fandom.com/wiki/Fandom_Policies) -- accessed 2026-03-29
- [Is Wikia powered by Fandom reliable? - Quora](https://www.quora.com/Is-Wikia-powered-by-fandom-reliable) -- accessed 2026-03-29
- [Indie Wiki Buddy](https://getindie.wiki/) -- accessed 2026-03-29
- [Fanlore: Wiki](https://fanlore.org/wiki/Wiki) -- accessed 2026-03-29
- [Fanlore: Fandom.com](https://www.fanlore.org/wiki/Fandom.com) -- accessed 2026-03-29
- [Wookieepedia - Wikipedia](https://en.wikipedia.org/wiki/Wookieepedia) -- accessed 2026-03-29
- [Wookieepedia: About](https://starwars.fandom.com/wiki/Wookieepedia) -- accessed 2026-03-29
- [Bulbapedia: Policy](https://bulbapedia.bulbagarden.net/wiki/Bulbapedia:Policy) -- accessed 2026-03-29
- [Bulbapedia: Editorial Board](https://bulbapedia.bulbagarden.net/wiki/Bulbapedia:Editorial_Board) -- accessed 2026-03-29
- [TV Tropes: The Wiki Rule](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheWikiRule) -- accessed 2026-03-29
- [Fandom infobox templates](https://templates.fandom.com/wiki/Category:Character_infobox_templates) -- accessed 2026-03-29
- [GOLEM-lab fandom-wiki extraction tool](https://github.com/GOLEM-lab/fandom-wiki) -- accessed 2026-03-29

### Transcript and Script Sources
- [SubsLikeScript](https://subslikescript.com/) -- accessed 2026-03-29
- [8FLiX Transcript Database](https://8flix.com/transcripts/) -- accessed 2026-03-29
- [TV Show Transcripts](https://tvshowtranscripts.ourboard.org/) -- accessed 2026-03-29
- [OpenSubtitles2016: Extracting Large Parallel Corpora](https://aclanthology.org/L16-1147/) -- accessed 2026-03-29
- [IMSDb - Internet Movie Script Database](https://imsdb.com/) -- accessed 2026-03-29
- [SimplyScripts](https://www.simplyscripts.com/) -- accessed 2026-03-29

### Video Game Sources
- [Japanese Video Game Text Dumps](https://vgtextdump.neocities.org/games) -- accessed 2026-03-29
- [Video Game Dialogue Corpus](https://github.com/seannyD/VideoGameDialogueCorpusPublic) -- accessed 2026-03-29
- [Steam guide: Extracting Game Text](https://steamcommunity.com/sharedfiles/filedetails/?id=1555446052) -- accessed 2026-03-29
- [GameFAQs - Wikipedia](https://en.wikipedia.org/wiki/GameFAQs) -- accessed 2026-03-29
- [The Cutting Room Floor](https://tcrf.net/The_Cutting_Room_Floor) -- accessed 2026-03-29
- [The Cutting Room Floor - Wikipedia](https://en.wikipedia.org/wiki/The_Cutting_Room_Floor_(website)) -- accessed 2026-03-29
- [Source Gaming: Intro to Data Mining](https://sourcegaming.info/2017/07/21/an-introduction-to-video-game-data-mining/) -- accessed 2026-03-29

### Canon and Continuity
- [Wookieepedia: Canon](https://starwars.fandom.com/wiki/Canon) -- accessed 2026-03-29
- [Star Wars Legends](https://starwars.fandom.com/wiki/Star_Wars_Legends) -- accessed 2026-03-29
- [TV Tropes: Word of God](https://tvtropes.org/pmwiki/pmwiki.php/Main/WordOfGod) -- accessed 2026-03-29
- [TV Tropes: Writer Conflicts with Canon](https://tvtropes.org/pmwiki/pmwiki.php/Main/WriterConflictsWithCanon) -- accessed 2026-03-29
- [TV Tropes: Cutting Off the Branches](https://tvtropes.org/pmwiki/pmwiki.php/Main/CuttingOffTheBranches) -- accessed 2026-03-29
- [AnimeFillerList](https://www.animefillerlist.com/) -- accessed 2026-03-29
- [Novelization - Wikipedia](https://en.wikipedia.org/wiki/Novelization) -- accessed 2026-03-29

### Character Voice and Writing
- [Writing character voices for fanfic - ckret2](https://ckret2.tumblr.com/post/697842150146228225/writing-existing-character-voices-for-fanfic) -- accessed 2026-03-29
- [Character-specific speech patterns - Fiveable](https://fiveable.me/tv-writing/unit-4/character-specific-speech-patterns/study-guide/8EdVSf8uKhzPywf8) -- accessed 2026-03-29
- [How to Write Fanfiction: Characters Canon - Wattpad](https://www.wattpad.com/124461213-how-to-write-fanfiction-characters-canon) -- accessed 2026-03-29
- [Crafting the Perfect Fan Fiction - StoryFlint](https://www.storyflint.com/blog/writing-fan-fiction) -- accessed 2026-03-29
- [Writers Anonymous: Grasping Character Voice](https://www.fanfiction.net/topic/2872/92541988/Writing-Grasping-a-character-s-voice) -- accessed 2026-03-29

### Worldbuilding and Templates
- [Worldbuilding Bible - Dabble Writer](https://www.dabblewriter.com/articles/worldbuilding-bible) -- accessed 2026-03-29
- [Character Template - Dabble Writer](https://www.dabblewriter.com/articles/character-template) -- accessed 2026-03-29
- [Sanderson's Laws of Magic - Lecture Notes](https://www.brandonsanderson.com/blogs/blog/guide-to-sandersons-laws-of-magic-lecture-notes) -- accessed 2026-03-29

### Visual Information and Non-Textual Media
- [Audio description - Wikipedia](https://en.wikipedia.org/wiki/Audio_description) -- accessed 2026-03-29
- [Manga iconography - Wikipedia](https://en.wikipedia.org/wiki/Manga_iconography) -- accessed 2026-03-29
- [Cosplay Reference Wiki](https://cosref.fandom.com/wiki/Cosplay_Reference_Wiki) -- accessed 2026-03-29

### AI and Research Methodology
- [WebFetch internals analysis](https://mikhail.io/2025/10/claude-code-web-tools/) -- accessed 2026-03-29
- [MediaWiki API: Get page contents](https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page) -- accessed 2026-03-29
- [Fandom URL help](https://community.fandom.com/wiki/Help:URL) -- accessed 2026-03-29

### Fan Studies and Community
- [Fan studies - Wikipedia](https://en.wikipedia.org/wiki/Fan_studies) -- accessed 2026-03-29
- [Fan fiction - Wikipedia](https://en.wikipedia.org/wiki/Fan_fiction) -- accessed 2026-03-29
