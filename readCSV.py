import csv
from Is_Number import *
import sys
import logging


def read_csv(path):
    """
        :Synopsis: Read input from files
        :param path: The path of the input file
        :returns: The data (including time and ecg) in the file
        :raise: Data should be stored as two columns: time, ecg
    """
    with open(path, newline='') as f:
        data = list(csv.reader(f))
    for item in data:
        try:
            assert (len(item) == 2)
        except AssertionError:
            logging.error(path+" : Data should be stored as two columns:"
                               " time, ecg")
            logging.error("Process exit\n\n")
            sys.exit(1)
    return data


def validation(data):
    """
        :Synopsis: Remove wrong data from the original version
        :param data: The data (including time and ecg)
        :returns: The data removed with wrong style of data
     """
    for item in data[:]:
        if not is_number(item[0]) or (not is_number(item[1])):
            logging.warning("Find non-number data")
            data.remove(item)
        else:
            item[0] = float(item[0])
            item[1] = float(item[1])
            if item[1] > 300:
                logging.warning("Find ecg data larger than 300")
                data.remove(item)
    return data


def get_data(data):
    """
        :Synopsis: Split up data into time and ecg
        :param data: The validated data
        :returns: Separate data lists including time and ecg
    """
    time = []
    ecg = []
    for item in data:
        time.append(item[0])
        ecg.append(item[1])
    return [time, ecg]
