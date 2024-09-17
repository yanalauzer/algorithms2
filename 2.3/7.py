import unittest
def laba3(num_vertices, edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    def is_bipartite(graph):
        color = {}
        visited = set()

        def dfs(vertex, current_color):
            color[vertex] = current_color
            next_color = 1 - current_color
            for neighbor in graph.get(vertex, []):
                if neighbor in color:
                    if color[neighbor] == current_color:
                        return False
                else:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        if not dfs(neighbor, next_color):
                            return False
            return True

        for vertex in graph:
            if vertex not in visited:
                visited.add(vertex)
                if not dfs(vertex, 0):
                    return 0
        return 1

    return is_bipartite(graph)


class TestLaba3(unittest.TestCase):
    def test_laba3(self):
        num_vertices = 5
        edges = [(4,4), (1,2), (4,1), (2,3), (3,1)]
        result = laba3(num_vertices, edges)
        print(result)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
