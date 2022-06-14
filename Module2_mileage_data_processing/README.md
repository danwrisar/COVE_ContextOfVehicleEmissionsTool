# mileage_data_processing

This GitHub folder contains Python code to create the visualisation data .csv file.

## Overview

Here it is assumed that we have the following files:
- one or more mileage .csv files which contain the registration numbers in a 'Registration' column.
- the cache .json file as output by the `ves_api_request.py` module. The cache file has been generated using the registraion numbers in the .csv files.

Before doing further data analysis and visualistion on this data, it is useful to merge these files into a single .csv file. 

This is done in the `mileage_data_processing.py` module in this folder.

## How to download

The files can be downloaded by navigating to the parent folder 'cove-project' and choosing the 'Download ZIP' option from the 'Code' button. Alternative the repository could be forked and/or cloned using Git.

## File available in this folder

- mileage_data_processing.py - a Python module which contains the `create_visualisation_data` function. This function is used to create the output .csv file based on the mileage .csv files and the registration number cache .json file.
- tests.py - a Python module with a series of Python unittests of the `create_visualisation_data` function.
- mileagetestdata_spacemission.csv - a csv file with a list of registration numbers used in the `tests.py` tests.
- cache.json - a JSON file containing a cache of registration numbers used in the `tests.py` tests.
- visualisation_data.csv - a csv file which is the output of the tests in `tests.py`.
- README.md - a Markdown readme file (this file).

## The `create_visualisation_data` function

This is the main function provided in this GitHib folder. The call signature is:

```Python
create_visualisation_data(files, cache_filename, output_filename='visualisation_data.csv')
```

This function creates the visualisation data .csv file by merging:
- one or more mileage .csv files
- the registration number cache file created by the ves_api_request module.
    
The output is a single (perhaps large) csv file which contains all the data ready to use in the visualisation Jupyter notebook.

The arguments are:
- files (list): A list of .csv filenames.
- cache_filename (str): A filename of the JSON cach file created by the ves_api_request module.
- output_filename (str): A filename to save the output of this function to. Optional, default is 'visualisation_data.csv'
        
The function has no return value (i.e. returns `None`).            

## Using the `request` function in a Python script

The `request` function can be used in a Python script as follows:

```Python
import mileage_data_processing

files=['mileagetestdata_spacemission.csv']  # modify to your own list of mileage csv filenames.
        
cache_filename='cache.json'  # modify to your registration number cache .json filename.
        
mileage_data_processing.create_visualisation_data(
    files,
    cache_filename=cache_filename
    )
```
This example code will merge all the .csv files, insert the data form the cache.json file, and save the entire data in a single .csv file named 'visualisation_data.csv'.

For this to work, the `mileage_data_processing.py` module will need to be placed in the same local folder as the Python script, or to be included in the `sys.path` list.

## Using the `mileage_data_processing.py` module via the command prompt.

The module can also be run using the command prompt. In this case, files in the current working directory are used for the inputs and outputs: 
- the 'mileage_data_processing.py' file shold be placed in a local directory.
- the input mileage .csv files are read as all .csv files stored in the local directory. The filename 'visualisation_data.csv' is ignored.
- the registration number cache file is imported from a JSON file named 'cache.json'.
- the output is a new file named 'visualisation_data.csv' which is saved in the local directory.

The module is run by opening the command prompt, navigating to the directory with the files and then running the command:

```bash
python mileage_data_processing.py
```

A new file named 'visualisation_data.csv' is created.

See the `test_using_command_line` test in the `tests.py` module for more details.

Depending on the operating system the command `python` may need to be replaced with `python3`. If the Anaconda distribution has been installed for running Python, then this command is best run in the Anaconda Prompt.

