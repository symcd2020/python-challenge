# import necessary modules
import os
import csv

budget_data_csv = os.path.join('C:/Users/sym0002/python-challenge/PyBank/Resources/budget_data.csv')

# set variables
total_months = 0
net_total = 0
profit_losses = 0
prior_profit_losses = 0
changes_list = []
dates = []

# reading CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    
    csv_header = next(csvreader)

# Analyzing the data to find results
    for row in csvreader:
        total_months += 1
        profit_losses = int(row[1])
        net_total += profit_losses

        if total_months > 1:
            change = profit_losses - prior_profit_losses
            changes_list.append(change)
            dates.append(row[0])
    
        prior_profit_losses = profit_losses

    # Calculating the average of the changes
    average_of_changes = sum(changes_list) / len(changes_list)
    
    # Calculating the greatest increase in profits
    max_change_index = changes_list.index(max(changes_list))
    greatest_increase_date = dates[max_change_index]
    greatest_increase_amount = max(changes_list)
    
    # Calculating the greatest decrease in profits
    min_change_index = changes_list.index(min(changes_list))
    greatest_decrease_date = dates[min_change_index]
    greatest_decrease_amount = min(changes_list)

#Creating the file path to the text file
output_file_path = "analysis.txt"

# Printing the results to the terminal and the text file
with open(output_file_path, "w") as output_file:
    # Print to the terminal
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months:", total_months)
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_of_changes:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")
    
    # Print to the text file
    print("Financial Analysis", file=output_file)
    print("-----------------------", file=output_file)
    print("Total Months:", total_months, file=output_file)
    print(f"Total: ${net_total}", file=output_file)
    print(f"Average Change: ${average_of_changes:.2f}", file=output_file)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})", file=output_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})", file=output_file)
    