#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 20:08
# @Author  : Scheaven
# @File    : test002.py
# @description: 

import cv2
import numpy as np
path = '/home/basic/workspace/Scheaven/06_action_recognition/slowfast/'
matimage = cv2.imread(path + 'test.png')

#matimagenew = np.zeros((matimage.shape[0],matimage.shape[1],3))
matimagenew = matimage-matimage
watermark_template_filename = path + 'logo.png'
matlogo = cv2.imread(watermark_template_filename)

matimagenew[0:0+matlogo.shape[0],0:0+matlogo.shape[1]] = matlogo
imagenew = cv2.addWeighted(matimage,1,matimagenew,1,1)
savepath = path + 'test_logo.png'
cv2.imwrite(savepath,imagenew)