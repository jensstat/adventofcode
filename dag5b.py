with open("data_folder/data5.txt") as file:
    dataset = [code.strip() for code in file.readlines()]

seeds = [int(seed) for seed in dataset[0].split()[1:]]

tmp = []
map_list = []
for val in dataset[2:]:
    if val == "":
        map_list.append(tmp)
        tmp = []
    else:
        tmp.append(val)

map_list.append(tmp)

destination = []
locations_set = set()
import numpy as np

seeds_b = np.array_split(np.array(seeds), len(seeds)/2)

for seed_b in seeds_b:
    seed_range = np.arange(seed_b[0], seed_b[0]+seed_b[1])
    for val in map_list:
        for i, range in enumerate(val[1:]):
            maps = np.array([int(x) for x in range.split(" ")])
            cond = np.logical_and(seed_range >= maps[1], seed_range < maps[1]+maps[2])
            seed_range = np.where(cond, maps[0]+seed_range-maps[1], seed_range)
          
    locations_set.update(seed_range.tolist())
    print(locations_set)
print(min(locations_set))
