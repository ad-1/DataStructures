# Data Structures -  Binary Search Tree

from bst import BST
import random


# Program driver
if __name__ == '__main__':

    # number of values between upper and lower limits
    lower, upper, n_val = 1, 1000, 100

    # value used to test search method in bst
    search_val = random.randint(lower, upper)

    # generate array of non-repeating random values
    values = random.sample(range(lower, upper), n_val)

    print(values, end='\n\n')

    bst = BST()  # instantiate binary search tree object
    for v in values:
        bst.add_leaf(v)  # add leafs to tree

    bst.print_order()  # print all values in order
    print('\n\nheight of binary tree: ', bst.height())
    print('\nfound: {} : {}\n'.format(search_val, bst.search(search_val)))
