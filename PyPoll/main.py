import os
import csv
#import pandas


poll_csv = os.path.join('Resources', 'election_data.csv')

def print_percents(election_data):
    voter = str(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

#The total number of votes cast
with open (poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    total_votes = len(list(csvreader)) - 1
    print("Total Votes: " + str(total_votes))
#A complete list of candidates who received votes
    data = csv.DictReader(poll_csv)
    print("Candidates who received votes:")

#The percentage of votes each candidate won
#need list of candidates; dictionary? sum per candidate
#vote_percent = ( / total_votes) * 100
#The total number of votes each candidate won

#The winner of the election based on popular vote.

