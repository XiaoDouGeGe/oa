#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import oaapp.models as _db
from common import error, login, mytime

@error.error_decorator
def get_data(request, args, kwargs):
    
    username = request.GET.get('username', '')
    cookie = request.GET.get('cookie', '')
    if not login.is_login(username, cookie):
        return {'errorno': 1, 'error_msg_en': 'Error', 'error_msg_zh': '请重新登录'}

    month = request.GET.get('month', '')
    key = request.GET.get('key', '')
    head_keys= []
    detail = []
    salary_rows = _db.Salary.objects.filter(row_status=True, month=month).order_by('id')
    for salary_row in salary_rows:
        if salary_row.is_head == True and salary_row.col_num > 0:
            # 表头，与前端约定：前6个不展示
            head_keys = [salary_row.id, salary_row.month, salary_row.create_time, salary_row.is_head, salary_row.col_num, salary_row.email_address]
            for j in range(salary_row.col_num):
                v_name = 'v' + str((j+1))  # j从0开始，v_name从v1开始
                head_keys.append(getattr(salary_row, v_name, v_name))
            head_keys.append(u'最近发送')  
            continue

        # 模糊查询
        is_mohu = False  # false表示不满足模糊条件
        if not key:
            is_mohu = True

        salary_row_value = [salary_row.id, salary_row.month, salary_row.create_time, salary_row.is_head, salary_row.col_num, salary_row.email_address]
        
        for jj in range(salary_row.col_num):
            v_name = 'v' + str((jj+1))  # j从0开始，v_name从v1开始
            salary_row_value.append(getattr(salary_row, v_name, v_name))

            if not is_mohu and key in str(getattr(salary_row, v_name, v_name)):
                is_mohu = True

        if not is_mohu:
            continue

        # lastest_ok，最近一次发送成功，初始值是False。
        lastest_ok = False
        history_rows = _db.MailHistory.objects.filter(row_status=True, salary_id=salary_row.id).order_by('-id')
        if len(history_rows) > 0 and history_rows[0].status:
            lastest_ok = True
        
        salary_row_value.append(lastest_ok)

        detail.append(salary_row_value)

    page = int(request.GET.get('page',1))
    pagesize = int(request.GET.get('pagesize',len(detail)))
    start_count = (page-1) * pagesize
    end_count = page * pagesize

    res = {'errorno': 0, 'data': {'all':len(detail), 'page':page, 'pagesize':pagesize, 'detail': detail[start_count:end_count], 'head_keys': head_keys}}

    return  res
