#This is the code for the PyBank assignment
import os
import csv 

csvpath= os.path.join('Resources','budget_data.csv')

total_revenue=[]
date=[]
profit_change=[]
total=0

with open(csvpath, encoding='utf-8-sig') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csvheader=next(csvfile)
    # print(f"Header:{csvheader}") 

# Define sum_revenue to add up calues of profit/loss list
    def sum_revenue(csvreader):
        total=0
        for row in csvreader:
            total=int(total)+int(row) 
        #print(total)
        return total 

# loop to get value for date and total_revenue
    for row in csvreader:
        date.append(row[0])
        total_revenue.append(row[1]) 
    # print(len(date))

# change in profit month by month
for i in range(len(total_revenue)-1):
    change=int(total_revenue[i+1])+(0-int(total_revenue[i])) 
    profit_change.append(change)
    #print(profit_change)

endtime=(len(total_revenue))-1
months=len(date) 
total_sum=sum_revenue(total_revenue)

#find total change
change=int(total_revenue[int(endtime)])-int(total_revenue[0])
total_change="{:.2f}".format(change/endtime) 
#print(total_change) 

# find greatest increase/decrease
greatest_increase=max(profit_change)
#print(greatest_increase)
greatest_decrease=min(profit_change)
#print(greatest_decrease)

#find the date of corresponding greatest increase/decrease
for i in range(len(profit_change)-1):
    if profit_change[i]==greatest_increase:
        max_date=date[i+1]
    elif profit_change[i]==greatest_decrease:
        min_date=date[i+1]  
#print(max_date) 
#print(min_date) 

print("Financial Analysis")
print("-------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${total_sum}') 
print(f'Average Change: ${total_change}')
print(f'Greatest Increase in Profits: {max_date} (${greatest_increase})') 
print(f'Greatest Decrease in Profits: {min_date} (${greatest_decrease})') 

output=os.path.join('Analysis','PyBank_Analysis.txt')
 
file= open(output,'w')
file.write(" Financial Analysis" + "\n")  
file.write("------------------------- \n")
file.write(f'Total Months: {len(date)} \n')
file.write(f'Total: ${total_sum} \n')
file.write(f' Average Change: ${total_change} \n')
file.write(f' Greatest Increase in Profits: {max_date} (${greatest_increase}) \n')
file.write(f' Greatest Decrease in Profits: {min_date} (${greatest_decrease}) \n')




    

    











