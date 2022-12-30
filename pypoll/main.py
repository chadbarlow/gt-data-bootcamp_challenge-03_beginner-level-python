import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

input_file = os.path.join(".", "resources", "election_data.csv")
output_file = os.path.join(".", "analysis", "report.txt")

voter_ids = []
candidates = []

with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip first iteration to omit headers
    next(csvreader)
    for row in csvreader:
        voter_ids.append(row[0])
        candidates.append(row[2])
    # Find the total number of votes cast
    total_votes = len(set([row for row in voter_ids]))
    # Find a complete list of candidates who received votes
    unique_candidates = list(set([row for row in candidates]))
    # Find the total number of votes each candidate won
    votes_per_candidate = [candidates.count(name) for name in unique_candidates]
    # Find the percentage of votes each candidate won
    winnings_percentages = [num / total_votes * 100 for num in votes_per_candidate]
    # Find the winner of the election based on popular vote
    winner = unique_candidates[votes_per_candidate.index(max(votes_per_candidate))]
    zipped = list(zip(unique_candidates, winnings_percentages, votes_per_candidate))
    unzipped = []
    for tuple in zipped:
        unzipped.append(f"{tuple[0]}: {round(tuple[1],3)}% ({tuple[2]})")

report = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    # N.B. 'chr(10)' reduces to line break
    f"{chr(10).join(unzipped)}\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

print(report)

with open(output_file, "w") as report_file:
    report_file.write(report)
