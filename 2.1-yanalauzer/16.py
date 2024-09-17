from itertools import permutations
import unittest


def tsp(distances):
    n = len(distances)  # Определяет количество городов (число списков в distances).
    min_distance = float(
        'inf')  # Инициализирует переменную min_distance максимально возможным значением (бесконечность),
    # чтобы мы могли сравнивать ее с длинами маршрутов и находить минимальное значение.
    best_order = None  # хранится оптимальный порядок посещения городов.

    for order in permutations(range(1, n)):  # цикл, который перебирает все возможные перестановки номеров городов
        # (от 1 до n - 1, так как 0 - это начальный город).
        total_distance = distances[0][
            order[0]]  # вычисляет начальное расстояние от первого города до первого города в текущей перестановке.
        for i in range(len(order) - 1):
            total_distance += distances[order[i]][order[
                i + 1]]  # вычисляет суммарное расстояние по всем последовательным парам городов в текущей перестановке.
        total_distance += distances[order[-1]][
            0]  # Добавляет расстояние от последнего города в перестановке до исходного города.

        if total_distance < min_distance:  # является ли текущее расстояние меньше предыдущего минимума.
            min_distance = total_distance
            best_order = (0,) + order

    return min_distance, best_order


# with open("input.txt", "r") as f:
#     n = int(f.readline())
#     distances = []
#     for _ in range(n):
#         distances.append([int(x) for x in f.readline().split()])
#
# min_distance, best_order = tsp(distances)
# print(tsp(distances))
#
# with open("output.txt", "w") as f:
#     f.write(str(min_distance) + "\n")
#     f.write(" ".join([str(x) for x in best_order]))


class TestDistance(unittest.TestCase):
    def test_distance(self):
        distances = [[0, 183, 163, 173, 181],
                     [183, 0, 165, 172, 171],
                     [163, 165, 0, 189, 302],
                     [173, 172, 189, 0, 167],
                     [181, 171, 302, 167, 0]]
        min_distance, best_order = tsp(distances)
        self.assertEqual(min_distance, 839)
        self.assertEqual(best_order, (0, 2, 1, 4, 3))
        print(tsp(distances))


if __name__ == '__main__':
    unittest.main()
