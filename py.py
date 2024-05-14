import heapq
class Node:
    def __init__(self,state,g_cost,h_cost):
        self.state=state
        self.g_cost=g_cost
        self.h_cost=h_cost
        self.f_cost=g_cost+h_cost

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def astar(initial_state,goal_state,successor,heuristic):
    visited=set()
    frontier=[]
    heapq.heappush(frontier,Node(initial_state,0,heuristic(initial_state)))
    
    while frontier:
        current_node=heapq.heappop(frontier)
        current_state=current_node.state
        
        if current_state is visited:
            continue
        visited.add(current_state)
        
        
        if current_state==goal_state:
            return current_node
        
        for successor_state , cost in successor(current_state):
            if successor_state not in visited:
                g_cost=current_node.g_cost+cost
                h_cost=heuristic(successor_state)
                heapq.heappop(frontier,Node(successor_state,g_cost,h_cost))
    return None



def heuristic(state):
    return 0


def successor(state):
    return [(state+1,1),(state+2,1)]


initial_state=0
goal_state=5


result_node=astar(initial_state,goal_state,successor,heuristic)
if result_node:
    print("Goal found at state: ",result_node.state)
    print("Total_cost:",result_node.f_cost)
    
else:
    print("Goal not found at state: ",result_node.state)
    