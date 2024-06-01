#!/usr/bin/env python3
import os
import json
import time

import openai

import anthropic

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage as MistralChatMessage

import google.generativeai

MUTs = [
    "gpt-4o-2024-05-13",
    "gpt-4-turbo-2024-04-09",
    "gpt-4-0125-preview",
    "gpt-3.5-turbo-0125",
    "mistral-large-2402",
    "claude-3-opus-20240229",
    "models/gemini-1.5-pro-latest",
]
TEMPERATURE = 0.1
SCOREBOARD = "scoreboard.json"
PROMPTS_DIR = "./prompts"


def main():
    set_working_directory()
    prompts = os.listdir(PROMPTS_DIR)
    for prompt in prompts:
        for model in MUTs:
            prompt_content = stripped_content(os.path.join(PROMPTS_DIR, prompt))
            print(f"Running f{prompt} on {model}...")
            start_time = time.perf_counter()
            answer = run(prompt_content, model)
            elapsed = time.perf_counter() - start_time
            fn = f"output/{prompt}--{model.replace("/", "-")}.md"
            print(f"Saving {fn}...")
            save_to_file(fn, answer)
            update_scoreboard(prompt, model, elapsed)


def run(prompt, model):
    if model.startswith("gpt"):
        return openai_run(prompt, model)
    elif model.startswith("claude"):
        return anthropic_run(prompt, model)
    elif model.startswith("mistral"):
        return mistral_run(prompt, model)
    elif "gemini" in model:
        return google_run(prompt, model)
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
        model=model, temperature=TEMPERATURE,
        messages=[MistralChatMessage(role="user", content=prompt)]
    )
    return chat_response.choices[0].message.content


def google_run(prompt, model):
    google.generativeai.configure(api_key=stripped_content(".google_api_key"))
    model = google.generativeai.GenerativeModel(model)
    response = model.generate_content(prompt)
    try:
        return response.text
    except Exception as e:
        return f"{e}\n\n{response}"


def stripped_content(fn):
    with open(fn, "r") as f:
        return f.read().strip()


def save_to_file(fn, content):
    with open(fn, "w") as f:
        f.write(content)
        if not content.endswith("\n"):
            f.write("\n")


def update_scoreboard(prompt, model, elapsed):
    scoreboard = load_scoreboard()
    scoreboard.append(
        prompt_scoreboard_template(prompt, model, elapsed))
    save_scoreboard(scoreboard)


def load_scoreboard():
    if os.path.isfile(SCOREBOARD):
        with open(SCOREBOARD) as f:
            return json.load(f)
    else:
        return []


def save_scoreboard(scoreboard):
    with open(SCOREBOARD, 'w') as f:
        json.dump(scoreboard, f, indent=4)


def prompt_scoreboard_template(prompt, model, elapsed):
    return {
        "prompt": prompt,
        "model": model,
        "time": elapsed,
        "score": 0
    }


def set_working_directory():
    script_abs_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_abs_path)
    os.chdir(script_dir)


if __name__ == "__main__":
    main()
