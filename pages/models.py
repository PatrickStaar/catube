# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Id(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    pwd = models.CharField(max_length=100)
    avatar = models.FileField(default=None, upload_to='avatars')


class Item(models.Model):
    number = models.AutoField(primary_key=True)
    type = models.CharField(default='vid', max_length=4)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    tag = models.CharField(max_length=20, default='fun')

    played = models.IntegerField(default=0)
    liked = models.IntegerField(default=0)

    file = models.FileField(upload_to='upload')
    time = models.DateTimeField(auto_now=True)  # ??????
    owner = models.ForeignKey(Id, on_delete=models.CASCADE)

    def _unicode_(self):
        return self.name


class Behavior(models.Model):
    type = models.CharField(default='l', max_length=10)
    # Django 2 需要设置外键在删除时的方式
    performer = models.ForeignKey(Id, on_delete=models.CASCADE)
    aim = models.ForeignKey(Item, on_delete=models.CASCADE)
