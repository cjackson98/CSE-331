"""
# Project 4
# Name: Chris Jackson
# PID: A54488350
"""


class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """Returns the current number of items in the stack (size)
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :return: the size of stack
        """
        return self.size

    def is_empty(self):
        """Returns true if stack is empty, false if the stack has at least one item in it
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :return: True if stack is empty, False if stack is not empty
        """
        return self.size == 0

    def top(self):
        """Returns (but doesn't remove) the top item from the stack
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :return: Top element in stack (last element)
        """
        if self.is_empty():
            return None
        return self.data[self.size - 1]

    def push(self, val):
        """Adds an item to the stack. Grows stack if size equals capacity. No return
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :param: value The value to add to the stack
        :return: No return
        """
        if self.size >= self.capacity:
            self.grow()
        self.data[self.size] = val
        self.size += 1

    def pop(self):
        """Removes top item from the stack and returns it.
        Shrinks size of stack if size is less than or equal to half the capacity
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :return: The item removed from the top of the stack
        """
        if self.is_empty():
            return None

        end = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1

        if self.size <= (self.capacity / 2):
            self.shrink()
        return end

    def grow(self):
        """Doubles the capacity of the list
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :return: no return
        """
        temp = self.capacity
        self.capacity = self.capacity * 2
        while temp > 0:
            self.data.append(None)
            temp -= 1

    def shrink(self):
        """Halves the capacity of the list
        :param: self (instance of the class. Provides stack and its attributes/methods)
        :return: no return
        """
        self.capacity = self.capacity / 2
        if self.capacity < 2:
            self.capacity = 2
        cnt = 0
        for element in self.data:
            cnt += 1
        while cnt > self.capacity:
            self.data.pop()
            cnt -= 1


def reverse(stack):
    """Reverses the order of the given stack. Return is the new, reversed stack
    :param: stack The stack to be reversed
    :return: reversed version of stack
    """
    if stack.is_empty():
        return None
    new_stack = Stack()
    while stack.is_empty() is False:
        new_stack.push(stack.top())
        stack.pop()
    return new_stack

    # Original method used indexing which was not allowed:
    # new_stack = Stack()
    # end = stack.size - 1
    # while end >= 0:
    #     new_stack.push(stack.data[end])
    #     end -= 1
    # return new_stack


def replace(stack, old, new):
    """Replaces all items in a given stack that have the value "old" with the value "new".
    Returns the updated stack.
    :param: stack The stack with items to be replaced
    :param: old The values to replace
    :param: new What to replace the old values with
    :return: new stack with replaced items
    """
    if stack.is_empty():
        return
    new_stack = Stack()
    x = stack.size
    while x > 0:
        temp = stack.top()
        if temp == old:
            temp = new
        new_stack.push(temp)
        stack.pop()
        x = stack.size
    new_stack = reverse(new_stack)
    return new_stack

    # Original method used indexing which was not allowed:
    # if stack.size == 0:
    #     return None
    # end = stack.size - 1
    # while end >= 0:
    #     if stack.data[end] == old:
    #         stack.data[end] = new
    #     end -= 1
    # return stack
