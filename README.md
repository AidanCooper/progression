# Progression App Data Converter
Analyse data exports from the Progression Workout Tracker Android app.

1. Transfer your 'fws.json' file from `Android > data > workout.progression` to the repository directory.

2. To create and activate the environment, run `conda env create -f environment.yml` in the console, followed by `activate progression` (Windows) or `source activate progression` (macOS and Linux).

3. Run `Python read_data.py` in console to obtain a CSV file of the 'fws.json' input.

[The Jupyter notebook](example_analysis.ipynb) provides a starting point for analysis of the output file.
