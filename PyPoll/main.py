





# Step 1: The total number of votes cast

# Step 2: A complete list of candidates who received votes

# Step 3: The percentage of votes each candidate won

# Step 4: The total number of votes each candidate won

# Step 5: The winner of the election based on popular vote.




#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```

# Step 6: Export Data Table to Excel Table:

# Specify the file to write to and open in write mode. 
# output_path = os.path.join('Resources', 'voting_result.csv')
# with open(output_path, 'w', newline='') as csvfile:

# Initialize csv.writer
# csvwriter = csv.writer(csvfile, delimiter=',')

# Write the rows
#  csvwriter.writerow([f"Financial Analysis"])
#  csvwriter.writerow([f"----------------------------"])
#  csvwriter.writerow([f"Total Months: {len(months)}"])
#  csvwriter.writerow([f"Total: ${sum(total)}"])
#  csvwriter.writerow([f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}"])
#  csvwriter.writerow([f"Greatest Increase in Profits: {grtincrease_month} (${max(monthly_change)})"])
#  csvwriter.writerow([f"Greatest Decrease in Profits: {grtdecrease_month} (${min(monthly_change)})"])

  # End of this story...