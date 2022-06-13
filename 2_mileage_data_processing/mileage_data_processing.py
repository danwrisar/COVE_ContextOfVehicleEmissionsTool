# -*- coding: utf-8 -*-

import csv
import json


def create_visualisation_data(
        files,
        cache_filename,
        output_filename='visualisation_data.csv'
        ):
    """Function to create the visualisation data .csv file.
    
    This merges:
        - one or more mileage .csv files
        - the registration number cache file created by the ves_api_request module.
        
    The output is a single (perhaps large) csv file which contains all the data
        ready to use in the visualisation Jupyter notebook.
    
    Arguments:
        - files (list): A list of .csv filenames.
        - cache_filename (str): A filename of the JSON cach file created by
            the ves_api_request module.
        - output_filename (str): A filename to save the output of this function to.
            Optional, default is 'visualisation_data.csv'
            
    Returns:
        - None
    
    """
    
    with open(cache_filename) as f:
        cache=json.load(f)
    
    # get unique mileage fieldnames
    mileage_fieldnames=set()
    for file in files:
        with open(file) as f:
            reader=csv.reader(f,delimiter=',')
            mileage_fieldnames.update(next(reader))
    
    #print(mileage_fieldnames)
    
    # get unique fieldnames in cache
    cache_fieldnames=set()
    for k,v in cache.items():
        cache_fieldnames.update(v.keys())
    cache_fieldnames.remove('errors')
    
    #print(cache_fieldnames)
    
    fieldnames=list(mileage_fieldnames) + list(cache_fieldnames)
    
    #print(fieldnames)
    
    with open(output_filename,'w', newline='') as f:
        
        writer=csv.DictWriter(f, fieldnames)
        
        writer.writeheader()
        
        for file in files:
            
            print(file)
            
            with open(file) as f1:
                
                reader=csv.DictReader(f1, delimiter=',')
                
                for row in reader:
                    
                    # get cache data for this row
                    d=row
                    regno=d['Registration']
                    cache_dict=cache.get(regno,{})
                    if not 'errors' in cache_dict:
                        d.update(cache_dict)
                    
                    writer.writerow(d)
        
        return None
        

if __name__=='__main__':
    
    
    import os
    import sys
    
    files=[file for file in os.listdir() 
           if os.path.splitext(file)[1]=='.csv' and not file=='visualisation_data.csv']
    #print(files)
    
    create_visualisation_data(
        files,
        cache_filename='cache.json'
        )
    
    sys.exit(0)
    
        
        
# old code - to be deleted    
# def process_mileage_data(
#         files,
#         output_filename='processed_mileage_data.csv'
#         ):
#     """
#     """
    
#     # get fieldnames
#     with open(files[0]) as f:
#         reader=csv.reader(f, delimiter=',')
#         fieldnames=next(reader)
    
#     #print(fieldnames)
    
#     with open(output_filename,'w', newline='') as f:
        
#         writer=csv.DictWriter(f, fieldnames)
        
#         writer.writeheader()
    
#         for file in files:
            
#             with open(file) as f1:
                
#                 reader=csv.DictReader(f1, delimiter=',')
                
#                 for row in reader:
                    
#                     writer.writerow(row)
                    

# def create_registration_number_data(
#         cache_filename,
#         output_filename='registration_plate_data.csv'
#         ):
#     """
#     """
    
#     with open(cache_filename) as f:
#         cache=json.load(f)
        
#     # get unique fieldnames in cache
#     fieldnames=set()
#     for k,v in cache.items():
#         fieldnames.update(v.keys())
#     fieldnames.remove('errors')
        
    
#     with open(output_filename,'w', newline='') as f:
        
#         writer=csv.DictWriter(f, fieldnames)
        
#         writer.writeheader()
        
#         for k,v in cache.items():
            
#             if 'registrationNumber' in v:
            
#                 writer.writerow(v)
            
#             #break
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    