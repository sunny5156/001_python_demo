 # -*- coding: utf-8 -*-
# @Time    : 2020/7/30 17:27
# @Author  : suntianyu
# @FileName: extract_target.py
# @Software: PyCharm
# coding:utf-8
import cv2
import numpy as np
from rgbsplite import non_max_suppression_slow
import os


# from pypolar import img_polar_transform

'''
根据轮廓检测印章的位置
'''


# 加载图片

def exc_img(img_path, outpath):
    image = cv2.imread(img_path)
    # cv2.imshow('7-8t', image)
    h, w, _ = image.shape
    bg_area = w*h
    # print(image.shape)
    img = np.zeros(image.shape, np.uint8)
    img[:, :, 0] = np.zeros([h, w]) + 255
    img[:, :, 1] = np.ones([h, w]) + 254
    img[:, :, 2] = np.ones([h, w]) * 255
    # cv2.imshow("iamge", img)
    # print(img.shape)
    # img2 = np.zeros([400, 400, 3], np.uint8) + 255
    # cv2.imshow("iamge2", img2)
    # cv2.waitKey(0)
    # 统一处理图片大小
    # img_w = 650 if image.shape[1] > 600 else 400
    # image = cv2.resize(image, (img_w, int(img_w * image.shape[0] / image.shape[1])), interpolation=cv2.IMREAD_COLOR)
    impng = cv2.cvtColor(image.copy(), cv2.COLOR_RGB2RGBA)
    # cv2.imshow("impng",impng)
    # cv2.waitKey()
    # image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    # image = cv2.imread('img\\public-2004-16-a7912dbd-72b0-4d96-9d65-70abc21940d5.png')
    hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_range = np.array([0, 43, 46])
    high_range = np.array([10, 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    th = cv2.dilate(th, element)
    index1 = th == 255
    img1 = np.zeros(impng.shape, np.uint8)
    img1[:, :, :] = (255, 255, 255, 0)
    img1[index1] = impng[index1]  # (0,0,255)
    # cv2.imwrite("res_6_22wt.jpg",img1)
    # cv2.imshow("img1",img1)
    # cv2.waitKey()

    # img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    # 创建四通道图片
    # img1=topng(img1)
    # img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2RGBA)
    # cv2.imwrite('m1.png', img1)
    # cv2.imshow('1', img1)
    # cv2.waitKey()
    # cv2.imwrite("img1.png", img1)
    low_range = np.array([156, 43, 46])
    high_range = np.array([180, 255, 255])
    th = cv2.inRange(hue_image, low_range, high_range)
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    th = cv2.dilate(th, element)
    index1 = th == 255
    img2 = np.zeros(impng.shape, np.uint8)
    img2[:, :, :] = (255, 255, 255, 0)
    img2[index1] = impng[index1]
    # cv2.imshow('2', img2)
    # cv2.imwrite('m2.png', img2)

    imgreal = cv2.add(img2, img1)
    # cv2.imwrite('m222.png', imgreal)
    # cv2.waitKey()
    # img31 = cv2.cvtColor(img31, cv2.COLOR_BGR2RGB)
    white_px = np.asarray([255, 255, 255, 255])
    # black_px = np.asarray([0, 0, 0, 255])
    (row, col, _) = imgreal.shape
    for r in range(row):
        for c in range(col):
            px = imgreal[r][c]
            if all(px == white_px):
                imgreal[r][c] = impng[r][c]

    # 扩充图片防止截取部分
    # img4png = cv2.copyMakeBorder(imgreal, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255, 255, 255, 0])
    # cv2.imshow('imgreal', imgreal)
    # cv2.waitKey()
    img2gray = cv2.cvtColor(imgreal, cv2.COLOR_RGBA2GRAY)
    retval, grayfirst = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY_INV)

    # 再次膨胀，轮廓查找
    # img6 = cv2.GaussianBlur(grayfirst, (1, 1), 0, 0)
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (22, 22))
    img6 = cv2.dilate(grayfirst, element)
    # cv2.imshow('c_canny_img', img6)
    # cv2.waitKey()
    # cv2.imshow('img4', img6)

    c_canny_img = cv2.Canny(img6, 10, 10)
    # cv2.imshow('c_canny_img', c_canny_img)
    # cv2.waitKey()
    contours, hierarchy = cv2.findContours(c_canny_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    areas = []
    # rets = []
    for i, cnt in enumerate(contours):
        rect = cv2.minAreaRect(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        # print(x, y, w, h)
        ars = [area, i, x, y, x + w, y + h]
        areas.append(ars)
    areas = np.array(sorted(areas, reverse=True))
    index = 0
    for i, area in enumerate(areas):
        # print("area: ", area[0])
        # print("area: ",area[0])
        # print("bg_area: ",bg_area)
        if area[0]/bg_area < 0.01:
            index = i
            break
    # print("index: ", index)
    preboxes = areas[0:index]
    # print("preboxes: ", preboxes)

    picks = non_max_suppression_slow(preboxes, 0.1)

    print("picks: ", picks)
    # print("picks_len: ", len(picks))
    targets_area = []
    for i, pick in enumerate(picks):
        maxares = [pick]
        # print('maxares: ', maxares)
        x, y, w, h = cv2.boundingRect(contours[maxares[0][1]])
        # print(x, y, w, h)
        temp = image[y:(y + h), x:(x + w)]
        cv2.imshow("temp",temp)

        cv2.waitKey()
        # 高小于宽
        # print(temp.shape)
        # if temp.shape[0] < temp.shape[1]:
        #     # temp = cv2.resize(temp, (150, temp.shape[0]))
        #     zh = int((temp.shape[1] - temp.shape[0]) / 2)
        #     temp = cv2.copyMakeBorder(temp, zh, zh, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255, 0])
        # else:
        #     # temp = cv2.resize(temp, (temp.shape[1], 150))
        #     zh = int((temp.shape[0] - temp.shape[1]) / 2)
        #     temp = cv2.copyMakeBorder(temp, 0, 0, zh, zh, cv2.BORDER_CONSTANT, value=[255, 255, 255, 0])
        # cv2.imshow('sunty', temp)
        # dst = cv2.resize(temp, (150, 150), cv2.IMREAD_GRAYSCALE)
        # print(pick[2], pick[4], pick[3], pick[5])
        # print(img.shape)
        img[pick[3]: pick[5], pick[2]:pick[4]] = temp
        targets_area.append(w*h)
        # cv2.imshow(str(i), img)
    # cv2.imwrite(outpath, img)
    cv2.imshow("outpath", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    # filedir = 'test'
    # outdir = 'output'
    # filenames = os.listdir(filedir)
    # for filename in filenames:
    # filepath = filedir + '/' + filename
    # outpath = outdir + '/' + filename
    # print(filepath)
    exc_img("7-8pt.jpg", "./")