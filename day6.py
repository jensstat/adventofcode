import math
import numpy as np

# Read in input-data
with open("data_folder/data6.txt") as file:
    dataset = [code.strip() for code in file.readlines()]
"""
time = np.array(dataset[0].split()[1:], int)
max_dist = np.array(dataset[1].split()[1:], int)

win_list = []

for i in range(len(time)):
    wins = 0
    for j in range(time[i]):
        race_dist = j*(time[i]-j)
        if race_dist > max_dist[i]:
            wins += 1
    win_list.append(wins)

print(math.prod(win_list))
"""

time_list = dataset[0].split()[1:]
dist_list = dataset[1].split()[1:]
time = ''
max_dist = ''

for i in range(len(time_list)):
    time += time_list[i]
    max_dist += dist_list[i]

time = int(time)
max_dist = int(max_dist)
win_list = []

wins = 0
for j in range(time):
    race_dist = j*(time-j)
    if race_dist > max_dist:
        wins += 1
win_list.append(wins)

print(math.prod(win_list))