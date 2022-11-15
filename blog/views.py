from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Blog
from .forms import BlogForm

# Create your views here.


def all_blog(request):
    """ A view to show all blog us submissions """

    blog = Blog.objects.all()

    context = {
        'blog' : blog,
    }
    
    return render(request, 'blog/blog.html', context)


def blog_post(request, blog_id):
    """ A view to show individual post """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog' : blog,
    }
    
    return render(request, 'blog/blog_post.html', context)


def add_post(request):
    """ Add a post to blog  """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:    
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_blog(request, blog_id):
    """ Edit a post in the blog """
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Post!')
            return redirect(reverse('blog_post', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update Post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.name}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


def delete_blog(request, blog_id):
    """ Delete a post from the blog """
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Post Deleted!')
    return redirect(reverse('blogs'))
