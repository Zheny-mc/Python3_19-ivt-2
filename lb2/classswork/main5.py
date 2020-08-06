num = int(input("Input integer number: "))
k = 0  #количество делителей числа

print("Делители: ", end = '')

for x in range(1, num+1, 1):
    if (num % x == 0):
        print(x, end = ' ')
        k+=1

print()

print("Количество делителей числа %d: %d" % (num, k))
