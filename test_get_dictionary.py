import math
from dic import get_dictionary


def test_get_dictionary():
    data = []
    for x in range(1001):
        data.append(math.cos(x*2*math.pi/400))
    dic_t = get_dictionary(range(1001), data)
    dic_expected = {"mean_hr_bpm": 0.12, "voltage_extremes": (1.0, -1.0),
                    "duration": 1000, "num_beats": 2,
                    "beats": [400, 800]}
    dic_t["beats"] = list(dic_t["beats"])
    assert dic_expected == dic_t
