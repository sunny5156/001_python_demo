import os
import xml.dom.minidom
import cv2 as cv
import random
import re

ImgPath = '/home/disk1/s_dataset/00_tracking_data/JPEGImages/'
AnnoPath = '/home/disk1/s_dataset/00_tracking_data/Annotations/'

def get_random(ran_len):
    ran_cord="";
    for x in range(ran_len):
        ran_cord += str(random.randint(0, 9))
    return ran_cord


imagelist = os.listdir(ImgPath)
for image in imagelist:
 
    image_pre, ext = os.path.splitext(image)
    if re.search(r"\W",image_pre) != None:

        imgfile = ImgPath + image
        xmlfile = AnnoPath + image_pre + '.xml'
        if not os.path.exists(xmlfile):
            # os.remove(image)
            continue
     
        #打开xml文档
        DOMTree = xml.dom.minidom.parse(xmlfile)
        #得到文档元素对象
        collection = DOMTree.documentElement
        #读取图片
        img = cv.imread(imgfile)
     
        filenamelist = collection.getElementsByTagName("filename")
        filename = filenamelist[0].childNodes[0].data
        src = os.path.join(os.path.abspath(ImgPath), image);
        name = get_random(15)
        n_filename =  name + '.jpg'
        n_xml_filename = name  + '.xml'
        filenamelist[0].childNodes[0].data
        dst = os.path.join(os.path.abspath(ImgPath), n_filename)#处理后的格式也为jpg格式的，当然这里可以改成png格式
        xml_dst = os.path.join(os.path.abspath(AnnoPath), n_xml_filename)#处理后的格式也为jpg格式的，当然这里可以改成png格式
        filenamelist[0].childNodes[0].data = n_filename
        try:
            print(src,"==========",dst)
            os.rename(src, dst)
            DOMTree.write(xmlfile)

            #os.remove(xmlfile)
            os.rename(xmlfile, xml_dst)
            print('converting %s to %s ...' % (src, dst))
            print('converting %s to %s ...' % (xmlfile, xml_dst))
        except Exception as e:
            continue





# 备用版本
# import os
# import xml.dom.minidom
# from xml.etree import ElementTree as ET
# import cv2 as cv
# import random
# import re

# ImgPath = '/data/disk1/project/01_py_project/03_Detection/ssd_mobiledet-main/test-data/images/'
# AnnoPath = '/data/disk1/project/01_py_project/03_Detection/ssd_mobiledet-main/test-data/annotations/'

# def get_random(ran_len):
#     ran_cord="";
#     for x in range(ran_len):
#         ran_cord += str(random.randint(0, 9))
#     return ran_cord


# imagelist = os.listdir(ImgPath)
# for image in imagelist:

#     image_pre, ext = os.path.splitext(image)
#     # if re.search(r"\W",image_pre) != None:

#     imgfile = ImgPath + image
#     xmlfile = AnnoPath + image_pre + '.xml'
#     if not os.path.exists(xmlfile):
#         # os.remove(image)
#         continue

#     #打开xml文档
#     DOMTree = ET.parse(xmlfile)
#     #得到文档元素对象
#     # collection = DOMTree.documentElement
#     root = DOMTree.getroot()
#     #读取图片
#     img = cv.imread(imgfile)
#     filenamelist = root.find("filename")
#     # filenamelist = collection.getElementsByTagName("filename")
#     filename = filenamelist.text
#     print(filename)
#     src = os.path.join(os.path.abspath(ImgPath), image);
#     name = get_random(15)
#     n_filename =  name + '.jpg'
#     n_xml_filename = name  + '.xml'
#     # filenamelist[0].childNodes[0].data
#     dst = os.path.join(os.path.abspath(ImgPath), n_filename)#处理后的格式也为jpg格式的，当然这里可以改成png格式
#     xml_dst = os.path.join(os.path.abspath(AnnoPath), n_xml_filename)#处理后的格式也为jpg格式的，当然这里可以改成png格式
#     filenamelist.text = n_filename
#     try:
#         os.rename(src, dst)
#         print(src,"==========",dst)
#         DOMTree.write(xmlfile, encoding="utf-8")
#         print(src,"==??????===",xml_dst)
#         #os.remove(xmlfile)
#         os.rename(xmlfile, xml_dst)
#         print(src,"==??????===",xml_dst)
#         print('converting %s to %s ...' % (src, dst))
#         print('converting %s to %s ...' % (xmlfile, xml_dst))
#     except Exception as e:
#         print(e)
#         continue
