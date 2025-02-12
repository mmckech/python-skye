import modules.function as f

def test_func_wrong():
    assert f.func(3) == 5

def test_func_right():
    assert f.func(-5) == -4

    