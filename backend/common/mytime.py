#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pytz
from datetime import datetime

def utc2cst(utc_time):
    utc_tz = pytz.timezone('UTC')
    cst_tz = pytz.timezone('Asia/Shanghai')
    cst_time = utc_tz.localize(utc_time).astimezone(cst_tz)
    return cst_time
