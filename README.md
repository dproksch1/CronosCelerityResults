# CronosCelerityResults

This repository contains performance evaluation results for the [CronosCelerity](https://github.com/philippgs/CronosCelerity) research project.

## Results

We performed our performance evaluation using the standalone operation mode of our [CronosCelerityBlock](https://github.com/dproksch1/CronosCelerityBlock) proxyapp, is functionally similar to the main **CronosCelerity** project but allows for easier recompilation due to its reduced codebase. The evaluation results are provided in the form of command line outputs during single-step Sedov explosion simulations with restricted asynchronicity, as described in the paper.

The directory `results_celerity` contains the outputs for the performance evaluations of our Celerity port. The names of the subdirectories represent the utilized 3-dimensional domain sizes.

The directories `results_seq` and `results_seq_block` contain performance evaluation results for the sequential versions of Cronos. The outputs in `results_seq` are generated using the publically avalaible Cronos codebase, while the outputs in `results_seq_block` are created using a sequential, unoptimized version of our algorithm.

## Performance Output Parser

We also provided the Python 3 script, that can be utilized to parse the output files and extract the evaluation results. The script does require the non-standard library *NumPy*. Use the `--help` flag to learn about optional and required input parameters.

To correctly parse the results in the `results_celerity` directory, use the `--fix` flag. Parsing the results of both sequential evaluations does not require this flag and utilization will lead to wrong results.

## Context

This project was created as part of a master's thesis by Daniel Proksch at the University of Innbruck. The thesis and project were supervised by Phillip Gschwandtner.