from django.shortcuts import render
from .models import Blog

# Create your views here.


def all_blog(request):
    """ A view to show all blog us submissions """

    blog = Blog.objects.all()

    context = {
        'blog' : blog,
    }
    
    return render(request, 'blog/blog.html', context)