
# Import necessary modules and libraries
from utils.sound import Sound
from utils.brick import TouchSensor, Motor, wait_ready_sensors, reset_brick,EV3UltrasonicSensor,EV3GyroSensor,EV3ColorSensor
import time

# Initialize touch sensors and drum motor
#TS = TouchSensor(1)

DISTANCE_FROM_WALL_BACK=5

US2 = EV3UltrasonicSensor(1)#side US
US = EV3UltrasonicSensor(2)#front US

#turning right increases angle
#turning left decreases angle
GS = EV3GyroSensor(4)
CS = EV3ColorSensor(3)


RIGHT_MOTOR = Motor("A")
LEFT_MOTOR = Motor("B")
RELOAD_MOTOR = Motor("C")
CATAPULT_MOTOR = Motor("D")

## Wait for sensors to be ready
wait_ready_sensors()
print("Done initializing code")


initial_angle = GS.get_abs_measure()
curr_angle = initial_angle


#print("US2 (side): ",US2.get_cm())

#print("GS: ",GS.get_abs_measure())
#while True:
#print("US: (front)",US.get_cm())
#while True:
#print("CS: ",CS.get_rgb())
#print("TS: ",TS.is_pressed())
#print("RELOAD_MOTOR: ",RELOAD_MOTOR.position())
#print("CATAPULT_MOTOR: ",CATAPULT_MOTOR.position())
#print("RIGHT_MOTOR: ",RIGHT_MOTOR.get_position())
#print("LEFT_MOTOR: ",LEFT_MOTOR.get_position())

def turn_right(target):
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    RIGHT_MOTOR.set_dps(180)
    LEFT_MOTOR.set_dps(-180)
    while (curr_angle%360)!=target%360:
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        print(curr_angle)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    
    
def turn_left(target):
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    RIGHT_MOTOR.set_dps(-180)
    LEFT_MOTOR.set_dps(180)
    while (curr_angle%360)!=target%360:
        time.sleep(0.01)
        curr_angle=GS.get_abs_measure()
        print(curr_angle)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    
    
def move_straight_line_distance_from_wall(distance,dps,from_wall):
    P_US=30
    P_GS=30
    initial_distance= from_wall
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>15:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(curr_distance-initial_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(initial_distance-curr_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        print(curr_angle)
        print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)

def move_straight_line_in_tunnel(distance,dps):
    P_US=30
    P_GS=30
    initial_distance= 7.2
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>15 and US2.get_cm()<12:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(initial_distance-curr_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(curr_distance-initial_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        #print(curr_angle)
        #print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    
    
def move_straight_line_back_line(distance,dps):
    P_US=30
    P_GS=30
    initial_distance= 9.5
    curr_distance = 9
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>11 and CS.get_rgb()[2]>90 and CS.get_rgb()[0]<115:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(initial_distance-curr_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(curr_distance-initial_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        #print(curr_angle)
        #print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    
def move_straight_line_back(distance,dps):
    P_US=30
    P_GS=30
    initial_distance= DISTANCE_FROM_WALL_BACK
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>4:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(initial_distance-curr_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(curr_distance-initial_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        #print(curr_angle)
        #print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)

def move_straight_line(distance,dps):
    P_US=30
    P_GS=30
    initial_distance= US2.get_cm()
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>11:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle))
        left = (dps+P_GS*(curr_angle-initial_angle))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        #print(curr_angle)
        #print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)

def move_straight_line_till_line(distance,dps):
    P_US=30
    P_GS=30
    initial_distance= US2.get_cm()
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()>11:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle)+P_US*(curr_distance-initial_distance))
        left = (dps+P_GS*(curr_angle-initial_angle)+P_US*(initial_distance-curr_distance))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        #print(curr_angle)
        #print(curr_distance)
    move_straight_line(1100,-300)

def move_final(distance,dps):
    P_US=30
    P_GS=30
    initial_distance= US2.get_cm()
    curr_distance = initial_distance
    initial_angle=GS.get_abs_measure()
    curr_angle=initial_angle
    while distance>0 and US.get_cm()<1:
        # minus moves forward
        right = (dps+P_GS*(initial_angle-curr_angle))
        left = (dps+P_GS*(curr_angle-initial_angle))
        RIGHT_MOTOR.set_dps(right)
        LEFT_MOTOR.set_dps(left)
        time.sleep(0.001)
        curr_angle=GS.get_abs_measure()
        curr_distance=US2.get_cm()
        distance-=1
        print(curr_angle)
        print(curr_distance)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)


def first_adjustment_for_right_tunnel():
    turn_left(-90)
    RIGHT_MOTOR.set_dps(180)
    LEFT_MOTOR.set_dps(180)
    time.sleep(2.2)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    turn_right(0)
    time.sleep(2)
    
def adjustment_for_left_tunnel():
    turn_left(-90)
    RIGHT_MOTOR.set_dps(-180)
    LEFT_MOTOR.set_dps(-180)
    time.sleep(5)
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    turn_right(0)
    time.sleep(2)

try:
    z=0
    
    move_straight_line(20000,-750)
    
    first_adjustment_for_right_tunnel()
    if (US.get_cm()<15):
        adjustment_for_left_tunnel()
        DISTANCE_FROM_WALL_BACK=37.2
    move_straight_line(500,-750)
    move_straight_line_in_tunnel(50000,-750)
    move_straight_line(50000,-750)
    turn_left(-90)
    move_straight_line(50000,-750)
    turn_right(90)
    move_straight_line_back(70000,-750)
    turn_right(180)
    move_straight_line(500,-750)
    move_straight_line_in_tunnel(50000,-750)
    move_straight_line_back_line(5000,-300)
    
    turn_left(-270)
    
    
except BaseException as e:  
    print(e)
finally:
    RIGHT_MOTOR.set_dps(0)
    LEFT_MOTOR.set_dps(0)
    reset_brick()
    print("Resetting brick")
    time.sleep(0.1)