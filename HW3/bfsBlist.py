'''
CS 361 HW 3
Kiana Tarter
Implementation of BFS on graph B using an adjacency list

'''
from queue import Queue
from collections import deque
import time
import tracemalloc
tracemalloc.start()

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

start = time.perf_counter()
def BFS(graph, src):
    visited = set()
    q = deque([src])
    solution = []

    while (q):
        current = q.popleft()

        if current not in visited:
            visited.add(current)
            solution.append(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    q.append(neighbor)

    return solution

end = time.perf_counter()

def main():
    elp = end - start
    print(elp)
    print(BFS(graph, 'A'))

if __name__ == "__main__":
    main()