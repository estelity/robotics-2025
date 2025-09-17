# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       grace.shen                                                   #
# 	Created:      9/15/2025, 8:47:42 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)

controller = Controller()

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        # arcade drive
        forward = controller.axis3.position()
        turn = controller.axis1.position()
        left_motor.spin(DirectionType.FORWARD, forward + turn, VelocityUnits.PERCENT)
        right_motor.spin(DirectionType.FORWARD, forward - turn, VelocityUnits.PERCENT)

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()