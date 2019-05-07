import cv2
import os
chuan=['quzhujian_or_huweijian_or_xunyangjian','yuchuan','haijingchuan','washachuan','qizhongchuan','yunshuchuan','youlun','qidianchuan','pobingchuan','hangmu']
for q in range(len(chuan)):
    for root, _, files in os.walk('Z:\BaiduImageSpider-master\\'+chuan[q]+'_test'):

        print('当前路径'+root) #当前目录路径
        # for n in range(len(files)):
        #     im = cv2.imread(root + '\\' + files[n])
        #     print(files[n])
        #     print(im.shape)
        for n in range(len(files)):


            if files[n].endswith('.jpeg'):
                print(files[n][:-5])
                im = cv2.imread(root + '\\' + files[n])
                cv2.imwrite(root+'\\'+files[n][:-5]+'.jpg',im)
            if files[n].endswith('.png'):
                print(files[n][:-4])
                im = cv2.imread(root + '\\' + files[n])
                cv2.imwrite(root+'\\'+files[n][:-4]+'.jpg',im)
# for root, _, files in os.walk('Z:\BaiduImageSpider-master\\xunyangjian_test'):
#     print('当前路径' + root)  # 当前目录路径
#     for n in range(len(files)):
#         im = cv2.imread(root + '\\' + files[n])
#         cv2.imwrite('Z:\BaiduImageSpider-master\\quzhujian_test'+ '\\'+'1'+ files[n], im)