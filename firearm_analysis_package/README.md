# Firearm Analysis Package

This package provides tools for analyzing and visualizing firearm data in the United States
from the followig source:
https://www.kaggle.com/datasets/pedropereira94/nics-firearm-background-checks

Population of the United States has been considered from the following source:
https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/us-state-populations.csv

## Structure of the project

- `data/`: Contains the CSV and JSON data.
- `firearm_analysis/`: Contains the modules to process, visualize, state analysis and map generation of the data
- `tests/`: Tests files for each module.
- `main.py`: File to execute the analysis.
- `LICENSE.txt`: License of the project.
- `requirements.txt`: Project dependencies.

## Modules

- `data_processing.py`: Functions for reading, cleaning, and processing firearm data.
- `visualization.py`: Functions for visualizing the temporal evolution of firearm data.
- `state_analysis.py`: Functions for calculating firearm percentages by state.
- `map_generation.py`: Functions for generating choropleth maps based on firearm data.

## Installation

1 - Clone the repository
```bash
git clone https://github.com/Diego-58/firearm_analysis_package
cd firearm_analysis
```
2 - Install dependencies
```bash
pip install -r requirements.txt
```
