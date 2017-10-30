#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-28 18:37:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import WeChat_group
import Push_Weather
import time
import itchat



class mains():

	def __init__(self):
		self.group = WeChat_group.Push_WeChat_group_news()
		self.Weather = Push_Weather.Push_Weather()        #天气



	def main(self):
		Push_msg = {}
		date = '13:07:50'
		itchat.auto_login(hotReload = True)
		while 1:
			print(time.strftime("%X"))
			date2 = str(time.strftime("%X")) #获取当前时间（按照指定格式）  
			time.sleep(1)
			if date == date2:
				weather_data,city,tip = self.Weather.Weather_post()
				Push_msg['weather_data'] = weather_data
				Push_msg['city'] = city
				Push_msg['tip'] = tip
				self.group.Push_msg(Push_msg)
				break


if __name__ == '__main__':
	M= mains()
	M.main()

