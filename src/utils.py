import matplotlib.pyplot as plt
import random


def initialize_graph(g, N, seed=42):
    # random.seed(seed)  # comment this line to get a random graph

    for i in range(N):
        x = i % 2
        y = i // 2
        g.add_node(i, y, x)

    for i in range(N):
        # edges 0 to 1, 1 to 2, 2 to 3, 3 to 4, 4 to 5, 5 to 6, 6 to 7, 7 to 8
        for j in range(i + 1, N):
            if abs(i - j) > 3 and i == j:
                continue

            if len(g.get_neighbors(i)) < 3 and len(g.get_neighbors(j)) < 3:
                g.add_edge(i, j, i + j)

    print("ok")
    return g


def visualize_graph(g, nodes, edges):
    node_xs, node_ys = zip(*[g.get_node_coordinates(node) for node in nodes])

    plt.figure(figsize=(6, 6))
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

    distance = (
        g.dijkstra(source, target)
        if algorithm == "dijkstra"
        else g.a_star(source, target)
    )

    parents = g.dijkstra_parents if algorithm == "dijkstra" else g.a_star_parents

    plt.figure(figsize=(16, 8))
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
            plt.text(
                (x1 + x2) / 2,
                (y1 + y2 / 2),
                f"{edge_weight_str}",
                ha="center",
                va="center",
                fontsize=14,
                c="g",
            )
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
