import multiprocessing as mp
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin Definitions
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

# Direction Definition
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


# GPIO.setup(GPIO_VIB4, GPIO.OUT)

def distance1():
    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
    StartTime1 = time.time()
    StopTime1 = time.time()

    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime1 = time.time()

    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime1 = time.time()

    TimeElapsed1 = StopTime1 - StartTime1

    distance1 = (TimeElapsed1 * 34300) / 2

    return distance1


def distance2():
    GPIO.output(GPIO_TRIGGER2, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
    StartTime2 = time.time()
    StopTime2 = time.time()

    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime2 = time.time()

    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime2 = time.time()

    TimeElapsed2 = StopTime2 - StartTime2

    distance2 = (TimeElapsed2 * 34300) / 2

    return distance2


def distance3():
    GPIO.output(GPIO_TRIGGER3, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER3, False)
    StartTime3 = time.time()
    StopTime3 = time.time()

    while GPIO.input(GPIO_ECHO3) == 0:
        StartTime3 = time.time()

    while GPIO.input(GPIO_ECHO3) == 1:
        StopTime3 = time.time()

    TimeElapsed3 = StopTime3 - StartTime3

    distance3 = (TimeElapsed3 * 34300) / 2

    return distance3


def distance4():
    GPIO.output(GPIO_TRIGGER4, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER4, False)
    StartTime4 = time.time()
    StopTime4 = time.time()

    while GPIO.input(GPIO_ECHO4) == 0:
        StartTime4 = time.time()

    while GPIO.input(GPIO_ECHO4) == 1:
        StopTime4 = time.time()

    TimeElapsed4 = StopTime4 - StartTime4

    distance4 = (TimeElapsed4 * 34300) / 2

    return distance4


def call1():
    try:
        while True:
            dist1 = distance1()
            print("Measured Distance from sensor 1 = %.1f cm" % dist1)
            time.sleep(0.1)
            while (dist1 < 75):
                GPIO.output(GPIO_VIB1, True)
                dist1 = distance1()
            GPIO.output(GPIO_VIB1, False)

    except Exception as e:
        print(e)
        GPIO.cleanup()


def call2():
    try:
        while True:
            dist2 = distance2()
            print("Measured Distance from sensor 2 = %.1f cm" % dist2)
            time.sleep(0.1)
            if (dist2 < 75):
                GPIO.output(GPIO_VIB2, True)
                time.sleep(1)
            GPIO.output(GPIO_VIB2, False)

    except Exception as e:
        print(e)
        GPIO.cleanup()


def call3():
    try:
        while True:
            dist3 = distance3()
            print("Measured Distance from sensor 3 = %.1f cm" % dist3)
            time.sleep(0.1)
            while (dist3 < 75):
                GPIO.output(GPIO_VIB3, True)
                dist3 = distance3()
            GPIO.output(GPIO_VIB3, False)

    except Exception as e:
        print(e)
        GPIO.cleanup()


def call4():
    try:
        while True:
            dist4 = distance4()
            print("Measured Distance from sensor 4 = %.1f cm" % dist4)
            time.sleep(0.1)
            while (dist4 < 75):
                GPIO.output(GPIO_VIB3, True)
                dist4 = distance4()
            GPIO.output(GPIO_VIB3, False)

    except Exception as e:
        print(e)
        GPIO.cleanup()


p1 = mp.Process(target=call1)
p2 = mp.Process(target=call2)
p3 = mp.Process(target=call3)
p4 = mp.Process(target=call4)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

print("Time: ", time.perf_counter())