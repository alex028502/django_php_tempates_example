from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    message = models.TextField(blank=False, default='')
