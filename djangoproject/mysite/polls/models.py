from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class Question(models.Model):
    # 创建问题字段为字符串格式
    question_text = models.CharField(max_length=200)
    # 创建提交时间为datetime格式
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 最近发表过
    def was_published_recently(self):
        # datetime.timedelta(days=10) 设置天数
        # pub_date的格式为datetime.datetime(2017, 8, 31, 11, 22, 20, 769868)
        # 先计算时间，后判断大小
        # 数据库记录的时间 >= 现在的时间-减去一天
        # 可以查出最近两天的记录
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 创建问题的外键和问题表相关联
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 创建int字段，默认为0
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text