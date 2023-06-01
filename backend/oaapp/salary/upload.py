#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import oaapp.models as _db
from django.db import transaction
from common import error, num, login
import xlrd
import datetime
import json
import sys
import importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

@error.error_decorator
def do_post(request, args, kwargs):

    # req = json.loads(request.body.decode())
    # username = req.get('username', '')
    # cookie = req.get('cookie', '')

    username = request.POST.get('username', '')
    cookie = request.POST.get('cookie', '')

    if not login.is_login(username, cookie):
        return {'errorno': 1, 'error_msg_en': 'Error', 'error_msg_zh': '请重新登录'}

    salary_excel = request.FILES.get('salary_excel')
    month = request.POST['month']

    if salary_excel is None:
        res = {"errorno": "S9999", "error_msg_en": "Error", "error_msg_zh": "请选择要上传的文件"}
        return res
    
    file_path = '/projects/oa/files/salary_excel/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_' + salary_excel.name
    
    file_path = file_path.encode('UTF-8')

    # 1.上传至指定目录，加以时间戳保存文件
    with open(file_path, 'wb') as f:
        for i in salary_excel.readlines():
            f.write(i)
    
    # 2.写入pg
    book = xlrd.open_workbook(file_path)
    sheet = book.sheet_by_index(0)  # 第1个sheet页
    v_email = -1  # 邮箱是第x列，从0开始
    # nrows = sheet.nrows  # 行数
    # ncols = sheet.ncols  # 列数
    with transaction.atomic():
        for i in range(sheet.nrows):
            if i == 0:
                salary_row = _db.Salary.objects.create(month=month, is_head=True, col_num=sheet.ncols)
            else:
                salary_row = _db.Salary.objects.create(month=month, is_head=False, col_num=sheet.ncols)
            
            rows = str(sheet.row_values(i))  # 一行一行的读
            row = eval(rows)  # 此为某一行数据
            
            for j in range(len(row)):  # 遍历当前行的每个数据
                if row[j] == u'邮箱':
                    v_email = j   # 循环体内，该值不重置

                v_name = 'v' + str((j+1))  # j从0开始，v_name从v1开始
                setattr(salary_row, v_name, row[j])

            salary_row.email_address = row[v_email] if v_email > -1
            
            salary_row.save()

    res = {'errorno': 0, 'data': {}}
    
    return res