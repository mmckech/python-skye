from modules.myclass import *

def test_f():
    # arrange
    my = MyClass()
    expected = "hello world"

    # act
    actual = my.greet()

    # assert
    assert actual == expected