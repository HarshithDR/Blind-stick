import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER1 = 2
GPIO_ECHO1 = 3
GPIO_VIB1 = 2

GPIO_TRIGGER2 = 5
GPIO_ECHO2 = 6
GPIO_VIB2 = 8

GPIO_TRIGGER3 = 11
GPIO_ECHO3 = 12
GPIO_VIB3 = 13

GPIO_TRIGGER4 = 17
GPIO_ECHO4 = 19
GPIO_VIB4 = 22

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_VIB1, GPIO.OUT)

GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(GPIO_VIB2, GPIO.OUT)


GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
GPIO.setup(GPIO_VIB3, GPIO.OUT)


GPIO.setup(GPIO_TRIGGER4, GPIO.OUT)
GPIO.setup(GPIO_ECHO4, GPIO.IN)
GPIO.setup(GPIO_VIB4, GPIO.OUT)


def distance1():
    # set Trigger to HIGH
    CountTime = time.time()
    CountTime1 = CountTime+0.0035

    GPIO.output(GPIO_TRIGGER1, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)

    # StartTime = time.time()
    # StopTime = time.time()

    # save StartTime

    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()

    # save time of arrival
    while True:
        if time.time() == CountTime1:
            print("Sensor1 is not working")
            break
        while GPIO.input(GPIO_ECHO1) == 1:
            StopTime = time.time()


    # time difference between start and arrival

    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2
    return distance


def distance2():
    # set Trigger to HIGH
    CountTime = time.time()
    CountTime1 = CountTime + 0.0035

    GPIO.output(GPIO_TRIGGER2, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)

    # StartTime = time.time()
    # StopTime = time.time()

    # save StartTime

    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()

    # save time of arrival
    while True:
        if time.time() == CountTime1:
            print("Sensor2 is not working")
            break
        while GPIO.input(GPIO_ECHO2) == 1:
            StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance


def distance3():
    # set Trigger to HIGH
    CountTime = time.time()
    CountTime1 = CountTime + 0.0035

    GPIO.output(GPIO_TRIGGER3, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER3, False)

    # StartTime = time.time()
    # StopTime = time.time()

    # save StartTime

    while GPIO.input(GPIO_ECHO3) == 0:
        StartTime = time.time()

    # save time of arrival
    while True:
        if time.time() == CountTime1:
            print("Sensor3 is not working")
            break
        while GPIO.input(GPIO_ECHO3) == 1:
            StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance


def distance4():
    # set Trigger to HIGH
    CountTime = time.time()
    CountTime1 = CountTime + 0.0035

    GPIO.output(GPIO_TRIGGER4, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER4, False)

    # StartTime = time.time()
    # StopTime = time.time()

    # save StartTime

    while GPIO.input(GPIO_ECHO4) == 0:
        StartTime = time.time()

    # save time of arrival
    while True:
        if time.time() == CountTime1:
            print("Sensor1 is not working")
            break
        while GPIO.input(GPIO_ECHO4) == 1:
            StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance


def vib1():
    # vibration = (((distance - 0.02) * -1) / (2 - 0.02)) + 1
    GPIO.output(GPIO_VIB1, True)
    # time.sleep(0.5)
    GPIO.output(GPIO_VIB1, False)

def vib2():
    # vibration = (((distance - 0.02) * -1) / (2 - 0.02)) + 1
    GPIO.output(GPIO_VIB2, True)
    # time.sleep(0.5)
    GPIO.output(GPIO_VIB2, False)

def vib3():
    # vibration = (((distance - 0.02) * -1) / (2 - 0.02)) + 1
    GPIO.output(GPIO_VIB3, True)
    # time.sleep(0.5)
    GPIO.output(GPIO_VIB3, False)

def vib4():
    # vibration = (((distance - 0.02) * -1) / (2 - 0.02)) + 1
    GPIO.output(GPIO_VIB4, True)
    # time.sleep(0.5)
    GPIO.output(GPIO_VIB4, False)


if __name__ == '__main__':
    try:
        while True:
            dist = distance1()
            print("Measured Distance1 = %.1f cm" % dist)

            dist = distance2()
            print("Measured Distance2 = %.1f cm" % dist)

            dist = distance3()
            print("Measured Distance3 = %.1f cm" % dist)

            dist = distance4()
            print("Measured Distance4 = %.1f cm" % dist)

            # if (dist <= 50):
            #     vib()
            # # print(vibration)
            # time.sleep(0.05)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

