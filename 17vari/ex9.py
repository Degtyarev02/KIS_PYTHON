class main:
    def __init__(self):
        self.__state = 'A'

    def pull(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'C':
            self.__state = 'E'
            return 5
        if self.__state == 'D':
            self.__state = 'E'
            return 6
        raise KeyError

    def show(self):
        if self.__state == 'A':
            self.__state = 'D'
            return 2
        if self.__state == 'B':
            self.__state = 'C'
            return 3
        if self.__state == 'C':
            self.__state = 'D'
            return 4
        raise KeyError

    def bolt(self):
        if self.__state == 'A':
            self.__state = 'E'
            return 1
        if self.__state == 'D':
            self.__state = 'F'
            return 6
        if self.__state == 'E':
            self.__state = 'F'
            return 8
        raise KeyError


o = main()
try:
    print(o.pull())  # 0
    print(o.show())  # 3
    print(o.show())  # 4
    print(o.pull())  # 6
    print(o.bolt())  # 8
except KeyError:
    print("KeyError")
