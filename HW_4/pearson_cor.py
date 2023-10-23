def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))

    sum_x_squared = sum((x[i] - mean_x) ** 2 for i in range(len(x)))
    sum_y_squared = sum((y[i] - mean_y) ** 2 for i in range(len(y)))

    denominator = (sum_x_squared ** 0.5) * (sum_y_squared ** 0.5)

    if denominator == 0:
        return 0  # Защита от деления на ноль

    correlation = numerator / denominator

    return correlation

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 7]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)


