# GPTFrenzy Repository

This repository contains persona instructions and knowledge files used for GPT experiments.

## Directory Layout

- `personas/` – Contains GPT instruction files and public persona references.
- `knowledge/` – Contains deep knowledge reference files.
- `RESOURCE.txt` – Additional resource list.
- `websiteinfo.txt` – Summary of website information.

## Using Filenames with Special Characters

Some filenames include exclamation points (`!`) and spaces. When referencing these files from the command line, enclose the name in single quotes or escape the special characters. For example:

```bash
# Access a persona file
cat 'personas/!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt'

# Access a deep knowledge file
cat 'knowledge/!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_MIMI.txt'
```

Alternatively, you can escape each exclamation mark with a backslash (`\!`) if your shell interprets `!` specially.
