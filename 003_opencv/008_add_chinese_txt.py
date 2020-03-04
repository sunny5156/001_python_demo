#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 20:08
# @Author  : Scheaven
# @File    : test002.py
# @description: 

import cv2
import numpy as np


def paint_chinese_opencv(im, chinese, pos, color):
    img_PIL = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype('NotoSansCJK-Bold.ttc', 40)
    fillColor = color #(255,0,0)
    position = pos #(100,100)
    #if not isinstance(chinese,unicode):
    #    chinese = chinese.decode('utf-8')
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, chinese, font=font, fill=fillColor)

    img = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return img




font = cv.FONT_HERSHEY_SIMPLEX
# 文字输出位置
position = (100, 100)


imgzi = cv.putText(img1, str(" english+number "), (200, 130), font, 1.2, (255, 255, 255), 2)
# 输出内容
img1 = paint_chinese_opencv(img1, "中文", position, (0, 0, 255))

