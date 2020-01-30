# Binary Search Driver Program

from BST import BST
import random


def main():
    """ test binary search tree methods """

    lower, upper, n_val = 1, 1000, 300
    find_val = random.randint(lower, upper)

    values = random.sample(range(lower, upper), n_val)
    print(values, end='\n\n')

    bst = BST()
    for v in values:
        bst.add_leaf(v)

    bst.print_order()
    print('\nheight of binary tree: ', bst.height())
    print('found value: {} : {}'.format(find_val, bst.search(find_val)))


if __name__ == '__main__':
    main()
