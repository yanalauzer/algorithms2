import unittest


def laba2(input_lines):
    rez = []
    output_lines = []

    for line in input_lines:
        s = line.split()
        if s[0] == "+1":  # Записывает число в rez
            rez.append(int(s[1]))
            rez.sort()
        elif s[0] == "0":  # Находит последний элемент в rez и записывает его в output
            last_index = len(rez) - int(s[1])
            if last_index >= 0:
                output_lines.append(str(rez[last_index]))
        elif s[0] == "-1":  # удаляет число из списка rez
            rez.remove(int(s[1]))

    return output_lines


class Laba2Test(unittest.TestCase):
    def test_laba2(self):
        input_data = [
            "+1 5",
            "+1 3",
            "+1 7",
            "0 1",
            "0 2",
            "0 3",
            "-1 5",
            "+1 10",
            "0 1",
            "0 2",
            "0 3"
        ]
        expected_output = ["7", "5", "3", "10", "7", "3"]
        result = laba2(input_data)
        print(result)
        self.assertListEqual(expected_output, result)


if __name__ == '__main__':
    unittest.main()
