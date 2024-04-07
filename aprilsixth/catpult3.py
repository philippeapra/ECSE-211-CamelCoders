from utils.sound import Sound
from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick,EV3UltrasonicSensor,EV3GyroSensor,EV3ColorSensor
import time


# Intialize global variables and sensors
INITIAL_POSITION = 15
CATAPULT_MOTOR = Motor("C")
POWER_RELOAD=5
POWER_INITIAL=15
RELOAD_POSITION=-5

## Wait for sensors to be ready
wait_ready_sensors()
print("Done initializing code")

def firstbucket():
    LAUNCH_POSITION=50
    POWER_LAUNCH=30
    KD_LAUNCH=60
    return LAUNCH_POSITION, POWER_LAUNCH, KD_LAUNCH
    
def lastbucket():
    LAUNCH_POSITION=95
    POWER_LAUNCH=100
    KD_LAUNCH=50
    return LAUNCH_POSITION, POWER_LAUNCH, KD_LAUNCH
    
def middlebucket():
    LAUNCH_POSITION=60
    POWER_LAUNCH=70
    KD_LAUNCH=70
    return LAUNCH_POSITION, POWER_LAUNCH, KD_LAUNCH

def launch(LAUNCH_POSITION, POWER_LAUNCH, KD_LAUNCH):
    CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
    CATAPULT_MOTOR.set_position(15)
    time.sleep(1)
    
    CATAPULT_MOTOR.set_position_kp(POWER_LAUNCH)
    CATAPULT_MOTOR.set_position_kd(KD_LAUNCH)
    
    CATAPULT_MOTOR.set_position(LAUNCH_POSITION)
    CATAPULT_MOTOR.set_position_relative(LAUNCH_POSITION)
    time.sleep(1.5)
    
    CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
    CATAPULT_MOTOR.set_position(45)
    time.sleep(1)


def reload():
    CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
    CATAPULT_MOTOR.set_position(15)
    time.sleep(1.5)
    CATAPULT_MOTOR.set_position_kp(POWER_RELOAD)
    CATAPULT_MOTOR.set_position(RELOAD_POSITION)
    time.sleep(1.5)
    CATAPULT_MOTOR.set_position_kp(POWER_RELOAD)
    CATAPULT_MOTOR.set_position(15)

#CATAPULT_MOTOR.set_position_kp(POWER_LAUNCH)
for i in range (10):
    reload()
    CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
    CATAPULT_MOTOR.set_position(INITIAL_POSITION)
    time.sleep(1.5)
    if 0 <= i <= 7:
        launch(*lastbucket())
    elif i == 8:
        launch(*middlebucket())
    elif i == 9:
        launch(*firstbucket())
    
    
    
CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
CATAPULT_MOTOR.set_position(INITIAL_POSITION)


