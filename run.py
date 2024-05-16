#!/usr/bin/env python3
import os

import openai

MUTs = [
    "gpt-4o-2024-05-13",
    "gpt-4-turbo-2024-04-09",
    "gpt-4-0125-preview",
    "gpt-3.5-turbo-0125",
    # "mistral-large-2402",
    # "claude-3-opus-20240229",
    # "models/gemini-1.5-pro-latest",
]


def main():
    # Change working directory to script's directory
    script_abs_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_abs_path)
    os.chdir(script_dir)

    prompts = os.listdir("./prompts")

    for prompt in prompts:
        for model in MUTs:
            answer = run(prompt, model)
            fn = f"output/{prompt}--{model}.md"
            print(fn)
            with open(fn, "w") as f:
                f.write(answer)


def run(p, m):
    if m.startswith("gpt"):
        return openai_run(p, m)
    else:
        raise RuntimeError(f"Unknown model {m}")


def openai_run(p, m):
    return ""


if __name__ == "__main__":
    main()
