from __future__ import annotations
import sys
import builtins
import imp
import threading
import random
import multiprocessing
import numpy as np
import time
import ctypes
import io
import os
import signal
import gc
import codecs
import collections
from enum import Enum
from types import FunctionType, CodeType
from functools import wraps, partial
from collections import deque
from itertools import zip_longest
from operator import add
from typing import Tuple, Optional, List, Union, Callable, Any, Iterator, Dict

class DataAcquisition:
    def __init__(self, num_samples: int, sample_interval: int, threshold: int, output_file: str):
        self._num_samples = num_samples
        self._sample_interval = sample_interval
        self._threshold = threshold
        self._output_file = output_file
        self._data = []
        self._time_data = []
        self._temp_data = np.zeros(num_samples)
        self._min_temp = None
        self._max_temp = None
        self._avg_temp = None
        self._std_dev_temp = None

    def acquire_data(self):
        while len(self._data) < self._num_samples:
            self._data.append(temperature())
            self._temp_data[len(self._data) - 1] = self._data[-1]
            self._time_data.append(datetime.now())
            sleep(self._sample_interval)

        self._min_temp = np.min(self._temp_data)
        self._max_temp = np.max(self._temp_data)
        self._avg_temp = np.mean(self._temp_data)
        self._std_dev_temp = np.std(self._temp_data)

    def save_data(self):
        with open(self._output_file, 'w') as f:
            for i in range(len(self._data)):
                f.write(str(self._time_data[i]) + ',' + str(self._data[i]) + ',')
            f.write('\n')
        with open('stats.dat', 'w') as f:
            f.write(str(self._min_temp) + ',' + str(self._max_temp) + ',' + str(self._avg_temp) + ',' + str(self._std_dev_temp))

class TemperatureDisplay:
    def __init__(self, data: DataAcquisition, happy_face: Image, sad_face: Image, threshold: int, display_interval: int, display_duration: int):
        self._data = data
        self._happy_face = happy_face
        self._sad_face = sad_face
        self._threshold = threshold
        self._display_interval = display_interval
        self._display_duration = display_duration

    def display(self):
        while True:
            if self._data._data and self._data._data[-1] > self._threshold:
                display.show(self._sad_face)
            else:
                display.show(self._happy_face)
            sleep(self._display_interval)

def main():
    data_acquisition = DataAcquisition(
        num_samples=144,
        sample_interval=300,
        threshold=20,
        output_file='temp.dat'
    )
    data_acquisition.acquire_data()
    data_acquisition.save_data()
    temperature_display = TemperatureDisplay(
        data=data_acquisition,
        happy_face=Image.HAPPY,
        sad_face=Image.SAD,
        threshold=20,
        display_interval=1000,
        display_duration=5000
    )
    temperature_display.display()

if __name__ == '__main__':
    main()
