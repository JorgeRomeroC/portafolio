from django.shortcuts import render, get_object_or_404

from blog.models import Post


def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, post_id):
    get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post_id})