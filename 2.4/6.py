def laba4(s):
    zf = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        if i <= right:
            zf[i] = min(right - i, zf[i - left])
        while i + zf[i] < len(s) and s[zf[i]] == s[i + zf[i]]:
            zf[i] = zf[i] + 1
        if i + zf[i] > right:
            left = i
            right = i + zf[i]
    return zf

import unittest

class TestLaba4(unittest.TestCase):
    def test_laba4(self):
        s = "abacaba"
        result = laba4(s)
        self.assertEqual(result, [0, 0, 1, 0, 3, 0, 1])
        print(result)

if __name__ == '__main__':
    unittest.main()