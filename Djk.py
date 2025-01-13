import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx
import time

def dijkstra_shortest_path(graph, source, target):
    """Compute the shortest path using Dijkstra's algorithm."""
    return nx.dijkstra_path(graph, source, target)

def animate_2d(graph, path):
    """Animate the traversal of the shortest path in 2D."""
    pos = nx.spring_layout(graph)  # 2D layout
    plt.figure(figsize=(10, 7))
    
    for i in range(len(path) - 1):
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold")
        current_path = path[:i + 2]
        nx.draw_networkx_edges(graph, pos, edgelist=list(zip(current_path, current_path[1:])), edge_color='red', width=2)
        plt.title("2D Animation: Dijkstra's Algorithm", fontsize=20)
        plt.pause(1)  # Pause for animation effect
        plt.clf()

    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold")
    nx.draw_networkx_edges(graph, pos, edgelist=list(zip(path, path[1:])), edge_color='red', width=2)
    plt.show()

def animate_3d(graph, path):
    """Animate the traversal of the shortest path in 3D."""
    pos_2d = nx.spring_layout(graph)  # 2D layout
    pos_3d = {node: (x, y, i * 0.5) for i, (node, (x, y)) in enumerate(pos_2d.items())}  # Add z-coordinates

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(path) - 1):
        ax.clear()
        for edge in graph.edges():
            x_vals = [pos_3d[edge[0]][0], pos_3d[edge[1]][0]]
            y_vals = [pos_3d[edge[0]][1], pos_3d[edge[1]][1]]
            z_vals = [pos_3d[edge[0]][2], pos_3d[edge[1]][2]]
            ax.plot(x_vals, y_vals, z_vals, color='black')

        current_path = path[:i + 2]
        for j in range(len(current_path) - 1):
            x_vals = [pos_3d[current_path[j]][0], pos_3d[current_path[j + 1]][0]]
            y_vals = [pos_3d[current_path[j]][1], pos_3d[current_path[j + 1]][1]]
            z_vals = [pos_3d[current_path[j]][2], pos_3d[current_path[j + 1]][2]]
            ax.plot(x_vals, y_vals, z_vals, color='red', linewidth=2)

        ax.set_title("3D Animation: Dijkstra's Algorithm", fontsize=20)
        plt.pause(1)  # Pause for animation effect

    plt.show()

if __name__ == "__main__":
    graph = nx.Graph()

    print("Enter nodes (comma-separated, e.g., A,B,C):")
    nodes = input().split(',')
    graph.add_nodes_from(nodes)

    print("Enter edges with weights (comma-separated, e.g., A-B-4,B-C-3):")
    edges = input().split(',')
    for edge in edges:
        u, v, weight = edge.split('-')
        graph.add_edge(u, v, weight=int(weight))

    print("Enter source node:")
    source = input().strip()

    print("Enter target node:")
    target = input().strip()

    try:
        shortest_path = dijkstra_shortest_path(graph, source, target)
        print(f"Shortest path: {' -> '.join(shortest_path)}")
        
        print("Animating in 2D...")
        animate_2d(graph, shortest_path)
        
        print("Animating in 3D...")
        animate_3d(graph, shortest_path)
        
    except nx.NetworkXNoPath:
        print("No path exists between the source and target nodes.")
    except Exception as e:
        print(f"An error occurred: {e}")
