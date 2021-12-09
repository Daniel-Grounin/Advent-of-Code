#---------------------part-2b---------------------
with open('part2.txt') as f:
    # count = 0
    lines = f.readlines()
    results = [str(i) for i in lines]
    # print(results)
    res = list(map(lambda sub: int(''.join([ele for ele in sub if ele.isnumeric()])), results))
    string = list(map(lambda sub: str(''.join([ele for ele in sub if not ele.isnumeric()])), results))

depth, aim, horizontal = 0, 0, 0
for i in range(len(res)):
    if(string[i] == 'forward \n'):
        horizontal += res[i]
        depth += aim * res[i]
    elif(string[i] == 'up \n'):
        aim -= res[i]
    elif(string[i] == 'down \n'):
        aim += res[i]

print("horizontal * depth =  ", horizontal*depth)