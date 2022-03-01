from django.db import models


# Create your models here.
class Library(models.Model):
    normalStartTime = models.IntegerField(verbose_name="오픈시간", null=True)
    normalEndTime = models.IntegerField(verbose_name="마감시간", null=True)
    closedNotice = models.TextField(verbose_name="마감후공지", null=True)
    normalNotice = models.TextField(verbose_name="공지", null=True)


class ShuttleA(models.Model):
    departureTime = models.TimeField(verbose_name="a노선 출발시간", null=True)


class ShuttleB(models.Model):
    departureTime = models.TimeField(verbose_name="b노선 출발시간", null=True)