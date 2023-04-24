# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 27

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
global y


def distance():
    y = 100
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = 0  # change to time.time()
    StopTime = 0

    # save StartTime
    while y == 0 or GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        y -= 1
        if y == 0:
            print('stuck in loop')
            break

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

        # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


def main():
    x = True
    y = 100
    while x:
        dist = distance()
        print("Measured Distance = %.1f cm" % dist)
        time.sleep(0.08)
        # if y == 0:
        # print('stuck in lop')
        # y = 100


main()