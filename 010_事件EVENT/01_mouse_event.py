#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 10:52
# @Author  : Scheaven
# @File    :  mouse_event.py
# @description: 鼠标响应事件
import cv2
point = None
point_flog = True
def __on_mouse(event,x ,y ,flags,param):
    global point,point_flog
    if event == cv2.EVENT_LBUTTONDOWN: #鼠标左击事件
        if(point_flog):
            point = (x, y)
            cv2.circle(param[0], point, 2, (0, 255, 0), 2)
            point_flog = False
        else:
            return

    for i in range(len(param[1])-1):
        cv2.line(param[0], tuple(param[1][i]), tuple(param[1][i+1]), (0, 0, 255), 2)

    cv2.imshow('region',param[0])
    # cv2.waitKey(0)

def select_point(region):
    cap = cv2.VideoCapture("rtsp://admin:a1234567@192.168.5.36:554/h264/ch1/main/av_stream")
    ret, frame = cap.read()
    cv2.namedWindow('region')
    w,h = frame.shape[:2]
    img = cv2.resize(frame,(1200,1200*w//h))
    cv2.setMouseCallback("region", __on_mouse, [img, region])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    global point
    return point


if __name__ == '__main__':
    region = [(100, 100), (100, 200), (800, 100), (800, 50)]
    select_point(region)
    print(point)

