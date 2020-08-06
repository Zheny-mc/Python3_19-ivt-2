sum = 0

while (True):
    num = float(input("Input num: "))
    if (num > 0): 
        sum += num
    if (num == 0):
        break

print("Summa = %.3f" % sum)

