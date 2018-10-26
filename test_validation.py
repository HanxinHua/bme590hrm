from readCSV import validation
import pytest


@pytest.mark.parametrize("data,expected", [
    ([[1, 2], [1, 2]], [[1, 2], [1, 2]]),
    ([[1, "s"], [1, 2]], [[1, 2]]),
    ([[1, "2s"], [1, 2]], [[1, 2]]),
    ([['', 1], [1, 2]], [[1, 2]]),
    ([[1, 2000], [1, 2]], [[1, 2]]),
    ])
def test_is_number(data, expected):
    response = validation(data)
    assert response == expected
