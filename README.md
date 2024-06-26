# LLM engineering applications benchmark

Purpose of this repository is to compare various LLM's performance for engineering
applications. There are several prompts in the `prompts` directory in markdown
that are submitted to all LLM's and their output is stored in `output` directory
and manually evaluated with every answer getting a score between 0 and 10.

## Models

Models that are benchmarked are:

* `gpt-4o-2024-05-13`
* `gpt-4-turbo-2024-04-09`
* `gpt-4-0125-preview`
* `gpt-3.5-turbo-0125`
* `mistral-large-2402`
* `claude-3-opus-20240229`
* `models/gemini-1.5-pro-latest`

## Requirements

Get latest Python and `pip` and install required libraries:

```
 pip install --user --break-system-packages openai mistralai anthropic google-generativeai
```

Save your API keys to `.<NAME>_api_key`, where `<NAME>` is `openai`, `mistral`,
`anthropic`, and `google`.

## Running

Ouputs are generated by running `./run.py`. It will prepare `scoreboard.json`
where you should put your evaluation of results as numbers between 0 (useless result)
and 10 (excellent result).

## Evaluation

After filling your impressions in `scoreboard.json`, run `./eval.py` and it crete visualization
for either time or score.

## Results

You can see raw output of models in [`./output`](./output), check the [`scoreboard.json`](./scoreboard.json)
with my personal opinion. Here are visualizations for score and time:

![Evaluated score](https://raw.githubusercontent.com/ChaoticRoman/llm-eng-benchmark/master/eval_score.png)

![Evaluated time](https://raw.githubusercontent.com/ChaoticRoman/llm-eng-benchmark/master/eval_time.png)
