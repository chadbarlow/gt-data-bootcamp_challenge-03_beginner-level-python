import os
import csv

input_file = os.path.join(".", "resources", "budget_data.csv")
output_file = os.path.join(".", "analysis", "report.txt")

all_data = []
dates = []
profits = []

with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        all_data.append(row)
        dates.append(row[0])
        profits.append(int(row[1]))
    # Find the total number of months included in the dataset
    total_months = len(set([row for row in dates]))
    # Find the net total amount of "Profit/Losses" over the entire period
    net_profit = sum([row for row in profits])
    # Find the changes in "Profit/Losses" over the entire period, and then the average of those changes
    profits_offset = profits.copy()[1:]
    all_changes = [item1 - item2 for (item1, item2) in zip(profits_offset, profits)]
    avg_change = sum(all_changes) / len(all_changes)
    # Find the greatest increase in profits (date and amount) over the entire period
    greatest_inc = max(all_changes)
    greatest_inc_month = dates[all_changes.index(greatest_inc) + 1]
    # Find the greatest decrease in profits (date and amount) over the entire period
    greatest_dec = min(all_changes)
    greatest_dec_month = dates[all_changes.index(greatest_dec) + 1]

report = (
    f"Financial Analysis\n----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit}\n"
    f"Average Change: ${round(avg_change,2)}\n"
    f"Greatest Increase in Profits: {greatest_inc_month} ${greatest_inc}\n"
    f"Greatest Decrease in Profits: {greatest_dec_month} ${greatest_dec}"
)

print(report)

with open(output_file, "w") as report_file:
    report_file.write(report)
