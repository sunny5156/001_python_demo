#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:18
# @Author  : Scheaven
# @File    : 007_read_subfolder_file.py
# @description: Read files in folders and subfolders,and read the classification of subfolder names.
from imutils import paths
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
import cv2
import random,os
import numpy as np


def load_image_date(path):
    list_x = []
    list_y = []
    count = 0

    A = sorted(list(paths.list_images(path)))
    random.shuffle(A)
    for line in A:
        x, y = process_line(line)
        list_x.append(x)
        list_y.append(y)
        count += 1
        if count >= 20:
            data = np.array(list_x, dtype='float') / 255.0
            labels = np.array(list_y)
            yield data, labels
            count = 0
            list_x = []
            list_y = []


# 读取图片和标签
def process_line(line):
    img_x = cv2.imread(line)
    img_x = cv2.resize(img_x, (32, 32))
    img_x = img_to_array(img_x)
    line = line.replace("/","\\")
    label = int(line.split(os.path.sep)[-2])
    emable = to_categorical(label, 2)  # one-hot编码
    return img_x, emable


if __name__ == '__main__':
    path = "./images/"
    # 不可 (x_t,y_t) = load_image_date(path)
    # generator的打印方式如下
    for (x_t,y_t) in load_image_date(path):
        print(x_t.shape,y_t.shape)