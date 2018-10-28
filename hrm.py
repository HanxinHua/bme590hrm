from readCSV import *
from write_info import write_info
from dic import get_dictionary
import os
import sys
import logging


def hrm():
    """
        :Synopsis: Transform data in all input files to output files
                   with information we want
        :raise: Input files are not in 'test_data'
                Input files are not .csv files
    """
    dir_path = 'test_data'
    out_path = 'results'
    if not os.path.isdir(out_path):
        logging.info("Create dir 'results'")
        os.mkdir(out_path)
    try:
        for f in os.listdir(dir_path):
            if f.endswith('.csv'):
                path = dir_path+"/"+f
                logging.info("Read input : "+path)
                data = read_csv(path)
                logging.info("Validate data")
                v_data = validation(data)
                logging.info("Get time and ecg")
                time, ecg = get_data(v_data)
                logging.info("Get metrics")
                metrics = get_dictionary(time, ecg)
                logging.info("Write metrics to output file : " +
                             out_path+"/"+f[:-4])
                write_info(out_path+"/"+f[:-4], metrics)
    except FileNotFoundError:
        logging.error("The system cannot find the path specified: 'test_data'")
        logging.info("Process exit\n\n")
        sys.exit(1)
    if not os.listdir(out_path):
        logging.info("No .csv file in 'test_data'")


if __name__ == "__main__":
    logging.basicConfig(filename='HeartRateMonitor.log', level=logging.INFO)
    logging.info("New process")
    hrm()
