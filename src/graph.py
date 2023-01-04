"""
@description: This module contains the Graph class and its methods.
@authors: Mustafa Mert Tunali, Ahmet Yildiz, Kerem Kaya
@instructor: Prof. Dr. Muhittin Gokmen
@course: COMP 303 - Algorithm Analysis
@date: 04-01-2023
"""

# Import libraries
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
from math import sqrt

# Import modules
from min_heap import MinHeap

# from utils import visualize_graph, visualize_shortest_path


class Graph(MinHeap):
    """
    This class represents a graph data structure, with support for adding and accessing
    nodes and edges, as well as performing dijkstra and A* searches.

    @attributes:
        graph (dict): A dictionary mapping nodes to a list of their neighbors and the weights
            of their edges.
        node_coordinates (dict): A dictionary mapping nodes to their x and y coordinates.
        a_star_parents (dict): A dictionary used to store the parent nodes during A* search.
        dijkstra_parents (dict): A dictionary used to store the parent nodes during dijkstra search.
    """

    def __init__(self):
        super().__init__()  # Inherit MinHeap class
        self.graph = {}
        self.node_coordinates = {}
        self.a_star_parents = {}
        self.dijkstra_parents = {}

    def add_node(self, node: int, x: int, y: int):
        """Adds a node to the graph.

        Args:
            node (int): node to be added
            x (int): x coordinate of the node
            y (int): y coordinate of the node

        Returns:
            None
        """
        self.graph[node] = []  # Initialize the node's neighbors list
        self.node_coordinates[node] = (
            x,
            y,
        )  # Add the node's coordinates to the dictionary

    def get_node(self, node: int) -> int:
        """Returns the node with the given id.

        Args:
            node (int): id of the node to be returned

        Returns:
            node (int): node with the given id
        """
        return self.node_coordinates[node]  # Return the node's coordinates

    def get_nodes(self) -> List[int]:
        """Returns a list of all nodes in the graph.
        Args:
            None

        Returns:
            nodes (list): list of all nodes in the graph
        """
        return list(self.graph.keys())  # Return the list of all nodes in the graph

    def get_node_coordinates(self, node: int) -> Tuple[int, int]:
        """Returns the coordinates of the given node.

        Args:
            node (int): id of the node whose coordinates are to be returned

        Returns:
            coordinates (tuple): coordinates of the given node
        """
        return self.node_coordinates[node]  # Return the node's coordinates

    def get_edge_weight(self, node1: int, node2: int) -> int:
        """Returns the weight of the edge between the given nodes.

        Args:
            node1 (int): id of the first node
            node2 (int): id of the second node

        Returns:
            weight (int): weight of the edge between the given nodes
        """
        for neighbor, weight in self.graph[
            node1
        ]:  # Iterate over the neighbors of the first node
            if neighbor == node2:  # If the neighbor is the second node
                return weight  # Return the weight of the edge
        return float("inf")  # Return infinity if there is no edge between the nodes

    def add_edge(self, node1: int, node2: int, weight: int):
        """Adds an edge between the given nodes.

        Args:
            node1 (int): id of the first node
            node2 (int): id of the second node
            weight (int): weight of the edge
        """
        self.graph[node1].append(
            (node2, weight)
        )  # Add the second node to the first node's neighbors list
        self.graph[node2].append(
            (node1, weight)
        )  # Add the first node to the second node's neighbors list

    def get_edges(self) -> List[Tuple[int, int]]:
        """Returns a list of all edges in the graph.

        Returns:
            edges (list): list of all edges in the graph
        """
        edges = []  # Initialize the list of edges
        for node in self.graph.keys():  # Iterate over the nodes in the graph
            for neighbor, _ in self.graph[
                node
            ]:  # Iterate over the neighbors of the current node
                if (
                    node,
                    neighbor,
                ) not in edges:  # If the edge is not in the list of edges
                    edges.append((node, neighbor))  # Add the edge to the list of edges
        return edges  # Return the list of edges

    def has_edge(self, node1: int, node2: int) -> bool:
        """Returns whether there is an edge between the given nodes.

        Args:
            node1 (int): id of the first node
            node2 (int): id of the second node
        Returns:
            has_edge (bool): whether there is an edge between the given nodes
        """
        for neighbor, _ in self.graph[
            node1
        ]:  # Iterate over the neighbors of the first node
            if neighbor == node2:  # If the neighbor is the second node
                return True  # Return True
        return False  # Return False if there is no edge between the nodes

    def get_neighbors(self, node: int) -> List[int]:
        """Returns a list of the neighbors of the given node.

        Args:
            node (int): id of the node whose neighbors are to be returned

        Returns:
            neighbors (list): list of the neighbors of the given node
        """
        return [
            neighbor for neighbor, _ in self.graph[node]
        ]  # Return the list of neighbors of the given node

    def dijkstra(self, source: int, target: int, viz=False) -> Tuple[List[int], int]:
        """Performs dijkstra search on the graph. Returns the shortest path from the source.
        It uses a min heap to keep track of the distances to the nodes. It iterates over the
        nodes in the heap and updates the distances to the neighbors of the current node.
        Firstly, it checks if the current node is the target node. If it is, it returns the
        path and the distance. Secondly, it checks if the current node is the source node.
        If it is, it adds the current node to the path. Thirdly, it checks if the current node
        is not the source node. If it is not, it adds the current node to the path and updates
        the distance. Lastly, it updates the distances to the neighbors of the current node.

        Args:
            source (int): id of the source node
            target (int): id of the target node
            viz (bool): whether to visualize the search
        Returns:
            metrics (dict): dictionary containing the number of visited nodes, the number of
                repetitions, the path and the distance of the shortest path from the source
                to the target node in the graph
        """

        distances = {
            node: float("inf") for node in self.graph.keys()
        }  # initialize the distance mapping
        distances[source] = 0  # set the distance of the source node to 0
        self.dijkstra_parents = (
            {source: source} if viz == False else {source: None}
        )  # initialize the parent mapping

        self.heap = []  # initialize the heap
        self.push((0, source))  # (distance, node)

        metrics = {
            "visited": 0,
            "repetition": 0,
            "path": [],
            "distance": 0,
        }  # initialize the metrics

        for node in self.graph.keys():  # add all nodes to the heap
            if node != source:  # except the source node
                self.push((float("inf"), node))  # push infinity [source, inf, inf inf]

        visited = 0  # initialize the number of visited nodes
        while self.heap:  # while the heap is not empty
            distance, node = self.pop()  # pop the node with the smallest distance
            if node == target:  # if the current node is the target node
                path = [target]  # initialize the path
                visited += 1  # increment the number of visited nodes
                while (
                    path[-1] != source
                ):  # while the last node in the path is not the source node
                    visited += 1  # increment the number of visited nodes
                    path.append(
                        self.dijkstra_parents[path[-1]]
                    )  # add the parent of the last node in the path to the path
                path.reverse()  # reverse the path
                metrics["visited"] = visited  # set the number of visited nodes
                metrics["repetition"] = self.counter  # set the number of repetitions
                metrics["path"] = path  # set the path
                metrics["distance"] = distance  # set the distance
                metrics[
                    "predecessor"
                ] = self.dijkstra_parents  # set the predecessor mapping
                return metrics  # return the metrics

            for neighbor, weight in self.graph[
                node
            ]:  # for each neighbor of the current node
                new_distance = distance + weight  # calculate the new distance
                if (
                    new_distance < distances[neighbor]
                ):  # if the new distance is smaller than the current distance
                    distances[neighbor] = new_distance  # update the distance
                    self.dijkstra_parents[neighbor] = node  # update the parent
                    self.decrease_key(
                        neighbor, new_distance
                    )  # decrease the key of the neighbor

        return metrics  # return the metrics

    def h_func(self, node: int, target: int) -> int:
        """This heuristic function estimates the distance between
        the two nodes by taking the absolute value of the difference
        between their indices.

        Args:
            node (int): id of the node
            target (int): id of the target node

        Returns (int): the estimated distance between the two nodes
        """
        return abs(
            target - node
        )  # return the absolute value of the difference between the indices

    def a_star(
        self, source: int, target: int, viz: bool = False
    ) -> Tuple[List[int], int]:
        """Performs A* search on the graph. Returns the shortest path from the source.
        It uses a list to keep track of the distances to the nodes. It iterates over the
        nodes in the list and updates the distances to the neighbors of the current node.
        Open set is a set of nodes that have been visited but whose neighbors haven't been
        completely explored. Closed set is a set of nodes that have been completely explored.
        Firstly, it checks if the current node is the target node. If it is, it returns the
        path and the distance. Secondly, it checks if the current node is the source node.
        If it is, it adds the current node to the path. Thirdly, it checks if the current node
        is not the source node. If it is not, it adds the current node to the path and updates
        the distance. Lastly, it updates the distances to the neighbors of the current node.

        Args:
            source (int): id of the source node
            target (int): id of the target node
            viz (bool): whether to visualize the search
        Returns:
            metrics (dict): dictionary containing the number of visited nodes, the number of
                repetitions, the path and the distance of the shortest path from the source
                to the target node in the graph.
        """
        distances = {
            node: float("inf") for node in self.graph.keys()
        }  # initialize the distance mapping
        distances[source] = 0  # set the distance of the source node to 0
        self.a_star_parents = (
            {source: source} if viz == False else {source: None}
        )  # initialize the parent mapping

        open_set = set([source])  # initialize the open set with the source node
        closed_set = set()  # initialize the closed set

        metrics = {
            "visited": 0,
            "repetition": 0,
            "path": [],
            "distance": 0,
        }  # initialize the metrics
        repetition = 0  # initialize the number of repetitions
        visited = 0  # initialize the number of visited nodes
        while open_set:  # while the open set is not empty
            node = min(
                open_set, key=lambda x: distances[x] + self.h_func(x, target)
            )  # get the node with the smallest distance + heuristic value

            if node == target:  # if the current node is the target node
                path = [target]  # initialize the path

                while (
                    path[-1] != source
                ):  # while the last node in the path is not the source node
                    path.append(
                        self.a_star_parents[path[-1]]
                    )  # add the parent of the last node in the path to the path
                path.reverse()  # reverse the path

                metrics["repetition"] = repetition  # set the number of repetitions
                metrics["visited"] = len(path)  # set the number of visited nodes
                metrics["path"] = path  # set the path
                metrics["distance"] = distances[target]  # set the distance
                metrics[
                    "predecessor"
                ] = self.a_star_parents  # set the predecessor mapping
                return metrics  # return the metrics

            open_set.remove(node)  # remove the current node from the open set
            closed_set.add(node)  # add the current node to the closed set

            for neighbor, weight in self.graph[
                node
            ]:  # for each neighbor of the current node
                if neighbor in closed_set:  # if the neighbor is in the closed set
                    continue  # continue to the next neighbor
                new_distance = distances[node] + weight  # calculate the new distance

                if (
                    new_distance < distances[neighbor]
                ):  # if the new distance is smaller than the current distance
                    repetition += 1  # increment the number of repetitions
                    distances[neighbor] = new_distance  # update the distance
                    self.a_star_parents[neighbor] = node  # update the parent
                    open_set.add(neighbor)  # add the neighbor to the open set
        return metrics  # return the metrics

    def __str__(self):
        """Returns a string representation of the graph.

        Args:
            None

        Returns:
            str: string representation of the graph
        """
        return str(self.graph)


""" python graph.py """
if __name__ == "__main__":
    # !!! TESTING USAGE ONLY  !!!
    g = Graph()  # create a graph

    # 4 nodes, 5 edges
    g.add_node(1, 0, 0)
    g.add_node(2, 0, 1)
    g.add_node(3, 1, 0)
    g.add_node(4, 1, 1)

    # add edges
    g.add_edge(1, 2, 8)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 3)
    g.add_edge(1, 4, 2)

    print(g)
    dijkstra_distance = g.dijkstra(
        1, 4
    )  # find the shortest path between node 1 and node 4
    print(f"dijkstra distance: {dijkstra_distance}")  # print the distance

    a_star_distance = g.a_star(1, 4)  # find the shortest path between node 1 and node 4
    print(f"A* distance: {a_star_distance}")  # print the distance

    nodes = list(g.graph.keys())  # get the nodes
    edges = []  # initialize the edges
    for node, neighbors in g.graph.items():  # for each node and its neighbors
        for neighbor, weight in neighbors:  # for each neighbor and its weight
            edges.append((node, neighbor))  # add the edge to the list of edges

    # visualize_graph(g, nodes, edges) # visualize the graph
    visualize_shortest_path(
        g, nodes, edges, 1, 4, "dijkstra"
    )  # visualize the shortest path

### HEURISTIC FUNCTIONS THAT CAN BE USED ###
## NOTE: The heuristic function must be consistent for A* to work properly ##
## NOTE: This is different kind of heuristic functions that can be used, we implemented to test the default h_func ##
# def h_func(self, node: int, target: int) -> int:
#     """This heuristic function is similar to the Manhattan distance,
#     but it allows for diagonal movement between nodes.
#    It is not consistent, so it is not recommended to use it.
#     Args:
#        node (int): Node id
#        target (int): Target node id
#     Returns:
#        int: The estimated distance between the two nodes
#     """
#     node_x, node_y = self.get_node_coordinates(node) # get the coordinates of the node
#     target_x, target_y = self.get_node_coordinates(target) # get the coordinates of the target node
#     dx = abs(node_x - target_x) # calculate the difference in x coordinates
#     dy = abs(node_y - target_y) # calculate the difference in y coordinates
#     return max(dx, dy) + (np.sqrt(2) - 1) * min(dx, dy) # return the estimated distance

# def h_func(self, node: int, target: int) -> int:
#     """Manhattan distance: This heuristic function calculates
#     the distance between two nodes as the sum of the absolute
#     differences of their coordinates.
#     Args:
#         node (int): Node id
#         target (int): Target node id
#     Returns:
#         int: The estimated distance between the two nodes
#     """
#     node_x, node_y = self.get_node_coordinates(node) # get the coordinates of the node
#     target_x, target_y = self.get_node_coordinates(target) # get the coordinates of the target node
#     return abs(node_x - target_x) + abs(node_y - target_y) # return the estimated distance

# def h_func(self, node: int, target: int) -> float:
#     """Calculate the Euclidean distance between two nodes.
#     Args:
#         node (int): The first node.
#         target (int): The second node.

#     Returns:
#         float: The Euclidean distance between the two nodes.
#     """
#     node_x, node_y = self.get_node_coordinates(node) # get the coordinates of the node
#     target_x, target_y = self.get_node_coordinates(target) # get the coordinates of the target node
#     dx = node_x - target_x # calculate the difference in x coordinates
#     dy = node_y - target_y # calculate the difference in y coordinates
#     return sqrt(dx**2 + dy**2) # return the estimated distance
