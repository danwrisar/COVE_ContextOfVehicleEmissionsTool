# -*- coding: utf-8 -*-

import unittest
import json

# Gets the api_key recorded in the api_key.txt file.
# If the api_key.txt file does not exist then it needs to be created by the user.
# The file is a standard text file, with a single line with the api key.
with open('api_key.json') as f:
    api_key=json.load(f)
    

class Test_ves_api_request(unittest.TestCase):
    ""
    
    def test_using_import(self):
        """This test uses a Python import of the `request` function.
        A single registration plate is requested.
        No cache is used.
        
        """
        import ves_api_request
        registration_numbers=['AA19AAA']
        cache={}
        result=ves_api_request.request(
            registration_numbers,
            api_key,
            cache=cache
            )
        self.assertEqual(
            result,
            {'AA19AAA':
                {'registrationNumber': 'AA19AAA', 
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
            )
            
            
    def test_using_import_from_csv(self):
        """This test uses a Python import of the `request` function.
        
        Based on the example csv file named 'mileagetestdata_spacemission.csv'.
        
        No cache is used.
        
        """
        import ves_api_request
        import csv
        import json
        
        # loads an existing csv file with a 'Registration' column for the number plates    
        #  will need modifying for other use cases
        with open('mileagetestdata_spacemission.csv') as f:
            reader=csv.DictReader(f, delimiter=',')
            registration_numbers=set([row['Registration'] for row in reader])
        
        cache={}
        result=ves_api_request.request(
            registration_numbers,
            api_key,
            cache=cache
            )
        
        with open('cache_spacemission.json', 'w') as f:
            json.dump(result,f,indent=4)
        
        self.assertEqual(
            result,
            {
                "E063JUW": {
                    "errors": [
                        {
                            "status": "404",
                            "code": "404",
                            "title": "Vehicle Not Found",
                            "detail": "Record for vehicle not found"
                        }
                    ]
                },
                "BF66YMO": {
                    "registrationNumber": "BF66YMO",
                    "co2Emissions": 120,
                    "engineCapacity": 1398,
                    "markedForExport": False,
                    "fuelType": "PETROL",
                    "motStatus": "Valid",
                    "colour": "BLUE",
                    "make": "VAUXHALL",
                    "typeApproval": "M1",
                    "yearOfManufacture": 2016,
                    "taxDueDate": "2022-12-01",
                    "taxStatus": "Taxed",
                    "dateOfLastV5CIssued": "2019-10-25",
                    "motExpiryDate": "2022-12-06",
                    "wheelplan": "2 AXLE RIGID BODY",
                    "monthOfFirstRegistration": "2016-12"
                },
                "BF66YM0": {
                    "errors": [
                        {
                            "status": "400",
                            "code": "400",
                            "title": "Bad Request",
                            "detail": "Invalid format for field - vehicle registration number"
                        }
                    ]
                }
            }
            )
        
        
    def test_using_command_line(self):
        """This test uses the command line to run the `ves_api_request.py` module.
        A single registration plate is requested.
        No cache is used.
        
        A file named `api_key.json` which contains the API key is required in 
         local directory for this test to run.
        
        """
        import subprocess
        
        with open('cache.json','w') as f:
            json.dump({},f)
        
        subprocess.run(
            'python ves_api_request.py',
            )
        
        with open('cache.json') as f:
            answer=json.load(f)
        
        self.assertEqual(
            answer,
            {'AA19AAA':
                {'registrationNumber': 'AA19AAA', 
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
            )
    
    
    def test_using_import_on_csv_file(self):
        """This test uses a csv file with 1,998 unique registration plates.
        If the cache file is empty, it takes around 6 minutes to run.
        The completed cache file, with 1,998 registration plates, is around 1.5MB.
        
        This requires a .csv file in a 'Data' directory with a 'Registration' column.
        
        """
        return  # comment/delete this line to run this test
        
        import ves_api_request
        import os
        import csv
        
        # loads an existing cache file
        with open('csv_file_cache.json') as f:
            cache=json.load(f)

        #print(len(cache))
        
        # loads an existing csv file with a 'Registration' column for the number plates    
        #  will need modifying for other use cases
        with open(os.path.join(os.pardir,
                               'data',
                               'DW01.01.21_31.01.21.csv_pseudo.csv')) as f:
            reader=csv.DictReader(f, delimiter=',')
            registration_numbers=set([row['Registration'] for row in reader])
        #print(len(registration_numbers))
        #print(registration_numbers)
        
        # runs the request function
        updated_cache=ves_api_request.request(
            registration_numbers,
            api_key,
            cache=cache
            )
        
        # saves the updated cache, replacing the original cache file
        with open('csv_file_cache.json', 'w') as f:
            json.dump(updated_cache,f,indent=4)
        
                
    
    def xtest_using_import_on_multiple_csv_file(self):
        """This test uses multiple csv files.
        If the cache file is based on the single csv file test above, 
            then this test takes around 8 minutes to run.
        The completed cache file is around 2.7MB.
        
        This requires the .csv files in a 'Data' directory with a 'Registration' column.
        
        """
        return  # comment/delete this line to run this test
        
        import ves_api_request
        import os
        import csv
        
        # loads an existing cache file
        with open('csv_file_cache2.json') as f:
            cache=json.load(f)

        #print(len(cache))
        
        # loads an existing csv file with a 'Registration' column for the number plates  
        #  will need modifying for other use cases
        csv_dir=os.path.join(os.pardir,'data')
        for file in os.listdir(csv_dir):
            
            print(file)
        
            with open(os.path.join(csv_dir,file)) as f:
                reader=csv.DictReader(f, delimiter=',')
                registration_numbers=set([row['Registration'] for row in reader])
            #print(len(registration_numbers))
            #print(registration_numbers)
            
            # runs the request function
            cache=ves_api_request.request(
                registration_numbers,
                api_key,
                cache=cache
                )
        
        # saves the updated cache, replacing the original cache file
        with open('csv_file_cache2.json', 'w') as f:
            json.dump(cache,f,indent=4)
    
        
        
    
if __name__=='__main__':
    
    unittest.main()
