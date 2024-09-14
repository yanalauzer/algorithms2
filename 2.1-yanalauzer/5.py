import unittest


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

class MaxSumTest(unittest.TestCase):
    def test_example(self):
        expected_result = [1, 2, 3]
        number_of_elements = len(expected_result)
        actual_result = find_maximum_summands(3)
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(number_of_elements, 3)

if __name__ == '__main__':
    unittest.main()
