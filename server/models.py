from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    author = models.CharField(max_length=123)
    created_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    likes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title
