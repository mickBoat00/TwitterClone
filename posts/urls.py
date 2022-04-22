from django.urls import path

from .views import *

app_name = 'post'

urlpatterns = [
    path('', timeline, name='timeline'),
    path('compose/tweet/', post_create, name='create'),
    path('status/<int:id>/', post_detail, name='detail'),
    path('status/<int:id>/update', post_update, name='update'),
    path('status/<int:id>/delete', post_delete, name='delete'),
    path('status/<int:id>/like', like_post, name='like-post'),
    path('status/<int:id>/retweet', retweet_post, name='retweet-post'),
    path('status/<int:id>/likes', post_likes_list, name='like-list'),
    path('status/<int:id>/retweets', post_retweet_list, name='retweet-list'),

    
    path('status/<int:id>/comment', post_comment, name='post-comment')
]
