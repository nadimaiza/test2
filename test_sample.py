import pytest

@pytest.fixture
def numbers():
    return 10, 5

class TestMathOperations:
    def test_addition(self, numbers):
        x, y = numbers
        assert x + y == 15

    def test_subtraction(self, numbers):
        x, y = numbers
        assert x - y == 5

    def is_positive(self, number):  # Fonction à tester
        return number > 0

    def test_is_positive(self):  # Méthode de test avec `self`
        assert self.is_positive(5) is True
        assert self.is_positive(-1) is False



