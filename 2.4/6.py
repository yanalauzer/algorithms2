def zfunction(s):
    zf = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        zf[i] = max(0, min(right - i, zf[i - left]))
        while i + zf[i] < len(s) and s[zf[i]] == s[i + zf[i]]:   # В этом цикле мы ищем наибольший префикс-суффикс, начинающийся с позиции i.
            zf[i] = zf[i] + 1  # Если найдено совпадение, мы увеличиваем zf[i] на 1.
        if i + zf[i] > right:
            left = i
            right = i + zf[i]
    return zf


f = open('input.txt')
stroka1 = f.readline()
stroka = stroka1[:len(stroka1)]
rez = zfunction(stroka)  # Вызов функции zfunction для получения z-функции строки stroka.
with open('output.txt', 'w') as z:
    for i in range(1, len(rez)):
        z.write(str(rez[i]) + ' ')
