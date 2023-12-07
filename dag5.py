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
locations = []

for seed in seeds:
    for count, val in enumerate(map_list):
        for i, range in enumerate(val[1:]):
            maps = [int(x) for x in range.split(" ")]
            if maps[1]+maps[2] > seed >= maps[1]: 
                seed = maps[0] + seed - maps[1]
                break
    locations.append(seed)

print(min(locations))
