from django.shortcuts import render, redirect
from blog.models import *

# można dodać kilka postów w manage.py shell, by widzieć wyniki
# from blog.models import *
# Post.objects.create(title='Mój pierwszy post', content='To mój pierwszy post!')
# Post.objects.create(title='Mój drugi post', content='To mój drugi post!')


def all_posts(request):
    posts = Post.objects.all().order_by("-publish_date")
    return render(request, "blog/all_posts.html", context={"posts": posts})


def add_post(request):
    error_message = ""
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if not title or not content:
            error_message = "Title and content is required"
        else:
            post = Post.objects.create(title=title, content=content)
            return redirect("/")
    return render(request, "blog/add_post.html", context={"error_message": error_message})


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "blog/post_details.html", context={"post": post})


def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    error_message = ""
    if request.method == "POST":
        author = request.POST.get("author")
        content = request.POST.get("content")
        if not author or not content:
            error_message = "Author and content are required"
        else:
            comment = Comment.objects.create(author=author, content=content, post=post)
            return redirect(f"/post_details/{post_id}")
    return render(request, "blog/add_comment.html", context={"error_message": error_message})
