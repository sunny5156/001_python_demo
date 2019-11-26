#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 16:24
# @Author  : Scheaven
# @File    :  measurement_distance.py
# @description:
import math
import numpy as np
from singlecam_meadistance.mont_region import Monitoring_Region
from utils.region_point import Linear
from utils.mouse_event import select_point

# 调整点的位置信息，并输出底部两个点的距离信息
def adjust_points(points_list):
    p1 = np.array(points_list[0])
    p2 = np.array(points_list[1])
    p3 = np.array(points_list[2])
    p4 = np.array(points_list[3])
    distance_p1p2 = math.hypot((p1 - p2)[0], (p1 - p2)[1])
    distance_p1p4 = math.hypot((p1 - p4)[0], (p1 - p4)[1])
    if distance_p1p2 > distance_p1p4:
        p2, p4 = p4, p2
    distance_p1p2 = math.hypot((p1 - p2)[0], (p1 - p2)[1])
    distance_p3p4 = math.hypot((p3 - p4)[0], (p3 - p4)[1])
    if distance_p1p2 > distance_p3p4:
        points_list = [p1, p2, p3, p4]
        return distance_p1p2, points_list
    else:
        points_list = [p3, p4, p1, p2]
        return distance_p3p4, points_list


def mea_distance(base_distance,bottom_distance,center_distance):
    result_distance = base_distance*bottom_distance/center_distance
    return result_distance


if __name__ == '__main__':
    base_distance = 590 #基线距离相机位置
    #绘制基线区域信息
    MR = Monitoring_Region()
    points_list = MR.get_RgPionts()
    bottom_distance, points_list = adjust_points(points_list)

    print(points_list)
    # 设置鼠标选点
    center_point = select_point(points_list)
    
    #通过几何关系测得选点和基线的长度关系，通过基线距离相机位置测距
    linear = Linear(points_list, center_point)
    center_distance = linear.calculate_distance()

    result = mea_distance(base_distance, bottom_distance, center_distance)

    print(result)







