# Read in input-data
with open("data_folder/data3.txt") as file:
    dataset = [code.strip() for code in file.readlines()]

# Preprocess input-data
dataset = ['.' + x + '.' for x in dataset]
gears_sum = 0

nums = '0123456789'

def find_number(txt, col):
    num = ""
    for col_val in txt[col:]:
        if col_val in nums:
            num += col_val
        else:
            break
    return num

def calc_parts(dataset, nums):
    parts = 0
    for row in range(len(dataset)):
        col = 0
        while col < len(dataset[row]) - 1:
            
            if dataset[row][col] in nums:
                num = find_number(dataset[row], col)
                range_ind = range(col - 1, col + len(num) + 1)
                for i in range_ind:
                    if row != 0 and dataset[row - 1][i] != '.' and dataset[row - 1][i] not in nums:
                        parts += int(num)
                    if dataset[row][i] != '.' and dataset[row][i] not in nums:
                        parts += int(num)
                    if row != len(dataset) - 1 and dataset[row + 1][i] not in nums and dataset[row + 1][i] != '.':
                        parts += int(num)
                col = col + len(num)
            else:
                col += 1
    return parts

print(calc_parts(dataset, nums))
