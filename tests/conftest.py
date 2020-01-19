from src.calculator import Calculator
import pytest


@pytest.fixture(scope="session", autouse=True)
def calc():
    calculator = Calculator()
    return calculator
