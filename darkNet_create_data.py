#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse
import xml.etree.ElementTree as ET
#转换
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
if __name__ == '__main__':
    #
    parser = argparse.ArgumentParser(description='利用该脚本文件: 1)将xml格式的标注文件转换为txt文件; 2)将图片的路径存储到txt文件中;3)根据实际情况修改脚本文件中的 classes')
    parser.add_argument('--input_images_dir',required = True,help = '输入存储图片的文件夹,darkNet是从文件夹名为images的文件夹中寻找图片,如/home/images')
    parser.add_argument('--input_annotations_dir',required = True,help='输入存储xml格式标注文件的文件夹,如/home/xml')
    parser.add_argument('--output_txt_dir',required = True,help='输出的存储txt文件的文件夹,darkNet是从文件夹名为labels的文件夹中寻找txt文件,而且文件夹images和labels位于同一级目录下,如/home/labels')
    parser.add_argument('--output_imagesdir_txt',required = True,help='输出的存储图片路径和图片名的txt文件名')
    args = parser.parse_args()
    #类别名
    classes = ['c1','c2']
    #索引出标注文件夹下的xml文件
    names = os.listdir(args.input_annotations_dir)
    #打开输出的txt文件
    output_imagesdir_txt = open(args.output_imagesdir_txt,'w')
    #创建存储xml转换为txt文件的文件夹
    output_txt_dir = args.output_txt_dir
    if not os.path.exists(output_txt_dir):
        os.makedirs(output_txt_dir)
    #循环处理
    for name in names:
        fileName,fileNameExtrend = os.path.splitext(name)
        #写入对应的图片文件路径
        output_imagesdir_txt.write(os.path.join(args.input_images_dir,fileName+'.jpg')+'\n')
        #读取xml文件
        xml_path = os.path.join(args.input_annotations_dir,name)
        #对应的输出的txt文件
        output_txt = open(os.path.join(output_txt_dir,fileName)+'.txt','w')
        #输出xml文件
        tree=ET.parse(xml_path)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text) 
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), 
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            #写入txt文件，如'0 0.2 0.3 0.4 0.5'
            output_txt.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        output_txt.close()
    output_imagesdir_txt.close()
        