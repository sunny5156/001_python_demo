#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 19:22
# @Author  : Scheaven
# @File    : S_KalmanFilter.py
# @description: Personal implementation of a simple kalman filter
import numpy as np
import pylab

class KalmanFileer():
    def __init__(self):
        # self.data_len = n
        self.R = 0.1 ** 2  # estimate of measurement variance, change to see effect
        self.P = 1.0
        self.Q = 1e-5  # process variance
        self.Z = 0.0  # process variance


    def calman_predict(self,lastx):
        xhatminus = lastx  # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
        Pminus = self.P+ self.Q

        return xhatminus, Pminus

    def claman_update(self,Pminus,xhatminus):
        K = Pminus / (Pminus + self.R)  # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
        xhat = xhatminus + K * (self.Z - xhatminus)  # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
        self.P = (1 - K) * Pminus  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1

        return xhat

    def calman_filter(self,oriam,lastx):
        self.Z = oriam
        xhatminus, Pminus = self.calman_predict(lastx)
        return self.claman_update(Pminus,xhatminus),Pminus


if __name__ == '__main__':
    amhat_list=[]
    Pminus_list=[]
    x = -0.37727  # truth value (typo in example at top of p. 13 calls this z)真实值
    n_iter = 50
    last_am = 0.0
    amhat_list.append(last_am)
    sz = (n_iter,)  # size of array
    amori_list = np.random.normal(x, 0.1, size=sz)  # observations (normal about x, sigma=0.1)观测值
    cf = KalmanFileer()
    for k in range(0, n_iter):
        last_am,p = cf.calman_filter(amori_list[k],last_am)
        amhat_list.append(last_am)
        Pminus_list.append(p)

    pylab.figure()
    pylab.plot(amori_list, 'k+', label='noisy measurements')  # 观测值
    pylab.plot(amhat_list, 'b-', label='a posteri estimate')  # 滤波估计值
    pylab.axhline(x, color='g', label='truth value')  # 真实值
    pylab.legend()
    pylab.xlabel('Iteration')
    pylab.ylabel('Voltage')

    pylab.figure()
    valid_iter = range(1, n_iter)  # Pminus not valid at step 0
    pylab.plot(Pminus_list, 'b-', label='a priori error estimate')
    pylab.xlabel('Iteration')
    pylab.ylabel('$(Voltage)^2$')
    pylab.setp(pylab.gca(), 'ylim', [0, .01])
    pylab.show()