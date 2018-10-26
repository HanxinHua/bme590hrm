import pytest
from readCSV import read_csv


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
def test_read_file_data(path, expected):
    data = read_csv(path)
    response = len(data[0])
    assert expected == response
