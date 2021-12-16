#---------------------part-3a---------------------
with open('part3.txt') as f:
    gamma_rate =""
    lines = f.readlines()
    results = [str(i) for i in lines]

for k in range(0, 12):
    countOne, countZero = 0, 0
    for i in range(len(results)):

        for j in range(k,k+1):

            if results[i][j] == '1':
                countOne += 1

            elif results[i][j] == '0':
                countZero += 1

    if countOne > countZero:
        gamma_rate += '1'
    else:
        gamma_rate += '0'

epsilon_rate = "111011100110"
print("Gamma rate: ", gamma_rate)
print("Epsilon rate: ",epsilon_rate)

ep = int(epsilon_rate, 2)
gm = int(gamma_rate, 2)
print("the consupmption is: ",ep*gm )














