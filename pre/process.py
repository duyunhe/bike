# coding=utf-8
__author__ = 'cd'
from datetime import datetime
from geo import bl2xy


def process_data():
    f = open("../data/tb_bike_gps_1802.csv", 'r')
    fp1 = open('../data/bike_08.txt', 'w')
    fp2 = open('../data/bike_18.txt', 'w')
    cnt = 0
    for line in f.readlines():
        if cnt == 0:
            cnt += 1
            continue
        items = line.split(',')
        lng, lat = float(items[4].strip('"')), float(items[5].strip('"'))
        x, y = bl2xy(lat, lng)
        state = int(items[7].strip('"'))
        stime = items[3].strip('"')
        dtime = datetime.strptime(stime, '%Y/%m/%d %H:%M:%S')
        if state == 0:
            new_str = "{0},{1},{2}\n".format(x, y, stime)
            if 6 <= dtime.hour < 9:
                fp1.write(new_str)
            elif 16 <= dtime.hour < 19:
                fp2.write(new_str)
        cnt += 1
    fp1.close()
    fp2.close()

process_data()
