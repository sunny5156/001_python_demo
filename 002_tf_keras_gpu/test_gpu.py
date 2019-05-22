#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 10:46
# @Author  : Scheaven
# @File    : test_gpu.py
# @description: 
import tensorflow as tf
# 加上下面一行就可以使用 个gpu了
config = tf.ConfigProto(allow_soft_placement=True)
# 这一行设置 gpu 随使用增长，我一般都会加上
config.gpu_options.allow_growth = True
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