import time


def setTimer(seconds):
    time1 = time.time()
    time2 = time1+seconds

    for i in range(seconds):
        time1 = time.time()
        test = time2-time1
        print(test)


setTimer(20)
