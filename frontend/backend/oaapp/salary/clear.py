#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import oaapp.models as _db
from common import error, login
import json

@error.error_decorator
def do_post(request, args, kwargs):

    # username = request.POST.get('username', '')
    # cookie = request.POST.get('cookie', '')
    # month = request.POST['month']

    req = json.loads(request.body.decode())
    username = req.get('username', '')
    cookie = req.get('cookie', '')
    month = req['month']

    if not login.is_login(username, cookie):
        return {'errorno': 1, 'error_msg_en': 'Error', 'error_msg_zh': '请重新登录'}

    _db.Salary.objects.filter(row_status=True, month=month).update(row_status=False)

    res = {'errorno': 0, 'data': {}}
    
    return res