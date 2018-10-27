import csv
from Is_Number import *


def read_csv(path):
    with open(path, newline='') as f:
        data = list(csv.reader(f))
    return data


def validation(data):
    for item in data[:]:
        if not is_number(item[0]) or (not is_number(item[1])):
            data.remove(item)
        else:
            item[0] = float(item[0])
            item[1] = float(item[1])
            if item[1] > 300:
                data.remove(item)
    return data


def get_data(data):
    time = []
    ecg = []
    for item in data:
        time.append(item[0])
        ecg.append(item[1])
    return [time, ecg]
