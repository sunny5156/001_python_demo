#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 9:37
# @Author  : Scheaven
# @File    :  01_image_reize.py
# @description: 图像大小变换 cvResize ()
import numpy as np
import cv2
'''
CV.INTER_NN - 最近邻插值,
CV.INTER_LINEAR - 双线性插值 (缺省值)
CV.INTER_AREA - 使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..
CV.INTER_CUBIC - 立方插值.

'''
def resizeImage(image, width=None, height=None, inter=cv2.INTER_AREA):
    newsize = (width, height)
    # 获取图像尺寸
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    # 高度算缩放比例
    if width is None:
        n = height / float(h)
        newsize = (int(n * w), height)
    else:
        n = width / float(w)
        newsize = (width, int(h * n))

    # 缩放图像
    newimage = cv2.resize(image, newsize, interpolation=inter)
    return newimage


imageOriginal = cv2.imread("../ski.jpg")
cv2.imshow("Original", imageOriginal)
# 获取图像尺寸
w = width = imageOriginal.shape[1]
h = width = imageOriginal.shape[2]
print("Image size:", w, h)
# 放大2倍
newimage = resizeImage(imageOriginal, w * 2, h * 2, cv2.INTER_CUBIC)
cv2.imshow("New", newimage)
# 保存缩放后的图像
cv2.imwrite('newimage12.jpg', newimage)
# 缩小5倍
newimage2 = resizeImage(imageOriginal, int(w / 5), int(h / 5), cv2.INTER_CUBIC)
cv2.imwrite('newimage22.jpg', newimage2)