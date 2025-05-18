#!/usr/bin/env python3
"""Simple Persona Selector for GPT FRENZY."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = [BASE_DIR, os.path.join(BASE_DIR, "personas")]


def find_file(filename: str) -> str | None:
    """Return the first path that exists for ``filename``.

    The function checks both the script directory and a ``personas``
    subdirectory so the script works whether the persona files are in
    the repository folder structure or placed alongside the script in a
    custom GPT environment.
    """
    for d in SEARCH_DIRS:
        candidate = os.path.join(d, filename)
        if os.path.exists(candidate):
            return candidate
    return None

PERSONAS = {
    "1": ("BLCKBUTTERFLY", "!!!ATTENTION_READ_ALL!!!_BLCKBUTTERFLY_GPT_INSTRUCTIONS.txt", "!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_BLCKBUTTERFLY.txt"),
    "2": ("Company", "!!!ATTENTION_READ_ALL!!!_COMPANY_GPT_INSTRUCTIONS.txt", "!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_COMPANY.txt"),
    "3": ("Mimi", "!!!ATTENTION_READ_ALL!!!_MIMI_GPT_INSTRUCTIONS.txt", "!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_MIMI.txt"),
    "4": ("Supernova", "!!!ATTENTION_READ_ALL!!!_supernova_GPT_INSTRUCTIONS.txt", "!!!ATTENTION_READ_ALL!!!_DEEP_KNOWLEDGE_supernova.txt"),
}

MENU = "\n".join(f"{key}. {val[0]}" for key, val in PERSONAS.items())

def main():
    print("Persona Selector\n")
    print(MENU)
    choice = input("Choose a persona number: ").strip()
    persona = PERSONAS.get(choice)
    if not persona:
        print("Invalid choice.")
        return
    name, instr, knowledge = persona
    instr_path = find_file(instr)
    knowledge_path = find_file(knowledge)
    if not (instr_path and knowledge_path):
        print("Instruction or knowledge file not found.")
        return
    print(f"\nTo activate the {name} persona:")
    print(f"1. Open {instr_path}")
    print(f"2. Append the contents of {knowledge_path}")
    print("3. Upload the combined text to ChatGPT Codex and start your conversation.")
    print("\nNote: Only one persona can be active at a time.")

if __name__ == "__main__":
    main()
