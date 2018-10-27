import pytest
from readCSV import *
from Is_Number import is_number
from write_info import write_info
import json
import math
from dic import get_dictionary
from peakfinder import peak_finder


@pytest.mark.parametrize("path,expected", [
    ("test_data/test_data1.csv", 2),
    ("test_data/test_data5.csv", 2),
    ("test_data/test_data9.csv", 2),
    ("test_data/test_data15.csv", 2),
    ("test_data/test_data20.csv", 2),
    ("test_data/test_data25.csv", 2),
    ("test_data/test_data30.csv", 2),
    ("test_data/test_data16.csv", 2),
    ])
def test_read_csv(path, expected):
    data = read_csv(path)
    response = len(data[0])
    assert expected == response


@pytest.mark.parametrize("data,expected", [
    ([[1, 2], [1, 2]], [[1, 2], [1, 2]]),
    ([[1, "s"], [1, 2]], [[1, 2]]),
    ([[1, "2s"], [1, 2]], [[1, 2]]),
    ([['', 1], [1, 2]], [[1, 2]]),
    ([[1, 2000], [1, 2]], [[1, 2]]),
    ])
def test_validation(data, expected):
    response = validation(data)
    assert response == expected


@pytest.mark.parametrize("word,expected", [
    ("123", True),
    ("-1.23 ", True),
    ("NaN", False),
    ("  ", False),
    (" ", False),
    ("1.23s", False),
    ("2.bad3", False),
    ("23f", False),
    ])
def test_is_number(word, expected):
    response = is_number(word)
    assert response == expected


@pytest.mark.parametrize("file_name, file_info", [
    ("tech", "xzc"),
    ("hello", "123"),
    ("hhx", {"s": 100, "z": 200}),
    ("znb", "smart"+"cool"),
    ("steven", [1, 2, 3]),
    ])
def test_write_info(file_name, file_info):
    write_info(file_name, file_info)
    with open('{}.json'.format(file_name)) as p:
        d = json.load(p)
        p.close()
    assert d == file_info


@pytest.mark.parametrize("data,expected", [
    ([[1, 2], [1, 2]], [[1, 1], [2, 2]]),
    ([[1, "s"], [1, 2], [200, 201]], [[1, 1, 200], ["s", 2, 201]]),
    ])
def test_get_data(data, expected):
    response = get_data(data)
    assert response == expected


def test_get_dictionary():
    data = []
    for x in range(1001):
        data.append(math.cos(x*2*math.pi/400))
    dic_t = get_dictionary(range(1001), data)
    dic_expected = {"mean_hr_bpm": 0.12, "voltage_extremes": (1.0, -1.0),
                    "duration": 1000, "num_beats": 2,
                    "beats": [400, 800]}
    assert dic_expected == dic_t


def test_peak_finder():
    data = []
    for x in range(1000):
        data.append(math.cos(x*2*math.pi/400))
    response = peak_finder(data)
    assert list(response) == [400, 800]
