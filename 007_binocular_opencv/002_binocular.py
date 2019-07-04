#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
# cap1 = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
cap2 = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
 
while True:
    # ret1, frame1 = cap1.read()
    et2, frame2 = cap2.read()
    # cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cap1.release()
cv2.destroyAllWindows()