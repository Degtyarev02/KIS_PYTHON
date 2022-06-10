class main:
    def __init__(self):
        self.__state = 'A'

    def clean(self):
        if self.__state == 'A':
            self.__state = 'C'
            return 1
        if self.__state == 'B':
            self.__state = 'C'
            return 3
        if self.__state == 'F':
            self.__state = 'D'
            return 8
        raise KeyError

    def melt(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'D':
            self.__state = 'E'
            return 5
        if self.__state == 'E':
            self.__state = 'F'
            return 6
        raise KeyError

    def stash(self):
        if self.__state == 'A':
            self.__state = 'E'
            return 2
        if self.__state == 'C':
            self.__state = 'D'
            return 4
        if self.__state == 'E':
            self.__state = 'B'
            return 7
        raise KeyError

o = main()

try:
    print(o.stash())
    print(o.stash())
    print(o.clean())
    print(o.stash())
except KeyError:
    print("Key Error")

