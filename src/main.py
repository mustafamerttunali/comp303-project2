import random
import argparse

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

N = int(input("Enter the number of nodes: "))

if not args.compare:
    if N < 2 or N > 20:
        print(
            "Number of nodes must be between 2 and 20. For higher N, python main.py --compare=True"
        )
        exit(1)

print(f"Graph is creating with {N} nodes...", end="")

g = initialize_graph(Graph(), N)

if args.compare:
    print("Comparing the results of the algorithms...")
    source = 1
    target = N - 1
    results = compare_algorithms(g, source, target)
    # results = g.compare_algorithms(source, target)
    # for algo_type, result in results.items():
    #     print(
    #         f"Algorithm {algo_type} found the shortest path: {result[0]} with distance {result[1]} and the total number of repetitions are {result[2]}."
    #     )
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

        shortest_path, distance = shortest_path_algorithms[algorithm](source, target)
        print(
            f"Shortest path from {source} to {target} is {shortest_path} with distance {distance}."
        )

        # TODO: Running time
        # TODO: Total number of repetitions
        # TODO: Theoretical running time of the algorithm

        break
    except KeyError:
        print("No path found!")
        continue
