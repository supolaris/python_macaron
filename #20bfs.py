graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8', '4'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []
queued = []

def bfs(visited, graph, node):
    visited.append(node)
    queued.append(node)

    while queued:
        m = queued.pop(0)
        print(m, end = ' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queued.append(neighbour)

print("Print the bfs")
bfs(visited, graph, '5')
