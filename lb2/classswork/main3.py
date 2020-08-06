num = int(input("Input int number: "))
k = 0

while (num > 0):
    if (num % 2):
        k+=1
    print(num % 2, end = '')
    num //= 2

print("\nNum 1: %d" % (k))


