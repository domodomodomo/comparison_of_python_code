import funcscale
import random


def comparison():
    funcscale.function_list = [
        while_statement_insert,
        while_statement_append,
        for_statement,
        for_statement_list_comprehension,
        filter_function,
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**i - 1) for _ in range(10**i)], ), {})
        for i in range(5)
    ]
    return funcscale.compare()


#
#
#
def while_statement_insert(lst):
    lst, tmp = [], lst
    while tmp:
        e = tmp.pop()
        if e % 2 == 0:
            lst.insert(0, e)
    return lst


def while_statement_append(lst):
    lst, tmp = [], lst
    while tmp:
        e = tmp.pop()
        if e % 2 == 0:
            lst.append(e)
    else:
        lst.reverse()
    return lst


def for_statement(lst):
    def reversed_enumerate(seq):
        return zip(reversed(range(len(lst))), reversed(lst))

    for i, e in reversed_enumerate(lst):
        if e % 2 == 1:
            del lst[i]
    return lst


def for_statement_list_comprehension(lst):
    lst = [e for e in lst if e % 2 == 0]
    return lst


def filter_function(lst):
    lst = list(filter(lambda e: e % 2 == 0, lst))
    return lst


#
#
#
if __name__ == '__main__':
    while_statement_append(list(range(10)))
    while_statement_insert(list(range(10)))
    for_statement(list(range(10)))
    for_statement_list_comprehension(list(range(10)))
    filter_function(list(range(10)))
    comparison()
