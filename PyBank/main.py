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
    grtincrease.append(int(row[1]))
    grtdecrease.append(int(row[1]))


#--- Step 3: Calculate average of the monthly changes for the entire period - how does this work?
average = [y-x for x, y in zip(total[:-1], total[1:])]

#--- Step 4: Calculate the greatest increase in profits (date and amount) over the entire period

for a, b in enumerate(grtincrease):
  if b == max(grtincrease):
    months_max_index = (a)

for c in [months[months_max_index]]:
    grtincrease_month = c

#--- Step 5: Calculate the greatest decrease in losses (date and amount) over the entire period

for d, e in enumerate(grtdecrease):
  if e == min(grtdecrease):
    months_min_index = (d)

for f in [months[months_min_index]]:
    grtdecrease_month = f

#--- Step 7: Summarise the findings into a single message 

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total)}")
print(f"Average Change: ${round(sum(average)/len(average),2)}") 
print(f"Greatest Increase in Profits: {grtincrease_month} ($ {max(grtincrease)})")
print(f"Greatest Decrease in Profits: {grtdecrease_month} ($ {min(grtdecrease)})")

#  Financial Analysis
#  ----------------------------
#  Total Months: 86 
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)

#--- Step 8: Export Data Table to Excel Table:



""" ## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.



## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down your tasks into discrete mini-objectives. This will be a _much_ better course of action than spending all your time looking for a solution on Stack Overflow.

* As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".

* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

* Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." If you need help, reach out because we're happy to help. But, come prepared and show us what you have done and your thought process.

* Always commit your work and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

* **Commit often**. """