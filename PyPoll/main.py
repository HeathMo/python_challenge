import os
import csv
#import pandas


poll_csv = os.path.join('Resources', 'election_data.csv')

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

khan_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent = 0

#def print_percents(election_data):
    #voter = str(election_data[0])
    #county = str(election_data[1])
    #candidate = str(election_data[2])

#The total number of votes cast
with open (poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #need list of candidates; dictionary? sum per candidate
    #vote_percent = ( / total_votes) * 100
    #The total number of votes each candidate won  
    #The winner of the election based on popular vote.
    for row in csvreader:
        total_votes += 1

        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    khan_percent = (khan_votes / total_votes) * 100
    correy_percent = (correy_votes / total_votes) * 100
    li_percent = (li_votes / total_votes) * 100
    otooley_percent = (otooley_votes / total_votes) * 100


print("Election Results")
print("-----------------")
print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print("-----------------")
print("Winner: Khan")
print("-----------------")

PyPoll_analysis = (
                f"Election Results\n"
                f"-----------------\n"
                f"Total Votes: {total_votes}\n"
                f"Khan: {khan_percent:.3f}% ({khan_votes})\n"
                f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
                f"Li: {li_percent:.3f}% ({li_votes})\n"
                f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
                f"-----------------\n"
                f"Winner: Khan\n"
                f"-----------------\n")

with open(PyPoll_analysis, "w") as txt_file:
    txt_file.write(PyPoll_analysis)
