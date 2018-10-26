from peakfinder import *
import numpy as np


def getdictionary(time, ecg):
    metrics = {}
    peaks_index = peakfinder(ecg)
    dur = time[len(time)-1]-time[0]
    metrics["mean_hr_bpm"] = len(peaks_index)/dur*60
    metrics["voltage_extremes"] = (max(ecg), min(ecg))
    metrics["duration"] = dur
    metrics["num_beats"] = len(peaks_index)
    bt = []
    for i in peaks_index:
        bt.append(time[i])
    beats_time = np.array(bt)
    metrics["beats"] = beats_time
    return metrics