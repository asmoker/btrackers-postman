# -*- coding: utf-8 -*-
# Created by zhangminpeng on 01/11/2017.

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

MAX_RETRIES = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
HTTP_ADAPTER = HTTPAdapter(max_retries=MAX_RETRIES)
TIMEOUT = 10
PROXY = 'socks5://127.0.0.1:1086'
PROXY_DICT = {
    'https': PROXY,
    'http': PROXY
}


def __get_session(url):
    session = requests.Session()
    session.mount(url, HTTP_ADAPTER)
    return session


def get_trackers_content(url):
    return __get_session(url).get(url, timeout=TIMEOUT, proxies=PROXY_DICT).text


def parse_content(content):
    return [item.strip() for item in content.split('\n') if item.strip()]
