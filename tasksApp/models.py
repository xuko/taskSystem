from django.db import models


class Check(models.Model):
    text = models.CharField(max_length=200)
    value = models.BooleanField()
