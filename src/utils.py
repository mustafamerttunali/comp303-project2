import time
import matplotlib.pyplot as plt


def initialize_graph(g, N):
    for i in range(1, N + 1):
        x = (i - 1) % 2
        y = (i - 1) // 2
        g.add_node(i, y, x)

    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if abs(i - j) <= 3 and i != j:
                g.add_edge(i, j, i + j)
    return g


def visualize_graph(g, nodes, edges):
    node_xs, node_ys = zip(*[g.get_node_coordinates(node) for node in nodes])

    plt.figure(figsize=(8, 4))
    plt.axis("off")
    plt.scatter(node_xs, node_ys, s=600, c="white", edgecolors="black", lw=3)

    for node in nodes:
        x, y = g.get_node_coordinates(node)
        plt.text(x, y, str(node), ha="center", va="center", fontsize=20, c="r")

    for edge in edges:
        x1, y1 = g.get_node_coordinates(edge[0])
        x2, y2 = g.get_node_coordinates(edge[1])
        # plt.plot([x1, x2], [y1, y2], "k-", lw=3) # ITS A LINE.
        edge_weight_str = str(g.get_edge_weight(edge[0], edge[1]))
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
        )
        plt.text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            f"{edge_weight_str}",
            ha="center",
            va="center",
            fontsize=14,
            c="black",
        )
    plt.show()


def visualize_shortest_path(g, nodes, edges, source, target, algorithm):

    metrics = (
        g.dijkstra(source, target)
        if algorithm == "dijkstra"
        else g.a_star(source, target)
    )

    parents = g.dijkstra_parents if algorithm == "dijkstra" else g.a_star_parents

    plt.figure(figsize=(8, 4))
    plt.axis("off")

    for node in nodes:
        x, y = g.get_node_coordinates(node)
        plt.text(x, y, str(node), ha="center", va="center", fontsize=20, c="black")

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parents[current]
    path = path[::-1]

    start_node_position = []
    end_node_position = []
    for edge in edges:
        x1, y1 = g.get_node_coordinates(edge[0])
        x2, y2 = g.get_node_coordinates(edge[1])

        edge_weight_str = str(g.get_edge_weight(edge[0], edge[1]))

        node_xs, node_ys = zip(*[g.get_node_coordinates(node) for node in nodes])

        if edge[0] in path and edge[1] in path:  # edge is part of the shortest path

            if edge[0] == metrics["path"][0]:
                start_node_position = [x1, y1]

            if edge[0] == metrics["path"][-1]:
                end_node_position = [x1, y1]

            print(edge[0], edge[1])

            plt.plot([x1, x2], [y1, y2], "g-", lw=3)
        else:  # edge is not part of the shortest path
            pass
            plt.annotate(
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
            )

        if len(start_node_position) == 2 and len(end_node_position) == 2:
            plt.scatter(
                start_node_position[0],
                start_node_position[1],
                s=600,
                c="red",
                edgecolors="black",
                marker="o",
            )
            plt.scatter(
                end_node_position[0],
                end_node_position[1],
                s=600,
                c="green",
                edgecolors="black",
                marker="o",
            )
        else:
            plt.scatter(x1, y1, s=600, c="white", edgecolors="black", marker="o")
    plt.show()


def compare_algorithms(g1, g2, source, target):

    # time complexity of dijkstra
    start = time.perf_counter()
    metrics1 = g1.dijkstra(source, target)
    dijkstra_time = time.perf_counter() - start

    # time complexity of a*
    start = time.perf_counter()
    metrics2 = g2.a_star(source, target)
    a_star_time = time.perf_counter() - start

    results = {
        "dijkstra": {
            "path": metrics1["path"],
            "distance": metrics1["distance"],
            "time": dijkstra_time,
            "visited": metrics1["visited"],
            "repetition": metrics1["repetition"],
        },
        "a_star": {
            "path": metrics2["path"],
            "distance": metrics2["distance"],
            "time": a_star_time,
            "visited": metrics2["visited"],
            "repetition": metrics2["repetition"],
        },
    }
    print("ok")
    return results

    # print(
    #     f"First 5 path of Dijkstra vs A*: {dijkstra_path[:5]} with distance of {dijkstra_distance} vs {a_star_path[:5]} with distance of {a_star_distance}"
    # )

    # print(f"Dijkstra vs A* Time: {dijkstra_time} vs {a_star_time}")
