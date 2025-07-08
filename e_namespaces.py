y = 0


def main_1():
    y = 1

    def bar():
        y = 2

        def foo():
            y = 3
            print("from foo", y)

        foo()
        print("from bar", y)

    bar()
    print("from main", y)


for i in range(3):
    y += 1000


def main_2():
    y = 1

    def bar():
        nonlocal y
        y = 2

        def foo():
            global y
            y = 3
            print("from foo", y)

        foo()
        print("from bar", y)

    bar()
    print("from main", y)


def main_3():
    funcs = []

    for i in range(10):

        def func():
            return i

        funcs.append(func)
    for f in funcs:
        print(f())


def main_4():
    funcs = []

    for i in range(10):

        def func():
            b = i
            return b

        funcs.append(func)
    for f in funcs:
        print(f())


def main_5():
    funcs = []

    for i in range(10):

        def func(i=i):
            return i

        funcs.append(func)
    for f in funcs:
        print(f())


if __name__ == "__main__":
    input("Press ENTER to run main_1")
    main_1()
    print("from global", y)
    input("Press ENTER to run main_2")
    main_2()
    print("from global", y)
    input("Press ENTER to run main_3")
    main_3()
    input("Press ENTER to run main_4")
    main_4()
    input("Press ENTER to run main_5")
    main_5()
