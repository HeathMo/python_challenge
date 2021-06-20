import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
profit = []
change_month = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    lines = len(list(csvreader))

    #something is off since getting a zero - need help
    total = sum([row[1]] for row in csvreader)

    #Calculate the changes in "Profit/Losses" over the entire period, 
    #then find the average of those changes
    #need to subtract - like the candies
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])

    for x in range(len(profit) - 1):
        change_month.append(profit[x+1] - profit[x])

#The greatest increase in profits (date and amount) over the entire period
#error reads: ValueError: max() arg is an empty sequence
    max_profit = max(change_month)
    max_month = change_month.index(max(change_month)) + 1

#The greatest decrease in profits (date and amount) over the entire period
    min_profit = min(change_month)
    min_month = change_month.index(min(change_month)) + 1

print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(lines - 1))
print("Total: $" + str({sum(profit)}))
print(f"Average Change: {round(sum(change_month)/len(change_month),2)}")
print(f"Greatest Increase in Profits: {months[max_month]} ${(str(max_profit))}")
print(f"Greatest Decrease in Profits: {months[min_month]} ${(str(min_profit))}")



    
