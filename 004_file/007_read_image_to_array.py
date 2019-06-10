#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:18
# @Author  : Scheaven
# @File    : 007_read_subfolder_file.py
# @description: Read files in folders and subfolders,and read the classification of subfolder names.
from imutils import paths
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
import cv2
import random,os
import numpy as np


def read_and_process_image(data_dir,width=32, height=32, channels=3, preprocess=False):
    
    train_classes= [data_dir +  i for i in os.listdir(data_dir) ]
    train_images = []
    for train_class in train_classes:
        train_images= train_images + [train_class + "/" + i for i in os.listdir(train_class)]
    
    random.shuffle(train_images)
    
    def read_image(file_path, preprocess):
        img = image.load_img(file_path, target_size=(height, width))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        
        if preprocess:
            x = preprocess_input(x)
        return x
    
    def prep_data(images, proprocess):
        count = len(images)
        data = np.ndarray((count, channels, height, width), dtype = np.float32)
        
        for i, image_file in enumerate(images):
            image = read_image(image_file, preprocess)
            data[i] = image
        
        return data
    
    def read_labels(file_path):
        labels = []
        label = 0
        for i in file_path:
            if 'cat' in str(i):
                label = 1
            elif 'dog' in str(i):
                label = 0
            labels.append(label)
        return labels
    
    X = prep_data(train_images, preprocess)
    labels = read_labels(train_images)
    
    assert X.shape[0] == len(labels)
    
    print("Train shape: {}".format(X.shape))
    
    return X, labels


if __name__ == '__main__':
    path = "./images/"
    # 不可 (x_t,y_t) = load_image_date(path)
    # generator的打印方式如下
    read_and_process_image(path)