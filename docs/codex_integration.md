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
