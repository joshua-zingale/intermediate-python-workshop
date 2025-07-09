def main():
    # The most basic (and also seldom-to-be-used) way to create a new type (Class) is with `type`
    name = "Person"
    base_classes = (
        object,
    )  # If this were empty, "object" would implicitely be the base
    attributes = {
        "__init__": lambda self, name: setattr(self, "name", name),
        "greet": lambda self: f"Hello, {self.name}!",
    }
    Person = type(name, base_classes, attributes)
    world = Person("World")
    print(world.greet())

    # The functions above get "bound" to an instance, meaning that
    # the first argument, which is idiomatically called `self`,
    # is set always to be the instance of the class.
    # In the example above, self is bound to `world`.

    # The `class` keyword instead should be used,
    # which is syntactic sugur for a call to `type`.

    # The following will do the same as above.

    class Person(
        object
    ):  # Again, the word "object" can (and should) be left out because it is automatically inserted when no other base class is given.
        def __init__(self, name):
            self.name = name

        def greet(self):
            return f"Hello, {self.name}!"

    world = Person("World")
    print(world.greet())

    # This is an example of inheritance:
    # Each object is a personality of Bob
    class BobPersonality(Person):
        def __init__(self, personality):
            super().__init__("Bob")
            self.personality = personality

        def express(self):
            match self.personality:
                case "angry":
                    return "Arrahahahah!"
                case "happy":
                    return "*smiles*"
                case _:
                    return "I do not know how I feel right now."

    anger = BobPersonality("angry")

    print(anger.name)
    print(anger.greet())
    print(anger.express())


if __name__ == "__main__":
    main()
