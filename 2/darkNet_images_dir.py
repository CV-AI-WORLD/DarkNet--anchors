#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse

if __name__=='__main__':
    #
    parser = argparse.ArgumentParser(description='利用该脚本文件将图片文件夹中图片路径索引到txt文件中')
    #图片存放的文件夹
    parser.add_argument('--input_images_dir',required = True,help='图片文件夹的路径.如/home/data/images')
    #"图片夹下的图片名存放到txt文件中"
    #(包含路径和文件名，比如：/home/zhangping/Desktop/trainImage.txt)
    parser.add_argument('--output_images_txt',required = True,help='输出的txt文件，如$HOME/trainImage.txt')
    args = parser.parse_args()
    #
    f = open(args.output_images_txt,'w')
    #得到文件夹下所有图片的文件名[image1.jpg,image2.jpg]
    names = os.listdir(args.input_images_dir)
    #将文件名（例如绝对路径：/home/Path/image1.jpg）写入文件中
    for name in names:
        f.write(os.path.join(args.input_images_dir,name)+'\n')
    f.close()
    
    