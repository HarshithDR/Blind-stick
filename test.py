# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER1 = 2
GPIO_ECHO1 = 3
GPIO_VIB1 = 4
GPIO_TRIGGER2 = 17
GPIO_ECHO2 = 27
GPIO_VIB2 = 22
GPIO_TRIGGER3 = 5
GPIO_ECHO3 = 6
GPIO_VIB3 = 13
GPIO_TRIGGER4 = 18
GPIO_ECHO4 = 23

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
GPIO.setup(GPIO_TRIGGER4, GPIO.OUT)
GPIO.setup(GPIO_ECHO4, GPIO.IN)
GPIO.setup(GPIO_VIB1, GPIO.OUT)
GPIO.setup(GPIO_VIB2, GPIO.OUT)
GPIO.setup(GPIO_VIB3, GPIO.OUT)

global y

def distance1():
    y = 100
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)

    StartTime = 0  # change to time.time()
    StopTime = 0

    # save StartTime
    while y == 0 or GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
        y -= 1
        if y == 0:
            print('stuck in loop')
            return 'a'

    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()


    TimeElapsed = StopTime - StartTime
    distance1 = (TimeElapsed * 34300) / 2
    print("Measured Distance = %.1f cm" % distance1)
    return 'x'


def distance2():
    y = 100
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)

    StartTime = 0  # change to time.time()
    StopTime = 0

    # save StartTime
    while y == 0 or GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
        y -= 1
        if y == 0:
            print('stuck in loop')
            return 'b'

    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance2 = (TimeElapsed * 34300) / 2
    print("Measured Distance = %.1f cm" % distance2)
    return 'x'


def distance3():
    y = 100
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER3, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER3, False)

    StartTime = 0  # change to time.time()
    StopTime = 0

    # save StartTime
    while y == 0 or GPIO.input(GPIO_ECHO3) == 0:
        StartTime = time.time()
        y -= 1
        if y == 0:
            print('stuck in loop')
            return 'c'

    # save time of arrival
    while GPIO.input(GPIO_ECHO3) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance3 = (TimeElapsed * 34300) / 2
    print("Measured Distance = %.1f cm" % distance3)
    return 'x'


def distance4():
    y = 100
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER4, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER4, False)

    StartTime = 0  # change to time.time()
    StopTime = 0

    # save StartTime
    while y == 0 or GPIO.input(GPIO_ECHO4) == 0:
        StartTime = time.time()
        y -= 1
        if y == 0:
            print('stuck in loop')
            return 'd'

    # save time of arrival
    while GPIO.input(GPIO_ECHO4) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance4 = (TimeElapsed * 34300) / 2
    print("Measured Distance = %.1f cm" % distance4)
    return 'x'


if _name_ == '_main_':
    x = True
    y = 100

    # while x:
    #     dist1 = distance()
    #     print("Measured Distance = %.1f cm" % dist1)
    #     time.sleep(0.08)
    #     # if y == 0:
    #     # print('stuck in loop')
    #     # y = 100

    failure = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'x': 0}
    while True:
        sen1 = distance1()
        sen2 = distance2()
        sen3 = distance3()
        sen4 = distance4()

        failure[sen1] = failure[sen1] + 1
        failure[sen2] = failure[sen2] + 1
        failure[sen3] = failure[sen3] + 1
        failure[sen4] = failure[sen4] + 1


        if failure['a'] == 10:
            print('Attention needed : sensor1 not working properly ')
            failure['a'] = 0

        if failure['b'] == 10:
            print('Attention needed : sensor2 not working properly ')
            failure['b'] = 0

        if failure['c'] == 10:
            print('Attention needed : sensor3 not working properly ')
            failure['c'] = 0

        if failure['d'] == 10:
            print('Attention needed : sensor4 not working properly ')
            failure['d'] = 0

        if failure['x'] == 10:
            failure['x'] = 0
