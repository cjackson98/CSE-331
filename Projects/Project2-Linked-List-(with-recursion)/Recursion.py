"""
PROJECT 2 - Recursion
Name: Chris Jackson
PID: 
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """"
    Adds the provided value into a linked list (in ascending order) with "node" (head node).
    Returns the starting node of the linked list.
    """

    if node is None or node.value >= value:
        new_node = LinkedNode(value, node)
        return new_node
    else:
        node.next_node = insert(value, node.next_node)
        return node


def string(node):
    """
    Creates a string of each item in linked list, starting at "node".
    Items of the list should be separated by a comma and a single space
     and should have no leading or trailing comma.
    Returns the string.
    """
    if node is None:
        return ''
    if node.next_node is not None:
        return str(node) + ', ' + string(node.next_node)
    if node.next_node is None:
        return str(node)


def reversed_string(node):
    """
    Creates and returns a string of each element in the list with
     head node, in reverse order. The values should be separated by
     a comma and a single space, with no leading or trailing comma.
    """
    if node is None:
        return ''
    if node.next_node is not None:
        return reversed_string(node.next_node) + ', ' + str(node)
    return str(node)


def remove(value, node):
    """"
    Goes through the list and removes the first node in the list with the value matching
     the one provided.
    Returns the starting node of the list.
    """

    if node is None:
        return None
    elif node.value == value:  # if the value is found at starting position
        return node.next_node
    else:
        node.next_node = remove(value, node.next_node)  # return to start with next_node as "node"
        return node


def remove_all(value, node):
    """
    Removes all nodes in the list that have a value matching the one provided
     starting at "node" (head node).
    Returns the starting node of the list.
    """
    if node is None:  # if head node is None
        return None
    if node.value == value:  # if head node value matches given value
        return remove_all(value, node.next_node)
    node.next_node = remove_all(value, node.next_node)  # send back with next node in list
    return node


def search(value, node):
    """
    Searches for given value in list starting at the given "head" node.
    If the value is in the list returns true, otherwise returns false.
    """
    if node is None:
        return False
    if node.value == value:
        return True
    return search(value, node.next_node)


def length(node):
    """
    Returns the length of the list starting at the provided node (head node)
    """
    if node is not None:
        return 1 + length(node.next_node)
    if node is None:
        return 0


def sum_all(node):
    """
    Calculates the sum of all the nodes in the list starting at "node" (head node).
    Returns the sum.
    """
    if node is not None:
        return node.value + sum_all(node.next_node)
    if node is None:
        return 0


def count(value, node):
    """
    Counts how many times a given value is in the list starting at "node" (head node).
    """
    if node is not None:
        if node.value == value:
            return 1 + count(value, node.next_node)
        else:
            return count(value, node.next_node)
    else:
        return 0
