"""
@description: This file contains the MinHeap class. It is used for the dijkstra's algorithm.
@authors: Mustafa Mert Tunali, Ahmet Yildiz, Kerem Kaya
@instructor: Prof. Dr. Muhittin Gokmen
@course: COMP 303 - Algorithm Analysis
@date: 04-01-2023
"""


class MinHeap:
    """
    This class implements the MinHeap data structure. It is used for the dijkstra's algorithm.
    It is implemented using the list data structure.

    @attributes:
        heap (list): List of tuples. Each tuple contains the distance and the node.
        counter (int): Number of comparisons.
    """

    def __init__(self):
        self.heap = []  # List of tuples. Each tuple contains the distance and the node.
        self.counter = 0  # Number of comparisons.

    def push(self, val):
        """
        This function adds a new element to the heap. It uses the _bubble_up function to maintain the heap property.

        Args:
            val (tuple): Tuple of the distance and the node.

        Returns:
            None
        """
        self.heap.append(val)  # Add the new element to the heap.
        self._bubble_up(
            len(self.heap) - 1
        )  # Call the _bubble_up function to maintain the heap property.

    def pop(self):
        """
        This function removes the root of the heap. It uses the _bubble_down function to maintain the heap property.

        Args:
            None

        Returns:
            val (tuple): Tuple of the distance and the node.
        """
        self._swap(0, len(self.heap) - 1)  # Swap the root with the last element.
        val = self.heap.pop()  # Remove the last element.
        self._bubble_down(
            0
        )  # Call the _bubble_down function to maintain the heap property.

        return val  # Return the removed element.

    def _bubble_up(self, index):
        """
        This function maintains the heap property by swapping the elements.
        It is called when a new element is added to the heap.

        Args:
            index (int): Index of the element.

        Returns:
            None
        """
        if index == 0:  # If the index is 0, return. Because the root has no parent.
            return  # Return

        self.counter += 1  # To count the number of repetitions.

        parent_index = (index - 1) // 2  # Get the parent index.

        if (
            self.heap[index] < self.heap[parent_index]
        ):  # If the child is smaller than the parent, swap them.
            self._swap(index, parent_index)  # Swap the elements.
            self._bubble_up(parent_index)  # Call the function recursively.

    def _bubble_down(self, index):
        """
        This function maintains the heap property by swapping the elements.
        It is called when the root is removed from the heap.

        Args:
            index (int): Index of the element.

        Returns:
            None
        """
        left_child_index = 2 * index + 1  # Get the left child index.
        right_child_index = 2 * index + 2  # Get the right child index.

        if left_child_index >= len(
            self.heap
        ):  # If the left child index is greater than the length of the heap,
            return  # return.

        if right_child_index >= len(
            self.heap
        ):  # If the right child index is greater than the length of the heap,
            min_index = left_child_index  # the minimum index is the left child index.
        else:
            if (
                self.heap[left_child_index] < self.heap[right_child_index]
            ):  # If the left child is smaller than the right child,
                min_index = (
                    left_child_index  # the minimum index is the left child index.
                )
            else:  # Otherwise,
                min_index = (
                    right_child_index  # the minimum index is the right child index.
                )

        if (
            self.heap[index] > self.heap[min_index]
        ):  # If the parent is greater than the child,
            self._swap(index, min_index)  # swap them.
            self._bubble_down(min_index)  # Call the function recursively.

    def decrease_key(self, node, new_distance):
        """
        This function decreases the distance of the given node. It is used for the dijkstra's algorithm.
        One of the main steps of the algorithm is to decrease the distance of the adjacent nodes of the current node.

        Args:
            node (int): Node.
            new_distance (int): New distance.

        Returns:
            None
        """
        for i, (distance, node_) in enumerate(self.heap):  # Iterate over the heap.
            if node_ == node:  # If the node is found,
                self.heap[i] = (new_distance, node_)  # update the distance.
                self._bubble_up(
                    i
                )  # Call the _bubble_up function to maintain the heap property.
                break  # Break the loop.

    def _swap(self, index1, index2):
        """
        This function swaps the elements of the heap. It is used by the _bubble_up and _bubble_down functions.

        Args:
            index1 (int): Index of the first element.
            index2 (int): Index of the second element.

        Returns:
            None
        """
        # Swap the elements. It is important to use the tuple unpacking.
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
