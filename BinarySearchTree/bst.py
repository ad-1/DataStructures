from node import Node


""" Binary Search Tree """


class BST:

    def __init__(self, root=None):
        """
        initialise binary search tree with a root node
        param root: root of the tree is the topmost node
        """
        self.root = root

    @staticmethod
    def create_leaf(value):
        """
        create leaf (node) in tree
        param value: create a new leaf given a value
        return n: the newly created node
        """
        n = Node()  # instantiate new node object
        n.value = value  # set the node value equal to input value
        return n

    def add_leaf(self, value):
        """
        add new leaf to tree
        param value: insert a new node in the tree
        """
        if self.root is None:
            self.root = self.create_leaf(value)  # create node leaf
        else:
            self._add_leaf(value, self.root)  # add new leaf

    def _add_leaf(self, value, node_ptr):
        """
        recursive function to determine leaf position and add it
        param value: value to be inserted
        param node_ptr: pointer to the current node being analysed
        """
        if value < node_ptr.value:  # move down the left of the tree
            if node_ptr.left is not None:  # if node has a node to left
                # ... continue moving down to the left of the tree
                # value remains the same
                # update pointer to be the left node of the current node
                self._add_leaf(value=value, node_ptr=node_ptr.left)
            else:  # if node does not have node to the left...
                # ... add the new node in the left position
                node_ptr.left = self.create_leaf(value)
                node_ptr.left.parent = node_ptr
        elif value > node_ptr.value:  # move down the right of the tree
            if node_ptr.right is not None:  # if node has a node on the right
                # ... continue moving down right of the tree
                # value remains the same
                # update pointer to be the right node of the current node
                self._add_leaf(value=value, node_ptr=node_ptr.right)
            else:  # if node does not have a node to the right...
                # ... create new node on the right of the current node
                node_ptr.right = self.create_leaf(value)
                node_ptr.right.parent = node_ptr
        else:
            print('Value already exists in tree')

    def height(self):
        """
        return height of tree. The height is the largest
        number of edges in a path from the root node to a leaf node
        """
        if self.root is None:  # tree has no nodes
            return 0
        return self._height(self.root, 0)  # pass root node to determine height

    def _height(self, node_ptr, height):
        """
        recursive function to find height at each node.
        This therefore, determines overall height of tree.
        param node_ptr: node to be analysed
        param height: height at current level in tree
        return: height at current position in tree
        """
        if node_ptr is None:  # if node being analysed is None
            return height  # return the height up to this position
        # recursive call to move down left of tree and increment height
        left_height = self._height(node_ptr.left, height + 1)
        # recursive call to move down right of tree and increment height
        right_height = self._height(node_ptr.right, height + 1)
        max_height = max(left_height, right_height)  # max height at node
        return max_height

    def search(self, value):
        """
        search for a given value
        param value: value to find
        return: boolean depending on value existing
        """
        if self.root is None:
            return False
        return self._search(value, self.root)

    def _search(self, value, node_ptr):
        """
        recursive function to search for value
        param value: value to find
        param node_ptr: pointer to current node being analysed
        """
        if value == node_ptr.value:  # value found
            return True
        # move down left branch if conditions are met
        if value < node_ptr.value and node_ptr.left is not None:
            # update node pointer to be left node of current node
            return self._search(value, node_ptr.left)
        # move down right branch if conditions are met
        elif value > node_ptr.value and node_ptr.right is not None:
            # update node pointer to be right node of current node
            return self._search(value, node_ptr.right)
        return False  # node is not found

    def print_order(self):
        """ print order of the tree """
        if self.root is None:
            print('No values in tree')
            return
        self._print_order(self.root)

    def _print_order(self, node_ptr):
        """
        In order traversal. Print from lowest to highest values.
        param node_ptr: current node being analysed
        """
        if node_ptr.left is not None:  # node to the left exists
            self._print_order(node_ptr.left)  # move down left
        print(node_ptr.value, end=" ")  # print node value
        if node_ptr.right is not None:  # node to the right exists
            self._print_order(node_ptr.right)  # move down right

    def find(self, value):
        """
        find a node given a value
        param value: value of node to find
        return: node object if found or None
        """
        if self.root is not None:
            return self._find(value, self.root)
        return None

    def _find(self, value, node_ptr):
        """
        recursive function to find node in tree
        param value: value to find
        param node_ptr: pointer to current node
        """
        if node_ptr.value == value:  # if current node has search value
            return node_ptr  # return pointer to current node
        # if value is less than current node value ...
        # ... and current node has a left child
        if value < node_ptr.value and node_ptr.left is not None:
            return self._find(value, node_ptr.left)  # recursive call to find
        # if value is greater than current node value ...
        # ... and current node has a child to the right
        elif value > node_ptr.value and node_ptr.right is not None:
            return self._find(value, node_ptr.right)  # recursive call to find
        return None

    def find_min_value(self, value):
        pass

    def delete(self, value):
        """
        delete node from tree.
        Three cases:
        1. Deleting a leaf node
        2. Deleting a node with a single child node
        3. Deleting a node with two child nodes
        param value: value to delete if exists
        param node_ptr: pointer to current node
        """
        node = self.find(value)
        print(node, node.value)
        # node is a leaf node if left and right pointers are None
        if node.left is None and node.right is None:
            self.delete_leaf(node)
        # node has a single child on the left
        elif node.right is None:
            self.delete_node_single_child(node, has_left_child=True)
        # node has a single child on the right
        elif node.left is None:
            self.delete_node_single_child(node, has_left_child=False)
        else:
            self.delete_node_two_children(node)

    def delete_leaf(self, node):
        """
        Deletion case 1. Delete if node is leaf
        param node: leaf node to delete
        """
        if node.parent.left == node:
            node.parent.left = None
        elif node.parent.right == node:
            node.parent.right = None
        node = None

    def delete_node_single_child(self, node, has_left_child):
        """
        Delete a node that has only one child
        param node: node to be deleted
        param has_left_child: bool indicating if child is on left or right
        """
        if has_left_child:
            node.parent.left = node.left
        else:
            node.parent.right = node.right

    def delete_node_two_children(node):
        print('Delete node with two children')
