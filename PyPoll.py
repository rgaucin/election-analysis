# DATA TO RETRIEVE
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

import csv
import os

# declare variable with path to election results
results_path = os.path.join("Resources","election_results.csv")
# declare variable with path to election analysis
analysis_path = os.path.join("Analysis","election_analysis.txt")

# open election results to perform analysis
with open(results_path, "r") as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

# open analysis file to write analysis
with open(analysis_path, "w") as txt_file:
    
