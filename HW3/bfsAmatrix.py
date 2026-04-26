'''
CS 361 HW 3
Kiana Tarter
Implementation of BFS on an adjacency matrix 
'''
from collections import deque
import time
import tracemalloc
tracemalloc.start()


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

start = time.perf_counter()
def BFS_matrix(matrix, nodes, src):
    
    index = {node: i for i, node in enumerate(nodes)}

    visited = set([src])
    q = deque([src])
    solution = []

    while q:
        node = q.popleft()
        solution.append(node)
        i = index[node]

        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                neighbor = nodes[j]

                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
    return solution  
end = time.perf_counter() 

 

def main():
    elapsed_time = end - start
    print(elapsed_time)

    result = BFS_matrix(matrix, nodes, '1')

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Result:", result)
    print("Memory (peak):", peak, "bytes")
    print(BFS_matrix(matrix, nodes, '1'))

if __name__ == "__main__":
    main()        
