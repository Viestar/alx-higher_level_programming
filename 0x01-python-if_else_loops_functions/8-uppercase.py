#!/usr/bin/python3
def uppercase(strn):
    string = ""
    for c in strn:
        if ord(c) > 96 and ord(c) < 123:
            char = (ord(c) - 32)
            string += "%c" % char
        else:
            string += "%c" % c
    print(f"{string:s}")
