"""
@description: This file contains the main function. It is used to run the program.
It it also used to compare the results of the algorithms. It is used to visualize the graph.
@authors: Mustafa Mert Tunali, Ahmet Yildiz, Kerem Kaya
@instructor: Prof. Dr. Muhittin Gokmen
@course: COMP 303 - Algorithm Analysis
@date: 04-01-2023
"""

# Import libraries
import random
import argparse
import matplotlib.pyplot as plt
from copy import deepcopy

# Import modules
from graph import Graph
from utils import (
    initialize_graph,
    visualize_graph,
    visualize_shortest_path,
    compare_algorithms,
)

# Create the parser
parser = argparse.ArgumentParser()

# Add the arguments
# Arguments are optional
parser.add_argument(
    "--compare", action="store_true", help="compare the results"
)  # Compare the results of the algorithms
parser.add_argument(
    "--viz", action="store_true", help="visualize the graph"
)  # Visualize the graph

args = parser.parse_args()  # Parse the arguments

print(f"Welcome to the COMP 303, Project 2 Assignment!")

# If the user does not want to compare the results of the algorithms
if not args.compare:
    # Get the number of nodes from the user
    N = int(input("Enter the number of nodes: "))
    if N < 2 or N > 20:  # If the number of nodes is less than 2 or greater than 20
        print(
            "Number of nodes must be between 2 and 20. For higher N, python main.py --compare"
        )
        exit(1)

    print(f"Graph is creating with {N} nodes...", end="")
    g = initialize_graph(Graph(), N)  # Create the graph
else:
    N_s = [
        10,
        50,
        100,
        200,
        500,
        1000,
        2000,
    ]  # Number of nodes according to the assignment
    print("Comparing the results of the algorithms...")
    source = 1  # Source node
    a_star_times = []
    a_star_repetitions = []
    a_star_total_cost = []
    djikstra_times = []
    djikstra_repetitions = []
    dijkstra_total_cost = []
    for N in N_s:
        print(f"Experiment is starting by creating Graph  with {N} nodes...", end="")

        g1 = initialize_graph(Graph(), N)  # Create the graph
        g2 = deepcopy(
            g1
        )  # Deep copy the graph to compare the results of the algorithms

        target = N  # Target node
        results = compare_algorithms(
            g1, g2, source, target
        )  # Compare the results of the algorithms
        djikstra_time, a_star_time = (
            results["dijkstra"]["time"],
            results["a_star"]["time"],
        )  # Get the running times of the algorithms

        djikstra_times.append(
            djikstra_time
        )  # Append the running times of the algorithms
        a_star_times.append(a_star_time)  # Append the running times of the algorithms

        djikstra_repetition, a_star_repetition = (
            results["dijkstra"]["repetition"],
            results["a_star"]["repetition"],
        )  # Get the number of repetitions of the algorithms

        djikstra_repetitions.append(
            djikstra_repetition
        )  # Append the number of repetitions of the algorithms
        a_star_repetitions.append(
            a_star_repetition
        )  # Append the number of repetitions of the algorithms

        dijkstra_total_cost.append(
            results["dijkstra"]["distance"]
        )  # Append the total cost of the algorithms
        a_star_total_cost.append(
            results["a_star"]["distance"]
        )  # Append the total cost of the algorithms

    plt.title(
        "Running time of Dijkstra and A* algorithms"
    )  # Plot the running times of the algorithms
    plt.plot(
        N_s, djikstra_times, label="Dijkstra"
    )  # Plot the running times of the algorithms
    plt.plot(N_s, a_star_times, label="A*")  # Plot the running times of the algorithms
    plt.xlabel("Input size (number of nodes in the Graph")  # Set the x label
    plt.ylabel("Running time (seconds)")  # Set the y label
    plt.legend()  # Show the legend
    plt.show()  # Show the plot

    # Djakstra counters
    plt.title(
        "Repetitions by Dijkstra and A*"
    )  # Plot the number of repetitions of the algorithms
    plt.plot(
        N_s, djikstra_repetitions, label="Dijkstra repetitions"
    )  # Plot the number of repetitions of the algorithms
    plt.plot(
        N_s, a_star_repetitions, label="A* repetitions"
    )  # Plot the number of repetitions of the algorithms
    plt.xlabel("Input size (number of nodes in the Graph")  # Set the x label
    plt.ylabel("Number of Repetitions")  # Set the y label
    plt.legend()  # Show the legend
    plt.show()  # Show the plot

    plt.title("Dijkstra Algorithm")  # Plot the total cost of the algorithms
    plt.yscale("log")  # Set the y scale to log
    plt.plot(
        N_s, dijkstra_total_cost, label="Repetition"
    )  # Plot the total cost of the algorithms
    # plt.plot(N_s, dijkstra_theoritical, label="A* repetitions") # Plot the total cost of the algorithms
    plt.xlabel("Input size (number of nodes in the Graph")  # Set the x label
    plt.ylabel("Cost")  # Set the y label
    plt.legend()  # Show the legend
    plt.show()  # Show the plot

    plt.title("A* Algorithm")  # Plot the total cost of the algorithms
    plt.yscale("log")  # Set the y scale to log
    plt.plot(
        N_s, a_star_total_cost, label="Repetition"
    )  # Plot the total cost of the algorithms
    # plt.plot(N_s, a_star_theoritical, label="A* repetitions")
    plt.xlabel("Input size (number of nodes in the Graph")  # Set the x label
    plt.ylabel("Cost")  # Set the y label
    plt.legend()  # Show the legend
    plt.show()  #

    exit(1)

# Get the number of nodes from the user
# visualize_graph(g, g.get_nodes(), g.get_edges()) if args.viz else None
shortest_path_algorithms = {0: g.dijkstra, 1: g.a_star}  # Algorithms to compare
while True:
    # Get the source and target nodes from the user
    algorithm = int(input("Select the algorithm [0 for djkstra, 1 for A*, ]: "))
    try:
        # Get the source and target nodes from the user
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
        ) if args.viz else None  # Visualize the shortest path if the user wants to

        metrics = shortest_path_algorithms[algorithm](
            source, target
        )  # Get the metrics of the shortest path
        print(
            f"Predecessor list: {metrics['predecessor']}"
        )  # Print the predecessor list
        print(
            f"Shortest path from {source} to {target} is {metrics['path']} with distance {metrics['distance']} and {metrics['visited']} nodes visited with {metrics['repetition']} repetition."
        )  # Print the shortest path
        break
    except KeyError:
        # If the source or target nodes are not in the graph
        print("No path found!")
        continue
