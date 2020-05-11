from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 50)
    image = models.ImageField(upload_to= 'blogpost/')
    summary = models.CharField(max_length= 300)

    def __str__(self):
        return self.title

    def restrict(self):
        return self.summary[:200]
