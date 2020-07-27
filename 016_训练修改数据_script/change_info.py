# -*- coding:utf-8 -*-
import glob
import os
import cv2 as cv
import xml.etree.ElementTree as ET
from random import randint

'''
更改数据中的name名字
'''

WSI_MASK_PATH = '/home/disk1/s_dataset/10_darknet_hat_data/'
IMAGE_PATH = 'JPEGImages'
XML_PATH = 'Annotations'
BACKGROUND_IMAGE_PATH = '/home/disk1/s_dataset/10_darknet_hat_data/background_images'
SIMULATION = 'VOCNEW'


# width,height为最终图片参数
def update_xml(xml_file, xml_save_path):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
        member.find('name').text='human_head'
            # cv.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 255, 0), thickness=1)
            # cv.putText(img, "head", (xmin, ymin), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0),
            #                thickness=2)
        tree.write(xml_save_path)

if not os.path.exists(SIMULATION):
    os.makedirs(SIMULATION +"/"+ IMAGE_PATH)
    os.makedirs(SIMULATION +"/"+ XML_PATH)

s_xml_path = WSI_MASK_PATH + XML_PATH

files= os.listdir(s_xml_path) #得到文件夹下的所有文件名称
n_name = 0;
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开

        xml_path = s_xml_path+"/"+file
        n_name +=1

        xml_save_path = SIMULATION + '/' + XML_PATH + '/' + file

        a_flag = update_xml(xml_path, xml_save_path)

        # cv.imshow("res", res)
        # cv.waitKey(0)
