f = open('input.txt')
t2 = f.readline()
t1 = t2[:len(t2) - 1]
p1 = f.readline()


def NaiveStringMatcher(t, p):
    n = len(t)
    m = len(p)
    ans = []
    for i in range(n - m + 1):
        if t[i:i + m] == p:
            ans.append(i + 1)
    return ans


z = open('output.txt', 'w')
itog = NaiveStringMatcher(p1, t1)
z.write(str(len(itog)) + '\n')
itog.sort()
for i in itog:
    z.write(str(i) + ' ')
