import csv
from Is_Number import isNumber
from peakfinder import *

path = "test_data/test_data15.csv"
with open(path, newline='') as f:
    data = list(csv.reader(f))

ecg = []
for item in data:
    if(not isNumber(item[0]) or (not isNumber(item[1]))):
        print(item)
        data.remove(item)
    else:
        item[0] = float(item[0])
        item[1] = float(item[1])
        ecg.append(item[1])
ecgindex= peakfinder(ecg)
newecg=[]
for i in ecgindex:
    newecg.append(ecg[i])
print(newecg)
print(len(newecg))
ecgindex= valleyfinder(ecg)
newecg=[]
for i in ecgindex:
    newecg.append(ecg[i])
print(newecg)
print(len(newecg))