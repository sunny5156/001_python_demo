import numpy as np
import cv2


left_camera_matrix = np.array([[837.046533944197,   0., 0.],
                               [-1.38537933662732,  838.772077702795,   0.],
                               [690.459242460418,   535.874773256865,   1.]])  #CameraParameters1.IntrinsicMatrix
left_distortion = np.array([[0.00372605723623423,   0.000603658659694726, 0.0100736540032466,   0.00134603874266809, -0.0625795789344168]])



right_camera_matrix = np.array([[829.904768800558,  0., 0.],
                                [0.449308928342319, 831.157653465328,   0.],
                                [728.582976346643,  550.936706268738,   1.]])
right_distortion = np.array([[0.00607433417962732,  -0.0112160302647384, 0.0104597000277839 ,0.00265721874066941,-0.0262959511445746]])


R = np.array([[1.,       0.0039,    -0.0038],
              [-0.0039,    1.,          0.],
              [0.0038,     0.,          1.]])#旋转向量
T = np.array([-59.5777,0.032,-2.9472]) # 平移关系向量TranslationOfCamera2

size = (1280, 960) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)
# ToDO 问题可能出在此处，读取的摄像头并不大，导致
cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 600, 0)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)#1920,1280
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)#1080,720
# camera2 = cv2.VideoCapture(1)

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print (threeD[y][x])

cv2.setMouseCallback("depth", callbackFunc, None)

while True:
    ret, frame= camera.read()
    # ret2, frame2 = camera2.read()

    if not ret :
        print('can \t open camera or camera has been opened' )
        break
    frame1=frame[0:960,0:1280]
    frame2=frame[0:960,1280:2560]
    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(frame1, left_map1, left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, right_map1, right_map2, cv2.INTER_LINEAR)

    # 将图片置为灰度图，为StereoBM作准备
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    # 两个trackbar用来调节不同的参数查看效果
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    stereo = cv2.StereoBM_create(numDisparities=16*num, blockSize=blockSize)
    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., Q)

    cv2.imshow("left", img1_rectified)
    cv2.imshow("right", img2_rectified)
    cv2.imshow("depth", disp)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("E:/pythonlearning/opencv/screenshot/BM_left.jpg", imgL)
        cv2.imwrite("E:/pythonlearning/opencv/screenshot/BM_right.jpg", imgR)
        cv2.imwrite("E:/pythonlearning/opencv/screenshot/BM_depth.jpg", disp)

camera.release()
# camera2.release()
cv2.destroyAllWindows()