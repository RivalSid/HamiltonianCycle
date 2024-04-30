import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')

# Draw the graph with red edges
nx.draw(G, with_labels=True, edge_color='red')

# Show the plot
plt.show()
