#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: camera_configs.py
import cv2
import numpy as np
 
left_camera_matrix = np.array([[740.00513,0,370.66598],
                               [0,738.85793,238.37029],
                               [0,0,1.0000]])
left_distortion = np.array([[0.07307,-0.17913,-0.00883,0.00369,0.00000]])
 
 
 
right_camera_matrix = np.array([[744.87113, 0., 363.51034],
                                [0., 744.87844, 229.51777],
                                [0., 0., 1.]])
right_distortion = np.array([[0.05342,-0.12668,-0.00960,0.00455,0.00000]])
 
om = np.array([-0.01171,-0.00147,-0.00274]) # 旋转关系向量
R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-62.80819,2.81759,2.88228]) # 平移关系向量
 
size = (640, 480) # 图像尺寸
 
# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)