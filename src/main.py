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
controller = Controller()

left_motor_front= Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
left_motor_back = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
right_motor_front= Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)
right_motor_back = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)

intake = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)

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
        forward = controller.axis1.position()
        turn = controller.axis3.position()

        left_motor_front.spin(DirectionType.REVERSE, forward + turn, VelocityUnits.PERCENT)
        left_motor_back.spin(DirectionType.REVERSE, forward + turn, VelocityUnits.PERCENT)
        right_motor_front.spin(DirectionType.REVERSE, forward - turn, VelocityUnits.PERCENT)
        right_motor_back.spin(DirectionType.REVERSE, forward - turn, VelocityUnits.PERCENT)

        if controller.buttonR1.pressing():
            intake_speed = 100
        elif controller.buttonR2.pressing():
            intake_speed = -100
        else:
            intake_speed = 0
        intake.spin(DirectionType.FORWARD, intake_speed, VelocityUnits.PERCENT)

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()