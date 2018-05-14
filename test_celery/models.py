from django.db import models

class Plus(models.Model):
    task_id = models.CharField(max_length=128)
    first = models.IntegerField()
    second = models.IntegerField()
    log_date = models.DateTimeField()

class Multi(models.Model):
    task_id = models.CharField(max_length=128)
    multiplier = models.IntegerField()
    multiplicand = models.IntegerField()
    log_date = models.DateTimeField()
