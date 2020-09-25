Makefile是编译darknet yolo的Makefile文件
编译darknet 注意事项：
1、头部设置
GPU=1
CUDNN=1
CUDNN_HALF=1
OPENCV=1
AVX=0
OPENMP=1
LIBSO=0
ZED_CAMERA=0
ZED_CAMERA_v2_8=0




运行  ./darknet detect cfg/yolov4-one.cfg ./backup/yolov4-one_best.weights data/dog.jpg

运行  ./darknet detector demo ./data/coco.data ./cfg/yolov3.cfg ../01_darknet/backup/yolov3_final.weights 01hand.mp4

 then open URL http://ip-address:8090 in Chrome/Firefox browser)

./darknet detector train data/head.data ./cfg/yolov4-one.cfg ./model/yolov4-head_final.weights -dont_show -mjpeg_port 8090 -map -gpus 4,5,6

./darknet detector train data/person.data ./cfg/yolov4-person.cfg ../darknet/model/yolov4.conv.137 -dont_show -mjpeg_port 8090 -map -gpus 4,5,6,7


./darknet detector train /home/disk1/Scheaven/start-yolov4/cfg/coco/coco.data /home/disk1/Scheaven/start-yolov4/cfg/coco/yolov4.cfg ./model_dump/yolov4.conv.137 -dont_show -mjpeg_port 8091 -map -gpus 4,5,6,7 -show_imgs

用 -show_imgs参数验证数据集是否正确
注意coco 数据集训练，标签位置是个大问题


./darknet detector train data/coco.data ./cfg/yolov4.cfg ./backup/yolov4.conv.137 -dont_show -mjpeg_port 8090 -map -gpus 6,7




make 后报错修改
./darknet

error while loading shared libraries: libcudart.so.10.0: cannot open shared object file: No such file or directory

在命令行临时运行一下命令
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64

opencv改成自己的路径
#LDFLAGS+= `pkg-config --libs opencv4 2> /dev/null || pkg-config --libs opencv`
#COMMON+= `pkg-config --cflags opencv4 2> /dev/null || pkg-config --cflags opencv`
CFLAGS+= -I/home/disk1/s_opt/opencv/opencv2.4.9/include
LDFLAGS+= -L/home/disk1/s_opt/opencv/opencv2.4.9/lib -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_video





操作步骤：
1、制作数据
2、数据文件重命名（可选做） rename_VOC_data.py
3、数据放缩（添加大背景）enhance_data.py
4、生成ImageSet中的train.txt test.txt val.txt get_inageSet.py
5、生成data文件夹下的2007_train.txt等以及生成数据集下的labels等 07_label_utils.py（需要根据实际修改分类 修改的文件包括obj.data、obj.names、obj_label.py）
6、修改对应的cfg文件(width/height ；batch； 三个yolo 附近的class分类 filters = （class+ 5）*3；
 max_batches to (classes*2000 but not less than number of training images, but not less than number of training images and not less than 6000), f.e. max_batches=6000 if you train for 3 classes
change line steps to 80% and 90% of max_batches, f.e. steps=4800,5400)
7、修改obj.name / obj.data 中对应的文件和分类



coco数据集训练
运行make_txt脚本生成TXT文件











darknet  使用概述 （https://blog.csdn.net/u010122972/article/details/83541978）


优点
Darknet是一个比较小众的深度学习框架，没有社区，主要靠作者团队维护，所以推广较弱，用的人不多。而且由于维护人员有限，功能也不如tensorflow等框架那么强大，但是该框架还是有一些独有的优点：
1.易于安装：在makefile里面选择自己需要的附加项（cuda，cudnn，opencv等）直接make即可，几分钟完成安装；
2.没有任何依赖项：整个框架都用C语言进行编写，可以不依赖任何库，连opencv作者都编写了可以对其进行替代的函数；
3.结构明晰，源代码查看、修改方便：其框架的基础文件都在src文件夹，而定义的一些检测、分类函数则在example文件夹，可根据需要直接对源代码进行查看和修改；
4.友好python接口：虽然darknet使用c语言进行编写，但是也提供了python的接口，通过python函数，能够使用python直接对训练好的.weight格式的模型进行调用；
5.易于移植：该框架部署到机器本地十分简单，且可以根据机器情况，使用cpu和gpu，特别是检测识别任务的本地端部署，darknet会显得异常方便。

代码结构
下图是darknet源代码下载解压后文件夹的分布情况：

1.cfg文件夹内是一些模型的架构，每个cfg文件类似与caffe的prototxt文件，通过该文件定义的整个模型的架构
2.data文件夹内放置了一些label文件，如coco9k的类别名等，和一些样例图（该文件夹主要为演示用，或者是直接训练coco等对应数据集时有用，如果要用自己的数据自行训练，该文件夹内的东西都不是我们需要的）
3.src文件夹内全是最底层的框架定义文件，所有层的定义等最基本的函数全部在该文件夹内，可以理解为该文件夹就是框架的源码；
4.examples文件夹是更为高层的一些函数，如检测函数，识别函数等，这些函数直接调用了底层的函数，我们经常使用的就是example中的函数；
5.include文件夹，顾名思义，存放头文件的地方；
6.python文件夹里是使用python对模型的调用方法，基本都在darknet.py中。当然，要实现python的调用，还需要用到darknet的动态库libdarknet.so，这个动态库稍后再介绍；
7.scripts文件夹中是一些脚本，如下载coco数据集，将voc格式的数据集转换为训练所需格式的脚本等
8.除了license文件，剩下的就是Makefile文件，如下图，在问价开头有一些选项，把你需要使用的选项设为1即可


安装
1.点开Makefile，将需要的选项设置为1，如图，使用GPU和CUDNN

2.打开终端，进入到darknet文件夹根目录，输入make，开始编译
3.几分钟后编译完成，文件夹中会多出一些文件夹和文件，obj文件中存放了编译过程中的.o文件，其他的几个空文件夹也不需要太大关注，这里最重要的就是三个：名为darknet的exe文件，名为libdarknet.a的静态链接库和名为libdarknet.so的动态链接库。如果直接在本地进行模型调用尝试，可以直接运行darknet这个exe文件，如果需要移植调用，则需要用到libdarknet.so这个动态链接库，这个动态链接库中只包含了src文件夹中定义的框架基础函数，没有包含examples中的高层函数，所以调用过程中需要自己去定义检测函数

检测
运行如下代码

./darknet detector test data/detect.data data/yolov3.cfg data/yolov3.weight
1
其中./darknet表示运行编译生成的darknet.exe文件，darknet.exe首先调用example文件夹下的darknet.c，该文件中的main函数需要预定义参数，detector即为预定义参数，如下代码

else if (0 == strcmp(argv[1], "detector")){
        run_detector(argc, argv);
1
2
由‘detector’转而调用run_detector，run_detector存在于example文件夹下的detector.c中，再根据预定义参数，确定是调用检测函数，训练函数还是验证函数：

if(0==strcmp(argv[2], "test")) test_detector(datacfg, cfg, weights, filename, thresh, hier_thresh, outfile, fullscreen);
else if(0==strcmp(argv[2], "train")) train_detector(datacfg, cfg, weights, gpus, ngpus, clear);
else if(0==strcmp(argv[2], "valid")) validate_detector(datacfg, cfg, weights, outfile);
else if(0==strcmp(argv[2], "valid2")) validate_detector_flip(datacfg, cfg, weights, outfile);
else if(0==strcmp(argv[2], "recall")) validate_detector_recall(cfg, weights);
else if(0==strcmp(argv[2], "demo")) 



其中test表示检测，train表示训练，valid表示验证，recall表示测试其召回率，demo为调用摄像头的实时检测

命令最后的三个参数表示运行需要的文件，.data文件记录了模型检测的类别，类名文件等，如下：

classes= 1
train  = /media/seven/yolov3/data/plate2/train.list
#valid = data/coco_val_5k.list
names = data/plate/plate.names
backup = /media/seven/yolov3/data/plate2/models
#eval=coco


class表示检测类别，train为训练中需要用到的训练数据的列表，valid为验证集列表，names为检测类别的名称，backup为训练中用到的存放训练模型的路径

.cfg文件定义了模型结构，而.weight文件为调用的模型权重文件

运行以上命令，会在终端得到如下提示：

Enter Image Path: 
1
直接在终端输入图像的路径，就可以对该图像进行检测，并在darknet的根目录生成名为predictions.png的检测结果，如图：


分类
分类和检测类似，调用命令如下：
./darknet classifier predict classify.data classify.cfg classify.weights
1
与检测同理，./darknet运行darknet.exe，并调用example中的darknet.c文件，通过classfier调用classifier.c中的run_classifier函数：

else if (0 == strcmp(argv[1], "classifier")){
        run_classifier(argc, argv);
1
2
并通过predict进而调用predict_classifier函数：

 if(0==strcmp(argv[2], "predict")) predict_classifier(data, cfg, weights, filename, top);
 else if(0==strcmp(argv[2], "fout")) file_output_classifier(data, cfg, weights, filename);
 else if(0==strcmp(argv[2], "try")) try_classifier(data, cfg, weights, filename, atoi(layer_s));
 else if(0==strcmp(argv[2], "train")) train_classifier(data, cfg, weights, gpus, ngpus, clear);
 else if(0==strcmp(argv[2], "demo")) demo_classifier(data, cfg, weights, cam_index, filename);
 ...


而classify.data，classify.cfg，classify.weights分别表示分类对应的.data文件，模型定义cfg文件和模型权重.weights文件。

训练
检测模型的训练：
（1）数据准备：
首先，你需要将数据的groundtruth转化为darknet需要的格式，如果你的gt为voc格式的xml，可以通过如下脚本进行转换
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
classes = ["plate"]#类别改为自己需要检测的所有类别
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
def convert_annotation(image_id):
    in_file = open(xml_path)#与图片对应的xml文件所在的地址
    out_file = open(txt_save_path,'w') #与此xml对应的转换后的txt，这个txt的保存完整路径
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')  #访问size标签的数据
    w = int(size.find('width').text)#读取size标签中宽度的数据
    h = int(size.find('height').text)#读取size标签中高度的数据

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes :#or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')   #访问boundbox标签的数据并进行处理，都按yolo自带的代码来，没有改动
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


上面的代码需要自行设置xml_path和txt_save_path
从上面的代码可以看到，对于object的位置x_min,x_max,y_min,y_max，先求得其中心点坐标center_x,center_y以及位置框的长宽width_rect,height_rect，再将这四个值分别除以长宽以将数据归一化，如果不是voc格式的数据可以按照这样的思路进行类似处理
如果是voc格式的数据可以参照我之前的博客进行一步一步的处理darknet用自己的数据进行训练
按照上面的流程，每张图像都生成了对应的txt文件来保存其归一化后的位置信息，如下图对应生成的txt如下：


0 0.250925925926 0.576388888889 0.1 0.0263888888889
0 0.485185185185 0.578125 0.0685185185185 0.0201388888889
1
2
图中共有车牌两个，每行保存一个车牌的信息，第一个0表示检测object的label，因为我只有一类，所以都是0
后面的四位即为归一化后的中心点坐标和位置框的长和宽
最后将图像和对应txt的文件名统一，并拷贝到同一个文件夹（a.jpg对应的txt为a.txt），如图：


注意，txt和对应jpg文件的名称除了最后.jpg,.txt的后缀不一样，其他的必须完全一样，且需要保存在同一文件夹，训练过程中会直接将a.jpg的名称替换为a.txt来寻找该图像对应的gt。对应的gt文件也不一定必须是txt格式，如果不是txt格式可以去源码中将这部分代码进行修改，将.jpg替换为你需要的格式后缀

（2）.data文件准备
前面已经贴过.data的图，训练的时候必须的项目有“class”，“train”，“backup”。“names”最好也设置上，方便以后调用。
“class”表示你要检测的类别个数，如检测类别为20则class=20
“backup”表示训练过程中的缓存和保存的模型。训练过程中，会在该路径下生成一个后缀为.backup的文件，该文件每100个step将模型更新一遍，以防止训练忽然终端而没有保存模型。并且，训练保存的模型也会存在该路径下。默认情况下，每10000step还是多少（记不太清了，我自己修改过）会保存一个模型，命名为yolov3_迭代次数.weights，最终训练完成还会保存一个yolov3_final.weights。这些模型都会保存在backup路径下
“names”为保存检测object名称的路径，names=plate.names
“train”为你训练集的list路径，如train=data/trainlist.txt，trainlist.txt中保存了所有训练集图像的路径，如下图

可以通过如下命令直接生成该文件：

find image_path -name \*.jpg > trainlist.txt
1
image_path为你数据集的路径

（3）.cfg文件准备
如果要调用yolo v3，可以直接使用cfg文件夹下的yolov3.cfg，但是需要做如下几个修改：
首先，将最上方的

# Testing
batch=1
subdivisions=1
# Training
# batch=64
# subdivisions=16

修改为

# Testing
#batch=1
#subdivisions=1
# Training
batch=64
subdivisions=16

其中batch表示batchsize，而subdivisions是为了解决想要大batchsize而显存又不够的情况，每次代码只读取batchsize/subdivisions 个图像，如图中设置为64/16=4，但是会将16次的结果也就是64张图的结果，作为一个batch来统一处理
（调用的时候再将testing部分解除注释，并将train部分注释）

然后，根据自己检测的类别，将每个[yolo]（共有三个[yolo]） 下方的classes修改为自己需要检测的类别，如果只检测一类则classes=1
然后将每个[yolo] 上方的第一个filters的值进行修改，计算方式为（5+classes）*3,如果classes为1，则为18，修改前后的对比：

[convolutional]
size=1
stride=1
pad=1
filters=255
activation=linear


[yolo]
mask = 0,1,2
anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
classes=80
num=9
jitter=.3
ignore_thresh = .5
truth_thresh = 1
random=1


[convolutional]
size=1
stride=1
pad=1
filters=18
activation=linear


[yolo]
mask = 0,1,2
anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
classes=1
num=9
jitter=.3
ignore_thresh = .5
truth_thresh = 1
random=1

图中的random表示论文中提及的resize network来增强网络的适应性，如果显存足够，最好设置为1，如果显存不够，也可以将其设置为0，即不进行network resizing

（4）weights文件准备
如果你使用的是作者提供的cfg模型结构，如yolov3，那么可以到其官网去下载预训练模型来初始化模型参数，这样可以加快收敛。当然，你也可以不使用预训练模型进行训练

（5）开始训练
如果使用预训练模型则使用如下命令

./darknet detector train data/detect.data data/yolov3.cfg data/yolov3.weight
1
否则，使用

./darknet detectortrain data/detect.data data/yolov3.cfg
1
命令类似与之前检测的调用命令，只是将test变为了train

分类模型的训练
（1）数据准备
和检测不一样，分类的gt只需要一个label即可，不再需要位置框的信息，所以不再需要单独的txt文件来保存gt，而是直接将label在图像名称上进行体现。所以需要对图像名称进行重命名，命名规则为：
（图片序号）_（标签）.（图片格式），如1_numzero.jpg
需要注意的是：
1.label不区分大小写，即 numzero和NumZero是一样的效果
2.label之间不能有包含关系，如ji和jin，不能出现这样的形式，可改为ji1和jin
（2）.data文件准备
和检测类似：

classes=65
train  = data/char/train.list
labels = data/char/labels.txt
backup = backup/
top=2


其中top不是在训练中使用，而是在分类调用时使用，表示输出Top个最高的可能值

（3）.cfg文件准备
可以从cfg文件夹中选择，也可以自行定义

（4）.weights文件
同上面的检测

（5）开始训练
使用命令：


./darknet classifier train cfg/cifar.data cfg/cifar_small.cfg （xxx.weights）

