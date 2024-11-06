import math


def calc_bounce(inning):
    # Do some stuff with the inning.
    return -math.sin(inning["OutOfBounceAngle"]*3.141592/180)/math.sin(inning["DropAngle"]*3.141592/180)
