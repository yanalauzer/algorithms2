f = open('input.txt')
st = f.readline()


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


z = open('output.txt', 'w')
itog = PrefixFunction(st)
for i in itog:
    z.write(str(i) + ' ')
