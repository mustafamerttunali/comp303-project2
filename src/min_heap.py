class MinHeap:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def push(self, val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._bubble_down(0)

        return val

    def _bubble_up(self, index):
        """_summary_

        Args:
            index (_type_): _description_
        """
        if index == 0:
            return

        self.counter += 1

        parent_index = (index - 1) // 2

        if self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        """_summary_

        Args:
            index (_type_): _description_
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index >= len(self.heap):
            return

        if right_child_index >= len(self.heap):
            min_index = left_child_index
        else:
            if self.heap[left_child_index] < self.heap[right_child_index]:
                min_index = left_child_index
            else:
                min_index = right_child_index

        if self.heap[index] > self.heap[min_index]:
            self._swap(index, min_index)
            self._bubble_down(min_index)

    def decrease_key(self, node, new_distance):
        """_summary_

        Args:
            node (_type_): _description_
            new_distance (_type_): _description_
        """
        for i, (distance, node_) in enumerate(self.heap):
            if node_ == node:
                self.heap[i] = (new_distance, node_)
                self._bubble_up(i)
                break

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
