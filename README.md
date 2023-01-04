# comp303-project2

## Introduction

Welcome to COMP 303 Analysis of Algorithms, Comparison of Two Shortest Path Algorithms project's repo. In this project, you will be comparing the A* algorithm and Dijkstra's algorithm for finding the shortest path in a graph. This course is taught by Prof. Dr. Muhittin Gokmen at the Computer Engineering Department of MEF University.


## Instructor
-[Prof. Dr. Muhittin Gokmen](https://www.linkedin.com/in/muhittin-g%C3%B6kmen-b240b319/)

## Requirements
To run this project, you will need to have the following installed on your machine:
- matplotlib
  
You can install matplotlib using the following command:
```
pip install matplotlib
```

## Running the Project
To run the project, you can use the following command:
```
python main.py
```

This will run the the program, you can then enter the number of nodes you want and select the algorithm you want to use. Then you can enter the start and end nodes and the program will output the shortest paths, the number of nodes visited and repetaitions.

To compare the A* algorithm and Dijkstra's algorithm, use the following command:
```
python main.py --compare
```
This will run the program and compare A* and Dijkstra's algorithm for 10, 50, 100, 200, 500, 1000 and 2000 nodes. You can change the number of nodes in the main.py file. It will output the number of nodes visited and repetaitions for each algorithm and visualize the results using matplotlib.

To visualize the algorithm for a specific number of nodes, use the following command:
```
python main.py --viz
```
This will run the program and ask you to enter the number of nodes you want. Then it will ask you to select the algorithm you want to use. Then you can enter the start and end nodes and the program will output the shortest paths, the number of nodes visited and repetaitions and visualize the results using matplotlib.

## Algorithms
### A*
The A* algorithm is a popular choice for finding the shortest path between two vertices in a graph. It utilizes a cost function that takes into account the distance from the source vertex to the current vertex (g(n)) and the estimated distance from the current vertex to the target vertex (h(n)). The algorithm efficiently searches through the graph by repeatedly selecting the vertex with the lowest cost (f(n) = g(n) + h(n)) from the open set, which is a set of vertices that are being considered for the shortest path, and adding its neighbors to the open set if they are not already in the closed set, which is a set of vertices that have already been considered. If a neighbor is already in the open set, its cost is updated if the new cost is lower.
### Dijkstra's Algorithm
Dijkstra's algorithm is another popular algorithm for finding the shortest path in a graph. It works by repeatedly selecting the vertex with the lowest distance from the source vertex and updating the distances of its neighbors. The distances are initialized to infinity for all vertices except for the source vertex, which has a distance of 0. The algorithm terminates when the target vertex is reached or if there are no more vertices in the open set to consider.

### Comparison
Both of these algorithms are useful for finding the shortest path in a graph, but they have different time and space complexity. The A* algorithm typically has a time complexity of O(|E| + |V|log|V|) and a space complexity of O(|E|), while Dijkstra's algorithm has a time complexity of O(|V|^2) and a space complexity of O(|V|). This means that the A* algorithm may be faster and more space efficient than Dijkstra's algorithm for large graphs, but Dijkstra's algorithm may be more suitable for smaller graphs.

I hope this project helps you understand these algorithms and how they can be used to find the shortest path in a graph. Thank you for using comp303-project2.

### Contributors
- [Mustafa Mert Tunali](https://www.linkedin.com/in/mustafa-mert-tunali/)
- [Ahmet Yildiz](https://www.linkedin.com/in/yildizahmet/)
- [Kerem Kaya](https://www.linkedin.com/in/kayakerem/)

### References
- Prof. Dr. Muhittin Gokmen's slides