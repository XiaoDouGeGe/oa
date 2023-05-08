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
    
    detail = []
    salary_rows = _db.Salary.objects.filter(row_status=True, month=month, name__contains=key).order_by('id')
    for salary_row in salary_rows:
        # send_ok 发送成功过，不表示最近一次是成功，初始值是False。
        # lastest_ok，最近一次发送成功，初始值是False。
        send_ok, lastest_ok, history_list = False, False, []
        history_rows = _db.MailHistory.objects.filter(row_status=True, salary_id=salary_row.id).order_by('-id')
        if len(history_rows) > 0 and history_rows[0].status:
            lastest_ok = True

        # 
        for history_row in history_rows:
            # 发送成功过，没有else
            if history_row.status:
                send_ok = True 
            # 
            history_item = {
                'id': history_row.id,
                'send_time': history_row.create_time,
                'status': history_row.status,
                'result': history_row.result,
            }
            history_list.append(history_item)
        
        # 封装数据
        item = {
            'id': salary_row.id,
            'name': salary_row.name,
            'position': salary_row.position,
            'bank_number': salary_row.bank_number,
            'base_pay': salary_row.base_pay,
            'seniority_pay': salary_row.seniority_pay,
            'title_pay': salary_row.title_pay,
            'academic_pay': salary_row.academic_pay,
            'assessment_bonus': salary_row.assessment_bonus,
            'housing_supplement': salary_row.housing_supplement,
            'total_pay': salary_row.total_pay,
            'pension': salary_row.pension,
            'medical_insurance': salary_row.medical_insurance,
            'unemployment': salary_row.unemployment,
            'accumulation_fund': salary_row.accumulation_fund,
            'income_tax': salary_row.income_tax,
            'union_fee': salary_row.union_fee,
            'total_deduction': salary_row.total_deduction,
            'paidin_amount': salary_row.paidin_amount,
            'phone_number': salary_row.phone_number,
            'email_address': salary_row.email_address,
            'month': salary_row.month,
            'create_time': salary_row.create_time,
            'send_ok': send_ok,
            'lastest_ok': lastest_ok,
            'mail_history': history_list,
        }

        detail.append(item)

    page = int(request.GET.get('page',1))
    pagesize = int(request.GET.get('pagesize',len(detail)))
    start_count = (page-1) * pagesize
    end_count = page * pagesize

    res = {'errorno': 0, 'data': {'all':len(detail), 'page':page, 'pagesize':pagesize, 'detail': detail[start_count:end_count]}}

    return  res
