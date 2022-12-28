from typing import Dict, List


class Graph(MinHeap):
    def __init__(self):
        self.graph = {}

    def add_node(self, node: int):
        self.graph[node] = []

    def add_edge(self, node1: int, node2: int, weight: int):
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def dijkstra(self, source: int, target: int) -> int:
        distances = {node: float("inf") for node in self.graph.keys()}
        distances[source] = 0

        self.heap = []
        self.push((0, source))  # (distance, node)

        while self.heap:
            distance, node = self.pop()

            if node == target:
                return distance

            for neighbor, weight in self.graph[node]:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    self.push((new_distance, neighbor))
        return float("inf")
