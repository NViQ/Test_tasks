def calculate_sum():
    print("Введите N, M, Q (количество строк, столбцов и ограничений):")
    N, M, Q = map(int, input().split())

    print("Введите имена столбцов через пробел:")
    columns = input().split()

    print(f"Введите данные таблицы: {N} строки и {M} столбцов:")
    data = [list(map(int, input().split())) for _ in range(N)]

    print("Введите ограничения (по одному в строке):")
    constraints = [input() for _ in range(Q)]

    def check_row(row):
        for constraint in constraints:
            col_name, operator, value = constraint.split(' ')
            col_index = columns.index(col_name)
            if not eval(f"{row[col_index]} {operator} {value}"):
                return False
        return True

    total_sum = sum(sum(row) for row in data if check_row(row))

    return total_sum

result = calculate_sum()
print(f"Результат: {result}")
