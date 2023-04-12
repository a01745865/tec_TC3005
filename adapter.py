# Author: Jose Angel Garcia Gomez
# Date: 11-04-2023
# Task: Write an adapter for the Speedometer to make it work
# with the CarDisplay

import random


class MphSpeedometer:
    """We are pretending this is a third-party class we can't change"""

    def __init__(self):
        pass

    def get_speed(self):
        """Returns speed in MPH"""
        speed = random.randint(0, 100)
        print("Speed in MPH: {}".format(speed))
        return speed


class MphToKphSpeedometerAdapter:
    """ TODO: Implement the adapter here.
    It should take in the MphSpeedometer """

    _KPH_MPH_CONVERSION_RATIO = 1.60934

    def __init__(self, speedometer: MphSpeedometer):
        self.speedometer = speedometer

    def get_speed(self):
        """Returns speed in KPH"""
        speed = self.speedometer.get_speed()
        return speed * self._KPH_MPH_CONVERSION_RATIO


class CarDisplay:
    """TODO: change to take in the MphtoKphSpeedometerAdapter instead
    of the Speedometer"""

    def __init__(self, speedometer: MphToKphSpeedometerAdapter):
        self.speedometer = speedometer

    def show_speed(self):
        speed = self.speedometer.get_speed()
        print(f'Speed: {speed}')


if __name__ == '__main__':
    """TODO: change as needed for your new adapter"""
    mph_speedometer = MphSpeedometer()
    adapter = MphToKphSpeedometerAdapter(mph_speedometer)
    car_display = CarDisplay(adapter)
    car_display.show_speed()
