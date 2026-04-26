'''
CS 361 HW 3
Kiana Tarter
Implementation of DFS on an adjacency matrix 
'''
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
