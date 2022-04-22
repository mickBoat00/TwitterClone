from django.contrib import admin
from .models import Post, Comment, Like, Retweet

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Retweet)