#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import hashlib
import base64

def str_md5(ss):
    return hashlib.md5(ss.encode("utf-8")).hexdigest()

def str_base64_encode(ss):
    return str(base64.b64encode(ss.encode("utf-8")), "utf-8")

def str_base64_decode(ss):
    return str(base64.b64decode(ss), "utf-8")
