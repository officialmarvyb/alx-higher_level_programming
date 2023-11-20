#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return (0)
    m = 0
    for i in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            m += 1
        except IndexError:
            break
    print("")
    return (m)
