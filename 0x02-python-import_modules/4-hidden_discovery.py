#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    functions = dir(hidden_4)
    for func in functions:
        if func[0:2] != "__":
            print("{:s}".format(func))
