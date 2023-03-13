#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val1 = 0
    val2 = 0
    if len(tuple_a) == 0:
        val1 = 0 + tuple_b[0]
        val2 = 0 + tuple_b[1]
    elif len(tuple_b) == 0:
        val1 = tuple_a[0] + 0
        val2 = tuple_a[1] + 0
    else:
        list_tmp1 = list(tuple_a)
        list_tmp2 = list(tuple_b)
        if len(list_tmp1) == 1:
            list_tmp1.append(0)
        if len(list_tmp2) == 1:
            list_tmp2.append(0)
        tuplex_final1 = tuple(list_tmp1)
        tuplex_final2 = tuple(list_tmp2)
        val1 = tuplex_final1[0] + tuplex_final2[0]
        val2 = tuplex_final1[1] + tuplex_final2[1]
    new_tuplex = (val1, val2)
    return(new_tuplex)
