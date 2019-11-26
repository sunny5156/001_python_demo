#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 20:16
# @Author  : Scheaven
# @File    :  003_test.py
# @description:

# -*- coding: utf-8 -*-

import cv2
import numpy as np
# -----------------------鼠标操作相关------------------------------------------


class Monitoring_Region():
    def __init__(self):
        self.lsPointsChoose = []
        self.tpPointsChoose = []
        self.pointsCount = 0
        self.count = 0
        self.pointsMax = 4
        self.cap = cv2.VideoCapture("rtsp://admin:a1234567@192.168.5.36:554/h264/ch1/main/av_stream")
        self.img = None
        # ---------------------------------------------------------
        # --图像预处理，设置其大小
        # height, width = img.shape[:2]
        # size = (int(width * 0.3), int(height * 0.3))
        # img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        # ------------------------------------------------------------
        self.ROI = None
        self.__set_init_region()

    def __set_init_region(self):
        ret, frame = self.cap.read()
        w,h = frame.shape[:2]
        self.img = cv2.resize(frame,(1200,1200*w//h))
        # ---------------------------------------------------------
        # --图像预处理，设置其大小
        # height, width = img.shape[:2]
        # size = (int(width * 0.3), int(height * 0.3))
        # img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        # ------------------------------------------------------------
        self.ROI = self.img.copy()
        cv2.namedWindow('src')
        cv2.setMouseCallback('src', self.__on_mouse)
        cv2.imshow('src', self.img)
        cv2.waitKey(0)

    def __on_mouse(self, event, x, y, flags, param):
        img2 = self.img.copy()  # 此行代码保证每次都重新再原图画  避免画多了
        # -----------------------------------------------------------
        #    count=count+1
        #    print("callback_count",count)
        # --------------------------------------------------------------

        if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
            self.pointsCount = self.pointsCount + 1
            # 感觉这里没有用？2018年8月25日20:06:42
            # 为了保存绘制的区域，画的点稍晚清零
            # if (pointsCount == pointsMax + 1):
            #     pointsCount = 0
            #     tpPointsChoose = []
            # print('pointsCount:', self.pointsCount)
            point1 = (x, y)
            # print(x, y)
            # 画出点击的点
            cv2.circle(img2, point1, 2, (0, 255, 0), 2)

            # 将选取的点保存到list列表里
            self.lsPointsChoose.append([x, y])  # 用于转化为darry 提取多边形ROI
            self.tpPointsChoose.append((x, y))  # 用于画点
            # ----------------------------------------------------------------------
            # 将鼠标选的点用直线连起来
            # print(len(self.tpPointsChoose))
            for i in range(len(self.tpPointsChoose) - 1):
                # print('i', i)
                cv2.line(img2, self.tpPointsChoose[i], self.tpPointsChoose[i + 1], (0, 0, 255), 2)
            # ----------------------------------------------------------------------
            # ----------点击到pointMax时可以提取去绘图----------------
            if (self.pointsCount == self.pointsMax):
                # -----------绘制感兴趣区域-----------
                self.__ROI_byMouse()
                __ROI_byMouse_flag = 1
                lsPointsChoose = []
                cv2.destroyAllWindows()
                return

            cv2.imshow('src', img2)
        # -------------------------右键按下清除轨迹-----------------------------
        if event == cv2.EVENT_RBUTTONDOWN:  # 右键点击
            # print("right-mouse")
            pointsCount = 0
            tpPointsChoose = []
            lsPointsChoose = []
            # print(len(tpPointsChoose))
            for i in range(len(tpPointsChoose) - 1):
                # print('i', i)
                cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
            cv2.imshow('src', img2)

    def __ROI_byMouse(self):
        mask = np.zeros(self.img.shape, np.uint8)
        pts = np.array([self.lsPointsChoose], np.int32)  # pts是多边形的顶点列表（顶点集）
        pts = pts.reshape((-1, 1, 2))
        # 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
        # OpenCV中需要先将多边形的顶点坐标变成顶点数×1×2维的矩阵，再来绘制

        # --------------画多边形---------------------
        mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
        ##-------------填充多边形---------------------
        mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
        self.ROI = cv2.bitwise_and(mask2, self.img)

    def get_RgPionts(self):
        return self.tpPointsChoose

if __name__ == '__main__':
    MR = Monitoring_Region()
    MR.get_RgPionts()

