#---------------------part-1a---------------------
with open('input.txt') as f:
    count = 0
    lines = f.readlines()
    results = [int(i) for i in lines]

    for i in range(1, len(results)):
        if(results[i] > results[i-1]):
            count += 1

print(count)
