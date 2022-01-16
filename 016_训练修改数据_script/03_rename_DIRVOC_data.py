import os
from os import path
import xml.dom.minidom
from xml.etree import ElementTree as ET
import cv2 as cv
import random
import re

def get_random(ran_len):
    ran_cord="";
    for x in range(ran_len):
        ran_cord += str(random.randint(0, 9))
    return ran_cord

def updete_xml(n_filename, xmlfile, n_xml_file):
        #打开xml文档
        # DOMTree = xml.dom.minidom.parse(xmlfile)
        DOMTree = ET.parse(xmlfile)
        #得到文档元素对象
        # collection = DOMTree.documentElement
        root = DOMTree.getroot()
       
        filenamelist = root.find("filename")
        filenamelist.text = n_filename+".jpg"
        try:
            # DOMTree.write(n_xml_file)
            DOMTree.write(n_xml_file, encoding="utf-8")
            #os.remove(xmlfile)
            # os.rename(xmlfile, n_xml_file)
            # print('converting %s to %s ...' % (src, dst))
            # print('converting %s to %s ...' % (xmlfile, xml_dst))
        except Exception as e:
            print("e",e)

def update_img(n_filename, imgfile, n_imgfile):
    img = cv.imread(imgfile)
    cv.imwrite(path.join(n_imgfile,n_filename), img)

save_xml = '/home/scheaven/xytest/dis_data/Annotations'
save_img = '/home/scheaven/xytest/dis_data/JPEGImages'

def scaner_file(dir_path):
    files = os.listdir(dir_path)
    for f in files:
        cur_path = path.join(dir_path,f)
        if path.isfile(cur_path):
            bool = f.endswith(".xml")
            if(bool):
                print(path.abspath(cur_path))
                # print(dir_path)
                path_list = dir_path.split("/")
                path_list.pop(-1)
                img_name = path.splitext(f)[0]
                img_path = path.join("/".join(path_list), "image",img_name+".jpg")
                n_name = get_random(6)

                updete_xml(n_name, cur_path, path.join(save_xml,n_name+".xml" ))
                update_img(n_name + ".jpg",img_path, save_img)


        elif path.isdir(cur_path):
            scaner_file(cur_path)
        else:
            print("error:")


if not path.exists(save_xml):
    print("-----------")
    os.makedirs(save_img)
    os.makedirs(save_xml)
scaner_file("/home/scheaven/xytest/origin")
