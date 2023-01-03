# coding=utf-8
import sys
import time
import datetime
from tkinter import Tk
from tkinter import messagebox


def tomatoes():
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    tomatoes_times = 1
    big_relax_times = 4
    work_interval = 25
    relax_interval = 5
    big_relax_interval = 15
    while True:
        messagebox.showinfo("番茄工作法", "开启第{}轮番茄计时".format(tomatoes_times))
        print("第{}轮番茄计时进行中, 请专注{}分钟, {}".format(tomatoes_times, work_interval, datetime.datetime.now()))
        time.sleep(work_interval * 60)
        if tomatoes_times % big_relax_times == 0:
            r_interval = big_relax_interval
        else:
            r_interval = relax_interval
        messagebox.showinfo("番茄工作法", "第{}轮番茄计时已结束，请休息{}分钟".format(tomatoes_times, r_interval))
        print("休息中{}".format(datetime.datetime.now()))
        time.sleep(r_interval * 60)
        tomatoes_times += 1
        ask = messagebox.askokcancel("番茄工作法", "休息结束，是否开启下一轮番茄计时")
        if not ask:
            sys.exit()


if __name__ == '__main__':
	tomatoes()
