#!/usr/bin/python3
def uppercase(str):
    string = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            char = (ord(c) - 32)
            string += "%c" % char
        else:
            string += "%c" % c
    print("{}".format(string))
