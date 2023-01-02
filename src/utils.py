import time
import matplotlib.pyplot as plt


def initialize_graph(g, N, seed=42):
    for i in range(N):
        x = i % 2
        y = i // 2
        g.add_node(i, y, x)

    for i in range(N):
        for j in range(i + 1, N):
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

    distance, _, _ = (
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

    for edge in edges:
        x1, y1 = g.get_node_coordinates(edge[0])
        x2, y2 = g.get_node_coordinates(edge[1])

        edge_weight_str = str(g.get_edge_weight(edge[0], edge[1]))

        if edge[0] in path and edge[1] in path:  # edge is part of the shortest path
            plt.plot([x1, x2], [y1, y2], "g-")
            # plt.text(
            #     (x1 + x2) / 2,
            #     (y1 + y2 / 2),
            #     f"{edge_weight_str}",
            #     ha="center",
            #     va="center",
            #     fontsize=18,
            #     c="g",
            # )
        else:  # edge is not part of the shortest path

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
            plt.text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                f"{edge_weight_str}",
                ha="center",
                va="center",
                fontsize=14,
                c="black",
            )

    node_xs, node_ys = zip(*[g.get_node_coordinates(node) for node in nodes])

    plt.scatter(node_xs, node_ys, s=600, c="white", edgecolors="black", marker="o")

    plt.show()


def compare_algorithms(g, source, target):
    # time complexity of dijkstra
    start = time.perf_counter()
    dijkstra_path, dijkstra_distance, djakstra_counter = g.dijkstra(source, target)
    dijkstra_time = time.perf_counter() - start

    # time complexity of a*
    start = time.perf_counter()
    a_star_path, a_star_distance, a_star_counter = g.a_star(source, target)
    a_star_time = time.perf_counter() - start

    results = {
        "dijkstra": {
            "path": dijkstra_path,
            "distance": dijkstra_distance,
            "time": dijkstra_time,
            "counter": djakstra_counter,
        },
        "a_star": {
            "path": a_star_path,
            "distance": a_star_distance,
            "time": a_star_time,
            "counter": a_star_counter,
        },
    }

    return results

    # print(
    #     f"First 5 path of Dijkstra vs A*: {dijkstra_path[:5]} with distance of {dijkstra_distance} vs {a_star_path[:5]} with distance of {a_star_distance}"
    # )

    # print(f"Dijkstra vs A* Time: {dijkstra_time} vs {a_star_time}")
