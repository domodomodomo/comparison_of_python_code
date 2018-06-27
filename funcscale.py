import timeit


def compare(function_list, argument_list):
    """Compare executing results against given functions."""
    _compare_result(function_list, argument_list)
    _compare_time(function_list, argument_list)


#
# _compare_result
#
def _compare_result(function_list, argument_list):
    for argument in argument_list:
        _all_same(function_list, argument)


def _all_same(function_list, argument):
    result_0 = _evaluate(function_list[0], argument)
    for function_k in function_list:
        result_k = _evaluate(function_k, argument)
        assert result_k == result_0


def _evaluate(function, argument):
    exec(setup(function, argument))
    return eval(stmt(function, argument))


#
# _compare_time
#
def _compare_time(function_list, argument_list):
    for argument in argument_list:
        print('#')
        for function in function_list:
            _measure(function, argument)


def _measure(function, argument):
    time = timeit.timeit(
        stmt=stmt(function, argument),
        setup=setup(function, argument),
        number=10)
    print(function.__name__.ljust(40), ':', "{0:7.4f}".format(time))


#
# util
#
def stmt(function, argument):
    """Return "function(*args, **kwargs)"."""
    return function.__name__ + repr_argument(argument)


def setup(function, argument):
    """Return "from module import function"."""
    # 'argument' is pseudo parameter for override.
    return 'from __main__ import ' + function.__name__


def repr_argument(argument):
    """Return "(*args, **kwargs)"."""
    args, kwargs = argument
    args = ', '.join('%s' % a for a in args)
    kwargs = ', '.join('%s=%s' % (p, a) for p, a in kwargs.items())
    joint = ', ' if args and kwargs else ''
    return '(' + joint.join((args, kwargs)) + ')'
