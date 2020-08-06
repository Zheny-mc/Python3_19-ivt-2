sum = 0

for x in range(51, 200, 1):
    if ((x % 5 == 0) and (x % 8 == 0)):
        sum += x

print("Sum = %d" % sum)
