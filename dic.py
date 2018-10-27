from peakfinder import peak_finder


def get_dictionary(time, ecg):
    metrics = {}
    peaks_index = peak_finder(ecg)
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
