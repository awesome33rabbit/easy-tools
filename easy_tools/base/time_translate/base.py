#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : pu mingzheng <pumz_1991@126.com>
# @Time     : 2023/03/20 09:45:31
# @File     : easy_tools/base/time_translate - base.py
# @Software : python3.11 PyCharm
# @Desc     : TODO

import datetime

import pytz

default_tz = pytz.timezone("Asia/Shanghai")


def timestamp_to_datetime(timestamp: int, timezone=default_tz) -> str:
    """

    :param timestamp: 10 位时间戳
    :param timezone: 时区
    :return:
    """
    res = datetime.datetime.fromtimestamp(timestamp, timezone).strftime("%Y-%m-%d %H:%M:%S")
    return res


# poetry install --with group_name

# poetry add py-easy-tools[center]
# pip install py-easy-tools[center]

# poetry install --extras "mysql pgsql"
# poetry install -E mysql -E pgsql
# poetry install --all-extras


# django =[{version = "3.2.17", python = "^2.7"},{version = "4.1.7", python = "^3.9"}]
