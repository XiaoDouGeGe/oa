#!/bin/env python
# -*- coding: UTF-8 -*-

from openpyxl import load_workbook
import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''

'''

class Test:
    def ck_log(self):
        pass

    def send_email(self, econtent, ename, mail):
        host = 'smtp.126.com'
        user = 'gooddou91@126.com'
        password = 'DSTIQNIEGHJBCHUT'
        receivers = [mail]
        subject = '员工工资表'

        msg = MIMEText(econtent, 'html', 'utf-8')
        msg['From'] = Header('youxian gongsi')
        msg['To'] = Header(ename)
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            obj = smtplib.SMTP_SSL(host, 465)
            obj.login(user, password)
            obj.sendmail(user, receivers, msg.as_string())
            print("send email success!")
        except smtplib.SMTPException as e:
            print("Error: send email failed!")
            print(e)



wb = load_workbook('./2023-02.xlsx')
o = Test()
cnt = 0
sheet = wb.active
thead = '<thead>'



for row in sheet:
    print("begin...")

    tbody = '<tr>'
    cnt += 1
    print("cnt="+str(cnt))
    if cnt == 1:
        for cell in row:
            thead += '<th>' + str(cell.value) + '</th>'
        thead += '</thead>'
    else:
        for cell in row:
            tbody += '<td>' + str(cell.value) + '</td>'
        tbody += '</tr>'
    name = row[0].value
    mail = row[1].value

    content = "<h3>" + name + ",hello</h3>" + "<p>2023-02 Salary</p>" + "<table border='1px solid black'>" + thead + tbody + "</table>"
        

    if cnt >= 3:
        print('content:', content)
        print(name, mail)
        o.send_email(content, name, 'gooddou91@126.com')
    
    print("end...")
