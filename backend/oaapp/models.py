from django.db import models

# Create your models here.


# 管理员
class User(models.Model):
    # 序号
    id = models.AutoField(primary_key=True)
    # 数据状态 False假删除
    row_status = models.BooleanField(default=True)
    # 用户名
    username = models.CharField(max_length=16)
    # 密码
    password = models.CharField(max_length=128)
    # 手机号码
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    # 邮箱地址
    email_address = models.CharField(max_length=128, blank=True, null=True)
    # 邮箱密码
    email_password = models.CharField(max_length=32, blank=True, null=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # cookie
    cookie = models.CharField(max_length=128, blank=True, null=True)
    
    class Meta():
        db_table = 'user'


# 工资条
class Salary(models.Model):
    # 自增序号
    id = models.AutoField(primary_key=True)
    # 数据状态 False假删除
    row_status = models.BooleanField(default=True)
    # 年月 2020-02 2020年2月 
    month = models.CharField(max_length=10, blank=True, null=True)
    # 上传时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 是否是表头
    is_head = models.BooleanField(default=False)
    # 数据的列数
    col_num = models.IntegerField(default=0)
    # 邮箱地址 单拎出来
    email_address = models.CharField(max_length=64, blank=True, null=True)
    # V1 第一列的数据（含表头）
    v1 = models.CharField(max_length=128, blank=True, null=True)
    # V2 
    v2 = models.CharField(max_length=128, blank=True, null=True)
    # V3 
    v3 = models.CharField(max_length=128, blank=True, null=True)
    # V4 
    v4 = models.CharField(max_length=128, blank=True, null=True)
    # V5 
    v5 = models.CharField(max_length=128, blank=True, null=True)
    # V6 
    v6 = models.CharField(max_length=128, blank=True, null=True)
    # V7 
    v7 = models.CharField(max_length=128, blank=True, null=True)
    # V8 
    v8 = models.CharField(max_length=128, blank=True, null=True)
    # V9 
    v9 = models.CharField(max_length=128, blank=True, null=True)
    # V10 
    v10 = models.CharField(max_length=128, blank=True, null=True)
    # V11 
    v11 = models.CharField(max_length=128, blank=True, null=True)
    # V12 
    v12 = models.CharField(max_length=128, blank=True, null=True)
    # V13 
    v13 = models.CharField(max_length=128, blank=True, null=True)
    # V14 
    v14 = models.CharField(max_length=128, blank=True, null=True)
    # V15 
    v15 = models.CharField(max_length=128, blank=True, null=True)
    # V16 
    v16 = models.CharField(max_length=128, blank=True, null=True)
    # V17 
    v17 = models.CharField(max_length=128, blank=True, null=True)
    # V18 
    v18 = models.CharField(max_length=128, blank=True, null=True)
    # V19 
    v19 = models.CharField(max_length=128, blank=True, null=True)
    # V20 
    v20 = models.CharField(max_length=128, blank=True, null=True)
    # V21 
    v21 = models.CharField(max_length=128, blank=True, null=True)
    # V22 
    v22 = models.CharField(max_length=128, blank=True, null=True)
    # V23 
    v23 = models.CharField(max_length=128, blank=True, null=True)
    # V24 
    v24 = models.CharField(max_length=128, blank=True, null=True)
    # V25 
    v25 = models.CharField(max_length=128, blank=True, null=True)
    # V26 
    v26 = models.CharField(max_length=128, blank=True, null=True)
    # V27 
    v27 = models.CharField(max_length=128, blank=True, null=True)
    # V28 
    v28 = models.CharField(max_length=128, blank=True, null=True)
    # V29 
    v29 = models.CharField(max_length=128, blank=True, null=True)
    # V30 
    v30 = models.CharField(max_length=128, blank=True, null=True)
    # V31 
    v31 = models.CharField(max_length=128, blank=True, null=True)
    # V32 
    v32 = models.CharField(max_length=128, blank=True, null=True)
    # V33 
    v33 = models.CharField(max_length=128, blank=True, null=True)
    # V34 
    v34 = models.CharField(max_length=128, blank=True, null=True)
    # V35 
    v35 = models.CharField(max_length=128, blank=True, null=True)
    # V36 
    v36 = models.CharField(max_length=128, blank=True, null=True)
    # V37 
    v37 = models.CharField(max_length=128, blank=True, null=True)
    # V38 
    v38 = models.CharField(max_length=128, blank=True, null=True)
    # V39 
    v39 = models.CharField(max_length=128, blank=True, null=True)
    # V40 
    v40 = models.CharField(max_length=128, blank=True, null=True)
    # V41 
    v41 = models.CharField(max_length=128, blank=True, null=True)
    # V42 
    v42 = models.CharField(max_length=128, blank=True, null=True)
    # V43 
    v43 = models.CharField(max_length=128, blank=True, null=True)
    # V44 
    v44 = models.CharField(max_length=128, blank=True, null=True)
    # V45 
    v45 = models.CharField(max_length=128, blank=True, null=True)
    # V46 
    v46 = models.CharField(max_length=128, blank=True, null=True)
    # V47 
    v47 = models.CharField(max_length=128, blank=True, null=True)
    # V48 
    v48 = models.CharField(max_length=128, blank=True, null=True)
    # V49 
    v49 = models.CharField(max_length=128, blank=True, null=True)
    # V50 
    v50 = models.CharField(max_length=128, blank=True, null=True)

    class Meta():
        db_table = 'salary'


# 发送邮件的记录
class MailHistory(models.Model):
    # 序号
    id = models.AutoField(primary_key=True)
    # 数据状态 False假删除
    row_status = models.BooleanField(default=True)
    # 工资条序号（不使用外键）
    salary_id = models.CharField(max_length=32, blank=True, null=True)
    # 发送时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 成功or失败
    status = models.BooleanField()
    # 结果详情
    result = models.TextField(blank=True, null=True)

    class Meta():
        db_table = 'mailhistory'
