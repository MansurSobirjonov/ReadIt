from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=222)
    email = models.EmailField()
    subject = models.CharField(max_length=222)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

