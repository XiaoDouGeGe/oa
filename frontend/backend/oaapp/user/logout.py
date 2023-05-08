#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import oaapp.models as _db
from common import error
import json

@error.error_decorator
def do_post(request, args, kwargs):
    
    # username = request.POST.get('username', '')
    # cookie = request.POST.get('cookie', '')

    req = json.loads(request.body.decode())
    username = req.get('username', '')
    cookie = req.get('cookie', '')

    _db.User.objects.filter(row_status=True, username=username, cookie=cookie).update(cookie='')

    res = {'errorno': 0, 'data': {}}
    
    return res
    