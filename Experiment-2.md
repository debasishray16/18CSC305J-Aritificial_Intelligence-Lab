# Real World Problem (Graph Coloring)

Graph coloring is a problem in graph theory and computer science that aims to assign colors to the vertices of a graph in such a way that no two adjacent vertices share the same color. The minimum number of colors needed to accomplish this is called the chromatic number of the graph.

1. Greedy Coloring Algorithm:

The greedy coloring algorithm is one of the simplest and most commonly used algorithms to solve the graph coloring problem. It works by iteratively assigning colors to the vertices of the graph, one vertex at a time, in a greedy manner.

```py
def greedyColoring(adj, V):
    result = [-1] * V
    result[0] = 0

    for u in range(1, V):
        available = {result[i] for i in adj[u]}
        result[u] = next(cr for cr in range(V) if cr not in available)

    for u, color in enumerate(result):
        print(f"Vertex {u} ---> Color {color}")



if __name__ == '__main__':
    g1 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
    print("Coloring of graph 1 ")
    greedyColoring(g1, 5)

    g2 = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 4), (4, 3)]
    print("\nColoring of graph 2")
    greedyColoring(g2, 5)
```


# Simple Agent Problem

```py

def simple_reflex_agent(location , status):

    if status=="Hungry":
        print("Looking for food...")
        if location=="Home":
            print("Found food at home.")
        else:
            print("Looking for a restaurent nearby.")
    

    elif status=="Tired":
        print("Looking for a place to rest...")
        if location=="Home":
            print("Going to bed.")
        else:
            print("Looking for a hotel nearby.")
    

    else:
        print("Doing nothing")
    
simple_reflex_agent("Home","Hungry")
simple_reflex_agent("Park","Tired")
simple_reflex_agent("Office","Normal")
```