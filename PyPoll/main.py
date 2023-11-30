# import necessary modules
import os
import csv

election_data_csv = os.path.join('C:/Users/sym0002/python-challenge/PyPoll/Resources/election_data.csv')

# set variables
total_votes = 0
candidates = {}

# reading CSV file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    
    csv_header = next(csvreader)

# Analyzing the data to find results
    for row in csvreader:
       total_votes += 1
       candidate_name = row[2]
       
       if candidate_name in candidates:
           candidates[candidate_name] += 1
       else:
           candidates[candidate_name] = 1

# Finding the winner
winner = max(candidates, key=candidates.get)       

#Creating the file path to the text file
output_file_path = "analysis.txt"

# Printing the results to the terminal and the text file
with open(output_file_path, "w") as output_file:
    # Print to the terminal 
    print("Election Results")
    print("-----------------------")
    print("Total Votes:", total_votes)
    print("-----------------------")
    for candidate in sorted(candidates):
        votes = candidates[candidate]
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------")
    
     # Print to the text file
    print("Election Results", file=output_file)
    print("-----------------------", file=output_file)
    print("Total Votes:", total_votes, file=output_file)
    print("-----------------------", file=output_file)
    for candidate in sorted(candidates):
        votes = candidates[candidate]
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})", file=output_file)
    print("-----------------------", file=output_file)
    print(f"Winner: {winner}", file=output_file)
    print("-----------------------", file=output_file)
