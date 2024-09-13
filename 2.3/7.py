def is_bipartite(graph):
    color = {}

    def dfs(vertex, current_color):
        color[vertex] = current_color
        next_color = 1 - current_color
        for neighbor in graph.get(vertex, []):
            if neighbor in color:
                if color[neighbor] == current_color:
                    return False
            else:
                if not dfs(neighbor, next_color):
                    return False
        return True

    for vertex in graph:
        if vertex not in color:
            if not dfs(vertex, 0):
                return 0
    return 1


filename = "input.txt"
graph = {}
with open(filename, 'r') as file:
    num_vertices, num_edges = map(int, file.readline().split())
    for _ in range(num_edges):
        u, v = map(int, file.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

result = is_bipartite(graph)
with open('output.txt', 'w') as file:
    file.write(str(result))