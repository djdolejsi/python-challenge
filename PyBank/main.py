# Import Dependencies
import os
import csv

# Create the path for the CSV file
budget_csv = os.path.join('Resources/budget_data.csv')

# Create the list to store your data
month_of_change = []
net_change_list= []

# Create your variables and giving them a starting point
total_net = 0
total_months = 0

# Open your CSV file using the path you created
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Identify the header and the following row after it
    header = next(csvreader)
    first_row = next(csvreader)

# Create additional variable needed prior to the loop
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    total_months +=1

# Start your for loop to look through the data   
    for row in csvreader:

# Looking through the total months data and saving the data to the month_of_change list
        total_months +=1
        month_of_change += [row[0]]
        
# Calculate the net change and then saving it to our list
        total_net += int(row[1]) 
        net_change = int(row[1])- prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]

# Calculate the average of the changes in Profits/Losses over the entire period and round that average 2 places
    net_monthly_change = sum(net_change_list) / len(net_change_list)
    rounded_monthly_change = round(net_monthly_change,2)

# Calculate the max and min value of the net change and the corresponding date it occured
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)
    greatest_increase_month = month_of_change[net_change_list.index(greatest_increase)]
    greatest_decrease_month = month_of_change[net_change_list.index(greatest_decrease)]

# Print my results
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_net}")
    print(f"Average Change: {rounded_monthly_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Create a txt file with my results and export it
with open('analysis.txt', 'w' ) as datafile:
    datafile.write(f"Financial Analysis \n")
    datafile.write(f"----------------------------\n")
    datafile.write(f"Total Months: {total_months} \n")
    datafile.write(f"Total: {total_net} \n")
    datafile.write(f"Average Change: {rounded_monthly_change} \n")
    datafile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) \n")
    datafile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) \n")