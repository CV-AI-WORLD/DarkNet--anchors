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
    parser = argparse.ArgumentParser(description='利用该脚本文件将xml格式的标注文件转换为txt文件')
    parser.add_argument('--input_annotations_dir',required = True,help='输入存储xml格式标注文件的文件夹,如/home/xml')
    parser.add_argument('--output_txt_dir',required = True,help='输出的存储txt文件的文件夹,如/home/trainImagetxt')
    args = parser.parse_args()
    #
    classes = ['c1','c2']
    #
    names = os.listdir(args.input_annotations_dir)
    #
    for name in names:
        fileName,fileNameExtrend = os.path.splitext(name)
        #
        xml_path = os.path.join(args.input_annotations_dir,name)
        #对应的输出的txt文件
        output_txt = open(os.path.join(args.output_txt_dir,fileName)+'.txt','w')
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
        
