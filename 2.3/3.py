import unittest

def laba3(vertices, edges, graph_data):
    graph = {}
    for u, v in graph_data:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    visited = set()
    rec_stack = set()

    def dfs(vertex):
        if vertex in rec_stack:
            return True
        if vertex in visited:
            return False

        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor in graph.get(vertex, []):
            if dfs(neighbor):
                return True

        rec_stack.remove(vertex)
        return False

    for vertex in graph:
        if dfs(vertex):
            return 1

    return 0

# Example usage:
# graph_data = [(4, 4), (1,2), (3,2), (4, 3), (1,4), (1,4)]
# result = laba3(4, 4, graph_data)
# print(result)



class TestLaba3(unittest.TestCase):
    def test_cycle_detection(self):

        graph_data = [(4, 4), (1,2), (3,2), (4, 3), (1,4), (1,4)]
        result = laba3(4, 4, graph_data)
        print(result)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()