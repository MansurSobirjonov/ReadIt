from django.db import models


class Employer(models.Model):
    describtion = models.TextField()
    name = models.CharField(max_length=222)
    avatar = models.ImageField(upload_to='Team/')
    position = models.CharField(max_length=222)

    def __str__(self):
        return self.name
