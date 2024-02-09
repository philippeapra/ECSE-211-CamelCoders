#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor,wait_ready_sensors, reset_brick


COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(3)
TOUCH_SENSOR = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    not_pressed = TOUCH_SENSOR.get_status
    curr_pressed = False
    try:
        output_file = open(COLOR_SENSOR_DATA_FILE, "w")
        while True:
            if not TOUCH_SENSOR.is_pressed():
                curr_pressed = False
            elif TOUCH_SENSOR.is_pressed() and curr_pressed==False :
                curr_pressed = True
                color_data = COLOR_SENSOR.get_rgb()
                if color_data is not None: # If None is given, then data collection failed that time
                    print("Touch sensor pressed")
                    print(color_data)
                    output_file.write(f"{color_data}\n")
                    
                    
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("Done collecting US distance samples")
        output_file.close()
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
