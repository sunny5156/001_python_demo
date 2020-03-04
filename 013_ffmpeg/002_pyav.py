#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 14:06
# @Author  : Scheaven
# @File    :  001_test.py.py
# @description: 给视频帧逐帧添加文字信息，pyav和img的转换，读取和存储
import av
import cv2 as cv

'''
	1、ffmpeg 对视频的读取、写入
	2、pyav 获取视频属性
	3、读取的视频流和图像的转化
'''

cap = av.open('/003_s.mp4', mode="r")
cap.streams.video[0].thread_type = "AUTO"
fps = float(cap.streams.video[0].average_rate)
duration = cap.streams.video[0].duration  # 容器的时长

# sz = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
#       int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
# fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')  # 保存视频的编码
# vout = cv.VideoWriter('./output/' + str(1) + '.mp4', fourcc, fps, sz, True)
out_container = av.open('./output/Scheaven.mp4', mode='w')
stream = out_container.add_stream('mpeg4', rate=fps)
print("cap wh::", cap.streams.video[0].width, cap.streams.video[0].height)
stream.width = int(cap.streams.video[0].width)
stream.height = int(cap.streams.video[0].height)
stream.pix_fmt = 'yuv420p'

if duration is None:
    isallvideo = True
else:
    isallvideo = False


 for frame in cap.decode(**{'video': 0}):
    f_count += 1
    out_frames.append(frame)
    init_frames.append(frame.to_rgb().to_ndarray())
    frame_index += 1
    
    init_frames = torch.as_tensor(np.stack(init_frames))


    font = cv.FONT_HERSHEY_SIMPLEX
    # 文字输出位置
    position = (100, 100)
    for frame in out_frames:
        img = frame.to_nd_array(format='rgb24')
        frame = av.VideoFrame.from_ndarray(img1, format='rgb24')
        for packet in stream.encode(frame):
            out_container.mux(packet)

    # frame = cv.flip(frame, 0)
    print("cnt::", cnt)
    out_frames = []
    init_frames = []
    frame_index = 1

cap.close()
# Flush stream
for packet in stream.encode():
    out_container.mux(packet)

# Close the file
out_container.close()