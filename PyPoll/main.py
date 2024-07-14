'''
A program to analyzes election votes and calculate each of the following:
    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote.
    * Print the analysis to the terminal and a text file
'''

import os
import csv

# Name the file paths and names for read and write files
poll_data = os.path.join(".", "Resources", "election_data.csv")
election_results = "election_results.txt"

total = 0
candidates = {}

with open(poll_data, 'r', newline="") as results:
    csvreader = csv.reader(results, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if not row[2] in candidates:
            candidates[row[2]] = 1
        if row[2] in candidates:
            candidates[row[2]] += 1
        total += 1
    winning_count = 0
    winner = str

    # Step through candidate dictionary
    for candidate in candidates:
        if candidates[candidate] > winning_count:
            winning_count = candidates[candidate] 
            winner = candidate
    
    # Print election resuts to terminal
    print("\nElection Results\n" + \
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
    "-------------------------\n")
    f.close()
