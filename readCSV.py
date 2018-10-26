import csv
from Is_Number import isNumber

path = "test_data/test_data31.csv"
with open(path, newline='') as f:
    data = list(csv.reader(f))

for item in data:
    if(not isNumber(item[0]) or (not isNumber(item[1]))):
        print(item)
        data.remove(item)
    else:
        item[0] = float(item[0])
        item[1] = float(item[1])
