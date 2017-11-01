# -*- coding: utf-8 -*-
# Created by zhangminpeng on 01/11/2017.

from btp.util import postman, trackers, fetcher

if __name__ == '__main__':
    url = trackers.get_trackers_url()
    content = fetcher.get_trackers_content(url)
    if content:
        url_list = fetcher.parse_content(content)
        aria2_jsonrpc_url = 'aria2_jsonrpc_url'
        aria2_jsonrpc_token = 'aria2_jsonrpc_url'
        result = postman.push(aria2_jsonrpc_url, aria2_jsonrpc_token, url_list)
        print(result)

    else:
        print('not content')
