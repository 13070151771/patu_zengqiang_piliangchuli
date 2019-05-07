import os
import random
import cv2
chuan=['quzhujian_or_huweijian_or_xunyangjian','yuchuan','haijingchuan','washachuan','qizhongchuan','yunshuchuan','youlun','qidianchuan','pobingchuan','hangmu']
for q in range(len(chuan)):
    for root, _, files in os.walk('Z:\BaiduImageSpider-master\\'+chuan[q]):
        print('当前路径'+root) #当前目录路径
        # for n in range(len(files)):
        #     im = cv2.imread(root + '\\' + files[n])
        #     print(files[n])
        #     print(im.shape)
        # for n in range(len(files)):
        #
        #
        #     if files[n].endswith('.jpeg'):
        #         print(files[n][:-5])
        #         im = cv2.imread(root + '\\' + files[n])
        #         cv2.imwrite(root+'\\'+files[n][:-5]+'.jpg',im)
        #     if files[n].endswith('.png'):
        #         print(files[n][:-4])
        #         im = cv2.imread(root + '\\' + files[n])
        #         cv2.imwrite(root+'\\'+files[n][:-4]+'.jpg',im)
        #
        # input()
        count=0
        for n in range(len(files)):
            re = random.random()
            im=cv2.imread(root+'\\'+files[n])
            if im.ndim==2:
                print(files[n])
                continue
            kuan=im.shape[0]
            chang=im.shape[1]
            if re<0.5:#反转
                im=cv2.flip(im,1)
                cv2.imwrite(root + '\\flip_' + files[n], im)
            else:#加噪
                for i in range(im.shape[0]):
                    for j in range(im.shape[1]):
                        rdn = random.random()
                        if rdn < 0.01:
                            im[i][j] = 0
                        elif rdn > 0.99:
                            im[i][j] = 255
                        else:
                            im[i][j] = im[i][j]
                cv2.imwrite(root+'\\noise_'+files[n],im)
            im1= cv2.imread(root + '\\' + files[n])
            re1 = random.random()
            if re1<0.5:
                im1 = cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY)
                cv2.imwrite(root + '\\gray_' + files[n], im1)
            if re1>0.5 and re1 < 0.75:
                print(files[n])
                rows, cols, channel = im1.shape
                #print(rows, cols, channel)
                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -20, 0.8)
                im1 = cv2.warpAffine(im1, M, (cols, rows))
                cv2.imwrite(root + '\\rotate_' + files[n], im1)
            if re1>0.75:
                print(files[n])
                rows, cols, channel = im1.shape
                # print(rows, cols, channel)
                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 20, 0.8)
                im1 = cv2.warpAffine(im1, M, (cols, rows))
                cv2.imwrite(root + '\\rotate_' + files[n], im1)
            count+=1
            if count%50==0:
                print(count)


