import os
import random
import funcscale


def comparison():
    function_list = [
        list_iterator,
        iterator,
        generator
    ]
    argument_list = [
        (([random.randint(0, 10**n - 1) for i in range(10**n)], ), {})
        for n in range(8)
    ]
    funcscale.compare(function_list, argument_list, __name__)


# overrides module's methods.
def setup(function, argument, module_name):
    return os.linesep.join((
        'from ' + __name__ + ' import ' + function.__name__,
        'from ' + __name__ + ' import BinarySearchTree',
        'tree = BinarySearchTree()',
        'tree.insert_list' + funcscale.repr_argument(argument),
        'BinarySearchTree.__iter__ = ' + function.__name__
    ))


def stmt(fucntion, argument):
    return '[element for element in tree]'


funcscale.stmt = stmt
funcscale.setup = setup


#
#
#
def sample():
    # BinarySearchTree.__iter__ = list_iterator
    BinarySearchTree.__iter__ = iterator
    # BinarySearchTree.__iter__ = generator

    print('# 1) for statement')
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert_list((8, 3, 1, 6, 10, 4, 7, 14, 13))
    for element in binary_search_tree:
        print(element)

    print('# 2) built-in function taking itrable object')
    tree_a = BinarySearchTree()
    tree_b = BinarySearchTree()
    tree_a.insert_list((1, 2, 3, 4, 5, 6))
    tree_b.insert_list((3, 4, 5, 6, 2, 1))
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

    def insert_list(self, iterable):
        for element in iterable:
            self.insert(element)

    def generate_sorted_list(self):
        sorted_list = []
        if self.left:
            sorted_list.extend(self.left.generate_sorted_list())
        sorted_list.append(self.element)
        if self.right:
            sorted_list.extend(self.right.generate_sorted_list())
        return sorted_list

    def __iter__(self):
        raise NotImplementedError


#
def list_iterator(self):
    return iter(self.generate_sorted_list())


#
def iterator(self):
    return BinarySearchTreeIterator(self)


class BinarySearchTreeIterator(object):
    def __init__(self, root):
        self._route = []
        # add pseudo_node
        pseudo_node = BinarySearchTree()
        pseudo_node.right = root
        self._route.append({
            'node': pseudo_node,
            'is_right_child': True})

    def __next__(self):
        if self._current_node().right is not None:
            self._down()
        else:
            self._up()
        return self._current_node().element

    def _down(self):
        # down to right side one time, then
        self._route.append({
            'node': self._current_node().right,
            'is_right_child': True})
        # down to left side until reaching leaf
        while self._current_node().left is not None:
            self._route.append({
                'node': self._current_node().left,
                'is_right_child': False})

    def _up(self):
        # up while node is right child
        try:
            while self._route.pop()['is_right_child']:
                pass
        # reaching pseudo_node
        except IndexError:
            raise StopIteration

    def _current_node(self):
        return self._route[-1]['node']

    def __iter__(self):
        return self


#
def generator(self):
    if self.left:
        yield from iter(self.left)
    yield self.element
    if self.right:
        yield from iter(self.right)


#
#
#
if __name__ == "__main__":
    comparison()
    sample()
