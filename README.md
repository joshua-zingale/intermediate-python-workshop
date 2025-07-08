# Python

Python is known as a simple language. Indeed, its clean syntax is condusive to the rapid creation of scripts, programs, and libraries with minimal boiler-plate. However, while Python may thus boast its simplicity, it also offers many robust features that lie unawares: for many are introducted to Python in an introductory programming course or through a playlist of tutorial videos, both of which are wont to leave out features useful for those who want to make clean, useful, shareable, and readable code.

Therefore, this workshop will touch on the following topics in Python that may have gone undiscussed during previous exposures to the language:
- Everything as an object
- Classes as object constructors
- Dunder methods (operator overloading)
- Decorators
- Namespaces (scoping rules)
- Installing Packages
- Organizing Packages
- Type hinting/Documenting

Exploring these reveals that Python is much more feature-full than what a cursory look from an introductory course would let on. In addition to and beyond these topics, there is the world of Python metaprogramming, which can leverage metadata from the code, like class names, inheritance hierarchies, and more, to modify behavior in specialized ways. This is mostly useful for creating libraries.

## Installing packages

Since installing a package is done outside of a Python script, the instructions lie partially here as opposed to lying fully in a Python file.

Python ships with `pip`, a command-line utility for installing Python packages into a Python environment. You can use

```bash
pip install PACKAGE_NAME
```

to install the package. If `pip` is not a recommended command, you can also access `pip` with

```bash
python3 -m pip install PACKAGE_NAME
```

For example, NumPy is ubiquitous among code that needs to run serious computation, especially with matrices or tensors, with large data structures. NumPy can be installed with

```bash
python3 -m pip install numpy.
```

Having installed the package, you now can see `f_installing_packages.py` for an example of using the package.

### Virtual Environments

You seldom (if ever) want to install a Python package to your global Python environment.
Python therefore ships with `venv`, a Python package for helping you manage your Python packages.
The reason for not installing packages globally is that one package may have conflicting
requirements for dependencies' versions to another.
It is moreover good practice to isolate one development environment from another.
For example, you do not want an update to a package for a depedency in one of your projects
to break another one of your projects.

To create a virtual environment, use

```bash
python3 -m venv my_venv
```

This creates a directory called `my_venv` in the current directory.
Hence, you can activate your virtual environment with

```bash
source my_venv/bin/activate
```

on Mac/Linux or with

```bash
.\my_venv\Scripts\activate
```

on Windows.