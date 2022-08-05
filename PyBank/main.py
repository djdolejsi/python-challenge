from itertools import count
import os
import csv

budget_csv = os.path.join('Resources/budget_data.csv')
month_of_change = []
net_change_list= []
total_net = 0
total_months =0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    total_months +=1
    
    for row in csvreader:
        total_months +=1
        total_net += int(row[1]) 
        month_of_change += [row[0]]
        net_change = int(row[1])- prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]

    net_monthly_change = sum(net_change_list) / len(net_change_list)

    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)

    print(f"Total Months: {total_months}")
    print(f"Total: {total_net}")
    print(f"Average Change: {net_monthly_change}")
    print(f"Greatest Increase in Profits:  {(greatest_increase)}")
    print(f"Greatest Decrease in Profits:  {(greatest_decrease)}")

    