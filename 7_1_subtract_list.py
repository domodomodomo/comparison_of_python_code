import funcscale


def comparison():
    function_list = [
        subtract_list_try_remove,
        subtract_list_for_if,
        subtract_list_while_if
    ]
    argument_list = [
        ((list1, list2), {}),
        ((list3, list4), {}),
        ((list5, list6), {}),
    ]
    funcscale.compare(function_list, argument_list)


#
#
#
def subtract_list_try_remove(lst1, lst2):
    lst = lst1.copy()
    for element in lst2:
        try:
            lst.remove(element)
        except ValueError:
            continue
    return lst


def subtract_list_for_if(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        for i, e1 in enumerate(lst):
            if e1 == e2:
                del lst[i]
                break
    return lst


def subtract_list_while_if(lst1, lst2):
    lst = lst1.copy()
    for e2 in lst2:
        n = len(lst)
        i = 0
        while i < n:
            # e1 = lst[i]
            if lst[i] == e2:
                del lst[i]
                break
            i += 1
    return lst


#
#
#
list1 = [i for i in range(100, 199)]
list2 = [i for i in range(200, 299)]
list3 = [i for i in range(100, 199)]
list4 = list(reversed(list1))
list5 = [i for i in range(1000, 1999)]
list6 = [i for i in range(2000, 2999)]


#
#
#
if __name__ == '__main__':
    comparison()
