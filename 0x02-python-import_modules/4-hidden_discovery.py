#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    contents = dir(hidden_4)

    for name in contents:
        if name[0:2] != "__":
            pass
        else:
            print(name)
