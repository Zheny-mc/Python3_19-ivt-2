num = int(input("Input Integer numder: "))
un_num = 0

while (num > 0):
    un_num = (un_num * 10) + (num % 10)
    num //= 10

print("Un_num = ", un_num)
