import numpy as np

# not efficient
def solve(graph):
    connections = np.zeros((len(graph), len(graph)))
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            connections[node, neighbor] = 1
    closure = connections
    for _ in range(len(graph)):
        connections = connections @ closure
        closure += connections
    return np.minimum(closure, 1)


graph = [[0, 1, 3], [1, 2], [2], [3]]
print(solve(graph))
