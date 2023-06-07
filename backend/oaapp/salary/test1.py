#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import xlrd
import sys
import importlib
importlib.reload(sys)

file_path = './xxx.xls'
book = xlrd.open_workbook(file_path)
sheet = book.sheet_by_index(0)  # 第1个sheet页
for i in range(sheet.nrows):
    rows = str(sheet.row_values(i))  # 一行一行的读
    row = eval(rows)  # 此为某一行数据
    for j in range(len(row)):
        print(row[j])