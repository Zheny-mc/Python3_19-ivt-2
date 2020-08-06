def Ln(x):
    M_LN2 = 0.69314718055995
    EPS = 1e-6
    lnln = M_LN2  #ln2
    k = 0
    while x > 2.0:
        x /= 2.0
        k+=1
    x -= 1.
    s = 0
    n = 1
    an = x
    while abs(an) > EPS:
        s += an
        n += 1
        an *= -x*(n - 1) / (n + 0.)
    s += k*lnln
    return s

def Exp(x):
    eps = 250
    res = 1
    num = 1
    for i in range(1, eps):
        num *= (x/i)
        res += num
    return res

def Sqrt(x):
    return Exp(0.5 * Ln(x))

def Pow(x, n):
    return Exp(n*Ln(x))

def Abs(x):
    if (x < 0):
        return ((-1)*x)
    return x

def Sin(x):
    eps = 200
    res = x
    num = x
    for i in range(3, eps, 2):
        num *= (-1) * (x*x / (i*(i-1)))
        res += num
    return res

def Cos(x):
    eps = 200
    res = 1
    num = 1
    for i in range(2, eps, 2):
        num *= (-1) * (x*x / (i*(i-1)))
        res += num
    return res

def Atan(x, eps=0.001):
    Step = 1
    sign = 1
    sum = 0
    num = 1
    while num >= eps:
        num *= (x / Step)
        sum += sign*num
        sign *= (-1)
        Step +=2
    return sum

def func(x):
    if Pow(x, 2) < 1:
        return Pow(x, 2) + Sqrt(Abs(x))
    if (Pow(x, 2) >= 1 and Pow(x, 2) <= 2):
        return Pow(x, 2) * Atan(2*x+1)
    if  Pow(x, 2) > 2:
        return Sin(Cos(Abs(x)))

A = 0
B = 30
H = 5

x = A/10 #значение аргумента фукции
N = int((B - A) / H)

matr = [[0]*N, [0]*N]

#вычисление значения функции
y = func(x)
#запись в  матрицу
matr[0][0] = x  #x
matr[1][0] = y  #y
#ищем максимальное по модулю занчение
max = abs(y)
#вывод результата
print("x = %5.2f | y = %5.2f" % (x, y))
#обновление x
A += H
x = float(A/10)

for i in range(1, N):
    #вычисление значения функции
    y = func(x)
    #запись в  матрицу
    matr[0][i] = x  #x
    matr[1][i] = y  #y
    #ищем максимальное по модулю занчение
    if max - abs(y) < 0:
        max = abs(y)
    #вывод результата
    print("x = %5.2f | y = %5.2f" % (x, y))
    #обновление x
    A += H
    x = float(A/10)
     
#вывод максимального по модулю занчения
print("|Max| = %5.2f" % max)






