import unittest

def laba2(n, tree):
    tree_version = [[-1] * 3 for _ in range(n)]
    for i in range(n):
        tree_version[i][0] = tree[i][0]
        if tree[i][1] != -1:
            tree_version[tree[i][1]][1] = i
        if tree[i][2] != -1:
            tree_version[tree[i][2]][2] = i
    top = 0  #корень
    postorder_result = []
    preorder_result = []
    inorder_result = []

    def postorder(v, x1, result):
        if v[x1][1] != -1:
            postorder(v, v[x1][1], result)
        if v[x1][2] != -1:
            postorder(v, v[x1][2], result)
        result.append(v[x1][0])

    def preorder(v, x1, result):
        result.append(v[x1][0])
        if v[x1][1] != -1:
            preorder(v, v[x1][1], result)
        if v[x1][2] != -1:
            preorder(v, v[x1][2], result)

    def inorder(v, x1, result):
        if v[x1][1] != -1:
            inorder(v, v[x1][1], result)
        result.append(v[x1][0])
        if v[x1][2] != -1:
            inorder(v, v[x1][2], result)

    postorder(tree_version, top, postorder_result)
    preorder(tree_version, top, preorder_result)
    inorder(tree_version, top, inorder_result)
    return postorder_result, preorder_result, inorder_result


class TreeTraversalTest(unittest.TestCase):
    def test_laba2(self):
        n = 5
        tree = [
            [4, 1, 2],
            [2, 3, 4],
            [5, -1, -1],
            [1, -1, -1],
            [3, -1, -1]
        ]
        expected_postorder = [1, 3, 2, 5, 4]
        expected_preorder = [4, 2, 1, 3, 5]
        expected_inorder = [1, 3, 2, 5, 4]
        postorder_result, preorder_result, inorder_result = laba2(n, tree)
        print("Postorder:", postorder_result)
        print("Preorder:", preorder_result)
        print("Inorder:", inorder_result)
        self.assertListEqual(postorder_result, expected_postorder)
        self.assertListEqual(preorder_result, expected_preorder)
        self.assertListEqual(inorder_result, expected_inorder)


if __name__ == '__main__':
    unittest.main()