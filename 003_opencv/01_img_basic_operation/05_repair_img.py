import numpy as np
import cv2
import cv2 as cv

m_path = "gc.jpg"

def replaceZeroes(data):
    min_nonzero = min(data[np.nonzero(data)])
    data[data == 0] = min_nonzero
    return data


def SSR(src_img, size):
    L_blur = cv2.GaussianBlur(src_img, (size, size), 0)
    img = replaceZeroes(src_img)
    L_blur = replaceZeroes(L_blur)

    dst_Img = cv2.log(img / 255.0)
    dst_Lblur = cv2.log(L_blur / 255.0)
    dst_IxL = cv2.multiply(dst_Img, dst_Lblur)
    log_R = cv2.subtract(dst_Img, dst_IxL)

    dst_R = cv2.normalize(log_R, None, 0, 255, cv2.NORM_MINMAX)
    log_uint8 = cv2.convertScaleAbs(dst_R)
    return log_uint8


def repair(path,img2):
    img = cv.imread(path)

    # b = cv.imread('cavity3.png',0)
    dst = cv.inpaint(img, cv.cvtColor(img2,cv.COLOR_BGR2GRAY), 9, cv.INPAINT_TELEA)
    cv.imshow('dst', dst)
    cv.imwrite(f'repair_{path}', dst)
    cv.waitKey()
    cv.destroyAllWindows()

def dim_font(path):
    # 增强通道信息
    size = 3
    src_img = cv2.imread(img)
    b_gray, g_gray, r_gray = cv2.split(src_img)
    b_gray = SSR(b_gray, size)
    g_gray = SSR(g_gray, size)
    r_gray = SSR(r_gray, size)
    result = cv2.merge([b_gray, g_gray, r_gray])

    # cv2.imshow('img', src_img)
    # cv2.imshow('aaa', result)

    cv2.imwrite('cavity1.png', result)

    # 检测边缘
    # img = cv.imread('cavity1.png', cv.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    canny_img = cv.Canny(img, 200, 150)
    cv.imwrite('cavity2.png', canny_img)

    # 对边缘图像记性闭运算
    # img = cv.imread('cavity2.png', 1)
    img = cv2.cvtColor(canny_img, cv2.COLOR_GRAY2BGR)
    k = np.ones((3, 3), np.uint8)
    img2 = cv.morphologyEx(img, cv.MORPH_CLOSE, k)  # 闭运算
    # cv2.imshow('img2',img2)

    # cv.imwrite('cavity3.png', img2)

    # 修复图像
    repair(m_path, img2)


if __name__ == '__main__':
    dim_font(m_path)


