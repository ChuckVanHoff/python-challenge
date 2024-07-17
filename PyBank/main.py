''' PnL data processing: DataBootCamp Homework 3 '''

import os
import csv
import sys

# Input and output data files
budget_data_csv = "Resources/budget_data.csv"
analysis = "Resources/financial_analysis.txt"

# lists and other variables to be initialized 
monthly_pnl = []
month = []
net_pnl = 0
change = float  # monthly_change values
monthly_change = []

# Process the lines of PnL data
with open(budget_data_csv, 'r', newline="") as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)
    lines = budgetfile.readlines()
    for row in lines:
        row = row.split(",")
        monthly_pnl.append(row[1])
        month.append(row[0])
        net_pnl += float(row[1])
    for x in range(len(monthly_pnl) - 1):
        change = float(monthly_pnl[x+1]) - float(monthly_pnl[x])
        monthly_change.append(change)
    average_change = sum(monthly_change) / len(monthly_change)
    
    # Assign values
    max_change = max(monthly_change) 
    min_change = min(monthly_change)
    max_change_month_index = monthly_change.index(max(monthly_change))
    min_change_month_index = monthly_change.index(min(monthly_change))

    
if __name__ == '__main__':
    # Print the financial analysis to terminal and financial_analysis.txt
    print("\n" + "Financial Analysis\n" + "-"*30)
    print("Total Months: " + str(len(lines)))
    print("Total:  " + str(net_pnl))
    print("Average Change = " + str(average_change))
    print(f'Greatest Increase in Profits: {month[max_change_month_index]} ({max_change})')
    print(f'Greatest Decrease in Profits: {month[min_change_month_index]} ({min_change})')
    print("-"*30 + "\n")

    f = open(analysis,"a+")
    f.write("Financial Analysis\n")
    f.write("Total Months: " + str(len(lines)) + "\n")
    f.write("Total:  " + str(net_pnl) + "\n")
    f.write("Average Change = " + str(average_change) + "\n")
    f.write(f'Greatest Increase in Profits: {month[max_change_month_index]} ({max_change})\n')
    f.write(f'Greatest Decrease in Profits: {month[min_change_month_index]} ({min_change})\n')
    f.write("\n")
    f.close()
