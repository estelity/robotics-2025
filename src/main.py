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
left_motor_back = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_motor_front= Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
right_motor_back = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)

left_motors = MotorGroup(left_motor_front, left_motor_back)
right_motors = MotorGroup(right_motor_front, right_motor_back)

intake = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
intake2 = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)

shoot = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)

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

def intake_in():
    intake.spin(REVERSE, 100, VelocityUnits.PERCENT)
    intake2.spin(REVERSE, 70, VelocityUnits.PERCENT)

def intake_out():
    intake.spin(FORWARD, 35, VelocityUnits.PERCENT)
    intake2.spin(FORWARD, 35, VelocityUnits.PERCENT)
    shoot.spin(FORWARD, 35, VelocityUnits.PERCENT)

def intake_stop():
    intake.stop()
    intake2.stop()

def high_unload():
    intake.spin(REVERSE, 65, VelocityUnits.PERCENT)
    intake2.spin(REVERSE, 65, VelocityUnits.PERCENT)
    shoot.spin(REVERSE, 65, VelocityUnits.PERCENT)

def high_stop():
    intake.stop()
    intake2.stop()
    shoot.stop()

def motors_stop():
    left_motors.stop()
    right_motors.stop()

def autonomous_right():
    brain.screen.clear_screen()
    brain.screen.print("autonomous right side code")
    # place automonous code here

    # pneumatics up, go to center balls and pick up those three
    solenoidA.set(False)

    intake_in()
    drive_forward(65, 650)
    turn_right(20,180)
    drive_forward(25,1750)
    motors_stop()
    wait(1000, MSEC)
    intake_stop()
    
    # put one into the low goal
    drive_reverse(25, 375)
    turn_left(20, 730)
    drive_forward(40, 325)
    motors_stop()
    wait(20, MSEC)
    intake_out()
    wait(2000, MSEC)
    intake_stop()

    # grab as many as possible from the loader
    drive_reverse(75, 965)

    turn_right(55, 500)

    drive_forward(55, 200)

    turn_right(36, 600)

    solenoidA.set(True)

    motors_stop()
    intake_in()
    # drive into loader
    drive_forward(35, 600)
    motors_stop()
    drive_forward(100, 1000)
    motors_stop()
    drive_forward(72, 250)

    motors_stop()
    intake_stop()
    
    # fill the high goal

    drive_reverse(40, 1600)
    motors_stop()
    motors_stop()
    wait(20, MSEC)
    high_unload()
    wait(2000, MSEC)
    high_stop()


def autonomous_left():
    brain.screen.clear_screen()
    brain.screen.print("autonomous left side code")
    # place automonous code here

    # pneumatics up, go to center balls and pick up those three
    solenoidA.set(False)

    intake_in()
    drive_forward(65, 650)
    turn_left(20,180)
    drive_forward(25,1750)
    motors_stop()
    wait(1000, MSEC)
    intake_stop()
    
    # put one into the low goal
    drive_reverse(25, 107)
    turn_left(20, 725)
    drive_reverse(40, 325)
    motors_stop()
    wait(20, MSEC)
    high_unload()
    wait(2000, MSEC)
    high_stop()

    # grab as many as possible from the loader
    drive_forward(75, 965)

    turn_right(55, 500)

    drive_forward(55, 45)

    turn_left(36, 600)

    solenoidA.set(True)

    motors_stop()
    intake_in()
    # drive into loader
    drive_forward(35, 600)
    motors_stop()
    drive_forward(90, 750)
    motors_stop()
    drive_forward(72, 500)

    motors_stop()
    intake_stop()
    
    # fill the high goal

    drive_reverse(40, 1600)
    motors_stop()
    motors_stop()
    wait(20, MSEC)
    high_unload()
    wait(2000, MSEC)
    high_stop()

def autonomous_skills_new():
    drive_reverse(100, 2000)
    motors_stop()


def autonomous_skills():
    brain.screen.clear_screen()
    brain.screen.print("autonomous skills")
    # place automonous code here

    # pneumatics up, go to center balls and pick up those three
    solenoidA.set(False)

    intake_in()
    drive_forward(65, 650)
    turn_right(20,180)
    drive_forward(25,1750)
    motors_stop()
    wait(1000, MSEC)
    intake_stop()
    
    # put one into the low goal
    drive_reverse(25, 375)
    turn_left(20, 725)
    drive_forward(40, 325)
    motors_stop()
    wait(20, MSEC)
    intake_out()
    wait(2000, MSEC)
    intake_stop()

    # grab as many as possible from the loader
    drive_reverse(75, 965)

    turn_right(55, 500)

    drive_forward(55, 170)

    turn_right(36, 600)

    solenoidA.set(True)

    motors_stop()
    intake_in()
    # drive into loader
    drive_forward(35, 600)
    motors_stop()
    drive_forward(90, 1000)
    motors_stop()
    drive_forward(72, 1500)

    motors_stop()
    intake_stop()
    
    # fill the high goal

    drive_reverse(40, 1600)
    motors_stop()
    motors_stop()
    wait(20, MSEC)
    high_unload()
    wait(2000, MSEC)
    high_stop()

    # matchloader pt 2

    drive_forward(35, 800)
    motors_stop()
    intake_in()
    drive_forward(90, 1000)
    motors_stop()
    drive_forward(72, 1500)
    motors_stop()

    drive_reverse(40, 1600)
    motors_stop()
    motors_stop()
    wait(20, MSEC)
    high_unload()
    wait(2000, MSEC)
    high_stop()


    # # go to other match loader
    # drive_forward(30, 750)
    # turn_right(36, 500)
    # drive_forward(100, 2500)
    # turn_left(36, 500)

    # drive into matchloader and unload
    

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

        direction = DirectionType.FORWARD
        direction2 = DirectionType.FORWARD
        shoot_speed = 0
        intake_speed = 0
        intake2_speed = 0

        if controller.buttonL2.pressing():
            direction = DirectionType.FORWARD
            direction2 = DirectionType.FORWARD
            intake_speed = 100
            intake2_speed = 100
            shoot_speed = 100
        elif controller.buttonL1.pressing():
            direction = DirectionType.REVERSE
            direction2 = DirectionType.REVERSE
            shoot_speed = 100
            intake_speed = 100
            intake2_speed = 100
        elif controller.buttonR2.pressing():
            direction2 = DirectionType.FORWARD
            intake_speed = 100
            intake2_speed = 100
        elif controller.buttonR1.pressing():
            direction2 = DirectionType.REVERSE
            intake_speed = 100
            intake2_speed = 85

        intake.spin(direction2, intake_speed, VelocityUnits.PERCENT)
        intake2.spin(direction2, intake2_speed, VelocityUnits.PERCENT)
        shoot.spin(direction, shoot_speed, VelocityUnits.PERCENT)

        if controller.buttonA.pressing():
            loaderDown = not loaderDown
            solenoidA.set(loaderDown)
            while controller.buttonA.pressing():
                wait(10, MSEC)

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous_right)

# actions to do when the program starts
while True:
    wait(100, MSEC)