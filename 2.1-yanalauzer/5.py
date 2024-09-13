def find_maximum_summands(n):
    summands = []
    current_number = 1

    while n > 0:
        if n >= current_number:
            summands.append(current_number)
            n -= current_number
            current_number += 1
        else:
            summands[-1] += n
            n = 0

    return summands

# Чтение входных данных
with open('input.txt', 'r') as file:
    n = int(file.readline())

# Решение задачи и запись результата в файл вывода
summands = find_maximum_summands(n)
with open('output.txt', 'w') as file:
    file.write(str(len(summands)) + '\n')
    file.write(' '.join(map(str, summands)))
