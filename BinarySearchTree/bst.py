from BinarySearchTree.node import Node


class BST:
    """ Binary Search Tree """

    def __init__(self, root=None):
        """ init binary search tree """

        self.root = root

    @staticmethod
    def create_leaf(value):
        """ create leaf in tree """

        n = Node()
        n.value = value
        return n

    def add_leaf(self, value):
        """ add new leaf to tree """

        if self.root is None:
            self.root = self.create_leaf(value)
        else:
            self._add_leaf(value, self.root)

    def _add_leaf(self, value, node_ptr):
        """ recursive function to determine leaf position and add it """

        if value < node_ptr.value:
            if node_ptr.left is not None:
                self._add_leaf(value=value, node_ptr=node_ptr.left)
            else:
                node_ptr.left = self.create_leaf(value)
        elif value > node_ptr.value:
            if node_ptr.right is not None:
                self._add_leaf(value=value, node_ptr=node_ptr.right)
            else:
                node_ptr.right = self.create_leaf(value)
        else:
            print('Value already exists in tree')

    def height(self):
        """
            return height of tree :  largest number of edges in a
            path from the root node to a leaf node
        """

        if self.root is None:
            return 0
        return self._height(self.root, 0)

    def _height(self, node_ptr, height):
        """ recursive function to find height of each node and thus overall tree """

        if node_ptr is None:
            return height
        left_height = self._height(node_ptr.left, height+1)
        right_height = self._height(node_ptr.right, height+1)
        return max(left_height, right_height)

    def search(self, value):
        """ search for a given value : return True if found """

        if self.root is None:
            return False
        return self._search(value, self.root)

    def _search(self, value, node_ptr):
        """ recursive function to search left and right branches """

        if value == node_ptr.value:
            return True
        if value < node_ptr.value and node_ptr.left is not None:
            return self._search(value, node_ptr.left)
        elif value > node_ptr.value and node_ptr.right is not None:
            return self._search(value, node_ptr.right)
        return False

    def print_order(self):
        """ print order of the tree """
        if self.root is None:
            print('No values in tree')
            return
        self._print_order(self.root)

    def _print_order(self, node_ptr):
        """ in order traversal method to print from lowest to highest values """

        if node_ptr.left is not None:
            self._print_order(node_ptr.left)
        print(node_ptr.value, end=" ")
        if node_ptr.right is not None:
            self._print_order(node_ptr.right)
