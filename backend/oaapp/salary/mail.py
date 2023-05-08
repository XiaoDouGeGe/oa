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

    if ids == "all":
        salary_rows = _db.Salary.objects.filter(row_status=True, month=month)
    else:
        id_list = ids.strip().split(",")
        salary_rows = _db.Salary.objects.filter(row_status=True, month=month, id__in=id_list)
    
    for salary_row in salary_rows:

        if not salary_row.email_address:
            continue

        # 发送邮件
        is_success, result = mail.send_email(
            sender_email_address, sender_email_password,
            salary_row.name, salary_row.position, salary_row.bank_number, salary_row.base_pay, 
            salary_row.seniority_pay, salary_row.title_pay, salary_row.academic_pay, 
            salary_row.assessment_bonus, salary_row.housing_supplement, salary_row.total_pay, 
            salary_row.pension, salary_row.medical_insurance, salary_row.unemployment,
            salary_row.accumulation_fund, salary_row.income_tax, salary_row.union_fee, 
            salary_row.total_deduction, salary_row.paidin_amount, salary_row.phone_number, 
            salary_row.email_address, salary_row.month,
        )
        
        # 保存结果
        _db.MailHistory.objects.create(salary_id=salary_row.id, status=is_success, result=result,)

    res = {'errorno': 0, 'data': {}}
    
    return res