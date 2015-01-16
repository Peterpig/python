#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-16 10:18:31
# @Last Modified by:   30987
# @Last Modified time: 2015-01-16 10:37:52

#第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
#网址 http://tieba.baidu.com/p/2166231880
#
#经分析，每张的图片都有类似的格式，其中只有src地址不一样。所有写正则即可
#<img pic_type="0" class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=6b12a1088718367aad897fd51e738b68/1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg" bdwater="杉本有美吧,955,550" width="560" height="323" changedsize="true" style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer;">
#
#正则如下
#r'<img pic_type="0" class="BDE_Image" src="(.*?\.jpg)" bdwater='
#


import re
import urllib

def get_html(url):
	html = urllib.urlopen(url).read()
	return html

def Schedule(a,b,c):
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print '%.2f%%' % per


def get_img(html):
	reg = r'<img pic_type="0" class="BDE_Image" src="(.*?\.jpg)" bdwater='
	img = re.compile(reg)
	imglist = re.findall(img,html)
	i = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg'%i,Schedule)
		i+=1


if __name__ == '__main__':
	 html = get_html('http://tieba.baidu.com/p/2166231880')
	 get_img(html)