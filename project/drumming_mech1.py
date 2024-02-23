
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
tone1 = Sound(duration=3, volume=80, pitch="C5")
tone2 = Sound(duration=3, volume=80, pitch="G5")
tone3 = Sound(duration=3, volume=80, pitch="A5")
tone4 = Sound(duration=3, volume=80, pitch="F5")
tone5 = Sound(duration=3, volume=80, pitch="E5")
tone6 = Sound(duration=3, volume=80, pitch="D5")
print("Done initializing sounds")

def stop_all_sound():
    tone1.stop()
    tone2.stop()
    tone3.stop()
    tone4.stop()
    tone5.stop()
    tone6.stop()


try:
    
    print("Starting main loop")
    DRUM_STARTED = False
    while True:

        # Emergency stop mechanism
        if TS1.is_pressed() and TS2.is_pressed() and TS3.is_pressed():
            break

        # Drumming mechanism
        if DRUM_SENSOR.is_pressed() and not DRUM_STARTED:
            DRUM_MOTOR.set_power(100)
            DRUM_STARTED = True
            time.sleep(0.25)
        if DRUM_SENSOR.is_pressed() and DRUM_STARTED:
            DRUM_MOTOR.set_power(0)
            DRUM_STARTED = False
            time.sleep(0.25)

        # Flute mechanism
        if TS1.is_pressed() and not TS2.is_pressed() and not TS3.is_pressed() and not tone1.is_playing():
            stop_all_sound()
            tone1.play()
        elif not TS1.is_pressed() and  TS2.is_pressed() and not TS3.is_pressed() and not tone2.is_playing():
            stop_all_sound()
            tone2.play()
        elif not TS1.is_pressed() and not TS2.is_pressed() and TS3.is_pressed() and not tone3.is_playing():
            stop_all_sound()
            tone3.play()
        elif TS1.is_pressed() and TS2.is_pressed() and not TS3.is_pressed() and not tone4.is_playing():
            stop_all_sound()
            tone4.play()
        elif not TS1.is_pressed() and  TS2.is_pressed() and TS3.is_pressed() and not tone5.is_playing():
            stop_all_sound()
            tone5.play()
        elif TS1.is_pressed() and  not TS2.is_pressed() and TS3.is_pressed() and not tone6.is_playing():
            stop_all_sound()
            tone6.play()
        elif not TS1.is_pressed() and not TS2.is_pressed() and not TS3.is_pressed():
            stop_all_sound()

# capture all exceptions
except BaseException as e:  
    print(e)
finally:
    print("Exiting/Reseting program")
    reset_brick()
    exit()
