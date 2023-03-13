#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    tam = len(matrix[0])
    if tam is 0:
        print()
    else:
        tam = len(matrix[0])
        cont = 0
        for int in matrix:
            for int2 in int:
                cont += 1
                if cont == tam:
                    print("{:d}".format(int2), end="\n")
                else:
                    print("{:d} ".format(int2), end="")
            cont = 0
