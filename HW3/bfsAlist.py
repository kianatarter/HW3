'''
CS 361 HW 3
Kiana Tarter
Implementation of BFS on graph A using an adjacency list

'''
from queue import Queue
from collections import deque
import time
import tracemalloc

graph = {
    '1': ['2', '3', '4'],
    '3': ['0', '1', '5'],
    '2': ['0', '1'],
    '4': ['1', '6'],
    '5': ['3', '7'],
    '0': ['2', '3', '7', '8'],
    '6': ['4', '9', '11'],
    '7': ['0', '5'], '8': ['0', '10'],
    '9': ['6', '11'],
    '10': ['8'],
    '11' : ['6', '9']
}



def BFS(graph, src, target):
    visited = set()
    q = deque([(src, [src])])
    nodes_visited = 0

    while q:
        current, path = q.popleft()

        if current not in visited:
            visited.add(current)
            nodes_visited += 1

            if current == target:
                return path, nodes_visited

            for neighbor in graph[current]:
                if neighbor not in visited:
                    q.append((neighbor, path + [neighbor]))

    return None, nodes_visited

import time
import tracemalloc

def benchmark(algorithm, *args):
    times = []
    memories = []
    result = None

    for _ in range(5):
        tracemalloc.start()
        start = time.perf_counter()

        result = algorithm(*args)

        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append(end - start)
        memories.append(peak)

    avg_time = sum(times) / len(times)
    avg_memory = sum(memories) / len(memories)

    return result, avg_time, avg_memory

def main():
    result, avg_time, avg_memory = benchmark(BFS, graph, '0', '7')

    path, nodes_visited = result

    print("BFS Adjacency List - Graph A")
    print("Path:", path)
    print("Nodes visited before reaching target:", nodes_visited)
    print("Average time:", avg_time)
    print("Average memory:", avg_memory, "bytes")

if __name__ == "__main__":
    main()


  




