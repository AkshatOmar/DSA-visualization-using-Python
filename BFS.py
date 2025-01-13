import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

def visualize_tree_2d(graph):
    """Visualize the tree in 2D."""
    pos = nx.spring_layout(graph)  # Layout for 2D visualization
    plt.figure(figsize=(10, 7))
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold")
    plt.title("2D Tree Visualization", fontsize=20)
    plt.show()

def visualize_tree_3d(graph):
    """Visualize the tree in 3D."""
    pos_2d = nx.spring_layout(graph)  # Get 2D layout
    pos_3d = {node: (x, y, 0.5 * i) for i, (node, (x, y)) in enumerate(pos_2d.items())}  # Convert to 3D layout

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    for edge in graph.edges():
        x_vals = [pos_3d[edge[0]][0], pos_3d[edge[1]][0]]
        y_vals = [pos_3d[edge[0]][1], pos_3d[edge[1]][1]]
        z_vals = [pos_3d[edge[0]][2], pos_3d[edge[1]][2]]
        ax.plot(x_vals, y_vals, z_vals, color='black')

    for node, (x, y, z) in pos_3d.items():
        ax.scatter(x, y, z, color='skyblue', s=100)
        ax.text(x, y, z, f'{node}', fontsize=12, fontweight='bold')

    ax.set_title("3D Tree Visualization", fontsize=20)
    plt.show()

# Input nodes and edges to create the tree
if __name__ == "__main__":
    graph = nx.Graph()
    
    print("Enter nodes (comma-separated, e.g., A,B,C):")
    nodes = input().split(',')
    graph.add_nodes_from(nodes)
    
    print("Enter edges (comma-separated pairs, e.g., A-B,B-C):")
    edges = input().split(',')
    for edge in edges:
        u, v = edge.split('-')
        graph.add_edge(u, v)
    
    print("Visualizing the tree...")
    visualize_tree_2d(graph)
    visualize_tree_3d(graph)
