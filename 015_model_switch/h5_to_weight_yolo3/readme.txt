转换步骤解释如下
https://blog.csdn.net/qinchang1/article/details/105776132

主要步骤包括：
1、在解压的文件夹中放入Keras训练的yolo.h5文件。
2、将coco_classes.txt和voc_classes.txt文件中的识别对象类型改为训练中标记的对象。
例如：本文训练了2个对象，down / person。

3、
打开yolov3.cfg，在里面查找 yolo（注意有3处），需要修改的地方处：
1.filters = 3 * ( 5 + classes)
2.classes = n （这个是你要训练的类的数量）
例如：本文这里有23个类，所以filters=21，classes=2。

4、
运行check_weight.py程序，就可以生成yolov3.weights文件了
