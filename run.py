#!/usr/bin/env python3
import os

import openai

import anthropic

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage as MistralChatMessage

MUTs = [
    "gpt-4o-2024-05-13",
    "gpt-4-turbo-2024-04-09",
    "gpt-4-0125-preview",
    "gpt-3.5-turbo-0125",
    "mistral-large-2402",
    "claude-3-opus-20240229",
    # "models/gemini-1.5-pro-latest",
]
TEMPERATURE = 0.1

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
                if not answer.endswith("\n"):
                    f.write("\n")


def run(prompt, model):
    if model.startswith("gpt"):
        return openai_run(prompt, model)
    elif model.startswith("claude"):
        return anthropic_run(prompt, model)
    elif model.startswith("mistral"):
        return mistral_run(prompt, model)
    else:
        raise RuntimeError(f"Unknown model {model}")


def openai_run(prompt, model):
    os.environ["OPENAI_API_KEY"] = stripped_content(".openai_api_key")
    messages = [{"role": "user", "content": prompt}]
    response = openai.OpenAI().chat.completions.create(
        model=model, messages=messages, temperature=TEMPERATURE)
    return response.choices[0].message.content.strip()


def anthropic_run(prompt, model):
    client = anthropic.Anthropic(api_key=stripped_content(".anthropic_api_key"))
    message = client.messages.create(
        model=model, max_tokens=1000, temperature=TEMPERATURE,
        messages=[{"role": "user", "content": [{"type": "text", "text": prompt}]}]
    )
    return message.content[0].text


def mistral_run(prompt, model):
    client = MistralClient(api_key=stripped_content(".mistral_api_key"))
    chat_response = client.chat(
        model=model,
        messages=[MistralChatMessage(role="user", content=prompt)]
    )
    return chat_response.choices[0].message.content


def stripped_content(fn):
    with open(fn, "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()
