import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_net = 0
months_change = []
net_change_list = []
greatest_up = ["",0]
greatest_down = ["",0]

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #something is off since getting a zero - need help
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + float(first_row[1])
    previous_net = float(first_row[1])

    #Calculate the changes in "Profit/Losses" over the entire period, 
    #then find the average of those changes
    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - previous_net
        net_change_list = net_change_list + [net_change]
        months_change = months_change + [row[0]]
        month_average = sum(net_change_list) / len(net_change_list)

#The greatest increase in profits (date and amount) over the entire period
        #error reads: ValueError: max() arg is an empty sequence
        #max_profit = max(change_month)
        #max_month = change_month.index(max(change_month)) + 1
        if net_change > greatest_up[1]:
            greatest_up[0] = row[0]
            greatest_up[1] = net_change
#The greatest decrease in profits (date and amount) over the entire period
        #min_profit = min(change_month)
        #min_month = change_month.index(min(change_month)) + 1
        if net_change < greatest_down[1]:
            greatest_down[0] = row[0]
            greatest_down[1] = net_change

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${month_average:.2f}")
print(f"Greatest Increase in Profits: {greatest_up[0]} (${greatest_up[1]})")
print(f"Greatest Decrease in Profits: {greatest_down[0]} (${greatest_down[1]})")

PyBank_analysis = (
                    f"Financial Analysis\n"
                    f"--------------------\n"
                    f"Total Months: {total_months}\n"
                    f"Average Change: ${month_average:.2f}\n"
                    f"Greatest Increase in Profits: {greatest_up[0]} (${greatest_up[1]}\n"
                    f"Greatest Decrease in Profits: {greatest_down[0]} (${greatest_down[1]}\n")

with open(PyBank_analysis, "w") as txt_file:
    txt_file.write(PyBank_analysis)