#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 16:07
# @Author  : Scheaven
# @File    :  region_point.py
# @description:
import math
import cv2
class Linear():
    def __init__(self,points_list, center_p):
        self.points_list = points_list
        self.p1 = points_list[0]
        self.p2 = points_list[1]
        self.p3 = points_list[2]
        self.p4 = points_list[3]
        self.x1, self.y1 = self.p1
        self.x2, self.y2 = self.p2
        self.x3, self.y3 = self.p3
        self.x4, self.y4 = self.p4
        self.center_p = center_p
        self.k = 0
        self.b = 0
        self.flag = 0
        self.__bottom_line()
        self.__third_line()

    # 直线法表示底边的直线
    def __bottom_line(self):
        x1, y1 = self.p1
        x2, y2 = self.p2
        if x2 == x1:
            self.flag = 1  # 平行于y轴
        elif y2 == y1:
            self.flag = 2  # 平行于x轴
        else:
            self.flag = 0
            self.k = (y2 - y1) / (x2 - x1)

    # 经过定点并平行于底边
    def __third_line(self):
        center_x, center_y = self.center_p
        if self.flag == 0:
            self.b = center_y - self.k * center_x
        return self.flag, self.k, self.b

    # 计算交点
    def __inter_ponits(self, Pm, Pn):
        xm, ym = Pm
        xn, yn = Pn
        if xm == xn:
            xx = xm
            if self.flag == 2:
                yy = self.center_p[1]
            else:
                yy = self.k*xx + self.b
        elif ym == yn:
            yy = ym
            if self.flag == 1:
                xx = self.center_p[0]
            else:
                xx = (yy - self.b)/self.k
        else:
            k1 = (ym-yn)/(xm-xn)
            b1 = ym - k1*xm
            if self.flag == 1:
                xx = self.center_p[0]
                yy = k1*xx + b1
            elif self.flag == 2:
                yy = self.center_p[1]
                xx = (yy - b1)/k1
            else:
                xx = (self.b - b1)/(k1 - self.k)
                yy = k1*xx + b1
        return xx, yy

    #绘制显示结果
    def deaw_regions(self,x_s, y_s, x_e, y_e):
        cap = cv2.VideoCapture("../../../cs01.avi")
        _,frame = cap.read()
        img = frame
        cv2.circle(img,self.center_p,2,(0,255,0),2)
        for i in range(len(self.points_list) - 1):
            cv2.line(img, tuple(self.points_list[i]), tuple(self.points_list[i + 1]), (0, 0, 255), 2)
        cv2.line(img,(int(x_s),int(y_s)),(int(x_e),int(y_e)),(255,0,0),2)
        cv2.imshow("imgg",img)
        cv2.waitKey(0)

    # 计算人所在位置的截断距离
    def calculate_distance(self):
        x_s, y_s = self.__inter_ponits(self.p1, self.p4)
        x_e, y_e = self.__inter_ponits(self.p2, self.p3)
        # self.deaw_regions(x_s, y_s, x_e, y_e)
        return math.hypot(x_s-x_e, y_s-y_e)

if __name__ == '__main__':
    line = Linear()