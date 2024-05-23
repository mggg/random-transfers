# random-transfers
Replication code for random transfer experiments.

This project uses `poetry` (more info [here](https://python-poetry.org/)) to manage dependencies. After cloning the repository, run `poetry install` to install the necessary libraries. Then run `poetry shell` to activate virtual shell or use `poetry run python <python_file>` to run scripts. 

To replicate the experiments on Cambridge city council data, run `poetry run python experiments.py NUM_TRIALS YEAR-RANGE`. For example, to simulate 10,000 elections across the years 2003-2017, execute `poetry run python experiments.py 10000 2003-2017`. Similar simulations can be conducted on data from Cambridge school board elections using the `experiments_school.py` script.

Code used to pre-process elections data and create result visuals can be found in the `notebooks` folder. 
