#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(sender_email_address, sender_email_password, name, position, bank_number, base_pay, 
        seniority_pay, title_pay, academic_pay, assessment_bonus, housing_supplement, total_pay, 
        pension, medical_insurance, unemployment, accumulation_fund, income_tax, union_fee, 
        total_deduction, paidin_amount, phone_number, receiver_email_address, month):
    
    content = set_content(name, position, bank_number, base_pay, seniority_pay, title_pay, academic_pay, 
        assessment_bonus, housing_supplement, total_pay, pension, medical_insurance, unemployment,
        accumulation_fund, income_tax, union_fee, total_deduction, paidin_amount)
    
    is_success, result = send(sender_email_address, sender_email_password, name, receiver_email_address, 
        month, content)

    return is_success, result


# 拼装内容格式
def set_content(name, position, bank_number, base_pay, seniority_pay, title_pay, academic_pay, 
        assessment_bonus, housing_supplement, total_pay, pension, medical_insurance, unemployment,
        accumulation_fund, income_tax, union_fee, total_deduction, paidin_amount):
    
    content = '''
<table border="1">
  <tr>
    <td bgcolor="#f8f8f8" width=80px height=50px style="padding:0 5px;"><b>姓名</b></td>
    <td width=120px style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" width=80px style="padding:0 5px;"><b>岗位</b></td>
    <td width=120px style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" width=80px style="padding:0 5px;"><b>银行卡号</b></td>
    <td width=120px style="word-break:break-all;padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" width=80px style="padding:0 5px;"><b>基本工资</b></td>
    <td width=120px style="padding:0 5px;">%s</td>
  </tr>
  <tr>
    <td bgcolor="#f8f8f8" height=50px style="padding:0 5px;"><b>工龄工资</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>职称工资</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>学历工资</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>考核奖金</b></td>
    <td style="padding:0 5px;">%s</td>
  </tr>
  <tr>
    <td bgcolor="#f8f8f8" height=50px style="padding:0 5px;"><b>房补</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>应发合计</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>养老</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>医保</b></td>
    <td style="padding:0 5px;">%s</td>
  </tr>
  <tr>
    <td bgcolor="#f8f8f8" height=50px style="padding:0 5px;"><b>失业</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>公积金</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>个税</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>工会费</b></td>
    <td style="padding:0 5px;">%s</td>
  </tr>
  <tr>
    <td bgcolor="#f8f8f8" height=50px style="padding:0 5px;"><b>扣款合计</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>实发金额</b></td>
    <td style="padding:0 5px;">%s</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>其他</b></td>
    <td style="padding:0 5px;">-</td>
    <td bgcolor="#f8f8f8" style="padding:0 5px;"><b>备注</b></td>
    <td style="padding:0 5px;">-</td>
  </tr>
</table>
    ''' % (name, position, bank_number, base_pay, seniority_pay, title_pay, academic_pay, 
    assessment_bonus, housing_supplement, total_pay, pension, medical_insurance, unemployment, 
    accumulation_fund, income_tax, union_fee, total_deduction, paidin_amount)

    return content

# 发送
def send(sender_email_address, sender_email_password, name, receiver_email_address, month, content):
    
    is_success, result = True, ''

    host = 'smtp.126.com'
    subject = month + u' 工资，请查收！'

    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = _format_addr('淮安工业园区人民医院 <%s>' % sender_email_address)
    msg['To'] = _format_addr('%s <%s>' % (name, receiver_email_address))
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        obj = smtplib.SMTP_SSL(host, 465)
        obj.login(sender_email_address, sender_email_password)
        obj.sendmail(sender_email_address, [receiver_email_address], msg.as_string())
        print("send email success!")
    except smtplib.SMTPException as e:
        print("Error: send email failed!")
        is_success, result = False, str(e)
    
    return is_success, result
        
