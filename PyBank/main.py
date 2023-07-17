# Import
import os
import csv

pybank_csv_path = "/Users/flynnlives/Documents/GitHub/UCI_DABC_Python_Challenge/PyBank/resource/budget_data.csv"

# Lists & Variables
month_count = 0
pl_total = 0
total_value = 0
total_change = 0
profit_list = []
date_list = []

# Open CSV
with open(pybank_csv_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    pl_total = int(first_row[1])
    total_value = int(first_row[1])
    month_count = month_count + 1

    #Loop
    for row in csvreader:
        date_list.append(row[0])
        total_change = int(row[1]) - total_value
        profit_list.append(total_change)
        total_value = int(row[1])
        month_count = month_count + 1
      
        # Prof/Loss
        pl_total = pl_total + int(row[1])
    
    #Greatest increase in profits
    greatest_increase = max(profit_list)
    greatest_index = profit_list.index(greatest_increase)
    greatest_date = date_list[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profit_list)
    least_index = profit_list.index(greatest_decrease)
    least_date = date_list[least_index]

    #Average change in "Profit/Losses between months over entire period"
    mean = sum(profit_list)/len(profit_list)
      
print("----------------------------------------------------------")
print("Financial Analysis:")
print("----------------------------------------------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total Profits: ${str(pl_total)}")
print(f"Average Change: ${str(round(mean))}")
print(f"Greatest Increase in Profits: {greatest_date} ${str(greatest_increase)}")
print(f"Greatest Decrease in Profits: {least_date} ${str(greatest_decrease)}")
print("----------------------------------------------------------")

with open('pybank_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis:" + "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(month_count) + "\n")
    text.write("    Total Profits: " + "$" + str(pl_total) +"\n")
    text.write("    Average Change: " + '$' + str(int(mean)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(greatest_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(least_date) + " ($" + str(greatest_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")
