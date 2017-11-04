# -*- coding: utf-8 -*-
# Created by asmoker on 01/11/2017.

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from btp.util import req

MAX_RETRIES = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
HTTP_ADAPTER = HTTPAdapter(max_retries=MAX_RETRIES)


def __get_session(url):
    session = requests.Session()
    session.mount(url, HTTP_ADAPTER)
    return session


def get_trackers_content(url, proxy=None):
    return __get_session(url).get(url, proxies=req.build_proxies(proxy)).text


def parse_content(content):
    return [item.strip() for item in content.split('\n') if item.strip()]
