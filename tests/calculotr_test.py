import pytest


@pytest.mark.parametrize(
    'x,y,result',
    [
        (1, 2, 3),
        (0, 0, 0),
        (1, 1, 2)
    ]
)
def test_add(calc, x, y, result):
    assert calc.add(x, y) == result


def test_sub(calc):
    assert calc.sub(1, 2) == -1
