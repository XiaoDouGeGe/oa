#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import oaapp.models as _db
from common import error, encryption
import base64
import datetime
import json

@error.error_decorator
def do_post(request, args, kwargs):
    
    # username = request.POST.get('username', '')
    # password = request.POST.get('password', '')

    req = json.loads(request.body.decode())
    username = req.get('username', '')
    password = req.get('password', '')
    
    password_encryption = encryption.str_md5(password)

    user_rows = _db.User.objects.filter(row_status=True, username=username, password=password_encryption)
    
    if len(user_rows) == 0:
        return {'errorno': 1, 'error_msg_en': 'Error', 'error_msg_zh': '账号或密码错误'}
    
    user_row = user_rows[0]  # 用户名不会重复，只有1条记录

    # 更新cookie
    cookie_old = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + username
    cookie_new = encryption.str_base64_encode(cookie_old)
    user_row.cookie = cookie_new
    user_row.save()

    res = {
        'errorno': 0, 
        'data': {
            'cookie': cookie_new,
        },
        'error_msg_en': '', 
        'error_msg_zh': '登录成功',
        }
    
    return res