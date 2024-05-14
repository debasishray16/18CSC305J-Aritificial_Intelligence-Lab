from collections import deque

def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
            
            
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    
    while queue:
        node=queue.popleft()
        print(node,end=' ')
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

start_node='A'
print("DFS")
dfs(graph, start_node)
bfs(graph, start_node)