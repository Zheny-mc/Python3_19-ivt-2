
x = 5
y = (x/100)**(7/3) + 3/(x/100) - 4*((x/100)**6) + 4/((x/100)**5)
print("x = %.2f, y = %11.2f" % (x/100, y))

max = y
min = y

#middle
sum = 0
n = 1.55//0.05

for x in range(10, 160, 5):
    y = (x/100)**(7/3) + 3/(x/100) - 4*((x/100)**6) + 4/((x/100)**5)

    if (min > y):
         min = y
    if (max < y):
         max = y
    sum += y

    print("x = %.2f, y = %11.2f" % (x/100, y))

middle = sum / n
print("Middle: %11.2f" % middle)
print("Min =   %11.2f\nMax =   %11.2f" % (min, max))
