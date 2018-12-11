#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Usage:

pthon list_dir_name.py  
--data_dir /path/image
--output_txt /path/trainImage.txt
'''
from absl import flags
from absl import app
import os
#图片存放的文件夹
flags.DEFINE_string('data_dir', '', 'Root directory to images dataset.')
#图片夹下的图片名存放到txt文件中
#(包含路径和文件名，比如：/home/zhangping/Desktop/trainImage.txt)
flags.DEFINE_string('output_txt','','Path to directory to txt')
FLAGS=flags.FLAGS
#
def main(_):
    data_dir = FLAGS.data_dir
    output_txt=FLAGS.output_txt
    #打开txt文件
    f = open(output_txt,'w')
    #得到文件夹下所有图片的文件名[image1.jpg,image2.jpg]
    names = os.listdir(data_dir)
    #循环处理文件名和文件的扩展名分开
    for name in names:
        fileName,fileNameExtrend = os.path.splitext(name)
        #f.write(os.path.join(data_dir,name)+'\n')
        f.write(fileName+'\n')
    f.close()
if __name__=='__main__':
    app.run(main)