from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    comment = models.TextField(blank=False, default='')
