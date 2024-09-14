import time
import unittest
import resource
mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
start = time.time()


def is_almost_palindrome(word, k):
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - 1 - i]:
            k -= 1
            if k < 0:
                return False
    return True


def count_almost_palindromes(word, k):
    count = 0
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substring = word[i:j]
            if is_almost_palindrome(substring, k):
                count += 1
    return count


with open("input.txt", "r") as f:
    n, k = map(int, f.readline().split())
    word = f.readline().strip()

count = count_almost_palindromes(word, k)

with open("output.txt", "w") as f:
    f.write(str(count))


end = time.time() - start
print(end)
print('{}'.format(mem))

class AlmostPalindromeTest(unittest.TestCase):
    def test_count_almost_palindromes(self):
        expected_result = [6]
        actual_result = count_almost_palindromes('aaa', 3)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()