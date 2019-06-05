from scipy.misc import imread, imresize
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.optimizers import SGD
import cv2

if __name__ == "__main__":
    #=============加载模型预测单张图片======start=
    img = imresize(imread('../test/1160.jpg'), (32, 32)).astype(np.float32)

    #方法二opencv方法不一样
    # img = cv2.imread('../test/1160.jpg')
    # b,g,r = cv2.split(img) 
    # img = cv2.merge([r,g,b]) 

    orig = img_to_array(img)
    img = np.expand_dims(orig, axis=0)
    
    model = load_model('./weights-522-0.17.hdf5')
    # model.compile(optimizer=sgd, loss='categorical_crossentropy')
    out = model.predict(img)  # note: the model has three outputs
    print(np.argmax(out[2]),out)
