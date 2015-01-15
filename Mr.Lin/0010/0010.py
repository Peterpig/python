#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-14 18:20:01
# @Last Modified by:   30987
# @Last Modified time: 2015-01-15 12:20:59

#第 0010 题：使用 Python 生成字母验证码图片

import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

_letter_cases = 'abcdefghjkmnpqrstuvwxy' #小写字母，忽略了容易误解的i,l,o,z
_upper_cases = _letter_cases.upper()	#转换为大写字母
_number = ''.join(map(str,range(3,10))) #生成[3,4,5,6,7,8,9]，然后将他们连接为3456789
init_chars=''.join((_letter_cases,_upper_cases,_number))


def create_validate_code(size=(120, 30),
                         chars=init_chars,
                         img_type="JPEG",
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(0, 0, 255),
                         font_size=18,
                         font_type="ahronbd.ttf",
                         length=4,
                         draw_lines=True,
                         n_line=(1, 2),
                         draw_points=True,
                         point_chance = 2):
	"""
	@todo:生成验证码图片
	@param size:	生成验证码图片的尺寸，默认（240，60）
	@param chars:	图片中的字符集
	@param img_type:图片保存的格式，默认JPEG，支持GIF,JPEG,TIFF,PNG
	@param mode:	图片颜色的模式，默认RGB
	@param bg_color:图片背景颜色，默认白色
	@param fg_color:前景颜色，验证码字符的颜色，默认蓝色#0000FF
	@param font_size:验证码字体字体大小，默认18号
	@param font_type:验证码字体，默认ae_AlArabiya.ttf
	@param length：	验证码字符个数
	@param draw_lines:是否有干扰线
	@param n_line:	干扰线条数，元组，只有draw_lines为True时才有效
	@param draw_points:是否画干扰点
	@param point_chance:干扰点出现的概率，范围为[0,100]
	"""
	width,height = size
	img = Image.new(mode,size,bg_color)	#创建图形
	draw = ImageDraw.Draw(img)	#创建画笔

	def get_chars():
		#生成验证码字符
		return random.sample(chars,length)	#random.sample(),从chars中去length长度的内容返回为列表['4', 'g', 'U', 'n']

	def creat_lines():
		#创建干扰线
		line_num = random.randint(*n_line)	#干扰线条数，随机生成,randon.randint(a,b) 用于生成一个指定范围内的整数，a为下限，b为上限，生成的随机整数a<=n<=b;若a=b，则n=a；若a>b，报错

		for i in range(line_num):
			#起始点
			begin = (random.randint(0,size[0]),random.randint(0,size[1]))
			#结束点
			end = (random.randint(0,size[0]),random.randint(0,size[1]))
			draw.line([begin,end],fill=(0,0,0))

	def creat_points():
		#绘制干扰点
		chance = min(100,max(0,int(point_chance)))	#大小限制在[0,100]

		for w in xrange(width):
			for h in xrange(height):
				tmp = random.randint(0,100)
				if tmp > 100-chance:
					draw.point((w,h),fill=(0,0,0))

	def creat_chars():
		#绘制验证码
		c_chars = get_chars()
		strs = ' %s' %''.join(c_chars)	#每个字符前以空格隔开

		font = ImageFont.truetype(font_type,font_size)
		font_width,font_height = font.getsize(strs)

		#draw.text((width-font_width)/3,(height-font_height)/3,strs,font=font,fill=fg_color)
		draw.text(((width - font_width) / 3, (height - font_height) / 3),strs, font=font, fill=fg_color)

		return ''.join(c_chars)

	if draw_lines:
		creat_lines()
	if draw_points:
		creat_points()
	strs = creat_chars()

	#图形扭曲
	#param = [1-float(random.randint(1,2)/100),0,0,0,1 - float(random.randint(1, 10)) / 100,float(random.randint(1, 2)) / 5000.001,float(random.randint(1, 2)) / 500]
	params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
	img = img.transform(size, Image.PERSPECTIVE, params)	#创建扭曲
	img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）
	img.save("validate.JPG", "JPEG")



if __name__ == '__main__':
	code_img = create_validate_code(point_chance = 5)
