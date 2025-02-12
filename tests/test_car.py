from modules.car import *

def test_setgear():
    mycar = Car()
    other = Car()

    mycar.setgear(4)
    other.setgear(2)

    print("my car gear", mycar.gear)
    print("other car gear", other.gear)
