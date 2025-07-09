import typing

# Type hints in python are entirely optional and do not affect the functionality
# of the code in anyway (unless metaprogramming and introspection are used to do
# some wackey things behind the scenes; but that is an edge case).

# Type hints, in addition to making your code more understandible to another
# programmer, empower type checkers to check for errors in your code, helping
# you to catch bugs early.

# If you are using a modern IDE like VSCode, type hints have the added benefit
# of giving you more useful hints, like possible methods to be called on an
# object.


def main():
    greet_print("World")
    print(greet("Friends"))
    print(add_then_stringify(3, 4))
    print(add(1.0, 2))


# Function (or method) parameters can be typed with "arg_name COLON type",
# as in
def greet_print(name: str):
    print(f"Hello, {name}!")


# The output's type for a function can also be specified with an arrow "->"
def greet(name: str) -> str:
    return f"Hello, {name}!"


# "|" or typing.Union can be used to specify that a parameter can be eiher
def add_then_stringify(a: int | float, b: typing.Union[int, float]) -> str:
    return str(a + b)


# If the output type of a function can be multiple things,
# it can likewise be specified to be multiple types:
def add(a: int | float, b: int | float) -> int | float:
    return a + b


# Often, when the output of a function can take on multiple types,
# the type is determined by the argument types.
# This can be made explicit with `typing.overload`.
# Note that the overloads must be shadowed by the actual implementation,
# so the overloads must appear before the implementation.
# To emphasize, only the final implementation will be used, no matter the
# types of the input arguments. Overloading is only for giving the
# type checker more information.


@typing.overload
def add(a: int, b: int) -> int: ...
@typing.overload
def add(a: int, b: float) -> float: ...
@typing.overload
def add(a: float, b: float) -> float: ...
@typing.overload
def add(a: float, b: int) -> float: ...
def add(a: int | float, b: int | float) -> int | float:
    return a + b


if __name__ == "__main__":
    main()
