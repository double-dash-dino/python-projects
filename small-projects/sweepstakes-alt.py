'''
MyBuilder 2021 Euro Sweepstakes
'''

import random
teams = ['Turkey', 'Italy', 'Wales', 'Switzerland', 'Denmark', 'Finland', 'Belgium', 'Russia', 'Netherlands', 'Ukraine', 'Austria', 'North Macedonia', 'England', 'Croatia', 'Scotland', 'Czech Republic', 'Spain', 'Sweden', 'Poland', 'Slovakia', 'Hungary', 'Portugal', 'France', 'Germany']
entries = ['Lionel', 'Andrew Shapiro', 'Ben Scales', 'Jack Fishwick', 'Jevon', 'Rainer', 'Finn', 'Holly', 'Karina', 'Chris', 'Adam', 'Andy Simms', 'Peter', 'Kelly', 'Georgia', 'Helen', 'Sten', 'Leo', 'Aiden', 'David', 'Hannah', 'Andrew Cowie', 'Josh', 'Jack Coles']
random.shuffle(teams)
teams_and_entries = zip(teams, entries)

for couple in teams_and_entries:
    print(couple)