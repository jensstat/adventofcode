# Read in input-data
with open("data_folder/data3.txt") as file:
    dataset = [code.strip() for code in file.readlines()]

# Preprocess input-data
dataset = ['.' + x + '.' for x in dataset]
gears_sum = 0

nums = '0123456789'

def find_number(txt, col):
    start, end = col, col
    while start > 0 and txt[start - 1] in nums:
        start -= 1
    while end < len(txt) - 1 and txt[end + 1] in nums:
        end += 1
    return [start, end]

for row in range(len(dataset)):
    col = 0
    for col in range(len(dataset[row])):
        if dataset[row][col] == "*":
            gears = []
            for i in range(-1, 2):
                if 0 <= row + i < len(dataset):
                    row_adj = dataset[row + i] 
                    col_adj = max(col - 1, 0)
                    while col_adj <= col + 1:
                        if 0 <= col_adj < len(row_adj) and row_adj[col_adj] in nums:
                            num_indexes = find_number(row_adj, col_adj)
                            gears.append(row_adj[num_indexes[0]:num_indexes[1] + 1])
                            col_adj= num_indexes[1] + 1
                        else:
                            col_adj+= 1
            if len(gears) == 2:
                gears_sum += int(gears[0]) * int(gears[1])

print(gears_sum)
