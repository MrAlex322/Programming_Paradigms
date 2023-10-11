# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для 
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

numbers = [5, 2, 9, 1, 5, 6]
sort_list_imperative(numbers)
print(numbers)