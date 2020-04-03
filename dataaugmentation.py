#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 11:30
# @Author  : Chenhao
# @File    : dataaugmentation.py
# @Software: PyCharm
# @Done    : 数据增强
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import os
# 图像裁剪
def crop():
    size = 200
    img = cv2.imread('baby.png',)[...,::-1]
    y = random.randint(1, img.shape[0]-size)
    x = random.randint(1, img.shape[1]-size)
    cropimg = img[y:y+size, x:x+size]
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('原始图像')
    plt.subplot(1, 2, 2)
    plt.imshow(cropimg)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('剪切图像')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.savefig('crop.png',dpi=150)

# 图像翻转
def flip():
    img = cv2.imread('baby.png',)[...,::-1]
    ximg = cv2.flip(img, 0)     # 绕x轴翻转
    yimg = cv2.flip(img, 1)     # 绕y轴翻转
    xyimg = cv2.flip(img, -1)     # 绕xy轴翻转
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('原始图像')
    plt.subplot(2, 2, 2)
    plt.imshow(ximg)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('x-图像')
    plt.subplot(2, 2, 3)
    plt.imshow(yimg)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('y-图像')
    plt.subplot(2, 2, 4)
    plt.imshow(xyimg)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('xy-图像')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.savefig('clip.png', dpi=150)

# 图像旋转
def rotate_bound():
    image = cv2.imread('baby.png', )[...,::-1]
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    LM = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)     # 左旋转90°
    RM = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)    # 右旋转90°
    cos = np.abs(LM[0, 0])
    sin = np.abs(LM[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    LM[0, 2] += (nW / 2) - cX
    LM[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    limage = cv2.warpAffine(image, LM, (nW, nH))
    rimage = cv2.warpAffine(image, RM,(nW, nH))
    plt.subplot(1,3,1)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('原始图像')
    plt.subplot(1, 3, 2)
    plt.imshow(limage)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('左-图像')
    plt.subplot(1, 3, 3)
    plt.imshow(rimage)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('右-图像')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.savefig('rotate.png', dpi=150)

# 图像颜色变化
def color():
    img = cv2.imread('baby.png')
    grapimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    plt.subplot(1, 2, 1)
    plt.imshow(img[...,::-1])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('原始图像')
    plt.subplot(1, 2, 2)
    plt.imshow(grapimg, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('灰度图像')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.savefig('color.png', dpi=150)

# 获取BICUBIC图像
def getBicubic():
    basepath = './Set5/'
    savepath = './Set5_Bicubic'
    for name in os.listdir(basepath):
        path = basepath+name
        img = cv2.imread(path)
        temp = cv2.resize(img, (int(img.shape[0] / 3), int(img.shape[1] / 3)), interpolation=cv2.INTER_CUBIC)
        img = cv2.resize(temp, (temp.shape[0] * 3, temp.shape[1] * 3), interpolation=cv2.INTER_CUBIC)

        if not os.path.exists(savepath):
            os.mkdir(savepath)

        temppath = '{}/b{}'.format(savepath,name)
        cv2.imwrite(temppath, img)
    cv2.destroyAllWindows()

# 结果比较
def compare():
    sourcepath = './Set5/'
    bicubicpath = './Set5_Bicubic/'
    capath = './Set5_CA/'
    number = 1
    for name in os.listdir(sourcepath):
        source = cv2.imread(sourcepath+name)[...,::-1]
        bicubic = cv2.imread('{}b{}'.format(bicubicpath, name))[...,::-1]
        ca = cv2.imread('{}{}_x2_SR.png'.format(capath, name.split('.')[0]))[...,::-1]
        plt.subplot(2, 3, number)
        plt.imshow(source)
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('source_{}'.format(name.split('.')[0]))
        plt.subplot(2, 3, number+1)
        plt.imshow(bicubic)
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('bicubic_{}'.format(name.split('.')[0]))
        plt.subplot(2, 3, number + 2)
        plt.imshow(ca)
        plt.xticks([])
        plt.yticks([])
        plt.xlabel('ca_{}'.format(name.split('.')[0]))
        number = number+3

    plt.savefig('result.png', dpi=150)


if __name__ == '__main__':
    getBicubic()