from collections import defaultdict


def check_path_correctness( corridors, path):
    graph = defaultdict(list)
    for u, v, c in corridors:
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


with open("input.txt", 'r') as file:
    n, m = map(int, file.readline().split())
    corridors = [tuple(map(int, file.readline().split())) for _ in range(m)]
    path_length = int(file.readline())
    path = list(map(int, file.readline().split()))

result = check_path_correctness(corridors, path)

with open("output.txt", 'w') as file:
    file.write(str(result))

