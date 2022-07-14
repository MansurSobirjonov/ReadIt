from django.contrib.auth.models import User
from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category (models.Model):
    category = models.CharField(max_length=222)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tags = models.CharField(max_length=222)

    def __str__(self):
        return self.tags


class Post(Timestamp):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='Articlaes/')
    content = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author_name = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='author', null=True)
    author_commit = models.TextField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=222)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='comment/', null=True)
    website = models.CharField(max_length=222, null=True)
    massage = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
