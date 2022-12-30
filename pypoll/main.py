# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

input_file = os.path.join(".", "resources", "election_data.csv")
output_file = os.path.join(".", "analysis", "report.txt")

voter_ids = []
candidates = []

with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        voter_ids.append(row[0])
        candidates.append(row[2])

    total_votes = len(set([row for row in voter_ids]))
    unique_candidates = list(set([row for row in candidates]))
    totals = [candidates.count(name) for name in unique_candidates]
    percentages = [number / total_votes * 100 for number in totals]
    data = list(zip(unique_candidates, percentages, totals))
    winner = unique_candidates[totals.index(max(totals))]
    thing = []
    for tuple in data:
        thing.append(f"{tuple[0]}: {round(tuple[1],2)}% ({tuple[2]})")

report = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{chr(10).join(thing)}\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

print(report)

with open(output_file, "w") as report_file:
    report_file.write(report)
