#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 10:46
# @Author  : Scheaven
# @File    : test_gpu.py
# @description: 
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1" #设置CPU
# 加上下面一行就可以使用 个gpu了
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" #多GPU设置哪些GPU参与运算
# 设置gpu根据需求调用显存
config = tf.ConfigProto(allow_soft_placement=True)  
config.gpu_options.allow_growth=True   
session = tf.Session(config=config)
KTF.set_session(session)


with tf.Session(config=config) as sess:
    with tf.device("/gpu:10"):
        a = tf.placeholder(tf.int16)
        b = tf.placeholder(tf.int16)
        adda = tf.add(a, b)
        print ("add:%i" % sess.run(adda,feed_dict={a:10,b:5}))


import os
from tensorflow.python.client import device_lib
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"

if __name__ == "__main__":
    print(device_lib.list_local_devices())