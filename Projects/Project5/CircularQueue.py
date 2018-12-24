class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
        Used for testing locally. Creates a string form of the queue
        :return: string form of queue
        """
        if self.size == 0:
            return "Empty"
        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def is_empty(self):
        """
        Determines whether or not the queue is empty
        :return: Returns True if queue is empty and False if it is not
        """
        return self.size == 0

    def __len__(self):
        """
        Gets the size of the queue
        :return: the size of the queue
        """
        return self.size

    def first_value(self):
        """
        Gets the value at the front of the queue
        :return: the value at the front of the queue
        """
        if self.is_empty():
            return None
        return self.data[self.head]

    def enqueue(self, val):
        """
        Adds a value to the back of the queue
        :param val: the value to be added to the queue
        :return: no return
        """
        self.data[self.tail] = val
        self.size += 1
        self.tail = (self.head + self.size) % self.capacity  # head doesn't need to be updated
        if self.size == self.capacity:
            self.grow()

    def dequeue(self):
        """
        Removes an element at the front of the queue and returns the element removed.
        If list is empty, do nothing.
        :return: the element removed from the list
        """
        if not self.is_empty():
            temp = self.data[self.head]
            self.data[self.head] = None
            self.head = (self.head + 1) % self.capacity  # tail doesn't need to be updated
            self.size -= 1
            if self.size <= (self.capacity / 4):
                self.shrink()
            return temp

    def grow(self):
        """
        Doubles the capacity of the list when size = capacity.
        :return: no return
        """
        self.capacity = self.capacity * 2  # update capacity

        holder = self.data  # create a list that holds the initial values of self.data
        self.data = [None] * self.capacity  # update (and fill) self.data to match new capacity
        temp = self.head  # use temp variable to hold value of head (will be changed in for loop)

        for num in range(self.size):  # for each real value (not None) in the queue
            self.data[num] = holder[temp]  # assign each value to self.data using num as the index
            temp = (1 + temp) % len(holder)  # update temp for next iteration through the loop
        self.head = 0  # update head to start of self.data
        self.tail = self.size  # (self.head + self.size) % self.capacity  # update tail

    def shrink(self):
        """
        If the size is 1/4 the capacity, the capacity should be halved.
        Capacity should always be above 4.
        :return: no return
        """
        if (self.capacity / 2) >= 4:  # only shrink if capacity/2 >= 4 (capacity should never be below 4)
            self.capacity = (self.capacity // 2)  # // used integer division to update capacity
            holder = self.data  # create a list that holds the initial values of self.data
            self.data = [None] * self.capacity  # update (and fill) self.data to match new capacity
            temp = self.head  # use temp variable to hold value of head (will be changed in for loop)

            for num in range(self.size):  # for each real value (not None) in the queue
                self.data[num] = holder[temp]  # assign each value to self.data using num as the index
                temp = (1 + temp) % len(holder)  # update temp for next iteration through the loop
            self.head = 0  # update head to start of self.data
            self.tail = self.size  # (self.head + self.size) % self.capacity  # update tail
