# Define blank variables/lists:
vote_candidate = []
candidate_name = []
candidate_option = []
candidate_dict = {}

# Variable Default Values
votes_total = 0
votes_Khan = 0
votes_Correy = 0
votes_Li = 0
votes_OTooley = 0

# Import CSV Data
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)

# create a new indexed list to identify/confirm  the names of the candicates.

# Step 1: The total number of votes cast - create a new list called "voter_count", then simply add that to the end table with len
  for row in csvreader:
    votes_total +=1
    
# Step 2: A complete list of candidates who received votes - create a new list called "candidate_option"...
    candidate_name = row[2]
    if candidate_name not in candidate_option:
      candidate_option.append(candidate_name)

      candidate_dict[candidate_name] = 0

    candidate_dict[candidate_name] += 1

#Calcualations of the candidates and their  
votes_Khan = candidate_dict["Khan"]
Khan_percent_votes = votes_Khan / votes_total
print(votes_Khan)
print(Khan_percent_votes)

votes_Correy = candidate_dict["Correy"]
Correy_percent_votes = votes_Correy / votes_total
print(votes_Correy)
print(Correy_percent_votes)

votes_Li = candidate_dict["Li"]
Li_percent_votes = votes_Li / votes_total
print(votes_Li)
print(Li_percent_votes)

votes_OTooley = candidate_dict["O'Tooley"]
OTooley_percent_votes = votes_OTooley / votes_total
print(votes_OTooley)
print(OTooley_percent_votes)


# Step 3: The percentage of votes each candidate won - tally all votes 

# Step 4: The total number of votes each candidate won

# Step 5: The winner of the election based on popular vote.

# Step 6: Export Data Table to Excel Table:

# Specify the file to write to and open in write mode. 
output_path = os.path.join('Resources', 'voting_result.csv')
with open(output_path, 'w', newline='') as csvfile:

#Initialize csv.writer
  csvwriter = csv.writer(csvfile, delimiter=',')
  
#Write the rows
  csvwriter.writerow([f"Election Results"])
  csvwriter.writerow([f"-------------------------"])
  csvwriter.writerow([f"Total Votes: {votes_total}"])
  csvwriter.writerow([f"Khan: {votes_Khan} {Khan_percent_votes:.3f}"])
  csvwriter.writerow([f"Correy: {votes_Correy} {Correy_percent_votes:.3f} "])
  csvwriter.writerow([f"Li: {votes_Li} {Li_percent_votes:.3f}"])
  csvwriter.writerow([f"O'Tooley: {votes_OTooley} {OTooley_percent_votes:.3f}"])
  csvwriter.writerow([f"-------------------------"])
  csvwriter.writerow([f"Winner: "])
  csvwriter.writerow([f"-------------------------"])

# End of this story...




print([f"Election Results"])
print([f"-------------------------"])
print([f"Total Votes: {votes_total}"])
print([f"Khan: {votes_Khan} {Khan_percent_votes:.3f}"])
print([f"Correy: {votes_Correy} {Correy_percent_votes:.3f} "])
print([f"Li: {votes_Li} {Li_percent_votes:.3f}"])
print([f"O'Tooley: {votes_OTooley} {OTooley_percent_votes:.3f}"])
print([f"-------------------------"])
print([f"Winner: "])
print([f"-------------------------"])

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