"""
for code in data:
    sum_list = []
    for char in code:
        try:
            sum_list.append(int(char))
        except: 
            pass
    try: 
        sum_list = sum_list[::len(sum_list)-1]
    except:
        pass
    if len(sum_list)==1:
            sum_list.append(sum_list[0])

"""

with open("data_folder/data.txt") as file:
    data = file.readlines()
    data = [code.strip() for code in data]


sum = 0
for code in data:
    word = code.split()
    res = []
    if 'one' in code:
        code = code.replace('one', 'o1e')
    if 'two' in code:
        code = code.replace('two', 't2o')
    if 'three' in code:
        code = code.replace('three', 't3e')
    if 'four' in code:
        code = code.replace('four', 'f4r')
    if 'five' in code:
        code = code.replace('five', 'f5e')
    if 'six' in code:
        code = code.replace('six', 's6x')
    if 'seven' in code:
        code = code.replace('seven', 's7n')
    if 'eight' in code:
        code = code.replace('eight', 'e8t')
    if 'nine' in code:
        code = code.replace('nine', 'n9e')

    i = 0 
    for char in code:
        if not char.isalpha():
            res.append(char)
    
    if len(res)>=1:
        res = int("".join([res[0], res[-1]]))
        print(res)
        sum += res

print(sum)

