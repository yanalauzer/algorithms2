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


class MaxSumTest(unittest.TestCase):
    def test_example(self):
        expected_result = [1, 2]
        result = find_maximum_summands(3)
        self.assertEqual(result, expected_result)
        print(result)


if __name__ == '__main__':
    unittest.main()