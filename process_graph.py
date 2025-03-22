import json

file_path = "/Users/ravikanth/Downloads/DV_Major_assignment_3/Emails_Graph.json"

# Open the JSON file in read mode
with open(file_path, 'r') as f:
    # Load the data from the file into a Python dictionary
    data = json.load(f)

# Print the keys of the dictionary to understand its structure
print(data.keys())
import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
for node in data['nodes']:
    G.add_node(node['id'], degree=node['degree'])

# Add edges (links) to the graph
for link in data['links']:
    G.add_edge(link['source'], link['target'])

# Print basic information about the graph
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
import matplotlib.pyplot as plt

# Draw the graph
nx.draw(G, with_labels=True, node_size=50, font_size=8, alpha=0.8)
plt.title("Email Communication Network")
plt.show()
# Degree Centrality
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)
print("Betweenness Centrality:", betweenness_centrality)

# Clustering Coefficient
clustering_coefficient = nx.average_clustering(G)
print("Average Clustering Coefficient:", clustering_coefficient)
import community as community_louvain

# Detect communities using the Louvain algorithm
partition = community_louvain.best_partition(G)

# Add community and cluster_label to each node
for node in data['nodes']:
    node['community'] = partition[node['id']]
    node['cluster_label'] = str(partition[node['id']])  # Convert to string if needed

# Save the updated JSON file
with open('Emails_Graph_updated.json', 'w') as f:
    json.dump(data, f, indent=4)

# Save the updated JSON file
with open('Emails_Graph_updated.json', 'w') as f:
    json.dump(data, f, indent=4)