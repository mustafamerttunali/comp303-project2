import matplotlib.pyplot as plt

from min_heap import MinHeap
from typing import Dict, List, Tuple
from math import sqrt

# from utils import visualize_graph, visualize_shortest_path


class Graph(MinHeap):
    def __init__(self):
        super().__init__()
        self.graph = {}
        self.node_coordinates = {}
        self.a_star_parents = {}
        self.dijkstra_parents = {}

    def add_node(self, node: int, x: int, y: int):
        self.graph[node] = []
        self.node_coordinates[node] = (x, y)

    def get_node(self, node: int):
        return self.node_coordinates[node]

    def get_nodes(self) -> List[int]:
        return list(self.graph.keys())

    def get_node_coordinates(self, node: int) -> Tuple[int, int]:
        return self.node_coordinates[node]

    def get_edge_weight(self, node1: int, node2: int) -> int:
        for neighbor, weight in self.graph[node1]:
            if neighbor == node2:
                return weight
        return float("inf")

    def add_edge(self, node1: int, node2: int, weight: int):
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def get_edges(self) -> List[Tuple[int, int]]:
        edges = []
        for node in self.graph.keys():
            for neighbor, _ in self.graph[node]:
                if (node, neighbor) not in edges:
                    edges.append((node, neighbor))
        return edges

    def has_edge(self, node1: int, node2: int) -> bool:
        for neighbor, _ in self.graph[node1]:
            if neighbor == node2:
                return True
        return False

    def get_neighbors(self, node: int) -> List[int]:
        return [neighbor for neighbor, _ in self.graph[node]]

    def dijkstra(self, source: int, target: int) -> Tuple[List[int], int]:
        distances = {node: float("inf") for node in self.graph.keys()}
        distances[source] = 0
        self.dijkstra_parents = {source: None}  # initialize the parent mapping

        self.heap = []
        self.push((0, source))  # (distance, node)

        metrics = {"visited": 0, "repetition": 0, "path": [], "distance": 0}

        for node in self.graph.keys():
            if node != source:
                self.push((float("inf"), node))

        visited = 0
        while self.heap:
            distance, node = self.pop()
            if node == target:
                path = [target]
                visited += 1
                while path[-1] != source:
                    visited += 1
                    path.append(self.dijkstra_parents[path[-1]])
                path.reverse()
                metrics["visited"] = visited
                metrics["repetition"] = self.counter
                metrics["path"] = path
                metrics["distance"] = distance
                return metrics

            for neighbor, weight in self.graph[node]:
                # TODO: Counter?
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    self.dijkstra_parents[neighbor] = node
                    # self.push((new_distance, neighbor))
                    self.decrease_key(neighbor, new_distance)

        return metrics

    def h_func(self, node: int, target: int) -> int:
        """This heuristic function estimates the distance between
        the two nodes by taking the absolute value of the difference
        between their indices.

        Args:
            node (int): _description_
            target (int): _description_

        Returns:
            int: _description_
        """
        return abs(target - node)

    def a_star(self, source: int, target: int) -> Tuple[List[int], int]:
        distances = {node: float("inf") for node in self.graph.keys()}
        distances[source] = 0
        self.a_star_parents = {source: None}  # initialize the parent mapping

        open_set = set([source])
        closed_set = set()

        metrics = {"visited": 0, "repetition": 0, "path": [], "distance": 0}
        repetition = 0
        visited = 0
        while open_set:
            node = min(
                open_set, key=lambda x: distances[x] + self.h_func(x, target)
            )  # f(n) = g(n) + h(n), looking for the node with the lowest f(n)

            if node == target:
                path = [target]
                while path[-1] != source:
                    path.append(self.a_star_parents[path[-1]])
                path.reverse()
                metrics["repetition"] = repetition
                metrics["visited"] = len(path)
                metrics["path"] = path
                metrics["distance"] = distances[target]
                return metrics

            open_set.remove(node)
            closed_set.add(node)

            for neighbor, weight in self.graph[node]:
                if neighbor in closed_set:
                    continue
                new_distance = distances[node] + weight

                if new_distance < distances[neighbor]:
                    repetition += 1
                    distances[neighbor] = new_distance
                    self.a_star_parents[neighbor] = node
                    open_set.add(neighbor)
        return metrics

    def __str__(self):
        return str(self.graph)


if __name__ == "__main__":
    # TESTING USAGE ONLY!!!
    g = Graph()

    # 4 nodes, 5 edges
    g.add_node(1, 0, 0)
    g.add_node(2, 0, 1)
    g.add_node(3, 1, 0)
    g.add_node(4, 1, 1)

    g.add_edge(1, 2, 8)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 3)
    g.add_edge(1, 4, 2)

    print(g)
    djikstra_distance = g.dijkstra(1, 4)
    print(f"Dijkstra distance: {djikstra_distance}")

    a_star_distance = g.a_star(1, 4)
    print(f"A* distance: {a_star_distance}")

    nodes = list(g.graph.keys())
    edges = []
    for node, neighbors in g.graph.items():
        for neighbor, weight in neighbors:
            edges.append((node, neighbor))

    # visualize_graph(g, nodes, edges)
    visualize_shortest_path(g, nodes, edges, 1, 4, "dijkstra")


# def h_func(self, node: int, target: int) -> int:
#     """This heuristic function is similar to the Manhattan distance,
#     but it allows for diagonal movement between nodes.

#     Args:
#         node (int): TODO
#         target (int): TODO

#     Returns:
#         int: TODO
#     """
#     node_x, node_y = self.get_node_coordinates(node)
#     target_x, target_y = self.get_node_coordinates(target)
#     dx = abs(node_x - target_x)
#     dy = abs(node_y - target_y)
#     return max(dx, dy) + (np.sqrt(2) - 1) * min(dx, dy)

# def h_func(self, node: int, target: int) -> int:
#     """Manhattan distance: This heuristic function calculates
#     the distance between two nodes as the sum of the absolute
#     differences of their coordinates.

#     Args:
#         node (int): TODO
#         target (int): TODO

#     Returns:
#         int: TODO
#     """
#     node_x, node_y = self.get_node_coordinates(node)
#     target_x, target_y = self.get_node_coordinates(target)
#     return abs(node_x - target_x) + abs(node_y - target_y)

# def h_func(self, node: int, target: int) -> float:
#     """Calculate the Euclidean distance between two nodes.

#     Args:
#         node (int): The first node.
#         target (int): The second node.

#     Returns:
#         float: The Euclidean distance between the two nodes.
#     """
#     node_x, node_y = self.get_node_coordinates(node)
#     target_x, target_y = self.get_node_coordinates(target)
#     dx = node_x - target_x
#     dy = node_y - target_y
#     return sqrt(dx**2 + dy**2)
