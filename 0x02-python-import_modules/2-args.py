#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv) - 1
    print("{:d} {:s}".format(length, "argument"), end="")
    if length != 1:
        print("{:s}".format("s"), end="")
    if length == 0:
        print(".")
    else:
        print(":")
        for i in range(1, length + 1):
            print("{:d}: {:s}".format(i, argv[i]))
