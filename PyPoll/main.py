#Dependencies
import os
import csv

budgetpath=os.path.join('..','Resources','election_data.csv')
with open(budgetpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    csvheader = next(reader)

    votes_by_candidate = []

    for row in reader:
        votes_by_candidate.append(row[2])

    candidate_count = [[x,votes_by_candidate.count(x)] for x in set(votes_by_candidate)]
    
    votes = []
    name = []
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(votes_by_candidate)

correy_total = votes_by_candidate.count('Correy')
correy_percent = correy_total / total_votes

o_tooley_total = votes_by_candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = votes_by_candidate.count('Li')
li_percent = li_total / total_votes

khan_total = votes_by_candidate.count('Khan')
khan_percent = khan_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)