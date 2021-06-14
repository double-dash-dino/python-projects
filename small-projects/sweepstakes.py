'''
MyBuilder 2021 Euro Sweepstakes
'''

import random
teams = ['Turkey', 'Italy', 'Wales', 'Switzerland', 'Denmark', 'Finland', 'Belgium', 'Russia', 'Netherlands', 'Ukraine', 'Austria', 'North Macedonia', 'England', 'Croatia', 'Scotland', 'Czech Republic', 'Spain', 'Sweden', 'Poland', 'Slovakia', 'Hungary', 'Portugal', 'France', 'Germany']
entries = ['Lionel', 'Andrew Shapiro', 'Ben Scales', 'Jack Fishwick', 'Jevon', 'Rainer', 'Finn', 'Holly', 'Karina', 'Chris', 'Adam', 'Andy Simms', 'Peter', 'Kelly', 'Georgia', 'Helen', 'Sten', 'Leo', 'Aiden', 'David', 'Hannah', 'Andrew Cowie', 'Josh', 'Jack Coles']
teams_and_entries = {}


for i in range(0, len(entries)):
    randomIndex = random.randint(0, len(teams)-1)
    randomTeam = teams[randomIndex]
    teams_and_entries[entries[i]] = randomTeam
    teams.pop(randomIndex)
print(teams_and_entries)

# Could have used the zip method instead!!