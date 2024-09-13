import time
import resource
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start = time.time()

def max_gold_weight(W, n, weights):
    # Создаем двумерный массив для хранения результатов
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # Если текущий слиток не превышает вместимость рюкзака,
            # то выбираем максимум между взятием этого слитка и не взятием
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], weights[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                # Иначе просто копируем результат из предыдущей строки
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


with open('input.txt', 'r') as file:
    W, n = map(int, file.readline().split())
    weights = list(map(int, file.readline().split()))

result = max_gold_weight(W, n, weights)
with open('output.txt', 'w') as file:
    file.write(str(result))

end = time.time() - start
print(end)
print('{}'.format(mem))