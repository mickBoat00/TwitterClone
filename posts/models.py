from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    retweets = models.IntegerField(default=0)
    quote_tweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads', null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

    def __str__(self):
        return self.content

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.content} - {self.user}'

class Retweet(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.content} - {self.user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.content} - {self.user} - {self.comment}'




