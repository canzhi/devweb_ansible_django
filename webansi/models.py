from django.db import models


# Create your models here.

class HostGroup(models.Model):
    group_name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return '组：%s' % self.group_name


class Host(models.Model):
    hostname = models.CharField(max_length=50, null=False, unique=True)
    ipaddr = models.CharField(max_length=15, null=False, unique=True)
    group = models.ForeignKey(HostGroup)

    def __str__(self):
        return '%s:%s=>%s' % (self.hostname, self.ipaddr, self.group)


class Module(models.Model):
    module_name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return '模块:%s' % self.module_name


class Argument(models.Model):
    arg_text = models.CharField(max_length=100, null=False, unique=True)
    module = models.ForeignKey(Module)

    def __str__(self):
        return '%s=>%s' % (self.module, self.arg_text)
