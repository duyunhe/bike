# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 14:06
# @Author  : C.D.
# @简介    : 读取自行车csv数据
# @File    : csv_data.py
from datetime import datetime


def get_data_everyday_in_month(filename):
    fp = open(filename, 'r')
    idx = 0
    data = {}
    for line in fp.readlines():
        if idx == 0:
            idx = 1
            continue
        temp = line.strip('\n').split(',')
        items = [one.strip('\"') for one in temp]
        companyid, bicycleno, str_time = items[1:4]
        bid = "{0}:{1}".format(companyid, bicycleno)
        position_time = datetime.strptime(str_time, '%Y/%m/%d %H:%M:%S')
        day_time = datetime.strptime(str_time, '%Y/%m/%d')
        flag = 0
        try:
            bid = data[day_time]
        except KeyError:
            data




