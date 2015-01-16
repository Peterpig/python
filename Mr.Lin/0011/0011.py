#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-15 12:22:00
# @Last Modified by:   30987
# @Last Modified time: 2015-01-15 12:37:53

#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

def fileter_words():
	file_obj = open('filtered_words.txt','r')
	file = file_obj.read()
	filt = file.split('\n')
	file_obj.close

	while True:
		flag = False
		input_text = raw_input("please input:")
		for x in filt:
			if input_text.find(x) != -1 :
				flag = True
		if flag:
			print "Freedom"
		else:
			print "Human Rights。"



if __name__ == '__main__':
	fileter_words()
