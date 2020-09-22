import json
import os
import cv2

parent_path = './train2017'
json_file = './annotations/instances_train2017.json'
with open(json_file) as annos:
    annotations = json.load(annos)

for i in range(len(annotations)):
    annotation = annotations[i]
    if annotation['category_id'] != 1: # 1表示人这一类
        continue
    image_id = annotation['image_id']
    bbox = annotation['bbox'] # (x1, y1, w, h)
    x, y, w, h = bbox
    image_path = os.path.join(parent_path, str(image_id).zfill(12) + '.jpg') # 记得加上.jpg
    image = cv2.imread(image_path)
    # 参数为(图像，左上角坐标，右下角坐标，边框线条颜色，线条宽度)
    # 注意这里坐标必须为整数，还有一点要注意的是opencv读出的图片通道为BGR，所以选择颜色的时候也要注意
    anno_image = cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 255), 2) 
    # 参数为(显示的图片名称，要显示的图片)  必须加上图片名称，不然会报错
    cv2.imshow('demo', anno_image)
    cv2.waitKey(5000)
