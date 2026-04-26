

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

nodes = sorted(graph.keys())
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

def main():
    print(DFS_matrix(matrix, nodes, 'A'))

if __name__ == "__main__":
    main()  
