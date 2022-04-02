# Define blank variables/lists:
months = []
total = []
grtincrease = []
grtdecrease = []

# Import CSV Data
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)

#--- Step 1: Calculate Total count of unique months - count added to monthcount
  #monthcount = sum(1 for line in csvfile)

#--- Step 2: Calculate Net total amount of Profit/Losses for the entire period

# ForLoop: loop through each row
  for row in csvreader:
    months.append(row[0])
    total.append(int(row[1]))
    #grtincrease.append(int(row[1]))
    #grtdecrease.append(int(row[1]))

#--- Step 3: Calculate average of the monthly changes for the entire period - how does this work?
monthly_change = [y-x for x, y in zip(total[:-1], total[1:])]

#--- Step 4: Calculate the greatest increase in profits (date and amount) over the entire period

for a, b in enumerate(monthly_change):
  if b == max(monthly_change):
    
    months_max_index = (a+1)
    print(months_max_index)

for c in [months[months_max_index]]:
    grtincrease_month = c

#--- Step 5: Calculate the greatest decrease in losses (date and amount) over the entire period

for d, e in enumerate(monthly_change):
  if e == min(monthly_change):
    months_min_index = (d)

for f in [months[months_min_index]]:
    grtdecrease_month = f

#--- Step 7: Summarise the findings into a single message 

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}") 
print(f"Greatest Increase in Profits: {grtincrease_month} (${max(monthly_change)})")
print(f"Greatest Decrease in Profits: {grtdecrease_month} (${min(monthly_change)})")

#--- Step 8: Export Data Table to Excel Table:

# Specify the file to write to and open in write mode. 
output_path = os.path.join('Resources', 'budget_result.csv')
with open(output_path, 'w', newline='') as csvfile:

# Initialize csv.writer
  csvwriter = csv.writer(csvfile, delimiter=',')

# Write the rows
  csvwriter.writerow([f"Financial Analysis"])
  csvwriter.writerow([f"----------------------------"])
  csvwriter.writerow([f"Total Months: {len(months)}"])
  csvwriter.writerow([f"Total: ${sum(total)}"])
  csvwriter.writerow([f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}"])
  csvwriter.writerow([f"Greatest Increase in Profits: {grtincrease_month} (${max(monthly_change)})"])
  csvwriter.writerow([f"Greatest Decrease in Profits: {grtdecrease_month} (${min(monthly_change)})"])

  # End of this story...