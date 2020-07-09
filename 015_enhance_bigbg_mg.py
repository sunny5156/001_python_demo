# -*- coding:utf-8 -*-
import glob
import os
import cv2 as cv
import xml.etree.ElementTree as ET
from random import randint

WSI_MASK_PATH = '/home/disk1/s_dataset/10_darknet_hat_data/'
IMAGE_PATH = 'JPEGImages'
XML_PATH = 'Annotations'
BACKGROUND_IMAGE_PATH = '/home/disk1/s_dataset/10_darknet_hat_data/background_images'
SIMULATION = 'VOCNEW'


# width,height为最终图片参数
def update_xml(xml_file, xml_save_path, width, height, zoom_rate, orig_row, orig_col,res):
    print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    size.find('width').text = str(width)
    size.find('height').text = str(height)
    flag =0 
    img=res
    for member in root.findall('object'):
        bndbox = member.find('bndbox')
        if member.find('name').text=='hat':
            xmin = int(int(bndbox.find('xmin').text) * zoom_rate)
            ymin = int(int(bndbox.find('ymin').text) * zoom_rate)
            xmax = int(int(bndbox.find('xmax').text) * zoom_rate)
            ymax = int(int(bndbox.find('ymax').text) * zoom_rate)
            # print("o1", xmin, ymin, xmax, ymax)
            bndbox.find('xmin').text = str(xmin + orig_col)
            bndbox.find('ymin').text = str(ymin + orig_row)
            bndbox.find('xmax').text = str(xmax + orig_col)
            bndbox.find('ymax').text = str(ymax + orig_row)
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            flag = 1
            # cv.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 255, 0), thickness=1)
            # cv.putText(img, "hat", (xmin, ymin), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0),
            #                thickness=2)
        else:
            xmin = int(int(bndbox.find('xmin').text) * zoom_rate)
            ymin = int(int(bndbox.find('ymin').text) * zoom_rate)
            xmax = int(int(bndbox.find('xmax').text) * zoom_rate)
            ymax = int(int(bndbox.find('ymax').text) * zoom_rate)
            # print("o1", xmin, ymin, xmax, ymax)
            bndbox.find('xmin').text = str(xmin + orig_col)
            bndbox.find('ymin').text = str(ymin + orig_row)
            bndbox.find('xmax').text = str(xmax + orig_col)
            bndbox.find('ymax').text = str(ymax + orig_row)
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            flag = 0
            # cv.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 255, 0), thickness=1)
            # cv.putText(img, "head", (xmin, ymin), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0),
            #                thickness=2)

    if flag:
        # cv.imshow('head', img)
        # cv.waitKey(100)
        tree.write(xml_save_path)


    return flag      


def get_random_background_image(background_path):
    file_list = os.listdir(background_path)
    total_num = len(file_list) - 1
    idx = randint(0, total_num)
    # print("idx: ",idx)
    image_path = file_list[idx]
    picture_path = os.path.join(os.path.abspath(background_path), image_path)
    return picture_path


def merge_picture(src_img, dst_img):
    src_rows, src_cols, _ = src_img.shape
    dst_rows, dst_cols, _ = dst_img.shape
    print(dst_cols,":",src_cols,":",dst_cols - src_cols - 1)
    print(dst_rows,":",src_rows,":",dst_rows - src_rows - 1)
    try:
        tl_left = randint(0, dst_cols - src_cols - 30)
        tl_top = randint(0, dst_rows - src_rows - 30)
        br_right = tl_left + src_cols
        br_bottom = tl_top + src_rows
        dst_img[tl_top:br_bottom, tl_left:br_right] = src_img
    except Exception as e:
        return dst_img, -1, -1
       
    return dst_img, tl_left, tl_top


if not os.path.exists(SIMULATION):
    os.makedirs(SIMULATION +"/"+ IMAGE_PATH)
    os.makedirs(SIMULATION +"/"+ XML_PATH)

s_xml_path = WSI_MASK_PATH + XML_PATH

files= os.listdir(s_xml_path) #得到文件夹下的所有文件名称
n_name = 0;
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        SZOOM_RATE = randint(6, 8) / 10
        ZOOM_RATE = randint(8, 9) / 10
        jpg_file = WSI_MASK_PATH+IMAGE_PATH+"/"+str(file.split(".")[0]) +  ".jpg"
        jpg_save_name = str(2742+n_name) +  ".jpg"

        xml_path = s_xml_path+"/"+file
        xml_save_name = str(2742+n_name) + ".xml"
        n_name +=1

        xml_save_path = SIMULATION + '/' + XML_PATH + '/' + xml_save_name
        bgi = get_random_background_image(BACKGROUND_IMAGE_PATH)
        img_bgi = cv.imread(bgi)
        # print(ZOOM_RATE)
        img_original = cv.imread(jpg_file)
        try:
            h, w, _ = img_original.shape
            if h<800:
                NEW_H = int(h)
                NEW_W = int(w)
                ZOOM_RATE = 1
            elif h<1000:
                NEW_H = int(h * ZOOM_RATE)
                NEW_W = int(w * ZOOM_RATE)
            elif h>1200:
                NEW_H = int(h * SZOOM_RATE)
                NEW_W = int(w * SZOOM_RATE)
                ZOOM_RATE = SZOOM_RATE

        except Exception as e:
            continue
        src = cv.resize(img_original, (NEW_W, NEW_H))
        dst = cv.imread(get_random_background_image(BACKGROUND_IMAGE_PATH))
        h, w, _ = dst.shape
        res, col, row = merge_picture(src, dst)        
        if col == -1 or row ==-1:
            print("================")
            continue

        a_flag = update_xml(xml_path, xml_save_path, w, h, ZOOM_RATE, row, col,res)

        if a_flag:
            cv.imwrite(SIMULATION + '/' + IMAGE_PATH + '/' + jpg_save_name, res)
        # cv.imshow("res", res)
        # cv.waitKey(0)
