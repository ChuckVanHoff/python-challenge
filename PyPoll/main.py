# A program to analyzes election votes and calculate each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

#   * Print the analysis to the terminal and a text file

import os
import csv

# Name the file paths and names for read and write files
poll_data = os.path.join("..", "Resources", "election_data.csv")
election_results = "election_results.txt"

# Open the read file
with open(poll_data, 'r', newline="") as results:
    csvreader = csv.reader(results, delimiter=",")

    # Step past the header
    next(csvreader)

    # Variables to hole vote total and candidate names and vote counts
    total = 0
    candidates = {}
    
    # Step though the remaining rows
    for row in csvreader:
        
        # If this row has the first instance of a candidate's name, put it in the dictionary
        if not row[2] in candidates:
        
            # This adds an entry to the dictionary and sets its value to 1
            candidates[row[2]] = 1
        
        # If this row has a repeated entry of the candidate's name add it to the dicitonary
        if row[2] in candidates:
            candidates[row[2]] += 1
        # Add one to the total vote count
        total += 1

    # Variables for the winning vote count and winner name
    winning_count = 0
    winner = str

    # Step through candidate dictionary
    for candidate in candidates:

        # Find the winner and the vote count
        if candidates[candidate] > winning_count:
            winning_count = candidates[candidate] 
            winner = candidate
    
    # Print election resuts to terminal
    print("Election Results\n" + \
    "-------------------------" + "\n" + \
    f"Total Votes: {total}" + "\n" + \
    "-------------------------" + "\n")

    for candidate in candidates:
        print(f"{candidate}: {candidates[candidate]/total:.1%} ({candidates[candidate]})")
        
    print("-------------------------" + "\n" + \
    "Winner: " + winner + "\n" + \
    "-------------------------")

    # Print to text file
    f = open(election_results,"a+")
    f.write("Election Results\n" + \
    "-------------------------" + "\n" + \
    f"Total Votes: {total}" + "\n" + \
    "-------------------------" + "\n")

    for candidate in candidates:
        f.write(f"{candidate}: {candidates[candidate]/total:.1%} ({candidates[candidate]})")

    f.write("-------------------------" + "\n" + \
    "Winner: " + winner + "\n" + \
    "-------------------------")
    f.close()