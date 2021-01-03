import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict 

G = nx.Graph()
connexions = [
    ["DSM", "ORD"],
	["ORD", "BGI"],
	["BGI", "LGA"],
	["SIN", "CDG"],
	["CDG", "BUG"],
	["DEL", "DOH"],
	["DEL", "CDG"],
	["TLV", "DEL"],
	["EWR", "HND"],
	["HND", "ICN"],
	["ICN", "JFK"],	
	["JFK", "LGA"],
	["EYW", "LHR"],	
	["LHR", "SFO"],
	["SFO", "SAN"],	
	["SFO", "DSM"],
	["SAN", "EYW"]  ]

for pts in connexions:
    G.add_edge(pts[0], pts[1])
    graphtest = defaultdict(list)
for connexion in connexions: 
        a, b = connexion[0], connexion[1] 
        # Creating the graph  
        # as adjacency list 
        graphtest[a].append(b)
        graphtest[b].append(a)
path_edges = zip(path, path[1:])
path_edges = set(path_edges)
pos = nx.spring_layout(G)

nx.draw(G, pos, node_color='lawngreen', with_labels = True)
plt.show()    

def short_Path(G, start, goal): 
    explored = [] 
      
    # Queue for traversing the  
    # graph in the short_Path 
    queue = [[start]] 
      
    # test if the desired node is  
    # the same as the start node 
    if start == goal: 
        print("Same Node") 
        return
      
    # Loop to traverse the graph  
    # with the help of the queue 
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
          
        # Codition to check if the 
        # current node is not visited 
        if node not in explored: 
            neighbours = graph[node] 
              
            # Loop to iterate over the  
            # neighbours of the node 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                  
                # Condition to check if the  
                # neighbour node is the goal 
                if neighbour == goal: 
                    print("Shortest path = ", *new_path) 
                    return
            explored.append(node) 
  
    # Condition when the nodes  
    # are not connected 
    print("So sorry, but this connecting path doesn't exist :(") 
    return
 # Graph using dictionaries 
graph2 = graphtest
graph1 = G

      
 # Function Call 
short_Path(graph1, 'LGA', 'DSM') 
short_Path(graph2, 'DSM', 'LGA') 

short_Path(graph1, 'DSM', 'LGA') 
short_Path(graph2, 'LGA', 'DSM') 