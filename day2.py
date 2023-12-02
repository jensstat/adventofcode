with open("data_folder/data2.txt") as file:
    data = file.readlines()
    data = [code.strip() for code in data]

max_red = 12
max_green = 13
max_blue = 14
sum_possible = 0
power = []

for index, data_row in enumerate(data,1):
    row = data_row.split()
    sum_list_red = []
    sum_list_green = []
    sum_list_blue = []
    for row_index, value in enumerate(row):
        if "red" in value:
            sum_list_red.append(row[row_index-1])
        if "green" in value:
            sum_list_green.append(row[row_index-1])
        if "blue" in value:
            sum_list_blue.append(row[row_index-1])

    red = [int(i) for i in sum_list_red]
    green = [int(i) for i in sum_list_green]
    blue = [int(i) for i in sum_list_blue]
    largest_red = max(red)
    largest_green = max(green)
    largest_blue = max(blue)
    power.append(largest_red*largest_green*largest_blue)


    if (largest_red<=max_red) and (largest_green<=max_green) and (largest_blue<=max_blue):
        sum_possible += index

    print(sum_possible) 
print(sum(power))
