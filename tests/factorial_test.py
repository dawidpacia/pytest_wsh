from src.factorial import factorial


def test_positive():
    assert factorial(4) == 24

def test_negative():
    assert factorial(-5) == False

def test_zero():
    assert factorial(0) == 1

def test_string():
    assert factorial("test") == False

def test_float():
    assert factorial(1.5) == False

