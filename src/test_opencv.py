# !python3
# -*- coding: utf-8 -*-

"""
Create on 2018 08 29 10:29
@author: wuyu
"""

import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


def test_opencv_1():
    img_path = "C://Users//admin//Pictures//sdkServerApi_Permission_deni.PNG"

    # 彩色图像 cv2.IMREAD_COLOR
    # img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # 灰度图 cv2.IMREAD_GRAYSCALE
    # img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 带alpha通道  cv2.IMREAD_UNCHANGED     测试和cv2.IMREAD_COLOR效果相同
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # print(img)

    if img is not None:
        # cv2.WINDOW_NORMAL 可调整图框尺寸   默认: cv2.WINDOW_AUTOSIZE
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("img is None, img_path={}, exists={}.".format(img_path, os.path.exists(img_path)))


def test_2():
    img_path = "C://Users//admin//Pictures//sdkServerApi_Permission_deni.PNG"
    img = cv2.imread(img_path, 0)
    cv2.imshow('image', img)
    # k = cv2.waitKey(0)
    # 64位机器
    k = cv2.waitKey(0) & 0xff

    # wait for ESC key to exit
    if k == 27:
        cv2.destroyAllWindows()
    # wait for 's' key to save and exit
    elif k == ord('s'):
        cv2.imwrite('C://Users//admin//Pictures//messigray.png', img)
        cv2.destroyAllWindows()


def test_3():
    img_path = "C://Users//admin//Pictures//sdkServerApi_Permission_deni.PNG"
    img = cv2.imread(img_path, 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()


def test_4():
    """
    使用 matplotlib 正确显示彩色图片  BGR -> RGB
    """

    img_path = "C://Users//admin//Pictures//sdkServerApi_Permission_deni.PNG"
    img = cv2.imread(img_path, 1)
    # print(img)
    # b, g, r = cv2.split(img)
    # img2 = cv2.merge([r, g, b])
    img2 = img[:, :, ::-1]
    plt.subplot(121)
    plt.imshow(img)  # expects distorted color
    plt.subplot(122)
    plt.imshow(img2)  # expect true color
    plt.show()

    cv2.imshow('bgr image', img)  # expects true color
    cv2.imshow('rgb image', img2)  # expects distorted color
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test_video():
    path = "rtsp://admin:1234qwer@192.168.16.202/h264/ch1/main"
    video_path = 0

    cap = cv2.VideoCapture(path)

    for i in range(18):
        print("cap.get({}) = {}".format(i, cap.get(i)))

    # not use ???
    cap.set(3, 640)
    cap.set(4, 480)
    print("cap.get(3) = {}, cap.get(4) = {}".format(cap.get(3), cap.get(4)))

    while True:
        try:
            ret, frame = cap.read()
        except Exception as e:
            print(str(e))
        if ret:
            cv2.namedWindow('gray Video', cv2.WINDOW_NORMAL)
            cv2.namedWindow('Oto Video', cv2.WINDOW_NORMAL)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("gray Video", gray)
            cv2.imshow("Oto Video", frame)
        else:
            print("camera catch image error!")
            break
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


def test_5():
    path = "rtsp://admin:1234qwer@192.168.16.202/h264/ch1/main"
    cap = cv2.VideoCapture(path)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret==True:
            # > 0 : L/R turn    0:Top/down turn    <0:L/R and Top/down turn
            frame = cv2.flip(frame, -1)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def test_draw():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1, cv2.LINE_AA)
    cv2.ellipse(img, (256, 256), (100, 50), 180, 0, 180, (125, 125, 125), -1, cv2.LINE_AA)

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 0, 255), 3, lineType=cv2.LINE_AA)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

    winname = "test_draw"
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.imshow(winname, img)

    k = cv2.waitKey(0) & 0xff

    if ord('q') == k:
        cv2.destroyAllWindows()


def test_mouse():
    # events = [i for i in dir(cv2) if 'EVENT' in i]
    # print(events)
    """['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON',
     'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK',
     'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL',
     'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']"""

    drawing = False
    mode = True
    ix, iy = -1, -1

    def draw_circle(event, x, y, flags, param):
        nonlocal drawing, mode, ix, iy

        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img, (x, y), 20, (255, 0, 0), 3)

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        # 当鼠标左键按下并移动是绘制图形。 event可以查看移动， flag查看是否按下
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            if drawing is True:
                if mode is True:
                    cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
                else:
                    # 绘制圆圈，小圆点连在一起就成了线， 3 代表了笔画的粗细
                    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                    # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                    #  r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                    #  cv2.circle(img,(x,y),r,(0,0,255),-1)
        # 当鼠标松开停止绘画。
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            mode = not mode
            # if mode==True:
            #     cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            # else:
            #     cv2.circle(img,(x,y),5,(0,0,255),-1)

    # 创建图像与窗口并将窗口与回调函数绑定
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while True:
        cv2.imshow('image', img)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


def test_progressbar():
    def nothing(x):
        pass

    # 创建一副黑色图像
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    switch = "0:OFF\n1:ON"
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv2.destroyAllWindows()


def test_6():
    img = cv2.imread("D:/project/py_test/test_open_cv_image/rose_1.jpg")
    bgr_100_100 = img[100, 100]
    b_100_100 = img[100, 100, 0]
    # print(img, type(img))
    print(bgr_100_100)
    print(b_100_100)
    print(img.item(100, 100, 0))
    img.itemset((100, 100, 0), 100)
    print(img.item(100, 100, 0))
    print("(高度，宽度，通道数) = ", img.shape)
    print("像素数：", img.size, 768*1366*3)
    print("数据类型: ", img.dtype)
    log = img[50:140, 1120:1300]
    # cv2.imshow('log', log)

    # img[300:390, 1120:1300] = log
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.split()是一个比较耗时的操作，尽量不要用
    # b, g , r = cv2.split(img)
    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    # print(b, g, r)


def test_border():
    """给图片添加边框"""

    BLUE = [0, 0, 255]
    img = cv2.imread('../test_open_cv_image/rose_3.jpg')
    img2 = img[:, :, ::-1]

    replicate = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img2, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=BLUE)
    plt.subplot(231), plt.imshow(img2, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    plt.show()


def test_cv_add():
    """openCvd的加法是一种饱和操作，Numpy的加法是一种模操作"""
    # x = np.uint8([250])
    # y = np.uint8([10])
    # print("cv2.add(x, y) = {}, x + y = {}".format(cv2.add(x, y), x + y))

    img1 = cv2.imread('../test_open_cv_image/rose_1920_1080_1.jpg')
    img2 = cv2.imread('../test_open_cv_image/rose_1920_1080_2.jpg')

    # 图片大小、类型必须一致
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindow()


if __name__ == "__main__":
    # test_opencv_1()
    # test_2()
    # test_3()
    # test_4()
    # test_video()
    # test_5()
    # test_draw()
    # test_mouse()
    # test_progressbar()
    # test_6()
    # test_border()
    test_cv_add()