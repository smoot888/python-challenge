#import dependancies
import pandas as pd
import os

#create csv file path
file_path = os.path.join("Resources","budget_data.csv")

#read csv
df =pd.read_csv(file_path)

#calculate total number of months in dataset
totalMonths = len(df.value_counts("Date"))

#calculate net total of profits and losses over the entire period
netTotal = df["Profit/Losses"].sum()

#calculate average change in profit/losses
#Calculate greatest increase and decrese in profits
profitDifferences = []
greatestGain = 0
greatestGainDate = ""
greatestLoss = 0
greatestLossDate = ""
for i in range(len(df["Profit/Losses"])-1):
    difference = df["Profit/Losses"][i+1] - df["Profit/Losses"][i]
    profitDifferences.append(difference)
    if difference > greatestGain:
        greatestGain = difference
        greatestGainDate = df["Date"][i+1]
    elif difference < greatestLoss:
        greatestLoss = difference
        greatestLossDate = df["Date"][i+1]
average = round(pd.Series(profitDifferences).mean(),2)

#Print out to terminal
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatestGainDate} (${greatestGain})")
print(f"Greatest Decrease in Profits: {greatestLossDate} (${greatestLoss})")

#Create text file
textPath = os.path.join("Analysis","FinancialAnalysis.txt")
with open(textPath,'w') as f:
    f.write("Financial Analysis\n")
    f.write("--------------------------\n")
    f.write(f"Total Months: {totalMonths}\n")
    f.write(f"Total: ${netTotal}\n")
    f.write(f"Average Change: ${average}\n")
    f.write(f"Greatest Increase in Profits: {greatestGainDate} (${greatestGain})\n")
    f.write(f"Greatest Decrease in Profits: {greatestLossDate} (${greatestLoss})\n")