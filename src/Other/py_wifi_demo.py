# !python3
# -*- coding: utf-8 -*-

"""
pywifi模块
"""

from pywifi import PyWiFi


AKMS = {
    0: "AKM_TYPE_NONE",
    1: "AKM_TYPE_WPA",
    2: "AKM_TYPE_WPAPSK",
    3: "AKM_TYPE_WPA2",
    4: "AKM_TYPE_WPA2PSK",
    5: "AKM_TYPE_UNKNOWN",
}


def check_state():
    wifi = PyWiFi()

    # 无线网卡
    faces = wifi.interfaces()
    if not faces:
        print("此电脑未安装无线网卡.")
        return

    # 判断第一个无线网卡的连接状态
    print(faces[0].status())
    if faces[0].status() == 4:
        print("电脑已连接WIFI.")
    else:
        print("电脑未连接WIFI.")


def get_wireless():
    wifi = PyWiFi()
    faces = wifi.interfaces()
    if not faces:
        print("此电脑未安装无线网卡.")
        return

    # face[0].scan() 扫描附近的无线信号
    wireless = faces[0].scan_results()

    print(wireless)

    for data in wireless:
        print("-" * 20)
        print(data.ssid)           # 无线信号名称
        print(AKMS[data.akm[0]])   # 加密方式
        print("-" * 20)


if __name__ == "__main__":
    check_state()
    get_wireless()
