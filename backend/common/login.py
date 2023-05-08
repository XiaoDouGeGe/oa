#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys
import django
defaultencoding = 'utf-8'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../oa")))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oa.settings')
django.setup()

import oaapp.models as _db
import datetime
from common import encryption

def is_login(username, cookie):
    # 1.cookie无效或过期
    if len(encryption.str_base64_decode(cookie)) < 8 or (encryption.str_base64_decode(cookie)[:8] != datetime.datetime.now().strftime('%Y%m%d')):
        return False

    # 2.查不到
    user_rows = _db.User.objects.filter(row_status=True, username=username, cookie=cookie)
    if len(user_rows) == 0:
        return False

    return True
    