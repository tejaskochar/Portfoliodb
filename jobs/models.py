from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length = 300)
    urls = models.URLField(max_length=200, blank=True)
