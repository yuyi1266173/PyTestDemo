# !python3
# -*- coding: utf-8 -*-

# author: wu yu
# create date: 2018-11-05
# function: test for threading packages


import time
import threading
from threading import Thread, Event


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


def test():
    t1 = Thread(target=countdown, args=(10,), daemon=True)
    t1.start()

    if t1.is_alive():
        print("Thread t1 is alive")
    else:
        print("Thread t1 is not alive")

    # threading.currentThread(): 返回当前的线程变量。
    # threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    # threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
    print(threading.current_thread(), type(threading.current_thread()))
    print("1 --- ", threading.activeCount(), threading.enumerate())

    # 等待t1线程结束
    t1.join()
    print("---- end ------")

    print("2 --- ", threading.activeCount(), threading.enumerate())


class CountDownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(5)


def test2():
    c = CountDownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    print("CountDownTask ia running...")
    c.terminate()
    t.join()


# 线程同步
def countdown_2(n, started_evt):
    print("countdown_2 starting...")
    started_evt.set()

    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


def test_event():
    start_event = Event()
    print("Launching countdown_2...")
    t = Thread(target=countdown_2, args=(5, start_event))
    t.start()

    start_event.wait()
    print("countdown_2 is running...")


if __name__ == "__main__":
    # test()
    # test2()
    test_event()
