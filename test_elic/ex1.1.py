class main:
    def __init__(self):
        self.__state = 'A'

    def cull(self):
        if self.__state == 'A':
            self.__state = 'D'
            return 1
        if self.__state == 'C':
            self.__state = 'A'
            return 5
        if self.__state == 'E':
            self.__state = 'F'
            return 8
        if self.__state == 'G':
            self.__state = 'A'
            return 11
        raise KeyError

    def skip(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'D':
            self.__state = 'H'
            return 7
        if self.__state == 'C':
            self.__state = 'D'
            return 4
        if self.__state == 'F':
            self.__state = 'G'
            return 9
        if self.__state == 'G':
            self.__state = 'H'
            return 10
        raise KeyError

    def model(self):
        if self.__state == 'B':
            self.__state = 'C'
            return 3
        if self.__state == 'D':
            self.__state = 'E'
            return 6
        if self.__state == 'A':
            self.__state = 'E'
            return 2
        raise KeyError


o = main()
try:
    print(o.cull())
    print(o.model())
    print(o.cull())
    print(o.skip())
    print(o.cull())
    print(o.skip())
    print(o.model())
    print(o.model())
except KeyError:
    print("KeyError")