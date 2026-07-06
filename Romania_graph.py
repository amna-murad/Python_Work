
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Romania Graph
romania_graph = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni']
}

def bfs(graph, start, goal):
    queue = deque()
    visited = set()
    parent = {}
    
    queue.append(start)
    visited.add(start)
    parent[start] = None
    
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    return parent

def get_path(parent, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    return path[::-1]

# RUN BFS
parent_bfs = bfs(romania_graph, 'Sibiu', 'Bucharest')
bfs_path = get_path(parent_bfs, 'Bucharest')
print("BFS Path:", " → ".join(bfs_path))

# Create NetworkX graph
G = nx.Graph(romania_graph)

# Draw full Romania map
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=2000, font_size=10, font_weight='bold', width=2)
plt.title("Romania Map - Full Graph")
plt.show()

# Highlight BFS path
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightgray', 
        node_size=2000, font_size=10, font_weight='bold', width=0.5)
nx.draw_networkx_edges(G, pos, edgelist=[(bfs_path[i], bfs_path[i+1]) for i in range(len(bfs_path)-1)], 
                       edge_color='red', width=4)
nx.draw_networkx_nodes(G, pos, nodelist=bfs_path, node_color='red', node_size=2500)
plt.title("BFS Path: Sibiu → " + " → ".join(bfs_path))
plt.show()
