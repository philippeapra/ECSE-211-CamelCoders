from utils.sound import Sound
from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick,EV3UltrasonicSensor,EV3GyroSensor,EV3ColorSensor
import time

#Bucket 3

INITIAL_POSITION = 15
CATAPULT_MOTOR = Motor("C")
RELOAD_POSITION=-5
LAUNCH_POSITION=95#145
POWER_LAUNCH=100#200
POWER_RELOAD=5
POWER_INITIAL=15
KD_LAUNCH=50

#Bucket 2
#INITIAL_POSITION = 15
CATAPULT_MOTOR = Motor("C")
'''RELOAD_POSITION=0
LAUNCH_POSITION=60#145
POWER_LAUNCH=70#200
POWER_RELOAD=20
POWER_INITIAL=15
KD_LAUNCH=70'''

## Wait for sensors to be ready
wait_ready_sensors()
print("Done initializing code")

def firstbucket():
    INITIAL_POSITION = 15
    CATAPULT_MOTOR = Motor("C")
    RELOAD_POSITION=0
    LAUNCH_POSITION=50#145
    POWER_LAUNCH=50#200
    POWER_RELOAD=20
    POWER_INITIAL=15
    KD_LAUNCH=70
    
def lastbucket():
    INITIAL_POSITION = 15
    CATAPULT_MOTOR = Motor("C")
    RELOAD_POSITION=-5
    LAUNCH_POSITION=95#145
    POWER_LAUNCH=100#200
    POWER_RELOAD=20
    POWER_INITIAL=15
    KD_LAUNCH=50
    
def middlebucket():
    INITIAL_POSITION = 15
    CATAPULT_MOTOR = Motor("C")
    RELOAD_POSITION=0
    LAUNCH_POSITION=60#145
    POWER_LAUNCH=70#200
    POWER_RELOAD=20
    POWER_INITIAL=15
    KD_LAUNCH=70


def launch():
    #CATAPULT_MOTOR.set_limits(0,0)
    #CATAPULT_MOTOR.set_limits(0,0)
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
#     CATAPULT_MOTOR.set_dps(300)
#     time.sleep(1)
#     CATAPULT_MOTOR.set_dps(0)
#     time.sleep(5)

def reload():
    CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
    CATAPULT_MOTOR.set_position(15)
    time.sleep(1.5)
    CATAPULT_MOTOR.set_position_kp(POWER_RELOAD)
    CATAPULT_MOTOR.set_position(RELOAD_POSITION)
    time.sleep(1.5)
    CATAPULT_MOTOR.set_position_kp(POWER_RELOAD)
    CATAPULT_MOTOR.set_position(15)

CATAPULT_MOTOR.set_position_kp(POWER_LAUNCH)
for i in range (10):
    reload()
    CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
    CATAPULT_MOTOR.set_position(INITIAL_POSITION)
    time.sleep(1.5)
    firstbucket()
    launch()

    
    #CATAPULT_MOTOR.set_position_kd(70)
    
CATAPULT_MOTOR.set_position_kp(POWER_INITIAL)
CATAPULT_MOTOR.set_position(INITIAL_POSITION)
#CATAPULT_MOTOR.float_motor()


#while True:
    
    #print(CATAPULT_MOTOR.get_encoder())

