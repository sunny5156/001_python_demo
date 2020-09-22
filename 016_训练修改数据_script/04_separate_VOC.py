#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 14:11
# @Author  : Scheaven
# @File    :  01_video2img.py
# @description: 
import os
import shutil
'''
	用于根据挑选出来的标注错误的文件，进行对原数据集的错误数据移出重新标注
'''

def move_file(src_path, dst_path,error_path):
	img_list = os.listdir(error_path)
	for img_name in img_list:
		name,exe = os.path.splitext(img_name)

		f_src = os.path.join(src_path, "JPEGImages", img_name)
		f_dst = os.path.join(dst_path, "JPEGImages", img_name)

		print(f_src,f_dst)
		if not os.path.exists(f_dst):
			os.makedirs(f_dst)

		if os.path.exists(f_src):
			shutil.move(f_src,f_dst)


		f_src = os.path.join(src_path, "Annotations", name+".xml")
		f_dst = os.path.join(dst_path, "Annotations", name+".xml")

		print(f_src,f_dst)
		if not os.path.exists(f_dst):
			os.makedirs(f_dst)

		if os.path.exists(f_src):
			shutil.move(f_src,f_dst)


if __name__ == '__main__':
	error_path = "./ERROR_VOCHAT/"
	src_path = "./10_darknet_hat_data/"
	dst_path = "./10_darknet_hat_data/error_hat_head/"

	move_file(src_path, dst_path, error_path)

