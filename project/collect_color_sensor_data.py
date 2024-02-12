#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor,wait_ready_sensors, reset_brick
import csv

COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(4)
TOUCH_SENSOR = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    curr_pressed = False
    counter=0
    try:
        output_file = open(COLOR_SENSOR_DATA_FILE, "w")
        writer = csv.writer(output_file) #imported csv library to remove the square brackets around each value
        
        while True:
            if counter == 10 :
                break
            if (not TOUCH_SENSOR.is_pressed()): #prevents the sensor from reading continuously at each touch sensor press, resets bool to false
                curr_pressed = False
                
            elif TOUCH_SENSOR.is_pressed() and curr_pressed == False :
                curr_pressed = True
                color_data = COLOR_SENSOR.get_rgb()
                if color_data is not None: # If None is given, then data collection failed that time
                    #output_file.write(f"{color_data[0],color_data[1];color_data[2]}\n")
                    writer.writerow(color_data)
                    counter = counter + 1
                    
                    
                    
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("Done collecting color data samples")
        output_file.close()
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
