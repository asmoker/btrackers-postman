# -*- coding: utf-8 -*-
# Created by asmoekr on 04/11/2017.

from unittest import TestCase

from btp.run import main


class TestConsole(TestCase):
    def test_basic(self):
        main()
