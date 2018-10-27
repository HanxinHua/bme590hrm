from output import write_info
import json
import pytest


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
