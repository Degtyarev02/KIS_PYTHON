class main:
    def __init__(self):
        self.__state = 'A'

    def bolt(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'B':
            self.__state = 'C'
            return 2
        if self.__state == 'C':
            self.__state = 'D'
            return 4
        if self.__state == 'D':
            self.__state = 'E'
            return 5
        if self.__state == 'F':
            self.__state = 'D'
            return 8
        if self.__state == 'G':
            self.__state = 'A'
            return 9
        raise KeyError

    def stash(self):
        if self.__state == 'A':
            self.__state = 'C'
            return 1
        if self.__state == 'B':
            self.__state = 'E'
            return 3
        if self.__state == 'E':
            self.__state = 'F'
            return 6
        if self.__state == 'F':
            self.__state = 'G'
            return 7
        raise KeyError


o = main()

try:
    print(o.bolt())  # 0
    print(o.stash())  # 3
    print(o.stash())  # 6
    print(o.bolt())  # 8
    print(o.bolt())  # 5
    print(o.stash())  # 6
    print(o.stash())  # 7
    print(o.bolt())  # 9
    print(o.stash())  # 1
    print(o.bolt())  # 4
    print(o.bolt())  # 5
    print(o.stash())  # 6
    print(o.bolt())  # 8
except KeyError:
    print("KE")
