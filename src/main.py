# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       grace.shen                                                   #
# 	Created:      9/15/2025, 8:47:42 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #go
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller = Controller()

left_motor_front= Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
left_motor_back = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
right_motor_front= Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
right_motor_back = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)

left_motors = MotorGroup(left_motor_front, left_motor_back)
right_motors = MotorGroup(right_motor_front, right_motor_back)

intake = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
intake2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)

solenoidA = DigitalOut(brain.three_wire_port.a)

def drive_forward(velocity, wait_time):
    left_motors.spin(REVERSE, velocity, VelocityUnits.PERCENT)
    right_motors.spin(FORWARD, velocity, VelocityUnits.PERCENT)
    wait(wait_time, MSEC)

def turn_left(velocity, wait_time):
    left_motors.spin(FORWARD, velocity, VelocityUnits.PERCENT)
    right_motors.spin(FORWARD, velocity, VelocityUnits.PERCENT)
    wait(wait_time, MSEC)

def turn_right(velocity, wait_time):
    left_motors.spin(REVERSE, velocity, VelocityUnits.PERCENT)
    right_motors.spin(REVERSE, velocity, VelocityUnits.PERCENT)
    wait(wait_time, MSEC)

def drive_reverse(velocity, wait_time):
    left_motors.spin(FORWARD, velocity, VelocityUnits.PERCENT)
    right_motors.spin(REVERSE, velocity, VelocityUnits.PERCENT)
    wait(wait_time, MSEC)

def autonomous_right():
    brain.screen.clear_screen()
    brain.screen.print("autonomous right side code")
    # place automonous code here

    # pneumatics up, go to center balls
    solenoidA.set(False)

    # intake.spin(FORWARD, 100, VelocityUnits.PERCENT)
    # intake2.spin(FORWARD, 100, VelocityUnits.PERCENT)
    drive_forward(65, 1200)

    # turn a little to the left and pick up group of 3
    turn_left(20, 500)

    # put one into the low goal
    drive_forward(10, 300)

    # grab as many as possible from the loader
    drive_reverse(75, 750)

    turn_right(55, 500)

    drive_forward(60, 300)

    turn_right(35, 500)


    # fill the high gaol


    # maybe wait and then push if we do that


def autonomous_left():
    brain.screen.clear_screen()
    brain.screen.print("autonomous left side code")
    # place automonous code here

    # pneumatics up, go to center balls
    solenoidA.set(False)

    drive_forward(65, 1200)

    # turn a little to the right and pick up group of 3
    turn_right(20, 500)

    # put one into the high goal
    drive_forward(10, 300)

    # grab as many as possible from the loader
    drive_reverse(75, 750)

    turn_left(55, 500)

    drive_forward(60, 300)

    turn_left(35, 500)

    # fill the high gaol


    # maybe wait and then push if we do that

def autonomous_skills():
    pass

def user_control():
    global loaderDown
    loaderDown = False

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

        if controller.buttonR2.pressing():
            direction = DirectionType.FORWARD
            intake_speed = 100
            intake2_speed = 100
        elif controller.buttonR1.pressing():
            direction = DirectionType.REVERSE
            intake_speed = 100
            intake2_speed = 100
        else:
            direction = DirectionType.FORWARD
            intake_speed = 0
            intake2_speed = 0
        intake.spin(direction, intake_speed, VelocityUnits.PERCENT)
        intake2.spin(direction, intake2_speed, VelocityUnits.PERCENT)

        if controller.buttonA.pressing():
            loaderDown = not loaderDown
            brain.screen.print("imgonnatweak")
            solenoidA.set(loaderDown)
            while controller.buttonA.pressing():
                wait(10, MSEC)

        wait(20, MSEC)

# create competition instance
# comp = Competition(user_control, autonomous_right)

# actions to do when the program starts
brain.screen.clear_screen()
# autonomous_right()
user_control()