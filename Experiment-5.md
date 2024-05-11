# Best-First Search

```py
import heapq

def best_first_search(graph, start, goal):
    visited = set()
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        if node == goal:
            return True
        
        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (edge_cost, neighbor))
    
    return False

# Example graph represented as an adjacency list with edge costs
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 5), ('E', 4)],
    'C': [('F', 7)],
    'D': [],
    'E': [('G', 6)],
    'F': [('H', 3)],
    'G': [],
    'H': []
}

start_node = 'A'
goal_node = 'G'

print("Is there a path from", start_node, "to", goal_node, "?", best_first_search(graph, start_node, goal_node))

```