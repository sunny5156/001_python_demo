#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 15:27
# @Author  : Scheaven
# @File    :  utils.py
# @description:
import cv2

class video_open:
    def __init__(self, args, carmmer_id):
        #self.readtype=read_type
        if args.in_type == "camera":
            if carmmer_id == "0":
                # self.readtype = args.c_first
                self.readtype = args.v_i
            else:
                # self.readtype = args.c_second
                self.readtype = args.v_in
        else:
            self.readtype= args.v_in

    def generate_video(self):
        video_capture = cv2.VideoCapture(self.readtype)
        return video_capture
