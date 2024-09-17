import math
import time
import resource
import unittest
# mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# start = time.time()

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


    return total_value

def main(n,W, items):

    result = fractional_knapsack(n, W, items)
    print(math.ceil(result))
    return result


class FractionalKnapsackTest(unittest.TestCase):
    def test_fractional_knapsack(self):
        result = main(3, 50, [(60, 20), (100, 50), (120, 30)])
        self.assertEqual(result, 180.0000)


if __name__ == '__main__':
    unittest.main()
