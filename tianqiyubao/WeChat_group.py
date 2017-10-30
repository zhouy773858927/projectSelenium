#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-28 14:13:29
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import itchat
from itchat.content import *
import re


class Push_WeChat_group_news():

	def get_full_group_names(self):  #获取所有的群聊名称
		Group_NickNames = []    
		Groups_infos= itchat.get_chatrooms(update=True, contactOnly=True) 
		for Group_info in Groups_infos:
			Group_NickName = Group_info['NickName']
			Group_NickNames.append(Group_NickName)
			return Group_NickNames




	def get_need_Push_msg_groups(self,config_path):   # 获取需要推送消息的群名称
		statu = os.path.exists(config_path)
		if statu ==False:
			return None
		else:
			f = open(config_path,'r')
			groups = f.read()
			Push_group_name = groups.split(',')
			return Push_group_name




	def Push_msg(self,Push_news):               #发送消息
		# itchat.auto_login(hotReload = True)
		config_path = 'C://properties//need_Push_msg_groups.txt'
		Group_NickNames = self.get_full_group_names()
		Push_group_name = self.get_need_Push_msg_groups(config_path)
		if Push_group_name != None:
			for d in Push_group_name:
				Group_infos = itchat.search_chatrooms(name = d)  
				UserName = Group_infos[0]['UserName']              #群聊的UserName
				weather_data = Push_news['weather_data']

				city = Push_news['city']
				tip = Push_news['tip']
				itchat_statu = itchat.send('您当前所在城市：%s \n天气预报：%s \n温馨提示：%s' % (city,weather_data,tip),toUserName = UserName)


#class get_group_news(Push_WeChat_group_news):



