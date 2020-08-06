#8 Вариант
import math

a = 0.35
x = 0.21

y = math.fabs(math.sin(x - a**2))**4
z = math.exp(2*x) + math.acos(2*x + a)

print("y = %lf\nz = %lf" % (y, z))
