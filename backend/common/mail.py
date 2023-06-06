#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


'''
is_success, result = mail.send_email(
    sender_email_address, sender_email_password, 
    salary_row.email_address, salary_row.month,
    head_keys, salary_row_value,
)
'''
def send_email(sender_email_address, sender_email_password, receiver_email_address, month, head_keys, salary_row_value):
    
    content = set_content(head_keys, salary_row_value)
    
    is_success, result = send(sender_email_address, sender_email_password, '我', receiver_email_address, month, content)

    return is_success, result


# 拼装内容格式
def set_content(head_keys, salary_row_value):
    content = '''
<table border="1">
    '''

    num = len(head_keys)
    
    for i in range(num):
      if (i+1) % 4 == 1:
        content += '''
  <tr>
    <td bgcolor="#f8f8f8" width=80px height=50px style="padding:0 5px;"><b>%s</b></td>
    <td width=120px style="padding:0 5px;">%s</td>
        ''' % (head_keys[i], salary_row_value[i])
      elif (i+1) % 4 == 0:
        content += '''
    <td bgcolor="#f8f8f8" width=80px style="padding:0 5px;"><b>%s</b></td>
    <td width=120px style="padding:0 5px;">%s</td>
  </tr>
        ''' % (head_keys[i], salary_row_value[i])
      else:
        content += '''
    <td bgcolor="#f8f8f8" width=80px style="padding:0 5px;"><b>%s</b></td>
    <td width=120px style="padding:0 5px;">%s</td>
        ''' % (head_keys[i], salary_row_value[i])
    

    if num % 4 == 0:
      content += '''
</table>
      '''
    else:
      content += '''
  </tr>
</table>
      '''

    return content


# 发送
def send(sender_email_address, sender_email_password, name, receiver_email_address, month, content):
    
    is_success, result = True, ''

    host = 'smtp.126.com'
    if sender_email_address.endswith('163.com'):
        host = 'smtp.163.com'

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
        
