import time
start = time.perf_counter()
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['D'],
    'D': ['E'],
    'E': ['K', 'F'],
    'F': ['M', 'H', 'G'],
    'G': ['K', 'N', 'L', 'H'],
    'H': ['I'],
    'M': ['O'],
    'N': ['O'],
    'K': ['L'],
    'I' : ['J'],
    'O' : [],
    'L' : [],
    'J' : ['D']

}

def DFS(graph,node,visited = None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

end = time.perf_counter()
print(end-start)

DFS(graph, 'A')

