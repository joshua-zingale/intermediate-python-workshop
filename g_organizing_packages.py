# When resolving import (i.e. when figuring out where to pull code from for an import statment)
# Python first checks the current directory for a package.
# Only if none is found does Python then search other places,
# like installed packages.


# In "namespace_package" are two packages, one that is comprised by a single file
# (package_1) and the other that is comprised of itself and one sub module,
# (package 2), which is done with a folder.
import namespace_package
from namespace_package import package_1
from namespace_package import package_2
from namespace_package import package_2
from namespace_package.package_2 import module_1


def main():
    # Modules are themselves objects of type "module"
    print(type(namespace_package))
    print(type(package_1))
    print(type(module_1))

    # In each module lies a function of the same name `foo`
    print(package_1.foo())
    print(package_2.foo())
    print(module_1.foo())

    # Module_1's `foo` is called via the re-import in package_2'sn__init__.py,
    print(package_2.module_1_foo())

    # Other packages can be imported as normal
    import random

    print(f"{random.randint(1, 10000)} is a random number")


if __name__ == "__main__":
    main()
