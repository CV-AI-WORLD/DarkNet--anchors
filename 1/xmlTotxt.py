#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from absl import app
from absl import flags
import xml.etree.ElementTree as ET
import os
'''
python xmlTotxt.py
--annotation annotation标注文件的路径，文件夹
--input_txt 所有annotation文件的文件名
--output_txt_dir 输出的对应的txt文件的文件路径
'''
#标注文件Annotation的文件存储路径（例如:/home/path/annotation）
flags.DEFINE_string('annotation','','annotation xml dir')
#这个输入的是list_dir_name的文件，其实也是所有Annotation文件的文件名
flags.DEFINE_string('input_txt','','')
#将每一个Annotation文件（xml文件）转换为 txt 文件,以下指的输出文件夹
flags.DEFINE_string('output_txt_dir','','output_txt_dir')
FLAGS = flags.FLAGS
#类别这个根据自己的需求，做出相应修改即可
classes = ['cat',]
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
def main(_):#convert_annotation
    #读取所有Annotation（xml）的文件名
    names = open(FLAGS.input_txt).read().strip().split()
    #循环将每一个Annotation的文件转换为xml文件
    for name in names:
        #Annotation文件路径
        xml_path = os.path.join(FLAGS.annotation,name)+'.xml'
        #对应的输出的txt文件
        output_txt = open(os.path.join(FLAGS.output_txt_dir,name)+'.txt','w')
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
if __name__=='__main__':
    app.run(main)
