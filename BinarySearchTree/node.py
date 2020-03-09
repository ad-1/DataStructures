# Data Structures - Binary Search Tree

""" Tree Node """


class Node:

    def __init__(self, value=None):
        """
        initialise node
        param value:  value for the node
        """
        self.value = value  # node value
        self.left = None  # value to left of node (less than value)
        self.right = None  # value to right of node (greater than value)
