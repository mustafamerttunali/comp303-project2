import random
import argparse
import matplotlib.pyplot as plt

from graph import Graph
from copy import deepcopy
from utils import (
    initialize_graph,
    visualize_graph,
    visualize_shortest_path,
    compare_algorithms,
)


parser = argparse.ArgumentParser()

parser.add_argument("--compare", action="store_true", help="compare the results")
parser.add_argument("--viz", action="store_true", help="visualize the graph")

args = parser.parse_args()


print(f"Welcome to the COMP 303, Project 2 Assignment!")

if not args.compare:
    N = int(input("Enter the number of nodes: "))
    if N < 2:
        print(
            "Number of nodes must be between 2 and 20. For higher N, python main.py --compare"
        )
        exit(1)

    print(f"Graph is creating with {N} nodes...", end="")
    g = initialize_graph(Graph(), N)
else:
    N_s = [10, 50, 100, 200, 500, 1000, 2000]
    print("Comparing the results of the algorithms...")
    source = 1
    a_star_times = []
    a_star_repetitions = []
    a_star_total_cost = []
    djikstra_times = []
    djikstra_repetitions = []
    dijkstra_total_cost = []
    for N in N_s:
        print(f"Experiment is starting by creating Graph  with {N} nodes...")

        g1 = initialize_graph(Graph(), N)
        g2 = deepcopy(g1)

        target = N
        results = compare_algorithms(g1, g2, source, target)
        djikstra_time, a_star_time = (
            results["dijkstra"]["time"],
            results["a_star"]["time"],
        )

        djikstra_times.append(djikstra_time)
        a_star_times.append(a_star_time)

        djikstra_repetition, a_star_repetition = (
            results["dijkstra"]["repetition"],
            results["a_star"]["repetition"],
        )

        djikstra_repetitions.append(djikstra_repetition)
        a_star_repetitions.append(a_star_repetition)

        dijkstra_total_cost.append(results["dijkstra"]["distance"])
        a_star_total_cost.append(results["a_star"]["distance"])

    plt.title("Running time of Dijkstra and A* algorithms")
    plt.yscale("log")
    plt.plot(N_s, djikstra_times, label="Dijkstra")
    plt.plot(N_s, a_star_times, label="A*")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Running time (seconds)")
    plt.legend()
    plt.show()

    print("Dijkstra Repetitions: ", djikstra_repetitions)
    print("A* Repetitions: ", a_star_repetitions)

    # Djakstra counters
    plt.title("Repetitions by Dijkstra and A*")
    plt.yscale("log")
    plt.plot(N_s, djikstra_repetitions, label="Dijkstra repetitions")
    plt.plot(N_s, a_star_repetitions, label="A* repetitions")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Number of Repetitions")
    plt.legend()
    plt.show()

    plt.title("Dijkstra Algorithm")
    plt.yscale("log")
    plt.plot(N_s, dijkstra_total_cost, label="Repetition")
    # plt.plot(N_s, dijkstra_theoritical, label="A* repetitions")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Cost")
    plt.legend()
    plt.show()

    plt.title("A* Algorithm")
    plt.yscale("log")
    plt.plot(N_s, a_star_total_cost, label="Repetition")
    # plt.plot(N_s, a_star_theoritical, label="A* repetitions")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Cost")
    plt.legend()
    plt.show()

    exit(1)


# visualize_graph(g, g.get_nodes(), g.get_edges()) if args.viz else None
shortest_path_algorithms = {0: g.dijkstra, 1: g.a_star}
while True:
    algorithm = int(input("Select the algorithm [0 for djkstra, 1 for A*, ]: "))
    try:
        source, target = (
            int(input("Enter the source node: ")),
            int(input("Enter the target node: ")),
        )

        visualize_shortest_path(
            g,
            g.get_nodes(),
            g.get_edges(),
            source,
            target,
            "dijkstra" if algorithm == 0 else "a_star",
        ) if args.viz else None

        metrics = shortest_path_algorithms[algorithm](source, target)
        print(f"Predecessor list: {metrics['predecessor']}")
        print(
            f"Shortest path from {source} to {target} is {metrics['path']} with distance {metrics['distance']} and {metrics['visited']} nodes visited with {metrics['repetition']} repetition."
        )
        break
    except KeyError:
        print("No path found!")
        continue
