import numpy as np
from keras.models import load_model
from keras.optimizers import SGD
from keras.preprocessing.image import img_to_array
import tensorflow as tf
import argparse,os
import imutils
import cv2
import keras.backend.tensorflow_backend as KTF
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" #设置CPU
# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" #多GPU设置哪些GPU参与运算
# 设置gpu根据需求调用显存
config = tf.ConfigProto()  
config.gpu_options.allow_growth=False   
session = tf.Session(config=config)
KTF.set_session(session)

if __name__ == "__main__":
    #=============加载模型预测单张图片======start=
    #load the image
    video_reader = cv2.VideoCapture(0+cv2.CAP_DSHOW)
    video_reader.set(3, 640)
    image_paths = []
    batch_size = 1
    labell = "22"
    count = 0
    with tf.device("/cpu:0"):
        model = load_model('./hat-01-1.00.hdf5')
        # model.compile(optimizer=sgd, loss='categorical_crossentropy')
        while(True):
            ret, image = video_reader.read()
            # print("===========")
            orig = image.copy()
            # pre-process the image for classification
            orig = cv2.resize(orig, (32, 32))
            orig = orig.astype("float") / 255.0
            orig = img_to_array(orig)
            img = np.expand_dims(orig, axis=0)
            out = model.predict(img)  # note: the model has three outputs
            print(np.argmax(out[2]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            if (np.argmax(out[2])) :
                # cv2.rectangle(img=img, pt1=(start_x, start_y), pt2=(end_x, end_y), color=(0, 0, 255))
                labell = "11111"
            else:
                # cv2.rectangle(img=img, pt1=(start_x, start_y), pt2=(end_x, end_y), color=(0, 255, 0))
                labell = "0000"
            print(labell)
            cv2.putText(image, labell, (100,100), font, 2, (0,0,255), 2)
            cv2.imshow("image", image)
            if cv2.waitKey(1) == 27:
                break