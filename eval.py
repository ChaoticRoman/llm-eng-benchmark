#!/usr/bin/env python3
import json
import sys

import matplotlib.pyplot as plt

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

def average(model):
    values = [
        data_dict[prompt][model] for prompt in prompts
        if prompt in data_dict and model in data_dict[prompt]
    ]
    return sum(values) / len(values)

# Get average values per model
averages_per_model = {m: average(m) for m in models}

# Sort prompts and models for consistent ordering
prompts.sort()
models.sort(key=lambda model: average(model))
print(models)

# Plotting
fig, ax = plt.subplots()
plt.grid()

bar_width = 0.1
index = range(len(prompts))
bar_positions = {model: [i + bar_width * idx for i in index] for idx, model in enumerate(models)}

for model in models:
    values = [data_dict[prompt][model] for prompt in prompts]
    ax.bar(bar_positions[model], values, bar_width, label=model)

# Set labels and title
ax.set_xlabel('Prompts')
ax.set_ylabel(metric.capitalize())
ax.set_title(f'{metric.capitalize()} by Prompt and Model')
ax.set_xticks([i + bar_width for i in index])
ax.set_xticklabels(prompts)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()