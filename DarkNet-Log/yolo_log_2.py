#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#最大迭代次数
max_batches=100000
#
minStep = 18
#其中minStep代表1行Loaded: 0.000024 seconds、10行 Region，1行第n次的结果 1+16+1=18
'''
Loaded: 0.000024 seconds
Region 16 Avg IOU: 0.182902, Class: 0.405722, Obj: 0.503862, No Obj: 0.424742, .5R: 0.000000, .75R: 0.000000,  count: 13
Region 23 Avg IOU: 0.105590, Class: 0.662942, Obj: 0.520905, No Obj: 0.509580, .5R: 0.000000, .75R: 0.000000,  count: 12
Region 16 Avg IOU: 0.130522, Class: 0.408217, Obj: 0.476290, No Obj: 0.424609, .5R: 0.000000, .75R: 0.000000,  count: 14
Region 23 Avg IOU: 0.182063, Class: 0.550706, Obj: 0.494642, No Obj: 0.507713, .5R: 0.070175, .75R: 0.000000,  count: 57
Region 16 Avg IOU: 0.200967, Class: 0.390888, Obj: 0.475645, No Obj: 0.427092, .5R: 0.062500, .75R: 0.000000,  count: 16
Region 23 Avg IOU: 0.143319, Class: 0.580808, Obj: 0.531322, No Obj: 0.509306, .5R: 0.064516, .75R: 0.000000,  count: 31
Region 16 Avg IOU: 0.237835, Class: 0.382465, Obj: 0.380643, No Obj: 0.427353, .5R: 0.066667, .75R: 0.000000,  count: 15
Region 23 Avg IOU: 0.106707, Class: 0.574932, Obj: 0.548107, No Obj: 0.510025, .5R: 0.000000, .75R: 0.000000,  count: 37
Region 16 Avg IOU: 0.163751, Class: 0.414830, Obj: 0.416970, No Obj: 0.425206, .5R: 0.000000, .75R: 0.000000,  count: 3
Region 23 Avg IOU: 0.174204, Class: 0.676216, Obj: 0.571296, No Obj: 0.510338, .5R: 0.045455, .75R: 0.000000,  count: 22
Region 16 Avg IOU: 0.191540, Class: 0.441109, Obj: 0.392017, No Obj: 0.425114, .5R: 0.047619, .75R: 0.000000,  count: 21
Region 23 Avg IOU: 0.144743, Class: 0.646313, Obj: 0.482872, No Obj: 0.507978, .5R: 0.000000, .75R: 0.000000,  count: 30
Region 16 Avg IOU: 0.192162, Class: 0.507017, Obj: 0.467949, No Obj: 0.425880, .5R: 0.000000, .75R: 0.000000,  count: 10
Region 23 Avg IOU: 0.129258, Class: 0.672717, Obj: 0.588547, No Obj: 0.509534, .5R: 0.000000, .75R: 0.000000,  count: 36
Region 16 Avg IOU: 0.182297, Class: 0.803474, Obj: 0.596444, No Obj: 0.424545, .5R: 0.000000, .75R: 0.000000,  count: 4
Region 23 Avg IOU: 0.172792, Class: 0.732352, Obj: 0.541576, No Obj: 0.507713, .5R: 0.041667, .75R: 0.000000,  count: 24
1: 756.629517, 756.629517 avg, 0.000000 rate, 1.112322 seconds, 64 images
'''
#在日志里每10个miniStep，即每10次迭代，一次迭代代表1个batch，会出现 2行（分别是Resize 608或者其它尺寸）
n=10
step=minStep*n+2#18x10+2 #2 Resize 608
#x%step==0 or x%step==1
#x%step!=0 and x%step!=1
lines=int(step*max_batches/n)#lines =91000=182*500
#替换相应的日志文件即可/home/zhangping/Desktop/yolo_log/ranPianTiny2.txt
result = pd.read_csv('C:/Users/zhangping/Desktop/yolo_Log/ranPianTiny13_1.txt',
                     skiprows=[x for x in range(lines) if (x%step==0 or x%step==1)],
                     error_bad_lines=False,names=['Region Avg IOU', 'Class','Obj','No Obj','.5R','.7R','count'])
#剔除掉Loaded: 0.000024 seconds 和 第n次的结果，即剔除掉如下类似的行:
'''
Loaded: 0.000024 seconds
1: 756.629517, 756.629517 avg, 0.000000 rate, 1.112322 seconds, 64 images
'''
result1=result.iloc[[i for i in range(minStep*max_batches) if ((i+1)%minStep!=0 and i%minStep!=0)]]#90000=18*5000
#取出 Region Avg IOU 列,并进行数据类型转换
Region =result1['Region Avg IOU'].str.split(': ').str[1]
Region = Region.astype(float)
#取出 Class 列,并进行数据类型转换
Class = result1['Class'].str.split(': ').str[1]
Class = Class.astype(float)
#取出 Obj 列,并进行数据类型转换
Obj = result1['Obj'].str.split(': ').str[1]
Obj = Obj.astype(float)
#取出 NoObj 列,并进行数据类型转换
NoObj = result1['No Obj'].str.split(': ').str[1]
NoObj = NoObj.astype(float)
#取出 R5 列,并进行数据类型转换
R5 = result1['.5R'].str.split(': ').str[1]
R5 = R5.astype(float)
#取出 R7 列,并进行数据类型转换
R7 = result1['.7R'].str.split(': ').str[1]
R7 = R7.astype(float)
#取出 count 列,并进行数据类型转换
count = result1['count'].str.split(': ').str[1]
count = count.astype(float)
#
figure = plt.figure()
gs1 = gridspec.GridSpec(4,2)
#画出 Region Avg IOU的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_Region=figure.add_subplot(gs1[0])
ax_Region.set_xlabel('Region Avg IOU')
ax_Region.set_ylabel("Region Avg IOU")
ax_Region.plot(Region.values,label='Region Avg IOU')
#画出 Class 的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_Class = figure.add_subplot(gs1[1])
ax_Class.set_xlabel('Class')
ax_Class.set_ylabel('Class')
ax_Class.plot(Class.values,label='Class')
#画出 Obj 的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_Obj = figure.add_subplot(gs1[2])
ax_Obj.set_xlabel('Obj')
ax_Obj.set_ylabel('Obj')
ax_Obj.plot(Obj.values,label='Obj')
#画出 NoObj 的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_NoObj = figure.add_subplot(gs1[3])
ax_NoObj.set_xlabel('NoObj')
ax_NoObj.set_ylabel('NoObj')
ax_NoObj.plot(NoObj.values,label='NoObj')
#画出 R5 的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_R5 = figure.add_subplot(gs1[4])
ax_R5.set_xlabel('R5')
ax_R5.set_ylabel('R5')
ax_R5.plot(R5.values,label='R5')
#画出 R7 的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_R7 = figure.add_subplot(gs1[5])
ax_R7.set_xlabel('R7')
ax_R7.set_ylabel('R7')
ax_R7.plot(R7.values,label='R7')
#画出 count 的值，至于set_xlabel和set_ylabel的值可以根据自己的定义修改
ax_count = figure.add_subplot(gs1[6])
ax_count.set_xlabel('count')
ax_count.set_ylabel('count')
ax_count.plot(count.values,label='count')
plt.show()