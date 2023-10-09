def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}")

if __name__ == "__main__":
    try:
        n = int(input("Введите число n: "))
        multiplication_table(n)
    except ValueError:
        print("Ошибка: Введите целое число.")
