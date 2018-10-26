from readCSV import get_data
import pytest


@pytest.mark.parametrize("data,expected", [
    ([[1, 2], [1, 2]], [[1, 1], [2, 2]]),
    ([[1, "s"], [1, 2], [200, 201]], [[1, 1, 200], ["s", 2, 201]]),
    ])
def test_get_data(data, expected):
    response = get_data(data)
    assert response == expected
