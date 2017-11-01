#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhangminpeng on 01/11/2017.

# from btp.util import postman, trackers, fetcher
#
# if __name__ == '__main__':
#     url = trackers.get_trackers_url()
#     content = fetcher.get_trackers_content(url)
#     if content:
#         url_list = fetcher.parse_content(content)
#         aria2_jsonrpc_url = 'aria2_jsonrpc_url'
#         aria2_jsonrpc_token = 'aria2_jsonrpc_url'
#         result = postman.push(aria2_jsonrpc_url, aria2_jsonrpc_token, url_list)
#         print(result)
#
#     else:
#         print('not content')

import importlib
import argparse
from argparse import RawTextHelpFormatter

trackers = importlib.import_module('util.trackers')

parser = argparse.ArgumentParser(
    prog='btp',
    formatter_class=RawTextHelpFormatter
)

# aria2 server jsonrpc url
parser.add_argument(
    'jsonrpc_url',
    metavar='jsonrpc_url',
    type=str,
    help='target aria2 server jsonrpc url'
)

# aria2 server jsonrpc token
parser.add_argument(
    'jsonrpc_token',
    metavar='jsonrpc_token',
    type=str,
    help='target aria2 server jsonrpc token'
)

# trackers url
parser.add_argument(
    '-i', '--index',
    metavar='index',
    choices=range(len(trackers.TRACKERS_URL_LIST)),
    type=int,
    help='0 - trackers_best (DEFAULT)\n'
         '1 - trackers_all\n'
         '2 - trackers_all_udp\n'
         '3 - trackers_all_http\n'
         '4 - trackers_all_https\n'
         '5 - trackers_best_ip\n'
         '6 - trackers_all_ip\n'
         'more detail: https://github.com/ngosang/trackerslist\n'
)

# request proxy
parser.add_argument(
    '-p', '--proxy',
    metavar='proxy',
    type=str,
    help='request proxy, http proxy or socks proxy likes: \n'
         'http://user:password@10.1.1.1:8080, socks5://127.0.0.1:1086'
)

args = parser.parse_args()
