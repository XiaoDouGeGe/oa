#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from decimal import Decimal

def str2num(str):
    if (not str) or (not str.strip()):
        return '-'
    return Decimal(float(str)).quantize(Decimal("0.00"))
    