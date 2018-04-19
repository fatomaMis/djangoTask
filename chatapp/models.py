from django.db import models


class Message(models.Model):
    msg = models.CharField(max_length = 500)
    date = models.DateTimeField('reg_date')

