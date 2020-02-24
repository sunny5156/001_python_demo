#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 14:06
# @Author  : Scheaven
# @File    :  001_test.py.py
# @description: 给视频帧逐帧添加文字信息，pyav和img的转换
import av
import cv2 as cv

video = av.open("003_s.mp4", mode="r")
out_container = av.open("003_r.mp4", mode="w")
fps = float(video.streams.video[0].average_rate)
stream = out_container.add_stream('mpeg4', rate=fps)
width = video.streams.video[0].width
height = video.streams.video[0].height
stream.width = width
stream.height = height
stream.pix_fmt = "yuv420p"
print("====-----====")
for frame in video.decode(**{'video': 0}):
    print("frame ok", type(frame))
    img = frame.to_nd_array(format='rgb24')
    font = cv.FONT_HERSHEY_SIMPLEX
    imgzi = cv.putText(img, str(11), (50, 300), font, 1.2, (255, 255, 255), 2)
    frame = av.VideoFrame.from_ndarray(img, format='rgb24')
    for packet in stream.encode(frame):
        print("packet ok")
        out_container.mux(packet)

print("frame close")
video.close()
for packet in stream.encode():
    out_container.mux(packet)
print("over")
out_container.close()
