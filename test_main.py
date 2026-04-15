from main import add, subtract, multiply


def test_add():
    """Тест функции сложения."""
    assert add(2, 3) == 5


def test_add_negative():
    """Тест сложения с отрицательным числом."""
    assert add(-1, 1) == 0


def test_subtract():
    """Тест функции вычитания."""
    assert subtract(10, 4) == 6


def test_multiply():
    """Тест функции умножения."""
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    """Тест умножения на ноль."""
    assert multiply(5, 0) == 0
