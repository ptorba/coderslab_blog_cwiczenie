from enum import auto
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class Comment(models.Model):
    author = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
