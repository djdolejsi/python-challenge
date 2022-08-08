# Import dependencies
import os
import csv

# Create the path for the CSV file
csvpath = os.path.join('Resources/election_data.csv')

# Create the list to store your data
voting_id = []
county = []
candidates_all = []
candidate_condensed = []
votes_counter = []
voting_percent = []

# Open your CSV file using the path you created
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# identify the header in the data
    header = next(csvreader)

# Looking through the data and adding all of the data in the voting_id, county and candidates_all lists
    for row in csvreader:
        voting_id.append(row[0])
        county.append(row[1])
        candidates_all.append(row[2])

# Calculating the total votes
    total_votes = len(voting_id)

# Removed duplicates from the candidiate all list to get a list of all the unique candidates and putting that in the candidate_condensed list   
    for x in range(total_votes-1):
        if candidates_all[x+1] != candidates_all[x] and candidates_all[x+1] not in candidate_condensed:
            candidate_condensed.append(candidates_all[x+1])

# Find the unique votes to each candidate and voting percentage and adding them to the appropriate lists
    for i in range (len(candidate_condensed)):
        votes_counter.append(candidates_all.count(candidate_condensed[i]))
        voting_percent.append(round(((votes_counter[i] / total_votes) * 100), 3))

# Calculating who had the most votes in the election   
    most_votes = max(votes_counter)
    winner = candidate_condensed[votes_counter.index(most_votes)]

# Print the results of the election
    print(f"Election Results")
    print(f"------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------------")
    print(f"{candidate_condensed[0]}: {voting_percent[0]} ({votes_counter[0]})")
    print(f"{candidate_condensed[1]}: {voting_percent[1]} ({votes_counter[1]})")
    print(f"{candidate_condensed[2]}: {voting_percent[2]} ({votes_counter[2]})")
    print(f"------------------------------")
    print(f"Winner: {winner}")
    print(f"------------------------------")

# # Create a txt file with my results and export it
with open('analysis.txt', 'w' ) as datafile:
    datafile.write(f"Election Results \n")
    datafile.write(f"------------------------------ \n")
    datafile.write(f"Total Votes: {total_votes} \n")
    datafile.write(f"------------------------------ \n")
    datafile.write(f"{candidate_condensed[0]}: {voting_percent[0]} ({votes_counter[0]}) \n")
    datafile.write(f"{candidate_condensed[1]}: {voting_percent[1]} ({votes_counter[1]}) \n")
    datafile.write(f"{candidate_condensed[2]}: {voting_percent[2]} ({votes_counter[2]}) \n")
    datafile.write(f"------------------------------ \n")
    datafile.write(f"Winner: {winner} \n")
    datafile.write(f"------------------------------ \n")




