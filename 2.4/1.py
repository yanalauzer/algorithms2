import unittest


def laba4(t, p):
    n = len(t)
    m = len(p)
    ans = []
    for i in range(n - m + 1):
        if t[i:i + m] == p:
            ans.append(i + 1)
    return ans


class TestLaba4(unittest.TestCase):
    def test_laba4(self):
        t = "abaCaba"
        p = "aba"
        result = laba4(t, p)
        result.sort()
        self.assertEqual(result, [1, 5])
        self.assertEqual(len(result), 2)
        print(len(result))
        print(result)



if __name__ == '__main__':
    unittest.main()
