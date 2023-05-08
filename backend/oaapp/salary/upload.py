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
    # nrows = sheet.nrows  # 行数
    # ncols = sheet.ncols  # 列数
    with transaction.atomic():
        for i in range(2, sheet.nrows):  # 第1-2行为表头，不读
            rows = str(sheet.row_values(i))  # 一行一行的读
            row = eval(rows)  # 此为某一行数据
            # 插入数据，不需要row[0]
            salary_row = _db.Salary.objects.create(
                name=row[1], position=row[2], bank_number=row[3], base_pay=str(num.str2num(str(row[4]))), seniority_pay=str(num.str2num(str(row[5]))),
                title_pay=str(num.str2num(str(row[6]))), academic_pay=str(num.str2num(str(row[7]))), assessment_bonus=str(num.str2num(str(row[8]))), 
                housing_supplement=str(num.str2num(str(row[9]))), total_pay=str(num.str2num(str(row[10]))), pension=str(num.str2num(str(row[11]))), 
                medical_insurance=str(num.str2num(str(row[12]))), unemployment=str(num.str2num(str(row[13]))), accumulation_fund=str(num.str2num(str(row[14]))), 
                income_tax=str(num.str2num(str(row[15]))), union_fee=str(num.str2num(str(row[16]))), total_deduction=str(num.str2num(str(row[17]))), 
                paidin_amount=str(num.str2num(str(row[18]))), phone_number=str(row[19]).split('.')[0], email_address=row[20], month=month,
            )

    res = {'errorno': 0, 'data': {}}
    
    return res