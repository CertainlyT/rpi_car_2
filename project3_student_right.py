######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import getDistance() method in the ultraModule
# =======================================================================
from ultraModule import getDistance

# =======================================================================
# import TurnModule() method
# =======================================================================
from TurnModule import *


# =======================================================================
# rightPointTurn() and leftPointTurn() in TurnModule module
# =======================================================================
# student assignment (1)
# student assignment (2)



# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis = 20  # distance standard value

# when obstacle=1, the power and
# running time of the first turn
PointPr = 80  # speed of point turn
PointTr = 0.45  # duration of point turn
SwingPr = 80  # speed of swing turn
SwingTr = 0.85  # duration of swing turn
obstacle = 1  # a number of obstacles

try:
    distance = getDistance()
    while True:
        distance = getDistance()
        # ultra sensor replies the distance back
        print('distance= ', distance)
        # If vehicle pass 2 obstalces, it will drive 1 more second and stop.
        if obstacle == 3:
            go_forward(70, 1)
            pwm_low()
            break
        # when the distance is above the dis, moving object forwards
        elif (distance > dis):
            go_forward_any(70)
            # stop and wait 1 second
            stop()
            sleep(1)
            # select type of turn
            if obstacle == 1:
                rightSwingTurn(SwingPr, SwingTr)
                obstacle += 1
            else:
                rightPointTurn(PointPr, PointTr)
                obstacle += 1
            # after turning, stop and wait 0.3 second
            stop()
            sleep(0.3)



# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
