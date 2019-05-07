#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import random
im=cv2.imread('Z:\\BaiduImageSpider-master\\demo\\1.jpeg')

# im=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
# cv2.imwrite('Z:\\BaiduImageSpider-master\\demo\\4.jpg',im)
cv2.imshow('true',im)
cv2.waitKey(0)
im1=cv2.flip(im,1)
cv2.imshow('flip',im1)
cv2.waitKey(0)
im2=cv2.imread('Z:\\BaiduImageSpider-master\\demo\\1.jpeg')
for i in range(im2.shape[0]):
    for j in range(im2.shape[1]):
        rdn = random.random()
        if rdn < 0.01:
            im2[i][j] = 0
        elif rdn > 0.99:
            im2[i][j] = 255
        else:
            im2[i][j] = im[i][j]
cv2.imshow('noise',im2)
cv2.waitKey(0)
im3=cv2.imread('Z:\\BaiduImageSpider-master\\demo\\1.jpeg')
rows,cols,channel=im3.shape
print(rows,cols,channel)
M=cv2.getRotationMatrix2D((cols/2,rows/2),-20,0.8)
M2=cv2.getRotationMatrix2D((cols/2,rows/2),20,0.8)
im4=cv2.warpAffine(im3,M,(cols,rows))
cv2.imshow('rota',im4)

cv2.waitKey(0)
im5=cv2.warpAffine(im3,M2,(cols,rows))
cv2.imshow('rota1',im5)
cv2.waitKey(0)
im6=cv2.imread('Z:\\BaiduImageSpider-master\\demo\\1.jpeg')
(b, g, r) = cv2.split(im6)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并每一个通道
result = cv2.merge((bH, gH, rH))
cv2.imshow("dou", result)
cv2.waitKey(0)