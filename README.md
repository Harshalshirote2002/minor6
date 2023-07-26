# minor6


1. Use the link: https://physionet.org/static/published-projects/big-ideas-glycemic-wearable/big-ideas-lab-glycemic-variability-and-wearable-device-data-1.1.1.zip to download the data as zip file.

2. Unzip the above file.

3. To extract data by time-stamp matching, run the commands:
cd data_generation (change the directory to data_generation)
python generate.py --Path_to_BVP_001.csv --path_to_Dexcom_001.csv --path_to_output_directory

4. the above command extracts data for patient number 1. use similar command to extract data for all 16 patients.

5. Refer CWT_generation.ipynb to generate CWT images
