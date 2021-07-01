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

# initialize total vote counter
total_votes = 0

# declare list to hold candidate options
candidate_options = []

# declare dictionary to hold the number of votes for each candidate
candidate_votes = {}

# declare variables to track the winning candidate and vote info
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open election results to perform analysis
with open(results_path, "r") as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:

        # add to the total vote count
        total_votes += 1

        # get the candidate name from each row
        candidate_name = row[2]

        # add candidate name to list of options if not already there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking new candidate's votes
            candidate_votes[candidate_name] = 0

        # add a vote to the current candidate's count
        candidate_votes[candidate_name] += 1

# calculate the vote percentage for each candidate
for candidate_name in candidate_votes:
    # get the number of votes
    votes = candidate_votes[candidate_name]
    # calculate the percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    # determine if current vote count is greater than current winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # set winning variables to current vote count, percentage, and candidate name
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    # print out the percentage rounded to 1 decimal place
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)

print(winning_candidate_summary)

# open analysis file to write analysis
#with open(analysis_path, "w") as txt_file:
