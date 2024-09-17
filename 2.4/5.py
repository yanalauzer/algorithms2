def laba4(s):
    def PrefixFunction(s):
        p = [0] * len(s)
        for i in range(1, len(s)):
            k = p[i - 1]
            while k > 0 and s[i] != s[k]:
                k = p[k - 1]
            if s[i] == s[k]:
                k += 1
            p[i] = k
        return p

    return PrefixFunction(s)

import unittest

class TestLaba4(unittest.TestCase):
    def test_laba4(self):
        s = "aaaAAA"
        result = laba4(s)
        self.assertEqual(result, [0, 1, 2, 0, 0, 0])
        print(result)

if __name__ == '__main__':
    unittest.main()