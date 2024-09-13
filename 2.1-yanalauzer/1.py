import time
import resource
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start = time.time()

def fractional_knapsack(n, W, items):
    # Сортируем предметы по убыванию отношения стоимости к весу
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0

    for value, weight in items:
        # Если предмет целиком помещается в сумку, добавляем его полностью
        if weight <= W:
            total_value += value
            W -= weight
        else:
            # Если предмет не помещается целиком, берем долю предмета,
            # которая поместится в сумку
            fraction = W / weight
            total_value += value * fraction
            break

    return total_value

# Чтение входных данных
with open('input.txt', 'r') as file:
    n, W = map(int, file.readline().split())
    items = [list(map(int, line.split())) for line in file]

# Решение задачи и запись результата в файл вывода
result = fractional_knapsack(n, W, items)
with open('output.txt', 'w') as file:
    file.write("{:.4f}".format(result))

end = time.time() - start
print(end)
print('{}'.format(mem))