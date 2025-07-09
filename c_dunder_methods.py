def main():
    right = Vec2(1, 0)
    up = Vec2(0, 1)
    diagonal = up + right

    directions = [up, right, diagonal]

    print(directions)
    for direction in directions:
        print(direction)

    print("Summation")
    up_three_over_four = diagonal + diagonal + diagonal + right
    print(up_three_over_four)

    print("iteration")
    for coordinate in up_three_over_four:
        print(coordinate)


class Vec2:
    def __init__(self, x, y):
        # It is idiomatic to name "private" attributes with a leading underscore.
        # By "private", I mean that any user of the class should not directly
        # access or modify the attribute.
        # However, Python prevents no such actions.
        # IDEs like VSCode often hide attributes that begin with an underscore
        # from users by default.
        self._x = x
        self._y = y

    def __add__(self, other):
        # The `__add__` dunder (D[ouble] UNDER[score]) method overloads `+`
        # There are corresponding methods for all mathematical operators
        return Vec2(self._x + other._x, self._y + other._y)

    def __iter__(self):
        # `__iter__` makes instances of the calss iterable
        yield self._x
        yield self._y

    def __repr__(self):
        return f"Vec2({self._x}, {self._y})"

    def __str__(self):
        return f"[{self._x} {self._y}]"


if __name__ == "__main__":
    main()
