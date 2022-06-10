class main:
    def __init__(self):
        self.__state = 'A'

    def color(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'B':
            self.__state = 'C'
            return 3
        if self.__state == 'C':
            self.__state = 'D'
            return 4
        raise KeyError

    def copy(self):
        if self.__state == 'A':
            self.__state = 'D'
            return 2
        if self.__state == 'D':
            self.__state = 'E'
            return 5
        if self.__state == 'F':
            self.__state = 'A'
            return 8
        if self.__state == 'E':
            self.__state = 'F'
            return 7
        raise KeyError

    def model(self):
        if self.__state == 'D':
            return 6
        if self.__state == 'A':
            self.__state = 'E'
            return 1


o = main()
try:
    print(o.model())
    print(o.copy())
    print(o.copy())
    print(o.color())
    print(o.color())
    print(o.color())
    print(o.model())
    print(o.model())
except KeyError:
    print("KeyError")




