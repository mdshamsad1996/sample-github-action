from src.math_operation import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5
    assert add(1.5, 2.7) == 4.2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2
    assert subtract(10, -5) == 15
    assert subtract(2.5, 1.2) == 1.3