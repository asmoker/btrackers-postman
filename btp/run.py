#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by asmoker on 01/11/2017.


import argparse
import importlib
from argparse import RawTextHelpFormatter

from btp.util import fetcher, postman

trackers = importlib.import_module('btp.util.trackers')

parser = argparse.ArgumentParser(
    prog='btp',
    formatter_class=RawTextHelpFormatter
)

# aria2 server jsonrpc url
parser.add_argument(
    'jsonrpc_url',
    metavar='jsonrpc_url',
    type=str,
    help='Target aria2 server jsonrpc url'
)

# aria2 server jsonrpc token
parser.add_argument(
    'jsonrpc_token',
    metavar='jsonrpc_token',
    type=str,
    help='Target aria2 server jsonrpc token'
)

# trackers url
parser.add_argument(
    '-i', '--index',
    metavar='index',
    choices=range(len(trackers.TRACKERS_URL_LIST)),
    type=int,
    default=0,
    help='0 - trackers_best (DEFAULT)\n'
         '1 - trackers_all\n'
         '2 - trackers_all_udp\n'
         '3 - trackers_all_http\n'
         '4 - trackers_all_https\n'
         '5 - trackers_best_ip\n'
         '6 - trackers_all_ip\n'
         'More detail: https://github.com/ngosang/trackerslist\n'
)

# request proxy
parser.add_argument(
    '-p', '--proxy',
    metavar='proxy',
    type=str,
    help='Request proxy, http proxy or socks proxy likes: \n'
         'http://user:password@10.1.1.6:8080 or socks5://127.0.0.1:1086'
)


def main():
    try:
        args = parser.parse_args()
        url = trackers.get_trackers_url(args.index)
        try:
            content = fetcher.get_trackers_content(url, proxy=args.proxy)
            if content:
                url_list = fetcher.parse_content(content)
                if not url_list:
                    print('Tracker urls empty, more detail: https://github.com/ngosang/trackerslist')
                else:
                    result = postman.push(args.jsonrpc_url, args.jsonrpc_token, url_list, proxy=args.proxy)
                    if result:
                        print('Success.')
                    else:
                        print('Failed to post urls to aria2 server.')

            else:
                print('Failed to get tracker urls from github.')
        except Exception as e:
            print('Exception, please try again later:\n    %s' % str(e))
    except:
        pass
