#import dependancies
import pandas as pd
import os

#create csv file path
file_path = os.path.join("Resources","election_data.csv")

#read csb
df = pd.read_csv(file_path)

#calculate total number of votes cast
totalVotes = df["Ballot ID"].count()

#Create list of candidates who recieved votes
candidates = df["Candidate"].unique()

#Find percent of votes each candidate won
candidatesGroup = df.groupby(["Candidate"]).size()

charlesPercent = round((candidatesGroup[0]/len(df["Candidate"]))*100,3)
dianaPercent = round((candidatesGroup[1]/len(df["Candidate"]))*100,3)
raymonPercent = round((candidatesGroup[2]/len(df["Candidate"]))*100,3)

#Find total votes for each candidate
charlesTotal = candidatesGroup[0]
dianaTotal = candidatesGroup[1]
raymonTotal = candidatesGroup[2]

#Find winner
if charlesTotal > dianaTotal and raymonTotal:
    winner = "Charles Casper Stockham"
elif dianaTotal > charlesTotal and raymonTotal:
    winner = "Diana DeGette"
elif raymonTotal > charlesTotal and dianaTotal:
    winner = "Raymon Anthony Doane"

 #Print out to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {totalVotes}")
print("--------------------------")
print(f"Charles Casper Stockham: {charlesPercent}% ({charlesTotal})")
print(f"Diana DeGette: {dianaPercent}% ({dianaTotal})")
print(f"Raymon Anthony Doane: {raymonPercent}% ({raymonTotal})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

#Create text file
textPath = os.path.join("Analysis","ElectionAnalysis.txt")
with open(textPath,'w') as f:
    f.write("Election Results\n")
    f.write("--------------------------\n")
    f.write(f"Total Votes: {totalVotes}\n")
    f.write("--------------------------\n")
    f.write(f"Charles Casper Stockham: {charlesPercent}% ({charlesTotal}\n")
    f.write(f"Diana DeGette: {dianaPercent}% ({dianaTotal})\n")
    f.write(f"Raymon Anthony Doane: {raymonPercent}% ({raymonTotal})\n")
    f.write("--------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("--------------------------\n")

