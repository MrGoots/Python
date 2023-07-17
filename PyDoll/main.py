# Import modules os and csv
import os
import csv

# Objective 2: Set the path for the CSV file in PyPollcsv
pydoll_csv_path = "/Users/flynnlives/Documents/GitHub/UCI_DABC_Python_Challenge/PyDoll/resource/election_data.csv"

# Lists
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV
with open(pydoll_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1
        
        # Set candidate list
        candidatelist.append(row[2])
        
        # Set unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        
        # y = the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        
        # z = the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {str(count)}")    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")
print("-------------------------")

# Text file: election_output.txt

with open('eletion_output.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
