'''
CS 361 HW 3
Kiana Tarter
Implementation of DFS on graph A using an adjacency list

'''
graph = {
    '1': ['2', '3', '4'],
    '3': ['0', '1', '5'],
    '2': ['0', '1'],
    '4': ['1', '6'],
    '5': ['3', '7'],
    '0': ['2', '3', '7', '8'],
    '6': ['4', '9', '11'],
    '7': ['0', '5'],
    '8': ['0', '10'],
    '9': ['6', '11'],
    '10': ['8'],
    '11' : ['6', '9']
}

def DFS(graph,node,visited = None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)


DFS(graph, '1')