''' PyPoll Solution
Author: Raymond Garskovas
Notes: This script expects the data called election_data.csv to be in a Resources folder.
'''

import os
import csv
import re

election_csv = os.path.join("../Resources/election_data.csv")
file_to_output = os.path.join("../Analysis/PyPoll_analysis.txt")

with open(election_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    
    #define dictionary and the total counter
    Candidate_Dict = {}
    Total_Votes = 0

    # go through the rows of the reader adding a new values to the dictionary while adding repeats to the total for the candidate
    for x in csv_reader:
        Total_Votes += 1
        if x[2] in Candidate_Dict:
            Candidate_Dict[x[2]] += 1
        else:
            Candidate_Dict[x[2]] = 1

# print the function table including formatted data to remove additional decimal places
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes:", Total_Votes)
print(f"--------------------------")
for i in Candidate_Dict:
    print(i,":", "{:.3f}".format((Candidate_Dict[i]/Total_Votes)*100),"% (",Candidate_Dict[i],")")
print(f"--------------------------")
print(f"Winner: ", max(Candidate_Dict, key=Candidate_Dict.get))
print(f"--------------------------")



# consolidate the candidates for text printing purposes via a list
Consolidated_Candidate_Dict = []
for i in Candidate_Dict:
    Consolidated_Candidate_Dict.append(f"{i} : {round(Candidate_Dict[i]/Total_Votes*100, 2)}% ({Candidate_Dict[i]})")


# write text functions for the summary table
text_file = open(file_to_output, "w")
text_file.write(f"Election Results")
text_file.write("\n")
text_file.write(f"--------------------------")
text_file.write("\n")
text_file.write(f"Total Votes: {Total_Votes}")
text_file.write("\n")
text_file.write(f"--------------------------")
text_file.write("\n")
text_file.write(f"{Consolidated_Candidate_Dict}")
text_file.write("\n")
text_file.write(f"--------------------------")
text_file.write("\n")
text_file.write(f"Winner: {max(Candidate_Dict, key=Candidate_Dict.get)}")
text_file.write("\n")
text_file.write(f"--------------------------")
text_file.write("\n")