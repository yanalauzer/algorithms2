f = open("input.txt")
n = int(f.readline())
tree = []
tree_version = [[-1] * 3 for _ in range(n)]
for i in range(n):
    s = f.readline().split()
    x = [int(i) for i in s]
    tree.append(x)
print(tree)
for i in range(n):
    tree_version[i][0] = tree[i][0]
    if tree[i][1] != -1:
        tree_version[tree[i][1]][1] = i
    if tree[i][2] != -1:
        tree_version[tree[i][2]][2] = i
top = -1
b = []
a = []
c = []
for i in range(n):
    if tree_version[i][1] == -1 and tree_version[i][2] == -1:
        top = i
print(tree_version, top)


def inorder(v, x1):
    if v[x1][1] != -1:
        inorder(v, v[x1][1])
    a.append(v[x1][0])
    if v[x1][2] != -1:
        inorder(v, v[x1][2])
    return a


def preorder(v, x1):
    b.append(v[x1][0])
    if v[x1][1] != -1:
        preorder(v, v[x1][1])
    if v[x1][2] != -1:
        preorder(v, v[x1][2])
    return b


def postorder(v, x1):
    if v[x1][1] != -1:
        postorder(v, v[x1][1])
    if v[x1][2] != -1:
        postorder(v, v[x1][2])
    c.append(v[x1][0])
    return c


z = open("output.txt", "w")
a1 = (postorder(tree, top))
a2 = (preorder(tree, top))
a3 = (inorder(tree, top))
for i in a1:
    z.write(str(i) + " ")
z.write("\n")
for i in a2:
    z.write(str(i) + " ")
z.write("\n")
for i in a3:
    z.write(str(i) + " ")
