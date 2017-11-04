# -*- coding: utf-8 -*-
# Created by byte on 02/11/2017.


def build_proxies(proxy=None):
    if proxy:
        return {
            'http': proxy,
            'https': proxy
        }
    return None
