m = int(input("Input m: "))
n = int(input("Input n: "))

c = m * n

while (m != n):
    if (m > n):
        m -= n
    else:
        n -= m
nod = m

nok = c // nod

print("НОК(m, n) = {0}".format(nok))

