# -*- coding: utf-8 -*-
# Created by asmoker on 01/11/2017.

TRACKERS_URL_LIST = [
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt',  # trackers_best
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt',  # trackers_all
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt',  # trackers_all_udp
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt',  # trackers_all_http
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt',  # trackers_all_https
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt',  # trackers_best_ip
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt',  # trackers_all_ip
]


def get_trackers_url(index=0):
    return TRACKERS_URL_LIST[index]
