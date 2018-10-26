import csv
from Is_Number import isNumber
from peakfinder import *
from dic import *


path = "test_data/test_data1.csv"
with open(path, newline='') as f:
    data = list(csv.reader(f))

time = []
ecg = []
for item in data:
    if(not isNumber(item[0]) or (not isNumber(item[1]))):
        print(item)
        data.remove(item)
    else:
        item[0] = float(item[0])
        item[1] = float(item[1])
        time.append(item[0])
        ecg.append(item[1])
metrics = getdictionary(time, ecg)
print(metrics)