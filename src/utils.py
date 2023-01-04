"""
@description: This file contains utility functions for the project.
@authors: Mustafa Mert Tunali, Ahmet Yildiz, Kerem Kaya
@instructor: Prof. Dr. Muhittin Gokmen
@course: COMP 303 - Algorithm Analysis
@date: 04-01-2023
"""

# Import libraries
import time
import matplotlib.pyplot as plt


def initialize_graph(g, N):
    """
    This function initializes the graph with the given number of nodes.

    Args:
        g (Graph): Graph object
        N (int): Number of nodes

    Return (Graph): Initialized graph
    """
    for i in range(1, N + 1):  # Iterate over the nodes
        x = (i - 1) % 2  # Get the x coordinate
        y = (i - 1) // 2  # Get the y coordinate
        g.add_node(i, y, x)  # Add the node to the graph

    for i in range(1, N + 1):  # Iterate over the nodes
        for j in range(i, N + 1):  # Iterate over the nodes
            if abs(i - j) <= 3 and i != j:  # Check if the nodes are neighbors
                g.add_edge(i, j, i + j)  # Add the edge to the graph
    return g  # Return the initialized graph


def visualize_graph(g, nodes, edges):
    """
    This function visualizes the graph. It uses matplotlib library.

    Args:
        g (Graph): Graph object
        nodes (list): List of nodes
        edges (list): List of edges

    Returns:
        None
    """
    node_xs, node_ys = zip(
        *[g.get_node_coordinates(node) for node in nodes]
    )  # Unzip the coordinates

    plt.figure(figsize=(8, 4))  # Set the figure size
    plt.axis("off")  # Turn off the axis
    plt.scatter(
        node_xs, node_ys, s=600, c="white", edgecolors="black", lw=3
    )  # Plot the nodes

    for node in nodes:  # Iterate over the nodes
        x, y = g.get_node_coordinates(node)  # Get the coordinates
        plt.text(
            x, y, str(node), ha="center", va="center", fontsize=20, c="r"
        )  # Plot the node labels

    for edge in edges:  # Iterate over the edges
        x1, y1 = g.get_node_coordinates(edge[0])  # Get the coordinates
        x2, y2 = g.get_node_coordinates(edge[1])  # Get the coordinates
        # plt.plot([x1, x2], [y1, y2], "k-", lw=3) # ITS A LINE.
        edge_weight_str = str(
            g.get_edge_weight(edge[0], edge[1])
        )  # Get the edge weight
        plt.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(
                arrowstyle="->",
                shrinkA=14,
                shrinkB=14,
                connectionstyle="arc3,rad=-0.2",
                mutation_scale=20,
            ),
        )  # Plot the edges
        plt.text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            f"{edge_weight_str}",
            ha="center",
            va="center",
            fontsize=14,
            c="black",
        )  # Plot the edge weights
    plt.show()  # Show the plot


def visualize_shortest_path(g, nodes, edges, source, target, algorithm):
    """
    This function visualizes the shortest path. It uses matplotlib library.

    Args:
        g (Graph): Graph object
        nodes (list): List of nodes
        edges (list): List of edges
        source (int): Source node
        target (int): Target node
        algorithm (str): Algorithm name

    Returns:
        None
    """
    metrics = (
        g.dijkstra(source, target, viz=True)
        if algorithm == "dijkstra"
        else g.a_star(source, target, viz=True)
    )  # Get the metrics from the algorithm

    parents = (
        g.dijkstra_parents if algorithm == "dijkstra" else g.a_star_parents
    )  # Get the parents from the algorithm

    plt.figure(figsize=(8, 4))  # Set the figure size
    plt.axis("off")  # Turn off the axis

    for node in nodes:  # Iterate over the nodes
        x, y = g.get_node_coordinates(node)  # Get the coordinates
        plt.text(
            x, y, str(node), ha="center", va="center", fontsize=20, c="black"
        )  # Plot the node labels

    path = []  # Initialize the path
    current = target  # Set the current node to the target node
    while current is not None:  # Iterate until the current node is None
        path.append(current)  # Append the current node to the path
        current = parents[
            current
        ]  # Set the current node to the parent of the current node
    path = path[::-1]  # Reverse the path

    start_node_position = []  # Initialize the start node position
    end_node_position = []  # Initialize the end node position
    for edge in edges:  # Iterate over the edges
        x1, y1 = g.get_node_coordinates(edge[0])  # Get the coordinates
        x2, y2 = g.get_node_coordinates(edge[1])  # Get the coordinates

        edge_weight_str = str(
            g.get_edge_weight(edge[0], edge[1])
        )  # Get the edge weight

        node_xs, node_ys = zip(
            *[g.get_node_coordinates(node) for node in nodes]
        )  # Unzip the coordinates

        if edge[0] in path and edge[1] in path:  # edge is part of the shortest path

            if edge[0] == metrics["path"][0]:  # Check if the edge is the start node
                start_node_position = [x1, y1]  # Set the start node position

            if edge[0] == metrics["path"][-1]:  # Check if the edge is the end node
                end_node_position = [x1, y1]  # Set the end node position

            print(edge[0], edge[1])  # Print the edge

            plt.plot([x1, x2], [y1, y2], "g-", lw=3)  # Plot the edges
        else:  # edge is not part of the shortest path
            plt.annotate(  # Plot the edges
                "",
                xy=(x2, y2),
                xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle="->",
                    shrinkA=14,
                    shrinkB=14,
                    connectionstyle="arc3,rad=-0.1",
                    mutation_scale=20,
                ),
            )  # Plot the edges
            plt.scatter(
                node_xs, node_ys, s=600, c="white", edgecolors="black"
            )  # Plot the nodes

        if (
            len(start_node_position) == 2 and len(end_node_position) == 2
        ):  # Check if the start and end node positions are set
            plt.scatter(
                start_node_position[0],
                start_node_position[1],
                s=600,
                c="red",
                edgecolors="black",
                marker="o",
            )  # Plot the start node
            plt.scatter(
                end_node_position[0],
                end_node_position[1],
                s=600,
                c="green",
                edgecolors="black",
                marker="o",
            )  # Plot the end node
        else:
            plt.scatter(
                x1, y1, s=600, c="white", edgecolors="black", marker="o"
            )  # Plot the nodes
    plt.show()  # Show the plot


def compare_algorithms(g1, g2, source, target):
    """
    This function compares the time complexity of dijkstra's algorithm and A* algorithm.

    Args:
        g1 (Graph): Graph object
        g2 (Graph): Graph object
        source (int): Source node
        target (int): Target node

    Returns:
        dict: Dictionary containing the results
    """

    # time complexity of dijkstra
    start = time.perf_counter()  # start time
    metrics1 = g1.dijkstra(source, target)  # run dijkstra
    dijkstra_time = time.perf_counter() - start  # end time

    # time complexity of a*
    start = time.perf_counter()  # start time
    metrics2 = g2.a_star(source, target)  # run a*
    a_star_time = time.perf_counter() - start  # end time

    results = {
        "dijkstra": {
            "path": metrics1["path"],
            "distance": metrics1["distance"],
            "time": dijkstra_time,
            "visited": metrics1["visited"],
            "repetition": metrics1["repetition"],
        },  # dijkstra results
        "a_star": {
            "path": metrics2["path"],
            "distance": metrics2["distance"],
            "time": a_star_time,
            "visited": metrics2["visited"],
            "repetition": metrics2["repetition"],
        },  # a* results
    }
    print("ok")
    return results  # return results
