# Loading Instruction Files into ChatGPT Codex

The new ChatGPT Codex interface lets you upload a small instruction file that guides the model. Follow these steps:

1. **Create your instruction file** – Save your custom instructions in a text-based format such as Markdown or plain text. Keep the file brief to ensure quick loading.
2. **Open ChatGPT Codex** – In the ChatGPT side panel, select the Codex option to open the upload interface.
3. **Upload your file** – Use the file picker to select the instruction file. The contents will appear in the editor for review.
4. **Start chatting** – Once the file is loaded, send a message to begin. The instructions will guide the assistant's behavior.

## Sample Codex JSON

Below is an example message payload in the new Codex format. The `system` message contains the uploaded instructions.
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant. Follow the company style guide and keep responses brief."
    },
    {
      "role": "user",
      "content": "How do I apply to be a model?"
    }
  ]
}
```

## Merging Persona Prompts with Deep Knowledge

Some personas in this repository have a corresponding `DEEP_KNOWLEDGE` file that expands on the tone, vocabulary, and backstory. Before uploading to Codex, merge the persona prompt with its knowledge file so the assistant has the full context.

1. Open the desired `GPT_INSTRUCTIONS.txt` file.
2. Append the entire contents of the matching `DEEP_KNOWLEDGE_*.txt` file beneath the instructions.
3. Save the combined text as a single file and upload that file to Codex.

### Sample Combined Message

Below is an abbreviated example showing how a merged instruction set might appear inside a Codex payload.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "<INTERNAL_ASSISTANT_DIRECTIVE> Persona rules here... </INTERNAL_ASSISTANT_DIRECTIVE>\n\n#CORE IDENTITY\nDetails from the deep knowledge file..."
    },
    {
      "role": "user",
      "content": "Describe the brand vision in two sentences."
    }
  ]
}
```

### Tips for Staying Within Codex Upload Limits

- Codex accepts relatively small files (roughly under 50&nbsp;KB). Keep your merged file concise so it loads quickly.
- Remove unnecessary blank lines, comments, or duplicate sections before uploading.
- Focus on the most important instructions and knowledge to stay well within the limit.
