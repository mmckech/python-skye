from modules.myclass import *

def test_f():
    # arrange
    my = MyClass()
    expected = "hello world"

    # act
    actual = my.greet()

    # assert
    assert actual == expected

def test_greet_custom():
    # arrange
    expected = "custom greeting"
    my = MyClass(expected)

    # act
    actual = my.greet()

    # assert
    assert actual == expected

def test_greet_named():
    # arrange
    expected = "happy hump day"
    my = MyClass(expected)

    # act
    actual = my.greet("tommy")

    # assert
    assert actual == expected + ", " + "tommy"
