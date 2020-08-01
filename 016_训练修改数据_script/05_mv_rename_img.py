import os
import xml.dom.minidom
import cv2 as cv
import random
import re
import string
import shutil

ImgPath = '/home/disk1/s_dataset/01_maskFace/JPEGImages/'
dstImgPath = '/home/disk1/s_dataset/00_tracking_data/JPEGImages/'

def get_random(ran_len):
    candidate = string.ascii_letters+string.digits
    ran_cord = "".join(random.sample(candidate,ran_len));
    return ran_cord


imagelist = os.listdir(ImgPath)
for image in imagelist:
 
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image
    print(imgfile)
 
    #读取图片
    name = get_random(20)

    n_filename =  name + '.jpg'
    dst = os.path.join(os.path.abspath(dstImgPath), n_filename)#处理后的格式也为jpg格式的，当然这里可以改成png格式
    try:
        shutil.copyfile(imgfile,dst)
        print(dst)
        # os.rename(src,dst)
    except Exception as e:
        continue

