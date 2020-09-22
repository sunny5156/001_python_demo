import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import cv2

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["person", "down", "run", "hat", "head", "face_mask", "face", "smoke", "no_smoke"]


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open('/home/disk1/s_dataset/04_VOC_Person/Annotations/%s.xml'%(image_id))
    out_file = open('/home/disk1/s_dataset/04_VOC_Person/labels/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    print(image_id)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    if w==0 or h==0 :
        h,w,_ = cv2.imread('/home/disk1/s_dataset/04_VOC_Person/JPEGImages/'+str(image_id)+".jpg").shape;
        print(w,h,"===============================",image_id)

    print(w,h,image_id)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('/home/disk1/s_dataset/04_VOC_Person/labels/'):
        os.makedirs('/home/disk1/s_dataset/04_VOC_Person/labels/')
    image_ids = open('/home/disk1/s_dataset/04_VOC_Person/ImageSets/Main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('/home/disk1/s_dataset/04_VOC_Person/JPEGImages/%s.jpg\n'%(image_id))
        convert_annotation(year, image_id)
    list_file.close()

#os.system("cat 2007_train.txt 2007_val.txt > 2007_train.txt")
#os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt > 2007_train.all.txt")

