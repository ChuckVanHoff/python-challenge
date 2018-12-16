

import os
import csv
import sys

# Declare the file path name
budget_data_csv = "Resources/budget_data.csv"

# Text file to be written and exported
analysis = "financial_analysis.txt"

# Open and read csv
with open(budget_data_csv, 'r', newline="") as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
    
    print(type(csv_header))

    # Creates a list of strings, each one being a separate row of the CSV file, and 
    # the variables to store the valuse
    lines = budgetfile.readlines()
    monthly_pnl = []
    month = []
    
    # A variable to keep net profit/losses sum
    net_pnl = 0

    # Some variables to hold and store monthly_change values
    change = float
    monthly_change = []

    # Split each line at the comma and add the split line to separated_lines
    for row in lines:
        row = row.split(",")
        
        # Add values to the monthly_pnl and month lists
        monthly_pnl.append(row[1])
        month.append(row[0])
        
        # Sum pofit and loss values
        net_pnl += float(row[1])

    # Add values to monthly_change list
    for x in range(len(monthly_pnl) - 1):
        change = float(monthly_pnl[x+1]) - float(monthly_pnl[x])
        monthly_change.append(change)

    # Calculate the average change between months
    average_change = sum(monthly_change) / len(monthly_change)

    # Variables for the max and min change
    max_change = float
    min_change = float
    max_change_month_index = int
    min_change_month_index = int

    # Assign values
    max_change = max(monthly_change) 
    min_change = min(monthly_change)
    max_change_month_index = monthly_change.index(max(monthly_change))
    min_change_month_index = monthly_change.index(min(monthly_change))

    # Print the financial analysis to terminal and financial_analysis.txt
    print("Financial Analysis\n" + "_"*30)
    print("Total Months: " + str(len(lines)))
    print("Total:  " + str(net_pnl))
    print("Average Change = " + str(average_change))
    print(f'Greatest Increase in Profits: {month[max_change_month_index]} ({max_change})')
    print(f'Greatest Decrease in Profits: {month[min_change_month_index]} ({min_change})')

    f = open(analysis,"a+")
    f.write("Financial Analysis\n" + "_"*30 + "\n")
    f.write("Total Months: " + str(len(lines)) + "\n")
    f.write("Total:  " + str(net_pnl) + "\n")
    f.write("Average Change = " + str(average_change) + "\n")
    f.write(f'Greatest Increase in Profits: {month[max_change_month_index]} ({max_change})\n')
    f.write(f'Greatest Decrease in Profits: {month[min_change_month_index]} ({min_change})\n')
    f.close()