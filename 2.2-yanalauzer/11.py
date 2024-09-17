import unittest


def laba2(operations):
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, key):
            self.root = self._insert(self.root, key)

        def _insert(self, node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = self._insert(node.left, key)
            elif key > node.key:
                node.right = self._insert(node.right, key)
            return node

        def exists(self, key):
            return self._exists(self.root, key)

        def _exists(self, node, key):
            if not node:
                return False
            if node.key == key:
                return True
            return self._exists(node.left, key) if key < node.key else self._exists(node.right, key)

        def next(self, key):
            return self._next(self.root, key)

        def _next(self, node, key):
            if not node:
                return None
            if key < node.key:
                left_result = self._next(node.left, key)
                return node.key if left_result is None or left_result <= key else left_result
            return self._next(node.right, key)

        def prev(self, key):
            return self._prev(self.root, key)

        def _prev(self, node, key):
            if not node:
                return None
            if key > node.key:
                right_result = self._prev(node.right, key)
                return node.key if right_result is None or right_result >= key else right_result
            return self._prev(node.left, key)

    bst = BinarySearchTree()
    results = []
    for operation, key in operations:
        key = int(key)
        if operation == 'insert':
            bst.insert(key)
        elif operation == 'delete':
            pass
        elif operation == 'exists':
            results.append('true' if bst.exists(key) else 'false')
        elif operation == 'next':
            result = bst.next(key)
            results.append(str(result) if result is not None else 'none')
        elif operation == 'prev':
            result = bst.prev(key)
            results.append(str(result) if result is not None else 'none')
    return results


class TestLaba2(unittest.TestCase):
    def test_laba2(self):
        operations = [
            ('insert', 2),
            ('insert', 5),
            ('insert', 3),
            ('exists', 2),
            ('exists', 4),
            ('next', 4),
            ('prev', 4),
            ('delete', 5),
            ('next', 4),
            ('prev', 4)
        ]
        expected_results = [
            'true',
            'false',
            '5',
            '3',
            '5',
            '3'
        ]
        results = laba2(operations)
        print(results)
        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()
