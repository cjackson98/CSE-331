class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Take a value and insert it into the proper position of the tree
        :param value: the value of the node to be inserted
        :return: No return value
        """

        if self.root is None:  # If tree is empty, set the root to the value provided
            self.root = Node(value)
            self.size += 1
        else:
            parent = self.search(value, self.root)  # Get parent node of value
            # Now 'parent' is the parent node of where value is to be inserted
            if value < parent.value:  # If value < parent node value, insert into left subtree
                # print value, "goes to the left subtree of", parent
                parent.left = Node(value)
                parent.left.parent = parent
                self.size += 1
            if value > parent.value:  # If value > parent node value, insert into left subtree
                # print value, "goes to the right subtree of", parent
                parent.right = Node(value)
                parent.right.parent = parent
                self.size += 1

    def remove(self, value):
        """
        Removes a node with the provided value. If node is not in the tree, do nothing.
        :param value: Value of node to be removed
        :return: No return
        """
        temp = self.root
        node = self.search(value, temp)

        if node is None or node.value != value or self.size == 0 or temp is None:
            return

        if self.size == 1 and value == self.root.value:  # If removing the only node in the tree
            self.root = None
            self.size -= 1
            return

        if temp.value != value:  # If not removing the root node
            while temp is not None:  # Move down the tree until a leaf node is reached
                parent = temp
                if temp.left is not None and temp.left.value == value:
                    break
                if temp.right is not None and temp.right.value == value:
                    break
                if value < temp.value:
                    temp = temp.left
                    continue
                if value > temp.value:
                    temp = temp.right
                    continue
        else:  # If removing root node, parent is none
            parent = None

        if node.left is not None and node.right is not None:  # Two children
            # When removing a node with two children, replace with the minimum of the right subtree
            min_parent = node
            min_node = node.right

            while min_node.left is not None:  # Get min and parent of min
                min_parent = min_node
                min_node = min_node.left

            node.value = min_node.value
            node.parent = parent

            if min_parent.left == min_node:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right

        elif node.left is None and node.right is None:  # If no children
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        else:  # If one child
            if node.left is None:
                holder = node.right
            else:
                holder = node.left
            if parent is None:  # Removing root node
                if self.root.left is None:
                    self.root = self.root.right
                    self.root.parent = None
                elif self.root.right is None:
                    self.root = self.root.left
                    self.root.parent = None
            else:
                if parent.left is node:
                    holder.parent = parent
                    parent.left = holder
                else:
                    holder.parent = parent
                    parent.right = holder
        self.size -= 1

    def search(self, value, node):
        """
        Searches the tree for a given value starting at a provided node. If value is found,
        return the node it is found it. Otherwise, return the parent node of where that value
        would be inserted. Must be recursive.
        :param value: Value to search for
        :param node: The root node of the given tree/subtree
        :return: Returns the node with the matching key (if found)
            If not found, return the parent node of where it would go.
        """
        if node is None:  # Accounts for an empty list being searched
            return None
        if value == node.value:  # if value is found (base case)
            return node
        if value > node.value:
            if node.right is None:
                return node  # if next node is none (base case)
            return self.search(value, node.right)
        if value < node.value:
            if node.left is None:
                return node  # if next node is none (base case)
            return self.search(value, node.left)

        # Iterative version. Made and used to help turn function recursive.
        # while node is not None:  # Move down the tree until a leaf node is reached
        #     parent = node  # Keep parent at the previous node
        #     if value == node.value:  # if value is already in the list, do nothing
        #         break
        #     if value > node.value:
        #         node = node.right
        #     elif value < node.value:
        #         node = node.left
        # return parent

    def inorder(self, node):
        """
        Returns a generator object of the tree traversed using the inorder method.
        Must be recursive.
        :param node: Node to begin at (root)
        :return: returns a generator object
        """
        if node is not None:

            for item in self.inorder(node.left):
                yield item

            yield node.value

            for item in self.inorder(node.right):
                yield item

    def preorder(self, node):
        """
        Returns a generator object of the tree traversed using the preorder method.
        Must be recursive.
        :param node: Node to begin at (root)
        :return: returns a generator object
        """
        if node is not None:

            yield node.value

            for item in self.preorder(node.left):
                yield item
            for item in self.preorder(node.right):
                yield item

    def postorder(self, node):
        """
        Returns a generator object of the tree traversed using the postorder method.
        Must be recursive.
        :param node: Node to begin at (root)
        :return: returns a generator object
        """
        if node is not None:

            for item in self.postorder(node.left):
                yield item
            for item in self.postorder(node.right):
                yield item

            yield node.value

    def depth(self, value):
        """
        Gets and returns the depth of the node with the given value
        :param value: Value of node to get depth of
        :return: The depth of the tree at the given value
        """
        if self.size == 1:
            return 0
        if self.size == 0:
            return -1
        node = self.root
        total = 0
        while node is not None:
            if node.value == value:
                return total
            if value < node.value:
                if node.right is None:  # Value not in tree
                    return -1
                node = node.left
                total += 1
            if value > node.value:
                if node.right is None:  # Value not in tree
                    return -1
                node = node.right
                total += 1

    def height(self, node):
        """
        Returns the height of the tree rooted at the given node. Must be recursive.
        :param node: Node to begin counting at (root)
        :return: The height of tree starting at the given node
        """
        if node is None:  # Base case
            return -1

        left = self.height(node.left)  # Get height of left and right subtree
        right = self.height(node.right)

        if left > right:  # Use the bigger of the two heights
            return left + 1
        else:
            return right + 1

    def min(self, node):
        """
        Returns the minimum node of the tree rooted at the given node. Must be recursive.
        :param node: Node to begin searching for minimum at (root)
        :return: The minimum node of the tree
        """
        if self.root is None:
            return None
        if node.left is not None:
            return self.min(node.left)
        return node

    def max(self, node):
        """
        Returns the maximum node of the tree rooted at the given node. Must be recursive.
        :param node: Node to begin searching for maximum at (root)
        :return: The maximum node of the tree
        """
        if self.root is None:
            return None
        if node.right is not None:
            return self.max(node.right)
        return node

    def get_size(self):
        """
        Returns the number of nodes in the tree
        :return: Size of tree (number of nodes)
        """
        return self.size

    def is_perfect(self, node):
        """
        Determines whether or not the tree is perfect (using the provided node as the root node)
        :param node: Node to begin at (root)
        :return: A bool of whether the tree is perfect or not
        """

        if self.root is None:
            return True
        elif self.root is not None and node is None:
            return

        height = self.height(node)
        total = (2**(height+1))-1

        new_size = self.curr_size(node)

        return total == new_size

    def is_degenerate(self):
        """
        Determines whether or not the tree is degenerate
        :return: A bool of whether the tree is degenerate or not
        """
        if self.root is None:
            return False

        node = self.root

        while node is not None:
            if node.left is not None and node.right is not None:  # If node has 2 children
                return False
            if node.left is None and node.right is not None:  # If node has 1 child, continue loop
                node = node.right
                continue
            if node.left is not None and node.right is None:  # If node has 1 child, continue loop
                node = node.left
                continue
            if node.left is None and node.right is None:  # If leaf node is reached, return True
                return True

    def curr_size(self, node):
        """
        Gets the size of a tree using "node" as the provided root
        :param node: Node to use as root
        :return: Size of tree using provided node as the root
        """
        if node is None:
            return 0
        else:
            return self.curr_size(node.right) + self.curr_size(node.left) + 1
