# Define blank variables/lists:
candidate_name = []
candidate_option = []
candidate_dict = {}
winner = {}

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

# Step 1: The total number of votes cast - create a new list called "voter_count", then simply add that to the end table with len
  for row in csvreader:
    votes_total +=1
    
# Step 2: A complete list of candidates who received votes - create a new list called "candidate_option"...
    candidate_name = row[2]
    if candidate_name not in candidate_option:
      candidate_option.append(candidate_name)

      candidate_dict[candidate_name] = 0

    candidate_dict[candidate_name] += 1

# Step 3: The percentage of votes each candidate won
# Step 4: The total number of votes each candidate won

votes_Khan = candidate_dict["Khan"]
Khan_percent_votes = (votes_Khan / votes_total) * 100

votes_Correy = candidate_dict["Correy"]
Correy_percent_votes = (votes_Correy / votes_total) * 100 

votes_Li = candidate_dict["Li"]
Li_percent_votes = (votes_Li / votes_total) * 100

votes_OTooley = candidate_dict["O'Tooley"]
OTooley_percent_votes = (votes_OTooley / votes_total) * 100

# Step 5: The winner of the election based on popular vote.
winner = ({"Khan": votes_Khan, "Correy": votes_Correy, "Li": votes_Li, "O'Tooley": votes_OTooley})
Overall_Winner = max(winner, key=winner.get)

print([f"Election Results"])
print([f"-------------------------"])
print([f"Total Votes: {votes_total}"])
print([f"Khan: {Khan_percent_votes:.3f}% ({votes_Khan})"])
print([f"Correy: {Correy_percent_votes:.3f}% ({votes_Correy})"])
print([f"Li: {Li_percent_votes:.3f}% ({votes_Li})"])
print([f"O'Tooley: {OTooley_percent_votes:.3f}% ({votes_OTooley})"])
print([f"-------------------------"])
print([f"Winner: {Overall_Winner}"])
print([f"-------------------------"])

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
  csvwriter.writerow([f"Khan: {Khan_percent_votes:.3f}% ({votes_Khan})"])
  csvwriter.writerow([f"Correy: {Correy_percent_votes:.3f}% ({votes_Correy})"])
  csvwriter.writerow([f"Li: {Li_percent_votes:.3f}% ({votes_Li})"])
  csvwriter.writerow([f"O'Tooley: {OTooley_percent_votes:.3f}% ({votes_OTooley})"])
  csvwriter.writerow([f"-------------------------"])
  csvwriter.writerow([f"Winner: {Overall_Winner}"])
  csvwriter.writerow([f"-------------------------"])

# End of this story...