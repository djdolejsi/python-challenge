import os
import csv

csvpath = os.path.join('Resources/election_data.csv')

def voting_results(voting_data):
    voting_id = str(voting_data[0])
    county = str(voting_data[1])
    candidate = str(voting_data[2])

    total_votes = len(voting_id)
    candidate_name = len(candidate)
    candidate_votes = int(candidate.count(candidate))
    vote_percentage = (candidate_votes / total_votes) * 100
    winner = max(candidate_votes)

    print(f"Election Results")
    print(f"------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------------")
    print(f"{candidate_name}: {vote_percentage} ({candidate_votes})")
    print(f"------------------------------")
    print(f"Winner: {winner}")


with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        voting_results(row)