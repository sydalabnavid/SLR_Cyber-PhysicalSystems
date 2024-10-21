
import networkx as nx
import matplotlib.pyplot as plt

# Rebuild the co-citation graph (G) and cluster names based on the previous computation
def draw_co_citation_network(G, cluster_names):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.15)
    clusters = {node: cluster for cluster, nodes in cluster_names.items() for node in nodes}
    
    # Draw the nodes, colors based on clusters
    nx.draw_networkx_nodes(G, pos, node_size=500, cmap=plt.cm.viridis, node_color=[clusters.get(node, 0) for node in G.nodes()])
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    
    # Label nodes by cluster name
    nx.draw_networkx_labels(G, pos, {node: f"Cluster {clusters.get(node, 'Unknown')}" for node in G.nodes()}, font_size=8)
    
    plt.title("Co-Citation Network with Cluster Names", size=15)
    plt.show()

# Example call
# draw_co_citation_network(G, cluster_names) 
