x = float(input("Input float num: "))

for i in range(0, 7, 1):
    D = (x - (2**i - 1))/(x - 2**i)

print("D = %lf" % D)
