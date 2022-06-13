# -*- coding: utf-8 -*-

import unittest
import mileage_data_processing
import os


class Test_create_visualisation_data(unittest.TestCase):
    ""
    
    def test_create_visualisation_data(self):
        """
        
        """
        
        with open('visualisation_data.csv','w') as f:
            f.write('')
        
        
        files=['mileagetestdata_spacemission.csv']
        
        cache_filename='cache.json'
        
        mileage_data_processing.create_visualisation_data(
            files,
            cache_filename=cache_filename
            )
    
    
        print('\n--- test_create_visualisation_data ---')
        print('\n- file starts -')
        for i, line in enumerate(open('visualisation_data.csv')):
            print(line)
            if i==3: break
    
    
    def test_using_command_line(self):
        """
        """
        
        import subprocess
        
        with open('visualisation_data.csv','w') as f:
            f.write('')
        
        subprocess.run(
            'python mileage_data_processing.py',
            )
        
        print('\n--- test_using_command_line ---')
        print('\n- file starts -')
        for i, line in enumerate(open('visualisation_data.csv')):
            print(line)
            if i==3: break
        
        
    def test_create_visualisation_data__all_files(self):
        """
        
        Takes approx 45 seconds.
        
        """
        return  # comment/delete this line to run this test
        
        csv_dir=os.path.join(os.pardir,'data')
        files=[os.path.join(csv_dir,file) for file in os.listdir(csv_dir)]
        
        cache_filename=os.path.join(os.pardir,'1_ves_api_request','csv_file_cache2.json')
        
        mileage_data_processing.create_visualisation_data(
            files,
            cache_filename=cache_filename,
            output_filename=os.path.join(os.pardir,'3_visualisation','visualisation_data.csv')
            )
    
        print('\n--- file starts---')
        for i, line in enumerate(open('visualisation_data2.csv')):
            print(line)
            if i==3: break
    
    
    
if __name__=='__main__':
    
    unittest.main(Test_create_visualisation_data())
    
    

# old code - to be deleted
# class Test_process_mileage_data(unittest.TestCase):
#     ""
    
#     def test_process_mileage_data_single_csv_file(self):
#         """
        
#         Takes approx 2 seconds
        
#         """
        
#         file=os.path.join(os.pardir,
#                           'data',
#                           'DW01.01.21_31.01.21.csv_pseudo.csv')
        
#         mileage_data_processing.process_mileage_data(
#             files=[file],
#             output_filename='processed_mileage_data_single_input_file.csv'
#             )
    
#         #print(result)
    
    
#     def test_process_mileage_data_multiple_csv_files(self):
#         """
        
#         Completes in approx 40 seconds
        
#         """
        
#         csv_dir=os.path.join(os.pardir,'data')
#         files=[os.path.join(csv_dir,file) for file in os.listdir(csv_dir)]
        
#         mileage_data_processing.process_mileage_data(
#             files=files,
#             output_filename='processed_mileage_data_multiple_input_files.csv'
#             )
    
    
# class Test_create_registration_number_data(unittest.TestCase):
#     ""
    
#     def test_create_registration_number_data(self):
#         """
#         """
#         cache_filename=os.path.join(os.pardir,'1_ves_api_request','csv_file_cache2.json')
#         mileage_data_processing.create_registration_number_data(
#             cache_filename
#             )
    
    
