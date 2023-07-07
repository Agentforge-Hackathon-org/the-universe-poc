---
quickshare-date: 2023-07-05 18:11:28
quickshare-url: "https://noteshare.space/note/cljqgchrl139201pjcvawvm4y#6tD4tOSXc69OCQ3gfpsmy43XewqejMLCrci8FV6tLNY"
---
collection of generation prompts:

```
1. 🚀 '[Assistant] Generate a unique gang in the dystopian city of CY_BORG with detailed hierarchical structure, their motif, territory, and the secret conspiracy they are plotting.'
    
2. 💥 '[Assistant] How would cybernetic prosthetics impact the economy and social dynamics in CY_BORG City? Detail the black market and the key players involved.'
    
3. 🕵️ '[Assistant] The protagonist uncovers encrypted data hinting at a significant plot point. Encapsulate the thrill of detection by simulating cryptic data decryption.'
    
4. 😉 '[Assistant] Write an encounter with an elusive, highly skilled, and mischievous hacker who leaves behind cryptic riddles.'
    
5. 🍸 '[Assistant] Generate dialogue for a meeting in the underground neo-noir bar—an undercover agent, a cybernetic hacker, and a rogue politician.'
    
6. 🦾 '[Assistant] Design a high-stakes and labyrinthine corporate skyscraper, riddled with state-of-the-art security systems, hidden chambers, and a clandestine research lab.'
    
7. 🏍️ '[Assistant] Describe a high-speed pursuit through neon-lit alleys: hoverbikes, indiscriminate drones, and the danger from rival gangs.
``````
Claude living db:
```
"Claude, update incoming[UUID]: Here's what took place since your last update....[Detailed events]. Now, generate a summary for the current world status and compile recent significant events or changes from factions, NPCs, or the environment.”
```
initial claude prompt:
```
summarize the events from the last game session leading up to the current game state. Include a detailed description of the previous rounds' actions and any significant world changes."
```

storyteller:
```
"Based on these out of character descriptions of events and actions...[OOC descriptions], craft a fitting narrative description capturing the dark, cyberpunk dystopian world of CY_BORG.”
```
alt storyteller:
```
"From these events...[Input from Claude], generate CY_BORG's fitting narrative that mystifies the cyberpunk dystopia."
```
storyteller enrichment:
```
"Examine the following story fragment: [Story from Storytelling module] Ensure consistency, depth, and vivid imagery."
```
rules checker:
```
"A player wants to perform ...[action]. What are the relevant rules or constraints from the CY_BORG rulebook?”
```
alt rules checker:
```
"Based on these attempted actions...[Player Actions], look up the relevant rules, perform the necessary die rolls, and determine the outcome."
```

rejected for incoherence, sent back with notes for improvement:
```
"Refine the narrative based on these notes...[Feedback from Jurassic-Ultra] to ensure it aligns with the CY_BORG tone and story progression."
```
GPT4, decide tools:
```
"Based on the refined narrative...[Narrative from Storytelling Correction Module], decide what game tools are needed (like background images, soundtracks, rules database checks, etc.)."
```
GPT4 - 'interplayer', resolves ambiguities and determines IC knowledge
```
"Players attempted the following actions...[Player Actions]. Resolve any ambiguities, check for character knowledge, and propose ways to reach their goals."
```
Update game state:
```
"The players made their actions and these events occurred...[Resultant events and actions]. Update the current game state and prepare for the next round."
```

suggested improvements:

Improvements:

- Consolidation: Some of the tasks assigned to different models are quite similar. Models that produce/refine narratives could be consolidated into one or two highly-tuned models for simplicity.
- Transition Buffering: The handoff between models may produce out-of-context responses. Adding a buffer that synthesizes the outputs of one model and formulates inputs for the next model could smooth transitions.
- - Sound/Image Buffering: Instead of generating new images/sounds continuously, the AI could create a 'buffer' of possible assets. It draws from the buffer according to the refined narrative for the next round.
- Explicit Error Handling: Given the diversity in tasks and assets, more robust error handling and quality checks should be integrated.

final pass prompts:
claude living db
```
"Claude, provide an overview and detailed description of events since our last gameplay session, focusing on the last few rounds."
```
GPT4 storyteller

```"From the information provided, generate a cohesive narrative consistent with the CY_BORG universe and provide detailed descriptions of significant events."```


Jurassic, narrative validation+feedback
```
"Ensure the coherency, depth, and vivid imagery of the following story fragment produced by GPT-4. Provide constructive critiques."
```

GPT4, tool selection [added: incorporate critiques]
```
"Based on the provided critiques, revise the narrative presented. Using this revised narrative, project what tools such as background images, soundtracks, and rules database checks might be necessary to enrich the gameplay experience."
```

gpt4, player interaction/clarifying questions/prompts to players:
```
"Gather player responses or questions about the scene. If necessary, propose actions based on their characters' knowledge and context."
```
claude, if used as or referencing rules db/alternate rules checker:
```
"Given the players' decisions as clarified, look up the relevant rules, perform necessary die rolls, determine the outcome, and notify GPT-4."
```
gpt4 gamestate updater:

```
Given the outcome of the players' actions and the current game state, prepare for the next round."
```