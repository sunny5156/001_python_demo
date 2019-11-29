#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 14:50
# @Author  : Scheaven
# @File    :  piont_region.py
# @description:  判断点和多边形区域的关系

def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        print(i, poly[i], j, poly[j])
        if ((poly[i][0] <= pt[0] and pt[0] < poly[j][0]) or (
                poly[j][0] <= pt[0] and pt[0] < poly[i][0])):
            if (pt[1] < (poly[j][1] - poly[i][1]) * (pt[0] - poly[i][0]) / (
                poly[j][0] - poly[i][0]) + poly[i][1]):
                c = not c
        j = i
    return c

if __name__ == '__main__':
    abc = [[1, 1], [1, 4], [3, 7], [4, 4], [4, 1]]
    print(isInsidePolygon([1, 3], abc))