from namespace_package import package_1


def main():
    # Variables store references to objects
    one = 1
    two = one + one
    hello = "hello"

    # These are the types of the objects
    print(type(one))
    print(type(two))
    print(type(one + one))
    print(type(hello))
    print(type(package_1))

    # This gives all of the attributes available to each object
    print(one.__dir__())
    print(hello.__dir__())

    # Calling an attribute
    print(hello.swapcase())

    # Functions are objects
    # As an object, arbitrary attributes can be defined thereon
    def add_two_nums(a, b):
        return a + b

    add_two_nums.arbitrary_attribute = (
        "This is an arbirary value for this arbitrary attribute."
    )
    print(add_two_nums.arbitrary_attribute)

    # Since functions are objects like any other,
    # they can themselves be function arguments or return values

    def get_multiplier(factor):
        def multiply(value):
            return value * factor

        return multiply

    mul_2 = get_multiplier(2)
    mul_3 = get_multiplier(3)

    print(mul_2(10))
    print(mul_3(10))


if __name__ == "__main__":
    main()
