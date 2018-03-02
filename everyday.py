# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 15:31
# @Author  : 
# @简介    : 
# @File    : everyday.py

from CSV import csv_data


def main():
    filename = './data/tb_bike_gps_1802.csv'
    csv_data.get_data_everyday_in_month(filename)

main()
