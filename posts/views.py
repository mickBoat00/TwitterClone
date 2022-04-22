from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import PostForm, CommentForm
from .models import Post, Like, Retweet, Comment

from django.conf import settings
User = settings.AUTH_USER_MODEL

User = get_user_model()


@login_required
def timeline(request):
    posts = Post.objects.all().order_by('-timestamp')

    context = {
        'posts': posts,
        'form': PostForm()
    }

    return render(request, 'posts/timeline.html', context)


@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment = Comment.objects.filter(post=post)
    form = CommentForm()

    context = {
        'post':post,
        'form': form,
        'comments': comment
    }

    return render(request, 'posts/detail.html', context)



@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponse('you cant update this post')

    form = PostForm(request.POST or None, instance=post)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponse('you can"t delete this post')

    if request.method == 'POST':
        post.delete()
        return redirect('/')

    context = {
        'object': post
    }
    return render(request, 'delete.html', context)


def post_likes_list(request, id):

    post_like_list = None

    if id is not None:
        post_liked = Post.objects.get(id=id)
        post_like_list = post_liked.like_set.all()

    content = {
        'likes_list': post_like_list
    }


    return render(request, 'posts/like-list.html', content)


def like_post(request, id):

    post_liked = Post.objects.get(id=id)

    query = None

    try:
        query = Like.objects.get(post=post_liked, user=request.user)
    except :
        pass

    if query:
        query.delete()
    else:
        Like.objects.create(post=post_liked, user=request.user)

    return redirect('/')    


def post_retweet_list(request, id):
    post_retweet_list = None

    if id is not None:
        post_retweeted = Post.objects.get(id=id)
        post_retweet_list = post_retweeted.retweet_set.all()

    content = {
        'likes_list': post_retweet_list,
        'type': 'Retweets'
    }


    return render(request, 'posts/like-list.html', content)

def retweet_post(request, id):

    post_retweeted = Post.objects.get(id=id)

    query = None

    try:
        query = Retweet.objects.get(post=post_retweeted, user=request.user)
    except :
        pass

    if query:
        query.delete()
    else:
        Retweet.objects.create(post=post_retweeted, user=request.user)
    
    # Retweet.objects.create(post=post_retweeted, user=request.user)

    return redirect('/') 

@login_required
def post_create(request):

    form = PostForm(request.POST)

    if form.is_valid():
        post_object = form.save(commit=False)
        post_object.author = request.user
        post_object.save()
        return redirect('/')

@login_required 
def post_comment(request, id):
    post = get_object_or_404(Post, id=id)

    form = CommentForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.user = request.user
            obj.save()
            
            form = CommentForm()

    return redirect(f"/status/{id}/") #change this later to use  name
