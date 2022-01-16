import os
import random

trainval_percent = 0.7  # 可以自己设置
train_percent = 0.8  # 可以自己设置

xmlfilepath = f"/home/disk1/s_dataset/10_darknet_hat_data/Annotations"  # 地址填自己的
txtsavepath = f"/home/disk1/s_dataset/10_darknet_hat_data/ImageSets/Main"
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)


def create_onlyName():
    total_xml = os.listdir(xmlfilepath)
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open(txtsavepath + '/trainval.txt', 'w')
    ftest = open(txtsavepath + '/test.txt', 'w')
    ftrain = open(txtsavepath + '/train.txt', 'w')
    fval = open(txtsavepath + '/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)


    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()

def create_PathName():
    total_xml = os.listdir(xmlfilepath)
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open(txtsavepath + '/trainval.txt', 'w')
    ftest = open(txtsavepath + '/test.txt', 'w')
    ftrain = open(txtsavepath + '/train.txt', 'w')
    fval = open(txtsavepath + '/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + ".jpg" + '\n'
        if i in trainval:
            ftrainval.write(os.path.join(imgfilepath,name))
            if i in train:
                ftrain.write(os.path.join(imgfilepath,name))
            else:
                fval.write(os.path.join(imgfilepath,name))
        else:
            ftest.write(os.path.join(imgfilepath,name))
    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()

create_onlyName()
print('Well finshed')
