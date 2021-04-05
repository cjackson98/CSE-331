########################################
# PROJECT: Binary Min Heap and Sort
# Author:  Chris Jackson
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []


    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        for value in self.table:
            print(value)

    def get_size(self):
        """
        Returns the number of nodes currently in the Heap
        :return: number of nodes (length) in heap
        """
        return len(self.table)

    def parent(self, position):
        """
        Finds the parent of the node at index "position" and returns it's index
        :param position: index to get parent of
        :return: index of the parent node
        """
        return (position - 1) // 2

    def left_child(self, position):
        """
        Finds the left child of the node at index position
        :param position: index to get left child of
        :return: index of left child node
        """
        return (2 * position) + 1

    def right_child(self, position):
        """
        Finds the right child of the node at index position
        :param position: index to get right child of
        :return: index of right child node
        """
        return (2 * position) + 2

    def has_left(self, position):
        """
        Determines if a node has a left child or not
        :param position:
        :return: True if node has a left child, False if it does not
        """
        return self.left_child(position) < len(self.table)

    def has_right(self, position):
        """
        Determines if a node has a right child or not
        :param position:
        :return: True if node has a right child, False if it does not
        """
        return self.right_child(position) < len(self.table)

    def find(self, value):
        """
        Searches for a node with the provided value. Returns it's index if found or None if not.
        :param value:
        :return: If found, returns index of node, otherwise returns None
        """
        ctr = 0
        for item in self.table:
            if item == value:
                return ctr
            else:
                ctr += 1
        return None

    def heap_push(self, value):
        """
        Adds a node with value of "value" to the heap (Duplicates are ignored)
        :param value: Value to insert into heap
        :return: No return
        """
        position = self.find(value)
        if position is None:
            self.table.append(value)
            self.percolate_up(len(self.table) - 1)

    def heap_pop(self, value):
        """
        Removes node with the given value from heap
        :param value: Value of node to be removed
        :return: No return
        """
        position = self.find(value)
        if position is not None:
            self.table[position] = self.table[len(self.table) - 1]
            self.table.pop()
            self.percolate_down(position)

    def pop_min(self):
        """
        Removes the minimum node in the heap
        :return: the value removed, or None
        """
        if self.get_size() > 0:
            self.swap(0, len(self.table) - 1)
            item = self.table.pop()
            self.percolate_down(0)
            return item

    def swap(self, p1, p2):
        """
        Swaps the elements at indices p1 and p2
        :param p1: First element to swap
        :param p2: Second element to swap
        :return: no return
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        Moves node at index position up the tree until it is in the proper place
        :param position: position to move up the tree
        :return: no return
        """
        parent = self.parent(position)
        if position > 0 and self.table[position] < self.table[parent]:
            self.swap(position, parent)
            self.percolate_up(parent)

    def percolate_down(self, position):
        """
        Moves node at index position down the tree until it is in the proper place
        :param position: position to move down the tree
        :return: no return
        """
        if self.has_left(position):
            left = self.left_child(position)
            small_child = left
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    small_child = right
            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)


def heap_sort(unsorted):
    """
    Sorts data provided using Heap Sort and BinaryMinHeap
    :param unsorted: Data to be sorted
    :return: Sorted data
    """
    heap = BinaryMinHeap()                  # Create empty heap
    sorted_heap = BinaryMinHeap()           # Create empty heap
    for element in unsorted:                # Fill heap with elements in unsorted list
        heap.heap_push(element)             # ^
    size = len(unsorted)                    # Get size of unsorted list
    while size:                             # For each element in the min heap
        sorted_heap.heap_push(heap.pop_min())  # Pop_min value of heap and append to sorted_heap
        size = size-1                       # Decrease size by 1
    return sorted_heap.table                # Return the sorted list
