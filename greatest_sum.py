#traveling salesman greedy heuristic prioritizing end node
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

values = {
    'A': 3,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 7,
    'F': 2
}

edges = [
    ('A', 'B'),
    ('A', 'D'),
    ('B', 'D'),
    ('B', 'E'),
    ('D', 'E'),
    ('D', 'F'),
    ('E', 'F'),
    ('E', 'C'),
    ('F', 'C')
]

start = 'A'
end = 'C'

visited = set()
path = []
current_node = start
total_sum = 0

while current_node != end:
    visited.add(current_node)
    path.append(current_node)
    total_sum += values[current_node]

    # Find the next node with the highest value
    next_node = None
    highest_value = float('-inf')
    for edge in edges:
        if current_node in edge:
            neighbor = edge[1 - edge.index(current_node)]
            if neighbor not in visited:
                if neighbor == end:
                    next_node = neighbor
                    highest_value = values[neighbor]
                    break  # Prioritize reaching the end node
                elif values[neighbor] > highest_value:
                    next_node = neighbor
                    highest_value = values[neighbor]
    
    if next_node is None:
        # If no unvisited neighbors,find the next unvisited node
        unvisited_neighbors = [(edge[1 - edge.index(node)], values[edge[1 - edge.index(node)]]) 
                               for edge in edges for node in path 
                               if node in edge and edge[1 - edge.index(node)] not in visited]
        if not unvisited_neighbors:
            print("No path found to connect all nodes.")
            break
        next_node = max(unvisited_neighbors, key=lambda x: x[1])[0]
    
    current_node = next_node

# Add the end node to the path
if current_node == end:
    path.append(current_node)
    total_sum += values[current_node]

disp = " -> ".join(path)

print("Greatest Path Sum from", start, "to", end, "is", total_sum)
print("Path:", disp)
