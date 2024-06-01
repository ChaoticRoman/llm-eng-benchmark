#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
import numpy as np

with open("scoreboard.json") as f:
    data = json.load(f)

# Extract unique prompts and models
prompts = list(set(item['prompt'] for item in data))
models = list(set(item['model'] for item in data))

# Create a dictionary to store times for each prompt and model
times_dict = {prompt: {model: None for model in models} for prompt in prompts}

item_type = input("Compare score or time? ")

# Populate the dictionary with times
for item in data:
    times_dict[item['prompt']][item['model']] = item[item_type]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for each model
colors = plt.cm.viridis(np.linspace(0, 1, len(models)))

# Plot data for each model
for i, model in enumerate(models):
    times = [times_dict[prompt][model] for prompt in prompts]
    ax.plot(prompts, times, marker='o', label=model, color=colors[i])

# Customize the plot
ax.set_title('Comparison of Times for Various Models and Prompts')
ax.set_xlabel('Prompts')
ax.set_ylabel('Time (seconds)')
ax.legend(title='Models')
ax.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()
