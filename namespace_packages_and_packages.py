import namespace_package
from namespace_package import package_1
from namespace_package import package_2
from namespace_package import package_2
from namespace_package.package_2 import module_1

def main():
    print(type(namespace_package))
    print(type(package_1))
    print(type(module_1))
    
    print(package_1.foo())
    print(package_2.foo())
    print(package_2.module_1_foo())
    print(module_1.foo())

    import random
    print(f"{random.randint(1,10000)} is a random number")


if __name__ == "__main__":
    main()
