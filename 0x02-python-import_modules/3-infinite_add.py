#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = sys.argv
    result = 0
    for b in range(len(a) - 1):
        result = result + int(a[b + 1])
    print("{}".format(result))
