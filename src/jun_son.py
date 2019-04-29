# !python3
# -*- coding: utf-8 -*-

"""
为前同事写一个早八点和晚八点执行特定函数的线程
为前同事写一个早延迟八小时执行特定函数的线程

Author : Wu Yu
Date   : 2019-04-25
"""

import time
from threading import Thread, Timer
from datetime import datetime


class EightHourWorkThread(Thread):
    """
    早八点和晚八点执行执行函数的线程
    """

    def __init__(self, work_fun=None, fun_args=None):
        """
        :param work_fun: 要执行的函数
        :param fun_args: 函数参数     无参数时不传此参数， 一个参数时传（5，） 多个传（5， ‘俊儿砸’， 3.14）
        """
        super(EightHourWorkThread, self).__init__()
        self.work_fun = work_fun
        self.fun_args = fun_args
        self.sleep_time = 12 * 3600  # 12h
        self.stop_flag = False

    def run(self):
        # 获取当前时间
        now = datetime.now()
        # print(now.hour, now.minute, now.second)

        if 0 == now.minute and 0 == now.second and now.hour in [8, 20]:
            # 当前时间为8 / 20
            wait_time = 0
        else:
            if now.hour in range(0, 8):
                tmp_hour = 7 - now.hour
            elif now.hour in range(8, 20):
                tmp_hour = 19 - now.hour
            else:
                tmp_hour = 23 - now.hour + 8

            wait_time = tmp_hour * 3600 + (60 - now.minute) * 60
            if now.second != 0:
                wait_time = wait_time - now.second

        if wait_time != 0:
            time.sleep(wait_time)

        if self.work_fun is not None:
            if self.fun_args is None:
                self.work_fun()
            else:
                self.work_fun(*self.fun_args)
        else:
            print("李俊是我儿砸！")

        while True:
            if self.stop_flag:
                break

            time.sleep(self.sleep_time)

            if self.work_fun is not None:
                self.work_fun()
            else:
                print("李俊是我儿砸！")

    def stop_thread(self):
        self.stop_flag = True


class DelayWorkThread(Thread):
    """
    延时执行线程
    """

    def __init__(self, delay_seconds=3, work_fun=None, fun_args=None):
        """
        :param delay_seconds:  延时的时间(s) 默认为3秒
        :param work_fun: 3 秒后执行的函数
        :param fun_args: 函数参数  例：（5， "字符串"）   一个参数时传（5，）
        """

        super(DelayWorkThread, self).__init__()
        self.work_fun = work_fun
        self.delay_seconds = delay_seconds
        self.fun_args = fun_args
        self.stop_flag = False

    def run(self):
        # self.work_fun为空时使用默认函数
        if self.work_fun is None:
            self.work_fun = lambda: print("李俊是我儿砸！")
            self.fun_args = None

        while True:
            if self.stop_flag:
                break

            time.sleep(self.delay_seconds)
            if self.fun_args is None:
                self.work_fun()
            else:
                self.work_fun(*self.fun_args)

    def stop_thread(self):
        """
        使线程停止工作
        """
        self.stop_flag = True


def delay_eight_hour_work_once(delay_seconds=3, work_fun=None, fun_args=None):
    """
    延时指定时间执行指定函数（一次执行）
    :param delay_seconds: 延时时间（s）
    :param work_fun: 指定函数
    :param fun_args: 函数参数 无参数时不传此参数， 一个参数时传（5，） 多个传（5， ‘俊儿砸’， 3.14）
    :return:
    """

    if work_fun is None:
        work_fun = lambda: print("李俊是我儿砸！")
        fun_args = None

    Timer(delay_seconds, work_fun, fun_args).start()


def test_fun(x, y):
    print("李俊是我儿砸！out.", x, y)


if __name__ == "__main__":
    # work_thread = EightHourWorkThread(test_fun)
    # work_thread.start()

    delay_work = DelayWorkThread()
    delay_work = DelayWorkThread(delay_seconds=2, work_fun=test_fun, fun_args=('hahaha', 10))
    delay_work.start()
    time.sleep(6)
    delay_work.stop_thread()

    # delay_eight_hour_work_once(work_fun=test_fun, fun_args=('hahaha', 10))


