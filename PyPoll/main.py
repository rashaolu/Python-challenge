# This is the code for PyPoll assignment 
import os
import csv 

csvpath= os.path.join('Resources','election_data.csv')
# defining variables
candidate_count1=0 
candidate_count2=0
candidate_count3=0

C1="Charles Casper Stockham"
C2="Diana DeGette"
C3="Raymon Anthony Doane"
#print(C2)

#open file with correct path
with open(csvpath ,encoding='utf-8-sig') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csvheader=next(csvfile)
    #print(f"header:{csvheader}")

    for row in csvreader: 
        #count up the votes for each candidate
        if row[2] ==C1:
            candidate_count1=candidate_count1+1
        elif row[2]==C2:
            candidate_count2=candidate_count2+1
        elif row[2]==C3:
            candidate_count3=candidate_count3+1

    totalvote=candidate_count1+candidate_count2+candidate_count3
    #print(totalvote)
    #print(candidate_count1)

    #find percentage of votes and round
    c1p=round((candidate_count1/totalvote)*100,3)
    c2p=round((candidate_count2/totalvote)*100,3)
    c3p=round((candidate_count3/totalvote)*100,3)
    #print(c2p) 

    #print results
    print("Election Results")
    print("-------------------------")
    print(f'Total votes: {totalvote}')
    print("-------------------------")
    print(f'{C1}: {c1p}% ({candidate_count1})')
    print(f'{C2}: {c2p}% ({candidate_count2})')
    print(f'{C3}: {c3p}% ({candidate_count3})')
    print("-------------------------") 

    # if statement to choose winner
    if candidate_count1>candidate_count2 and candidate_count1>candidate_count3:
        print(f'Winner: {C1}') 
    elif candidate_count2>candidate_count1 and candidate_count2>candidate_count3:
        print(f'Winner: {C2}')
    elif candidate_count3>candidate_count1 and candidate_count3>candidate_count2:
        print(f'Winner: {C3}')
    print("-------------------------")

#putting results in a text file
output=os.path.join('Analysis','PyPoll_Analysis.txt') 

file=open(output,'w')
file.write(f'Election Results \n') 
file.write(f'------------------------- \n')
file.write(f'Total Votes: {totalvote} \n')
file.write(f'------------------------- \n')
file.write(f'{C1}: {c1p}% ({candidate_count1}) \n')
file.write(f'{C2}: {c2p}% ({candidate_count2}) \n')
file.write(f'{C3}: {c3p}% ({candidate_count3}) \n') 
file.write(f'------------------------- \n') 
file.write(f'Winner: {C2} \n')
file.write(f'------------------------- \n')      
    




