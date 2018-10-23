from Is_Number import isNumber
import pytest

@pytest.mark.parametrize ("word,expected", [
	("123", True),
	("-1.23 ", True),
	("NaN", False),
	("  ", False),
	(" ", False),
	("1.23s", False),
	("2.bad3", False),
	("23f", False),
])

def test_is_isNumber (word,expected):
	response = isNumber(word)
	assert response == expected



