import csv

path = "test_data/"
for file in glob.glob(os.path.join(path, '*.csv')):
    with open(file,'r') as f:
        text=f.read()
        print(text)