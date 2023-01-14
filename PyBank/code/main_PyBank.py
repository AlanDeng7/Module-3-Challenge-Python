import os
import csv

month = []
total = 0 
profits = []
change_list=[]
greatest_inc = 0 
greatest_dec = 0 
greatest_inc_index = 0

#path to collect data from csv file in resources folder
budget_data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')
cwd = os.getcwd()


#open and read csv 
with open(budget_data_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        #stores the dates in a list 
        month.append(row[0])
        #total of all loss/profits
        total = total + int(row[1])
        #store loss/profits in a list 
        profits.append(int(row[1]))
        
#average changes in a list
    for index in range(1,len(profits)):
        changes = profits[index]-profits[index-1]
        change_list.append(changes)

#greatest increase in profits (without using the changes_list)
    for index in range(1,len(profits)):
        if profits[index]-profits[index-1] > greatest_inc :
            greatest_inc = profits[index]-profits[index-1]
            greatest_inc_index = index

#greatest decrease in profits (using the changes_list)
greatest_dec = min(change_list)   
# +1 because index value is offset to the previous value 
greatest_dec_index = change_list.index(greatest_dec) + 1 

#priting outputs to terminal 
print(f"Financial Analysis \n -----------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: ${total}")
print(f"Average Change: ${round(sum(change_list)/len(change_list),2)}")
print(f"Greatest Increase in Profits: {month[greatest_inc_index]} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {month[greatest_dec_index]} (${greatest_dec})")


#write putput to txt file 
output_path = os.path.join('PyBank', 'Resources', 'result.txt')

with open(output_path, "w") as f:
    csvwriter = csv.writer(f,delimiter = ' ')
    csvwriter.writerow (["Financial Analysis"])
    csvwriter.writerow (["-----------------------------"])
    csvwriter.writerow (["Total Months: "])
