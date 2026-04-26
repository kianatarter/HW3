'''
CS 361 HW 3
Kiana Tarter
Implementation of BFS on graph A using an adjacency list

'''
from queue import Queue
from collections import deque
graph = {
    '1': ['2', '3', '4'],
    '3': ['0', '1', '5'],
    '2': ['0', '1'],
    '4': ['1', '6'],
    '5': ['3', '7'],
    '0': ['2', '3', '7', '8'],
    '6': ['4', '9', '11'],
    '7': ['0', '5'],
}



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

def main():
    print(BFS(graph, '1'))

if __name__ == "__main__":
    main()


  




