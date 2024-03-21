# Import necessary modules and libraries
from utils.sound import Sound
from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick,EV3UltrasonicSensor,EV3GyroSensor,EV3ColorSensor
import time

# Initialize touch sensors and drum motor
#TS = TouchSensor(1)
US2 = EV3UltrasonicSensor(1)#side US
US = EV3UltrasonicSensor(2)#front US
GS = EV3GyroSensor(3)
#CS = EV3ColorSensor(4)


RIGHT_MOTOR = Motor("A")
LEFT_MOTOR = Motor("B")
RELOAD_MOTOR = Motor("C")
CATAPULT_MOTOR = Motor("D")

## Wait for sensors to be ready
wait_ready_sensors()
print("Done initializing code")


initial_angle = GS.get_abs_measure()
curr_angle = initial_angle


print("US: ",US.get_cm())
print("GS: ",GS.get_abs_measure())
#print("CS: ",CS.get_red())
#print("TS: ",TS.is_pressed())
#print("RELOAD_MOTOR: ",RELOAD_MOTOR.position())
#print("CATAPULT_MOTOR: ",CATAPULT_MOTOR.position())
print("RIGHT_MOTOR: ",RIGHT_MOTOR.get_position())
print("LEFT_MOTOR: ",LEFT_MOTOR.get_position())
def turn_right():
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while abs(curr_angle-initial_angle)!=91:
        RIGHT_MOTOR.set_dps(90)
        LEFT_MOTOR.set_dps(-90)
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        print(curr_angle)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    
    
def turn_left():
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while abs(curr_angle-initial_angle)!=90:
        RIGHT_MOTOR.set_dps(-90)
        LEFT_MOTOR.set_dps(90)
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        print(curr_angle)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    
    
def move_straight_line_till_tunnel(distance,dps):
    P_US=20
    P_GS=20
    initial_distance= US2.get_cm()
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>15:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(curr_distance-initial_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(initial_distance-curr_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        print(curr_angle)
        print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)

def move_straight_line_in_tunnel(distance,dps):
    P_US=20
    P_GS=20
    initial_distance= 7.2
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>15 and US2.get_cm()<12:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(curr_distance-initial_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(initial_distance-curr_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        print(curr_angle)
        print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)

def move_straight_line(distance,dps):
    P_US=20
    P_GS=20
    initial_distance= US2.get_cm()
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>15:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(curr_distance-initial_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(initial_distance-curr_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        print(curr_angle)
        print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)

def tunnel():
    turn_left()
    while US.get_cm()<28:
        RIGHT_MOTOR.set_power(10)
        LEFT_MOTOR.set_power(10)
        time.sleep(0.01)
    RIGHT_MOTOR.set_power(0)
    LEFT_MOTOR.set_power(0)
    turn_right()
    time.sleep(0.1)
    while US.get_cm()>10:
        RIGHT_MOTOR.set_power(-20)
        LEFT_MOTOR.set_power(-20)

def first_adjustment_for_right_tunnel():
    turn_left()
    RIGHT_MOTOR.set_dps(180)
    LEFT_MOTOR.set_dps(180)
    time.sleep(2.5)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    turn_right()
    time.sleep(2)
    
def adjustment_for_left_tunnel():
    turn_left()
    RIGHT_MOTOR.set_dps(-180)
    LEFT_MOTOR.set_dps(-180)
    time.sleep(5)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    turn_right()
    time.sleep(2)

try:
    #z=0
    move_straight_line(2000,-300)
    first_adjustment_for_right_tunnel()
    if (US.get_cm):
        adjustment_for_left_tunnel()
    RIGHT_MOTOR.set_dps(-180)
    LEFT_MOTOR.set_dps(-180)
    time.sleep(5)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    move_straight_line_in_tunnel(5000,-300)
    move_straight_line(5000,-300)
    turn_left()
    move_straight_line(5000,-300)
    #time.sleep()
    
    
        
    #move_staight_line()
    #move_straight_line(1000000,300)
    
    
    
    
    #move_straight_line(5000,-300)
    
    #move_straight_line(50,-300)
    #move_straight_line(5000,300)
    #for i in range(10):
        #turn_right()
        #turn_left()
        
except BaseException as e:  
    print(e)
finally:
    reset_brick()
    print("Resetting brick")
    time.sleep(0.1)
    
