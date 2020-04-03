#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 11:17
# @Author  : Chenhao
# @File    : util.py
# @Software: PyCharm
# @Done    : 图像处理工具库
import cv2
import os


'''
    path1: source img path
    path2: sr img path
'''
def img_sub(path1, path2):
    for name in ['Set5', 'Set14', 'BSDS100', 'Urban100']:
        source_path = '{}/{}'.format(path1, name)
        sr_path = '{}/results-{}'.format(path2, name)
        for img_name in os.listdir(source_path):
            img_path1 = '{}/{}'.format(source_path,img_name)
            img1 = cv2.imread(img_path1)
            temp = img_name.split('.')[0]
            for scale in [2, 3, 4]:
                img_path2 = '{}/{}_x{}_SR.png'.format(sr_path, temp.replace('_', ''), scale)
                img2 = cv2.imread(img_path2)

                if img1.size != img2.size:
                    if (img1.shape[0] > img2.shape[0]):
                        img1 = img1[0:img2.shape[0]]
                    elif (img1.shape[0] < img2.shape[0]):
                        img2 = img2[0:img1.shape[0]]

                    if (img1.shape[1] > img2.shape[1]):
                        img1 = img1[:, 0:img2.shape[1]]
                    elif (img1.shape[1] < img2.shape[1]):
                        img2 = img2[:, 0:img1.shape[1]]

                img = cv2.subtract(img1, img2)
                path = "{}/result/{}/{}_x{}.png".format(path2, name, temp, scale)
                cv2.imwrite(path, img)

def Sobel(path):
    img = cv2.imread(path, 0)
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    cv2.imshow('absX', absX)
    cv2.imshow('absY', absY)
    cv2.imshow('source', img)
    dst = cv2.resize(dst, (dst.shape[0]*4, dst.shape[1]*4), cv2.INTER_CUBIC)
    cv2.imshow('dst', dst)
    cv2.imwrite('./source/test_x4.png', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # img_sub('E:/dataset', './sr')
    Sobel('E:/dataset/Set5/butterflyx4.png')