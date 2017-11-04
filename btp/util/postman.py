# -*- coding: utf-8 -*-
# Created by asmoker on 01/11/2017.
import uuid

import requests

from btp.util import req


def __build_post_body(token, url_list):
    return {
        'jsonrpc': '2.0',
        'method': 'aria2.changeGlobalOption',
        'id': str(uuid.uuid4()),
        'params': [
            'token:{token}'.format(token=token),
            {
                'bt-tracker': ','.join(url_list)
            }
        ]
    }


def push(aria2_jsonrpc_url, aria2_jsonrpc_token, url_list, proxy=None):
    post_body = __build_post_body(aria2_jsonrpc_token, url_list)
    resp = requests.post(aria2_jsonrpc_url, json=post_body, proxies=req.build_proxies(proxy)).json()
    if resp and 'result' in resp and resp['result'] == 'OK':
        return True
    return False
