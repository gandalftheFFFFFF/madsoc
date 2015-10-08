from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    text = models.TextField()