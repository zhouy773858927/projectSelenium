#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-23 15:49:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import urllib.request
import urllib.parse
import re
import gzip
import json


class Push_Weather():


	def url_open(self,url):
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req)
		html = response.read()
		return html


	#解压网页数据
	def Unzip_datas(self,html):
		try:
			zip_data = gzip.decompress(html).decode('utf-8')
		except Exception as e:
			print ('解压数据出错：%s'% e)
		else:
			return zip_data


	#将json数据转换为dict数据
	def json_data_change(self,zip_data):
		try:
			dict_data = json.loads(zip_data)
		except Exception as e:
			print ('json数据转换失败:%s' %e)
		else:
			return dict_data
			
	#将想要的数据按天处理出来
	def split_data_day(self,dict_data,date='明天'):
		if date == '昨天':
			weather_data = dict_data['data']['yesterday']
		elif date == '今天':
			weather_data = dict_data['data']['forecast'][0]
		elif date == '明天':
			weather_data = dict_data['data']['forecast'][1]
		elif date == '后天':
			weather_data = dict_data['data']['forecast'][2]
		elif date == '大后天':
			weather_data = dict_data['data']['forecast'][3]

		city = dict_data['data']['city']
		tip = dict_data['data']['ganmao']
		return weather_data,city,tip



	def Format_datas(self,weather_data):
		Format_data = {}
		Format_data['查询日期'] = weather_data['date']
		Format_data['最高温'] = weather_data['high']
		Format_data['最低温'] = weather_data['low']
		Format_data['风力'] = weather_data['fengli']
		Format_data['风向'] = weather_data['fengxiang']
		Format_data['天气状况'] = weather_data['type']
		return Format_data
		


	def Weather_post(self):
		cityName = '深圳'
		url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityName)
		html = self.url_open(url)
		zip_data = self.Unzip_datas(html)
		dict_data = self.json_data_change(zip_data)
		if dict_data['desc'] == 'invilad-citykey':
			return '未查询到您的城市,请重新定位！'
		else:
			weather_data,city,tip = self.split_data_day(dict_data)
			Format_data = self.Format_datas(weather_data)
			return Format_data,city,tip
						

# 