import random
import networkx as nx
import pickle


edges = {}
p = 0.12

max_length = 15

num_nodes = 5000

for src in range(num_nodes):
    for dst in range(src + 1, num_nodes):
        if random.random() <= p:
            edges[(src,dst)] = random.randint(2,max_length)
            edges[(dst,src)] = edges[(src,dst)]

G = nx.Graph()
G.add_weighted_edges_from([(src,dest,edges[(src,dest)]) for src,dest in edges.keys() if src < dest])
print(f'Number of connected components: {nx.algorithms.number_connected_components(G)}')
print(f'Shortest path from node 0 to node 42: {nx.dijkstra_path(G,0,42,"weight")} with distance of {nx.shortest_path_length(G, source=0, target=42, weight="weight")}')

with open('jenn_graph_other.pkl', 'wb') as f:
    pickle.dump(edges, f)
