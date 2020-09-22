import os
import xml.dom.minidom
import cv2 as cv
import random
 
ImgPath = '/home/disk1/s_dataset/10_darknet_hat_data/JPEGImages/'
AnnoPath = '/home/disk1/s_dataset/10_darknet_hat_data/Annotations_all/'

sava_txt_path = 'annotation/'
ftest = open(sava_txt_path + '/test.txt', 'w')
ftrain = open(sava_txt_path + '/train.txt', 'w')
fval = open(sava_txt_path + '/val.txt', 'w')

trainval_percent = 0.9  
train_percent = 0.8     


imagelist = os.listdir(ImgPath)
xml_num = len(imagelist)
xml_rang = range(xml_num)
trainVal_num = int(xml_num*trainval_percent)
train_num = int(trainVal_num*train_percent)

trainVal_rang = random.sample(xml_rang, trainVal_num)
train_rang = random.sample(trainVal_rang, train_num)

random_i = -1

for image in imagelist:    
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image
    xmlfile = AnnoPath + image_pre + '.xml'
    print(image)
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
    print(filename)
    #得到标签名为object的信息
    objectlist = collection.getElementsByTagName("object")
    line_obj = image

    for objects in objectlist:
        #每个object中得到子标签名为name的信息
        namelist = objects.getElementsByTagName('name')
        #通过此语句得到具体的某个name的值
        objectname = namelist[0].childNodes[0].data
 
        print("objectname-----",objectname)
        bndbox = objects.getElementsByTagName('bndbox')
        for box in bndbox:
            x1_list = box.getElementsByTagName('xmin')
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)

            if objectname == "hat":
                # print("hat-----")
                # cv.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), thickness=1)
                # cv.putText(img, objectname, (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0),
                #            thickness=2)
                line_obj += " " +str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+str(0)
            elif objectname == "head":
                print("---head-----")
                line_obj += " " +str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+str(1)
                # cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), thickness=1)
                # cv.putText(img, objectname, (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
                #            thickness=2)

    print("--------", line_obj)
    line_obj += "\n"
    random_i+=1
    if random_i in trainVal_rang:
        if random_i in train_rang:
            ftrain.write(line_obj)
        else:
            fval.write(line_obj)
    else:
        ftest.write(line_obj)
        # cv.imwrite("/home/newbee/CODEs/CSRNet-pytorch-master/havatry.jpg", img)   #save picture
