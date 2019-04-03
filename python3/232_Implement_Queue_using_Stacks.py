""" Use two stack, one for input and one for output
    Push new element into input, pop and peek from output"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.output) == 0:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.output)  == 0:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.input and not self.output