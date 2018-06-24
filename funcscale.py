import timeit


def compare(function_list, argument_list, module_name):
    """Compare executing results against given functions."""
    _compare_time(function_list, argument_list, module_name)
    _compare_result(function_list, argument_list, module_name)


#
# _compare_time
#
def _compare_time(function_list, argument_list, module_name):
    for argument in argument_list:
        print('#')
        for function in function_list:
            _measure(function, argument, module_name)


def _measure(function, argument, module_name):
    time = timeit.timeit(
        stmt=stmt(function, argument),
        setup=setup(function, argument, module_name),
        number=10)
    print(function.__name__.ljust(40), ':', "{0:7.4f}".format(time))


#
# _compare_result
#
def _compare_result(function_list, argument_list, module_name):
    for argument in argument_list:
        _all_same(function_list, argument, module_name)


def _all_same(function_list, argument, module_name):
    result_0 = _evaluate(function_list[0], argument, module_name)
    for function_k in function_list:
        result_k = _evaluate(function_k, argument, module_name)
        assert result_k == result_0


def _evaluate(function, argument, module_name):
    exec(setup(function, argument, module_name))
    return eval(stmt(function, argument))


#
# util
#
def stmt(function, argument):
    """Return "function(*args, **kwargs)"."""
    return function.__name__ + repr_argument(argument)


def setup(function, argument, module_name):
    """Return "from module import function"."""
    # 'argument' is pseudo parameter for override.
    return 'from ' + module_name + ' import ' + function.__name__


def repr_argument(argument):
    """Return "(*args, **kwargs)"."""
    args, kwargs = argument
    args = ', '.join('%s' % a for a in args)
    kwargs = ', '.join('%s=%s' % (p, a) for p, a in kwargs.items())
    joint = ', ' if args and kwargs else ''
    return '(' + joint.join((args, kwargs)) + ')'
