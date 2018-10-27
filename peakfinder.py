import numpy as np
import peakutils


def peak_finder(data):
    """
        :param data: The ecg data
        :returns: The indexes of peaks in the ecg data
    """
    ecg = peakutils.indexes(np.array(data), thres=0.02/max(data), min_dist=200)
    return ecg
