# `unittest` is Python's built-in unit-test framework.
# PyTest, however, is prefered by most because of its
# proclivity not to require as high an amount of boiler
# plate.
from namespace_package import package_1, package_2

def test_package_1_foo():
    assert "Package 1" in package_1.foo()

def test_package_2_foo():
    assert "Package 2" in package_2.foo()

def test_package_2_module_1_foo():
    assert "Package 2" in package_2.foo() and "module 1" in package_2.module_1_foo()
