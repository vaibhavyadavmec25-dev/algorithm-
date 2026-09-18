# Flexible Job Shop Scheduling (FJSP)

Complete Algorithms assignment implementation.

## Pipeline
Random generator -> candidate schedule -> independent validator -> metrics -> experiments -> failure analysis.

## Structure
fjsp/ contains generator, validator, algorithm, metrics, model, experiment, edge_cases and CLI.
tests/ contains pipeline tests.
instances/ and results/ contain reproducible experiment data.
analysis/REPORT.md contains the technical report.

## Run
python run_pipeline.py
python -m unittest discover -s tests -v

The generator records seed and parameters for reproducibility.
