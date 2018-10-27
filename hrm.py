from readCSV import *
from write_info import write_info
from dic import get_dictionary
import os


def hrm():
    dir_path = 'test_data'
    out_path = 'results/'
    for f in os.listdir(dir_path):
        if f.endswith('.csv'):
            path = dir_path+"/"+f
            data = read_csv(path)
            v_data = validation(data)
            time, ecg = get_data(v_data)
            metrics = get_dictionary(time, ecg)
            write_info(out_path+f[:-4], metrics)


if __name__ == "__main__":
    hrm()
