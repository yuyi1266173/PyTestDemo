# python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def draw_circle(e, x, y, flags, param):
    if e == cv2.EVENT_LBUTTONDOWN:
        global img
        img = cv2.imread("../../test_open_cv_image/save_rose_1.jpg")

        print(x, y)
        global g_x, g_y
        g_x, g_y = x, y
        c = np.random.randint(0, 256, size=3)
        print(c, c[1], c[2])
        cv2.circle(img, (x, y), 10, (int(c[1]), int(c[2])), -1)


# img = np.ones((365, 500, 3), np.uint8) * 255
img = cv2.imread("../../test_open_cv_image/save_rose_1.jpg")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 500, 500)
# cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)

g_x = 0
g_y = 0

while True:
    cv2.imshow("image", img)
    key_value = cv2.waitKey(1)
    if key_value != -1:
        print(key_value & 0xff)

    if key_value & 0xff == 27:
        break
    elif key_value & 0xff == 119:  # w
        g_y -= 5
    elif key_value & 0xff == 115:  # s
        g_y += 5
    elif key_value & 0xff == 97:  # a
        g_x -= 5
    elif key_value & 0xff == 100:  # d
        g_x += 5

    img = cv2.imread("../../test_open_cv_image/save_rose_1.jpg")
    cv2.circle(img, (g_x, g_y), 10, (255, 255), -1)

cv2.destroyAllWindows()
