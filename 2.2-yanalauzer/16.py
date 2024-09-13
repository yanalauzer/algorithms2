f = open("input.txt")
n = int(f.readline())
rez = []
z = open("output.txt", "w")
for i in range(n):
    s = f.readline().split()
    if s[0] == "+1":   # Записывает число в rez
        rez.append(int(s[1]))
        rez.sort()
    elif s[0] == "0":     # Находит последний элемент в rez и записывает его в output
        z.write(str(rez[len(rez) - int(s[1])]) + "\n")
    elif s[0] == "-1":   #удаляет число из списка rez
        rez.remove(int(s[1]))
