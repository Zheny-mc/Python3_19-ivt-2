import math

X1 = -20
X2 = 20
N = X2 - X1 + 1
x = -20
_x = x/10

#занчение функции
arr = [[0]*N, [0]*N]

y = math.sqrt(_x - _x**3)

arr[0][0] = _x
arr[1][0] = y

min = y
max = y
print("x = %5.2f | y = %.2f" % (_x, y))

x+=1
_x = x/10


for i in range(1, N):
    #поиск y
    if (_x - _x**3 >= 0):
        y = math.sqrt(_x - _x**3)
    else:
        y = 0

    arr[0][i] = _x
    arr[1][i] = y
    #поиск минимума
    if (min > y):
        min = y
    #поиск максимума
    elif (max < y):
        max = y
    #вывод результата
    print("x = %5.2f | y = %.2f" % (_x, y))
    #обновление x
    x+=1
    _x = x/10

print("\nMax = %.2f" % (max))
print ("Min = %.2f" % (min))
