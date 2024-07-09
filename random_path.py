import random

nodes = ['A', 'B', 'C', 'D', 'E', 'F']

values = {
    'A': 3,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 7,
    'F': 2
}

edges = {
    ('A', 'B'): 2,
    ('A', 'D'): 8,
    ('B', 'D'): 5,
    ('B', 'E'): 6,
    ('D', 'E'): 3,
    ('D', 'F'): 2,
    ('E', 'F'): 1,
    ('E', 'C'): 9,
    ('F', 'C'): 3
}

start = 'A'
end = 'C'

#initialize variables for path finding
visited = set()
path = []
current_node = start

while current_node != end:
    visited.add(current_node)
    path.append(current_node)

    #get neighbors of current node
    neighbors = [edge[1 - edge.index(current_node)] for edge in edges if current_node in edge]

    #randomly select the next node from neighbors (excluding visited nodes)
    unvisited_neighbors = [node for node in neighbors if node not in visited]
    if unvisited_neighbors:
        next_node = random.choice(unvisited_neighbors)
    else:
        print("No unvisited neighbors to continue the path.")
        break

    current_node = next_node

#add the end node to the path
path.append(end)

#calculate path sum (distance in terms of number of edges)
path_sum = sum(edges[(path[i], path[i+1])] for i in range(len(path)-1))

disp = " -> ".join(path)

print()
print(disp)
print("Distance:", path_sum)
print("Path Sum:", sum(values[node] for node in path))
print()
