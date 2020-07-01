''' PyBank Solution
Author: Raymond Garskovas
Notes: This script expects the data called budget_data.csv to be in a Resources folder.
'''

import os
import csv

budget_csv = os.path.join("../Resources/budget_data.csv")
file_to_output = os.path.join("../Analysis/PyBank_analysis.txt")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Establish the header of the file
    header = next(csv_reader)
    
    # Establish lists for Total Months, the profit changing, and the total profit
    Total_Months = []
    Change_Profit = []
    Total_Profit = []

    # Loop to go through the rows of the CSV, adding the Net Income to the Total Profit List and Months to Months list
    for row in csv_reader:
        Total_Profit.append(float(row[1]))
        Total_Months.append(row[0])
    
    for i in range(1,len(Total_Profit)):
        Change_Profit.append(Total_Profit[i] - Total_Profit[i-1])
        Avg_Profit_Change = sum(Change_Profit)/len(Change_Profit)
        Max_Profit_Change = max(Change_Profit)
        Min_Profit_Change = min(Change_Profit)

    # Print summary table including headers
    print(f"Financial Analysis")
    print(f"--------------------------")
    print(f"Total Months:", len(Total_Months))
    print(f"Total Profit:", sum(Total_Profit))
    print(f"Average Change in Profit:", round(Avg_Profit_Change))
    print(f"Greatest Increase in Profit:", round(Max_Profit_Change))
    print(f"Greatest Decrease in Profit:", round(Min_Profit_Change))

# create functions to plug into the summary table for text output
Summary_Months = len(Total_Months)
Summary_Profit = sum(Total_Profit)
Summary_Change = round(Avg_Profit_Change)
Summary_Increase = round(Max_Profit_Change)
Summary_Decrease = round(Min_Profit_Change)

# write text functions for the summary table
text_file = open(file_to_output, "w")
text_file.write(f"Financial Analysis")
text_file.write("\n")
text_file.write(f"--------------------------")
text_file.write("\n")
text_file.write(f"Total Months: {Summary_Months}")
text_file.write("\n")
text_file.write(f"Total Profit: {Summary_Profit}")
text_file.write("\n")
text_file.write(f"Average Change in Profit: {Summary_Change}")
text_file.write("\n")
text_file.write(f"Greatest Increase in Profit: {Summary_Increase}")
text_file.write("\n")
text_file.write(f"Greatest Decrease in Profit: {Summary_Decrease}")
text_file.write("\n")
text_file.write(f"--------------------------")