#!/usr/bin/env python3
import json
import sys

import matplotlib.pyplot as plt

ZERO_SCORE_ANSWERS_AFFECT_AVERAGE_SCORE = False

with open("scoreboard.json") as f:
    data = json.load(f)

# Command-line argument to choose between 'time' and 'score'
if len(sys.argv) != 2 or sys.argv[1] not in ['time', 'score']:
    print("Usage: python script.py <time|score>")
    sys.exit(1)

metric = sys.argv[1]

# Extract unique prompts and models
prompts = list(set(item['prompt'] for item in data))
models = list(set(item['model'] for item in data))

# Prepare data for plotting
data_dict = {prompt: {model: None for model in models} for prompt in prompts}
for item in data:
    data_dict[item['prompt']][item['model']] = item[metric]


def result_is_present(model, prompt):
    return prompt in data_dict and model in data_dict[prompt]


def include_result(model, prompt):
    return (
        result_is_present(model, prompt)
        and (
            ZERO_SCORE_ANSWERS_AFFECT_AVERAGE_SCORE
            or data_dict[prompt][model] != 0
        )
    )


def average(model):
    values = [data_dict[prompt][model] for prompt in prompts
              if include_result(model, prompt)]
    return sum(values) / len(values)


# Get average values per model
averages_per_model = {m: average(m) for m in models}

# Sort prompts and models for consistent ordering
prompts.sort()
models.sort(key=lambda model: average(model))

# Plotting
fig, ax = plt.subplots()
plt.grid()

bar_width = 0.1  # TODO: bar_width * number_of_models is supposed to be slightly less than one
prompt_indices = range(len(prompts))
bar_positions = {
    model: [prompt_i + bar_width * model_i for prompt_i in prompt_indices]
    for model_i, _ in enumerate(models)
}

for model in models:
    values = [data_dict[prompt][model] for prompt in prompts]
    ax.bar(bar_positions[model], values, bar_width, label=model)

# Set labels and title
ax.set_xlabel('Prompts')
ax.set_ylabel(metric.capitalize())
ax.set_title(f'{metric.capitalize()} by Prompt and Model')
ax.set_xticks([i + bar_width for i in prompt_indices])
ax.set_xticklabels(prompts)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()