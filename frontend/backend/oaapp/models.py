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
    # 姓名
    name = models.CharField(max_length=32, blank=True, null=True)
    # 岗位
    position = models.CharField(max_length=32, blank=True, null=True)
    # 银行卡号
    bank_number = models.CharField(max_length=32, blank=True, null=True)
    # 基本工资
    base_pay = models.CharField(max_length=10, blank=True, null=True)
    # 工龄工资
    seniority_pay = models.CharField(max_length=10, blank=True, null=True)
    # 职称工资
    title_pay = models.CharField(max_length=10, blank=True, null=True)
    # 学历工资
    academic_pay = models.CharField(max_length=10, blank=True, null=True)
    # 考核奖金
    assessment_bonus = models.CharField(max_length=10, blank=True, null=True)
    # 房补
    housing_supplement = models.CharField(max_length=10, blank=True, null=True)
    # 应发合计
    total_pay = models.CharField(max_length=10, blank=True, null=True)
    # 养老
    pension = models.CharField(max_length=10, blank=True, null=True)
    # 医保
    medical_insurance = models.CharField(max_length=10, blank=True, null=True)
    # 失业
    unemployment = models.CharField(max_length=10, blank=True, null=True)
    # 公积金
    accumulation_fund = models.CharField(max_length=10, blank=True, null=True)
    # 个税
    income_tax = models.CharField(max_length=10, blank=True, null=True)
    # 工会费
    union_fee = models.CharField(max_length=10, blank=True, null=True)
    # 扣款合计
    total_deduction = models.CharField(max_length=10, blank=True, null=True)
    # 实发金额
    paidin_amount = models.CharField(max_length=10, blank=True, null=True)
    # 手机号码
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    # 邮箱地址
    email_address = models.CharField(max_length=32, blank=True, null=True)
    # 年月 2020-02 2020年2月 
    month = models.CharField(max_length=10, blank=True, null=True)
    # 上传时间
    create_time = models.DateTimeField(auto_now_add=True)

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
