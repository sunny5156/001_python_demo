#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 18:52
# @Author  : Scheaven
# @File    :  0102.py
# @description: 视频录制功能

import cv2
import time
cap = cv2.VideoCapture('rtsp://admin:a1234567@192.168.5.37:554/h264/ch1/main/av_stream')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = cap.get(cv2.CAP_PROP_FPS)
print("fps", fps)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('fall2001.avi', fourcc, fps, size)
frame_count = 0
s_t = 0
while 1:
    e_t = time.time()
    # if s_t != 0:
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_count*(e_t- s_t)*cv2.CAP_PROP_FRAME_COUNT))
    #     frame_count += 1
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (854, 480))
    s_t = time.time()

    if frame is None:
        continue

    # print("qqqqqqqqqqqqqqq",cv2.CAP_PROP_FRAME_COUNT)

    # print("1111111", s_t)
    out.write(frame)
    cv2.imshow("d", frame)
    cv2.waitKey(1)
    # time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


