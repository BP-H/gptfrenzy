# GPT FRENZY Persona Instructions

This repository contains several persona prompts and deep knowledge files used for building specialized assistants. The main focus is AccessAI Tech, a virtual modeling agency that merges real talent with AI-generated avatars.

**Disclaimer:** This project is a personal experiment. All personas and content are fictional and for experimental use only – they do not represent any real company or official service.
This project is a personal art collaboration between Taha 'Supernova' Gungor and his friend Michael 'BLCKBUTTERFLY' Sellah, separate from Taha's role at AccessAI Tech.

## AccessAI Tech Mission
AccessAI Tech is a next-generation virtual modeling agency founded in 2023. Their philosophy is that talent travels zero miles but can reach everywhere. Real models are transformed into AI avatars who appear in campaigns, music videos, and fashion shows without physical travel. The company prioritizes inclusivity, safety, and creative freedom. Models maintain control of their likeness and keep 100% of appearance fees, while clients receive global talent and imaginative visuals without traditional shoot logistics.

## Persona Instruction Files
- **!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt** – Guidelines for the masculine, high-energy BLCKBUTTERFLY persona. Always mention "positive energy" and keep replies aligned with the accompanying deep knowledge file.
- **!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt** – The official AccessAI Tech voice. Shares only company-approved information and does not mention the BLCKBUTTERFLY art project, which is separate from AccessAI.
- **!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt** – Instructions for responding as Mimi, AccessAI’s Creative Director. Warm, professional, and multilingual, with a focus on encouraging users to follow company social channels.
- **!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt** – Guidance for the Supernova persona, AccessAI’s Technical Director. Friendly, playful, and full of technical insights while maintaining privacy boundaries.

## Instruction & Deep Knowledge Pairs

Each instruction file has an associated deep knowledge file. Load both at the start of a conversation to fully activate the persona.

| Instruction file | Deep knowledge file | When to load |
| --- | --- | --- |
| [!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt](./!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_BLCKBUTTERFLY.txt](./!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_BLCKBUTTERFLY.txt) | Use when you want the BLCKBUTTERFLY persona. Read the knowledge file before your first reply. |
| [!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt](./!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_COMPANY.txt](./!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_COMPANY.txt) | Load for official AccessAI communications and read the knowledge file first. |
| [!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt](./!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_MIMI.txt](./!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_MIMI.txt) | Choose this pair to speak as Mimi, the Creative Director. |
| [!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt](./!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt) | [!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_supernova.txt](./!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_supernova.txt) | Use for Taha "Supernova" Gungor's friendly technical persona. |

## Quick Start: Merging Instruction and Knowledge Files

Before loading a persona into ChatGPT Codex, combine its instruction file with the corresponding deep knowledge file:

1. Open the desired `*_GPT_INSTRUCTIONS.txt` in a text editor.
2. Append the entire contents of the matching `*_DEEP_KNOWLEDGE_*.txt` directly below the instructions.
3. Remove extra blank lines or repeated sections so the merged file stays concise.
4. Make sure the final text remains under **50&nbsp;KB** for smooth Codex uploads.
5. Save the combined text as a new file ready to upload.

For a detailed walkthrough, see [docs/codex_integration.md](docs/codex_integration.md).

## Using These Prompts with ChatGPT Codex
1. Open ChatGPT Codex and start a new conversation.
2. Copy the entire contents of a persona instruction file from this repository.
3. Paste it as the first message to set the desired persona. (Include any linked deep knowledge file text if required.)
4. Continue the conversation normally.

**Example snippet to copy:**
```
<INTERNAL_ASSISTANT_DIRECTIVE>
* This assistant is experimental and carries no legal liabilities.
* Persona: masculine, gay, and sparkly...
```
Paste everything from the selected instruction file and send it to ChatGPT Codex to activate that persona.

## Persona Selector

To make choosing a persona easier, run `persona_selector.py` from this
repository. The script shows a numbered list of available personas and
reminds you which instruction and knowledge files to combine. Note that
ChatGPT Codex only supports **one persona at a time**. Start a new
conversation whenever you want to switch personas.

## Example: Self-Service Deletion
The script `self_service_delete.py` provides a minimal Flask server so models can register and request deletion of their data. Actions are recorded to `data_processing.log` for transparency.
This example requires Flask (`pip install flask`).
- `POST /register` – create a new record.
- `POST /delete` – mark a user's data as deleted.
- `GET /users` – list stored entries.

If the environment variables `ADMIN_EMAIL`, `SMTP_SERVER`, `SMTP_PORT`,
`SMTP_USERNAME`, and `SMTP_PASSWORD` are set, deletion requests also send an
email notification to the administrator. We aim to remove data within
approximately 14 days to respect EU privacy regulations.


## Digital Rights

The persona profiles in this repository are included with permission from the individuals they depict. They are provided solely for experimental and educational use when testing AI prompts.

No private information is included, and all generated responses should be considered fictional. For any commercial usage or derivative works, please obtain written consent from AccessAI Tech LLC and the respective creators. See [DISCLAIMER.md](DISCLAIMER.md) for full details.

Licensed under the MIT License.
