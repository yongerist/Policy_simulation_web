from django.contrib.auth.models import UserManager
from django.db import models
from django.db import models


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(max_length=32, verbose_name='标题')

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(max_length=16, verbose_name='姓名')
    password = models.CharField(max_length=64, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='入职时间', null=True, blank=True)
    depart = models.ForeignKey(to='Department', to_field="id", on_delete=models.CASCADE, verbose_name="部门", null=True,
                               blank=True)
    gender_choices = (
        (1, "男"),
        (0, "女"),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, null=True, blank=True)


class Target(models.Model):
    """ 指标表 """
    target = models.CharField(max_length=32, verbose_name='指标')

    def __str__(self):
        return self.target


class Algorithm(models.Model):
    """ 指标表 """
    algorithm = models.CharField(max_length=32, verbose_name='算法')

    def __str__(self):
        return self.algorithm


class Simulation(models.Model):
    """政策模拟表"""
    target = models.ForeignKey(to='Target', to_field='id', on_delete=models.CASCADE)
    algorithm = models.ForeignKey(to='Algorithm', to_field='id', on_delete=models.CASCADE)
    data = models.IntegerField(verbose_name='数据')
    outcome = models.IntegerField(verbose_name='模拟结果', null=True, blank=True)


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0, null=True, blank=True)

    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    status_choices = (
        (1, "占用"),
        (2, "未占用")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)
