# -*- coding: utf-8 -*-

# This Python module contains the `request` function to request data from
#  the Vehicle Enquiry Service API.
#
# The module can also be run as a command line programme. In this case, 
#  files in the current working directory are used for the inputs and outputs: 
#  - registration numbers are imported from a JSON file named 'in.json' 
#  - the API key is imported from a JSON file named 'api_key.json'
#  - the cache is updated using a JSON file named 'cache.json'


import requests
import json
import sys


def request(registration_numbers,
            api_key,
            cache=None,
            url ='https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
            ):
    """Function to send requests to the Vehicle Enquiry Service API.
    
    The API is available here:
    https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html#vehicle-enquiry-service-api

    Each API call takes a few seconds, so a cache system is used to 
        avoid unneccessary duplicate API requests. The output from running
        this function can be used as the input cache when running it the 
        next time.   

    Arguments:
        - registration_numbers (list): A list of registration numbers,
            given as a list of strings.
        - api_key (str): The API key as provided as a part of the registration 
            for the Vehicle Enquiry Service API. 
        - cache (dict): A dictionary of previous results returned by this function.
            Optional, default is None (which is set as an empty dictionary).
        - url (str): The URL for the Vehicle Enquiry Service API.
            Default is the currently active URL.
        
    Returns:
        - (dict): An updated dictionary with any new API request results.
            The dictionary has keys as the registration number strings,
            and values as the JSON return values from the API requests.
            The dictionary values will be either the vehicle data if the request
            was successful or the reponse error message if the request
            was not successful.
            
        
    """
    if cache is None: cache={}
    
    for registration_number in registration_numbers:
        
        if not registration_number in cache:
            
            response = requests.post(url,
                                     headers={'x-api-key':api_key,
                                              "Content-Type":"application/json"},
                                     data=f'{{"registrationNumber": "{registration_number}"}}' 
                                    )
            
            cache[registration_number]=response.json()
    
    return cache

    
    
if __name__=='__main__':
    
    with open('in.json') as f:
        registration_numbers=json.load(f)
    
    with open('api_key.json') as f:
        api_key=json.load(f)
        
    try:
        with open('cache.json') as f:
            cache=json.load(f)
    except FileNotFoundError:
        cache={}
    
    cache=request(
        registration_numbers,
        api_key,
        cache=cache
        )
    
    with open('cache.json','w') as f:
        json.dump(cache,f,indent=4)
    
    sys.exit(0)
    
    
    
    