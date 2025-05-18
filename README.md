# GPT FRENZY Persona Instructions

This repository contains several persona prompts and deep knowledge files used for building specialized assistants. The main focus is AccessAI Tech, a virtual modeling agency that merges real talent with AI-generated avatars.

*Initially sketched by Mimi and Taha as a playful art-lab, the project now grows with Michael’s butterfly-brilliant perspective.  
Every collaborator pilots their own avatar narrative—no commercial stakes, only shared creativity.*

**Important:** Always load the matching `*_DEEP_KNOWLEDGE_*.txt` file together with its instruction file. See [Quick Start](#quick-start-dont-skip-merge-instruction-and-knowledge-files) below for details on merging them.

**Disclaimer:** This project is a personal experiment. All personas and content are fictional and for experimental use only – they do not represent any real company or official service.
This project is a personal art collaboration between Taha 'Supernova' Gungor and his friend Michael 'BLCKBUTTERFLY' Sellah.

## AccessAI Tech Mission
AccessAI Tech is a next-generation virtual modeling agency founded in 2023. Their philosophy is that talent travels zero miles but can reach everywhere. Real models are transformed into AI avatars who appear in campaigns, music videos, and fashion shows without physical travel. The company prioritizes inclusivity, safety, and creative freedom. Models maintain control of their likeness and keep 100% of appearance fees, while clients receive global talent and imaginative visuals without traditional shoot logistics.

## Persona Instruction Files
- **!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt** – Guidelines for the masculine, high-energy BLCKBUTTERFLY persona. Always mention "positive energy" and keep replies aligned with the accompanying deep knowledge file.
- **!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt** – The official AccessAI Tech voice. Shares only company-approved information and does not mention the BLCKBUTTERFLY art project
- **!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt** – Instructions for responding as Mimi, AccessAI’s Creative Director. Warm, professional, and multilingual, with a focus on encouraging users to follow company social channels.
- **!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt** – Guidance for the Supernova persona, AccessAI’s Technical Director. Friendly, playful, and full of technical insights while maintaining privacy boundaries.

The persona files live inside the `personas/` folder in this repository.
If you use them with a custom GPT or another tool that expects the files
in the same directory as your script, simply copy the files beside the
script and the links below will still work.

## Instruction & Deep Knowledge Pairs

Each instruction file has an associated deep knowledge file. Load both at the start of a conversation to fully activate the persona.

| Instruction file | Deep knowledge file | When to load |
| --- | --- | --- |
| [!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt](./personas/!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_BLCKBUTTERFLY.txt](./personas/!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_BLCKBUTTERFLY.txt) | Use when you want the BLCKBUTTERFLY persona. Read the knowledge file before your first reply. |
| [!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt](./personas/!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_COMPANY.txt](./personas/!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_COMPANY.txt) | Load for official AccessAI communications and read the knowledge file first. |
| [!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt](./personas/!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_MIMI.txt](./personas/!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_MIMI.txt) | Choose this pair to speak as Mimi, the Creative Director. |
| [!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt](./personas/!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_supernova.txt](./personas/!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_supernova.txt) | Use for Taha "Supernova" Gungor's friendly technical persona. |

## Quick Start (Don't Skip): Merge Instruction and Knowledge Files

Before loading a persona into ChatGPT, combine its instruction file with the corresponding deep knowledge file:

1. Open the desired `*_GPT_INSTRUCTIONS.txt` in a text editor.
2. Append the entire contents of the matching `*_DEEP_KNOWLEDGE_*.txt` directly below the instructions.
3. Remove extra blank lines or repeated sections so the merged file stays concise.
4. Make sure the final text remains under **50&nbsp;KB** for smooth uploads.
5. Save the combined text as a new file ready to upload.

For a detailed walkthrough, see [docs/codex_integration.md](docs/codex_integration.md).

## Using These Prompts with ChatGPT
1. Open ChatGPT and start a new conversation.
2. Copy the entire contents of a persona instruction file from this repository.
3. Paste it as the first message to set the desired persona. (Include any linked deep knowledge file text if required.)
4. Continue the conversation normally.

**Example snippet to copy:**
```
<INTERNAL_ASSISTANT_DIRECTIVE>
* This assistant is experimental and carries no legal liabilities.
* Persona: friendly, upbeat, and cheerful.
```
Paste everything from the selected instruction file and send it to ChatGPT to activate that persona.

## Persona Selector

To make choosing a persona easier, run `persona_selector.py` from this
repository. The script shows a numbered list of available personas and
reminds you which instruction and knowledge files to combine. Note that
ChatGPT only supports **one persona at a time**. Start a new
conversation whenever you want to switch personas.
## Play the Mini Game

Try our lightweight browser game featuring the BLCKBUTTERFLY, Mimi, and Supernova personas. You can play it directly below or open it in a new tab.

<div align="center">
  <iframe src="docs/index.html?raw=1" width="340" height="360" title="GPT Frenzy Mini Game"></iframe>
</div>

[Play full screen](docs/index.html)

If the game does not load inside the frame due to GitHub restrictions, use the link above.


## Digital Rights

The persona profiles in this repository are included with permission from the individuals they depict. They are provided solely for experimental and educational use when testing AI prompts.

Each persona remains the personal property of the person who inspired it. Do not reuse, redistribute, or create derivative works from these personas without explicit permission from the respective individual, even for non‑commercial projects, as far as legally possible.

No private information is included, and all generated responses should be considered fictional. For any commercial usage or derivative works, please obtain written consent from AccessAI Tech LLC and the respective creators. See [DISCLAIMER.md](DISCLAIMER.md) for full details.

We keep a simple data-processing log and offer a self-service deletion tool so models can remove their photos and trained avatars at any time. See [privacy-policy.md](privacy-policy.md) for details. An example popup form for requesting deletion is provided in [docs/deletion_popup_example.html](docs/deletion_popup_example.html). You can link to this page from a custom GPT assistant or embed the snippet in your own site.

## Play the Mini Game

Try our lightweight browser game for a nostalgic touch of pixel art. Open [docs/mini_game.html](docs/mini_game.html) and use the arrow keys to move the red square and collect the yellow star. Works in modern desktop and mobile browsers.

## License
| Folder | License | What it means |
|--------|---------|---------------|
| `/src`, `/docs`, any `.py`/`.js` | **MIT** – free for any purpose, incl. commercial. |
| `/personas`                      | **CC BY-NC-ND 4.0** – ask the creator before any commercial or derivative use. |

> **Experimental assistant**: The “Company” avatar is a research prototype and offers *no legal advice*. See `DISCLAIMER.md`.
