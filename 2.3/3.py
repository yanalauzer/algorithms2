def has_cycle(graph):
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
            return True

    return False


filename = "input.txt"
graph = {}
with open(filename, 'r') as file:
    vertices, edges = map(int, file.readline().split())
    for _ in range(edges):
        u, v = map(int, file.readline().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

with open('output.txt', 'w') as file:
  if has_cycle(graph):
    file.write('1')
  else:
    file.write('0')
