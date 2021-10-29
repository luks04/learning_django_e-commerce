from django.shortcuts import render
from .models import Resume, Post
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, 'resume/home.html')

def about(request):
    resume = Resume.objects.get(pk = 1)
    return render(request, 'resume/about.html', {'resume': resume})

def blog(request):
    posts_objects = Post.objects.all().order_by('-date')
    item_name = request.GET.get('item_name') # <input name="item_name" />

    if item_name != "" and item_name is not None:
        posts_objects = posts_objects.filter(title__icontains = item_name)
    return render(request, 'resume/blog.html', {'posts_objects': posts_objects})

'''
class PostListView(ListView):
    model = Post
    template_name = 'resume/blog.html' # 'template_name' -> kew word
    context_object_name = 'posts_objects' # 'context_object_name' -> kew word
    ordering = ['-date']
'''
