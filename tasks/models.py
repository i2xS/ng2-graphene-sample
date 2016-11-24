from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=32)


class Sprint(models.Model):
    name = models.CharField(max_length=32)
    status = models.CharField(max_length=32)



class Task(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(default=u'')
    status = models.CharField(max_length=32)

