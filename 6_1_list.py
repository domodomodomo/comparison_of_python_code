import os
import funcscale


def comparison():
    function_list = [
        list_iterator,
        iterator,
        generator
    ]
    argument_list = [
        (([None] * 10**n, ), {}) for n in range(6)
    ]
    funcscale.compare(function_list, argument_list, __name__)


# overrides module's method.
def setup(function, argument, module_name):
    return os.linesep.join((
        'from ' + __name__ + ' import ' + function.__name__,
        'from ' + __name__ + ' import Container',
        'container = Container' + funcscale.repr_argument(argument),
        'Container.__iter__ = ' + function.__name__
    ))


def stmt(fucntion, argument):
    return '[element for element in container]'


funcscale.stmt = stmt
funcscale.setup = setup


#
#
#
def sample():
    Container.__iter__ = list_iterator
    # Container.__iter__ = iterator
    # Container.__iter__ = generator

    print('# 1) for statement')
    container = Container(('Yaruo', 'Yaranaio', 'Yarumi'))
    for element in container:
        print(element)

    print('# 2) built-in function taking itrable object')
    container_a = Container(('hello', 'nihao', 'hola'))
    container_b = Container(('nihao', 'holda', 'hello'))
    print(set(container_a) == set(container_b))  # True

    print('# 3) you do not need implement list method.')
    print(list(container))


#
#
#
class Container(object):
    def __init__(self, iterable):
        self._list = list(iterable)

    def __iter__(self):
        raise NotImplementedError


#
def list_iterator(self):
    return iter(self._list)


#
def iterator(self):
    return ListIterator(self._list)


class ListIterator(object):
    def __init__(self, list_):
        self._list = list_
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            element = self._list[self._index]
            self._index = self._index + 1
            return element
        except IndexError:
            raise StopIteration
        """
        # このようなケースでは if よりも try が速い。
        if self._index < len(self._list):
            element = self._list[self._index]
            self._index = self._index + 1
            return element
        else:
            raise StopIteration
        """


#
def generator(self):
    index = 0
    while True:
        try:
            yield self._list[index]
        except IndexError:
            break
        else:
            index = index + 1


#
#
#
if __name__ == "__main__":
    comparison()
    sample()