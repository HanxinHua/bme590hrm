from peakfinder import peak_finder
import sys
import logging


def get_dictionary(time, ecg):
    """
        :Synopsis: Calculate the information we want and store them
                in a dictionary
        :param time: The time data
        :param ecg: The ecg data corresponding to time
        :returns: A dictionary including the key information we want
        :raise: Time duration is zero!
    """
    metrics = {}
    try:
        logging.info("Try to find peaks")
        peaks_index = peak_finder(ecg)
    except ZeroDivisionError:
        logging.error("Time duration is zero!")
        logging.error("Process exit\n\n")
        sys.exit(1)
    dur = time[len(time)-1]-time[0]
    metrics["mean_hr_bpm"] = len(peaks_index)/dur*60
    metrics["voltage_extremes"] = (max(ecg), min(ecg))
    metrics["duration"] = dur
    metrics["num_beats"] = len(peaks_index)
    bt = []
    for i in peaks_index:
        bt.append(time[i])
    metrics["beats"] = bt
    return metrics
