from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView

def post_views(request, post_id=None):
    context = {}

    if post_id is not None:
        # Если post_id предоставлен, то получаем только один пост по его идентификатору
        context["post"] = Post.objects.get(pk=post_id)
    else:
        # В противном случае получаем все посты
        context["all_posts"] = Post.objects.all()

    return render(request, "all_posts_func.html", context)


class PostListView(ListView):
    model = Post
    template_name = "all_posts_class.html"
