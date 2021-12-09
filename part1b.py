#---------------------part-1b---------------------
with open('input.txt') as f:
    lines = f.readlines()
    results = [int(i) for i in lines]
    count = 0
    for i in range(len(results)):
        max, tempmax = 0, 0
        for j in range(1,4):
            max += results[i - j]
            tempmax += results[i - j - 1]
        if(max > tempmax):
            count += 1


print(count)
