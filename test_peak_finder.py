from peakfinder import peak_finder
import math


def test_peak_finder():
    data = []
    for x in range(1000):
        data.append(math.cos(x*2*math.pi/400))
    response = peak_finder(data)
    assert list(response) == [400, 800]
