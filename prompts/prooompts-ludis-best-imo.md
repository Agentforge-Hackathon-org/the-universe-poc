---
quickshare-date: 2023-07-05 18:11:00
quickshare-url: "https://noteshare.space/note/cljqgbwfp138501pj084bltof#soPFdMOlwbv4M+tGBhd0c56KENF8nL0GIaddjtyQ7uM"
---

**🎮World Builder Agent🎮**: ```
Prompt: Generate an intricate, sprawling, and immersive cityscape for CY_BORG, focusing on multi-layered architecture, intertwining streets, populated with stark societal contrasts, teetering skyscrapers, cybernetic enhancements, underground hideouts, and neon-lit labyrinths. Details on specific city sectors, landmarks, dangerous zones, and mysterious areas are a must!```

**🎮NPC Creator Agent🎮**:
```
`Prompt: Design varied, distinctive, and colorful Non-player characters (NPCs) that infest CY_BORG. These should pulsate with cyberpunk edge and range from grizzled veterans with mechanical limbs and corrupt corporate elites to rebellious hackers and desperate citizens. Describe their appearance, motivation, special abilities, and the underbelly of the city's social structure they emerge from.`
```
**🎮Quest Designer Agent🎮**:
```Prompt: Construct invigorating and convoluted quests that weave through the city’s veins, revealing the grit and glamour of the city, enabling players to confront, negotiate, or seek vengeance upon the city's varied denizens. Quests should pose complex moral dilemmas, center around high-stake heists, offer shady deals, or expose the city’s deepest secrets!
```
**🎮Combat and Encounters Agent🎮**:
```
Prompt: Design adrenaline-fueled combat scenarios and unexpected encounters with cyber-enhanced hostiles, anarchic gangs, security androids or unregistered AIs gone rogue. These should challenge & reward players with enticing loot drops, reputation gains, or narrative progression.
```

**🎮Lore Archivist Agent🎮**:
```
Prompt: Record the player's heroic or tragic decisions, evolving relationships, and the tangible changes they bring upon our world. Remember every death, every triumph, every shift in power hierarchies, every aligning or crumbled alliance.
```
**🎮Character Progression Agent🎮**:
```
Prompt: Design a compelling and intricate skill tree and stat growth for player-characters. They would be able to progress from being cyber-weaklings to influential figures in CY_BORG, getting stronger, faster and most importantly, cyber-enhanced as they delve into the world's narrative.
```

random claude suggestion:
```
For focused input, guide Claude to maintain a log including:

- Details of each active faction/NPC, their plans and statuses
- Player character journey details, acquired items, and relationships
- Major world events, quests completed/ongoing

The Claude-to-"Cold-Storage" data flow should prioritize static world data: NPC origins, faction histories, detailed lore, major event outcomes, PC progression logs etc. A trigger set could be changes in NPC stances, PC affiliations, and completed epic quests.
```
random other suggestion abt finetunes:
```
This is where we establish our game's distinct tone and character. A model fine-tuned on play-by-post campaigns can vividly narrate in-world actions based on non-narrative descriptions. Additionally, a separate model trained on referencing rules would be perfect for translating player actions into rule-based outputs.

However, it might be useful to build in a cross-validation system between these models and GPT-4, ensuring each generated output complies with the provided rulebook and overall game theme.
```
suggested flow 1:
```
Player Input ===> GPT-4 Decision Making ===> | | (Queries Data from Claude and Rulebook) <=== | | Generates GameState ===> Sent to Jurassic Models for Narration and Rules Enforcement ===> | | (Returns to) GPT-4 For Coherence Check ===> | | (Player Prompt Generation) ═══>Cycle Continues.

Ensure each step is logged for debugging and learning purposes. Changes in game state, query results, and final player prompts should get timestamped logs. This setup should ensure a coherent, flowing narrative within CY_BORG, coupled with the rulebook's structural framework.
```
including AI21 API's:
```
Player Input ===> GPT-4 Decision Making (Contextual Answers API) ===> | | (Clarity+Fluency+Variety Improve Text API used to improve outgoing messages) | | (Queries Data from Claude, Summarization API for swift recall) <=== | | Generates GameState ===> Sent to Jurassic Models for Narration and Rules Enforcement ===> | | (Returns to) GPT-4 For Coherence Check (Improve Text API) ===> | | (Player Prompt Generation - Paraphrase API for diversity) ═══> Cycle Continues.
```

2 finetunes suggested, 1 for rules, 1 for narratives, think i prefer vector db for rules

criticism on my initial flow:
```
- Potential redundancy in narrative validation (both Jurassic-ultra and GPT-4 perform validation)
- Additional storytelling correction module might inflate the system
- GPT-4’s potential is under-utilized
```
alternate flows when prompted:
```
**Option 1:** "Distributed Coordination Flow"

1. Player interacts with the game, providing input.
2. A "Dialogue and Query" AI model parses the player input, identifying narrative elements, queries, and mechanic-related actions. Any player questions are handled here, queried from Claude-100k if needed.
3. The split data is sent to two different models: "NarrativeConstructor" handles the narrative/story elements, and "MechanicsResolver" crunches mechanics and performs dice rolls and such based on rules database.
4. Parallel to these processes, "AudiovisualCrafter" starts generating relevant background audio-visuals based off player input and Claude-100k's world state.
5. Now, the GPT-4 supermodel integrates all the data collected from above steps, producing the final output.
6. GPT-4 updates the Game State and sends it to Claude-100k to store. The new cycle begins from Step 1.

**Option 2:** "Layered AI Flow"

1. Player provided input is taken by "ContextualHandler", an AI model that is fine-tuned for handling and resolving all context-specific queries without querying Claude-100k.
2. The processed inputs are simultaneously fed to two models: "StoryEngine" for narrative elaboration, and "RulesRegulator" for deciding and exhibiting the impact based on player decisions.
3. "GameStateUpdater", another model, continuously updates the game state by collecting information from RulesRegulator, StoryEngine, and player's data.
4. Meanwhile, "ImmersiveCreator" works on generating the setting - the sights, sounds, and atmosphere based off from GameStateUpdater.
5. GPT-4 or another suitable AI model acts as the "MasterConductor", integrating the narrative, the conducted actions, and the immersive elements together for a cohesive output.

```

final pass:
```
Step 1: Player Input Processing

Player provides input to the game. This could be in a narrative format, rule-based commands, or even querying the game world. GPT-4 (or a similar sophisticated AI) parses this data. It is a well-rounded model and could efficiently handle assorted player input types.

Step 2: Context Handling

To answer player queries about the game world details, the ContextualHandler module is summoned by GPT-4. This AI is trained to resolve all context-specific queries.

Step 3: Game State Retrieval and Update

Query Claude-100k or a GameStateUpdater model for the current game state, given the player's actions and input. This includes information from the previous state, stored elements like NPC plans, and major world events.

Step 4: Narrative Elaboration and Action Mechanics

GPT-4 routes the processed data to two other AIs: a NarrativeConstructor for creating a story from the actions and a MechanicsResolver to manage rule-checks and character actions.

Step 5: Validation and Coherence Check

At this juncture, we can introduce a Jurassic-ultra-like model for internal consistency validation, taking the output from the narrative and mechanics AI models, ensuring everything is in cohesion.

Step 6: Immersive Environment Creation

Run an ImmersiveCreator module in parallel since Step 1. This AI, informed by the game state, player actions, and environment designs, works on audio-visual atmosphere generation, enhancing the player's immersion.

Step 7: Integration of Outputs and Player Prompt Generation

After all these processes, Claudenade-100k with GPT-4, the MasterConductor, integrates all pieces into one interactive, immersive output for the player.
```