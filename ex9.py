class main:
    def __init__(self):
        self.__state = 'A'

    def crash(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'C':
            self.__state = 'G'
            return 6
        raise KeyError

    def show(self):
        if self.__state == 'A':
            self.__state = 'H'
            return 1
        if self.__state == 'B':
            self.__state = 'C'
            return 4
        if self.__state == 'D':
            self.__state = 'E'
            return 7
        if self.__state == 'F':
            self.__state = 'G'
            return 9
        raise KeyError

    def print(self):
        if self.__state == 'A':
            self.__state = 'G'
            return 2
        if self.__state == 'G':
            self.__state = 'H'
            return 11
        raise KeyError

    def log(self):
        if self.__state == 'A':
            self.__state = 'E'
            return 3
        if self.__state == 'C':
            self.__state = 'D'
            return 5
        if self.__state == 'F':
            self.__state = 'C'
            return 10
        if self.__state == 'E':
            self.__state = 'F'
            return 8
        raise KeyError


o = main()
try:
    print(o.crash())
    print(o.show())
    print(o.log())
    print(o.show())
    print(o.print())
    print(o.log())
    print(o.log())
    print(o.log())
    print(o.log())
    print(o.show())
    print(o.log())
    print(o.show())
    print(o.print())
except KeyError:
    print("KeyError")
