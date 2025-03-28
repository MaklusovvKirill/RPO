n = int(input("Введите количество троек целых чисел (n): "))

if n <= 0:
    print("Количество троек должно быть натуральным (больше 0).")
else:
    co = 0
    for i in range(n):
        a, b, c = map(int, input(f"Введите тройку целых чисел (a b c) для\
            {i + 1}-й тройки: ").split())
        if a + b >= c and a + c >= b and b + c >= a:
            co += 1
    print(f"Количество троек, которые могут быть использованы\
        для построения треугольника: {co}")
