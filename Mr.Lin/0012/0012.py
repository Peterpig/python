#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-15 18:36:29
# @Last Modified by:   30987
# @Last Modified time: 2015-01-16 10:09:01
#
# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
# 发现读取文件的时候中文识别不了。。
#


def filter_words(words):
	#从文件中读取过滤单词名单
	file_object = open('filtered_words.txt','r')
	filtered_words = []
	for line in file_object:
		filtered_words.append(line.strip('\n'))
	file_object.close()
	#print filtered_words
	#判断filtered_words是否在用户输入的words中
	for f_words in filtered_words:
		#f_words.decode('gbk')
		if f_words in words:
			words = words.replace(f_words,'*' * len(f_words))


	print(words)


if __name__ == '__main__':
	input_words = raw_input('Please input some words:')
	input_words.decode('gbk')
	print "input_words:",input_words
	filter_words(input_words)
