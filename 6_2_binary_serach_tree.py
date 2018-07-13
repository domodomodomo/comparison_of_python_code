import funcscale
import random


def comparison():
    # Create parameters.
    function_list = [
        list_iterator,
        iterator,
        generator
    ]
    argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(7)
    ]

    def setup(function, argument):
        return '\n'.join((
            'from __main__ import ' + function.__name__,
            'from __main__ import BinarySearchTree',
            'tree = BinarySearchTree()',
            'tree.insert_iterable' + funcscale.repr_argument(argument),
            'BinarySearchTree.__iter__ = ' + function.__name__
        ))

    def stmt(fucntion, argument):
        return '[element for element in tree]'

    # Set parameters.
    funcscale.function_list = function_list
    funcscale.argument_list = argument_list
    funcscale.stmt = stmt
    funcscale.setup = setup

    # Execute.
    funcscale.compare()


#
#
#
def sample():
    # BinarySearchTree.__iter__ = list_iterator
    BinarySearchTree.__iter__ = iterator
    # BinarySearchTree.__iter__ = generator

    print('# 1) for statement')
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert_iterable((8, 3, 1, 6, 10, 4, 7, 14, 13))
    for element in binary_search_tree:
        print(element)

    print('# 2) built-in function taking itrable object')
    tree_a = BinarySearchTree()
    tree_b = BinarySearchTree()
    tree_a.insert_iterable((1, 2, 3, 4, 5, 6))
    tree_b.insert_iterable((3, 4, 5, 6, 2, 1))
    print(set(tree_a) == set(tree_b))  # True

    print('# 3) you do not need implement list method.')
    print(list(binary_search_tree))
    print(binary_search_tree.generate_sorted_list())


#
#
#
class BinarySearchTree(object):
    def __init__(self):
        self.element = None
        self.left = None
        self.right = None

    def insert(self, element):
        if self.element is None:
            self.element = element
        # if less, add to left tree
        elif element <= self.element:
            if self.left is None:
                self.left = BinarySearchTree()
            self.left.insert(element)
        # if bigger, add to right tree
        elif element > self.element:
            if self.right is None:
                self.right = BinarySearchTree()
            self.right.insert(element)

    def insert_iterable(self, iterable):
        for element in iterable:
            self.insert(element)

    def generate_sorted_list(self):
        sorted_list = []
        if self.left is not None:
            sorted_list.extend(self.left.generate_sorted_list())
        sorted_list.append(self.element)
        if self.right is not None:
            sorted_list.extend(self.right.generate_sorted_list())
        return sorted_list

    def __iter__(self):
        raise NotImplementedError


# 1.
def list_iterator(self):
    return iter(self.generate_sorted_list())


# 2.
def iterator(self):
    return BinarySearchTreeIterator(self)


class BinarySearchTreeIterator(object):
    def __init__(self, root):
        pseudo_node = BinarySearchTree()
        pseudo_node.right = root
        self._route = [pseudo_node]

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_node().right is not None:
            self._down()
        else:
            self._up()
        return self._current_node().element

    def _down(self):
        self._route.append(self._current_node().right)
        while self._current_node().left is not None:
            self._route.append(self._current_node().left)

    def _up(self):
        while self._route.pop() == self._current_node_safety().right:
            pass

    def _current_node(self):
        return self._route[-1]

    def _current_node_safety(self):
        try:
            return self._route[-1]
        except IndexError:
            raise StopIteration


# 3.
def generator(self):
    if self.left is not None:
        yield from self.left
    yield self.element
    if self.right is not None:
        yield from self.right


#
#
#
if __name__ == "__main__":
    sample()
    comparison()
