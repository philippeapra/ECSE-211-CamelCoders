
# Import necessary modules and libraries
from utils.sound import Sound
from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick
import time

# Initialize touch sensors and drum motor
TS1 = TouchSensor(1)
TS2 = TouchSensor(2)
TS3 = TouchSensor(3)

DRUM_SENSOR = TouchSensor(4)
DRUM_MOTOR= Motor("B")

## Wait for sensors to be ready
wait_ready_sensors()
print("Done initializing code")

# Initialize tone sounds
tone1 = Sound(duration=3, volume=90, pitch="C5")
tone2 = Sound(duration=3, volume=90, pitch="G5")
tone3 = Sound(duration=3, volume=90, pitch="A5")
tone4 = Sound(duration=3, volume=90, pitch="F5")
tone5 = Sound(duration=3, volume=90, pitch="E5")
tone6 = Sound(duration=3, volume=90, pitch="D5")
print("Done initializing sounds")

def stop_all_sound():
    tone1.stop()
    tone2.stop()
    tone3.stop()
    tone4.stop()
    tone5.stop()
    tone6.stop()

def update_pressed_str():
        pressed = ""
        if TS1.is_pressed():
            pressed+="1"
        else:
            pressed+="0"

        if TS2.is_pressed():
            pressed+="1"
        else:
            pressed+="0"

        if TS3.is_pressed():
            pressed+="1"
        else:
            pressed+="0"

        if DRUM_SENSOR.is_pressed():
            pressed+="1"
        else:
            pressed+="0"

try:
    
    print("Starting main loop")
    DRUM_STARTED = False
    pressed = ""   #string expressing which btns are pressed in this iteration
    
    
    while True:

        pressed = update_pressed_str()

        # Emergency stop mechanism
        if pressed=="1111":
            break

        # Drumming mechanism
        if DRUM_SENSOR.is_pressed() and not DRUM_STARTED:
            DRUM_MOTOR.set_power(100)
            DRUM_STARTED = True
            time.sleep(0.1)
        # Flute mechanism
        elif pressed=="1000":
            stop_all_sound()
            tone1.play()
        elif pressed=="0100":
            stop_all_sound()
            tone2.play()
        elif pressed=="0010":
            stop_all_sound()
            tone3.play()
        elif pressed=="1100":
            stop_all_sound()
            tone4.play()
        elif pressed=="0110":
            stop_all_sound()
            tone5.play()
        elif pressed=="1010":
            stop_all_sound()
            tone6.play()
        elif pressed=="0000":
            stop_all_sound()

# capture all exceptions
except BaseException as e:  
    print(e)
finally:
    print("Exiting/Reseting program")
    reset_brick()
    exit()
