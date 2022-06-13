# ves_api_request

This GitHub folder contains Python code to request data from the Vehicle Enquiry Service API.

## Overview

The Vehicle Enquiry Service API allows users to request the details of cars based on their registration numbers. 

The API is available here: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html#vehicle-enquiry-service-api

An API call is made by sending the registration number to the API service, which then returns either the car details or an error message.

The code provided here allows users to make these API calls using Python scripts. Each API call takes a few seconds, so a cache system is used to avoid unneccessary duplicate API requests. The output cache from running the code can be used as the input cache when running it the next time.  

## How to download

The files can be downloaded by navigating to the parent folder 'cove-project' and choosing the 'Download ZIP' option from the 'Code' button. Alternative the repository could be forked and/or cloned using Git.

## File available in this folder

- ves_api_request.py - a Python module which contains the `request` function. This function is used to make the API request to the Vehicle Enquiry Service.
- tests.py - a Python module with a series of Python unittests of the `request` function.
- in.json - a JSON file with a list of registration numbers used in the `tests.py` tests.
- cache.json - a JSON file containing a cache of registration numbers used in the `tests.py` tests.
- mileagetestdata_spacemission.csv - a csv file with a list of registration numbers used in the `tests.py` tests.
- cache_spacemission.json - a JSON file containing a cache of registration numbers used in the `tests.py` tests.
- README.md - a Markdown readme file (this file).


## The `request` function

This is the main function provided in this GitHib folder. The call signature is:

```Python
ves_api_request.request(registration_numbers, api_key, cache=cache)
```

This function sends and receives requests to the Vehicle Enquiry Service API.

It's arguments are:
- registration_numbers (list): A list of registration numbers,
    given as a list of strings.
- api_key (str): The API key as provided as a part of the registration 
    for the Vehicle Enquiry Service API. 
- cache (dict): A dictionary of previous results returned by this function.
    Optional, default is None (which is set as an empty dictionary).
- url (str): The URL for the Vehicle Enquiry Service API.
    Default is the currently active URL.

The function returns:
- (dict): An updated dictionary with any new API request results.
    The dictionary has keys as the registration number strings,
    and values as the JSON return values from the API requests.
    The dictionary values will be either the vehicle data if the request
    was successful or the reponse error message if the request
    was not successful. This dictionaru can be used as the cache for future calls if needed.
            

## Using the `request` function in a Python script

The `request` function can be used in a Python script as follows:

```Python
import ves_api_request
registration_numbers=['AA19AAA']
api_key="..."  # replace with your api key string
cache={}
result=ves_api_request.request(
    registration_numbers,
    api_key,
    cache=cache
    )
print(result)
```
This example code gives the following output:
```Python
{ 
    'AA19AAA':
    {
        'registrationNumber': 'AA19AAA', 
        'co2Emissions': 126, 
        'engineCapacity': 1332, 
        'euroStatus': 'EURO 6 DG', 
        'markedForExport': False, 
        'fuelType': 'PETROL', 
        'motStatus': 'No details held by DVLA', 
        'revenueWeight': 1945, 
        'colour': 'WHITE', 
        'make': 'MERCEDES-BENZ', 
        'typeApproval': 'M1', 
        'yearOfManufacture': 2019, 
        'taxDueDate': '2022-07-01', 
        'taxStatus': 'Taxed', 
        'dateOfLastV5CIssued': '2020-07-17', 
        'wheelplan': '2 AXLE RIGID BODY', 
        'monthOfFirstRegistration': '2019-07'
        }
}
```
For this to work, the `ves_api_request.py` module will need to be placed in the same local folder as the Python script, or to be included in the `sys.path` list.

## Using the `ves_api_request.py` module via the command prompt.

The module can also be run using the command prompt. In this case, files in the current working directory are used for the inputs and outputs: 
- the 'ves_api_request.py' file shold be placed in a local directory.
- registration numbers are imported from a JSON file named 'in.json' containing a list of registration umber strings (i.e. ["AA19AAA"]).
- the API key is imported from a JSON file named 'api_key.json' containing a string of the user's API key.
- the cache is updated using a JSON file named 'cache.json' containing a dictionary of previous (cached) results. This file is optional and if not provided then the cache is assumed to be empty.

The module is run by opening the command prompt, navigating to the directory with the files and then running the command:

```bash
python ves_api_request.py
```

A new or updated file named 'cache.json' is created.

See the `test_using_command_line` test in the `tests.py` module for more details.

Depending on the operating system the command `python` may need to be replaced with `python3`. If the Anaconda distribution has been installed for running Python, then this command is best run in the Anaconda Prompt.

