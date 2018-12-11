#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from absl import flags
from absl import app
import os
'''
Usage:
python list_dir.py
--data_dir /home/Path
--output_txt /home/path/trainPathImage.txt
'''
#图片存放的文件夹
flags.DEFINE_string('data_dir', '', 'Root directory to images dataset.')
#"图片夹下的图片名存放到txt文件中"
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
    #将文件名（例如绝对路径：/home/Path/image1.jpg）写入文件中
    for name in names:
        f.write(os.path.join(data_dir,name)+'\n')
    f.close()
if __name__=='__main__':
    app.run(main)
