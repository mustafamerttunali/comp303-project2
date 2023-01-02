import random
import argparse
import matplotlib.pyplot as plt

from graph import Graph
from utils import (
    initialize_graph,
    visualize_graph,
    visualize_shortest_path,
    compare_algorithms,
)


parser = argparse.ArgumentParser()

parser.add_argument("--compare", action="store_true", help="compare the results")

args = parser.parse_args()


print(f"Welcome to the COMP 303, Project 2 Assignment!")

if not args.compare:
    N = int(input("Enter the number of nodes: "))
    if N < 2 or N > 20:
        print(
            "Number of nodes must be between 2 and 20. For higher N, python main.py --compare=True"
        )
        exit(1)

    print(f"Graph is creating with {N} nodes...", end="")
    g = initialize_graph(Graph(), N)
else:
    N_s = [10, 50, 100, 200, 500, 1000, 2000]
    print("Comparing the results of the algorithms...")
    source = 1
    a_star_times = []
    a_star_counters = []
    djikstra_times = []
    djikstra_counters = []
    for N in N_s:
        print(f"Experiment is starting by creating Graph  with {N} nodes...")
        g = initialize_graph(Graph(), N)
        target = N - 1
        results = compare_algorithms(g, source, target)
        djikstra_time, a_star_time = (
            results["dijkstra"]["time"],
            results["a_star"]["time"],
        )
        djikstra_times.append(djikstra_time)
        djikstra_counters.append(results["dijkstra"]["counter"])
        a_star_times.append(a_star_time)
        a_star_counters.append(results["a_star"]["counter"])

    plt.title("Running time of Dijkstra and A* algorithms")
    plt.plot(N_s, djikstra_times, label="Dijkstra")
    plt.plot(N_s, a_star_times, label="A*")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Running time (seconds)")
    plt.legend()
    plt.show()

    print("Dijkstra counters: ", djikstra_counters)
    print("A* counters: ", a_star_counters)

    # Djakstra counters
    plt.title("Number of nodes visited by Dijkstra Algotihm")
    plt.plot(N_s, djikstra_counters, label="Dijkstra counter")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Number of nodes visited")
    plt.legend()
    plt.show()

    # A* counters
    plt.title("Number of nodes visited by A* Algotihm")
    plt.plot(N_s, a_star_counters, label="A* counter")
    plt.xlabel("Input size (number of nodes in the Graph")
    plt.ylabel("Number of nodes visited")
    plt.legend()
    plt.show()

    exit(1)


visualize_graph(g, g.get_nodes(), g.get_edges())
shortest_path_algorithms = {0: g.dijkstra, 1: g.a_star}
while True:
    algorithm = int(input("Select the algorithm [0 for djkstra, 1 for A*, ]: "))
    try:
        source, target = int(input("Enter the source node: ")), int(
            input("Enter the target node: ")
        )
        visualize_shortest_path(
            g,
            g.get_nodes(),
            g.get_edges(),
            source,
            target,
            "dijkstra" if algorithm == 0 else "a_star",
        )

        shortest_path, distance, counter = shortest_path_algorithms[algorithm](
            source, target
        )
        print(
            f"Shortest path from {source} to {target} is {shortest_path} with distance {distance} and {counter} nodes visited."
        )
        break
    except KeyError:
        print("No path found!")
        continue
