#!/usr/bin/python3
def max_integer(my_list=[]):
    tam = len(my_list)
    if tam == 0:
        return None
    else:
        l = my_list[0]
        for iter in range(1, tam):
            if my_list[iter] > l:
                l = my_list[iter]
    return l
