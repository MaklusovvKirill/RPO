a = int(input("Введите двухзначное число: "))
a0 = a // 10
a1 = a % 10


if a0 > a1:
    print("Первая цифра больше")
elif a0 < a1:
    print("Вторая цифра больше")
else:
    print("Цифры ровны")
