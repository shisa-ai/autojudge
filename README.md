# AutoJudge

AutoJudge is an optimized LLM-as-a-Judge eval implementation.

* Simpler and more intuitive execution.

* Runs completely standalone for use with scripted evals (eg, run after training)

* Internal Database/Queue for resuming runs (useful when paying by the token)

* High performance - vLLM with HF fallback with batching

* Config support organized by evals, judges, and results (organized by runs, no overwriting of your results, easy PRs)

## Install

To install the required dependencies, run:

```sh
pip install packaging
pip install -r requirements.txt
```

To install the optional dependencies, run:

```sh
pip install -r requirements-optional.txt
```

## Usage
```sh
autojudge evaluate --model <model-path> --dataset <dataset-path> --output <output-path> --user <user>
```

```
autojudge config
```

## Development

To set up the development environment, run:

```sh
pip install -e .[dev]
```

## TODO

Tests: 
* LLM-as-a-Judge Reliability Testing
  * Sample 10% and run 10X
  * Calculate violin graph of distribution
* PoLL
