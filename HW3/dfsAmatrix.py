'''
CS 361 HW 3
Kiana Tarter
Implementation of DFS on an adjacency matrix 
'''
from collections import deque
import time
start = time.perf_counter()
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


nodes = sorted(graph.keys(), key = int)
index = {node: i for i, node in enumerate(nodes)}

n = len(nodes)
matrix = [[0]*n for _ in range(n)]

for x in graph:
    for y in graph[x]:
        matrix[index[x]][index[y]] = 1
        matrix[index[y]][index[x]] = 1

def DFS_matrix(matrix, nodes, src):
    index = {node: i for i, node in enumerate(nodes)}

    visited = set()
    stack = [src]
    solution = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            solution.append(node)

            i = index[node]

            for j in reversed(range(len(matrix))):
                if matrix[i][j] == 1:
                    neighbor = nodes[j]

                    if neighbor not in visited:
                        stack.append(neighbor)
    return solution
end = time.perf_counter()

def main():
    print(end-start)
    print(DFS_matrix(matrix, nodes, '1'))

if __name__ == "__main__":
    main() 
