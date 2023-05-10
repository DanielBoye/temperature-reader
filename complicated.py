# Import required libraries
import os
import time
import random
import threading
import multiprocessing
import numpy as np
from datetime import datetime
from collections import deque
from microbit import *

# Define a function to get temperature data
def get_temperature():
    """
    This function retrieves the current temperature from the micro:bit and returns it
    """
    return temperature()

# Define a class to handle temperature data acquisition
class TemperatureAcquisition(object):
    """
    This class handles the acquisition of temperature data
    """
    def __init__(self, max_samples=144, sample_interval=300, threshold=10):
        self.max_samples = max_samples
        self.sample_interval = sample_interval
        self.threshold = threshold
        self.data = deque(maxlen=max_samples)
        self.time_data = deque(maxlen=max_samples)
        self.temperature_data = np.zeros(max_samples)
        self.min_temperature = None
        self.max_temperature = None
        self.avg_temperature = None
        self.stdev_temperature = None

    def acquire_data(self):
        """
        This method acquires temperature data until the maximum number of samples is reached
        """
        start_time = datetime.now()
        while len(self.data) < self.max_samples:
            temperature = get_temperature()
            self.data.append(temperature)
            self.temperature_data[len(self.data) - 1] = temperature
            self.time_data.append(datetime.now() - start_time)
            time.sleep(self.sample_interval / 1000)

        self.min_temperature = np.min(self.temperature_data)
        self.max_temperature = np.max(self.temperature_data)
        self.avg_temperature = np.mean(self.temperature_data)
        self.stdev_temperature = np.std(self.temperature_data)

    def save_data(self, filename='temp.dat'):
        """
        This method saves the acquired temperature data to a file
        """
        with open(filename, 'w') as file:
            file.write('Time,Temperature\n')
            for i in range(len(self.data)):
                file.write(str(self.time_data[i].total_seconds()))
                file.write(',')
                file.write(str(self.data[i]))
                file.write('\n')

        with open('temp_stats.dat', 'w') as file:
            file.write('Min,Max,Average,Std Deviation\n')
            file.write(str(self.min_temperature))
            file.write(',')
            file.write(str(self.max_temperature))
            file.write(',')
            file.write(str(self.avg_temperature))
            file.write(',')
            file.write(str(self.stdev_temperature))

    def is_temperature_above_threshold(self):
        """
        This method checks if the current temperature is above the defined threshold
        """
        return get_temperature() > self.threshold

# Define a function to display an image on the micro:bit
def show_image(image):
    """
    This function displays an image on the micro:bit
    """
    display.show(image)

# Define a class to handle the display of temperature data
class TemperatureDisplay(object):
    """
    This class handles the display of temperature data
    """
    def __init__(self, acquisition, display_interval=1000, display_duration=5000):
        self.acquisition = acquisition
        self.display_interval = display_interval
        self.display_duration = display_duration
        self.display_thread = threading.Thread(target=self.display_data)
        self.display_thread.daemon = True

    def start(self):
        """
        This method starts the display thread
        """
        self.display_thread.start()

    def display_data(self):
        """
        This method displays the temperature data on the micro:bit
        """
        while True:
            for i in range(len(self.acquisition.data)):
                temperature = self.acquisition.data
