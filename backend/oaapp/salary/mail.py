#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import oaapp.models as _db
from common import error, mail, login
import json

@error.error_decorator
def do_post(request, args, kwargs):

    req = json.loads(request.body.decode())
    username = req['username']
    cookie = req['cookie']
    month = req['month']
    ids = req['ids']  # 多个id之间以逗号分隔

    # username = request.POST.get('username', '')
    # cookie = request.POST.get('cookie', '')
    if not login.is_login(username, cookie):
        return {'errorno': 1, 'error_msg_en': 'Error', 'error_msg_zh': '请重新登录'}
    
    # 管理员是否有email_address
    user_rows = _db.User.objects.filter(row_status=True, username=username)
    sender_email_address, sender_email_password = user_rows[0].email_address, user_rows[0].email_password
    if (not sender_email_address) or (not sender_email_password):
        return {'errorno': 1, 'error_msg_en': 'Error', 'error_msg_zh': '管理员邮箱地址未正确配置，不能发送邮件！'}
    
    # ids = request.POST['ids']  # 多个id之间以逗号分隔
    salary_rows = None
    head_keys= []

    if ids == "all":
        salary_rows = _db.Salary.objects.filter(row_status=True, month=month).order_by('id')
    else:  # 需要把表头的id也传过来
        id_list = ids.strip().split(",")
        salary_rows = _db.Salary.objects.filter(row_status=True, month=month, id__in=id_list).order_by('id')
    
    for salary_row in salary_rows:
        # 
        if salary_row.is_head == True and salary_row.col_num > 0:
            # 纯表头
            for j in range(salary_row.col_num):
                v_name = 'v' + str((j+1))  # j从0开始，v_name从v1开始
                head_keys.append(getattr(salary_row, v_name, v_name))
            continue
        
        # 真正的xinzi数据(排除掉表头)
        if not salary_row.email_address:
            continue

        salary_row_value = []
        for jj in range(salary_row.col_num):
            v_name = 'v' + str((jj+1))  # j从0开始，v_name从v1开始
            salary_row_value.append(getattr(salary_row, v_name, v_name))
        
        # 发送邮件
        is_success, result = mail.send_email(
            sender_email_address, sender_email_password, 
            salary_row.email_address, salary_row.month,
            head_keys, salary_row_value,
        )
        
        # 保存结果
        _db.MailHistory.objects.create(salary_id=salary_row.id, status=is_success, result=result,)

    res = {'errorno': 0, 'data': {}}
    
    return res