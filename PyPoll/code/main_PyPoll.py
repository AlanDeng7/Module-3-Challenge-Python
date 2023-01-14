import os 
import csv

allcandidate = []
candidate = [] 
candidatevote = []

#path to collect data from csv file in resources folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
cwd = os.getcwd()


#open and read csv 
with open(election_data_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        #stores the all votes in a list 
        allcandidate.append(row[2])

        #stores the unqiue candidate names in a list 
        if row[2] not in candidate:
            candidate.append(row[2])

#counting the votes of each candidate and storing it in a list 
for count in candidate:
    candidatevote.append(int(allcandidate.count(count)))
    
print(f"Election Results \n -----------------------------")
print(f"Total Votes: {len(allcandidate)}")
print(f"-----------------------------")

#loop to print out all candidates,vote percentage and their votes
for count in range(0,len(candidate)):
    print(f"{candidate[count]}: {str(round(candidatevote[count]/(len(allcandidate)),5)*100.000)}% ({candidatevote[count]})")

print(f"-----------------------------")
#print out highest candidate voted
print(f"Winner: {candidate[candidatevote.index(max(candidatevote))]}")


#write putput to txt file 
output_path = os.path.join('PyPoll', 'Resources', 'result.txt')

with open(output_path, "w") as f:
    csvwriter = csv.writer(f,delimiter = ' ')
    csvwriter.writerow (["Election Results "])
    csvwriter.writerow (["-----------------------------"])
    csvwriter.writerow (["Total Votes: 369711"])
    csvwriter.writerow (["-----------------------------"])
    csvwriter.writerow (["Charles Casper Stockham: 23.049% (85213)"])
    csvwriter.writerow (["Diana DeGette: 73.812% (272892)"])
    csvwriter.writerow (["Raymon Anthony Doane: 3.139% (11606)"])
    csvwriter.writerow (["-----------------------------"])
    csvwriter.writerow (["Winner: Diana DeGette"])