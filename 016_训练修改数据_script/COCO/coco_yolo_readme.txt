Makefile是编译darknet yolo的Makefile文件

转化coco数据集可以在yolo下训练，我是用的别人的脚本（修改过）
脚本仍然存在bug，


项目地址如下：
参考文章地址 https://segmentfault.com/a/1190000024425275
https://github.com/ikuokuo/start-yolov4/blob/master/docs/darknet_train_using_docker.md

关键步骤
'''
cd start-yolov4/
pip install -r scripts/requirements.txt

export COCO_DIR=/home/disk1/data/COCO/coco

转化数据集
# train
python 03_coco2yolo.py --coco_img_dir $COCO_DIR/train2017/ --coco_ann_file $COCO_DIR/annotations/instances_train2017.json --yolo_names_file ./cfg/coco/coco.names --output_dir ./data/ --output_name train2017 --output_img_prefix /home/disk1/Scheaven/start-yolov4/data/train2017
# valid
python 03_coco2yolo.py --coco_img_dir $COCO_DIR/val2017/ --coco_ann_file $COCO_DIR/annotations/instances_val2017.json --yolo_names_file ./cfg/coco/coco.names --output_dir./data/ --output_name val2017 --output_img_prefix /home/disk1/Scheaven/start-yolov4/data/val2017
'''


from coco.label import ... 如果报错，coco 其实是个文件夹，在本文件同目录
