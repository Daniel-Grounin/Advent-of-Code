#---------------------part-2a---------------------
with open('part2.txt') as f:
    lines = f.readlines()
    results = [str(i) for i in lines]
    # print(results)
    res = list(map(lambda sub: int(''.join([ele for ele in sub if ele.isnumeric()])), results))
    string = list(map(lambda sub: str(''.join([ele for ele in sub if not ele.isnumeric()])), results))

forward, up, down, aim = 0, 0, 0, 0
for i in range(len(res)):
    if(string[i] == 'forward \n'):
        forward += res[i]
    elif(string[i] == 'up \n'):
        up -= res[i]
    elif(string[i] == 'down \n'):
        up += res[i]

print("the planned course is: ", forward*up)
