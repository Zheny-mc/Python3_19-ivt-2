#a
print("a)")
for i in range(10, 26, 1):
    print(i, ' ', i+0.4)

#b
print("b)")
for i in range(21, 36, 1):
    print("{0} {1}".format(i, i-0.6))

#c
print("c)")
for i in range(25, 30, 1):
    print("{0} {1} {2}".format(i, i+0.5, i-0.12))

#d
print("d)")
for i in range(1, 7, 1):
    print("%.2d %.5d" % (i, 5**i))
