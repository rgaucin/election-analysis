# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

import csv
import os

# path to election results
results_path = os.path.join("Resources","election_results.csv")
# declare variable with path to election analysis
analysis_path = os.path.join("Analysis","election_analysis.txt")

# initialize total vote counter
total_votes = 0

# list to hold candidate options
candidate_options = []

# dictionary to hold the number of votes for each candidate
candidate_votes = {}

# list to hold county names
counties = []

# dictionary to hold the number of votes from each county
county_votes = {}

# track the winning candidate and vote info
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# track the county with the largest turnout and its number of votes
largest_county = ""
largest_turnout = 0

# open election results to perform analysis
with open(results_path, "r") as election_data:

    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:

        # add to the total vote count
        total_votes += 1

        # get county and candidate name from each row
        county_name = row[1]
        candidate_name = row[2]

        # add county to list of counties if not already there
        if county_name not in counties:
            counties.append(county_name)
            # begin tracking new county's votes
            county_votes[county_name] = 0 

        # add candidate name to list of options if not already there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking new candidate's votes
            candidate_votes[candidate_name] = 0

        # add a vote to the current county
        county_votes[county_name] += 1
        # add a vote to the current candidate's count
        candidate_votes[candidate_name] += 1

# open analysis file to write analysis
with open(analysis_path, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )

    # print total vote count to terminal
    print(election_results, end="")

    # write the total vote count to the analysis text file
    txt_file.write(election_results)

    # print to terminal and write to analysis a header for county turnout results
    print("County Votes:\n")
    txt_file.write("County Votes:\n")

    # loop through each county from the county dictionary
    for county in county_votes:

        # retrieve the county vote count
        vote_count = county_votes[county]

        # calculate the percentage of votes for the county
        county_percentage = float(vote_count) / float(total_votes) * 100

        # print county results to terminal and write to analysis text file
        county_results = (f"{county}: {county_percentage:.1f}% ({vote_count:,})\n")

        print(county_results)
        txt_file.write(county_results)

        # check if current county and vote count are the largest so far
        if vote_count > largest_turnout:
            largest_county = county
            largest_turnout = vote_count


    # print the turnout results to terminal
    turnout_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n"
    )

    print(turnout_results)

    # write the turnout results to analysis text file
    txt_file.write(turnout_results)

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

        # print the candidate's results to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # write the candidate's results to analysis text file
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )

    # print winning candidate to terminal
    print(winning_candidate_summary)
    # write winning candidate to analysis text file
    txt_file.write(winning_candidate_summary)
    