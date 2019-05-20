"""Blog view render methods"""
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
  """Method to render all blogs on Blog page"""
  blogs = Blog.objects
  return render(request, 'blog/allBlogs.html', {
    'blogs': blogs
  })

def detail(request, blog_id):
  """Method to render a single clicked blog"""
  detail_blog = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'blog/detail.html', {
    'blog': detail_blog
  })
