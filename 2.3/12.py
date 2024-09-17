import unittest

def laba3(n, m, corridors, path_length, path):
    graph = {}
    for u, v, c in corridors:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, c))
        graph[v].append((u, c))

    current_room = 1

    for color in path:
        next_room = None

        for room, corridor_color in graph[current_room]:
            if corridor_color == color:
                next_room = room
                break

        if next_room is None:
            return "INCORRECT"
        current_room = next_room
    return current_room

class PathCorrectnessTest(unittest.TestCase):
    def test_path_invalid(self):
        n = 3
        m = 2
        corridors = [(1, 2, 10), (1, 3, 5)]
        path_length = 5
        path = [10, 10, 10, 10, 5]
        result = laba3(n, m, corridors, path_length, path)
        print(f"Result: {result}")
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()